# Limits and Continuity

## Limit of a function {#limit-definition}

Let $f$ be defined on a set $D \subseteq \R$ and let $c$ be a **limit point** of $D$ ($f$ need not be defined at $c$).

**Cauchy (ε–δ) definition.** $\lim_{x\to c} f(x) = \ell$ means: for every $\varepsilon > 0$ there is $\delta > 0$ such that

$$0 < |x - c| < \delta,\ x \in D \implies |f(x) - \ell| < \varepsilon.$$

The condition $0 < |x - c|$ means the value $f(c)$ plays **no part** in the limit.

**Heine (sequential) definition.** $\lim_{x\to c} f(x) = \ell$ means: for **every** sequence $(x_n)$ in $D$ with $x_n \ne c$ and $x_n \to c$, we have $f(x_n) \to \ell$.

The two definitions are **equivalent** (the proof of "Cauchy ⇐ Heine" uses $\delta = 1/n$ and contradiction).

**Using Heine to show a limit does not exist.** Find two sequences $x_n \to c$ and $y_n \to c$ (avoiding $c$) with $\lim f(x_n) \ne \lim f(y_n)$, or one sequence with $f(x_n)$ divergent. For $\sin(1/x)$ at $0$:

$$x_n = \frac{1}{n\pi} \Rightarrow \sin\frac{1}{x_n} = 0, \qquad y_n = \frac{2}{(4n + 1)\pi} \Rightarrow \sin\frac{1}{y_n} = \sin\left(2n\pi + \frac{\pi}{2}\right) = 1.$$

So $\lim_{x\to 0}\sin(1/x)$ does not exist.

**One-sided limits.** $f(c+) = \lim_{x\to c+} f(x)$ uses only $c < x < c + \delta$; $f(c-)$ uses $c - \delta < x < c$. Then

$$\lim_{x\to c} f(x) = \ell \iff f(c-) \text{ and } f(c+) \text{ both exist and equal } \ell.$$

For the floor function $[x]$ (greatest integer $\le x$) at an integer $n$: $[n-] = n - 1$ and $[n+] = n$, so $\lim_{x\to n}[x]$ does not exist.

**Limits at infinity** and **infinite limits** are defined the same way: $\lim_{x\to\infty} f(x) = \ell$ if for every $\varepsilon > 0$ there is $K$ with $x > K \Rightarrow |f(x) - \ell| < \varepsilon$; $\lim_{x\to c} f(x) = \infty$ if for every $G$ there is $\delta$ with $0 < |x - c| < \delta \Rightarrow f(x) > G$. An infinite limit is **not** a limit in the sense of "the limit exists".

**A typical ε–δ proof.** Prove $\lim_{x\to 3} x^2 = 9$. We have $|x^2 - 9| = |x - 3|\,|x + 3|$. First restrict to $|x - 3| < 1$, so $2 < x < 4$ and $|x + 3| < 7$. Then $|x^2 - 9| < 7|x - 3|$, and

$$\delta = \min\left\{1, \frac{\varepsilon}{7}\right\}$$

works for every $\varepsilon > 0$.

:::caution
$\delta = \varepsilon/7$ alone is **not** enough: for large $\varepsilon$ the bound $|x + 3| < 7$ is no longer guaranteed. The "$\min\{1, \cdot\}$" is what makes the proof valid.
:::

## Algebra of limits and the sandwich rule {#algebra-sandwich}

If $\lim_{x\to c} f = \ell$ and $\lim_{x\to c} g = m$ (both **finite**), then

$$\lim (f \pm g) = \ell \pm m, \qquad \lim fg = \ell m, \qquad \lim \frac{f}{g} = \frac{\ell}{m}\ (m \ne 0), \qquad \lim |f| = |\ell|.$$

These follow from the sequence versions through the Heine definition.

- The **converses fail.** $\lim(f + g)$ may exist when neither $\lim f$ nor $\lim g$ does: $f = \sin(1/x)$, $g = -\sin(1/x)$.
- **Order is preserved:** if $f(x) \le g(x)$ near $c$, then $\ell \le m$. Strict inequality is **not** preserved: $x^2 > 0$ for $x \ne 0$, but the limit is $0$.
- **Local sign:** if $\ell > 0$, then $f(x) > 0$ in some deleted neighbourhood of $c$.
- **Local boundedness:** if $\lim_{x\to c} f$ exists (finite), $f$ is bounded in some deleted neighbourhood of $c$.

