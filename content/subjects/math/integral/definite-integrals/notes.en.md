# Definite Integrals

## The definite integral as the limit of a sum {#limit-of-sum}

Let $f$ be continuous (more generally, bounded and integrable) on $[a, b]$. Divide $[a, b]$ into $n$ **equal** parts of width
$$h = \frac{b - a}{n}, \qquad \text{points } a,\ a + h,\ a + 2h,\ \ldots,\ a + nh = b.$$
Then
$$\int_a^b f(x)\,dx = \lim_{n \to \infty} h \sum_{r=1}^{n} f(a + rh) = \lim_{h \to 0} h \sum_{r=0}^{n-1} f(a + rh).$$
The right-endpoint sum ($r = 1$ to $n$) and the left-endpoint sum ($r = 0$ to $n - 1$) differ by $h\,[f(b) - f(a)] \to 0$, so either may be used. Geometrically, for $f \ge 0$ the sum is the total area of $n$ thin rectangles, and the limit is the area under the curve.

**Example (first principles).** $\displaystyle\int_0^1 x^2\,dx$. Here $h = \frac1n$ and $f(rh) = \frac{r^2}{n^2}$:
$$h\sum_{r=1}^{n} \frac{r^2}{n^2} = \frac{1}{n^3}\cdot\frac{n(n + 1)(2n + 1)}{6} = \frac{(n + 1)(2n + 1)}{6n^2} \;\to\; \frac{2}{6} = \frac13.$$

```plot
title: Right-endpoint rectangles for $\int_0^1 x^2\,dx$ with $n = 4$: the sum overestimates $\tfrac13$
x: -0.2, 1.3
y: -0.1, 1.2
f: x^2 | $y = x^2$
shade: x^2, 0, 1
point: 0.25, 0.0625 | $f(h)$
point: 0.5, 0.25 | $f(2h)$
point: 0.75, 0.5625 | $f(3h)$
point: 1, 1 | $f(4h)$
```

**Example.** $\displaystyle\int_a^b e^x\,dx$ with $h = \frac{b - a}{n}$:
$$h\sum_{r=1}^{n} e^{a + rh} = h\,e^{a + h}\,\frac{e^{nh} - 1}{e^h - 1} = e^{a + h}\,(e^{b - a} - 1)\cdot\frac{h}{e^h - 1} \;\to\; e^b - e^a,$$
because $\frac{h}{e^h - 1} \to 1$.

The sums you need:
$$\sum_{r=1}^{n} r = \frac{n(n+1)}{2}, \quad \sum_{r=1}^{n} r^2 = \frac{n(n+1)(2n+1)}{6}, \quad \sum_{r=1}^{n} r^3 = \left[\frac{n(n+1)}{2}\right]^2.$$
For $\sin$ and $\cos$, use $\displaystyle\sum_{r=1}^{n}\sin(rh) = \frac{\sin\frac{nh}{2}\,\sin\frac{(n+1)h}{2}}{\sin\frac h2}$.

:::caution
The intervals must be **equal** for the formula $h\sum f(a + rh)$. With unequal partitions you are in Riemann's general theory (upper and lower sums), which is a later topic, `math.analysis.riemann-integration`.
:::

## Limits of sums as integrals {#sum-to-integral}

Reverse the definition with $a = 0$, $b = 1$, $h = \frac1n$:
$$\lim_{n \to \infty} \frac1n \sum_{r=1}^{n} f\!\left(\frac rn\right) = \int_0^1 f(x)\,dx.$$

**Recipe.**
1. Take out $\frac1n$ so that each term depends on $r$ and $n$ only through $\frac rn$.
2. Replace $\frac rn \to x$ and $\frac1n \to dx$.
3. Find the limits from the range of $\frac rn$: as $r$ runs from $1$ (or $0$) to $pn$, $x$ runs from $0$ to $p$.

**Worked examples.**

