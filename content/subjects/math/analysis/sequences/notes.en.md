# Sequences

## Bounds, limits and divergence {#limit-definition}

A **sequence** of reals is a function $a : \N \to \R$, written $(a_n)$. Here $\N = \{1, 2, 3, \dots\}$. The **range** $\{a_n : n \in \N\}$ is a set; the sequence keeps order and repetition. $(-1)^n$ has range $\{-1, 1\}$ but infinitely many terms.

**Bounds.** $(a_n)$ is bounded above if $a_n \le K$ for all $n$, bounded below if $a_n \ge k$ for all $n$, and **bounded** if both hold, i.e. $|a_n| \le M$ for some $M$. The supremum and infimum of the range are the least upper and greatest lower bounds; they need not be terms. For $a_n = \frac{n}{n+1}$: $\inf = \frac12$ (attained at $n = 1$), $\sup = 1$ (not attained).

**Limit (ε–N).** $a_n \to l$ means
$$\forall \varepsilon > 0\ \exists N \in \N:\ |a_n - l| < \varepsilon \text{ for all } n \ge N.$$
Every neighbourhood of $l$ contains all but finitely many terms.

*Example.* $a_n = \frac{n+1}{n}$: $|a_n - 1| = \frac1n < \varepsilon \iff n > \frac1\varepsilon$. For $\varepsilon = \frac{1}{100}$ the least valid $N$ is $101$.

**Basic theorems.**
- **Uniqueness:** a sequence has at most one limit. If $l \ne l'$, take $\varepsilon = \frac{|l - l'|}{2}$; the two neighbourhoods are disjoint.
- **Convergent $\Rightarrow$ bounded:** with $\varepsilon = 1$, $|a_n| \le \max\{|a_1|, \dots, |a_{N-1}|, |l| + 1\}$.
- The **converse fails**: $(-1)^n$ is bounded but not convergent.
- Changing, adding or deleting finitely many terms does not affect convergence or the limit.

**Divergence and oscillation.**
- $a_n \to +\infty$ if $\forall G > 0\ \exists N:\ a_n > G$ for $n \ge N$. Similarly $a_n \to -\infty$.
- A sequence that neither converges nor tends to $\pm\infty$ **oscillates**: *finitely* if bounded ($(-1)^n$, $\sin\frac{n\pi}{2}$), *infinitely* if unbounded ($(-1)^n n$).

| Sequence | Behaviour |
|:---|:---|
| $\frac1n$, $\frac{(-1)^n}{n}$ | converges to $0$ |
| $n^2$, $\sqrt n$ | diverges to $+\infty$ |
| $(-1)^n$, $1 + (-1)^n$ | oscillates finitely |
| $(-1)^n n$ | oscillates infinitely |

:::caution
Indian texts (Mapa, Das–Mukherjee) reserve "divergent" for $\to \pm\infty$ and call the rest "oscillatory". Many Western books call every non-convergent sequence divergent. Read the stem's wording. An unbounded sequence need **not** tend to $\pm\infty$: $(-1)^n n$ does not.
:::

## Algebra of limits and the sandwich rule {#limit-algebra}

If $a_n \to a$ and $b_n \to b$ (finite), then
$$a_n \pm b_n \to a \pm b,\quad a_n b_n \to ab,\quad c\,a_n \to ca,\quad \frac{a_n}{b_n} \to \frac ab \ (b \ne 0,\ b_n \ne 0),\quad |a_n| \to |a|.$$

Further facts:
- **Order is preserved weakly.** If $a_n \le b_n$ eventually, then $a \le b$. Strict inequality is *not* preserved: $\frac1n > 0$ but the limit is $0$.
- **Null times bounded is null.** If $a_n \to 0$ and $(b_n)$ is bounded, then $a_n b_n \to 0$. Example: $\frac{\sin n}{n} \to 0$.
- If $a_n \to a$ and $a_n + b_n$ converges, then $b_n = (a_n + b_n) - a_n$ converges.
- The product rule cannot be reversed: $a_n = \frac1n$, $b_n = n$ gives $a_n b_n = 1$ convergent with $b_n$ divergent.
- $|a_n| \to |a|$ does **not** give $a_n \to a$: $(-1)^n$. But $|a_n| \to 0 \iff a_n \to 0$.

**Sandwich (squeeze) rule.** If $a_n \le c_n \le b_n$ for $n \ge N$ and $a_n \to l$, $b_n \to l$, then $c_n \to l$.