**Sandwich (squeeze) rule.** If $g(x) \le f(x) \le h(x)$ in a deleted neighbourhood of $c$ and $\lim g = \lim h = \ell$, then $\lim f = \ell$.

The most used corollary: **bounded × (tends to 0) → 0.** If $|g(x)| \le M$ near $c$ and $f(x) \to 0$, then $f(x)g(x) \to 0$. So

$$-|x| \le x\sin\frac1x \le |x| \implies \lim_{x\to 0} x\sin\frac1x = 0,$$

even though $\lim_{x\to 0}\sin(1/x)$ does not exist. The product rule cannot be used here, since one factor has no limit.

```plot
title: Sandwich rule: $x\sin(1/x)$ is trapped between $-|x|$ and $|x|$
x: -0.5, 0.5
y: -0.5, 0.5
f: x*sin(1/x) | $x\sin(1/x)$
f: abs(x) | $|x|$
f: -abs(x) | $-|x|$
```

**Limit of a composite.** If $\lim_{x\to c} f(x) = L$ and $g$ is **continuous at $L$**, then $\lim_{x\to c} g(f(x)) = g(L)$. If $g$ merely has a limit at $L$, this can fail. Take $f \equiv 0$ and $g(y) = 0$ for $y \ne 0$, $g(0) = 1$. Then $\lim_{y\to 0} g(y) = 0$, but $g(f(x)) = 1$ for all $x$.

:::exam-tip
For limits like $\lim_{x\to\infty}\frac{\sin x}{x}$ or $\lim_{x\to 0} x^2\cos\frac{1}{x^3}$, the answer is $0$ by "bounded × null". Do not try L'Hospital's rule on them.
:::

## Standard limits {#standard-limits}

Here $\log$ is the natural logarithm and $a > 0$.

| Limit | Value | Idea |
|:---|:---:|:---|
| $\lim_{x\to 0}\dfrac{\sin x}{x}$ | $1$ | $\sin x < x < \tan x$ on $(0, \frac{\pi}{2})$, then sandwich |
| $\lim_{x\to 0}\dfrac{1 - \cos x}{x^2}$ | $\tfrac12$ | $1 - \cos x = 2\sin^2\frac{x}{2}$ |
| $\lim_{x\to 0}\dfrac{\tan x}{x}$ | $1$ | $\frac{\sin x}{x}\cdot\frac{1}{\cos x}$ |
| $\lim_{x\to 0}\dfrac{\log(1 + x)}{x}$ | $1$ | $\log(1 + x)^{1/x} \to \log e$ |
| $\lim_{x\to 0}\dfrac{e^x - 1}{x}$ | $1$ | put $e^x - 1 = t$ in the previous line |
| $\lim_{x\to 0}\dfrac{a^x - 1}{x}$ | $\log a$ | $a^x = e^{x\log a}$ |
| $\lim_{x\to 0}(1 + x)^{1/x}$ | $e$ | from $(1 + 1/n)^n \to e$ |
| $\lim_{x\to\infty}\left(1 + \dfrac{a}{x}\right)^{x}$ | $e^{a}$ | for any real $a$ |

These are proved from the definition of $e$ as $\lim (1 + 1/n)^n$ (the sequences topic) and the continuity of $\log$ and $\exp$.

**Working rule.** Scale the variable so a standard form appears:

$$\lim_{x\to 0}\frac{\log(1 + 2x)}{\sin 5x} = \lim\frac{\log(1 + 2x)}{2x}\cdot\frac{5x}{\sin 5x}\cdot\frac{2}{5} = \frac25.$$

$$\lim_{x\to 0}\frac{3^x - 2^x}{x} = \lim\frac{3^x - 1}{x} - \lim\frac{2^x - 1}{x} = \log 3 - \log 2 = \log\frac32.$$

**The $1^\infty$ form.** If $f(x) \to 1$ and $g(x) \to \infty$, then

$$\lim f(x)^{g(x)} = e^{\lim g(x)\,(f(x) - 1)},$$

provided the last limit exists. For example:

