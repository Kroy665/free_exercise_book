# Series of Positive Terms

## Infinite series and convergence {#convergence}

Given a real sequence $(a_n)$, the **infinite series** $\sum a_n$ is studied through its **partial sums**

$$s_n = a_1 + a_2 + \cdots + a_n.$$

$\sum a_n$ **converges** to $s$ if $s_n \to s$; then $s$ is its **sum**. Otherwise it **diverges**. A series of positive terms either converges or diverges to $+\infty$; it cannot oscillate.

:::keyfacts
- **Positive terms.** If $a_n \ge 0$, then $(s_n)$ is increasing, so $\sum a_n$ converges **iff $(s_n)$ is bounded above**. Every test in this topic comes from this fact.
- **Necessary condition.** If $\sum a_n$ converges, then $a_n = s_n - s_{n-1} \to 0$. The converse is **false**.
- **Cauchy's criterion.** $\sum a_n$ converges iff for every $\varepsilon > 0$ there is an $N$ such that
  $$\lvert a_{n+1} + a_{n+2} + \cdots + a_m\rvert < \varepsilon \quad \text{for all } m > n \ge N.$$
:::

**The harmonic series** $\sum \frac1n$ diverges although $\frac1n \to 0$. The Cauchy criterion shows it at once:

$$s_{2n} - s_n = \frac{1}{n + 1} + \cdots + \frac{1}{2n} \ge n \cdot \frac{1}{2n} = \frac12 \quad \text{for every } n.$$

So the block sums never become small, and the criterion fails with $\varepsilon = \frac12$. Equivalently, $s_{2^k} \ge 1 + \frac k2 \to \infty$.

**Simple facts.**
- Adding, removing or changing finitely many terms does not change convergence (it changes the sum).
- If $\sum a_n$ and $\sum b_n$ converge, so do $\sum (a_n + b_n)$ and $\sum c\,a_n$.
- If $\sum a_n$ converges and $\sum b_n$ diverges, then $\sum(a_n + b_n)$ diverges.
- If $a_n \ge 0$ and $\sum a_n$ converges, then $\sum a_n^2$ converges: eventually $a_n < 1$, so $a_n^2 \le a_n$.

**Telescoping.** If $a_n = b_n - b_{n+1}$, then $s_n = b_1 - b_{n+1}$. For example,

$$\sum_{n=1}^{\infty} \frac{1}{n(n + 1)} = \sum_{n=1}^{\infty}\left(\frac1n - \frac{1}{n + 1}\right) = \lim\left(1 - \frac{1}{n + 1}\right) = 1.$$

:::caution
"$a_n \to 0$" only **removes** a series from the list of obvious failures; it never proves convergence. Use it the other way: if $a_n \not\to 0$, the series diverges. For example, $\sum \left(1 + \frac1n\right)^{-n}$ diverges, because its terms tend to $\frac1e \ne 0$.
:::

:::exam-tip
"$s_{2n} - s_n \to 0$" is also only necessary. For $\sum \frac{1}{n\ln n}$ it holds (the block is about $\ln\frac{\ln 2n}{\ln n} \to 0$), yet the series diverges. Cauchy's criterion needs **all** $m > n \ge N$, not just $m = 2n$.
:::

```plot
title: Partial sums of $\sum 1/n$ grow like $\ln n$; those of $\sum 1/n^2$ level off at $\pi^2/6$
x: 0, 11
y: 0, 3.2
f: ln(x) + 0.5772 | $\ln n + \gamma$
hline: 1.6449
point: 1, 1
point: 2, 1.5
point: 3, 1.833
point: 4, 2.083
point: 5, 2.283
point: 6, 2.45
point: 7, 2.593
point: 8, 2.718
point: 9, 2.829
point: 10, 2.929 | $H_n$
point: 2, 1.25
point: 3, 1.361
point: 4, 1.424
point: 5, 1.464
point: 6, 1.491
point: 7, 1.512
point: 8, 1.527
point: 9, 1.54
point: 10, 1.55 | $\sum_{k \le n} 1/k^2$
xlabel: n
ylabel: partial sum
```

## Geometric series, p-series and condensation {#p-series}

**Geometric series.** For $r \ge 0$,

