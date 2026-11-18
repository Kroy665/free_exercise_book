import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from qlib import Topic, eq

T = Topic("math.analysis.series-positive")

# ---------------------------------------------------------------- single (20)
# q1
T.single(1, ["convergence"], r"If $\sum a_n$ is a convergent series of positive terms, then necessarily",
         [r"$a_n \to 0$", r"$n a_n \to 0$", r"$\lim \dfrac{a_{n+1}}{a_n} < 1$", r"$(a_n)$ is decreasing"],
         r"""Since $a_n = s_n - s_{n-1}$ and both partial sums tend to the same limit $s$:
$$a_n = s_n - s_{n-1} \to s - s = 0.$$

The others are not forced:
- $n a_n \to 0$ needs $(a_n)$ **decreasing** (Abel–Pringsheim). Without it, take $a_n = \frac1n$ at perfect squares and $\frac{1}{n^2}$ elsewhere.
- For $\sum\frac{1}{n^2}$ the ratio tends to $1$, not to a number below $1$.
- A convergent series can have non-monotone terms, e.g. $\frac{1}{n^2}$ and $\frac{1}{2n^2}$ alternately.""")

# q2
T.single(1, ["p-series"], r"The series $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^p}$ converges if and only if",
         [r"$p > 1$", r"$p \ge 1$", r"$p > 0$", r"$p < 1$"],
         r"""Condensation: $\sum 2^k\cdot\frac{1}{2^{kp}} = \sum\left(2^{1-p}\right)^k$ is geometric with ratio $2^{1-p}$. It converges iff $2^{1-p} < 1$, i.e. $p > 1$.

The boundary $p = 1$ is the harmonic series, which **diverges**, so "$p \ge 1$" is wrong. For $0 < p \le 1$ the terms tend to $0$ but the series still diverges.""")

# q3
T.single(1, ["p-series", "exam-tips"], r"The sum $\displaystyle\sum_{n=1}^{\infty}\left(\frac23\right)^n$ equals",
         [r"$2$", r"$3$", r"$\dfrac23$", r"$\dfrac13$"],
         r"""A geometric series starting at $n = 1$:
$$\sum_{n=1}^{\infty} r^n = \frac{r}{1 - r} = \frac{2/3}{1/3} = 2.$$

$3 = \frac{1}{1 - r}$ is the sum from $n = 0$; it counts the extra term $1$.""")

# q4
T.single(1, ["convergence"], r"The sum $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n(n + 1)}$ equals",
         [r"$1$", r"$\dfrac12$", r"$2$", r"the series diverges"],
         r"""Partial fractions: $\frac{1}{n(n + 1)} = \frac1n - \frac{1}{n + 1}$. The series telescopes:
$$s_n = 1 - \frac{1}{n + 1} \to 1.$$

$\frac12$ is just the first term. The series cannot diverge: its terms behave like $\frac{1}{n^2}$.""")

# q5
T.single(2, ["ratio-root", "standard-examples"],
         r"For $a_n = \dfrac{n!}{n^n}$, the value of $\displaystyle\lim_{n\to\infty}\frac{a_{n+1}}{a_n}$ is",
         [r"$\dfrac1e$", r"$e$", r"$1$", r"$0$"],
         r"""$$\frac{a_{n+1}}{a_n} = \frac{(n + 1)!}{(n + 1)^{n+1}}\cdot\frac{n^n}{n!} = \frac{n^n}{(n + 1)^n} = \frac{1}{\left(1 + \frac1n\right)^n} \to \frac1e.$$

Since $\frac1e < 1$, $\sum\frac{n!}{n^n}$ converges by D'Alembert's test.

$e$ is the reciprocal ratio $\frac{a_n}{a_{n+1}}$; $1$ comes from cancelling $\frac{(n + 1)!}{n!}$ against only one factor $n + 1$ and forgetting the $n$th power.""")

# q6
T.single(2, ["ratio-root", "standard-examples"],
         r"For $a_n = \left(1 + \dfrac1n\right)^{-n^2}$, the value of $\displaystyle\lim_{n\to\infty} a_n^{1/n}$ is",
         [r"$\dfrac1e$", r"$e$", r"$1$", r"$0$"],
         r"""$$a_n^{1/n} = \left(1 + \frac1n\right)^{-n} \to \frac1e.$$

Since $\frac1e < 1$, $\sum\left(1 + \frac1n\right)^{-n^2}$ converges by Cauchy's root test.

$1$ is the limit of $1 + \frac1n$ alone (forgetting the exponent $n$ that remains); $e$ drops the minus sign.""")

