import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from qlib import Topic, eq

T = Topic("math.algebra.inequalities")

# ---------------------------------------------------------------- single (21)
# q1
T.single(1, ["extrema", "am-gm-hm"], r"For $x > 0$, the least value of $x + \dfrac{1}{x}$ is",
         [r"$2$", r"$1$", r"$2\sqrt2$", r"$0$"],
         r"""By AM ≥ GM on the positive numbers $x$ and $\frac1x$:
$$x + \frac1x \ge 2\sqrt{x\cdot\frac1x} = 2,$$
with equality iff $x = \frac1x$, that is, $x = 1$. So the least value is $2$.

The value $1$ is $\sqrt{x\cdot\frac1x}$, the GM itself; the sum is twice the GM.""")

# q2
T.single(1, ["extrema"], r"If $x, y > 0$ and $x + y = 10$, the greatest value of $xy$ is",
         [r"$25$", r"$50$", r"$100$", r"$20$"],
         r"""With the sum fixed, the product is greatest when the numbers are equal:
$$\sqrt{xy} \le \frac{x + y}{2} = 5 \implies xy \le 25,$$
attained at $x = y = 5$.

$100 = (x + y)^2$ forgets to divide by $4$.""")

# q3
T.single(1, ["am-gm-hm", "exam-tips"],
         r"The arithmetic mean of two positive numbers is $\dfrac{13}{2}$ and their geometric mean is $6$. Their harmonic mean is",
         [r"$\dfrac{72}{13}$", r"$\dfrac{11}{2}$", r"$\dfrac{13}{72}$", r"$\dfrac{78}{13}$"],
         r"""For two positive numbers $G^2 = AH$, so
$$H = \frac{G^2}{A} = \frac{36}{13/2} = \frac{72}{13}.$$
(The numbers are $4$ and $9$: $H = \frac{2\cdot 36}{13}$.)

Check: $H = \frac{72}{13} \approx 5.54 < G = 6$, as it must be. $\frac{11}{2}$ comes from guessing an arithmetic pattern $A, G, H$.""")

# q4
T.single(1, ["standard-bounds"],
         r"For positive reals $a, b, c$, the least value of $(a + b + c)\left(\dfrac1a + \dfrac1b + \dfrac1c\right)$ is",
         [r"$9$", r"$3$", r"$6$", r"$27$"],
         r"""By $A \ge H$ for $a, b, c$:
$$\frac{a + b + c}{3} \ge \frac{3}{\frac1a + \frac1b + \frac1c} \implies (a + b + c)\Big(\frac1a + \frac1b + \frac1c\Big) \ge 9,$$
with equality at $a = b = c$ (put $a = b = c = 1$: $3 \cdot 3 = 9$).

In general the bound is $n^2$, not $n$ or $n^3$.""")

# q5
T.single(1, ["am-gm-hm"],
         r"For positive reals $a_1, \dots, a_n$, equality holds in $\dfrac{a_1 + \cdots + a_n}{n} \ge (a_1 a_2 \cdots a_n)^{1/n}$ if and only if",
         [r"$a_1 = a_2 = \cdots = a_n$", r"$a_1 a_2 \cdots a_n = 1$", r"$a_1 + a_2 + \cdots + a_n = n$", r"$n = 2$"],
         r"""AM = GM exactly when all the numbers are equal. If two of them differ, replacing both by their mean keeps the sum and strictly increases the product, so AM > GM.

A product equal to $1$ does not force equality: for $2$ and $\frac12$, the AM is $\frac54$ but the GM is $1$.""")

# q6
T.single(2, ["extrema"], r"For $x > 0$, the least value of $4x + \dfrac{9}{x}$ is",
         [r"$12$", r"$13$", r"$6$", r"$36$"],
         r"""$$4x + \frac9x \ge 2\sqrt{4x\cdot\frac9x} = 2\sqrt{36} = 12,$$
with equality when $4x = \frac9x$, i.e. $x = \frac32$.

$13$ is the value at $x = 1$, which is not the minimiser; $6 = \sqrt{36}$ forgets the factor $2$.""")