$$\sum_{n=0}^{\infty} r^n = \frac{1}{1 - r} \quad (0 \le r < 1), \qquad \text{and it diverges for } r \ge 1.$$

Mind the starting index: $\sum_{n=1}^{\infty} r^n = \dfrac{r}{1 - r}$.

**Cauchy's condensation test.** Let $(a_n)$ be **positive and decreasing**. Then

$$\sum_{n=1}^{\infty} a_n \quad \text{and} \quad \sum_{k=0}^{\infty} 2^k a_{2^k}$$

converge or diverge together.

*Proof idea.* Group terms in blocks $[2^k, 2^{k+1})$. Each block has $2^k$ terms, each between $a_{2^{k+1}}$ and $a_{2^k}$. So $\frac12\sum 2^{k+1}a_{2^{k+1}} \le \sum a_n \le \sum 2^k a_{2^k}$.

**The p-series.** For $a_n = \frac{1}{n^p}$ with $p > 0$, the condensed series is $\sum 2^k\cdot 2^{-kp} = \sum \left(2^{1-p}\right)^k$, a geometric series with ratio $2^{1-p}$. Hence:

$$\sum_{n=1}^{\infty} \frac{1}{n^p} \text{ converges} \iff p > 1.$$

For $p \le 0$ the terms do not tend to $0$. Known sums: $\sum \frac{1}{n^2} = \frac{\pi^2}{6}$ and $\sum \frac{1}{n^4} = \frac{\pi^4}{90}$.

**Logarithmic scale.** Condensing $a_n = \dfrac{1}{n(\ln n)^p}$ ($n \ge 2$, $p > 0$) gives $\sum \dfrac{2^k}{2^k (k\ln 2)^p} = \dfrac{1}{(\ln 2)^p}\sum \dfrac{1}{k^p}$. So:

| Series ($n \ge 2$) | Verdict |
|:---|:---|
| $\sum \dfrac{1}{n\ln n}$ | diverges (condensed: $\sum \frac{1}{k\ln 2}$) |
| $\sum \dfrac{1}{n(\ln n)^p}$ | converges $\iff p > 1$ |
| $\sum \dfrac{1}{(\ln n)^p}$, any $p$ | diverges ($(\ln n)^p < n$ eventually) |
| $\sum \dfrac{1}{n^{p}}$ | converges $\iff p > 1$ |

:::caution
Condensation needs $(a_n)$ **decreasing**. It also does not care about the base: with $\log_{10}$ in place of $\ln$, every verdict above is unchanged, because the two differ by a constant factor.
:::

:::exam-tip
The p-series is the yardstick for every comparison. Remember the boundary case: $p = 1$ **diverges**. So "converges iff $p \ge 1$" is always wrong.
:::

## Comparison tests {#comparison}

Let $a_n, b_n > 0$.

:::keyfacts
- **Direct comparison.** If $a_n \le k\,b_n$ for all $n \ge N$ (some $k > 0$), then $\sum b_n$ convergent $\Rightarrow$ $\sum a_n$ convergent, and $\sum a_n$ divergent $\Rightarrow$ $\sum b_n$ divergent.
- **Limit comparison.** If $\dfrac{a_n}{b_n} \to l$ with $0 < l < \infty$, then $\sum a_n$ and $\sum b_n$ converge or diverge together.
- **Edge cases.** If $\frac{a_n}{b_n} \to 0$ and $\sum b_n$ converges, then $\sum a_n$ converges. If $\frac{a_n}{b_n} \to \infty$ and $\sum b_n$ diverges, then $\sum a_n$ diverges.
:::

**Method.** Find the dominant power: $a_n \sim \dfrac{c}{n^p}$ means $n^p a_n \to c \ne 0$. Then compare with $\sum \frac{1}{n^p}$.

**Worked examples.**