# q7
T.single(2, ["ratio-root", "standard-examples"],
         r"For $x > 0$, the series $\displaystyle\sum_{n=1}^{\infty}\frac{x^n}{n}$ converges if and only if",
         [r"$0 < x < 1$", r"$0 < x \le 1$", r"$x > 1$", r"$x > 0$"],
         r"""Ratio test:
$$\frac{a_{n+1}}{a_n} = \frac{n}{n + 1}\,x \to x.$$
So it converges for $x < 1$ and diverges for $x > 1$.

At $x = 1$ the test is silent, and the series is $\sum\frac1n$, which **diverges**. So the answer is $0 < x < 1$. "$0 < x \le 1$" is the trap: it wrongly includes the harmonic series at $x = 1$.""")

# q8
T.single(2, ["p-series", "abel-pringsheim"], r"The series $\displaystyle\sum_{n=2}^{\infty}\frac{1}{n\ln n}$",
         [r"diverges, by Cauchy's condensation test", r"converges, by comparison with $\sum\frac{1}{n^2}$",
          r"converges, since $n a_n \to 0$", r"converges, by the ratio test"],
         r"""The terms are positive and decreasing. Condense:
$$2^k a_{2^k} = \frac{2^k}{2^k\,k\ln 2} = \frac{1}{\ln 2}\cdot\frac1k,$$
a multiple of the harmonic series. So the series **diverges**.

- $n a_n = \frac{1}{\ln n} \to 0$ is true but is only a **necessary** condition (Abel–Pringsheim); it does not give convergence.
- $\frac{1}{n\ln n} \le \frac{1}{n^2}$ is false for large $n$.
- The ratio tends to $1$, so the ratio test decides nothing.""")

# q9
T.single(2, ["comparison"], r"Which of the following series converges?",
         [r"$\displaystyle\sum\frac{\sqrt{n + 1} - \sqrt n}{n}$", r"$\displaystyle\sum\left(\sqrt{n + 1} - \sqrt n\right)$",
          r"$\displaystyle\sum\frac{1}{\sqrt{n(n + 1)}}$", r"$\displaystyle\sum\sin\frac1n$"],
         r"""Rationalise: $\sqrt{n + 1} - \sqrt n = \dfrac{1}{\sqrt{n + 1} + \sqrt n}$. So
$$\frac{\sqrt{n + 1} - \sqrt n}{n} = \frac{1}{n(\sqrt{n + 1} + \sqrt n)}, \qquad n^{3/2}a_n \to \frac12.$$
By limit comparison with $\sum n^{-3/2}$ ($p = \frac32 > 1$) it converges.

- $\sum\left(\sqrt{n + 1} - \sqrt n\right)$ telescopes to $\sqrt{n + 1} - 1 \to \infty$.
- $\frac{1}{\sqrt{n(n + 1)}} \sim \frac1n$: diverges.
- $\sin\frac1n \sim \frac1n$: diverges.""")

# q10
T.single(1, ["convergence", "exam-tips"], r"The series $\displaystyle\sum_{n=1}^{\infty}\left(1 + \frac1n\right)^{-n}$",
         [r"diverges, since its terms tend to $\dfrac1e \ne 0$", r"converges, by the root test",
          r"converges, since its terms are decreasing", r"converges, by the ratio test"],
         r"""$$a_n = \frac{1}{\left(1 + \frac1n\right)^n} \to \frac1e \ne 0.$$
A convergent series must have $a_n \to 0$, so this one **diverges**.

The root and ratio limits both equal $1$, so those tests decide nothing. Decreasing terms are not enough either: they decrease to $\frac1e$, not to $0$. (Compare $\sum(1 + \frac1n)^{-n^2}$, which does converge.)""")

# q11
T.single(3, ["ratio-root", "standard-examples"],
         r"For $a > 0$, the series $\displaystyle\sum_{n=1}^{\infty}\frac{a^n\,n!}{n^n}$ converges if and only if",
         [r"$0 < a < e$", r"$0 < a \le e$", r"$0 < a < 1$", r"$0 < a < \dfrac1e$"],
         r"""Ratio test:
$$\frac{a_{n+1}}{a_n} = \frac{a}{\left(1 + \frac1n\right)^n} \to \frac ae.$$
It converges for $a < e$ and diverges for $a > e$.

End point $a = e$: $\frac{a_{n+1}}{a_n} = \frac{e}{(1 + 1/n)^n} > 1$, because $(1 + \frac1n)^n < e$ for every $n$. So the terms **increase** and cannot tend to $0$: it diverges. (Stirling: $a_n \sim \sqrt{2\pi n}$.)

So the answer is $0 < a < e$. "$0 < a < \frac1e$" inverts the ratio.""")

