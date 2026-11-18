import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from qlib import Topic, eq

T = Topic("math.analysis.series-arbitrary")

ABS, COND, DIV = r"Absolutely convergent", r"Conditionally convergent", r"Divergent"

# ---------------------------------------------------------------- single (21)
# q1
T.single(1, ["standard-examples"], r"The sum of the series $1 - \dfrac12 + \dfrac13 - \dfrac14 + \cdots$ is",
         [r"$\ln 2$", r"$\dfrac{\pi}{4}$", r"$1$", r"$\dfrac{\pi^2}{12}$"],
         r"""The $2n$th partial sum is
$$S_{2n} = H_{2n} - H_n = \sum_{k=n+1}^{2n}\frac1k \to \int_1^2\frac{dx}{x} = \ln 2,$$
and $S_{2n+1} - S_{2n} = \frac{1}{2n+1} \to 0$. Equivalently, it is $\ln(1 + x)$ at $x = 1$.

$\frac{\pi}{4}$ is the sum of $1 - \frac13 + \frac15 - \cdots$ (odd denominators); $\frac{\pi^2}{12}$ is $\sum\frac{(-1)^{n+1}}{n^2}$.""")

# q2
T.single(1, ["standard-examples"], r"The series $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^n}{n^p}$ is conditionally convergent if and only if",
         [r"$0 < p \le 1$", r"$p > 1$", r"$0 < p < 1$", r"$p \ge 1$"],
         r"""- $p > 1$: $\sum\frac{1}{n^p}$ converges, so the series is **absolutely** convergent.
- $0 < p \le 1$: $\sum\frac1{n^p}$ diverges, but $\frac1{n^p}$ decreases to $0$, so Leibniz gives convergence: **conditional**.
- $p \le 0$: the terms do not tend to $0$: divergent.

The trap is $p = 1$: the alternating harmonic series is conditionally convergent, so $0 < p < 1$ misses it.""")

# q3
T.single(1, ["absolute-convergence"], r"For a series $\sum a_n$ of real terms, which of the following is always true?",
         [r"If $\sum \lvert a_n\rvert$ converges, then $\sum a_n$ converges.",
          r"If $\sum a_n$ converges, then $\sum \lvert a_n\rvert$ converges.",
          r"If $a_n \to 0$, then $\sum a_n$ converges.",
          r"If $\sum a_n$ converges, then $\sum a_n^2$ converges."],
         r"""Absolute convergence implies convergence, by Cauchy's criterion:
$$|a_{n+1} + \cdots + a_m| \le |a_{n+1}| + \cdots + |a_m|.$$

The others fail:
- $\sum\frac{(-1)^n}{n}$ converges, but $\sum\frac1n$ does not.
- $a_n = \frac1n \to 0$, but $\sum\frac1n$ diverges.
- $a_n = \frac{(-1)^n}{\sqrt n}$: $\sum a_n$ converges (Leibniz) but $\sum a_n^2 = \sum\frac1n$ diverges.""")

# q4
T.single(1, ["leibniz-test", "exam-tips"],
         r"Using the Leibniz error bound $\lvert S - S_n\rvert \le u_{n+1}$, the least $n$ for which the partial sum $S_n$ of $\displaystyle\sum_{k=1}^{\infty}\frac{(-1)^{k+1}}{k}$ is guaranteed to differ from $\ln 2$ by less than $\dfrac{1}{100}$ is",
         [r"$100$", r"$99$", r"$101$", r"$10$"],
         r"""The first omitted term is $u_{n+1} = \frac{1}{n+1}$. We need
$$\frac{1}{n+1} < \frac{1}{100} \iff n + 1 > 100 \iff n \ge 100.$$

$99$ gives $u_{100} = \frac1{100}$, which is not **less than** $\frac1{100}$. $10$ comes from confusing this with $\frac{1}{n^2}$-type terms.""")

# q5
T.single(1, ["standard-examples", "exam-tips"], r"The series $\displaystyle\sum_{n=1}^{\infty}(-1)^n\frac{n}{n+1}$ is",
         [DIV, COND, ABS, r"Convergent with sum $0$"],
         r"""The terms $(-1)^n\frac{n}{n+1}$ have modulus $\frac{n}{n+1} \to 1$, so $a_n \not\to 0$ and the series **diverges**.

Leibniz does not apply: $\frac{n}{n+1}$ increases and does not tend to $0$. Alternating signs alone never give convergence.""")