$$\lim_{n\to\infty}\sum_{r=1}^{n}\frac{n}{n^2 + r^2} = \lim \frac1n\sum \frac{1}{1 + (r/n)^2} = \int_0^1 \frac{dx}{1 + x^2} = \frac{\pi}{4}.$$

$$\lim_{n\to\infty}\sum_{r=1}^{n}\frac{1}{n + r} = \int_0^1\frac{dx}{1 + x} = \ln 2, \qquad \lim_{n\to\infty}\sum_{r=1}^{2n}\frac{1}{n + r} = \int_0^2\frac{dx}{1 + x} = \ln 3.$$

$$\lim_{n\to\infty}\sum_{r=1}^{n}\frac{r}{n^2 + r^2} = \int_0^1 \frac{x\,dx}{1 + x^2} = \frac12\ln 2, \qquad \lim_{n\to\infty}\sum_{r=1}^{n}\frac{r^{k}}{n^{k+1}} = \int_0^1 x^k\,dx = \frac{1}{k + 1}.$$

**Limits of products.** Take logarithms first. For $P_n = \left(\dfrac{n!}{n^n}\right)^{1/n}$:
$$\ln P_n = \frac1n\sum_{r=1}^{n}\ln\frac rn \;\to\; \int_0^1 \ln x\,dx = \Big[x\ln x - x\Big]_0^1 = -1, \qquad\text{so } P_n \to \frac1e.$$
(The integrand is unbounded at $0$, so this is an improper integral; the limit is still correct and is a standard exam result.)

:::exam-tip
Count the powers of $n$: a term like $\dfrac{n}{n^2 + r^2}$ has degree $-1$ in $(n, r)$, which supplies exactly the $\frac1n$ you need. If the degree is $-1$, the sum tends to an integral; if it is lower (e.g. $\frac{1}{n^2 + r^2}$), the sum tends to $0$.
:::

:::caution
Watch the upper limit. $\sum_{r=1}^{n}$ gives $\int_0^1$, but $\sum_{r=1}^{2n}$ or $\sum_{r=1}^{3n}$ gives $\int_0^2$ or $\int_0^3$. Writing $\int_0^1$ for $\sum_{r=1}^{2n}\frac{1}{n + r}$ gives $\ln 2$ instead of $\ln 3$.
:::

## The fundamental theorem and the Leibniz rule {#fundamental-theorem}

**Fundamental theorem of integral calculus (working form).**

1. If $f$ is **continuous** on $[a, b]$, then $F(x) = \displaystyle\int_a^x f(t)\,dt$ is differentiable on $[a, b]$ and $F'(x) = f(x)$.
2. If $f$ is integrable on $[a, b]$ and $\phi$ is differentiable on $[a, b]$ with $\phi' = f$ there, then
$$\int_a^b f(x)\,dx = \phi(b) - \phi(a).$$

So a definite integral is evaluated through any antiderivative, provided the antiderivative is valid on the **whole** closed interval.

**Leibniz rule for variable limits.** If $f$ is continuous on an interval containing the values of $u(x)$ and $v(x)$, and $u, v$ are differentiable, then
$$\frac{d}{dx}\int_{u(x)}^{v(x)} f(t)\,dt = f\big(v(x)\big)\,v'(x) - f\big(u(x)\big)\,u'(x).$$
It follows from part 1 and the chain rule: the integral is $F(v(x)) - F(u(x))$.

**Examples.**
- $\dfrac{d}{dx}\displaystyle\int_0^{x^2}\cos t\,dt = 2x\cos(x^2)$.
- For $x > 1$: $\dfrac{d}{dx}\displaystyle\int_x^{x^2}\frac{dt}{\ln t} = \frac{2x}{\ln x^2} - \frac{1}{\ln x} = \frac{x - 1}{\ln x}$.
- When $x$ is also inside the integrand, take it outside first:
$$\phi(x) = \int_0^x (x - t)g(t)\,dt = x\int_0^x g(t)\,dt - \int_0^x t\,g(t)\,dt \;\Rightarrow\; \phi'(x) = \int_0^x g(t)\,dt,\quad \phi''(x) = g(x).$$