# q12
T.single(2, ["raabe-gauss"],
         r"For $a_n = \dfrac{1\cdot 3\cdot 5\cdots(2n - 1)}{2\cdot 4\cdot 6\cdots(2n)}$, the value of $\displaystyle\lim_{n\to\infty} n\left(\frac{a_n}{a_{n+1}} - 1\right)$ is",
         [r"$\dfrac12$", r"$1$", r"$2$", r"$0$"],
         r"""$a_{n+1} = a_n\cdot\dfrac{2n + 1}{2n + 2}$, so
$$\frac{a_n}{a_{n+1}} - 1 = \frac{2n + 2}{2n + 1} - 1 = \frac{1}{2n + 1}, \qquad n\left(\frac{a_n}{a_{n+1}} - 1\right) = \frac{n}{2n + 1} \to \frac12.$$

Since $\frac12 < 1$, Raabe's test gives **divergence** of $\sum a_n$ (indeed $a_n \sim \frac{1}{\sqrt{\pi n}}$).

$0$ is $\lim\left(\frac{a_n}{a_{n+1}} - 1\right)$ without the factor $n$, which is why the ratio test fails here.""")

# q13
T.single(3, ["standard-examples", "raabe-gauss"],
         r"For $x > 0$, the series $\displaystyle\sum_{n=1}^{\infty}\frac{(n!)^2}{(2n)!}\,x^n$ converges if and only if",
         [r"$0 < x < 4$", r"$0 < x \le 4$", r"$0 < x < 2$", r"$0 < x < \dfrac14$"],
         r"""$$\frac{a_{n+1}}{a_n} = \frac{(n + 1)^2}{(2n + 1)(2n + 2)}\,x \to \frac x4.$$
So it converges for $x < 4$ and diverges for $x > 4$.

At $x = 4$:
$$\frac{a_{n+1}}{a_n} = \frac{4(n + 1)^2}{(2n + 1)(2n + 2)} = \frac{2n + 2}{2n + 1} > 1,$$
so the terms increase (they behave like $\sqrt{\pi n}$) and the series diverges. Hence $0 < x < 4$.

$\frac14$ comes from inverting the ratio; $2$ from taking $\frac{(n + 1)^2}{2n + 2}$ and missing the factor $2n + 1$.""")

# q14
T.single(3, ["raabe-gauss", "standard-examples"],
         r"For $x > 0$, the series $\displaystyle\sum_{n=1}^{\infty}\frac{n^n x^n}{n!}$ converges if and only if",
         [r"$0 < x < \dfrac1e$", r"$0 < x \le \dfrac1e$", r"$0 < x < e$", r"$0 < x < 1$"],
         r"""$$\frac{a_n}{a_{n+1}} = \frac{1}{x\left(1 + \frac1n\right)^n} \to \frac{1}{ex}.$$
It converges for $x < \frac1e$, diverges for $x > \frac1e$.

At $x = \frac1e$ use the logarithmic test:
$$n\ln\frac{a_n}{a_{n+1}} = n\left[1 - n\ln\left(1 + \tfrac1n\right)\right] = n\left[\frac{1}{2n} - \frac{1}{3n^2} + \cdots\right] \to \frac12 < 1,$$
so it **diverges**. (Stirling: $a_n \sim \frac{1}{\sqrt{2\pi n}}$, like $n^{-1/2}$.) Hence $0 < x < \frac1e$; the closed end point is the trap.""")

# q15
T.single(3, ["raabe-gauss"],
         r"Let $a_n = \dfrac{1\cdot 3\cdots(2n - 1)}{2\cdot 4\cdots(2n)}$ and $p > 0$. The series $\displaystyle\sum_{n=1}^{\infty} a_n^{\,p}$ converges if and only if",
         [r"$p > 2$", r"$p \ge 2$", r"$p > 1$", r"$p > \dfrac12$"],
         r"""$$\frac{a_n^p}{a_{n+1}^p} = \left(\frac{2n + 2}{2n + 1}\right)^p = \left(1 + \frac{1}{2n + 1}\right)^p = 1 + \frac{p/2}{n} + O\!\left(\frac{1}{n^2}\right).$$
In Gauss's test $\lambda = 1$ and $\mu = \frac p2$. It converges iff $\mu > 1$, i.e. $p > 2$; for $\mu \le 1$ it diverges.

At $p = 2$ Raabe's limit is exactly $1$ (no decision), but Gauss gives **divergence** ($a_n^2 \sim \frac{1}{\pi n}$). So "$p \ge 2$" is wrong; "$p > 1$" treats $a_n$ as if it were $\frac1n$ rather than $\frac{1}{\sqrt{\pi n}}$.""")

