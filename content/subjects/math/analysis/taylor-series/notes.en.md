# Taylor's Theorem and Expansions

## Taylor's theorem and the remainder {#taylor-theorem}

Taylor's theorem extends Lagrange's mean value theorem: it approximates $f(a + h)$ by a polynomial in $h$ and gives the error exactly, through an unknown point between $a$ and $a + h$.

:::keyfacts
- **Hypotheses.** $f^{(n)}$ is continuous on $[a, a + h]$ and $f^{(n+1)}$ exists on the open interval $(a, a + h)$. (The case $h < 0$ is the same with $[a + h, a]$.)
- **Conclusion.** There is a $\theta \in (0, 1)$ with
  $$f(a + h) = f(a) + h f'(a) + \frac{h^2}{2!}f''(a) + \cdots + \frac{h^n}{n!}f^{(n)}(a) + R_{n+1}.$$
- **Lagrange form:** $\displaystyle R_{n+1} = \frac{h^{n+1}}{(n+1)!}\,f^{(n+1)}(a + \theta h)$.
- **Cauchy form:** $\displaystyle R_{n+1} = \frac{h^{n+1}(1 - \theta)^{n}}{n!}\,f^{(n+1)}(a + \theta h)$.
:::

- $\theta$ depends on $f$, $a$, $h$, $n$ **and on the form** chosen. The Lagrange $\theta$ and the Cauchy $\theta$ are usually different numbers.
- With $n = 0$ the Lagrange form is exactly Lagrange's MVT: $f(a + h) = f(a) + h f'(a + \theta h)$.
- **Schlömilch–Roche form** (general): $R_{n+1} = \dfrac{h^{n+1}(1 - \theta)^{n + 1 - p}}{p\cdot n!}f^{(n+1)}(a + \theta h)$, $p > 0$. Putting $p = n + 1$ gives Lagrange; $p = 1$ gives Cauchy.

**Proof idea.** Fix $p$ and apply Rolle's theorem on $[a, a + h]$ to
$$\phi(x) = f(a + h) - \sum_{k=0}^{n}\frac{(a + h - x)^k}{k!}f^{(k)}(x) - A\,(a + h - x)^p,$$
with $A$ chosen so that $\phi(a) = \phi(a + h) = 0$. The derivative telescopes to a single term, and $\phi'(c) = 0$ gives the remainder.

**Finding $\theta$.** For $f(x) = (1 - x)^{5/2}$, $a = 0$, $h = 1$, $n = 1$ (Lagrange):
$$0 = 1 - \frac52 + \frac12\cdot\frac{15}{4}(1 - \theta)^{1/2} \;\Rightarrow\; \sqrt{1 - \theta} = \frac45 \;\Rightarrow\; \theta = \frac{9}{25}.$$

For $f(x) = x^3$, $a = 0$, $n = 1$: Lagrange gives $h^3 = \frac{h^2}{2}\cdot 6\theta h$, so $\theta = \frac13$. Cauchy gives $h^3 = h^2(1 - \theta)\cdot 6\theta h$, so $\theta(1 - \theta) = \frac16$ and $\theta = \frac{3 \pm \sqrt3}{6}$: a different value.