*Example.* $c_n = \sum_{k=1}^{n} \frac{1}{\sqrt{n^2 + k}}$. Each of the $n$ terms lies between $\frac{1}{\sqrt{n^2 + n}}$ and $\frac{1}{\sqrt{n^2 + 1}}$, so
$$\frac{n}{\sqrt{n^2 + n}} \le c_n \le \frac{n}{\sqrt{n^2 + 1}},$$
and both bounds $\to 1$. Hence $c_n \to 1$.

*Example.* $(2^n + 3^n)^{1/n}$: since $3^n \le 2^n + 3^n \le 2\cdot 3^n$, we get $3 \le c_n \le 3\cdot 2^{1/n} \to 3$. In general $(a_1^n + \cdots + a_k^n)^{1/n} \to \max a_i$ for $a_i > 0$.

**Rationalising.** $\sqrt{n^2 + n} - n = \dfrac{n}{\sqrt{n^2 + n} + n} \to \dfrac12$.

:::exam-tip
For a ratio of polynomials in $n$, divide by the highest power in the denominator: the limit is the ratio of leading coefficients if the degrees are equal, $0$ if the top has lower degree, and $\pm\infty$ if it has higher degree.
:::

## Monotone sequences and the number e {#monotone-e}

$(a_n)$ is **monotone increasing** if $a_{n+1} \ge a_n$ for all $n$ (strictly if $>$), and **monotone decreasing** if $a_{n+1} \le a_n$.

**Monotone convergence theorem.** A monotone increasing sequence bounded above converges to $\sup_n a_n$. A monotone decreasing sequence bounded below converges to $\inf_n a_n$. An unbounded increasing sequence tends to $+\infty$.

So **a monotone sequence converges iff it is bounded.** The proof uses the completeness (LUB) axiom: given $\varepsilon$, $s - \varepsilon$ is not an upper bound, so some $a_N > s - \varepsilon$, and monotonicity keeps all later terms in $(s - \varepsilon, s]$. In $\Q$ this fails: the decimal truncations of $\sqrt2$ are increasing and bounded but have no rational limit.

**The number $e$.** Let $a_n = \left(1 + \frac1n\right)^n$. By the binomial theorem,
$$a_n = 1 + 1 + \frac{1}{2!}\Big(1 - \frac1n\Big) + \frac{1}{3!}\Big(1 - \frac1n\Big)\Big(1 - \frac2n\Big) + \cdots.$$
- Passing from $n$ to $n + 1$ increases each bracket and adds a positive term, so $(a_n)$ is **strictly increasing**.
- Each bracket is $< 1$ and $\frac{1}{k!} \le \frac{1}{2^{k-1}}$, so $a_n < 1 + \left(1 + \frac12 + \frac14 + \cdots\right) = 3$.

Hence $(a_n)$ converges; its limit is **defined** to be $e$, with $2 \le e \le 3$ ($e \approx 2.71828$). Also $e = \sum_{k \ge 0} \frac{1}{k!}$, and $e$ is irrational.

```plot
title: The terms $\left(1 + \frac1n\right)^n$ increase towards $e$
x: 0, 12
y: 1.8, 3
point: 1, 2
point: 2, (3/2)^2
point: 3, (4/3)^3
point: 4, (5/4)^4
point: 5, (6/5)^5
point: 6, (7/6)^6
point: 7, (8/7)^7
point: 8, (9/8)^8
point: 9, (10/9)^9
point: 10, (11/10)^10
point: 11, (12/11)^11
hline: e | $y = e$
hline: 3 | bound $3$
xlabel: n
```

**Consequences.** $\left(1 + \frac xn\right)^n \to e^x$ for every real $x$. So $\left(1 - \frac1n\right)^n \to e^{-1}$, $\left(1 + \frac1n\right)^{2n} \to e^2$, $\left(1 + \frac{1}{2n}\right)^n \to \sqrt e$. Also $b_n = \left(1 + \frac1n\right)^{n+1}$ decreases to $e$, so $a_n < e < b_n$.

:::caution
$\left(1 + \frac1n\right)^n \to e$, not $1$. "$1^\infty$" is indeterminate: the base tends to $1$ but the exponent grows.
:::

## Nested intervals and Cauchy's general principle {#nested-cauchy}

**Nested interval theorem.** Let $I_n = [a_n, b_n]$ be **closed and bounded** intervals with $I_1 \supseteq I_2 \supseteq \cdots$. Then $\bigcap_n I_n \ne \emptyset$. If also $b_n - a_n \to 0$, the intersection is exactly one point.

The proof: $(a_n)$ increases, $(b_n)$ decreases, and every $a_m \le b_n$. So $\sup a_n \le \inf b_n$, and every point between them lies in all $I_n$.