# q16
T.single(2, ["convergence"], r"Cauchy's criterion states that a series $\sum a_n$ converges if and only if, for every $\varepsilon > 0$, there is an $N$ such that",
         [r"$\lvert a_{n+1} + a_{n+2} + \cdots + a_m\rvert < \varepsilon$ for all $m > n \ge N$",
          r"$\lvert a_n\rvert < \varepsilon$ for all $n \ge N$",
          r"$\lvert a_{n+1} + \cdots + a_{2n}\rvert < \varepsilon$ for all $n \ge N$",
          r"$\lvert a_{n+1} - a_n\rvert < \varepsilon$ for all $n \ge N$"],
         r"""The criterion is Cauchy's principle for the partial sums: $\lvert s_m - s_n\rvert = \lvert a_{n+1} + \cdots + a_m\rvert < \varepsilon$ for **all** $m > n \ge N$.

The others are necessary but not sufficient:
- $a_n \to 0$ holds for $\sum\frac1n$, which diverges.
- $s_{2n} - s_n \to 0$ holds for $\sum\frac{1}{n\ln n}$, which diverges.
- $a_{n+1} - a_n \to 0$ holds even for $a_n = 1$.""")

# q17
T.single(2, ["abel-pringsheim"],
         r"Let $(a_n)$ be a decreasing sequence of positive terms such that $\sum a_n$ converges. Which of the following must hold?",
         [r"$n a_n \to 0$", r"$n^2 a_n \to 0$", r"$\displaystyle\lim\frac{a_{n+1}}{a_n} < 1$", r"$\sum n a_n$ converges"],
         r"""This is the **Abel–Pringsheim test**: positive, decreasing and convergent force $n a_n \to 0$.

Counterexamples for the others, all with $a_n = n^{-p}$:
- $p = \frac32$: $n^2 a_n = \sqrt n \to \infty$.
- $p = 2$: the ratio tends to $1$.
- $p = 2$: $\sum n a_n = \sum\frac1n$ diverges.""")

# q18
T.single(2, ["abel-pringsheim"],
         r"The integral test for $\displaystyle\sum_{n=2}^{\infty}\frac{1}{n(\ln n)^2}$ uses $\displaystyle\int_2^{\infty}\frac{dx}{x(\ln x)^2}$ (here $\ln$ is the natural logarithm). Its value is",
         [r"$\dfrac{1}{\ln 2}$", r"$\ln 2$", r"$\infty$", r"$\dfrac{1}{(\ln 2)^2}$"],
         r"""Put $u = \ln x$, $du = \frac{dx}{x}$:
$$\int_2^{\infty}\frac{dx}{x(\ln x)^2} = \int_{\ln 2}^{\infty}\frac{du}{u^2} = \left[-\frac1u\right]_{\ln 2}^{\infty} = \frac{1}{\ln 2}.$$
The integral is finite, so the series converges ($f$ is positive, continuous and decreasing on $[2, \infty)$).

$\infty$ is the answer for $\frac{1}{x\ln x}$ (power $1$ on the logarithm).""")

# q19
T.single(3, ["ratio-root"],
         r"Consider $\displaystyle\sum_{n=1}^{\infty} 2^{(-1)^n - n}$. Which statement is correct?",
         [r"The ratio test is inconclusive, but the root test gives convergence",
          r"The ratio test gives convergence",
          r"Both the ratio and root tests are inconclusive",
          r"The root test gives divergence"],
         r"""Ratio: for even $n$, $\frac{a_{n+1}}{a_n} = 2^{-1-(n+1)-1+n} = 2^{-3} = \frac18$; for odd $n$, $\frac{a_{n+1}}{a_n} = 2^{1-(n+1)+1+n} = 2$. The ratio oscillates between $\frac18$ and $2$, with $\liminf < 1 < \limsup$: no decision.

Root:
$$a_n^{1/n} = 2^{(-1)^n/n - 1} \to \frac12 < 1,$$
so the series converges. (Directly: $a_n \le 2\cdot 2^{-n}$.)

This is the standard example showing the root test is strictly stronger.""")

# q20
T.single(3, ["comparison"], r"The series $\displaystyle\sum_{n=1}^{\infty}\left(n^{1/n} - 1\right)$",
         [r"diverges, by comparison with $\sum\frac{\ln n}{n}$", r"converges, since $n^{1/n} - 1 \to 0$",
          r"converges, by the root test", r"converges, by comparison with $\sum\frac{1}{n^2}$"],
         r"""Write $n^{1/n} - 1 = e^{(\ln n)/n} - 1$. Since $e^t - 1 \ge t$:
$$n^{1/n} - 1 \ge \frac{\ln n}{n} \ge \frac1n \quad (n \ge 3).$$
So the series **diverges** by comparison with the harmonic series.

- $a_n \to 0$ is only necessary.
- $a_n^{1/n} \to 1$, so the root test decides nothing.
- $n^2 a_n \sim n\ln n \to \infty$, so $a_n$ is not $O(1/n^2)$.""")