# q6
T.single(2, ["standard-examples"], r"The series $\displaystyle\sum_{n=2}^{\infty}\frac{(-1)^n}{\ln n}$ is",
         [COND, ABS, DIV, r"Convergent only if grouped in pairs"],
         r"""- **Not absolutely:** $\ln n < n$, so $\frac{1}{\ln n} > \frac1n$, and $\sum\frac1n$ diverges.
- **Convergent:** $\frac1{\ln n}$ decreases to $0$, so Leibniz applies.

Hence conditionally convergent. Absolute convergence would need $|a_n|$ to be small like $\frac{1}{n^p}$, $p > 1$; $\frac{1}{\ln n}$ decays far more slowly.""")

# q7
T.single(1, ["ratio-root"], r"The series $\displaystyle\sum_{n=1}^{\infty}\frac{(-2)^n}{n^2}$ is",
         [DIV, ABS, COND, r"Convergent by the Leibniz test"],
         r"""Ratio test on $|a_n| = \frac{2^n}{n^2}$:
$$\left|\frac{a_{n+1}}{a_n}\right| = 2\left(\frac{n}{n+1}\right)^2 \to 2 > 1.$$
A ratio limit above $1$ means $|a_n| \not\to 0$, so $\sum a_n$ itself diverges.

The Leibniz test needs $u_n = \frac{2^n}{n^2}$ decreasing to $0$; it increases without bound.""")

# q8
T.single(2, ["standard-examples"], r"The series $\displaystyle\sum_{n=1}^{\infty}(-1)^n\left(\sqrt{n+1} - \sqrt n\right)$ is",
         [COND, ABS, DIV, r"Convergent with all partial sums positive"],
         r"""Rationalise:
$$u_n = \sqrt{n+1} - \sqrt n = \frac{1}{\sqrt{n+1} + \sqrt n} \sim \frac{1}{2\sqrt n}.$$
- $\sum u_n$ diverges (limit comparison with $\frac1{\sqrt n}$, $p = \frac12$): not absolutely convergent.
- $u_n$ decreases (the denominator increases) and $u_n \to 0$: Leibniz gives convergence.

So conditionally convergent. The first partial sum is $-(\sqrt2 - 1) < 0$, so the last option fails.""")

# q9
T.single(2, ["ratio-root"], r"For $\displaystyle\sum_{n=1}^{\infty}(-1)^n\frac{n!}{n^n}$, the limit $\displaystyle\lim_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|$ equals",
         [r"$\dfrac1e$", r"$e$", r"$1$", r"$0$"],
         r"""$$\left|\frac{a_{n+1}}{a_n}\right| = \frac{(n+1)!}{(n+1)^{n+1}}\cdot\frac{n^n}{n!} = \left(\frac{n}{n+1}\right)^n = \frac{1}{\left(1 + \frac1n\right)^n} \to \frac1e.$$
Since $\frac1e < 1$, the series converges absolutely.

$e$ is the reciprocal slip: $\left(\frac{n+1}{n}\right)^n \to e$.""")

# q10
T.single(2, ["interval-of-convergence"], r"The set of real $x$ for which $\displaystyle\sum_{n=1}^{\infty}\frac{x^n}{n\,2^n}$ converges is",
         [r"$[-2, 2)$", r"$(-2, 2)$", r"$(-2, 2]$", r"$[-2, 2]$"],
         r"""Ratio test: $\left|\frac{a_{n+1}}{a_n}\right| = \frac{n}{n+1}\cdot\frac{|x|}{2} \to \frac{|x|}{2}$. So: absolute convergence for $|x| < 2$, divergence for $|x| > 2$.

Endpoints:
- $x = 2$: $\sum\frac1n$ diverges.
- $x = -2$: $\sum\frac{(-1)^n}{n}$ converges (conditionally).

So the set is $[-2, 2)$. Forgetting to test the endpoints gives $(-2, 2)$.""")

# q11
T.single(2, ["interval-of-convergence"], r"The set of real $x$ for which $\displaystyle\sum_{n=1}^{\infty}\frac{(x-2)^n}{n\,3^n}$ converges is",
         [r"$[-1, 5)$", r"$(-1, 5]$", r"$(-1, 5)$", r"$[-3, 3)$"],
         r"""Ratio limit: $\frac{|x - 2|}{3}$. So the series converges absolutely for $|x - 2| < 3$, i.e. $-1 < x < 5$.

- $x = 5$: $\sum\frac{3^n}{n3^n} = \sum\frac1n$ diverges.
- $x = -1$: $\sum\frac{(-3)^n}{n3^n} = \sum\frac{(-1)^n}{n}$ converges.

So $[-1, 5)$. $[-3, 3)$ forgets the centre $2$; $(-1, 5]$ swaps the endpoints.""")