# q7
T.single(2, ["weighted"], r"If $x, y > 0$ and $x + y = 3$, the greatest value of $x^2 y$ is",
         [r"$4$", r"$\dfrac{27}{8}$", r"$1$", r"$\dfrac{9}{4}$"],
         r"""Split $x$ into two equal parts, so that the sum stays fixed: $\frac x2 + \frac x2 + y = 3$. By AM ≥ GM,
$$\frac x2\cdot\frac x2\cdot y \le \Big(\frac{3}{3}\Big)^3 = 1 \implies x^2 y \le 4,$$
with equality at $\frac x2 = y = 1$, i.e. $x = 2,\ y = 1$.

Check by calculus: $f(x) = x^2(3 - x)$, $f'(x) = 6x - 3x^2 = 0 \Rightarrow x = 2$, $f(2) = 4$. $\frac{27}{8}$ is the value at $x = y = \frac32$, which is not the maximum.""")

# q8
T.single(2, ["extrema"], r"If $x, y > 0$ and $xy = 6$, the least value of $2x + 3y$ is",
         [r"$12$", r"$6$", r"$2\sqrt6$", r"$24$"],
         r"""$$2x + 3y \ge 2\sqrt{2x\cdot 3y} = 2\sqrt{6\cdot 6} = 12,$$
with equality when $2x = 3y$; with $xy = 6$ this gives $x = 3,\ y = 2$.

$2\sqrt6$ is the bound for $x + y$, ignoring the coefficients.""")

# q9
T.single(1, ["cauchy-schwarz"], r"If $x^2 + y^2 = 1$, the greatest value of $3x + 4y$ is",
         [r"$5$", r"$7$", r"$1$", r"$\sqrt7$"],
         r"""By Cauchy–Schwarz,
$$(3x + 4y)^2 \le (3^2 + 4^2)(x^2 + y^2) = 25,$$
so $3x + 4y \le 5$, with equality at $(x, y) = \big(\frac35, \frac45\big)$.

$7 = 3 + 4$ would need $x = y = 1$, which is not on the circle.""")

# q10
T.single(2, ["cauchy-schwarz"], r"If $x + 2y + 2z = 9$, the least value of $x^2 + y^2 + z^2$ is",
         [r"$9$", r"$3$", r"$81$", r"$27$"],
         r"""By Cauchy–Schwarz,
$$81 = (x + 2y + 2z)^2 \le (1 + 4 + 4)(x^2 + y^2 + z^2),$$
so $x^2 + y^2 + z^2 \ge 9$. Equality holds when $(x, y, z) \propto (1, 2, 2)$, i.e. at $(1, 2, 2)$.

$3$ is the least **distance** $\frac{9}{\sqrt9}$, not its square.""")

# q11
T.single(2, ["cauchy-schwarz"], r"If $x, y > 0$ and $x + y = 1$, the least value of $\dfrac1x + \dfrac4y$ is",
         [r"$9$", r"$8$", r"$5$", r"$10$"],
         r"""By Engel's form of Cauchy–Schwarz,
$$\frac{1^2}{x} + \frac{2^2}{y} \ge \frac{(1 + 2)^2}{x + y} = 9,$$
with equality when $\frac1x = \frac2y$, i.e. $x = \frac13,\ y = \frac23$.

$8$ comes from $\frac1x + \frac4y \ge \frac{4}{\sqrt{xy}} \ge 8$ using $xy \le \frac14$; but the two equality cases ($y = 4x$ and $x = y$) cannot hold together, so $8$ is never attained. $10$ is the value at $x = y = \frac12$.""")

# q12
T.single(2, ["standard-bounds"], r"For every integer $n \ge 2$,",
         [r"$n! < \left(\dfrac{n + 1}{2}\right)^n$", r"$n! > \left(\dfrac{n + 1}{2}\right)^n$",
          r"$n! < \left(\dfrac{n}{2}\right)^n$", r"$n! < \left(\dfrac{n - 1}{2}\right)^n$"],
         r"""Apply AM ≥ GM to $1, 2, \dots, n$:
$$\sqrt[n]{n!} \le \frac{1 + 2 + \cdots + n}{n} = \frac{n + 1}{2},$$
and the inequality is strict since the numbers are not all equal. So $n! < \left(\frac{n + 1}{2}\right)^n$.

$n! < \left(\frac n2\right)^n$ fails at $n = 2$: $2 > 1$.""")