Both hypotheses matter:
- **Closed:** $\bigcap_n \left(0, \frac1n\right) = \emptyset$ (open intervals).
- **Bounded:** $\bigcap_n [n, \infty) = \emptyset$ (closed but unbounded).

Contrast: $\bigcap_n \left[-\frac1n, \frac1n\right] = \{0\}$ and $\bigcap_n \left[0, \frac1n\right] = \{0\}$.

**Cauchy sequence.** $(a_n)$ is Cauchy if
$$\forall \varepsilon > 0\ \exists N:\ |a_m - a_n| < \varepsilon \text{ for all } m, n \ge N.$$
The terms get close to **each other**; no limit is mentioned.

**Cauchy's general principle of convergence.** A sequence of reals converges **if and only if** it is Cauchy.
- Convergent $\Rightarrow$ Cauchy: $|a_m - a_n| \le |a_m - l| + |l - a_n|$.
- Cauchy $\Rightarrow$ bounded $\Rightarrow$ (Bolzano–Weierstrass) a convergent subsequence $\Rightarrow$ the whole sequence converges to the same limit.
- The converse direction is completeness of $\R$. It fails in $\Q$.

**Using it to prove divergence.** For $s_n = 1 + \frac12 + \cdots + \frac1n$:
$$s_{2n} - s_n = \frac{1}{n+1} + \cdots + \frac{1}{2n} \ge n\cdot\frac{1}{2n} = \frac12,$$
so $(s_n)$ is not Cauchy and diverges (to $+\infty$, as it increases).

**Using it to prove convergence.** For $t_n = \sum_{k=1}^{n} \frac{1}{k^2}$ and $m > n$,
$$t_m - t_n < \sum_{k=n+1}^{m} \Big(\frac{1}{k-1} - \frac1k\Big) < \frac1n,$$
so $(t_n)$ is Cauchy.

**Contractive sequences.** If $|a_{n+2} - a_{n+1}| \le k\,|a_{n+1} - a_n|$ for all $n$, with a fixed $0 < k < 1$, then $(a_n)$ is Cauchy, hence convergent.

:::caution
$|a_{n+1} - a_n| \to 0$ is **not** enough for Cauchy: $s_n = \sum_{k \le n} \frac1k$ and $\sqrt n$ both have this property and diverge.
:::

## Subsequences, Bolzano–Weierstrass, lim sup and lim inf {#subsequences}

A **subsequence** of $(a_n)$ is $(a_{n_k})$ with $n_1 < n_2 < n_3 < \cdots$ (so $n_k \ge k$).

- If $a_n \to l$, **every** subsequence tends to $l$.
- Hence: two subsequences with different limits prove divergence. For $(-1)^n$: $a_{2k} \to 1$, $a_{2k-1} \to -1$.
- If $a_{2k} \to l$ and $a_{2k-1} \to l$, then $a_n \to l$.
- **Every sequence of reals has a monotone subsequence** (the peak lemma).

**Bolzano–Weierstrass theorem (sequences).** Every **bounded** sequence of reals has a convergent subsequence. (It follows from the two facts above with the monotone convergence theorem. The set version is in Point Sets.)

**Subsequential limits.** $l$ is a *subsequential limit* (limit point of the sequence) if some subsequence tends to $l$. For a bounded sequence:
$$\limsup a_n = \overline{\lim}\, a_n = \text{greatest subsequential limit} = \lim_{n\to\infty} \sup_{k \ge n} a_k,$$
$$\liminf a_n = \underline{\lim}\, a_n = \text{least subsequential limit} = \lim_{n\to\infty} \inf_{k \ge n} a_k.$$
If $(a_n)$ is unbounded above, $\limsup a_n = +\infty$; if unbounded below, $\liminf a_n = -\infty$.

**Key facts.**
- $\liminf a_n \le \limsup a_n$, always.
- $(a_n)$ converges $\iff \liminf a_n = \limsup a_n$, finite; the common value is the limit.
- $\inf a_n \le \liminf a_n \le \limsup a_n \le \sup a_n$. The outer pair can differ from the inner pair.

| $a_n$ | $\inf$, $\sup$ | $\liminf$, $\limsup$ |
|:---|:---|:---|
| $(-1)^n\left(1 + \frac1n\right)$ | $-2$, $\frac32$ | $-1$, $1$ |
| $1 + (-1)^n$ | $0$, $2$ | $0$, $2$ |
| $\sin\frac{n\pi}{3}$ | $-\frac{\sqrt3}{2}$, $\frac{\sqrt3}{2}$ | $-\frac{\sqrt3}{2}$, $\frac{\sqrt3}{2}$ |
| $(-1)^n n$ | none, none | $-\infty$, $+\infty$ |
| $n\left(1 + (-1)^n\right)$ | $0$, none | $0$, $+\infty$ |