:::exam-tip
**Limit of $\theta$.** In $f(a + h) = f(a) + hf'(a) + \frac{h^2}{2}f''(a + \theta h)$, if $f'''$ is continuous at $a$ and $f'''(a) \ne 0$, then $\theta \to \frac13$ as $h \to 0$. In general, with $n$ terms before the remainder, $\theta \to \frac{1}{n + 1}$ (Lagrange's MVT: $\theta \to \frac12$).
:::

## Maclaurin's theorem and Maclaurin series {#maclaurin-theorem}

Put $a = 0$, $h = x$ in Taylor's theorem. If $f^{(n)}$ is continuous on $[0, x]$ (or $[x, 0]$) and $f^{(n+1)}$ exists between, then
$$f(x) = \sum_{k=0}^{n}\frac{f^{(k)}(0)}{k!}x^k + R_{n+1}(x),$$
$$R_{n+1} = \frac{x^{n+1}}{(n+1)!}f^{(n+1)}(\theta x)\ \text{(Lagrange)}, \qquad R_{n+1} = \frac{x^{n+1}(1 - \theta)^n}{n!}f^{(n+1)}(\theta x)\ \text{(Cauchy)}.$$

**Maclaurin series.** If $f$ has derivatives of all orders near $0$, the series $\sum \frac{f^{(k)}(0)}{k!}x^k$ can be written down. It equals $f(x)$ **if and only if $R_{n}(x) \to 0$** as $n \to \infty$. Convergence of the series alone is not enough (see [the $e^{-1/x^2}$ example](#non-analytic)).

**A sufficient test.** If $|f^{(n)}(t)| \le M$ for all $n$ and all $t$ between $0$ and $x$, then $|R_{n+1}| \le M\frac{|x|^{n+1}}{(n+1)!} \to 0$. This settles $\sin x$, $\cos x$ and $e^x$ (on $|t| \le |x|$, $e^t \le e^{|x|}$).

**Why both remainders are needed: $\log(1 + x)$.** Here $f^{(n+1)}(t) = \frac{(-1)^n n!}{(1 + t)^{n+1}}$.

- **Lagrange:** $R_{n+1} = \dfrac{(-1)^n}{n + 1}\left(\dfrac{x}{1 + \theta x}\right)^{n+1}$. For $0 \le x \le 1$, $\left|\frac{x}{1 + \theta x}\right| \le 1$, so $|R_{n+1}| \le \frac{1}{n + 1} \to 0$. For $-1 < x < -\frac12$ this bound fails, since $\frac{|x|}{1 - \theta|x|}$ can exceed $1$.
- **Cauchy:** $R_{n+1} = (-1)^n x^{n+1}\dfrac{(1 - \theta)^n}{(1 + \theta x)^{n+1}}$. For $-1 < x < 0$, $\frac{1 - \theta}{1 + \theta x} < 1$, so $|R_{n+1}| \le \frac{|x|^{n+1}}{1 - |x|} \to 0$.

The binomial series $(1 + x)^m$ is handled the same way, with the Cauchy form for $|x| < 1$.

:::caution
"The Maclaurin series converges" and "the Maclaurin series converges **to $f$**" are different claims. The test is always $R_n \to 0$.
:::

## Standard expansions and their ranges {#standard-expansions}

| Function | Maclaurin series | Valid for |
|:---|:---|:---|
| $e^x$ | $1 + x + \dfrac{x^2}{2!} + \dfrac{x^3}{3!} + \cdots$ | all real $x$ |
| $a^x$ ($a > 0$) | $1 + x\ln a + \dfrac{(x\ln a)^2}{2!} + \cdots$ | all real $x$ |
| $\sin x$ | $x - \dfrac{x^3}{3!} + \dfrac{x^5}{5!} - \cdots$ | all real $x$ |
| $\cos x$ | $1 - \dfrac{x^2}{2!} + \dfrac{x^4}{4!} - \cdots$ | all real $x$ |
| $\log(1 + x)$ | $x - \dfrac{x^2}{2} + \dfrac{x^3}{3} - \cdots$ | $-1 < x \le 1$ |
| $\tan^{-1}x$ | $x - \dfrac{x^3}{3} + \dfrac{x^5}{5} - \cdots$ | $-1 \le x \le 1$ |
| $(1 + x)^m$ | $1 + mx + \dfrac{m(m - 1)}{2!}x^2 + \cdots$ | $-1 < x < 1$ (see below) |

Here $\log$ is the natural logarithm. The coefficient of $x^n$ in $a^x$ is $\frac{(\ln a)^n}{n!}$, since $a^x = e^{x\ln a}$.

**Endpoints of the binomial series** ($m$ not a non-negative integer; for $m = 0, 1, 2, \ldots$ it is a polynomial, valid for all $x$):

| $m$ | at $x = 1$ | at $x = -1$ |
|:---|:---|:---|
| $m > 0$ | converges (absolutely) | converges (absolutely) |
| $-1 < m < 0$ | converges (conditionally) | diverges |
| $m \le -1$ | diverges | diverges |

Where it converges, the sum is $(1 + x)^m$ (by Abel's limit theorem). So $(1 + x)^{-1/2}$ is represented on $(-1, 1]$ and $(1 + x)^{1/2}$ on $[-1, 1]$, while $(1 + x)^{-1} = 1 - x + x^2 - \cdots$ only on $(-1, 1)$.

**Endpoint values worth knowing:** $\log 2 = 1 - \frac12 + \frac13 - \cdots$ and $\frac{\pi}{4} = 1 - \frac13 + \frac15 - \cdots$ (Gregory–Leibniz).

:::caution
$\tan^{-1}x$ comes from integrating $\frac{1}{1 + t^2} = 1 - t^2 + t^4 - \cdots$, which converges only for $|t| < 1$. The arctan series still converges at $x = \pm1$ (alternating series with terms decreasing to $0$), and the sum is correct there. Don't conclude that the integrated series fails at $\pm1$ just because the integrand series does.
:::

**Related series.** $\log\dfrac{1 + x}{1 - x} = 2\left(x + \dfrac{x^3}{3} + \dfrac{x^5}{5} + \cdots\right)$ for $|x| < 1$, and $-\log(1 - x) = x + \dfrac{x^2}{2} + \dfrac{x^3}{3} + \cdots$ for $-1 \le x < 1$.

## Expansion by known series {#expansion-by-series}

Direct differentiation is slow. Instead, combine the standard series by multiplication, substitution and division, keeping only the powers you need.

**Products.** Up to $x^3$:
$$e^x\sin x = \left(1 + x + \tfrac{x^2}{2} + \tfrac{x^3}{6}\right)\left(x - \tfrac{x^3}{6}\right) = x + x^2 + \left(\tfrac12 - \tfrac16\right)x^3 + \cdots = x + x^2 + \frac{x^3}{3} + \cdots$$

**Substitution.** With $s = \sin x = x - \frac{x^3}{6} + \cdots$,
$$\log(1 + \sin x) = s - \frac{s^2}{2} + \frac{s^3}{3} - \cdots = x - \frac{x^2}{2} + \left(-\tfrac16 + \tfrac13\right)x^3 + \cdots = x - \frac{x^2}{2} + \frac{x^3}{6} - \cdots$$

Similarly $e^{\sin x} = 1 + x + \frac{x^2}{2} - \frac{x^4}{8} - \cdots$ (the $x^3$ terms cancel).

**Division.** $\tan x = \dfrac{\sin x}{\cos x} = x + \dfrac{x^3}{3} + \dfrac{2x^5}{15} + \cdots$ (for $|x| < \frac{\pi}{2}$).

**Coefficient of $x^n$.**

- $e^{kx}$: $\dfrac{k^n}{n!}$.
- $\dfrac{e^x}{1 - x} = \left(\sum \frac{x^j}{j!}\right)\left(\sum x^i\right)$: the coefficient is $\displaystyle\sum_{j=0}^{n}\frac{1}{j!}$.
- $(1 + x)^{1/2}$: $\binom{1/2}{3} = \frac{\frac12\cdot(-\frac12)(-\frac32)}{3!} = \frac{1}{16}$ for $x^3$.

**Derivatives at $0$ from a series.** If $f(x) = \sum c_k x^k$ near $0$, then $f^{(n)}(0) = n!\,c_n$.

- $f(x) = x^2e^x = \sum \frac{x^{k+2}}{k!}$, so $c_{10} = \frac{1}{8!}$ and $f^{(10)}(0) = \frac{10!}{8!} = 90$.
- $\tan^{-1}x$: $c_5 = \frac15$, so the fifth derivative at $0$ is $\frac{5!}{5} = 24$. Even-order derivatives at $0$ vanish (odd function).

```plot
title: $\sin x$ and its Taylor polynomials of degree 1, 3 and 5 at $0$
x: -2pi, 2pi
y: -3, 3
xticks: pi
f: sin(x) | $\sin x$
f: x | $T_1 = x$
f: x - x^3/6 | $T_3$
f: x - x^3/6 + x^5/120 | $T_5$
```

Each higher-degree polynomial hugs $\sin x$ over a wider interval, but every polynomial eventually leaves it. Convergence is pointwise in $n$ for each fixed $x$, not with a fixed degree.

## A smooth function its Taylor series misses {#non-analytic}

Let
$$f(x) = \begin{cases} e^{-1/x^2}, & x \ne 0, \\ 0, & x = 0. \end{cases}$$

- $f$ is continuous at $0$, since $e^{-1/x^2} \to 0$.
- For $x \ne 0$, every derivative has the form $f^{(n)}(x) = P_n\!\left(\frac1x\right)e^{-1/x^2}$ with $P_n$ a polynomial. Since $t^k e^{-t^2} \to 0$ as $|t| \to \infty$, induction on the difference quotient gives **$f^{(n)}(0) = 0$ for every $n$**.
- So $f$ is infinitely differentiable on $\R$, and its Maclaurin series is $0 + 0x + 0x^2 + \cdots$, which converges for every $x$, to $0$.
- But $f(x) > 0$ for $x \ne 0$. The series represents $f$ **only at $x = 0$**.

In Taylor's language, $R_n(x) = f(x)$ for every $n$, which does not tend to $0$.

```plot
title: $e^{-1/x^2}$ is extremely flat at $0$, yet not identically zero
x: -3, 3
y: -0.2, 1
f: exp(-1/x^2) | $e^{-1/x^2}$
hline: 1
point: 0, 0 | all derivatives $0$
```

**Consequences.**

- Infinitely differentiable ($C^\infty$) does **not** imply analytic (equal to its Taylor series near each point).
- Two different $C^\infty$ functions can have the same Maclaurin series: $g$ and $g + e^{-1/x^2}$.
- Contrast with complex analysis, where one complex derivative already forces analyticity.

:::caution
A common wrong option says "$f$ has no Maclaurin series because $f'(0)$ does not exist". All derivatives exist and are $0$. The series exists; it simply converges to the wrong function.
:::

## Limits by expansion {#limits-by-series}

For $\frac00$ forms at $0$, expand numerator and denominator to the first non-vanishing power. This is often faster than repeated L'Hospital (covered with the other indeterminate forms in the next topic).

$$\lim_{x \to 0}\frac{x - \sin x}{x^3} = \lim\frac{\frac{x^3}{6} - \frac{x^5}{120} + \cdots}{x^3} = \frac16, \qquad \lim_{x \to 0}\frac{e^x - 1 - x}{x^2} = \frac12.$$

$$\lim_{x \to 0}\frac{\tan x - x}{x^3} = \frac13, \qquad \lim_{x \to 0}\frac{\cos x - 1 + \frac{x^2}{2}}{x^4} = \frac{1}{24}.$$

**$\infty - \infty$.** Combine first, or expand. Since $\sin^2 x = x^2 - \frac{x^4}{3} + \cdots$,
$$\frac{1}{\sin^2x} = \frac{1}{x^2}\left(1 - \frac{x^2}{3} + \cdots\right)^{-1} = \frac{1}{x^2} + \frac13 + \cdots, \quad\text{so}\quad \lim_{x \to 0}\left(\frac{1}{x^2} - \frac{1}{\sin^2x}\right) = -\frac13.$$

**Exponent forms.** $(1 + x)^{1/x} = \exp\!\left(\frac{\log(1 + x)}{x}\right) = \exp\!\left(1 - \frac{x}{2} + \frac{x^2}{3} - \cdots\right) = e\left(1 - \frac{x}{2} + \cdots\right)$. Hence
$$\lim_{x \to 0}\frac{e - (1 + x)^{1/x}}{x} = \frac{e}{2}.$$

:::exam-tip
Stop expanding at the **first power that survives** in the denominator. If the denominator is $x^3$, keep every term up to $x^3$ in the numerator, and check that lower powers cancel. If they don't, the limit is infinite.
:::

## Error estimates {#error-estimates}

The Lagrange remainder gives a **guaranteed** bound once you bound $f^{(n+1)}$ between $0$ and $x$.

**How many terms for $e$?** With $x = 1$,
$$e - \sum_{k=0}^{n}\frac{1}{k!} = \frac{e^{\theta}}{(n+1)!}, \qquad 0 < \frac{e^\theta}{(n+1)!} < \frac{3}{(n+1)!}.$$

To guarantee an error below $10^{-3}$ we need $(n+1)! > 3000$. Since $6! = 720$ and $7! = 5040$, the smallest is $n + 1 = 7$, i.e. $n = 6$: **seven terms** $1 + 1 + \frac1{2!} + \cdots + \frac1{6!} = 2.71806$. The true error is $0.00023$; with $n = 5$ it is $0.0016$, too large.

For **3 correct decimal places** (error $< 0.0005$) the bound needs $(n+1)! > 6000$, so $n = 7$ (eight terms), although $n = 6$ happens to suffice in fact. State the tolerance before counting terms.

**Using a zero term.** For $\sin x$, the $x^4$ coefficient is $0$, so $x - \frac{x^3}{6}$ is also the degree-4 Taylor polynomial. The Lagrange remainder after the $x^4$ term gives
$$\left|\sin x - x + \frac{x^3}{6}\right| = \left|\frac{x^5}{5!}\cos\theta x\right| \le \frac{|x|^5}{120}.$$

At $x = 0.1$ this is $8.3 \times 10^{-8}$, far better than the $\frac{|x|^4}{24} \approx 4.2 \times 10^{-6}$ from stopping at the $x^3$ term.

**Alternating series shortcut.** For an alternating series whose terms decrease to $0$ (such as $\sin x$, $\cos x$ for small $x$, or $\log(1 + x)$ for $0 < x \le 1$), the error is at most the first omitted term, and has its sign.

:::caution
$\log 2 = 1 - \frac12 + \frac13 - \cdots$ converges very slowly: for error below $10^{-3}$ the alternating bound needs about $1000$ terms. Use $\log 2 = \log\frac{1 + 1/3}{1 - 1/3} = 2\left(\frac13 + \frac{1}{3\cdot 27} + \cdots\right)$ instead.
:::

## Quick checks and traps {#exam-tips}

- **Hypotheses:** for the remainder after the $h^n$ term you need $f^{(n)}$ **continuous on the closed** interval and $f^{(n+1)}$ to **exist on the open** interval. No continuity of $f^{(n+1)}$ is required.
- **Lagrange vs Cauchy:** $\frac{h^{n+1}}{(n+1)!}$ versus $\frac{h^{n+1}(1 - \theta)^n}{n!}$. The $\theta$ values differ.
- **Ranges:** $e^x, a^x, \sin x, \cos x$: all $x$. $\log(1 + x)$: $(-1, 1]$. $\tan^{-1}x$: $[-1, 1]$. $(1 + x)^m$: $(-1, 1)$ plus endpoints depending on $m$.
- **Coefficient check at $x = 0$:** the constant term must equal $f(0)$ and the linear term $f'(0)$. This kills many distractors instantly.
- **Parity:** odd functions ($\sin$, $\tan$, $\tan^{-1}$) have only odd powers; even functions ($\cos$, $\log\cos x$) only even powers.
- **$f^{(n)}(0) = n!\,c_n$:** read derivatives at $0$ off the series.
- **$e^{-1/x^2}$:** $C^\infty$, all derivatives $0$ at $0$, Maclaurin series $\equiv 0$, not analytic.
- **Convergent is not enough:** the series must converge **to $f$**, i.e. $R_n \to 0$.
- **Limits:** $\frac{x - \sin x}{x^3} \to \frac16$, $\frac{\tan x - x}{x^3} \to \frac13$, $\frac{e^x - 1 - x}{x^2} \to \frac12$. Expand only up to the power in the denominator.
- **Error counts:** fix the tolerance first ($10^{-3}$ versus "3 decimal places" changes the answer for $e$ from $n = 6$ to $n = 7$ by the Lagrange bound).