# ------------------------------------------------------------ statements (3)
T.statements(1, ["convergence", "exam-tips"], r"Consider the following statements about series of positive terms:",
             [r"If $a_n \to 0$, then $\sum a_n$ converges.",
              r"$\sum\frac1n$ diverges.",
              r"If $\sum a_n$ converges, then $\sum a_n^2$ converges."],
             [r"2 and 3 only", r"1 and 2 only", r"2 only", r"1, 2 and 3"],
             r"""1. False: $\frac1n \to 0$ but $\sum\frac1n$ diverges.
2. True: $s_{2n} - s_n \ge \frac12$ for all $n$, so Cauchy's criterion fails.
3. True: $a_n \to 0$, so $0 < a_n < 1$ eventually and then $a_n^2 \le a_n$. Compare.

So 2 and 3 only.""")

T.statements(3, ["ratio-root"], r"Consider the following statements for sequences of positive terms $(a_n)$:",
             [r"If $\lim\frac{a_{n+1}}{a_n} = 1$, then $\sum a_n$ may converge or may diverge.",
              r"If $\lim\frac{a_{n+1}}{a_n} = l$ exists, then $\lim a_n^{1/n} = l$.",
              r"If $\lim a_n^{1/n}$ exists, then $\lim\frac{a_{n+1}}{a_n}$ exists."],
             [r"1 and 2 only", r"1 only", r"2 and 3 only", r"1, 2 and 3"],
             r"""1. True: $\frac1n$ diverges and $\frac{1}{n^2}$ converges; both have ratio limit $1$.
2. True: Cauchy's second limit theorem, from $\liminf\frac{a_{n+1}}{a_n} \le \liminf a_n^{1/n} \le \limsup a_n^{1/n} \le \limsup\frac{a_{n+1}}{a_n}$.
3. False: for $a_n = 2^{(-1)^n - n}$, $a_n^{1/n} \to \frac12$, but the ratio alternates between $\frac18$ and $2$.

So 1 and 2 only. This is why the root test is the stronger one.""")

T.statements(2, ["p-series", "abel-pringsheim"], r"Consider the following statements (all sums from $n = 2$; $\ln$ is the natural logarithm):",
             [r"$\sum\frac{1}{(\ln n)^2}$ diverges.",
              r"$\sum\frac{1}{n^{3/2}}$ converges.",
              r"$\sum\frac{1}{n(\ln n)^2}$ converges."],
             [r"1, 2 and 3", r"2 and 3 only", r"1 and 2 only", r"2 only"],
             r"""1. True: $(\ln n)^2 < n$ for large $n$, so $\frac{1}{(\ln n)^2} > \frac1n$ eventually. Compare with the harmonic series.
2. True: a p-series with $p = \frac32 > 1$.
3. True: condensation gives $\frac{1}{(\ln 2)^2}\sum\frac{1}{k^2}$, which converges (or the integral $\int_2^\infty\frac{dx}{x(\ln x)^2} = \frac{1}{\ln 2}$).

All three are correct. Statement 1 is the usual slip: any power of $\ln n$ grows slower than $n$.""")

# ----------------------------------------------------------------- match (2)
T.match(2, ["ratio-root", "standard-examples"],
        r"Match each series in List I with $\displaystyle\lim_{n\to\infty} a_n^{1/n}$ in List II.",
        [r"$\displaystyle\sum\frac{n^2}{2^n}$", r"$\displaystyle\sum\left(\frac{n}{n + 1}\right)^{n^2}$",
         r"$\displaystyle\sum\frac{3^n}{n^3}$", r"$\displaystyle\sum\frac{1}{n^5}$"],
        [r"$1$", r"$3$", r"$\dfrac12$", r"$\dfrac1e$"],
        [r"A-3, B-4, C-2, D-1", r"A-3, B-1, C-2, D-4", r"A-4, B-3, C-2, D-1", r"A-3, B-4, C-1, D-2"],
        r"""Use $n^{k/n} \to 1$ for fixed $k$.
- A: $\frac{(n^{1/n})^2}{2} \to \frac12$ (converges).
- B: $\left(\frac{n}{n + 1}\right)^n = \left(1 + \frac1n\right)^{-n} \to \frac1e$ (converges).
- C: $\frac{3}{(n^{1/n})^3} \to 3$ (diverges).
- D: $(n^{1/n})^{-5} \to 1$ (root test silent; the p-test gives convergence).

So A-3, B-4, C-2, D-1.""")

