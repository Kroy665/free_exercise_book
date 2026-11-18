# Alternating and Arbitrary Series

## Absolute and conditional convergence {#absolute-convergence}

A **series of arbitrary terms** $\sum a_n$ may have terms of both signs. The tests for positive series (comparison, Raabe, condensation) do not apply to it directly. What still holds:

- **Cauchy's criterion.** $\sum a_n$ converges $\iff$ for every $\varepsilon > 0$ there is $N$ with $|a_{n+1} + a_{n+2} + \cdots + a_m| < \varepsilon$ for all $m > n \ge N$.
- **Necessary condition.** If $\sum a_n$ converges, then $a_n \to 0$. The converse is false.

**Definitions.**

- $\sum a_n$ is **absolutely convergent** if $\sum |a_n|$ converges.
- $\sum a_n$ is **conditionally convergent** if $\sum a_n$ converges but $\sum |a_n|$ diverges.

:::keyfacts
- **Absolute convergence implies convergence**, and $\left|\sum a_n\right| \le \sum |a_n|$.
- Proof: $|a_{n+1} + \cdots + a_m| \le |a_{n+1}| + \cdots + |a_m|$, so the Cauchy criterion for $\sum |a_n|$ gives it for $\sum a_n$.
- The converse fails: $\sum \frac{(-1)^{n+1}}{n}$ converges, but $\sum \frac1n$ diverges.
:::

Every series of reals is exactly one of: **absolutely convergent**, **conditionally convergent**, or **divergent**.

**Positive and negative parts.** Put $p_n = \frac{|a_n| + a_n}{2}$ and $q_n = \frac{|a_n| - a_n}{2}$. Both are $\ge 0$, $a_n = p_n - q_n$ and $|a_n| = p_n + q_n$.

| $\sum p_n$ | $\sum q_n$ | $\sum a_n$ is |
|:---|:---|:---|
| converges | converges | absolutely convergent |
| diverges | converges (or vice versa) | divergent (to $+\infty$ or $-\infty$) |
| diverges | diverges | conditionally convergent **or** divergent |

So in a conditionally convergent series, the positive terms alone and the negative terms alone **both** sum to $\infty$. This is the engine of Riemann's rearrangement theorem.

**Testing for absolute convergence** is testing a positive series, so all the positive-term tests apply to $\sum |a_n|$. For example, $\left|\frac{\sin n}{n^2}\right| \le \frac{1}{n^2}$, so $\sum \frac{\sin n}{n^2}$ converges absolutely.

:::caution
Comparison works only with **non-negative** terms. If $a_n/b_n \to 1$ but the terms change sign, nothing follows. With $b_n = \frac{(-1)^n}{\sqrt n}$ and $a_n = \frac{(-1)^n}{\sqrt n} + \frac1n$: $a_n/b_n \to 1$, $\sum b_n$ converges (Leibniz), but $\sum a_n$ diverges, since it is a convergent series plus the harmonic series.
:::

:::exam-tip
To show that $\sum |a_n|$ diverges, any positive-term test will do. That shows only that the series is **not absolutely** convergent; $\sum a_n$ itself may still converge.
:::

## Alternating series and the Leibniz test {#leibniz-test}

An **alternating series** has the form $\sum (-1)^{n+1} u_n = u_1 - u_2 + u_3 - \cdots$ with $u_n > 0$.

:::keyfacts
**Leibniz test.** If $(u_n)$ is **monotone decreasing** ($u_{n+1} \le u_n$ for all $n$) and $u_n \to 0$, then $\sum (-1)^{n+1} u_n$ converges. If $S$ is its sum and $S_n$ the $n$th partial sum:

- $S$ lies between any two consecutive partial sums, and $0 \le S \le u_1$;
- **error bound:** $|S - S_n| \le u_{n+1}$, the first omitted term;
- $S - S_n$ has the sign of the first omitted term (or is $0$).
:::