**Limits with integrals.** Use L'Hospital's rule with part 1:
$$\lim_{x\to0}\frac{\int_0^x \sin(t^2)\,dt}{x^3} = \lim_{x\to0}\frac{\sin(x^2)}{3x^2} = \frac13.$$

**Extrema.** $F(x) = \int_0^x (t - 1)(t - 2)\,dt$ has $F'(x) = (x - 1)(x - 2)$, which changes sign from $+$ to $-$ at $x = 1$ (local maximum) and from $-$ to $+$ at $x = 2$ (local minimum).

:::caution
Check the hypotheses before using $\phi(b) - \phi(a)$. The "answer" $\int_{-1}^{1}\frac{dx}{x^2} = \left[-\frac1x\right]_{-1}^{1} = -2$ is absurd for a positive integrand: $\frac{1}{x^2}$ is unbounded on $[-1, 1]$, and $-\frac1x$ is not an antiderivative on the whole interval. Likewise, a substitution such as $t = \tan x$ fails on an interval containing $\frac{\pi}{2}$.
:::

## Properties of definite integrals {#properties}

For $f$ continuous on the intervals involved:

| Property | Statement |
|:---|:---|
| P1 dummy variable | $\int_a^b f(x)\,dx = \int_a^b f(t)\,dt$ |
| P2 reversal | $\int_a^b f = -\int_b^a f$, and $\int_a^a f = 0$ |
| P3 additivity | $\int_a^b f = \int_a^c f + \int_c^b f$ for any $c$ |
| P4 | $\int_a^b f(x)\,dx = \int_a^b f(a + b - x)\,dx$ |
| P5 (special case) | $\int_0^a f(x)\,dx = \int_0^a f(a - x)\,dx$ |
| P6 | $\int_0^{2a} f(x)\,dx = \int_0^a f(x)\,dx + \int_0^a f(2a - x)\,dx$ |

**Proof of P4.** Put $x = a + b - t$: $dx = -dt$, $x = a \mapsto t = b$, $x = b \mapsto t = a$, so $\int_a^b f(x)\,dx = \int_b^a f(a + b - t)(-dt) = \int_a^b f(a + b - t)\,dt$.

**The add-the-two-forms trick.** If $I = \int_a^b g(x)\,dx$ and P4 turns $g(x)$ into $h(x)$ with $g + h$ simple, then $2I = \int_a^b (g + h)\,dx$.

**Example 1.** For any $n > 0$, let $I = \displaystyle\int_0^{\pi/2}\frac{\sin^n x}{\sin^n x + \cos^n x}\,dx$. By P5, $\sin \leftrightarrow \cos$, so
$$I = \int_0^{\pi/2}\frac{\cos^n x}{\cos^n x + \sin^n x}\,dx \;\Rightarrow\; 2I = \int_0^{\pi/2} 1\,dx = \frac{\pi}{2},\quad I = \frac{\pi}{4}.$$
The same works for $\dfrac{\sqrt{\tan x}}{1 + \sqrt{\tan x}}$, $\dfrac{1}{1 + \tan^n x}$, and so on: each gives $\frac{\pi}{4}$ on $[0, \frac{\pi}{2}]$.

**Example 2 (general form).** $\displaystyle\int_a^b \frac{f(x)}{f(x) + f(a + b - x)}\,dx = \frac{b - a}{2}$, if the denominator never vanishes. For instance
$$\int_2^3\frac{\sqrt x}{\sqrt x + \sqrt{5 - x}}\,dx = \frac{3 - 2}{2} = \frac12.$$

**Example 3.** $I = \displaystyle\int_0^{\pi/4}\ln(1 + \tan x)\,dx$. By P5, $1 + \tan\left(\frac{\pi}{4} - x\right) = \dfrac{2}{1 + \tan x}$, so
$$I = \int_0^{\pi/4}\big[\ln 2 - \ln(1 + \tan x)\big]dx = \frac{\pi}{4}\ln 2 - I, \qquad I = \frac{\pi}{8}\ln 2.$$