T.match(1, ["p-series", "convergence", "standard-examples"], r"Match each series in List I with its sum in List II.",
        [r"$\displaystyle\sum_{n=0}^{\infty}\frac{1}{2^n}$", r"$\displaystyle\sum_{n=1}^{\infty}\frac{1}{n(n + 1)}$",
         r"$\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^2}$", r"$\displaystyle\sum_{n=0}^{\infty}\frac{1}{n!}$"],
        [r"$e$", r"$2$", r"$\dfrac{\pi^2}{6}$", r"$1$"],
        [r"A-2, B-4, C-3, D-1", r"A-4, B-2, C-3, D-1", r"A-2, B-4, C-1, D-3", r"A-1, B-4, C-3, D-2"],
        r"""- A: geometric from $n = 0$: $\frac{1}{1 - 1/2} = 2$.
- B: telescoping, $1 - \frac{1}{n + 1} \to 1$.
- C: Euler's sum $\frac{\pi^2}{6}$.
- D: $e = \sum_{n\ge0}\frac{1}{n!}$.

So A-2, B-4, C-3, D-1. Starting A at $n = 1$ would give $1$, the usual slip.""")

# ------------------------------------------------------- assertion-reason (5)
T.assertion_reason(1, ["convergence"],
                   r"The harmonic series $\sum\frac1n$ diverges.",
                   r"For every $n$, $\dfrac{1}{n + 1} + \dfrac{1}{n + 2} + \cdots + \dfrac{1}{2n} \ge \dfrac12$.",
                   0,
                   r"""Both are true. R: each of the $n$ terms is at least $\frac{1}{2n}$, so the block is at least $\frac12$.

So $s_{2n} - s_n \ge \frac12$ for every $n$, and Cauchy's criterion fails with $\varepsilon = \frac12$. R explains A.""")

T.assertion_reason(2, ["ratio-root", "exam-tips"],
                   r"$\displaystyle\sum\frac{n!}{n^n}$ converges.",
                   r"If $a_n > 0$ and $\dfrac{a_{n+1}}{a_n} < 1$ for every $n$, then $\sum a_n$ converges.",
                   2,
                   r"""A is true: $\frac{a_{n+1}}{a_n} = \left(1 + \frac1n\right)^{-n} \to \frac1e < 1$, so the ratio test gives convergence.

R is false: for $a_n = \frac1n$, $\frac{a_{n+1}}{a_n} = \frac{n}{n + 1} < 1$ for every $n$, yet $\sum\frac1n$ diverges. The ratio test needs the limit (or limsup) to be **less than 1**, not each ratio.""")

T.assertion_reason(2, ["abel-pringsheim", "p-series"],
                   r"$\displaystyle\sum_{n=2}^{\infty}\frac{1}{n\ln n}$ converges.",
                   r"For $a_n = \dfrac{1}{n\ln n}$, $\displaystyle\lim_{n\to\infty} n a_n = 0$.",
                   3,
                   r"""A is false: condensation gives $\frac{1}{\ln 2}\sum\frac1k$, which diverges. (Also $\int_2^\infty\frac{dx}{x\ln x} = \infty$.)

R is true: $n a_n = \frac{1}{\ln n} \to 0$. But $n a_n \to 0$ is only the **necessary** condition of Abel–Pringsheim; this series shows the converse fails.""")

T.assertion_reason(2, ["ratio-root", "standard-examples"],
                   r"$\displaystyle\sum\left(1 + \frac1n\right)^{-n^2}$ converges.",
                   r"For $a_n = \left(1 + \dfrac1n\right)^{-n^2}$, $\displaystyle\lim a_n^{1/n} = \frac1e < 1$.",
                   0,
                   r"""Both are true. R: $a_n^{1/n} = \left(1 + \frac1n\right)^{-n} \to \frac1e$.

Since this limit is less than $1$, Cauchy's root test gives A. R explains A.""")

T.assertion_reason(3, ["comparison", "exam-tips"],
                   r"$\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^{1 + 1/n}}$ diverges.",
                   r"For every $n \ge 1$, the exponent $1 + \dfrac1n$ is greater than $1$.",
                   1,
                   r"""A is true: $\dfrac{a_n}{1/n} = n^{-1/n} \to 1$, so by limit comparison it behaves like $\sum\frac1n$ and diverges.

R is true but does not explain A; if anything it suggests convergence. The p-test needs a **fixed** exponent $p > 1$, and here the exponent tends to $1$.""")