:::caution
Do not confuse $\sup$ with $\limsup$. In the first row the supremum $\frac32$ is attained once, at $n = 2$, but the terms only approach $1$ infinitely often. $\limsup$ ignores finitely many terms; $\sup$ does not.
:::

## Cauchy's first and second limit theorems {#cauchy-limit-theorems}

**First limit theorem (Cauchy).** If $a_n \to l$ (finite, or $\pm\infty$), then
$$\frac{a_1 + a_2 + \cdots + a_n}{n} \to l.$$
The arithmetic means converge to the same limit. The converse fails: $a_n = (-1)^n$ has means $\to 0$.

**Geometric-mean form.** If $a_n > 0$ and $a_n \to l$ (finite or $+\infty$), then $(a_1 a_2 \cdots a_n)^{1/n} \to l$. Apply the first theorem to $\log a_n$ when $l > 0$.

**Second limit theorem (Cauchy).** If $a_n > 0$ and $\dfrac{a_{n+1}}{a_n} \to l$ (finite or $+\infty$), then
$$a_n^{1/n} \to l.$$
Apply the geometric-mean form to $\frac{a_2}{a_1}, \frac{a_3}{a_2}, \dots$: their product telescopes to $\frac{a_{n+1}}{a_1}$. The converse fails: for $a_n = 2$ ($n$ odd), $1$ ($n$ even), $a_n^{1/n} \to 1$ but the ratios alternate between $\frac12$ and $2$.

**Standard applications.**

| $a_n$ | $\dfrac{a_{n+1}}{a_n}$ | so $a_n^{1/n} \to$ |
|:---|:---|:---|
| $n$ | $\frac{n+1}{n} \to 1$ | $n^{1/n} \to 1$ |
| $n!$ | $n + 1 \to \infty$ | $(n!)^{1/n} \to \infty$ |
| $\dfrac{n^n}{n!}$ | $\left(1 + \frac1n\right)^n \to e$ | $\dfrac{n}{(n!)^{1/n}} \to e$ |
| $\dfrac{(2n)!}{(n!)^2}$ | $\frac{(2n+1)(2n+2)}{(n+1)^2} \to 4$ | $4$ |

The third row gives the important limit
$$\frac{(n!)^{1/n}}{n} \to \frac1e.$$

**Applications of the first theorem.**
- $\frac1n\left(1 + \frac12 + \cdots + \frac1n\right) \to 0$, since $\frac1n \to 0$.
- $\frac1n\left(1 + 2^{1/2} + 3^{1/3} + \cdots + n^{1/n}\right) \to 1$, since $n^{1/n} \to 1$.
- If $a_n \to l$, then $\dfrac{a_1 + 2a_2 + \cdots + n a_n}{n^2} \to \dfrac l2$. (Stolz–Cesàro: the ratio of differences is $\frac{n a_n}{2n - 1} \to \frac l2$.)

:::exam-tip
To find $\lim a_n^{1/n}$ for a factorial or product expression, compute $\lim \frac{a_{n+1}}{a_n}$ instead; it is usually one line. Check that $a_n > 0$.
:::

## Standard limits and recursive sequences {#standard-limits}

Logarithms are natural ($\log = \ln$). Here $p > 0$, $a > 0$, and $x$ is real.

| Sequence | Limit |
|:---|:---|
| $\frac{1}{n^p}$ | $0$ |
| $x^n$ | $0$ if $\lvert x\rvert < 1$; $1$ if $x = 1$; $+\infty$ if $x > 1$; oscillates if $x \le -1$ |
| $a^{1/n}$ | $1$ |
| $n^{1/n}$ | $1$ |
| $n^p x^n$, $\lvert x\rvert < 1$ | $0$ |
| $\frac{x^n}{n!}$ | $0$ |
| $\frac{\log n}{n^p}$ | $0$ |
| $\frac{n!}{n^n}$ | $0$ |
| $\left(1 + \frac xn\right)^n$ | $e^x$ |

Growth order for large $n$: $\log n \ll n^p \ll a^n\ (a > 1) \ll n! \ll n^n$.

**Recursive sequences.** For $x_{n+1} = f(x_n)$:
1. Show $(x_n)$ is **bounded** and **monotone**, by induction.
2. Conclude it converges to some $l$.
3. Let $n \to \infty$ in the recurrence: $l = f(l)$ (for continuous $f$). Choose the root consistent with the bounds.