**Greatest-integer integrands.** Split at the points where the integer part jumps. With $[\cdot]$ the greatest integer function, $[x^2]$ jumps at $x = 1, \sqrt2, \sqrt3$:
$$\int_0^2 [x^2]\,dx = 0 + 1(\sqrt2 - 1) + 2(\sqrt3 - \sqrt2) + 3(2 - \sqrt3) = 5 - \sqrt2 - \sqrt3.$$

:::exam-tip
P4 is the one-minute tool for symmetric-looking integrands. Whenever the integrand has $\sin$ and $\cos$ on $[0, \frac{\pi}{2}]$, or $x$ and $a + b - x$ on $[a, b]$, try the substitution and add.
:::

## Even, odd and periodic functions {#symmetry}

**Even and odd.** For $f$ continuous on $[-a, a]$:
$$\int_{-a}^{a} f(x)\,dx = \begin{cases} 2\displaystyle\int_0^a f(x)\,dx, & f \text{ even } (f(-x) = f(x)),\\[2mm] 0, & f \text{ odd } (f(-x) = -f(x)).\end{cases}$$
In general, $\int_{-a}^{a} f(x)\,dx = \int_0^a [f(x) + f(-x)]\,dx$.

Example: on $[-\frac{\pi}{2}, \frac{\pi}{2}]$, the functions $x^3$, $x\cos x$ and $\sin^5 x$ are odd, so
$$\int_{-\pi/2}^{\pi/2}\big(x^3 + x\cos x + \sin^5 x + 1\big)\,dx = 0 + \int_{-\pi/2}^{\pi/2}1\,dx = \pi.$$
The odd terms must be continuous on the closed interval: $\tan^5 x$ would be unbounded at $\pm\frac{\pi}{2}$, and then the rule does not apply.

**The $2a$ rule.** From P6:
$$\int_0^{2a} f(x)\,dx = \begin{cases} 2\displaystyle\int_0^a f(x)\,dx, & \text{if } f(2a - x) = f(x),\\[2mm] 0, & \text{if } f(2a - x) = -f(x).\end{cases}$$
Examples with $a = \frac{\pi}{2}$: $\sin(\pi - x) = \sin x$, so $\int_0^{\pi}\sin^3 x\,dx = 2\int_0^{\pi/2}\sin^3 x\,dx = \frac43$. And $\cos(\pi - x) = -\cos x$, so $\int_0^{\pi}\cos^{2k+1} x\,dx = 0$.

**Periodic functions.** If $f$ is continuous with period $T$, then for every $a$ and every positive integer $n$:
$$\int_a^{a + T} f(x)\,dx = \int_0^T f(x)\,dx, \qquad \int_0^{nT} f(x)\,dx = n\int_0^T f(x)\,dx.$$
So an integral over one full period does not depend on where the period starts.

**Example.** $|\sin x|$ has period $\pi$ and $\int_0^{\pi}|\sin x|\,dx = 2$. Hence $\int_0^{10\pi}|\sin x|\,dx = 20$, and for $0 \le v < \pi$:
$$\int_0^{n\pi + v}|\sin x|\,dx = 2n + \int_0^{v}\sin x\,dx = 2n + 1 - \cos v.$$

Similarly, $\int_0^{\pi}|\cos x|\,dx = 2$, since $|\cos x|$ also has period $\pi$.

:::caution
"Odd" is about symmetry **about $0$**. The rule $\int = 0$ needs a symmetric interval $[-a, a]$. An odd function on $[0, 2a]$ need not integrate to $0$: $\int_0^{2} x\,dx = 2$. On $[0, 2a]$, the test is $f(2a - x) = -f(x)$, not oddness.
:::

## Standard results {#standard-results}

Here $\log$ means the natural logarithm.

