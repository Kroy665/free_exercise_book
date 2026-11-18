// Unit tests for the graph expression parser and figure specs. Run: npm run test:figures
import { compile, num } from "../src/lib/markdown/expr.ts";
import { renderChart, renderPlot } from "../src/lib/markdown/figures.ts";

let bad = 0;
const fail = (msg: string) => { bad++; console.log("FAIL", msg); };

const cases: [string, string[], number[], number][] = [
  ["2x^2 - 3", ["x"], [2], 5], ["-x^2", ["x"], [3], -9], ["2^3^2", [], [], 512],
  ["sin^2(x) + cos^2(x)", ["x"], [0.7], 1], ["2sqrt(2)(x - sqrt(2))", ["x"], [2], 2 * Math.SQRT2 * (2 - Math.SQRT2)],
  ["(x+1)(x-1)", ["x"], [3], 8], ["|x - 5|", ["x"], [2], 3], ["xy + 2pi", ["x", "y"], [2, 3], 6 + 2 * Math.PI],
  ["e^(-x/2)", ["x"], [2], Math.exp(-1)], ["log(e)", [], [], 1], ["1/x", ["x"], [4], 0.25], ["3 − 1", [], [], 2],
  ["2π", [], [], 2 * Math.PI], ["log10(1000)", [], [], 3], ["max(x, 2)", ["x"], [5], 5],
];
for (const [src, vars, args, want] of cases) {
  const got = compile(src, vars)(...args);
  if (Math.abs(got - want) > 1e-9) fail(`${src} = ${got}, expected ${want}`);
}
for (const src of ["2x +", "foo(x)", "(x", "sin()", "x $ 2"]) {
  try { compile(src, ["x"]); fail(`"${src}" should be rejected`); } catch { /* expected */ }
}
if (num("-2pi") !== -2 * Math.PI) fail("num(-2pi)");

const ok = (name: string, f: () => unknown) => { try { f(); } catch (e) { fail(`${name}: ${(e as Error).message}`); } };
const rejects = (name: string, f: () => unknown) => { try { f(); fail(`${name} should be rejected`); } catch { /* expected */ } };
ok("plot f", () => renderPlot("x: -3, 3\nf: x^2 | parabola"));
ok("plot implicit", () => renderPlot("equal: true\nx: -3, 3\nimplicit: x^2 + y^2 = 4"));
ok("plot polar", () => renderPlot("polar: 1 + cos(t)"));
ok("plot param", () => renderPlot("param: cos(t), sin(t)\nequal: true"));
ok("chart bar", () => renderChart("type: bar\nlabels: a, b\ndata: 1, 2 | s1\ndata: 3, 4 | s2"));
ok("chart histogram", () => renderChart("type: histogram\nlabels: 0, 10, 20\ndata: 3, 5"));
ok("chart pie", () => renderChart("type: pie\nlabels: a, b\ndata: 1, 3"));
ok("chart scatter", () => renderChart("type: scatter\npoints: 1, 2; 2, 3\nfit: x + 1"));
rejects("unknown key", () => renderPlot("f: x\ncolour: red"));
rejects("bad range", () => renderPlot("x: 3, -3\nf: x"));
rejects("histogram length", () => renderChart("type: histogram\nlabels: 0, 10, 20\ndata: 1, 2, 3"));
rejects("bad type", () => renderChart("type: donut\ndata: 1"));
const legend = renderPlot("f: x | $y=x$").legend;
if (legend.length !== 1 || legend[0].label !== "$y=x$") fail("legend label");

console.log(bad ? `${bad} failure(s)` : "figures: all tests passed");
process.exit(bad ? 1 : 0);