$$\lim_{x\to 0}(\cos x)^{1/x^2} = e^{\lim (\cos x - 1)/x^2} = e^{-1/2}, \qquad \lim_{x\to\infty}\left(1 + \frac{2}{x}\right)^{3x} = e^{6}.$$

:::caution
$\lim_{x\to 0}(1 + x)^{1/x} = e$, but $\lim_{x\to\infty}(1 + x)^{1/x} = 1$ and $\lim_{x\to 0}\frac{\sin x}{x} = 1$ while $\lim_{x\to\infty}\frac{\sin x}{x} = 0$. Read where $x$ tends before using a table entry.
:::

## Continuity {#continuity}

**At a point.** $f$ is continuous at $c \in D$ if for every $\varepsilon > 0$ there is $\delta > 0$ with

$$|x - c| < \delta,\ x \in D \implies |f(x) - f(c)| < \varepsilon.$$

Equivalently (Heine): $x_n \to c$ in $D$ implies $f(x_n) \to f(c)$. When $c$ is a limit point of $D$, this says

$$\lim_{x\to c} f(x) = f(c),$$

that is, three things: $f(c)$ is defined, the limit exists, and they are equal. A function is automatically continuous at an isolated point of its domain.

**One-sided continuity.** $f$ is right-continuous at $c$ if $f(c+) = f(c)$. Continuity at $c$ ⇔ left- and right-continuity at $c$.

**On an interval.** $f$ is continuous on $(a, b)$ if it is continuous at every point. It is continuous on $[a, b]$ if it is continuous on $(a, b)$, right-continuous at $a$ and left-continuous at $b$.

**Algebra and composition.**
- Sums, differences, products, quotients (where the denominator $\ne 0$) and $|f|$ of continuous functions are continuous.
- Polynomials, rational functions (off their poles), $\sin$, $\cos$, $e^x$, $\log x$ ($x > 0$) and $x^r$ are continuous on their domains.
- **Composite:** if $f$ is continuous at $c$ and $g$ is continuous at $f(c)$, then $g \circ f$ is continuous at $c$.
- $|f|$ continuous does **not** imply $f$ continuous: take $f = 1$ on $\Q$ and $-1$ off $\Q$.

**Finding constants for continuity.** Equate the value at the break point with each one-sided limit.

*Example.* $f(x) = \dfrac{1 - \cos 2x}{x^2}$ for $x \ne 0$ and $f(0) = k$. Since $1 - \cos 2x = 2\sin^2 x$,

$$\lim_{x\to 0} f(x) = 2\lim\left(\frac{\sin x}{x}\right)^2 = 2, \qquad \text{so } k = 2.$$

*Example.* $f(x) = x^2 + a$ for $x < 1$, $f(1) = 3$, $f(x) = bx + 1$ for $x > 1$. Then $f(1-) = 1 + a$ and $f(1+) = b + 1$. Continuity at $1$ needs $1 + a = 3 = b + 1$, so $a = 2$ and $b = 2$.

:::exam-tip
A continuous function on an interval that takes only rational values (or only integer values) is **constant**. This follows from the intermediate value property, below.
:::

## Types of discontinuity {#discontinuities}

Suppose $f$ is not continuous at $c$ (with $c$ a limit point of the domain). The standard classification:

| Type | Condition | Example at $0$ (or $n$) |
|:---|:---|:---|
| **Removable** | $\lim_{x\to c} f$ exists, but $f(c)$ is undefined or $\ne$ the limit | $\frac{\sin x}{x}$; $[x] + [-x]$ at an integer |
| **Jump** (first kind) | $f(c-)$, $f(c+)$ both exist (finite) and $f(c-) \ne f(c+)$ | $[x]$ at an integer; $\operatorname{sgn} x$ |
| **Second kind** | at least one of $f(c-)$, $f(c+)$ does not exist | $\sin\frac1x$; $\frac1x$; $e^{1/x}$ (left limit $0$, right $\infty$) |

A removable discontinuity is "removed" by redefining $f(c)$ as the limit. A jump cannot be removed.

:::caution
Books differ on whether a removable discontinuity also counts as "of the first kind". Questions here keep the three labels **removable**, **jump** and **second kind** separate.
:::