# q12
T.single(2, ["interval-of-convergence"], r"The set of real $x$ for which $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^n x^n}{\sqrt n}$ converges is",
         [r"$(-1, 1]$", r"$[-1, 1)$", r"$[-1, 1]$", r"$(-1, 1)$"],
         r"""Ratio limit: $|x|$, so absolute convergence for $|x| < 1$ and divergence for $|x| > 1$.

- $x = 1$: $\sum\frac{(-1)^n}{\sqrt n}$ converges by Leibniz (conditionally).
- $x = -1$: $(-1)^n(-1)^n = 1$, so the series is $\sum\frac1{\sqrt n}$, which diverges ($p = \frac12$).

So $(-1, 1]$. The factor $(-1)^n$ moves the convergent endpoint from $-1$ to $+1$; $[-1, 1)$ is the answer for $\sum\frac{x^n}{\sqrt n}$.""")

# q13
T.single(3, ["interval-of-convergence"], r"The set of real $x$ for which $\displaystyle\sum_{n=1}^{\infty}\frac{x^{2n}}{n\,4^n}$ converges is",
         [r"$(-2, 2)$", r"$[-2, 2)$", r"$(-4, 4)$", r"$[-2, 2]$"],
         r"""Only even powers occur, so use the ratio of consecutive **terms**:
$$\left|\frac{a_{n+1}}{a_n}\right| = \frac{n}{n+1}\cdot\frac{x^2}{4} \to \frac{x^2}{4}.$$
Convergence for $x^2 < 4$, i.e. $|x| < 2$; divergence for $|x| > 2$.

At $x = \pm 2$: $x^{2n} = 4^n$, so the series is $\sum\frac1n$, which diverges at **both** endpoints.

So $(-2, 2)$. $[-2, 2)$ copies the pattern of $\sum\frac{x^n}{n}$ without noticing that $x^{2n} > 0$ at $x = -2$; $(-4, 4)$ forgets the square.""")

# q14
T.single(2, ["leibniz-test"],
         r"Let $u_n > 0$ and $u_n \to 0$, but suppose $(u_n)$ is **not** monotone. Then the series $\displaystyle\sum_{n=1}^{\infty}(-1)^{n+1}u_n$",
         [r"may converge or may diverge",
          r"always converges, by the Leibniz test",
          r"always diverges",
          r"always converges, but never absolutely"],
         r"""Without monotonicity the Leibniz test does not apply, and either outcome is possible.

- **Diverges:** $u_{2k-1} = \frac1k$, $u_{2k} = \frac1{k^2}$. Pairing terms, $\sum\left(\frac1k - \frac1{k^2}\right) = \infty$.
- **Converges:** $u_n = \frac{2 + (-1)^n}{n^2}$ is not monotone ($u_3 = \frac19 < u_4 = \frac3{16}$), yet $u_n \le \frac3{n^2}$, so the series converges absolutely.

The second example also kills the last option.""")

# q15
T.single(2, ["leibniz-test"],
         r"$\dfrac1e = \displaystyle\sum_{n=0}^{\infty}\frac{(-1)^n}{n!}$ is approximated by $1 - 1 + \dfrac12 - \dfrac16$. The Leibniz test guarantees that the error is at most",
         [r"$\dfrac1{24}$", r"$\dfrac16$", r"$\dfrac1{120}$", r"$\dfrac1{12}$"],
         r"""For $n \ge 1$, $u_n = \frac1{n!}$ decreases to $0$, so the error is at most the first omitted term:
$$\left|\frac1e - \left(1 - 1 + \frac12 - \frac16\right)\right| \le \frac1{4!} = \frac1{24}.$$
(Indeed $\frac13 - \frac1e \approx -0.0345$, and $0.0345 < \frac1{24} \approx 0.0417$.)

$\frac16$ is the last term **used**, not the first one omitted; $\frac1{120} = \frac1{5!}$ skips a term.""")