1. $\displaystyle\sum \frac{2n + 3}{n^3 + 1}$: here $n^2 a_n \to 2$. Compare with $\sum \frac{1}{n^2}$: it **converges**.
2. $\displaystyle\sum \frac{1}{\sqrt{n(n + 1)}}$: here $n a_n \to 1$. Compare with $\sum \frac1n$: it **diverges**.
3. $\displaystyle\sum \frac{\sqrt{n + 1} - \sqrt n}{n}$: rationalise, $a_n = \dfrac{1}{n(\sqrt{n + 1} + \sqrt n)}$, so $n^{3/2}a_n \to \frac12$. It **converges** ($p = \frac32$).
4. $\displaystyle\sum \left(\sqrt{n + 1} - \sqrt n\right)$ **diverges**: it telescopes to $\sqrt{n + 1} - 1 \to \infty$, though its terms tend to $0$.
5. $\displaystyle\sum \sin\frac1n$ diverges, since $\dfrac{\sin(1/n)}{1/n} \to 1$. But $\sum \sin^2\frac1n$ and $\sum\left(1 - \cos\frac1n\right)$ converge (compare with $\frac{1}{n^2}$).
6. $\displaystyle\sum \left(n^{1/n} - 1\right)$ diverges: $n^{1/n} - 1 = e^{(\ln n)/n} - 1 \ge \dfrac{\ln n}{n} \ge \dfrac1n$ for $n \ge 3$.
7. $\displaystyle\sum \frac{1}{n^{1 + 1/n}}$ **diverges**: $\dfrac{a_n}{1/n} = n^{-1/n} \to 1$. Each exponent exceeds 1, but not by a fixed amount.

:::caution
Do not compare with a series whose exponent drifts towards 1. Example 7 is the classic trap: "the power is greater than 1 for every $n$" proves nothing. The p-test needs a **fixed** $p > 1$.
:::

:::exam-tip
Standard asymptotics: $\sin x \sim x$, $\tan x \sim x$, $\ln(1 + x) \sim x$, $e^x - 1 \sim x$, and $1 - \cos x \sim \frac{x^2}{2}$ as $x \to 0$. Put $x = \frac1n$ and read off $p$.
:::

## Ratio and root tests {#ratio-root}

Let $a_n > 0$.

:::keyfacts
- **D'Alembert's ratio test.** Let $\dfrac{a_{n+1}}{a_n} \to l$. If $l < 1$, $\sum a_n$ converges. If $l > 1$ (including $l = \infty$), it diverges. If $l = 1$, the test is **inconclusive**.
- **Cauchy's root test.** Let $a_n^{1/n} \to l$ (or more generally $\limsup a_n^{1/n} = l$). If $l < 1$, it converges. If $l > 1$, it diverges, since then $a_n > 1$ infinitely often. If $l = 1$, it is **inconclusive**.
:::

**$l = 1$ decides nothing.** For both $\sum \frac1n$ (divergent) and $\sum \frac{1}{n^2}$ (convergent), the ratio and the root tend to $1$. Every p-series and every rational function of $n$ gives $l = 1$, so use comparison for those.

**General forms.** Without assuming a limit:
- if $\limsup \frac{a_{n+1}}{a_n} < 1$, the series converges;
- if $\frac{a_{n+1}}{a_n} \ge 1$ for all large $n$, the terms do not decrease to $0$, so it diverges;
- $\liminf \frac{a_{n+1}}{a_n} > 1$ also gives divergence.

**The root test is stronger.** Always

$$\liminf\frac{a_{n+1}}{a_n} \le \liminf a_n^{1/n} \le \limsup a_n^{1/n} \le \limsup\frac{a_{n+1}}{a_n}.$$