# q13
T.single(3, ["weighted"], r"If $x, y > 0$ and $x + y = 5$, the greatest value of $x^3 y^2$ is",
         [r"$108$", r"$\dfrac{3125}{32}$", r"$72$", r"$144$"],
         r"""Split into $\frac x3, \frac x3, \frac x3, \frac y2, \frac y2$; their sum is $x + y = 5$. By AM ≥ GM,
$$\Big(\frac x3\Big)^3\Big(\frac y2\Big)^2 \le \Big(\frac55\Big)^5 = 1 \implies x^3 y^2 \le 27\cdot 4 = 108.$$
Equality holds at $\frac x3 = \frac y2 = 1$, i.e. $x = 3,\ y = 2$ (in general $x : y = 3 : 2$).

$\frac{3125}{32}$ is the value at $x = y = \frac52$, which is smaller.""")

# q14
T.single(1, ["extrema"], r"If $a, b, c > 0$ and $a + b + c = 1$, the greatest value of $abc$ is",
         [r"$\dfrac{1}{27}$", r"$\dfrac19$", r"$\dfrac13$", r"$\dfrac18$"],
         r"""$$\sqrt[3]{abc} \le \frac{a + b + c}{3} = \frac13 \implies abc \le \frac{1}{27},$$
with equality at $a = b = c = \frac13$.

$\frac19$ forgets to cube; $\frac18$ uses the two-variable bound $\frac{s^2}{4}$ wrongly.""")

# q15
T.single(2, ["basics", "extrema"], r"If $a, b, c$ are real and $a + b + c = 6$, the greatest value of $ab + bc + ca$ is",
         [r"$12$", r"$36$", r"$9$", r"$18$"],
         r"""From $a^2 + b^2 + c^2 \ge ab + bc + ca$:
$$36 = (a + b + c)^2 = a^2 + b^2 + c^2 + 2(ab + bc + ca) \ge 3(ab + bc + ca),$$
so $ab + bc + ca \le 12$, with equality at $a = b = c = 2$.

$18 = \frac{36}{2}$ forgets that $a^2 + b^2 + c^2$ is at least $ab + bc + ca$, not zero.""")

# q16
T.single(3, ["power-means"], r"If $a, b > 0$ and $a + b = 2$, the least value of $a^4 + b^4$ is",
         [r"$2$", r"$1$", r"$8$", r"$16$"],
         r"""By the $m$th power theorem with $m = 4 > 1$:
$$\frac{a^4 + b^4}{2} \ge \Big(\frac{a + b}{2}\Big)^4 = 1 \implies a^4 + b^4 \ge 2,$$
with equality at $a = b = 1$.

$8 = \frac{(a + b)^4}{2}$ divides by $2$ instead of $2^4/2$; $1$ forgets to multiply by $2$.""")

# q17
T.single(3, ["extrema"],
         r"If $x, y > 0$ and $x + y = 1$, the least value of $\left(x + \dfrac1x\right)^2 + \left(y + \dfrac1y\right)^2$ is",
         [r"$\dfrac{25}{2}$", r"$8$", r"$\dfrac{25}{4}$", r"$9$"],
         r"""By the power mean inequality $u^2 + v^2 \ge \frac{(u + v)^2}{2}$:
$$\text{expression} \ge \frac12\Big(1 + \frac1x + \frac1y\Big)^2.$$
Also $\frac1x + \frac1y \ge \frac{4}{x + y} = 4$. Hence the expression is $\ge \frac12\cdot 5^2 = \frac{25}{2}$, with equality at $x = y = \frac12$ (each bracket is $\frac52$).

$8$ comes from $x + \frac1x \ge 2$ for each term, but that needs $x = y = 1$, which violates $x + y = 1$.""")

# q18
T.single(2, ["am-gm-hm"], r"If $a, b, c > 0$ and $abc = 1$, the least value of $(1 + a)(1 + b)(1 + c)$ is",
         [r"$8$", r"$1$", r"$2$", r"$27$"],
         r"""Each factor satisfies $1 + a \ge 2\sqrt a$. Multiplying,
$$(1 + a)(1 + b)(1 + c) \ge 8\sqrt{abc} = 8,$$
with equality at $a = b = c = 1$.

$27$ would be $3^3$, from wrongly taking each factor $\ge 3$.""")

# q19
T.single(3, ["extrema"], r"If $x, y, z > 0$ and $xy + yz + zx = 12$, the greatest value of $xyz$ is",
         [r"$8$", r"$64$", r"$4$", r"$16$"],
         r"""AM ≥ GM on $xy, yz, zx$:
$$\sqrt[3]{(xyz)^2} \le \frac{xy + yz + zx}{3} = 4 \implies (xyz)^2 \le 64 \implies xyz \le 8,$$
with equality at $x = y = z = 2$.

$64$ is $(xyz)^2$: forgetting the last square root.""")