# q16
T.single(2, ["abel-dirichlet"], r"For a fixed $x$ with $0 < x < \pi$, the series $\displaystyle\sum_{n=1}^{\infty}\frac{\sin nx}{n}$ is",
         [COND, ABS, DIV, r"Convergent only for $x = \dfrac{\pi}{2}$"],
         r"""**Converges:** for $x \notin 2\pi\Z$, $\left|\sum_{k=1}^n \sin kx\right| \le \frac{1}{\sin(x/2)}$ (bounded), and $\frac1n$ decreases to $0$. Dirichlet's test applies. (The sum is $\frac{\pi - x}{2}$.)

**Not absolutely:** $|\sin nx| \ge \sin^2 nx = \frac{1 - \cos 2nx}{2}$. Here $\sum\frac{1}{2n}$ diverges while $\sum\frac{\cos 2nx}{2n}$ converges (Dirichlet, as $2x \notin 2\pi\Z$), so $\sum\frac{|\sin nx|}{n}$ diverges.

Hence conditionally convergent, for every $x$ in $(0, \pi)$.""")

# q17
T.single(2, ["abel-dirichlet", "exam-tips"], r"The series $\displaystyle\sum_{n=1}^{\infty}\frac{\cos nx}{n}$ converges if and only if",
         [r"$x$ is not an integer multiple of $2\pi$",
          r"$x$ is not an integer multiple of $\pi$",
          r"$x$ is any real number",
          r"$0 < x < \pi$"],
         r"""- $x \notin 2\pi\Z$: the partial sums of $\sum\cos nx$ are bounded by $\frac{1}{|\sin(x/2)|}$ and $\frac1n \downarrow 0$, so Dirichlet's test gives convergence.
- $x = 2k\pi$: $\cos nx = 1$ and the series is $\sum\frac1n$, which diverges.

At $x = \pi$ the series is $\sum\frac{(-1)^n}{n}$, which converges, so "not a multiple of $\pi$" is wrong. Compare $\sum\frac{\sin nx}{n}$, which converges for **every** $x$.""")

# q18
T.single(3, ["rearrangements"],
         r"The rearrangement $1 + \dfrac13 - \dfrac12 + \dfrac15 + \dfrac17 - \dfrac14 + \cdots$ of $1 - \dfrac12 + \dfrac13 - \cdots$ (two positive terms, then one negative term, in turn) has sum",
         [r"$\dfrac32\ln 2$", r"$\ln 2$", r"$\dfrac12\ln 2$", r"$2\ln 2$"],
         r"""Taking $p$ positive terms then $q$ negative terms in turn gives the sum $\ln 2 + \frac12\ln\frac pq$. With $p = 2$, $q = 1$:
$$\ln 2 + \frac12\ln 2 = \frac32\ln 2.$$

Derivation: after $n$ blocks the partial sum is
$$\Big(H_{4n} - \tfrac12 H_{2n}\Big) - \tfrac12 H_n \approx \ln 4n - \tfrac12\ln 2n - \tfrac12\ln n = \tfrac32\ln 2.$$

$\ln 2$ assumes rearranging cannot change the sum, which is true only for absolutely convergent series. $\frac12\ln 2$ is the one-positive, two-negative rearrangement.""")

# q19
T.single(2, ["rearrangements"],
         r"The $n$th term $c_n$ ($n \ge 0$) of the Cauchy product of $\displaystyle\sum_{n=0}^{\infty}\frac1{2^n}$ with itself is",
         [r"$\dfrac{n+1}{2^n}$", r"$\dfrac{1}{4^n}$", r"$\dfrac{n}{2^n}$", r"$\dfrac{n+1}{4^n}$"],
         r"""$$c_n = \sum_{k=0}^{n}\frac1{2^k}\cdot\frac1{2^{n-k}} = \sum_{k=0}^{n}\frac1{2^n} = \frac{n+1}{2^n}.$$
Check: both series converge absolutely to $2$, so by Mertens $\sum c_n = 4$, and indeed $\sum_{n\ge0}\frac{n+1}{2^n} = 4$.

$\frac1{4^n}$ multiplies term by term ($a_n b_n$), which is not the Cauchy product; $\frac{n}{2^n}$ is the off-by-one slip (there are $n + 1$ terms from $k = 0$ to $n$).""")

# q20
T.single(3, ["ratio-root"],
         r"For $\displaystyle\sum_{n=1}^{\infty}(-1)^n\left(\frac{n}{n+1}\right)^{n^2}$, the value of $\displaystyle\lim_{n\to\infty}\lvert a_n\rvert^{1/n}$ is",
         [r"$\dfrac1e$", r"$e$", r"$1$", r"$0$"],
         r"""$$|a_n|^{1/n} = \left(\frac{n}{n+1}\right)^{n} = \frac{1}{\left(1 + \frac1n\right)^n} \to \frac1e < 1,$$
so the series converges absolutely by the root test.

$1$ is the limit of $\frac{n}{n+1}$ itself, forgetting the exponent $n^2$; $e$ inverts the fraction.""")