**Proof idea.** $S_{2n} = (u_1 - u_2) + \cdots + (u_{2n-1} - u_{2n})$ increases, and $S_{2n+1} = u_1 - (u_2 - u_3) - \cdots - (u_{2n} - u_{2n+1})$ decreases. Also $S_{2n} \le S_{2n+1}$ and $S_{2n+1} - S_{2n} = u_{2n+1} \to 0$. So the intervals $[S_{2n}, S_{2n+1}]$ are nested and shrink to one point $S$.

The partial sums of $1 - \frac12 + \frac13 - \cdots$ zig-zag about the sum $\ln 2$:

```plot
title: Partial sums $S_n$ of $1 - \frac12 + \frac13 - \cdots$ oscillate about $\ln 2$
x: 0, 11
y: 0.4, 1.05
hline: 0.6931 | $\ln 2$
point: 1, 1
point: 2, 0.5
point: 3, 0.8333
point: 4, 0.5833
point: 5, 0.7833
point: 6, 0.6167
point: 7, 0.7595
point: 8, 0.6345
point: 9, 0.7456
point: 10, 0.6456
xlabel: $n$
ylabel: $S_n$
```

**Both hypotheses matter.**

- $u_n \to 0$ is needed: $\sum (-1)^n \frac{n}{n+1}$ diverges, because its terms do not tend to $0$.
- Monotonicity is needed: take $u_{2k-1} = \frac1k$ and $u_{2k} = \frac{1}{k^2}$. Then $u_n \to 0$, but pairing gives $\sum\left(\frac1k - \frac1{k^2}\right) = \infty$.
- It is enough for $(u_n)$ to decrease **eventually** (from some $n_0$ on).

**Checking monotonicity.** Write $u_n = f(n)$ and show $f'(x) < 0$. For $u_n = \frac{\ln n}{n}$: $f'(x) = \frac{1 - \ln x}{x^2} < 0$ for $x > e$, so $u_n$ decreases for $n \ge 3$ and $\sum (-1)^n \frac{\ln n}{n}$ converges.

**Using the error bound.** How many terms of $\sum \frac{(-1)^{n+1}}{n}$ give $\ln 2$ with error less than $10^{-3}$? We need $\frac{1}{n+1} < 10^{-3}$, so $n + 1 > 1000$, i.e. $n \ge 1000$ terms (the bound is safe, not sharp). For $\sum \frac{(-1)^n}{n!} = e^{-1}$ the error after the term $\frac{(-1)^n}{n!}$ is at most $\frac{1}{(n+1)!}$; the six terms $n = 0$ to $5$ already give an error of at most $\frac{1}{6!} = \frac1{720}$.

:::caution
The error bound $|S - S_n| \le u_{n+1}$ needs the Leibniz hypotheses. It is **not** a general fact about convergent series.
:::

## Standard examples {#standard-examples}

:::keyfacts
- $\displaystyle 1 - \frac12 + \frac13 - \frac14 + \cdots = \ln 2$, conditionally convergent.
- $\displaystyle \sum \frac{(-1)^n}{n^p}$: absolutely convergent for $p > 1$; conditionally convergent for $0 < p \le 1$; divergent for $p \le 0$ (terms do not tend to $0$).
:::