# q20
T.single(3, ["basics", "exam-tips"], r"If $a, b, c$ are real and $a^2 + b^2 + c^2 = 1$, then $ab + bc + ca$ lies in",
         [r"$\left[-\dfrac12, 1\right]$", r"$[-1, 1]$", r"$[0, 1]$", r"$\left[-\dfrac12, \dfrac12\right]$"],
         r"""Upper bound: $ab + bc + ca \le a^2 + b^2 + c^2 = 1$, attained at $a = b = c = \frac{1}{\sqrt3}$.

Lower bound: $0 \le (a + b + c)^2 = 1 + 2(ab + bc + ca)$, so $ab + bc + ca \ge -\frac12$. It is attained when $a + b + c = 0$, e.g. $(a, b, c) = \big(\frac{1}{\sqrt2}, -\frac{1}{\sqrt2}, 0\big)$.

$[0, 1]$ forgets that the variables may be negative.""")

# q21
T.single(2, ["power-means"],
         r"Let $a_1, \dots, a_n$ be positive and not all equal, and let $0 < m < 1$. Then $\dfrac{a_1^m + \cdots + a_n^m}{n}$ is",
         [r"less than $\left(\dfrac{a_1 + \cdots + a_n}{n}\right)^m$", r"greater than $\left(\dfrac{a_1 + \cdots + a_n}{n}\right)^m$",
          r"equal to $\left(\dfrac{a_1 + \cdots + a_n}{n}\right)^m$", r"greater or less, depending on the $a_i$"],
         r"""$t \mapsto t^m$ is concave on $(0, \infty)$ for $0 < m < 1$, so by Jensen's inequality the mean of the powers is **less** than the power of the mean. (For $m > 1$ or $m < 0$ it is greater.)

Quick check with $a = 1$, $b = 9$, $m = \frac12$: $\frac{1 + 3}{2} = 2 < \sqrt5$.""")

# ------------------------------------------------------------ statements (2)
T.statements(2, ["basics", "am-gm-hm", "standard-bounds"],
             r"Consider the following statements for all positive reals $a, b, c$:",
             [r"$a^2 + b^2 + c^2 \ge ab + bc + ca$",
              r"$(a + b)(b + c)(c + a) \ge 8abc$",
              r"$(a + b + c)^3 \ge 81abc$"],
             [r"1 and 2 only", r"1 only", r"2 and 3 only", r"1, 2 and 3"],
             r"""1. True: the difference is $\frac12\left[(a - b)^2 + (b - c)^2 + (c - a)^2\right] \ge 0$.
2. True: $a + b \ge 2\sqrt{ab}$, and similarly for the other two factors; multiply them.
3. False: AM ≥ GM gives $(a + b + c)^3 \ge 27abc$. At $a = b = c = 1$ the claim reads $27 \ge 81$.

Testing at $a = b = c$ kills a wrong constant at once.""")

T.statements(3, ["cauchy-schwarz", "am-gm-hm"],
             r"Consider the following statements:",
             [r"For all real $a_1, \dots, a_n, b_1, \dots, b_n$: $\left(\sum a_i b_i\right)^2 \le \left(\sum a_i^2\right)\left(\sum b_i^2\right)$, with equality iff one tuple is a scalar multiple of the other.",
              r"For all real $x_1, \dots, x_n$ and all non-zero real $y_1, \dots, y_n$ with $\sum y_i \ne 0$: $\sum \dfrac{x_i^2}{y_i} \ge \dfrac{\left(\sum x_i\right)^2}{\sum y_i}$.",
              r"For all non-zero reals $a, b$ with $ab > 0$: $\dfrac{a + b}{2} \ge \sqrt{ab}$."],
             [r"1 only", r"1 and 2 only", r"1 and 3 only", r"1, 2 and 3"],
             r"""1. True: this is Cauchy–Schwarz, and it needs no sign condition. Equality holds iff the tuples are proportional.
2. False: Engel's form needs $y_i > 0$. With $x = (1, 1)$ and $y = \big(1, -\frac12\big)$: the left side is $1 - 2 = -1$, the right side is $\frac{4}{1/2} = 8$.
3. False: $ab > 0$ allows both negative. For $a = -1$, $b = -4$: $\frac{a + b}{2} = -\frac52 < 2 = \sqrt{ab}$.

So only statement 1 is correct.""")