# q21
T.single(3, ["standard-examples"], r"The series $\displaystyle\sum_{n=2}^{\infty}\frac{(-1)^n}{n\ln n}$ is",
         [COND, ABS, DIV, r"Convergent by the ratio test"],
         r"""- **Not absolutely:** by Cauchy condensation, $\sum\frac{1}{n\ln n}$ behaves like $\sum\frac{2^k}{2^k\, k\ln 2} = \frac{1}{\ln 2}\sum\frac1k$, which diverges.
- **Convergent:** $n\ln n$ increases to $\infty$, so $\frac{1}{n\ln n}$ decreases to $0$; Leibniz applies.

So conditionally convergent. The ratio limit is $1$, so the ratio test decides nothing. (With $(\ln n)^2$ in place of $\ln n$, the series would be absolutely convergent.)""")

# ------------------------------------------------------------ statements (2)
T.statements(2, ["rearrangements", "absolute-convergence"],
             r"Consider the following statements about a series $\sum a_n$ of real terms:",
             [r"If $\sum a_n$ converges absolutely, every rearrangement of it converges to the same sum.",
              r"If $\sum a_n$ converges conditionally, then for every real $s$ some rearrangement of it converges to $s$.",
              r"If $\sum a_n$ converges, then $\sum a_n^2$ converges."],
             [r"1 and 2 only", r"1 only", r"2 and 3 only", r"1, 2 and 3"],
             r"""1. True: Dirichlet's theorem on rearrangements of absolutely convergent series.
2. True: Riemann's rearrangement theorem.
3. False: $a_n = \frac{(-1)^n}{\sqrt n}$ gives a convergent series (Leibniz), but $\sum a_n^2 = \sum\frac1n$ diverges. (Statement 3 is true for **absolutely** convergent series, since then $|a_n| < 1$ eventually and $a_n^2 \le |a_n|$.)""")

T.statements(3, ["abel-dirichlet", "absolute-convergence"],
             r"Consider the following statements about real sequences $(a_n)$ and $(b_n)$:",
             [r"If $\sum a_n$ and $\sum b_n$ both converge, then $\sum a_n b_n$ converges.",
              r"If $\sum a_n$ converges absolutely and $(b_n)$ is bounded, then $\sum a_n b_n$ converges absolutely.",
              r"If the partial sums of $\sum a_n$ are bounded and $b_n \to 0$, then $\sum a_n b_n$ converges."],
             [r"2 only", r"1 and 2 only", r"2 and 3 only", r"1, 2 and 3"],
             r"""1. False: $a_n = b_n = \frac{(-1)^n}{\sqrt n}$; both converge, but $a_n b_n = \frac1n$.
2. True: $|a_n b_n| \le M|a_n|$ with $M = \sup|b_n|$; use comparison.
3. False: Dirichlet's test also needs $(b_n)$ **monotone**. With $a_n = (-1)^n$ and $b_n = \frac{(-1)^n}{n} \to 0$: $a_n b_n = \frac1n$, and the series diverges.""")

# ----------------------------------------------------------------- match (2)
T.match(1, ["standard-examples", "leibniz-test"], r"Match each series in List I with its sum in List II.",
        [r"$\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}$", r"$\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{2n-1}$",
         r"$\displaystyle\sum_{n=0}^{\infty}\frac{(-1)^{n}}{n!}$", r"$\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n^2}$"],
        [r"$\dfrac1e$", r"$\dfrac{\pi^2}{12}$", r"$\ln 2$", r"$\dfrac{\pi}{4}$"],
        [r"A-3, B-4, C-1, D-2", r"A-4, B-3, C-1, D-2", r"A-3, B-2, C-1, D-4", r"A-3, B-4, C-2, D-1"],
        r"""- A: $\ln(1 + x)$ at $x = 1$: $\ln 2$.
- B: $\tan^{-1}x$ at $x = 1$ (Gregory–Leibniz): $\frac{\pi}{4}$.
- C: $e^{x}$ at $x = -1$: $\frac1e$.
- D: $\sum\frac{(-1)^{n+1}}{n^2} = \left(1 - \frac{2}{2^2}\right)\sum\frac1{n^2} = \frac12\cdot\frac{\pi^2}{6} = \frac{\pi^2}{12}$.

So A-3, B-4, C-1, D-2. A and B are conditionally convergent; C and D absolutely.""")