def check():
    import sympy as sp
    n, k = sp.symbols("n k", positive=True, integer=True)
    x = sp.symbols("x", positive=True)
    oo = sp.oo

    def num_sum(expr, N=4000, start=1):
        return sum(float(expr.subs(n, i)) for i in range(start, N + 1))

    # q1: counterexample to "n a_n -> 0" without monotonicity; a_n -> 0 for 1/n^2
    sq = lambda i: 1 / i if int(i**0.5) ** 2 == i else 1 / i**2
    assert sum(sq(i) for i in range(1, 200000)) < 2 * float(sp.pi**2 / 6)
    assert all(i * sq(i) == 1 for i in (4, 9, 10000))
    eq(sp.limit(1 / n**2, n, oo), 0, "q1")
    eq(sp.limit((1 / (n + 1) ** 2) / (1 / n**2), n, oo), 1, "q1 ratio")
    # q2
    eq(sp.summation(1 / k**2, (k, 1, oo)), sp.pi**2 / 6, "q2 p=2")
    assert sp.summation(1 / k, (k, 1, oo)) == oo, "q2 p=1"
    assert sp.Sum(1 / sp.sqrt(k), (k, 1, oo)).is_convergent() is sp.false, "q2 p=1/2"
    # q3
    eq(sp.summation(sp.Rational(2, 3) ** k, (k, 1, oo)), 2, "q3")
    eq(sp.summation(sp.Rational(2, 3) ** k, (k, 0, oo)), 3, "q3 distractor")
    # q4
    eq(sp.summation(1 / (k * (k + 1)), (k, 1, oo)), 1, "q4")
    # q5
    a5 = sp.factorial(n) / n**n
    eq(sp.limit(sp.combsimp(a5.subs(n, n + 1) / a5), n, oo), sp.exp(-1), "q5")
    assert abs(num_sum(a5, 60) - float(sp.N(sp.Sum(a5, (n, 1, 200)).doit()))) < 1e-9
    # q6
    eq(sp.limit((1 + 1 / n) ** (-n), n, oo), sp.exp(-1), "q6")
    # q7: ratio limit x; harmonic at x = 1
    eq(sp.limit((n / (n + 1)) * x, n, oo), x, "q7")
    assert sp.summation(1 / k, (k, 1, oo)) == oo
    eq(sp.summation(sp.Rational(1, 2) ** k / k, (k, 1, oo)), sp.log(2), "q7 x=1/2")
    # q8: condensed term
    eq(sp.simplify(2**k / (2**k * sp.log(2**k))), 1 / (k * sp.log(2)), "q8 condensed")
    assert sp.summation(1 / k, (k, 1, oo)) == oo
    assert sp.integrate(1 / (x * sp.log(x)), (x, 2, oo)) == oo
    # q9
    eq(sp.limit(n**sp.Rational(3, 2) * (sp.sqrt(n + 1) - sp.sqrt(n)) / n, n, oo), sp.Rational(1, 2), "q9")
    eq(sp.limit(n / sp.sqrt(n * (n + 1)), n, oo), 1, "q9 d2")
    eq(sp.limit(sp.sin(1 / n) * n, n, oo), 1, "q9 d3")
    eq(sp.summation(sp.sqrt(k + 1) - sp.sqrt(k), (k, 1, 99)), 9, "q9 d1 telescopes")
    # q10
    eq(sp.limit((1 + 1 / n) ** (-n), n, oo), sp.exp(-1), "q10")
    eq(sp.limit(((1 + 1 / n) ** (-n)) ** (1 / n), n, oo), 1, "q10 root")
    # q11
    a = sp.symbols("a", positive=True)
    a11 = a**n * sp.factorial(n) / n**n
    eq(sp.limit(sp.combsimp(a11.subs(n, n + 1) / a11), n, oo), a / sp.E, "q11")
    for i in range(1, 300):  # at a = e terms increase: (1+1/i)^i < e
        assert (1 + sp.Rational(1, i)) ** i < sp.E
    eq(sp.limit(a11.subs(a, sp.E).rewrite(sp.gamma) / sp.sqrt(2 * sp.pi * n), n, oo), 1, "q11 Stirling")
    # q12
    r12 = (2 * n + 2) / (2 * n + 1)
    a12 = sp.factorial(2 * n) / (4**n * sp.factorial(n) ** 2)
    eq(sp.combsimp(a12 / a12.subs(n, n + 1)), r12, "q12 ratio")
    eq(sp.limit(n * (r12 - 1), n, oo), sp.Rational(1, 2), "q12")
    # q13
    a13 = sp.factorial(n) ** 2 / sp.factorial(2 * n) * x**n
    r13 = sp.combsimp(a13.subs(n, n + 1) / a13)
    eq(sp.limit(r13, n, oo), x / 4, "q13")
    eq(sp.simplify(r13.subs(x, 4) - (2 * n + 2) / (2 * n + 1)), 0, "q13 end")
    # q14
    a14 = n**n * x**n / sp.factorial(n)
    r14 = sp.combsimp(a14 / a14.subs(n, n + 1))
    eq(sp.limit(r14, n, oo), 1 / (sp.E * x), "q14")
    eq(sp.limit(n * sp.log(r14.subs(x, sp.exp(-1))), n, oo), sp.Rational(1, 2), "q14 log test")
    # q15: mu = p/2 ; at p = 2, n a_n^2 -> 1/pi
    p = sp.symbols("p", positive=True)
    t = sp.symbols("t", positive=True)  # t = 1/n
    ser = sp.series((1 + t / (2 + t)) ** p, t, 0, 2).removeO()
    eq(sp.expand(ser).coeff(t, 1), p / 2, "q15 mu")
    eq(sp.limit(n * a12.rewrite(sp.gamma) ** 2, n, oo), 1 / sp.pi, "q15 p=2")
    # q16: s_{2n} - s_n for 1/(n ln n) -> 0 (integral bound ln(ln 2n / ln n))
    eq(sp.limit(sp.log(sp.log(2 * x) / sp.log(x)), x, oo), 0, "q16")
    # q17
    eq(sp.limit(n**2 * n**sp.Rational(-3, 2), n, oo), oo, "q17 d1")
    eq(sp.summation(1 / k**sp.Rational(3, 2), (k, 1, oo)), sp.zeta(sp.Rational(3, 2)), "q17 conv")
    # q18
    eq(sp.integrate(1 / (x * sp.log(x) ** 2), (x, 2, oo)), 1 / sp.log(2), "q18")
    eq(sp.N(sp.Integral(1 / (x * sp.log(x) ** 2), (x, 2, 10**8))), sp.N(1 / sp.log(2) - 1 / sp.log(10**8)), "q18 numeric")
    # q19
    a19 = lambda m: sp.Integer(2) ** ((-1) ** m - m)
    eq(a19(5) / a19(4), sp.Rational(1, 8), "q19 even")
    eq(a19(6) / a19(5), 2, "q19 odd")
    for m in (10, 11):
        assert sp.limit(sp.Integer(2) ** (((-1) ** m) / n - 1), n, oo) == sp.Rational(1, 2)
    assert float(sum(a19(m) for m in range(1, 200))) < 3
    # q20
    for i in range(3, 400):
        assert float(sp.Integer(i) ** sp.Rational(1, i) - 1) >= 1 / i
    eq(sp.limit((n ** (1 / n) - 1) ** (1 / n), n, oo), 1, "q20 root")
    eq(sp.limit((n ** (1 / n) - 1) * n / sp.log(n), n, oo), 1, "q20 asymptotic")

    # statements 1
    for i in range(1, 50):
        assert sum(sp.Rational(1, j) for j in range(i + 1, 2 * i + 1)) >= sp.Rational(1, 2)
    # statements 2: 1/n and 1/n^2 both ratio 1; 2^{(-1)^n - n} counterexample checked in q19
    eq(sp.limit(n / (n + 1), n, oo), 1, "S2")
    # statements 3
    assert all(float(sp.log(i) ** 2) < i for i in range(10, 2000, 37))
    eq(sp.limit(sp.log(x) ** 2 / x, x, oo), 0, "S3.1")
    assert sp.integrate(1 / (x * sp.log(x) ** 2), (x, 2, oo)).is_finite
    # match 1
    eq(sp.limit((n**2 / 2**n) ** (1 / n), n, oo), sp.Rational(1, 2), "M1 A")
    eq(sp.limit((n / (n + 1)) ** n, n, oo), sp.exp(-1), "M1 B")
    eq(sp.limit((3**n / n**3) ** (1 / n), n, oo), 3, "M1 C")
    eq(sp.limit((1 / n**5) ** (1 / n), n, oo), 1, "M1 D")
    # match 2
    eq(sp.summation(1 / 2**k, (k, 0, oo)), 2, "M2 A")
    eq(sp.summation(1 / (k * (k + 1)), (k, 1, oo)), 1, "M2 B")
    eq(sp.summation(1 / k**2, (k, 1, oo)), sp.pi**2 / 6, "M2 C")
    eq(sp.summation(1 / sp.factorial(k), (k, 0, oo)), sp.E, "M2 D")
    # AR: harmonic block >= 1/2 (above); 1/n ratio < 1 yet divergent; 1/(n ln n) n a_n -> 0
    eq(sp.limit(n * 1 / (n * sp.log(n)), n, oo), 0, "AR3 R")
    eq(sp.limit(n ** (-1 / n), n, oo), 1, "AR5")
    assert sp.summation(1 / k, (k, 1, oo)) == oo


T.write(check)