# ----------------------------------------------------------------- match (2)
T.match(2, ["extrema"], r"For $x > 0$, match each expression in List I with its least value in List II.",
        [r"$x + \dfrac1x$", r"$x + \dfrac4x$", r"$x^2 + \dfrac2x$", r"$x + \dfrac{1}{4x}$"],
        [r"$3$", r"$4$", r"$1$", r"$2$"],
        [r"A-4, B-2, C-1, D-3", r"A-4, B-1, C-2, D-3", r"A-2, B-4, C-1, D-3", r"A-4, B-2, C-3, D-1"],
        r"""- A: $x + \frac1x \ge 2$ (at $x = 1$).
- B: $x + \frac4x \ge 2\sqrt4 = 4$ (at $x = 2$).
- C: $x^2 + \frac1x + \frac1x \ge 3\sqrt[3]{x^2\cdot\frac1x\cdot\frac1x} = 3$ (at $x = 1$).
- D: $x + \frac{1}{4x} \ge 2\sqrt{\frac14} = 1$ (at $x = \frac12$).

So A-4, B-2, C-1, D-3.""")

T.match(2, ["am-gm-hm", "power-means"], r"Match each mean of the numbers $2$ and $8$ in List I with its value in List II.",
        [r"arithmetic mean", r"geometric mean", r"harmonic mean", r"root mean square $\sqrt{\dfrac{a^2 + b^2}{2}}$"],
        [r"$\sqrt{34}$", r"$\dfrac{16}{5}$", r"$5$", r"$4$"],
        [r"A-3, B-4, C-2, D-1", r"A-3, B-2, C-4, D-1", r"A-1, B-4, C-2, D-3", r"A-4, B-3, C-2, D-1"],
        r"""- AM $= \frac{2 + 8}{2} = 5$.
- GM $= \sqrt{16} = 4$.
- HM $= \frac{2\cdot 2\cdot 8}{2 + 8} = \frac{16}{5}$ (check: $G^2 = AH = 5\cdot\frac{16}{5} = 16$).
- RMS $= \sqrt{\frac{4 + 64}{2}} = \sqrt{34} \approx 5.83$.

The order $H < G < A < M_2$ is the power mean chain. So A-3, B-4, C-2, D-1.""")

# ------------------------------------------------------- assertion-reason (5)
T.assertion_reason(1, ["extrema", "am-gm-hm"],
                   r"For every $x > 0$, $x + \dfrac1x \ge 2$.",
                   r"For positive reals $a$ and $b$, $\dfrac{a + b}{2} \ge \sqrt{ab}$.",
                   0,
                   r"""Both are true. Taking $a = x$ and $b = \frac1x$ in R gives $\frac{x + 1/x}{2} \ge 1$, which is A. So R explains A.""")

T.assertion_reason(2, ["am-gm-hm", "exam-tips"],
                   r"For every $x < 0$, $x + \dfrac1x \le -2$.",
                   r"The inequality $\dfrac{a + b}{2} \ge \sqrt{ab}$ holds for all non-zero reals $a, b$ with $ab > 0$.",
                   2,
                   r"""A is true: put $t = -x > 0$; then $t + \frac1t \ge 2$, so $x + \frac1x = -\big(t + \frac1t\big) \le -2$.

R is false: for $a = b = -1$, $\frac{a + b}{2} = -1 < 1 = \sqrt{ab}$. AM ≥ GM needs non-negative numbers.""")

T.assertion_reason(2, ["standard-bounds", "basics"],
                   r"If $a, b, c > 0$ and $a + b + c = 1$, then $\left(\dfrac1a - 1\right)\left(\dfrac1b - 1\right)\left(\dfrac1c - 1\right) \ge 8$.",
                   r"For all real $a, b, c$, $a^2 + b^2 + c^2 \ge ab + bc + ca$.",
                   1,
                   r"""A is true: $\frac1a - 1 = \frac{b + c}{a}$, so the product is $\frac{(b + c)(c + a)(a + b)}{abc} \ge \frac{2\sqrt{bc}\cdot 2\sqrt{ca}\cdot 2\sqrt{ab}}{abc} = 8$.

R is true (a sum of squares), but A is proved by AM ≥ GM on each pair, not by R. So R does not explain A.""")