T.match(3, ["interval-of-convergence"], r"Match each series in List I with the set of real $x$ for which it converges, in List II.",
        [r"$\displaystyle\sum_{n=1}^{\infty}\frac{x^n}{n}$", r"$\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n+1}x^n}{n}$",
         r"$\displaystyle\sum_{n=1}^{\infty}\frac{x^n}{n^2}$", r"$\displaystyle\sum_{n=1}^{\infty}x^n$"],
        [r"$(-1, 1)$", r"$[-1, 1]$", r"$(-1, 1]$", r"$[-1, 1)$"],
        [r"A-4, B-3, C-2, D-1", r"A-3, B-4, C-2, D-1", r"A-4, B-3, C-1, D-2", r"A-4, B-2, C-3, D-1"],
        r"""All four have ratio limit $|x|$, so each converges on $(-1, 1)$ and diverges for $|x| > 1$. Only the endpoints differ:
- A: $x = 1$ gives $\sum\frac1n$ (diverges); $x = -1$ gives $\sum\frac{(-1)^n}{n}$ (converges): $[-1, 1)$.
- B: $x = 1$ gives $\sum\frac{(-1)^{n+1}}{n}$ (converges); $x = -1$ gives $-\sum\frac1n$ (diverges): $(-1, 1]$.
- C: $\sum\frac{1}{n^2}$ converges, so both endpoints converge absolutely: $[-1, 1]$.
- D: at $x = \pm1$ the terms do not tend to $0$: $(-1, 1)$.

So A-4, B-3, C-2, D-1.""")

# ------------------------------------------------------- assertion-reason (5)
T.assertion_reason(1, ["leibniz-test"],
                   r"The series $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}$ converges.",
                   r"The sequence $\left(\dfrac1n\right)$ is monotone decreasing and tends to $0$.",
                   0,
                   r"""Both are true, and R is exactly the hypothesis of the Leibniz test, which gives A. So R explains A.""")

T.assertion_reason(2, ["absolute-convergence", "standard-examples"],
                   r"The series $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^n}{n}$ is not absolutely convergent.",
                   r"The series $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^n}{n}$ is convergent.",
                   1,
                   r"""A is true: $\sum\left|\frac{(-1)^n}{n}\right| = \sum\frac1n$ diverges.

R is true by Leibniz.

But convergence does not explain the failure of absolute convergence; that comes from the divergence of the harmonic series. Together, A and R say that the series is conditionally convergent.""")

T.assertion_reason(2, ["leibniz-test", "exam-tips"],
                   r"The series $\displaystyle\sum_{n=1}^{\infty}(-1)^n\frac{n+1}{n}$ converges by the Leibniz test.",
                   r"The sequence $\left(\dfrac{n+1}{n}\right)$ is monotone decreasing.",
                   3,
                   r"""R is true: $\frac{n+1}{n} = 1 + \frac1n$ decreases.

A is false: $1 + \frac1n \to 1$, not $0$, so the terms do not tend to $0$ and the series diverges. Monotonicity alone is not enough for the Leibniz test; the terms must also tend to $0$.""")

T.assertion_reason(3, ["rearrangements"],
                   r"The Cauchy product of $\displaystyle\sum_{n=0}^{\infty}\frac{(-1)^n}{(n+1)^2}$ with itself converges.",
                   r"The Cauchy product of any two convergent series converges.",
                   2,
                   r"""A is true: $\sum\frac{(-1)^n}{(n+1)^2}$ converges absolutely ($p = 2$), and by Mertens' theorem the Cauchy product of an absolutely convergent series with a convergent one converges (to the product of the sums).

R is false: for $a_n = b_n = \frac{(-1)^n}{\sqrt{n+1}}$, both convergent by Leibniz,
$$|c_n| = \sum_{k=0}^{n}\frac{1}{\sqrt{(k+1)(n-k+1)}} \ge \frac{2(n+1)}{n+2} \to 2,$$
using $(k+1)(n-k+1) \le \left(\frac{n+2}{2}\right)^2$. So $c_n \not\to 0$ and the product diverges.""")

T.assertion_reason(3, ["ratio-root", "exam-tips"],
                   r"If $\displaystyle\lim_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right| = 2$, then $\sum a_n$ diverges.",
                   r"If $\displaystyle\lim_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right| > 1$, then $a_n$ does not tend to $0$.",
                   0,
                   r"""R is true: if the limit $L$ exceeds $1$, then $|a_{n+1}| > |a_n|$ for all large $n$, so $|a_n|$ eventually increases and cannot tend to $0$.

A follows from R: terms not tending to $0$ force divergence of $\sum a_n$ itself (not merely of $\sum|a_n|$). So R explains A.

Contrast: showing $\sum|a_n| = \infty$ by comparison would not prove that $\sum a_n$ diverges.""")