*Example.* $x_1 = \sqrt2$, $x_{n+1} = \sqrt{2 + x_n}$.
- Bounded: if $x_n < 2$ then $x_{n+1} < \sqrt4 = 2$.
- Increasing: $x_{n+1}^2 - x_n^2 = 2 + x_n - x_n^2 = (2 - x_n)(1 + x_n) > 0$.
- Limit: $l^2 = 2 + l$ gives $l = 2$ or $l = -1$. All terms are positive, so $l = 2$.

*Example.* $x_{n+1} = \frac12\left(x_n + \frac{a}{x_n}\right)$, $x_1 > 0$: by AM ≥ GM, $x_n \ge \sqrt a$ for $n \ge 2$, and then $(x_n)$ decreases. Limit: $\sqrt a$ (Newton's square root).

*Example.* $x_1 = 1$, $x_{n+1} = \frac{1}{1 + x_n}$. This is **not monotone**: $1, \frac12, \frac23, \frac35, \dots$ (ratios of Fibonacci numbers). The odd and even subsequences are monotone in opposite directions. Alternatively, all $x_n \ge \frac12$, so
$$|x_{n+2} - x_{n+1}| = \frac{|x_{n+1} - x_n|}{(1 + x_n)(1 + x_{n+1})} \le \frac49\,|x_{n+1} - x_n|,$$
and the sequence is contractive. The limit solves $l^2 + l - 1 = 0$, $l > 0$: $l = \frac{\sqrt5 - 1}{2}$.

:::caution
Never solve $l = f(l)$ before proving convergence. $x_{n+1} = 2x_n$, $x_1 = 1$ "gives" $l = 0$, but the sequence tends to $+\infty$.
:::

## Quick checks and traps {#exam-tips}

:::keyfacts
- Convergent $\Rightarrow$ bounded; bounded $\not\Rightarrow$ convergent; bounded **and monotone** $\Rightarrow$ convergent.
- Bounded $\Rightarrow$ has a convergent subsequence (Bolzano–Weierstrass).
- In $\R$: convergent $\iff$ Cauchy.
- Converges $\iff \liminf = \limsup$ (finite).
- $\left(1 + \frac1n\right)^n \uparrow e$, with $2 \le a_n < 3$.
- $n^{1/n} \to 1$, $\;(n!)^{1/n} \to \infty$, $\;\frac{(n!)^{1/n}}{n} \to \frac1e$.
:::

**Fast checks.**
- **Ratio of polynomials:** compare degrees and leading coefficients.
- **$1^\infty$ forms:** $\left(1 + \frac{a}{n}\right)^{bn} \to e^{ab}$.
- **$n$-th roots:** use Cauchy's second theorem, $\lim a_n^{1/n} = \lim \frac{a_{n+1}}{a_n}$, whenever the ratio limit exists.
- **Averages:** Cauchy's first theorem, $\lim \frac{a_1 + \cdots + a_n}{n} = \lim a_n$.
- **Sums of $n$ terms:** squeeze between $n\times$(smallest term) and $n\times$(largest term).
- **Sums of powers:** $(a^n + b^n)^{1/n} \to \max(a, b)$ for $a, b > 0$.

**Traps.**

| Claim | Status |
|:---|:---|
| $\lvert a_n\rvert \to \lvert l\rvert \Rightarrow a_n \to l$ | false: $(-1)^n$; true when $l = 0$ |
| $a_n b_n$ and $a_n$ converge $\Rightarrow b_n$ converges | false: $\frac1n \cdot n$ |
| $a_{n+1} - a_n \to 0 \Rightarrow$ Cauchy | false: $\sqrt n$ |
| $a_n^{1/n} \to l \Rightarrow \frac{a_{n+1}}{a_n} \to l$ | false: $2, 1, 2, 1, \dots$ |
| Means converge $\Rightarrow a_n$ converges | false: $(-1)^n$ |
| Nested **open** intervals have a common point | false: $\left(0, \frac1n\right)$ |
| Unbounded $\Rightarrow a_n \to \pm\infty$ | false: $(-1)^n n$ |
| $a_n > 0$ for all $n$, $a_n \to l \Rightarrow l > 0$ | false: $\frac1n$; only $l \ge 0$ |

:::exam-tip
"Which sequence is bounded but not convergent?" The answer is always an oscillating one such as $(-1)^n$ or $\sin\frac{n\pi}{2}$. "Which is not Cauchy?" Look for the harmonic partial sums $\sum \frac1k$ or anything unbounded.
:::

:::caution
"Increasing" in some books means strictly increasing and in others non-decreasing. A constant sequence is monotone increasing in the non-strict sense. The monotone convergence theorem holds in either sense.
:::