T.assertion_reason(3, ["standard-bounds", "exam-tips"],
                   r"For every positive integer $n$, $n! < \left(\dfrac{n + 1}{2}\right)^n$.",
                   r"The geometric mean of $1, 2, \dots, n$ does not exceed their arithmetic mean $\dfrac{n + 1}{2}$.",
                   3,
                   r"""R is true (AM ≥ GM), and it gives $n! \le \left(\frac{n + 1}{2}\right)^n$, strictly only when the numbers are not all equal, i.e. $n \ge 2$.

A is false because of $n = 1$: both sides equal $1$. The strict inequality holds only for $n \ge 2$.""")

T.assertion_reason(3, ["standard-bounds"],
                   r"If $n \ge 2$ and $0 < a_i < 1$ for $i = 1, \dots, n$, then $(1 - a_1)(1 - a_2)\cdots(1 - a_n) > 1 - (a_1 + a_2 + \cdots + a_n)$.",
                   r"If $0 < a, b < 1$, then $(1 - a)(1 - b) > 1 - a - b$; and if $P > 1 - s$ with $0 < c < 1$, then $P(1 - c) > (1 - s)(1 - c) > 1 - s - c$.",
                   0,
                   r"""Both are true. R gives the case $n = 2$, since $(1 - a)(1 - b) = 1 - a - b + ab$ and $ab > 0$. Its second part is the induction step: multiplying by $1 - c > 0$ keeps the inequality, and $(1 - s)(1 - c) = 1 - s - c + sc > 1 - s - c$ since $s, c > 0$.

So R proves A (Weierstrass's inequality) by induction: R explains A.""")