**1. The log sine integral.**
$$\int_0^{\pi/2}\log\sin x\,dx = \int_0^{\pi/2}\log\cos x\,dx = -\frac{\pi}{2}\log 2.$$
The integrand tends to $-\infty$ at $x = 0$, so strictly this is a convergent improper integral (convergence belongs to `math.analysis.improper-integrals`). The evaluation is examinable:

- Let $I$ be the integral. By P5, $I = \int_0^{\pi/2}\log\cos x\,dx$.
- Add: $2I = \int_0^{\pi/2}\log(\sin x\cos x)\,dx = \int_0^{\pi/2}\log\sin 2x\,dx - \frac{\pi}{2}\log 2$.
- Put $t = 2x$: $\int_0^{\pi/2}\log\sin 2x\,dx = \frac12\int_0^{\pi}\log\sin t\,dt = \frac12\cdot 2I = I$ (by the $2a$ rule).
- So $2I = I - \frac{\pi}{2}\log 2$, giving $I = -\frac{\pi}{2}\log 2$.

**Consequences.**
- $\int_0^{\pi}\log\sin x\,dx = -\pi\log 2$.
- $\int_0^{\pi/2}\log\tan x\,dx = 0$ (it is $\int\log\sin - \int\log\cos$).
- $\int_0^{1}\dfrac{\log x}{\sqrt{1 - x^2}}\,dx = -\frac{\pi}{2}\log 2$ (put $x = \sin\theta$).

**2. The $x f(\sin x)$ result.** For $f$ continuous on $[0, 1]$:
$$\int_0^{\pi} x\,f(\sin x)\,dx = \frac{\pi}{2}\int_0^{\pi} f(\sin x)\,dx.$$
Proof: by P4, $I = \int_0^{\pi}(\pi - x)f(\sin x)\,dx$, since $\sin(\pi - x) = \sin x$. Adding gives $2I = \pi\int_0^{\pi} f(\sin x)\,dx$.

Examples:
$$\int_0^{\pi} x\sin x\,dx = \frac{\pi}{2}\int_0^{\pi}\sin x\,dx = \pi, \qquad \int_0^{\pi}\frac{x}{1 + \sin x}\,dx = \frac{\pi}{2}\cdot 2 = \pi,$$
$$\int_0^{\pi}\frac{x\sin x}{1 + \cos^2 x}\,dx = \frac{\pi}{2}\int_0^{\pi}\frac{\sin x}{1 + \cos^2 x}\,dx = \frac{\pi}{2}\Big[-\tan^{-1}(\cos x)\Big]_0^{\pi} = \frac{\pi}{2}\cdot\frac{\pi}{2} = \frac{\pi^2}{4}.$$
Here $\cos^2 x = 1 - \sin^2 x$, so the integrand really is of the form $x f(\sin x)$.

**3. The $\frac{\pi}{4}$ family.** For every $n > 0$,
$$\int_0^{\pi/2}\frac{\sin^n x}{\sin^n x + \cos^n x}\,dx = \frac{\pi}{4}$$
(see the properties section). Wallis's formula for $\int_0^{\pi/2}\sin^n x\,dx$ belongs to `math.integral.reduction-formulae`.

:::exam-tip
In $\int_0^{\pi} x\,(\ldots)\,dx$, first check that the bracket is unchanged by $x \to \pi - x$. If it is, replace $x$ by $\frac{\pi}{2}$ and integrate what is left.
:::

## The first mean value theorem and bounds {#mean-value-bounds}

**Bounds.** If $f$ is integrable on $[a, b]$ (with $a < b$) and $m \le f(x) \le M$ there, then
$$m(b - a) \le \int_a^b f(x)\,dx \le M(b - a).$$
Further:
- **Comparison:** $f \le g$ on $[a, b]$ gives $\int_a^b f \le \int_a^b g$. If $f, g$ are continuous and $f \ne g$ somewhere, the inequality is strict.
- **Modulus:** $\left|\int_a^b f\right| \le \int_a^b |f|$.