**Why the sum is $\ln 2$.** With $H_m = 1 + \frac12 + \cdots + \frac1m$:
$$S_{2n} = H_{2n} - 2\cdot\tfrac12 H_n = H_{2n} - H_n = \sum_{k=n+1}^{2n} \frac1k \to \int_1^2 \frac{dx}{x} = \ln 2.$$
It is also $\ln(1 + x)$ at $x = 1$, the endpoint of the Maclaurin series (justified by Abel's limit theorem).

**More classifications.**

| Series | Behaviour | Reason |
|:---|:---|:---|
| $\sum \frac{(-1)^{n+1}}{2n - 1} = \frac{\pi}{4}$ | conditional | Leibniz; $\frac1{2n-1} \sim \frac1{2n}$ |
| $\sum \frac{(-1)^{n+1}}{n^2} = \frac{\pi^2}{12}$ | absolute | $p = 2$ |
| $\sum \frac{(-1)^n}{n!} = \frac1e$ | absolute | ratio test |
| $\sum_{n \ge 2} \frac{(-1)^n}{\ln n}$ | conditional | $\frac1{\ln n} > \frac1n$ |
| $\sum_{n \ge 2} \frac{(-1)^n}{n \ln n}$ | conditional | condensation: $\sum \frac{1}{n\ln n} = \infty$ |
| $\sum_{n \ge 2} \frac{(-1)^n}{n (\ln n)^2}$ | absolute | condensation, $p = 2$ |
| $\sum (-1)^n \sin\frac1n$ | conditional | $\sin\frac1n \sim \frac1n$, decreasing |
| $\sum (-1)^n \left(1 - \cos\frac1n\right)$ | absolute | $\sim \frac{1}{2n^2}$ |
| $\sum (-1)^n \left(\sqrt{n + 1} - \sqrt n\right)$ | conditional | $= \frac{1}{\sqrt{n+1} + \sqrt n} \sim \frac{1}{2\sqrt n}$ |
| $\sum (-1)^n \frac{n}{n^2 + 1}$ | conditional | $\sim \frac1n$; decreasing for $n \ge 1$ |
| $\sum (-1)^n \frac{n + 1}{n}$ | divergent | terms $\to \pm 1$ |
| $\sum (-1)^n \frac{n^2}{2^n}$ | absolute | ratio $\to \frac12$ |

**Method.** (1) Do the terms tend to $0$? If not, it diverges. (2) Test $\sum |a_n|$ with a positive-term test (limit comparison with $\frac1{n^p}$ is usually enough). If it converges, the series is absolutely convergent. (3) If not, try Leibniz (or Dirichlet). If that works, it is conditionally convergent.

:::exam-tip
For $\sum (-1)^n f(n)$, the asymptotic form of $f(n)$ decides absolute convergence, and monotonicity plus $f(n) \to 0$ decides convergence. $f(n) \sim \frac{c}{n^p}$ with $0 < p \le 1$ almost always means "conditionally convergent".
:::

## Ratio and root tests for absolute convergence {#ratio-root}

For a series of arbitrary (non-zero) terms, apply the tests to $|a_n|$:

:::keyfacts
- **Ratio test (D'Alembert).** Let $L = \lim \left|\frac{a_{n+1}}{a_n}\right|$. If $L < 1$, then $\sum a_n$ converges absolutely. If $L > 1$, then $\sum a_n$ **diverges**. If $L = 1$, the test fails.
- **Root test (Cauchy).** Let $L = \limsup |a_n|^{1/n}$. If $L < 1$, then $\sum a_n$ converges absolutely. If $L > 1$, then $\sum a_n$ **diverges**. If $L = 1$, the test fails.
- Limsup form of the ratio test: $\limsup \left|\frac{a_{n+1}}{a_n}\right| < 1$ gives absolute convergence; $\left|\frac{a_{n+1}}{a_n}\right| \ge 1$ for all large $n$ gives divergence.
:::

**Why divergence of $\sum a_n$ itself.** If $L > 1$ in either test, then $|a_n| \not\to 0$ (in the ratio test, $|a_n|$ eventually increases; in the root test, $|a_n| > 1$ infinitely often). So $a_n \not\to 0$, and $\sum a_n$ diverges. This is special to these two tests. Showing $\sum |a_n| = \infty$ by comparison or Raabe's test does **not** show that $\sum a_n$ diverges.

**Examples.**

- $\sum (-1)^n \frac{n!}{n^n}$: $\left|\frac{a_{n+1}}{a_n}\right| = \left(\frac{n}{n+1}\right)^n \to \frac1e < 1$, so it converges absolutely.
- $\sum (-1)^n \left(\frac{n}{n+1}\right)^{n^2}$: $|a_n|^{1/n} = \left(1 + \frac1n\right)^{-n} \to \frac1e$, so it converges absolutely.
- $\sum \frac{(-2)^n}{n^2}$: the ratio tends to $2 > 1$, so it diverges.
- $\sum \frac{(-1)^n}{n^p}$ for any $p$: the ratio and root both tend to $1$, so these tests say nothing. Use Leibniz and the $p$-test.

**Root beats ratio.** Always
$$\liminf \left|\tfrac{a_{n+1}}{a_n}\right| \le \liminf |a_n|^{1/n} \le \limsup |a_n|^{1/n} \le \limsup \left|\tfrac{a_{n+1}}{a_n}\right|.$$
So when the ratio test decides, the root test decides the same way, but not conversely. For $a_n = 2^{(-1)^n - n}$ the ratios alternate between $\frac18$ and $2$, so the ratio test fails; but $|a_n|^{1/n} \to \frac12$, so the series converges.

:::caution
$L = 1$ tells you nothing: $\sum \frac{1}{n}$ diverges, $\sum \frac{(-1)^n}{n}$ converges conditionally, $\sum \frac{1}{n^2}$ converges absolutely, and all three have $L = 1$.
:::

## Abel's and Dirichlet's tests {#abel-dirichlet}

These handle products $\sum a_n b_n$ where Leibniz does not apply directly. Both rest on **Abel's partial summation**: with $A_n = a_1 + \cdots + a_n$,
$$\sum_{k=1}^{n} a_k b_k = A_n b_n + \sum_{k=1}^{n-1} A_k \,(b_k - b_{k+1}).$$

:::keyfacts
- **Dirichlet's test.** If the partial sums $A_n$ of $\sum a_n$ are **bounded**, and $(b_n)$ is **monotone** with $b_n \to 0$, then $\sum a_n b_n$ converges.
- **Abel's test.** If $\sum a_n$ **converges**, and $(b_n)$ is **monotone and bounded**, then $\sum a_n b_n$ converges.
- Leibniz is the special case of Dirichlet with $a_n = (-1)^{n+1}$ (partial sums $1, 0, 1, 0, \dots$).
:::

| | condition on $\sum a_n$ | condition on $(b_n)$ |
|:---|:---|:---|
| Dirichlet | partial sums bounded | monotone, $b_n \to 0$ |
| Abel | convergent | monotone, bounded |

**The trigonometric sums.** For $x$ not a multiple of $2\pi$,
$$\sum_{k=1}^{n} \sin kx = \frac{\sin\frac{nx}{2}\,\sin\frac{(n+1)x}{2}}{\sin\frac x2}, \qquad \left|\sum_{k=1}^{n} \sin kx\right| \le \frac{1}{\left|\sin\frac x2\right|},$$
and the same bound holds for $\sum_{k=1}^n \cos kx$.

**Applications.**

- $\sum \frac{\sin nx}{n}$ **converges for every real $x$**: by Dirichlet with $b_n = \frac1n$ when $x \notin 2\pi\Z$; all terms are $0$ when $x \in 2\pi\Z$. For $0 < x < 2\pi$ its sum is $\frac{\pi - x}{2}$.
- It is **not absolutely** convergent unless $x \in \pi\Z$: $|\sin nx| \ge \sin^2 nx = \frac{1 - \cos 2nx}{2}$, and $\sum \frac{1}{2n} = \infty$ while $\sum \frac{\cos 2nx}{2n}$ converges.
- $\sum \frac{\cos nx}{n}$ converges if and only if $x \notin 2\pi\Z$ (at $x = 2k\pi$ it is the harmonic series). More generally $\sum \frac{\cos nx}{n^p}$ and $\sum \frac{\sin nx}{n^p}$ converge for all $p > 0$ when $x \notin 2\pi\Z$, absolutely when $p > 1$.
- **Abel:** $\sum \frac{(-1)^{n+1}}{n}\left(1 + \frac1n\right)^n$ converges, since $\sum \frac{(-1)^{n+1}}{n}$ converges and $\left(1 + \frac1n\right)^n$ increases to $e$ (monotone, bounded). Similarly $\sum \frac{(-1)^{n}}{n}\cdot\frac{n}{n+1}$ and $\sum \frac{(-1)^n}{n} n^{1/n}$.

:::caution
Monotonicity of $(b_n)$ cannot be dropped. With $a_n = (-1)^n$ (bounded partial sums) and $b_n = \frac{(-1)^n}{n} \to 0$, not monotone: $\sum a_n b_n = \sum \frac1n$ diverges. Also, in Abel's test $b_n$ need not tend to $0$, but $\sum a_n$ must **converge**; bounded partial sums are not enough (take $a_n = (-1)^n$, $b_n = 1$).
:::

## Rearrangements and the Cauchy product {#rearrangements}

A **rearrangement** of $\sum a_n$ is $\sum a_{\sigma(n)}$ for a bijection $\sigma : \N \to \N$.

:::keyfacts
- **Dirichlet's theorem.** If $\sum a_n$ converges absolutely to $S$, then every rearrangement converges absolutely to the same sum $S$.
- **Riemann's rearrangement theorem.** If $\sum a_n$ (real terms) converges conditionally, then for any $s \in \R$ some rearrangement converges to $s$; other rearrangements diverge to $+\infty$ or to $-\infty$. (More generally, for any $-\infty \le \alpha \le \beta \le \infty$ a rearrangement has $\liminf S_n = \alpha$ and $\limsup S_n = \beta$.)
- So for real series: **every rearrangement converges to the same sum $\iff$ the series converges absolutely.**
:::

**Idea of Riemann's proof.** The positive terms and the negative terms both sum to $\infty$, and the terms tend to $0$. Add positive terms until you just pass $s$, then negative terms until you just drop below $s$, and repeat. The overshoot is at most the size of the last term, which tends to $0$.

**Alternating harmonic rearrangements.** Taking $p$ positive terms, then $q$ negative terms, in turn gives the sum $\ln 2 + \frac12 \ln\frac pq$:
$$1 - \tfrac12 - \tfrac14 + \tfrac13 - \tfrac16 - \tfrac18 + \cdots = \tfrac12 \ln 2, \qquad 1 + \tfrac13 - \tfrac12 + \tfrac15 + \tfrac17 - \tfrac14 + \cdots = \tfrac32 \ln 2.$$

**Brackets.** Inserting brackets into a convergent series does not change its sum (the new partial sums form a subsequence). Removing them can: $(1 - 1) + (1 - 1) + \cdots = 0$, but $1 - 1 + 1 - \cdots$ diverges.

### The Cauchy product

The **Cauchy product** of $\sum_{n \ge 0} a_n$ and $\sum_{n \ge 0} b_n$ is $\sum_{n \ge 0} c_n$ with
$$c_n = \sum_{k=0}^{n} a_k b_{n-k} = a_0 b_n + a_1 b_{n-1} + \cdots + a_n b_0.$$

- **Mertens' theorem.** If $\sum a_n = A$ **absolutely** and $\sum b_n = B$ (convergent), then $\sum c_n = AB$.
- If both converge absolutely, so does the product.
- **Abel's theorem.** If $\sum a_n$, $\sum b_n$ and $\sum c_n$ all converge, then $\sum c_n = AB$.
- Examples: $e^x e^y = e^{x+y}$ by multiplying the exponential series; $\left(\sum_{n\ge0} x^n\right)^2 = \sum_{n\ge0} (n + 1)x^n$ for $|x| < 1$.

:::caution
The Cauchy product of two conditionally convergent series may diverge. For $a_n = b_n = \frac{(-1)^n}{\sqrt{n + 1}}$: since $(k + 1)(n - k + 1) \le \left(\frac{n + 2}{2}\right)^2$, we get $|c_n| \ge \frac{2(n + 1)}{n + 2} \to 2$, so $c_n \not\to 0$.
:::

## Interval of convergence and endpoints {#interval-of-convergence}

Typical question: for which real $x$ does $\sum a_n x^n$ (or $\sum a_n (x - c)^n$) converge, and how?

**Method.**

1. Apply the ratio or root test to $|a_n x^n|$. This gives absolute convergence for $|x - c| < R$ and divergence for $|x - c| > R$ (the terms do not tend to $0$ there).
2. **Test the two endpoints separately**, by substituting them. There the ratio and root limits equal $1$, so use the $p$-test, Leibniz, or the $n$th-term test.
3. Each endpoint may be absolutely convergent, conditionally convergent, or divergent.

**Worked example.** $\sum \frac{x^n}{n}$: $\left|\frac{a_{n+1}}{a_n}\right| = \frac{n}{n+1}|x| \to |x|$. So it converges absolutely for $|x| < 1$ and diverges for $|x| > 1$.

- At $x = 1$: $\sum \frac1n$ diverges.
- At $x = -1$: $\sum \frac{(-1)^n}{n}$ converges conditionally.

The set of convergence is $[-1, 1)$.

| Series | Converges for | Endpoints |
|:---|:---|:---|
| $\sum x^n$ | $(-1, 1)$ | both diverge (terms $\pm 1$) |
| $\sum \frac{x^n}{n}$ | $[-1, 1)$ | $-1$: conditional |
| $\sum \frac{(-1)^{n+1} x^n}{n}$ | $(-1, 1]$ | $1$: conditional ($= \ln 2$) |
| $\sum \frac{x^n}{\sqrt n}$ | $[-1, 1)$ | $-1$: conditional |
| $\sum \frac{x^n}{n^2}$ | $[-1, 1]$ | both absolute |
| $\sum \frac{x^n}{n!}$ | $\R$ | none |
| $\sum n!\, x^n$ | $\{0\}$ only | none |
| $\sum \frac{(x - 2)^n}{n\, 3^n}$ | $[-1, 5)$ | $-1$: conditional; $5$: harmonic |

For $\sum \frac{(x - 2)^n}{n 3^n}$: the ratio limit is $\frac{|x - 2|}{3}$, so the open interval is $|x - 2| < 3$, i.e. $(-1, 5)$. At $x = 5$ the series is $\sum \frac1n$; at $x = -1$ it is $\sum \frac{(-1)^n}{n}$.

:::exam-tip
Answer options in these questions usually differ only at the endpoints, so the endpoint check is the whole question. Watch out for gaps in the powers: for $\sum \frac{x^{2n}}{n\,4^n}$ the ratio limit is $\frac{x^2}{4}$, giving $|x| < 2$; at $x = \pm 2$ the series is $\sum \frac1n$, so it converges exactly on $(-2, 2)$.
:::

The general theory (radius of convergence, the Cauchy–Hadamard formula $\frac1R = \limsup |a_n|^{1/n}$, Abel's limit theorem) belongs to the topic on power series.

## Quick checks and traps {#exam-tips}

- **Terms first.** If $a_n \not\to 0$, the series diverges; no further test is needed. $\sum (-1)^n \frac{n}{n + 1}$ diverges.
- **Absolute convergence $\Rightarrow$ convergence**, never the reverse. "Convergent but not absolutely convergent" = conditionally convergent.
- **Leibniz hypotheses:** $u_n$ decreasing (eventually) **and** $u_n \to 0$. Leibniz proves convergence only; it never proves absolute convergence.
- **Error bound:** $|S - S_n| \le u_{n+1}$. For error $< \varepsilon$ in $\sum \frac{(-1)^{n+1}}{n}$, take $n + 1 > \frac1\varepsilon$.
- **$\sum \frac{(-1)^n}{n^p}$:** absolute for $p > 1$, conditional for $0 < p \le 1$, divergent for $p \le 0$.
- **Ratio or root limit $> 1$** means $\sum a_n$ itself diverges. Divergence of $\sum |a_n|$ by any other test means only "not absolutely convergent".
- **Limit comparison needs positive terms.** Never conclude convergence of $\sum a_n$ from $a_n \sim b_n$ when the terms change sign.
- **Dirichlet vs Abel:** Dirichlet needs bounded partial sums and $b_n \downarrow 0$; Abel needs a convergent $\sum a_n$ and $b_n$ monotone and bounded.
- **$\sum \frac{\sin nx}{n}$** converges for every $x$; $\sum \frac{\cos nx}{n}$ converges iff $x \notin 2\pi\Z$.
- **Rearrangements:** absolute convergence makes the sum rearrangement-proof; a conditionally convergent series can be rearranged to any sum, or to diverge.
- **Cauchy product:** one series absolutely convergent and the other convergent is enough (Mertens).
- **Endpoints are tested separately** in $\sum a_n x^n$ problems.