def check():
    import random
    import sympy as sp
    x, y, z, t = sp.symbols("x y z t", positive=True)
    rng = random.Random(1)

    def min_pos(f, var=x):
        """Least value of f on (0, oo) via critical points (and check it is a min by sampling)."""
        crit = [c for c in sp.solve(sp.diff(f, var), var) if c.is_real and c > 0]
        vals = [sp.nsimplify(sp.simplify(f.subs(var, c))) for c in crit]
        m = min(vals, key=lambda v: float(v))
        for _ in range(300):
            v = rng.uniform(0.01, 20)
            assert float(f.subs(var, v)) >= float(m) - 1e-9
        return m

    def max_on(f, var, lo, hi):
        crit = [c for c in sp.solve(sp.diff(f, var), var) if c.is_real and lo < c < hi]
        m = max((sp.simplify(f.subs(var, c)) for c in crit), key=lambda v: float(v))
        for _ in range(300):
            v = rng.uniform(lo, hi)
            assert float(f.subs(var, v)) <= float(m) + 1e-9
        return m

    def min_on(f, var, lo, hi):
        crit = [c for c in sp.solve(sp.diff(f, var), var) if c.is_real and lo < c < hi]
        m = min((sp.simplify(f.subs(var, c)) for c in crit), key=lambda v: float(v))
        for _ in range(300):
            v = rng.uniform(lo + 1e-6, hi - 1e-6)
            assert float(f.subs(var, v)) >= float(m) - 1e-9
        return m

    eq(min_pos(x + 1 / x), 2, "q1")
    eq(max_on(x * (10 - x), x, 0, 10), 25, "q2")
    eq(sp.Integer(6) ** 2 / sp.Rational(13, 2), sp.Rational(72, 13), "q3")
    eq(2 * 4 * 9 / sp.Integer(13), sp.Rational(72, 13), "q3 numbers 4, 9")
    # q4: sampling, and value 9 at a = b = c
    for _ in range(500):
        a, b, c = (rng.uniform(0.01, 10) for _ in range(3))
        assert (a + b + c) * (1 / a + 1 / b + 1 / c) >= 9 - 1e-9
    eq(3 * 3, 9, "q4")
    # q5: product 1 does not force equality
    assert sp.Rational(5, 4) > 1
    eq(min_pos(4 * x + 9 / x), 12, "q6")
    eq(max_on(x**2 * (3 - x), x, 0, 3), 4, "q7")
    eq(sp.Rational(3, 2) ** 3, sp.Rational(27, 8), "q7 distractor")
    eq(min_pos(2 * x + 3 * 6 / x), 12, "q8")
    th = sp.symbols("theta", real=True)
    eq(sp.maximum(3 * sp.cos(th) + 4 * sp.sin(th), th, sp.Interval(0, 2 * sp.pi)), 5, "q9")
    # q10: Lagrange -> point (1,2,2)
    lam = sp.symbols("lam")
    X, Y, Z = sp.symbols("X Y Z", real=True)
    sol = sp.solve([2 * X - lam, 2 * Y - 2 * lam, 2 * Z - 2 * lam, X + 2 * Y + 2 * Z - 9], [X, Y, Z, lam], dict=True)[0]
    eq((X**2 + Y**2 + Z**2).subs(sol), 9, "q10")
    eq(min_on(1 / x + 4 / (1 - x), x, 0, 1), 9, "q11")
    eq((1 / x + 4 / (1 - x)).subs(x, sp.Rational(1, 2)), 10, "q11 distractor")
    for n in range(2, 40):
        assert sp.factorial(n) < sp.Rational(n + 1, 2) ** n, "q12"
    assert sp.factorial(2) > sp.Rational(2, 2) ** 2  # (n/2)^n distractor fails at n = 2
    assert sp.factorial(2) > sp.Rational(1, 2) ** 2
    eq(max_on(x**3 * (5 - x) ** 2, x, 0, 5), 108, "q13")
    eq(sp.Rational(5, 2) ** 5, sp.Rational(3125, 32), "q13 distractor")
    assert sp.Rational(3125, 32) < 108
    # q14: max abc with a+b+c = 1 (Lagrange) + sampling
    sol = sp.solve([Y * Z - lam, X * Z - lam, X * Y - lam, X + Y + Z - 1], [X, Y, Z, lam], dict=True)
    best = max((X * Y * Z).subs(s) for s in sol if all(s[v] > 0 for v in (X, Y, Z)))
    eq(best, sp.Rational(1, 27), "q14")
    for _ in range(500):
        a, b = rng.uniform(0, 1), rng.uniform(0, 1)
        if a + b < 1:
            assert a * b * (1 - a - b) <= 1 / 27 + 1e-12
    # q15: ab+bc+ca with c = 6-a-b: Hessian negative definite, critical value 12
    a_, b_ = sp.symbols("a b", real=True)
    q = a_ * b_ + (a_ + b_) * (6 - a_ - b_)
    cs = sp.solve([sp.diff(q, a_), sp.diff(q, b_)], [a_, b_], dict=True)[0]
    eq(q.subs(cs), 12, "q15")
    assert all(ev < 0 for ev in sp.hessian(q, (a_, b_)).eigenvals())
    eq(min_on(x**4 + (2 - x) ** 4, x, 0, 2), 2, "q16")
    eq(min_on((x + 1 / x) ** 2 + (1 - x + 1 / (1 - x)) ** 2, x, 0, 1), sp.Rational(25, 2), "q17")
    # q18: (1+a)(1+b)(1+1/(ab)) min 8
    for _ in range(500):
        a, b = rng.uniform(0.01, 20), rng.uniform(0.01, 20)
        assert (1 + a) * (1 + b) * (1 + 1 / (a * b)) >= 8 - 1e-9
    eq(2**3, 8, "q18")
    # q19: xyz max with xy+yz+zx = 12
    sol = sp.solve([Y * Z - lam * (Y + Z), X * Z - lam * (X + Z), X * Y - lam * (X + Y), X * Y + Y * Z + Z * X - 12],
                   [X, Y, Z, lam], dict=True)
    best = max((X * Y * Z).subs(s) for s in sol if all(s[v].is_real and s[v] > 0 for v in (X, Y, Z)))
    eq(best, 8, "q19")
    for _ in range(500):
        a, b = rng.uniform(0.01, 3.4), rng.uniform(0.01, 3.4)
        if a * b < 12:
            c = (12 - a * b) / (a + b)
            assert a * b * c <= 8 + 1e-9
    # q20: quadratic form with matrix [[0,1/2,1/2],...]; range on unit sphere = [min eig, max eig]
    M = sp.Matrix(3, 3, lambda i, j: 0 if i == j else sp.Rational(1, 2))
    evs = M.eigenvals()
    eq(max(evs), 1, "q20 max")
    eq(min(evs), sp.Rational(-1, 2), "q20 min")
    # q21: m = 1/2, a = 1, b = 9
    assert sp.Rational(1 + 3, 2) < sp.sqrt(5)
    for _ in range(300):
        m = rng.uniform(0.01, 0.99)
        vals = [rng.uniform(0.1, 10) for _ in range(4)]
        assert sum(v**m for v in vals) / 4 <= (sum(vals) / 4) ** m + 1e-12

    # statements 1
    for _ in range(500):
        a, b, c = (rng.uniform(0.01, 10) for _ in range(3))
        assert a * a + b * b + c * c >= a * b + b * c + c * a - 1e-9
        assert (a + b) * (b + c) * (c + a) >= 8 * a * b * c - 1e-9
    assert not (3**3 >= 81)  # statement 3 fails at a = b = c = 1
    # statements 2
    for _ in range(300):
        av = [rng.uniform(-5, 5) for _ in range(4)]
        bv = [rng.uniform(-5, 5) for _ in range(4)]
        assert sum(p * q for p, q in zip(av, bv)) ** 2 <= sum(p * p for p in av) * sum(q * q for q in bv) + 1e-9
    lhs = sp.Integer(1) ** 2 / 1 + sp.Integer(1) ** 2 / sp.Rational(-1, 2)
    rhs = sp.Integer(2) ** 2 / (1 + sp.Rational(-1, 2))
    eq(lhs, -1, "st2 lhs"); eq(rhs, 8, "st2 rhs"); assert lhs < rhs
    assert sp.Rational(-5, 2) < sp.sqrt((-1) * (-4))

    # match 1: least values 2, 4, 3, 1
    right1 = [3, 4, 1, 2]
    got = [min_pos(f) for f in (x + 1 / x, x + 4 / x, x**2 + 2 / x, x + 1 / (4 * x))]
    key = [right1.index(v) + 1 for v in got]
    assert key == [4, 2, 1, 3], key
    # match 2: means of 2 and 8
    right2 = [sp.sqrt(34), sp.Rational(16, 5), 5, 4]
    means = [sp.Rational(10, 2), sp.sqrt(16), sp.Rational(2 * 2 * 8, 10), sp.sqrt(sp.Rational(4 + 64, 2))]
    key = [[sp.simplify(r - m) == 0 for r in right2].index(True) + 1 for m in means]
    assert key == [3, 4, 2, 1], key

    # AR1: same as q1
    eq(min_pos(x + 1 / x), 2, "ar1")
    # AR2: A true (max of x + 1/x on x<0 is -2), R false
    u = sp.symbols("u", negative=True)
    eq(sp.maximum(u + 1 / u, u, sp.Interval.open(-sp.oo, 0)), -2, "ar2 A")
    assert sp.Rational(-1 - 1, 2) < sp.sqrt(1)
    # AR3: A true by sampling, equality at 1/3 gives 8
    eq(((3 - 1) ** 3), 8, "ar3")
    for _ in range(500):
        a, b = rng.uniform(0.001, 1), rng.uniform(0.001, 1)
        if a + b < 0.999:
            c = 1 - a - b
            assert (1 / a - 1) * (1 / b - 1) * (1 / c - 1) >= 8 - 1e-6
    # AR4: n = 1 gives equality
    eq(sp.factorial(1), sp.Rational(2, 2) ** 1, "ar4")
    # AR5: Weierstrass, and the other Weierstrass bounds in the notes
    for _ in range(500):
        n = rng.randint(2, 6)
        av = [rng.uniform(0.001, 0.999) for _ in range(n)]
        p1 = 1.0; p2 = 1.0
        for v in av:
            p1 *= 1 - v; p2 *= 1 + v
        assert p1 > 1 - sum(av) and p2 > 1 + sum(av)
        s = sum(av)
        if s < 1:
            assert p2 < 1 / (1 - s) and p1 < 1 / (1 + s)

    # notes examples
    eq(min_pos(9 * t**2 + 4 / t**2, t), 12, "notes tan/cot")
    eq(sp.minimum(x + 1 / x, x, sp.Interval(3, sp.oo)), sp.Rational(10, 3), "notes x>=3")
    for n in range(1, 30):
        assert sp.factorial(n) ** 2 >= sp.Integer(n) ** n, "notes (n!)^2 >= n^n"
    eq(min_pos(x**2 + 1 / x + 1 / x), 3, "notes table")
    eq((1 / x + 4 / (1 - x)).subs(x, sp.Rational(1, 3)), 9, "notes engel eq point")


T.write(check)