**First mean value theorem.** If $f$ is **continuous** on $[a, b]$, there is a $\xi \in [a, b]$ with
$$\int_a^b f(x)\,dx = f(\xi)\,(b - a).$$
The number $\dfrac{1}{b - a}\displaystyle\int_a^b f(x)\,dx$ is the **mean value** (average) of $f$ on $[a, b]$. Proof idea: the average lies between $\min f$ and $\max f$, and the intermediate value theorem gives $\xi$.

**Generalised form.** If $f$ is continuous on $[a, b]$, and $g$ is integrable and does **not change sign** on $[a, b]$, then for some $\xi \in [a, b]$,
$$\int_a^b f(x)g(x)\,dx = f(\xi)\int_a^b g(x)\,dx.$$
(The second mean value theorem, Bonnet's form, belongs to `math.analysis.riemann-integration`.)

**Examples.**
- Mean value of $x^2$ on $[0, 3]$: $\frac13\int_0^3 x^2\,dx = 3$, attained at $\xi = \sqrt3 \in [0, 3]$.
- On $[0, 1]$, $1 \le e^{x^2} \le e$, with equality only at an end point, so $1 < \int_0^1 e^{x^2}\,dx < e$. (Using $e^{x^2} \ge 1 + x^2$ gives the sharper bound $\ge \frac43$; the value is about $1.4627$.)
- For $0 \le x \le \frac12$ and $n \ge 1$, $x^{2n} \le x^2$, so $1 \le \dfrac{1}{\sqrt{1 - x^{2n}}} \le \dfrac{1}{\sqrt{1 - x^2}}$ and
$$\frac12 \le \int_0^{1/2}\frac{dx}{\sqrt{1 - x^{2n}}} \le \int_0^{1/2}\frac{dx}{\sqrt{1 - x^2}} = \frac{\pi}{6}.$$

:::caution
Continuity is essential in the mean value theorem. For $f = 0$ on $[0, 1)$ and $f = 1$ on $[1, 2]$, $\int_0^2 f = 1$, but $f(\xi)(2 - 0) = 1$ needs $f(\xi) = \frac12$, which $f$ never takes. Also, $\xi$ is **not** in general the midpoint: for $x^2$ on $[0, 3]$, $\xi = \sqrt3$, not $\frac32$.
:::

## Quick checks and traps {#exam-tips}

- **Sign check.** A positive integrand on $[a, b]$ with $a < b$ gives a positive integral. A negative answer, as in $\int_{-1}^{1}\frac{dx}{x^2} = -2$, means a hypothesis failed.
- **Odd-function shortcut:** on $[-a, a]$, delete every odd term first, e.g. $\int_{-1}^{1}(x^5\cos x + x^2)\,dx = \frac23$.
- **The $\frac{\pi}{4}$ family:** $\int_0^{\pi/2}\frac{\sin^n x}{\sin^n x + \cos^n x}\,dx = \frac{\pi}{4}$ for every $n > 0$; $\int_a^b\frac{f(x)}{f(x) + f(a + b - x)}\,dx = \frac{b - a}{2}$.
- **Log sine:** $-\frac{\pi}{2}\log 2$ on $[0, \frac{\pi}{2}]$, $-\pi\log 2$ on $[0, \pi]$, and $\int_0^{\pi/2}\log\tan x\,dx = 0$.
- **Limit of a sum:** pull out $\frac1n$, set $\frac rn = x$, and read the upper limit from the last value of $\frac rn$.
- **Leibniz rule:** do not forget the chain-rule factors $v'(x)$ and $u'(x)$, or the minus sign on the lower limit.
- **Periodic:** $\int_0^{n\pi}|\sin x|\,dx = 2n$ and $\int_0^{n\pi}|\cos x|\,dx = 2n$.
- **Mean value theorem:** needs continuity; $\xi$ exists, but it is rarely the midpoint.
- Riemann's theory (upper and lower sums, integrability) and the convergence of improper integrals are later topics: `math.analysis.riemann-integration` and `math.analysis.improper-integrals`.