So if $\frac{a_{n+1}}{a_n} \to l$, then also $a_n^{1/n} \to l$ (Cauchy's second limit theorem). The converse fails. Take $a_n = 2^{(-1)^n - n}$: the ratio alternates between $\frac18$ and $2$, so the ratio test decides nothing. But $a_n^{1/n} = 2^{(-1)^n/n - 1} \to \frac12$, so the root test gives convergence.

**Worked examples.**

- $\displaystyle\sum \frac{n!}{n^n}$: $\dfrac{a_{n+1}}{a_n} = \left(\dfrac{n}{n + 1}\right)^n = \dfrac{1}{(1 + 1/n)^n} \to \dfrac1e < 1$. It converges.
- $\displaystyle\sum \left(1 + \frac1n\right)^{-n^2}$: $a_n^{1/n} = \left(1 + \frac1n\right)^{-n} \to \frac1e < 1$. It converges. (The ratio test is awkward here; the $n^2$ in the exponent calls for the root.)
- $\displaystyle\sum \frac{n^2}{2^n}$: $a_n^{1/n} = \dfrac{(n^{1/n})^2}{2} \to \dfrac12$. It converges.
- $\displaystyle\sum \frac{x^n}{n}$, $x > 0$: the ratio is $\frac{n}{n + 1}x \to x$. It converges for $0 < x < 1$ and diverges for $x > 1$. At $x = 1$ it is the harmonic series, which diverges. So it converges iff $0 < x < 1$. (Negative $x$ belongs to the next topic.)

:::caution
**Convention.** Many Indian texts (Mapa, Das–Mukherjee) state D'Alembert's test with the reciprocal ratio: if $\frac{a_n}{a_{n+1}} \to l$, the series converges for $l > 1$ and diverges for $l < 1$. It is the same test. Read which ratio the question uses before you apply "$< 1$".
:::

## Raabe's, Gauss's and the logarithmic tests {#raabe-gauss}

When the ratio test gives $l = 1$, finer tests compare with the p-series. All three below use the reciprocal ratio $\frac{a_n}{a_{n+1}}$.

:::keyfacts
- **Raabe's test.** Let $n\left(\dfrac{a_n}{a_{n+1}} - 1\right) \to l$. If $l > 1$, $\sum a_n$ converges; if $l < 1$, it diverges; $l = 1$ is inconclusive.
- **Gauss's test.** Suppose
  $$\frac{a_n}{a_{n+1}} = \lambda + \frac{\mu}{n} + \frac{b_n}{n^{p}}, \qquad p > 1,\ (b_n) \text{ bounded}.$$
  If $\lambda > 1$ it converges; if $\lambda < 1$ it diverges. If $\lambda = 1$, it converges for $\mu > 1$ and **diverges for $\mu \le 1$**.
- **Logarithmic test.** Let $n\ln\dfrac{a_n}{a_{n+1}} \to l$. If $l > 1$ it converges; if $l < 1$ it diverges.
:::

Gauss's test settles Raabe's doubtful case $\mu = 1$: divergence. The logarithmic test is handy when $\frac{a_n}{a_{n+1}}$ contains $\left(1 + \frac1n\right)^n$, that is, when $e$ appears.

**Example (Raabe).** Let $a_n = \dfrac{1\cdot 3\cdot 5\cdots(2n - 1)}{2\cdot 4\cdot 6\cdots 2n}$. Then

$$\frac{a_n}{a_{n+1}} = \frac{2n + 2}{2n + 1}, \qquad n\left(\frac{a_n}{a_{n+1}} - 1\right) = \frac{n}{2n + 1} \to \frac12 < 1,$$

so $\sum a_n$ diverges. (In fact $a_n \sim \frac{1}{\sqrt{\pi n}}$.)

**Example (Gauss).** For $\sum a_n^{\,p}$ with the same $a_n$ and $p > 0$:

$$\frac{a_n^p}{a_{n+1}^p} = \left(1 + \frac{1}{2n + 1}\right)^p = 1 + \frac{p/2}{n} + O\!\left(\frac{1}{n^2}\right).$$

So $\lambda = 1$ and $\mu = \frac p2$. The series converges iff $p > 2$. At $p = 2$, Gauss gives divergence where Raabe is silent.

**Example (logarithmic test).** For $\sum \dfrac{n^n x^n}{n!}$, $x > 0$:

$$\frac{a_n}{a_{n+1}} = \frac{1}{x\left(1 + \frac1n\right)^n} \to \frac{1}{ex}.$$

It converges for $x < \frac1e$ and diverges for $x > \frac1e$. At $x = \frac1e$:

$$n\ln\frac{a_n}{a_{n+1}} = n\left[1 - n\ln\left(1 + \tfrac1n\right)\right] = n\left[\frac{1}{2n} - \frac{1}{3n^2} + \cdots\right] \to \frac12 < 1,$$

so it diverges. The series therefore converges iff $0 < x < \frac1e$.

:::exam-tip
With a parameter $x$, the pattern is always the same: the ratio test gives an open interval; then test the end point separately (comparison, Raabe, Gauss, or Stirling's $n! \sim \sqrt{2\pi n}\,(n/e)^n$).
:::

## Abel–Pringsheim and the integral test {#abel-pringsheim}

**Abel–Pringsheim test.** If $(a_n)$ is **positive and decreasing** and $\sum a_n$ converges, then

$$n\,a_n \to 0.$$

*Proof idea.* By Cauchy's criterion, $a_{n+1} + \cdots + a_{2n} \to 0$. Since the terms decrease, this block is at least $n\,a_{2n}$. So $2n\,a_{2n} \to 0$, and the odd indices follow similarly.

**Use (contrapositive).** If $(a_n)$ decreases and $n a_n \not\to 0$, then $\sum a_n$ diverges. For example, $\sum \frac{1}{an + b}$ ($a, b > 0$) diverges, since $n a_n \to \frac1a$.

:::caution
- The **converse is false**: for $a_n = \frac{1}{n\ln n}$, $n a_n = \frac{1}{\ln n} \to 0$, but the series diverges.
- **Monotonicity is needed.** Let $a_n = \frac1n$ when $n$ is a perfect square and $a_n = \frac{1}{n^2}$ otherwise. Then $\sum a_n \le 2\sum \frac{1}{n^2}$ converges, but $n a_n = 1$ for every square $n$, so $n a_n \not\to 0$.
- Nothing stronger such as $n^2 a_n \to 0$ is forced: $\sum \frac{1}{n^{3/2}}$ converges with $n^2 a_n = \sqrt n \to \infty$.
:::

**Integral test.** Let $f$ be **positive, continuous and decreasing** on $[1, \infty)$, and $a_n = f(n)$. Then

$$\sum_{n=1}^{\infty} f(n) \quad \text{and} \quad \int_1^{\infty} f(x)\,dx$$

converge or diverge together. Moreover $\int_1^{n+1} f \le s_n \le f(1) + \int_1^{n} f$.

```plot
title: Integral test: the rectangles of heights $1/n$ lie above the area under $1/x$
x: 0, 7
y: 0, 1.2
f: 1/x | $y = 1/x$
shade: 1/x, 1, 6
point: 1, 1
point: 2, 0.5
point: 3, 0.3333
point: 4, 0.25
point: 5, 0.2
point: 6, 0.1667
xlabel: x
ylabel: y
```

**Examples.**
- $\int_1^\infty x^{-p}\,dx$ is finite iff $p > 1$: another proof of the p-test.
- $\displaystyle\int_2^{\infty}\frac{dx}{x(\ln x)^2} = \left[-\frac{1}{\ln x}\right]_2^{\infty} = \frac{1}{\ln 2}$, so $\sum_{n\ge 2}\frac{1}{n(\ln n)^2}$ converges.
- $\displaystyle\int_2^{\infty}\frac{dx}{x\ln x} = \Big[\ln\ln x\Big]_2^{\infty} = \infty$, so $\sum \frac{1}{n\ln n}$ diverges.
- $\sum n e^{-n^2}$ converges: $\int_1^\infty x e^{-x^2}\,dx = \frac{1}{2e}$.

:::exam-tip
The integral gives a **convergence verdict**, not the sum. $\sum_{n\ge1}\frac{1}{n^2} = \frac{\pi^2}{6}$, while $\int_1^\infty \frac{dx}{x^2} = 1$.
:::

## Standard examples {#standard-examples}

| Series ($a_n > 0$) | Best test | Verdict |
|:---|:---|:---|
| $\sum \frac1n$ | Cauchy criterion, condensation | diverges |
| $\sum \frac{1}{n^p}$ | condensation, integral | converges $\iff p > 1$ |
| $\sum \frac{1}{n\ln n}$ | condensation, integral | diverges |
| $\sum \frac{1}{n(\ln n)^2}$ | condensation, integral | converges |
| $\sum \frac{n!}{n^n}$ | ratio, $l = \frac1e$ | converges |
| $\sum \frac{a^n n!}{n^n}$ | ratio, $l = \frac ae$ | converges $\iff 0 < a < e$ |
| $\sum \left(1 + \frac1n\right)^{-n^2}$ | root, $l = \frac1e$ | converges |
| $\sum \frac{x^n}{n}$, $x > 0$ | ratio, $l = x$ | converges $\iff 0 < x < 1$ |
| $\sum n^k x^n$, $x > 0$ | ratio or root, $l = x$ | converges $\iff 0 < x < 1$ |
| $\sum \frac{(n!)^2}{(2n)!}x^n$ | ratio, $l = \frac x4$ | converges $\iff 0 < x < 4$ |
| $\sum \frac{n^n x^n}{n!}$ | ratio, then logarithmic | converges $\iff 0 < x < \frac1e$ |
| $\sum \frac{1}{n^{1 + 1/n}}$ | limit comparison with $\frac1n$ | diverges |
| $\sum \left(1 + \frac1n\right)^{-n}$ | $a_n \to \frac1e \ne 0$ | diverges |

**End points with factorials.** At $a = e$ in $\sum \frac{a^n n!}{n^n}$:

$$\frac{a_{n+1}}{a_n} = \frac{e}{(1 + 1/n)^n} > 1,$$

since $(1 + \frac1n)^n < e$. So the terms increase and cannot tend to $0$: it diverges. (By Stirling, $a_n \sim \sqrt{2\pi n}$.)

Similarly, at $x = 4$ in $\sum \frac{(n!)^2}{(2n)!}x^n$, the ratio is $\frac{4(n + 1)^2}{(2n + 1)(2n + 2)} = \frac{2n + 2}{2n + 1} > 1$, so it diverges.

**A sum worth knowing.** $\displaystyle\sum_{n=0}^{\infty}\frac{1}{n!} = e$. The terms fall faster than any geometric series: the ratio is $\frac{1}{n + 1} \to 0$.

:::exam-tip
Which test? Use the shape of $a_n$:
- **factorials or $n^n$** → ratio test;
- **an $n$th power** such as $(\ldots)^{n}$ or $(\ldots)^{n^2}$ → root test;
- **rational or algebraic in $n$** → comparison with $\frac{1}{n^p}$;
- **logarithms** → condensation or the integral test;
- **ratio $\to 1$ with factorials** → Raabe or Gauss.
:::

## Quick checks and traps {#exam-tips}

- **Divergence first.** If $a_n \not\to 0$, stop: the series diverges. For example, $\sum \frac{n}{n + 1}$ and $\sum\left(1 + \frac1n\right)^{-n}$.
- **$a_n \to 0$ is not enough:** $\sum \frac1n$, $\sum\frac{1}{n\ln n}$, $\sum\left(\sqrt{n + 1} - \sqrt n\right)$ all diverge.
- **$l = 1$ in the ratio or root test decides nothing.** Switch to comparison, Raabe or Gauss.
- **"$\frac{a_{n+1}}{a_n} < 1$ for every $n$" does not give convergence.** For $\frac1n$ the ratio is $\frac{n}{n + 1} < 1$, yet it diverges. The test needs the limit (or limsup) to be **strictly less than 1**.
- **Root beats ratio.** Whenever the ratio test decides, the root test decides the same way. The root test can decide when the ratio oscillates.
- **Which ratio?** D'Alembert: $\frac{a_{n+1}}{a_n} \to l < 1$ converges; equivalently $\frac{a_n}{a_{n+1}} \to l > 1$. Raabe, Gauss and the logarithmic test use $\frac{a_n}{a_{n+1}}$, with "$> 1$ converges".
- **Abel–Pringsheim:** decreasing positive terms and convergence give $n a_n \to 0$. The converse fails ($\frac{1}{n\ln n}$).
- **Squares:** for $a_n \ge 0$, $\sum a_n$ convergent implies $\sum a_n^2$ convergent. The reverse fails: $\sum\frac{1}{n^2}$ converges, $\sum\frac1n$ does not.
- **Geometric sums:** check whether the sum starts at $n = 0$ or $n = 1$. $\sum_{n\ge1}\left(\frac23\right)^n = 2$, not $3$.
- **Sanity check by the p-scale:** any series behaving like $\frac{1}{n^{p}}$ converges iff $p > 1$; logarithms never change the verdict of a strict inequality $p \ne 1$.