def check():
    import mpmath as mp
    import sympy as sp
    n, k, x = sp.symbols("n k x", integer=True, positive=True)
    xr = sp.symbols("xr", real=True)
    oo = sp.oo

    def conv(expr, lo=1):
        return sp.Sum(expr, (n, lo, oo)).is_convergent()

    def classify(expr, lo=1):
        if sp.Sum(sp.Abs(expr), (n, lo, oo)).is_convergent():
            return "abs"
        return "cond" if conv(expr, lo) else "div"

    def ratio_lim(expr):
        return sp.limit(sp.Abs(sp.simplify(expr.subs(n, n + 1) / expr)), n, oo)

    # q1
    eq(sp.summation((-1) ** (n + 1) / n, (n, 1, oo)), sp.log(2), "q1")
    assert abs(float(mp.nsum(lambda j: (-1) ** (j + 1) / j, [1, mp.inf])) - float(sp.log(2))) < 1e-10
    # q2: p = 1/2, 1 conditional; p = 2 absolute; p = 0 divergent
    assert classify((-1) ** n / sp.sqrt(n)) == "cond"
    assert classify((-1) ** n / n) == "cond"
    assert classify((-1) ** n / n ** 2) == "abs"
    eq(sp.limit(1 / n ** 0, n, oo), 1, "q2 p=0 terms do not -> 0")
    # q3: counterexamples
    assert conv((-1) ** n / n) and not conv(1 / n)
    assert conv((-1) ** n / sp.sqrt(n)) and not conv(((-1) ** n / sp.sqrt(n)) ** 2)
    assert conv(1 / n ** 2)  # abs => conv instance
    # q4
    least = min(j for j in range(1, 1000) if sp.Rational(1, j + 1) < sp.Rational(1, 100))
    eq(least, 100, "q4")
    # q5
    eq(sp.limit(n / (n + 1), n, oo), 1, "q5 |a_n| -> 1")
    assert classify((-1) ** n * n / (n + 1)) == "div"
    # q6
    assert not conv(1 / sp.log(n), 2)
    assert conv((-1) ** n / sp.log(n), 2)
    # q7
    eq(ratio_lim((-2) ** n / n ** 2), 2, "q7")
    # q8
    u8 = sp.sqrt(n + 1) - sp.sqrt(n)
    eq(sp.limit(u8 * 2 * sp.sqrt(n), n, oo), 1, "q8 ~ 1/(2 sqrt n)")
    assert not conv(1 / sp.sqrt(n))
    assert all(float(u8.subs(n, j + 1)) < float(u8.subs(n, j)) for j in range(1, 300))
    eq(sp.limit(u8, n, oo), 0, "q8 -> 0")
    # q9
    eq(ratio_lim(sp.factorial(n) / n ** n), sp.exp(-1), "q9")
    # q10–q13: open interval by ratio limit, then endpoints
    eq(sp.limit(n / (n + 1), n, oo) / 2, sp.Rational(1, 2), "q10 ratio |x|/2")
    assert not conv(2 ** n / (n * 2 ** n)) and conv((-2) ** n / (n * 2 ** n))
    assert not conv(3 ** n / (n * 3 ** n)) and conv((-3) ** n / (n * 3 ** n))  # q11 x=5, x=-1
    assert sorted(sp.solve(sp.Eq(sp.Abs(xr - 2) / 3, 1), xr)) == [-1, 5]
    assert conv((-1) ** n * 1 ** n / sp.sqrt(n)) and not conv((-1) ** n * (-1) ** n / sp.sqrt(n))  # q12
    assert not conv(2 ** (2 * n) / (n * 4 ** n)) and not conv((-2) ** (2 * n) / (n * 4 ** n))  # q13 both ends
    eq(sp.limit((n / (n + 1)) * xr ** 2 / 4, n, oo).subs(xr, 2), 1, "q13 radius 2")
    # q14
    assert not conv(1 / n - 1 / n ** 2)  # paired divergent example
    u14 = (2 + (-1) ** n) / n ** 2
    assert float(u14.subs(n, 3)) < float(u14.subs(n, 4))
    assert conv(3 / n ** 2)
    # q15
    s3 = 1 - 1 + sp.Rational(1, 2) - sp.Rational(1, 6)
    eq(sp.Rational(1, sp.factorial(4)), sp.Rational(1, 24), "q15 bound")
    assert abs(sp.N(sp.exp(-1) - s3)) < sp.Rational(1, 24)
    eq(sp.summation((-1) ** n / sp.factorial(n), (n, 0, oo)), sp.exp(-1), "q15 sum")
    # q16: closed form of partial sums, bound, and the sum (pi - x)/2 numerically at x = 1
    t = sp.symbols("t", real=True)
    for N in range(1, 8):
        eq(sum(sp.sin(j * t) for j in range(1, N + 1)).subs(t, sp.Rational(7, 10)),
           (sp.sin(N * t / 2) * sp.sin((N + 1) * t / 2) / sp.sin(t / 2)).subs(t, sp.Rational(7, 10)), "q16 Lagrange")
    S = mp.nsum(lambda j: mp.sin(j) / j, [1, mp.inf])
    assert abs(float(S) - float((sp.pi - 1) / 2)) < 1e-8
    # |sin| >= sin^2, sum 1/(2n) diverges
    assert not conv(1 / (2 * n))
    # q17
    assert not conv(sp.cos(2 * sp.pi * n) / n)
    assert conv((-1) ** n / n)  # x = pi converges
    S17 = mp.nsum(lambda j: mp.cos(j) / j, [1, mp.inf])
    assert abs(float(S17) + float(sp.log(2 * sp.sin(sp.Rational(1, 2))))) < 1e-8
    # q18: blocks 1/(4k-3) + 1/(4k-1) - 1/(2k)
    S18 = mp.nsum(lambda j: 1 / (4 * j - 3) + 1 / (4 * j - 1) - 1 / (2 * j), [1, mp.inf])
    assert abs(float(S18) - float(sp.Rational(3, 2) * sp.log(2))) < 1e-10
    S18b = mp.nsum(lambda j: 1 / (2 * j - 1) - 1 / (4 * j - 2) - 1 / (4 * j), [1, mp.inf])
    assert abs(float(S18b) - float(sp.log(2) / 2)) < 1e-10
    # q19
    nn = sp.symbols("nn", integer=True, nonnegative=True)
    kk = sp.symbols("kk", integer=True, nonnegative=True)
    eq(sp.summation(sp.Rational(1, 2) ** kk * sp.Rational(1, 2) ** (nn - kk), (kk, 0, nn)), (nn + 1) / 2 ** nn, "q19")
    eq(sp.summation((nn + 1) / 2 ** nn, (nn, 0, oo)), 4, "q19 Mertens")
    # q20
    eq(sp.limit((n / (n + 1)) ** n, n, oo), sp.exp(-1), "q20")
    # q21
    assert not conv(1 / (n * sp.log(n)), 2)
    assert conv((-1) ** n / (n * sp.log(n)), 2)
    assert conv(1 / (n * sp.log(n) ** 2), 2)
    eq(ratio_lim(1 / (n * sp.log(n))), 1, "q21 ratio inconclusive")
    # statements 1: (3) false
    assert not conv(1 / n)
    # statements 2: (1) and (3) false via 1/n; (2) instance
    assert conv(1 / n ** 2)
    # match 1
    eq(sp.summation((-1) ** (n + 1) / n, (n, 1, oo)), sp.log(2), "m1 A")
    eq(sp.summation((-1) ** (n + 1) / (2 * n - 1), (n, 1, oo)), sp.pi / 4, "m1 B")
    eq(sp.summation((-1) ** nn / sp.factorial(nn), (nn, 0, oo)), sp.exp(-1), "m1 C")
    eq(sp.summation((-1) ** (n + 1) / n ** 2, (n, 1, oo)), sp.pi ** 2 / 12, "m1 D")
    # match 2 endpoints
    assert (not conv(1 / n)) and conv((-1) ** n / n)                        # A [-1,1)
    assert conv((-1) ** (n + 1) / n) and not conv(-1 / n)                   # B (-1,1]
    assert conv(1 / n ** 2) and conv((-1) ** n / n ** 2)                    # C [-1,1]
    assert not conv(1 + 0 * n) and not conv((-1) ** n + 0 * n)              # D (-1,1)
    # AR4: Cauchy product of (-1)^n/sqrt(n+1) with itself: |c_n| >= 2(n+1)/(n+2)
    for N in range(0, 60):
        c = sum(1 / mp.sqrt((j + 1) * (N - j + 1)) for j in range(N + 1))
        assert c >= 2 * (N + 1) / (N + 2) - 1e-12
    assert conv(1 / (n + 1) ** 2)
    # AR5 instance: ratio 2 => |a_n| = 2^n -> oo
    eq(sp.limit(2 ** n / n ** 2, n, oo), oo, "AR5 terms blow up")


T.write(check)
