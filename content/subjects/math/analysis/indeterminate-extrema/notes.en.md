# Indeterminate Forms, Maxima and Minima

## L'Hospital's rule {#lhospital}

:::keyfacts
- **L'Hospital's rule ($0/0$).** Let $f, g$ be differentiable on a deleted neighbourhood $N'(a) = (a - \delta, a) \cup (a, a + \delta)$, with $g'(x) \ne 0$ on $N'(a)$. If $f(x) \to 0$ and $g(x) \to 0$ as $x \to a$, and $\displaystyle\lim_{x\to a}\frac{f'(x)}{g'(x)} = L$ (finite, $+\infty$ or $-\infty$), then $\displaystyle\lim_{x\to a}\frac{f(x)}{g(x)} = L$.
- **The $\infty/\infty$ form.** The same conclusion holds when $\lvert g(x)\rvert \to \infty$ instead.
- The rule also holds for one-sided limits and for $a = \pm\infty$.
:::

**Proof idea.** Define $f(a) = g(a) = 0$. Cauchy's mean value theorem on $[a, x]$ gives $\dfrac{f(x)}{g(x)} = \dfrac{f'(\xi)}{g'(\xi)}$ for some $\xi$ between $a$ and $x$; as $x \to a$, $\xi \to a$. This is why $g' \ne 0$ near $a$ is needed.

**Repeated use.** If $f'/g'$ is again $0/0$, apply the rule again:
$$\lim_{x\to0}\frac{x - \sin x}{x^3} = \lim\frac{1 - \cos x}{3x^2} = \lim\frac{\sin x}{6x} = \frac16.$$

Simplify between steps: cancel factors, and replace $\sin x$, $\tan x$, $e^x - 1$, $\ln(1 + x)$ by $x$ where they appear as **factors** of a product or quotient.

**When the rule does not apply.**

1. **Not indeterminate.** $\displaystyle\lim_{x\to0}\frac{x + 1}{x + 2} = \frac12$, but differentiating blindly gives $1$. Always check the form first.
2. **$\lim f'/g'$ does not exist.** The rule is a one-way implication. For $\dfrac{x + \sin x}{x}$ as $x \to \infty$:
   $$\frac{x + \sin x}{x} = 1 + \frac{\sin x}{x} \to 1, \quad\text{but}\quad \frac{f'}{g'} = 1 + \cos x \text{ oscillates}.$$
   Similarly $\dfrac{x^2\sin(1/x)}{\sin x} \to 0$ as $x \to 0$, while $\dfrac{f'}{g'} = \dfrac{2x\sin(1/x) - \cos(1/x)}{\cos x}$ has no limit.
3. **Going round in circles.** For $\dfrac{e^x + e^{-x}}{e^x - e^{-x}}$ as $x \to \infty$, the rule swaps numerator and denominator for ever. Divide by $e^x$ instead: the limit is $1$.

```plot
title: $y = \dfrac{x + \sin x}{x}$ tends to $1$, although $\dfrac{f'}{g'} = 1 + \cos x$ keeps oscillating
x: 0.5, 30
y: -0.2, 2.2
f: (x + sin(x))/x | $\dfrac{x + \sin x}{x}$
f: 1 + cos(x) | $1 + \cos x$
hline: 1
```

:::caution
"$\lim f'/g'$ does not exist" never proves "$\lim f/g$ does not exist". It only means the rule is silent.
:::

## Other indeterminate forms {#other-forms}

Every indeterminate form is reduced to $0/0$ or $\infty/\infty$ before the rule is used.

| Form | Reduction |
|:---|:---|
| $0\cdot\infty$ | $fg = \dfrac{f}{1/g}$ or $\dfrac{g}{1/f}$; keep the logarithm in the numerator |
| $\infty - \infty$ | take an LCM, or factor out the dominant term |
| $0^0,\ 1^\infty,\ \infty^0$ | put $y = f^g$, so $\ln y = g\ln f$, which is $0\cdot\infty$; then $\lim y = e^{\lim \ln y}$ |

**$0\cdot\infty$.** $\displaystyle\lim_{x\to0^+} x\ln x = \lim\frac{\ln x}{1/x} = \lim\frac{1/x}{-1/x^2} = \lim(-x) = 0$. More generally $x^\alpha\ln x \to 0$ as $x \to 0^+$ for every $\alpha > 0$.

**$\infty - \infty$.**
$$\lim_{x\to0}\left(\frac1x - \frac{1}{e^x - 1}\right) = \lim\frac{e^x - 1 - x}{x(e^x - 1)} = \lim\frac{e^x - 1 - x}{x^2} = \frac12.$$

**$1^\infty$ shortcut.** If $f \to 1$ and $g \to \infty$, then
$$\lim f^g = e^{\lim g\,(f - 1)},$$
because $\ln f \sim f - 1$. For example, $\displaystyle\lim_{x\to0}(1 + 3x)^{1/x} = e^3$ and $\displaystyle\lim_{x\to\infty}\left(1 + \frac ax\right)^x = e^a$.

**$0^0$.** $y = x^x$ gives $\ln y = x\ln x \to 0$, so $\displaystyle\lim_{x\to0^+} x^x = e^0 = 1$.

**$\infty^0$.** $\ln\big(x^{1/x}\big) = \dfrac{\ln x}{x} \to 0$, so $x^{1/x} \to 1$ as $x \to \infty$. Similarly $(\cot x)^{\sin x} \to 1$ as $x \to 0^+$, since $\sin x\,\ln\cot x \sim -x\ln x \to 0$.

:::caution
$0^0$ as a **form** is indeterminate even if a convention sets the number $0^0 = 1$. For $x \to 0^+$, $x^{1/\ln x} = e$ for every $x$, although its base $\to 0$ and its exponent $\to 0$. Similarly $0^\infty = 0$ and $\infty^\infty = \infty$ are **not** indeterminate.
:::

:::exam-tip
In $1^\infty$ problems never write $1^\infty = 1$. Compute $\lim g(f - 1)$ and exponentiate. For example $(\cos x)^{1/x^2}$: $\frac{\cos x - 1}{x^2} \to -\frac12$, so the limit is $e^{-1/2}$.
:::

## Standard limits {#standard-limits}

Most limits in the paper reduce to a few series (Maclaurin) facts. As $x \to 0$:

$$\sin x = x - \frac{x^3}{6} + \cdots, \quad \tan x = x + \frac{x^3}{3} + \cdots, \quad \cos x = 1 - \frac{x^2}{2} + \frac{x^4}{24} - \cdots,$$
$$e^x = 1 + x + \frac{x^2}{2} + \cdots, \quad \ln(1 + x) = x - \frac{x^2}{2} + \cdots.$$

| Limit ($x \to 0$ unless stated) | Value |
|:---|:---|
| $\dfrac{1 - \cos x}{x^2}$ | $\dfrac12$ |
| $\dfrac{x - \sin x}{x^3}$, $\;\dfrac{\tan x - x}{x^3}$ | $\dfrac16$, $\;\dfrac13$ |
| $\dfrac{e^x - 1 - x}{x^2}$ | $\dfrac12$ |
| $\dfrac{a^x - 1}{x}$ $(a > 0)$ | $\ln a$ |
| $\dfrac1{x^2} - \dfrac1{\sin^2 x}$, $\;\dfrac1{x^2} - \cot^2 x$ | $-\dfrac13$, $\;\dfrac23$ |
| $\left(1 + \dfrac ax\right)^x$, $x \to \infty$ | $e^a$ |
| $x^x$, $x \to 0^+$ | $1$ |
| $\left(\dfrac{\sin x}{x}\right)^{1/x^2}$ | $e^{-1/6}$ |
| $\left(\dfrac{\tan x}{x}\right)^{1/x^2}$ | $e^{1/3}$ |
| $(\cos x)^{1/x^2}$ | $e^{-1/2}$ |
| $\left(\dfrac{a^x + b^x}{2}\right)^{1/x}$ $(a, b > 0)$ | $\sqrt{ab}$ |
| $\dfrac{(1 + x)^{1/x} - e}{x}$ | $-\dfrac e2$ |

**Worked example.** $L = \displaystyle\lim_{x\to0}\left(\frac{\sin x}{x}\right)^{1/x^2}$ is $1^\infty$. With the shortcut,
$$\frac{1}{x^2}\left(\frac{\sin x}{x} - 1\right) = \frac{\sin x - x}{x^3} \to -\frac16, \quad\text{so } L = e^{-1/6}.$$
In the same way $\dfrac{\tan x - x}{x^3} \to \dfrac13$ gives $\left(\dfrac{\tan x}{x}\right)^{1/x^2} \to e^{1/3}$.

**Finding constants.** If $\displaystyle\lim_{x\to0}\frac{a\sin x - \sin 2x}{x^3}$ is finite, the $x$-term of the numerator must vanish: $a - 2 = 0$. Then $2\sin x - \sin 2x = x^3 + \cdots$, so the limit is $1$.

:::exam-tip
Sign check for the exponential forms: $\frac{\sin x}{x} < 1$ near $0$, so its limit power must be **below** $1$ ($e^{-1/6}$); $\frac{\tan x}{x} > 1$, so its limit is **above** $1$ ($e^{1/3}$).
:::

## Local extrema and the first-derivative test {#local-extrema}

$f$ has a **local maximum** at $c$ if $f(x) \le f(c)$ for all $x$ in some neighbourhood of $c$ (a **strict** local maximum if $f(x) < f(c)$ for $x \ne c$). Local minimum is similar. An extreme value is a local maximum or minimum value.

:::keyfacts
- **Fermat (necessary condition).** If $c$ is an interior point, $f$ has a local extremum at $c$ and $f'(c)$ exists, then $f'(c) = 0$.
- **Critical points** are the points where $f'(c) = 0$ (stationary points) or $f'(c)$ does not exist. Interior extrema occur only at critical points.
- **First-derivative test.** Let $f$ be continuous at $c$ and differentiable on $(c - \delta, c) \cup (c, c + \delta)$.
  - $f' > 0$ on the left and $f' < 0$ on the right: strict local **maximum**.
  - $f' < 0$ on the left and $f' > 0$ on the right: strict local **minimum**.
  - $f'$ has the same sign on both sides: **no** extremum.
:::

The test does **not** need $f'(c)$ to exist: $f(x) = \lvert x\rvert$ has a minimum at $0$, where $f$ is not differentiable. Conversely $f'(c) = 0$ is not enough: $x^3$ has $f'(0) = 0$ but $f' \ge 0$ on both sides, so there is no extremum.

**Example.** $f(x) = x^3 - 6x^2 + 9x + 1$, $f'(x) = 3(x - 1)(x - 3)$.

| Interval | $(-\infty, 1)$ | $(1, 3)$ | $(3, \infty)$ |
|:---|:---:|:---:|:---:|
| sign of $f'$ | $+$ | $-$ | $+$ |
| $f$ | increasing | decreasing | increasing |

So $f$ has a local maximum $f(1) = 5$ and a local minimum $f(3) = 1$.

**Max and min alternate.** Between two local maxima of a continuous function there is a local minimum, and vice versa.

:::caution
A local maximum value can be **smaller** than a local minimum value. For $f(x) = x + \dfrac1x$, the local maximum is $f(-1) = -2$ and the local minimum is $f(1) = 2$.
:::

## The second- and higher-derivative tests {#higher-derivative-test}

:::keyfacts
- **Second-derivative test.** If $f'(c) = 0$ and $f''(c)$ exists: $f''(c) < 0$ gives a local maximum; $f''(c) > 0$ gives a local minimum; $f''(c) = 0$ gives **no conclusion**.
- **Higher-derivative test.** Suppose $f'(c) = f''(c) = \cdots = f^{(n-1)}(c) = 0$ and $f^{(n)}(c) \ne 0$ (so $f^{(n)}$ is the first non-vanishing derivative at $c$).
  - $n$ **even**: an extremum; a **maximum** if $f^{(n)}(c) < 0$ and a **minimum** if $f^{(n)}(c) > 0$.
  - $n$ **odd**: **no** extremum. For $n \ge 3$ the point is a stationary point of inflexion.
:::

**Proof idea.** By Taylor's theorem, $f(c + h) - f(c) = \dfrac{h^n}{n!}\big(f^{(n)}(c) + \varepsilon(h)\big)$ with $\varepsilon(h) \to 0$. Near $c$ the sign is that of $h^n f^{(n)}(c)$. For even $n$ this sign is fixed; for odd $n$ it changes with the sign of $h$.

**Examples.**

- $x^4$ at $0$: $f' = f'' = f''' = 0$, $f^{(4)}(0) = 24 > 0$, $n = 4$ is even: **minimum**.
- $x^5$ at $0$: first non-zero derivative $f^{(5)}(0) = 120$, $n$ odd: **no extremum**.
- $f(x) = x^5 - 5x^4 + 5x^3 - 1$: $f'(x) = 5x^2(x - 1)(x - 3)$ and $f''(x) = 10x(2x^2 - 6x + 3)$.
  - $x = 1$: $f''(1) = -10 < 0$, a maximum, $f(1) = 0$.
  - $x = 3$: $f''(3) = 90 > 0$, a minimum, $f(3) = -28$.
  - $x = 0$: $f''(0) = 0$, $f'''(0) = 30 \ne 0$, $n = 3$ is odd: **neither**.

:::caution
The test needs a **non-vanishing** derivative. For $f(x) = e^{-1/x^2}$ ($x \ne 0$), $f(0) = 0$, every derivative at $0$ is zero, so the test says nothing. Yet $f$ has a minimum at $0$, because $f(x) > 0 = f(0)$ for $x \ne 0$.
:::

:::exam-tip
When $f''(c) = 0$, do not stop. Either go on to $f'''$, $f^{(4)}$, … or check the sign of $f'$ on both sides of $c$, which is often faster.
:::

## Concavity and points of inflexion {#inflexion}

$f$ is **concave upward** (convex) on an interval if its graph lies above every tangent there; this holds when $f'' > 0$. It is **concave downward** when $f'' < 0$.

A **point of inflexion** is a point $(c, f(c))$ of a continuous curve at which the concavity changes from one side to the other.

:::keyfacts
- **Necessary condition.** If $(c, f(c))$ is a point of inflexion and $f''(c)$ exists, then $f''(c) = 0$.
- **Sufficient conditions.** $f''$ changes sign at $c$; or $f''(c) = 0$ and $f'''(c) \ne 0$. More generally: if $f''(c) = \cdots = f^{(n-1)}(c) = 0$ and $f^{(n)}(c) \ne 0$, then $c$ is a point of inflexion when $n$ is odd ($n \ge 3$).
:::

- $f''(c) = 0$ is **not sufficient**: $y = x^4$ has $f''(0) = 0$ but is concave upward on both sides, so $0$ is not a point of inflexion.
- $f''$ need not exist: $y = x^{1/3}$ has $f'' = -\frac29 x^{-5/3}$, which is positive for $x < 0$ and negative for $x > 0$. The origin is a point of inflexion with a vertical tangent.
- At a point of inflexion the curve **crosses** its tangent.

**Example.** $y = x^4 - 4x^3$: $y'' = 12x(x - 2)$ changes sign at $0$ and at $2$, so there are two points of inflexion, $(0, 0)$ and $(2, -16)$. At $(0, 0)$ also $y' = 0$: a stationary point of inflexion.

For the cubic of the previous sections, $f'' = 6(x - 2)$, so the inflexion is at $(2, 3)$, midway between the maximum and the minimum. Every cubic has exactly one point of inflexion, at $x = -\frac{b}{3a}$ for $ax^3 + bx^2 + cx + d$.

```plot
title: $y = x^3 - 6x^2 + 9x + 1$ with its local maximum, local minimum and point of inflexion
x: -0.5, 4.5
y: -2, 7
f: x^3 - 6x^2 + 9x + 1 | $y = x^3 - 6x^2 + 9x + 1$
f: 3 - 3(x - 2) | tangent at the inflexion
point: 1, 5 | max $(1, 5)$
point: 3, 1 | min $(3, 1)$
point: 2, 3 | inflexion $(2, 3)$
```

:::exam-tip
For "number of points of inflexion", find the zeros of $f''$ and keep only those where $f''$ **changes sign**. A double root of $f''$ is not an inflexion.
:::

## Global extrema and applied problems {#global-extrema}

By the extreme value theorem, a function **continuous on a closed bounded interval** $[a, b]$ attains a greatest and a least value. They occur at a critical point in $(a, b)$ or at an endpoint.

**Closed-interval method.** Evaluate $f$ at the critical points in $(a, b)$ and at $a$ and $b$; the largest and smallest values are the global maximum and minimum.

**Example.** $f(x) = x^3 - 3x^2$ on $[-1, 4]$: $f' = 3x(x - 2)$. The values are $f(-1) = -4$, $f(0) = 0$, $f(2) = -4$, $f(4) = 16$. The global maximum is $16$ (at the endpoint $4$, not at the local maximum $x = 0$); the global minimum is $-4$.

On an open interval, or an unbounded one, a single critical point that is a local extremum is the global one if $f$ is continuous there.

**Applied problems.** Choose one variable, write the quantity, restrict the domain, then use the tests.

| Problem | Optimum |
|:---|:---|
| rectangle inscribed in a circle of radius $r$ | square; area $2r^2$ |
| rectangle inscribed in $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$ | sides $a\sqrt2$, $b\sqrt2$; area $2ab$ |
| rectangle of given perimeter | square |
| closed cylinder of given volume, least total surface | $h = 2r$ |
| open-top cylinder of given volume, least surface | $h = r$ |
| cylinder inscribed in a sphere of radius $R$ | $h = \dfrac{2R}{\sqrt3}$; $V = \dfrac{4\pi R^3}{3\sqrt3}$ |
| cone inscribed in a sphere of radius $R$ | $h = \dfrac{4R}{3}$; $V = \dfrac{32\pi R^3}{81}$ |
| open box from a square sheet of side $a$ | cut squares of side $\dfrac a6$; $V = \dfrac{2a^3}{27}$ |
| projectile with given speed $u$ | range greatest at $\alpha = 45^\circ$; $R = \dfrac{u^2}{g}$ |

**Cylinder in a sphere.** With height $h$, radius $r^2 = R^2 - \frac{h^2}{4}$, so $V = \pi\left(R^2h - \frac{h^3}{4}\right)$. Then $V' = \pi\left(R^2 - \frac{3h^2}{4}\right) = 0$ gives $h = \frac{2R}{\sqrt3}$, and $V'' < 0$ there.

**Minimum distance.** Minimise the **square** of the distance; it has the same minimiser. From $(0, 2)$ to $y = x^2$: $D = x^2 + (x^2 - 2)^2 = u + (u - 2)^2$ with $u = x^2 \ge 0$. $D'(u) = 2u - 3 = 0$ gives $u = \frac32$, $D = \frac74$, so the least distance is $\frac{\sqrt7}{2}$. The vertex $(0, 0)$ is at distance $2$, which is larger.

:::caution
Check the endpoints and the domain of the variable. A stationary point outside the physical range (a negative length, $u < 0$) is rejected.
:::

## Quick checks and traps {#exam-tips}

- **Check the form first.** L'Hospital's rule applies only to $0/0$ or $\infty/\infty$; differentiate the numerator and denominator **separately**, not as a quotient.
- **One-way rule.** $\lim f'/g'$ existing implies $\lim f/g$ exists; the converse fails, e.g. $(x + \sin x)/x \to 1$.
- **Hypotheses:** $f, g$ differentiable in a deleted neighbourhood, $g' \ne 0$ there, and $\lim f'/g'$ exists (finite or infinite).
- **$1^\infty$:** $\lim f^g = e^{\lim g(f - 1)}$. **$0^0$ and $\infty^0$:** take logarithms.
- **Not indeterminate:** $0^\infty = 0$, $\infty^\infty = \infty$, $\infty + \infty = \infty$, $0/\infty = 0$.
- **Series beat repeated differentiation** for $x^3$ denominators: $\sin x - x \sim -\frac{x^3}{6}$, $\tan x - x \sim \frac{x^3}{3}$, so $\dfrac{\tan x - x}{x - \sin x} \to 2$.
- **Higher-derivative test:** first non-vanishing derivative of **even** order gives an extremum (sign decides max or min); **odd** order gives none.
- **$f''(c) = 0$** proves neither an extremum nor an inflexion ($x^4$ at $0$ has a minimum and no inflexion).
- **Global extrema on $[a, b]$:** always compare the endpoint values.
- **$x^{1/x}$** ($x > 0$) is greatest at $x = e$, with value $e^{1/e}$; so $e^\pi > \pi^e$.