```plot
title: A jump at $x = 1$: $f(x) = x^2$ for $x < 1$, $f(x) = x + 1$ for $x \ge 1$
x: -1, 2.5
y: -0.5, 4
f: x^2 + 0*sqrt(1 - x) | $x^2$ for $x < 1$
f: x + 1 + 0*sqrt(x - 1) | $x + 1$ for $x \ge 1$
point: 1, 1 | $f(1-) = 1$ (not attained)
point: 1, 2 | $f(1) = f(1+) = 2$
vline: 1
```

**The standard examples.**
- $\sin(1/x)$ (any value at $0$): oscillates between $-1$ and $1$; neither one-sided limit exists. **Second kind.**
- $x\sin(1/x)$ with $f(0) = 0$: **continuous** at $0$ (sandwich). With $f(0) = 1$, the discontinuity is **removable**.
- $[x]$: continuous at non-integers; a **jump** of size $1$ at each integer. $[x] + [-x]$ equals $0$ at integers and $-1$ elsewhere, so it has a **removable** discontinuity at each integer.
- **Dirichlet function** $D(x) = 1$ ($x \in \Q$), $0$ ($x \notin \Q$): every interval contains rationals and irrationals, so no limit exists anywhere. **Discontinuous at every point**, all of the second kind.
- $x D(x)$, or $f(x) = x$ on $\Q$ and $0$ off $\Q$: continuous **only at $0$**. Similarly, $f(x) = x$ on $\Q$ and $1 - x$ off $\Q$ is continuous only where $x = 1 - x$, i.e. at $x = \tfrac12$.
- **Thomae function** (brief): $T(p/q) = 1/q$ for $p/q$ in lowest terms with $q > 0$, and $T(x) = 0$ for irrational $x$. Since only finitely many $q$ give $1/q \ge \varepsilon$ in a bounded interval, $\lim_{x\to c} T(x) = 0$ at **every** $c$. So $T$ is continuous at every irrational and has a removable discontinuity at every rational.

**Monotone functions.** If $f$ is monotone on $(a, b)$, then $f(c-)$ and $f(c+)$ exist at every point. Its discontinuities are therefore all **jumps**, and there are at most **countably many**.

## Continuous functions on a closed bounded interval {#closed-interval}

Let $f$ be **continuous on the closed bounded interval $[a, b]$**. Then:

1. **Boundedness.** $f$ is bounded on $[a, b]$.
2. **Extreme values.** $f$ attains its supremum and infimum: there are $p, q \in [a, b]$ with $f(p) = \sup f$ and $f(q) = \inf f$.
3. **Intermediate value property (IVT).** If $f(a) \ne f(b)$, then $f$ takes every value between $f(a)$ and $f(b)$ at some point of $(a, b)$.
4. **Bolzano's theorem** (root location). If $f(a)\,f(b) < 0$, there is $c \in (a, b)$ with $f(c) = 0$.
5. Hence $f([a, b]) = [m, M]$, where $m = \min f$ and $M = \max f$. The continuous image of a closed bounded interval is a closed bounded interval.

**Every hypothesis matters.**

| Drop | Counterexample |
|:---|:---|
| closed | $\frac1x$ on $(0, 1]$: continuous, unbounded |
| bounded | $x$ on $[0, \infty)$: unbounded |
| closed | $x$ on $(0, 1)$: bounded, but no max or min attained |
| continuity | $f(x) = \frac1x$ on $(0, 1]$, $f(0) = 0$: unbounded on $[0, 1]$ |
| continuity (IVT) | $\operatorname{sgn} x$ on $[-1, 1]$ never takes the value $\frac12$ |

**Fixed-point corollary.** If $f\colon [0, 1] \to [0, 1]$ is continuous, then $f(c) = c$ for some $c$. Apply Bolzano to $g(x) = f(x) - x$: $g(0) \ge 0$ and $g(1) \le 0$.

**Locating roots.** Evaluate at integer points and look for a sign change.

*Example.* $p(x) = x^3 - x - 1$: $p(1) = -1 < 0$ and $p(2) = 5 > 0$, so there is a root in $(1, 2)$. (Halving the interval repeatedly is the bisection method.) Similarly $x^3 - 3x + 1$ has $p(0) = 1$, $p(1) = -1$, giving a root in $(0, 1)$.

*Example.* Every real polynomial of **odd** degree has a real root: $p(x) \to \pm\infty$ with opposite signs as $x \to \pm\infty$.

:::caution
The IVT has **no converse**. A function with the intermediate value property need not be continuous: $\sin(1/x)$ with $f(0) = 0$ has the property on $[-1, 1]$ but is discontinuous at $0$. (Derivatives also have it, by Darboux's theorem.)
:::

## Inverse of a strictly monotone continuous function {#inverse-functions}

**Theorem.** Let $f$ be **strictly increasing and continuous** on an interval $I$. Then:

- $J = f(I)$ is an interval (by the IVT);
- $f\colon I \to J$ is a bijection, so $f^{-1}\colon J \to I$ exists;
- $f^{-1}$ is **strictly increasing** and **continuous** on $J$.

The same holds with "decreasing" throughout.

**Why $f^{-1}$ is continuous.** $f^{-1}$ is monotone, so its only possible discontinuities are jumps. A jump would leave a gap in its range. But its range is the whole interval $I$, so there is no gap.

**Converse.** A continuous **injective** function on an interval is strictly monotone. Combined with the theorem: a continuous bijection between intervals has a continuous inverse.

**Applications.**
- $\sin$ is strictly increasing and continuous on $[-\frac{\pi}{2}, \frac{\pi}{2}]$, so $\sin^{-1}\colon [-1, 1] \to [-\frac{\pi}{2}, \frac{\pi}{2}]$ is continuous. Likewise $\log = \exp^{-1}$ and $x^{1/n}$.
- $f(x) = x^5 + x$ is strictly increasing and continuous on $\R$, and $f(x) \to \pm\infty$ as $x \to \pm\infty$. So $f^{-1}$ exists on all of $\R$ and is continuous, even though no formula for it is available. For example, $f^{-1}(2) = 1$.

:::caution
The interval matters. On $[0, 1) \cup [2, 3]$, the function $f(x) = x$ for $x < 1$ and $f(x) = x - 1$ for $x \ge 2$ is continuous, strictly increasing and a bijection onto $[0, 2]$. But $f^{-1}$ jumps from near $1$ to $2$ at the value $1$.
:::

**Uniform continuity (mention only).** $f$ is uniformly continuous on $D$ if one $\delta$ works for all points of $D$ at once. On a closed bounded interval, continuity implies uniform continuity. $\frac1x$ on $(0, 1)$ and $x^2$ on $\R$ are continuous but not uniformly continuous. Details are in the topic *Uniform Continuity*.

## Quick checks and traps {#exam-tips}

- **The value at $c$ is irrelevant to the limit.** Change $f(c)$ and $\lim_{x\to c} f$ does not change; continuity may.
- **Bounded × null → 0:** $x\sin\frac1x$, $x^2\cos\frac1x$, $\frac{\sin x}{x}$ as $x \to \infty$ all tend to $0$.
- **Scale to a standard form:** $\frac{\sin ax}{bx} \to \frac{a}{b}$, $\frac{e^{ax} - 1}{x} \to a$, $\frac{\log(1 + ax)}{x} \to a$, $(1 + ax)^{1/x} \to e^{a}$.
- **$1^\infty$:** $\lim f^g = e^{\lim g(f - 1)}$. Check: $(1 + \sin x)^{\cot x} \to e^{\lim \cot x\sin x} = e$.
- **Floor function:** $\lim_{x\to n-}[x] = n - 1$, $\lim_{x\to n+}[x] = n$. A jump of size $1$.
- **Classify by one-sided limits:** both exist and are equal → removable (or continuous); both exist and differ → jump; one fails → second kind.
- **Rational/irrational definitions:** a function equal to $g$ on $\Q$ and $h$ off $\Q$ ($g$, $h$ continuous) is continuous exactly where $g(x) = h(x)$.
- **Closed bounded interval** is essential for boundedness and attained bounds; $\frac1x$ on $(0, 1]$ fails.
- **IVT for roots:** a sign change of a continuous $f$ on $[a, b]$ gives a root in $(a, b)$; no sign change does not prove there is no root.
- **Continuous injective on an interval ⇒ strictly monotone ⇒ continuous inverse.**
