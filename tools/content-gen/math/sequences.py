import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from qlib import Topic, eq

T = Topic("math.analysis.sequences")

# ---------------------------------------------------------------- single (20)
# q1
T.single(1, ["limit-algebra", "exam-tips"], r"$\displaystyle\lim_{n\to\infty} \frac{3n^2 + 2n}{5n^2 - 1}$ equals",
         [r"$\dfrac35$", r"$0$", r"$1$", r"$+\infty$"],
         r"""Divide the numerator and the denominator by $n^2$:
$$\frac{3 + \frac2n}{5 - \frac{1}{n^2}} \to \frac{3}{5}.$$
Equal degrees give the ratio of the leading coefficients.

$0$ would need a lower-degree numerator, and $+\infty$ a higher-degree one.""")

# q2
T.single(1, ["monotone-e"], r"$\displaystyle\lim_{n\to\infty} \left(1 + \frac1n\right)^{2n}$ equals",
         [r"$e^2$", r"$e$", r"$2e$", r"$1$"],
         r"""Write it as a square of the sequence that defines $e$:
$$\left(1 + \frac1n\right)^{2n} = \left[\left(1 + \frac1n\right)^n\right]^2 \to e^2.$$
The square of a convergent sequence converges to the square of the limit.

$1$ is the "$1^\infty$" trap: the base tends to $1$, but the exponent grows.""")

# q3
T.single(1, ["cauchy-limit-theorems", "standard-limits"], r"$\displaystyle\lim_{n\to\infty} n^{1/n}$ equals",
         [r"$1$", r"$0$", r"$e$", r"$+\infty$"],
         r"""Take $a_n = n$. Then $\frac{a_{n+1}}{a_n} = \frac{n+1}{n} \to 1$, so by Cauchy's second limit theorem
$$n^{1/n} = a_n^{1/n} \to 1.$$
Check: $10^{1/10} \approx 1.26$ and $1000^{1/1000} \approx 1.007$.

$+\infty$ ignores the shrinking exponent; $0$ ignores the growing base.""")

# q4
T.single(2, ["standard-limits"],
         r"Let $x_1 = \sqrt2$ and $x_{n+1} = \sqrt{2 + x_n}$ for $n \ge 1$. Then $\displaystyle\lim_{n\to\infty} x_n$ equals",
         [r"$2$", r"$-1$", r"$\sqrt2$", r"$\dfrac{1 + \sqrt5}{2}$"],
         r"""By induction $0 < x_n < 2$ and
$$x_{n+1}^2 - x_n^2 = (2 - x_n)(1 + x_n) > 0,$$
so $(x_n)$ is increasing and bounded above. It converges to some $l$, and $l^2 = 2 + l$ gives $l = 2$ or $l = -1$. All terms are positive, so $l = 2$.

$-1$ is the rejected root. $\frac{1 + \sqrt5}{2}$ is the limit of $x_{n+1} = \sqrt{1 + x_n}$.""")

# q5
T.single(2, ["cauchy-limit-theorems"], r"$\displaystyle\lim_{n\to\infty} \frac{(n!)^{1/n}}{n}$ equals",
         [r"$\dfrac1e$", r"$e$", r"$1$", r"$0$"],
         r"""Write $\frac{(n!)^{1/n}}{n} = \left(\frac{n!}{n^n}\right)^{1/n}$ and let $a_n = \frac{n!}{n^n}$. Then
$$\frac{a_{n+1}}{a_n} = \frac{(n+1)!}{(n+1)^{n+1}}\cdot\frac{n^n}{n!} = \left(\frac{n}{n+1}\right)^n = \frac{1}{\left(1 + \frac1n\right)^n} \to \frac1e.$$
By Cauchy's second limit theorem, $a_n^{1/n} \to \frac1e$.

$e$ is the limit of the reciprocal $\frac{n}{(n!)^{1/n}}$. $0$ comes from $\frac{n!}{n^n} \to 0$, forgetting the $n$-th root.""")

# q7
T.single(2, ["limit-algebra"],
         r"$\displaystyle\lim_{n\to\infty} \left(\frac{1}{\sqrt{n^2 + 1}} + \frac{1}{\sqrt{n^2 + 2}} + \cdots + \frac{1}{\sqrt{n^2 + n}}\right)$ equals",
         [r"$1$", r"$0$", r"$\dfrac12$", r"$+\infty$"],
         r"""There are $n$ terms, each between $\frac{1}{\sqrt{n^2 + n}}$ and $\frac{1}{\sqrt{n^2 + 1}}$. So
$$\frac{n}{\sqrt{n^2 + n}} \le c_n \le \frac{n}{\sqrt{n^2 + 1}}.$$
Both bounds tend to $1$, so $c_n \to 1$ by the sandwich rule.

$0$ comes from "each term tends to $0$": that argument fails because the number of terms grows with $n$.""")

# q8
T.single(1, ["limit-definition", "exam-tips"], r"Which of the following sequences is bounded but not convergent?",
         [r"$\left((-1)^n\right)$", r"$\left(\dfrac1n\right)$", r"$\left(\dfrac{(-1)^n}{n}\right)$", r"$(n)$"],
         r"""$(-1)^n$ takes only the values $\pm1$, so it is bounded. Its even terms tend to $1$ and its odd terms to $-1$, so it does not converge.

$\frac1n$ and $\frac{(-1)^n}{n}$ both converge to $0$; $(n)$ is unbounded.""")

# q9
T.single(2, ["subsequences"],
         r"For $a_n = (-1)^n\left(1 + \dfrac1n\right)$, the values of $\displaystyle\limsup_{n\to\infty} a_n$ and $\displaystyle\liminf_{n\to\infty} a_n$ are respectively",
         [r"$1$ and $-1$", r"$\dfrac32$ and $-2$", r"$1$ and $1$", r"$0$ and $0$"],
         r"""The even terms $1 + \frac{1}{2k} \to 1$ and the odd terms $-\left(1 + \frac{1}{2k-1}\right) \to -1$. These are the only subsequential limits, so
$$\limsup a_n = 1, \qquad \liminf a_n = -1.$$

$\frac32$ and $-2$ are the $\sup$ and $\inf$ of the terms ($a_2 = \frac32$, $a_1 = -2$). Each is attained once, and finitely many terms do not affect $\limsup$ or $\liminf$.""")

# q10
T.single(1, ["limit-definition"], r"For the sequence $a_n = \dfrac{n}{n+1}$, $n \ge 1$, which statement is correct?",
         [r"$\inf a_n = \dfrac12$ and $\sup a_n = 1$; the supremum is not attained",
          r"$\inf a_n = 0$ and $\sup a_n = 1$",
          r"$\inf a_n = \dfrac12$ and $\sup a_n = 1$; the supremum is attained",
          r"$\inf a_n = \dfrac12$ and the sequence is not bounded above"],
         r"""$a_n = 1 - \frac{1}{n+1}$ increases. The least term is $a_1 = \frac12$, so $\inf = \frac12$ (attained). The terms approach $1$ but $a_n < 1$ always, so $\sup = 1$ is not attained.

$\inf = 0$ would be the value at $n = 0$, which is not a term.""")

# q11
T.single(2, ["limit-definition"],
         r"For $a_n = \dfrac{n+1}{n}$, the least positive integer $N$ such that $|a_n - 1| < \dfrac{1}{100}$ for all $n \ge N$ is",
         [r"$101$", r"$100$", r"$99$", r"$10$"],
         r"""$$|a_n - 1| = \frac1n < \frac{1}{100} \iff n > 100.$$
So the inequality holds for all $n \ge 101$, and fails at $n = 100$ (where $\frac1n = \frac{1}{100}$, not less).

$100$ is the off-by-one slip from the strict inequality.""")

# q12
T.single(3, ["cauchy-limit-theorems"], r"$\displaystyle\lim_{n\to\infty} \left(\frac{n^n}{n!}\right)^{1/n}$ equals",
         [r"$e$", r"$\dfrac1e$", r"$1$", r"$+\infty$"],
         r"""Let $a_n = \frac{n^n}{n!}$. Then
$$\frac{a_{n+1}}{a_n} = \frac{(n+1)^{n+1}}{(n+1)!}\cdot\frac{n!}{n^n} = \left(1 + \frac1n\right)^n \to e.$$
By Cauchy's second limit theorem, $a_n^{1/n} \to e$.

$\frac1e$ is the limit of the reciprocal $\left(\frac{n!}{n^n}\right)^{1/n}$.""")

# q13
T.single(2, ["limit-algebra"], r"$\displaystyle\lim_{n\to\infty} \left(\sqrt{n^2 + n} - n\right)$ equals",
         [r"$\dfrac12$", r"$0$", r"$1$", r"$+\infty$"],
         r"""Rationalise:
$$\sqrt{n^2 + n} - n = \frac{n}{\sqrt{n^2 + n} + n} = \frac{1}{\sqrt{1 + \frac1n} + 1} \to \frac12.$$

$0$ comes from "$\sqrt{n^2 + n} \approx n$", which loses the first-order term: $\sqrt{n^2 + n} \approx n + \frac12$.""")

# q14
T.single(3, ["standard-limits", "nested-cauchy"],
         r"Let $x_1 = 1$ and $x_{n+1} = \dfrac{1}{1 + x_n}$ for $n \ge 1$. Then $\displaystyle\lim_{n\to\infty} x_n$ equals",
         [r"$\dfrac{\sqrt5 - 1}{2}$", r"$\dfrac{-1 - \sqrt5}{2}$", r"$\dfrac12$", r"$\dfrac{1 + \sqrt5}{2}$"],
         r"""The terms $1, \frac12, \frac23, \frac35, \dots$ are not monotone, but all lie in $\left[\frac12, 1\right]$, so
$$|x_{n+2} - x_{n+1}| = \frac{|x_{n+1} - x_n|}{(1 + x_n)(1 + x_{n+1})} \le \frac49|x_{n+1} - x_n|.$$
The sequence is contractive, hence Cauchy, hence convergent. Its limit satisfies $l = \frac{1}{1 + l}$, i.e. $l^2 + l - 1 = 0$, and $l > 0$:
$$l = \frac{\sqrt5 - 1}{2} \approx 0.618.$$

$\frac{-1 - \sqrt5}{2}$ is the negative root. $\frac{1 + \sqrt5}{2}$ is the reciprocal, the limit of the Fibonacci ratios $\frac{F_{n+1}}{F_n}$.""")

# q15
T.single(2, ["limit-definition"],
         r"Which of the following sequences is unbounded but tends neither to $+\infty$ nor to $-\infty$?",
         [r"$\left((-1)^n n\right)$", r"$\left(n^2\right)$", r"$\left(-\sqrt n\right)$", r"$\left((-1)^n\right)$"],
         r"""$(-1)^n n$: the even terms tend to $+\infty$ and the odd terms to $-\infty$. It is unbounded, but neither limit holds; it oscillates infinitely.

$n^2 \to +\infty$ and $-\sqrt n \to -\infty$. $(-1)^n$ oscillates, but it is bounded.""")

# q16
T.single(3, ["cauchy-limit-theorems"],
         r"If $a_n \to l$ (finite), then $\displaystyle\lim_{n\to\infty} \frac{a_1 + 2a_2 + 3a_3 + \cdots + n a_n}{n^2}$ equals",
         [r"$\dfrac{l}{2}$", r"$l$", r"$0$", r"$2l$"],
         r"""By Stolz–Cesàro with $x_n = a_1 + 2a_2 + \cdots + n a_n$ and $y_n = n^2$ (increasing to $\infty$):
$$\frac{x_n - x_{n-1}}{y_n - y_{n-1}} = \frac{n a_n}{2n - 1} \to \frac{l}{2}.$$
Check with $a_n = l$ for all $n$: $\frac{l(1 + 2 + \cdots + n)}{n^2} = \frac{l\,n(n+1)}{2n^2} \to \frac l2$.

$l$ comes from applying Cauchy's first theorem without the weights.""")

# q17
T.single(2, ["nested-cauchy"], r"Which of the following intersections is empty?",
         [r"$\displaystyle\bigcap_{n=1}^{\infty} \left(0, \frac1n\right)$",
          r"$\displaystyle\bigcap_{n=1}^{\infty} \left[0, \frac1n\right]$",
          r"$\displaystyle\bigcap_{n=1}^{\infty} \left[-\frac1n, \frac1n\right]$",
          r"$\displaystyle\bigcap_{n=1}^{\infty} \left[1 - \frac1n, 1 + \frac1n\right]$"],
         r"""For $x > 0$, the Archimedean property gives $n$ with $\frac1n < x$, so $x \notin \left(0, \frac1n\right)$; and $0$ is in none of them. The intersection is empty.

The other three are nested **closed bounded** intervals with lengths $\to 0$, so by the nested interval theorem each meets in one point: $\{0\}$, $\{0\}$ and $\{1\}$. The theorem needs closed intervals.""")

# q18
T.single(2, ["nested-cauchy", "exam-tips"], r"Which of the following sequences is **not** a Cauchy sequence?",
         [r"$s_n = 1 + \dfrac12 + \dfrac13 + \cdots + \dfrac1n$",
          r"$t_n = 1 + \dfrac{1}{2^2} + \dfrac{1}{3^2} + \cdots + \dfrac{1}{n^2}$",
          r"$u_n = \dfrac{(-1)^n}{n}$",
          r"$v_n = \dfrac{\sin n}{n}$"],
         r"""$$s_{2n} - s_n = \frac{1}{n+1} + \cdots + \frac{1}{2n} \ge \frac12$$
for every $n$, so $(s_n)$ is not Cauchy (it diverges to $+\infty$).

$t_n$ converges (to $\frac{\pi^2}{6}$); $u_n \to 0$ and $v_n \to 0$ (null times bounded). In $\R$ every convergent sequence is Cauchy.""")

# q19
T.single(3, ["cauchy-limit-theorems"], r"$\displaystyle\lim_{n\to\infty} \left(\frac{(2n)!}{(n!)^2}\right)^{1/n}$ equals",
         [r"$4$", r"$2$", r"$1$", r"$e^2$"],
         r"""Let $a_n = \frac{(2n)!}{(n!)^2}$. Then
$$\frac{a_{n+1}}{a_n} = \frac{(2n+2)(2n+1)}{(n+1)^2} = \frac{2(2n+1)}{n+1} \to 4.$$
By Cauchy's second limit theorem, $a_n^{1/n} \to 4$. (Check: $a_n = \binom{2n}{n} \le 4^n$.)

$2$ keeps only one factor of $2n + 1$ over $n + 1$.""")

# q20
T.single(2, ["limit-algebra", "exam-tips"], r"$\displaystyle\lim_{n\to\infty} \left(2^n + 3^n\right)^{1/n}$ equals",
         [r"$3$", r"$5$", r"$2$", r"$6$"],
         r"""$3^n \le 2^n + 3^n \le 2\cdot 3^n$, so
$$3 \le \left(2^n + 3^n\right)^{1/n} \le 3\cdot 2^{1/n} \to 3.$$
By the sandwich rule the limit is $3$, the larger base.

$5 = 2 + 3$ wrongly treats the $n$-th root as additive.""")

# ---------------------------------------------------------------- monotone (single, easy)
# q21
T.single(1, ["monotone-e"], r"The sequence $a_n = \left(1 + \dfrac1n\right)^n$, $n \ge 1$, is",
         [r"strictly increasing and bounded above by $3$",
          r"strictly decreasing and bounded below by $2$",
          r"strictly increasing and unbounded",
          r"not monotone but bounded"],
         r"""In the binomial expansion
$$a_n = 1 + 1 + \frac{1}{2!}\Big(1 - \frac1n\Big) + \frac{1}{3!}\Big(1 - \frac1n\Big)\Big(1 - \frac2n\Big) + \cdots,$$
each bracket grows with $n$ and a new positive term appears, so $a_n$ strictly increases. Since $\frac{1}{k!} \le \frac{1}{2^{k-1}}$, $a_n < 1 + 2 = 3$. So $a_n \uparrow e$.

The decreasing one is $\left(1 + \frac1n\right)^{n+1}$, which decreases to $e$.""")

# ---------------------------------------------------------------- statements (3)
T.statements(1, ["limit-definition", "subsequences"], r"Consider the following statements about sequences of real numbers:",
             [r"Every convergent sequence is bounded.",
              r"Every bounded sequence is convergent.",
              r"Every bounded sequence has a convergent subsequence."],
             [r"1 and 3 only", r"1 only", r"1, 2 and 3", r"2 and 3 only"],
             r"""1. True: with $\varepsilon = 1$, all terms from some $N$ on lie in $(l - 1, l + 1)$, and finitely many terms are bounded.
2. False: $(-1)^n$ is bounded but not convergent.
3. True: the Bolzano–Weierstrass theorem. For $(-1)^n$, the even terms form a convergent subsequence.""")

T.statements(3, ["limit-algebra", "exam-tips"], r"Let $(a_n)$ and $(b_n)$ be sequences of real numbers. Consider the following statements:",
             [r"If $a_n \to 0$ and $(b_n)$ is bounded, then $a_n b_n \to 0$.",
              r"If $(a_n)$ and $(a_n + b_n)$ both converge, then $(b_n)$ converges.",
              r"If $(a_n)$ and $(a_n b_n)$ both converge, then $(b_n)$ converges."],
             [r"1 and 2 only", r"1 only", r"2 and 3 only", r"1, 2 and 3"],
             r"""1. True: if $|b_n| \le M$, then $|a_n b_n| \le M|a_n| \to 0$.
2. True: $b_n = (a_n + b_n) - a_n$ is a difference of convergent sequences.
3. False: $a_n = \frac1n \to 0$ and $b_n = n$ give $a_n b_n = 1$, convergent, while $(b_n)$ diverges. Division needs $\lim a_n \ne 0$.""")

T.statements(2, ["monotone-e", "limit-algebra", "exam-tips"], r"Consider the following statements about a sequence $(a_n)$ of real numbers:",
             [r"A monotone sequence converges if and only if it is bounded.",
              r"If $|a_n| \to |l|$, then $a_n \to l$.",
              r"If $a_n \to l$, then $|a_n| \to |l|$."],
             [r"1 and 3 only", r"1 only", r"2 and 3 only", r"1, 2 and 3"],
             r"""1. True: convergent sequences are bounded, and bounded monotone sequences converge (to the sup or inf).
2. False: $a_n = (-1)^n$ has $|a_n| = 1 \to 1$, but $(a_n)$ diverges. (It is true when $l = 0$.)
3. True: $\big||a_n| - |l|\big| \le |a_n - l| \to 0$.""")

# ---------------------------------------------------------------- match (2)
T.match(2, ["monotone-e", "cauchy-limit-theorems", "standard-limits"],
        r"Match each sequence in List I with its limit in List II.",
        [r"$\left(1 + \dfrac1n\right)^n$", r"$n^{1/n}$", r"$\dfrac{(n!)^{1/n}}{n}$", r"$\left(1 + \dfrac{1}{2n}\right)^n$"],
        [r"$1$", r"$\sqrt e$", r"$e$", r"$\dfrac1e$"],
        [r"A-3, B-1, C-4, D-2", r"A-3, B-2, C-4, D-1", r"A-3, B-1, C-2, D-4", r"A-4, B-1, C-3, D-2"],
        r"""- A: the definition of $e$.
- B: Cauchy's second theorem with $a_n = n$: $\frac{n+1}{n} \to 1$.
- C: $\left(\frac{n!}{n^n}\right)^{1/n}$; the ratio is $\left(1 + \frac1n\right)^{-n} \to \frac1e$.
- D: $\left[\left(1 + \frac{1}{2n}\right)^{2n}\right]^{1/2} \to e^{1/2}$.

So A-3, B-1, C-4, D-2. Swapping C and A confuses $\frac{(n!)^{1/n}}{n}$ with its reciprocal.""")

T.match(3, ["subsequences"],
        r"Match each sequence in List I with its limit inferior and limit superior in List II.",
        [r"$(-1)^n\left(1 + \dfrac1n\right)$", r"$1 + (-1)^n$", r"$(-1)^n n$", r"$n\left(1 + (-1)^n\right)$"],
        [r"$\liminf = 0$, $\limsup = +\infty$", r"$\liminf = -1$, $\limsup = 1$",
         r"$\liminf = -\infty$, $\limsup = +\infty$", r"$\liminf = 0$, $\limsup = 2$"],
        [r"A-2, B-4, C-3, D-1", r"A-2, B-1, C-3, D-4", r"A-4, B-2, C-3, D-1", r"A-2, B-4, C-1, D-3"],
        r"""Split into even and odd terms:
- A: even terms $\to 1$, odd terms $\to -1$: $(-1, 1)$, item 2.
- B: even terms $= 2$, odd terms $= 0$: $(0, 2)$, item 4.
- C: even terms $\to +\infty$, odd terms $\to -\infty$: item 3.
- D: even terms $2n \to +\infty$, odd terms $= 0$: $(0, +\infty)$, item 1.

So A-2, B-4, C-3, D-1. For A, $\sup = \frac32$ and $\inf = -2$ are not the limit superior and inferior.""")

# ---------------------------------------------------------------- assertion-reason (5)
T.assertion_reason(1, ["monotone-e"],
                   r"The sequence $\left(1 + \dfrac1n\right)^n$ converges.",
                   r"Every monotone sequence of real numbers that is bounded converges.",
                   0,
                   r"""Both are true. The sequence is increasing and bounded above by $3$ (binomial expansion), so R gives A directly. Its limit is $e$.""")

T.assertion_reason(2, ["limit-definition", "subsequences"],
                   r"The sequence $\left((-1)^n\right)$ does not converge.",
                   r"Every bounded sequence of real numbers converges.",
                   2,
                   r"""A is true: the subsequences of even and odd terms tend to $1$ and $-1$, two different limits.

R is false, and A itself is the counterexample: $(-1)^n$ is bounded. Only bounded **monotone** sequences must converge; a bounded sequence only has a convergent **subsequence**.""")

T.assertion_reason(3, ["cauchy-limit-theorems", "exam-tips"],
                   r"If $a_n > 0$ for all $n$ and $a_n^{1/n} \to 1$, then $\dfrac{a_{n+1}}{a_n} \to 1$.",
                   r"If $a_n > 0$ for all $n$ and $\dfrac{a_{n+1}}{a_n} \to l$, then $a_n^{1/n} \to l$.",
                   3,
                   r"""A is false. Take $a_n = 2$ for odd $n$ and $a_n = 1$ for even $n$. Then $a_n^{1/n}$ is $2^{1/n}$ or $1$, which tends to $1$; but $\frac{a_{n+1}}{a_n}$ alternates between $\frac12$ and $2$.

R is true: it is Cauchy's second limit theorem. Its converse, A, fails.""")

T.assertion_reason(2, ["cauchy-limit-theorems", "limit-definition"],
                   r"$\displaystyle\lim_{n\to\infty} \frac{1}{n}\left(1 + \frac12 + \cdots + \frac1n\right) = 0$.",
                   r"Every convergent sequence of real numbers is bounded.",
                   1,
                   r"""A is true by Cauchy's first limit theorem: $\frac1n \to 0$, so the means of $1, \frac12, \dots, \frac1n$ tend to $0$. (Also $1 + \cdots + \frac1n \le 1 + \log n$, and $\frac{1 + \log n}{n} \to 0$.)

R is true, but it does not give A. Boundedness of $(1/n)$ alone gives only that the means are bounded, not that they tend to $0$.""")

T.assertion_reason(3, ["nested-cauchy"],
                   r"The sequence $s_n = 1 + \dfrac12 + \dfrac13 + \cdots + \dfrac1n$ does not converge.",
                   r"A sequence of real numbers converges if and only if it is a Cauchy sequence.",
                   0,
                   r"""Both are true, and R explains A. For every $n$,
$$s_{2n} - s_n = \frac{1}{n+1} + \cdots + \frac{1}{2n} \ge n\cdot\frac{1}{2n} = \frac12,$$
so with $\varepsilon = \frac12$ no $N$ works: $(s_n)$ is not Cauchy. By Cauchy's general principle (R), it does not converge.""")


def check():
    import sympy as sp
    n, k = sp.symbols("n k", positive=True, integer=True)
    x = sp.symbols("x")
    oo = sp.oo
    L = lambda e: sp.limit(e, n, oo)

    eq(L((3 * n**2 + 2 * n) / (5 * n**2 - 1)), sp.Rational(3, 5), "q1")
    eq(L((1 + 1 / n) ** (2 * n)), sp.E**2, "q2")
    eq(L(n ** (1 / n)), 1, "q3")
    # q4: fixed points and numeric iteration
    assert set(sp.solve(sp.Eq(x**2, 2 + x), x)) == {2, -1}
    t = sp.sqrt(2)
    for _ in range(8):
        t2 = sp.sqrt(2 + t); assert sp.N(t2 - t, 50) > 0 and sp.N(t2, 50) < 2; t = t2
    assert abs(sp.N(t - 2)) < 1e-4, "q4"
    eq(L(sp.factorial(n) ** (1 / n) / n), 1 / sp.E, "q5")
    eq(L((sp.factorial(n + 1) / (n + 1) ** (n + 1)) / (sp.factorial(n) / n**n)), 1 / sp.E, "q5 ratio")
    # notes example (first limit theorem): means of k^(1/k) -> 1
    avg = sum(m ** (1.0 / m) for m in range(1, 200001)) / 200000
    assert abs(avg - 1) < 1e-3, ("notes means", avg)
    eq(L(n / sp.sqrt(n**2 + n)), 1, "q7 low"); eq(L(n / sp.sqrt(n**2 + 1)), 1, "q7 high")
    m = 2000
    assert abs(sum(1 / (m * m + j) ** 0.5 for j in range(1, m + 1)) - 1) < 1e-3, "q7 numeric"
    # q8: (-1)^n bounded, subsequential limits differ
    assert {(-1) ** j for j in range(1, 10)} == {-1, 1}
    eq(L(1 / n), 0, "q8 1/n"); eq(L(((-1) ** n / n).subs(n, 2 * n)), 0, "q8 even"); eq(L(((-1) ** n / n).subs(n, 2 * n - 1)), 0, "q8 odd")
    # q9
    eq(L(1 + 1 / (2 * n)), 1, "q9 even"); eq(L(-(1 + 1 / (2 * n - 1))), -1, "q9 odd")
    terms = [(-1) ** j * (1 + sp.Rational(1, j)) for j in range(1, 50)]
    eq(max(terms), sp.Rational(3, 2), "q9 sup"); eq(min(terms), -2, "q9 inf")
    # q10
    eq(sp.minimum(x / (x + 1), x, sp.Interval(1, oo)), sp.Rational(1, 2), "q10 inf")
    eq(L(n / (n + 1)), 1, "q10 sup"); assert all(sp.Rational(j, j + 1) < 1 for j in range(1, 200))
    # q11
    N = next(j for j in range(1, 1000) if all(abs(sp.Rational(i + 1, i) - 1) < sp.Rational(1, 100) for i in range(j, j + 50)))
    eq(N, 101, "q11")
    # (direct sp.limit of this form returns a wrong value in this SymPy; use the ratio + a numeric check)
    import math
    big = 10**6
    assert abs(math.exp(math.log(big) - math.lgamma(big + 1) / big) - math.e) < 1e-4, "q12 numeric"
    eq(L(((n + 1) ** (n + 1) / sp.factorial(n + 1)) / (n**n / sp.factorial(n))), sp.E, "q12 ratio")
    eq(L(sp.sqrt(n**2 + n) - n), sp.Rational(1, 2), "q13")
    # q14
    roots = sp.solve(sp.Eq(x, 1 / (1 + x)), x)
    pos = [r for r in roots if r > 0]
    eq(pos[0], (sp.sqrt(5) - 1) / 2, "q14 root")
    t = sp.Integer(1)
    for _ in range(40):
        t = 1 / (1 + t)
    assert abs(sp.N(t - (sp.sqrt(5) - 1) / 2)) < 1e-12, "q14 numeric"
    # q15: even -> +oo, odd -> -oo
    assert L(2 * n) == oo and L(-(2 * n - 1)) == -oo
    assert L(n**2) == oo and L(-sp.sqrt(n)) == -oo
    # q16: constant sequence and a non-constant one
    lsym = sp.symbols("l")
    eq(L(lsym * sp.summation(k, (k, 1, n)) / n**2), lsym / 2, "q16 const")
    eq(L(sp.summation(k * (1 + 1 / k), (k, 1, n)) / n**2), sp.Rational(1, 2), "q16 a_n=1+1/n")
    eq(L(n * lsym / (2 * n - 1)), lsym / 2, "q16 stolz")
    # q17: closed intervals -> one point
    eq(L(1 / n), 0, "q17"); eq(L(1 - 1 / n), 1, "q17b"); eq(L(1 + 1 / n), 1, "q17c")
    # q18
    assert all(sp.summation(1 / k, (k, j + 1, 2 * j)) >= sp.Rational(1, 2) for j in range(1, 40)), "q18 not Cauchy"
    eq(sp.summation(1 / k**2, (k, 1, oo)), sp.pi**2 / 6, "q18 t")
    eq(L(sp.sin(n) / n), 0, "q18 v")
    a19 = sp.factorial(2 * n) / sp.factorial(n) ** 2
    eq(L(sp.combsimp(a19.subs(n, n + 1) / a19)), 4, "q19 ratio")
    assert abs(sp.N(sp.log(sp.binomial(4000, 2000)) / 2000 - sp.log(4))) < 0.01, "q19 numeric"
    eq(L((2**n + 3**n) ** (1 / n)), 3, "q20")
    # q21
    seq = [(1 + sp.Rational(1, j)) ** j for j in range(1, 60)]
    assert all(seq[i] < seq[i + 1] for i in range(len(seq) - 1)) and all(s < 3 for s in seq), "q21"
    seq2 = [(1 + sp.Rational(1, j)) ** (j + 1) for j in range(1, 60)]
    assert all(seq2[i] > seq2[i + 1] for i in range(len(seq2) - 1)), "q21 decreasing companion"
    # statements 1: (-1)^n bounded, not convergent; even subsequence constant
    # statements 2: 3 false via 1/n * n
    eq(L((1 / n) * n), 1, "st2 product"); assert L(n) == oo
    eq(L(sp.sin(n) / n), 0, "st2 null*bounded")
    # statements 3: |(-1)^n| = 1
    assert all(abs((-1) ** j) == 1 for j in range(1, 20))
    # match 1
    lims = [L((1 + 1 / n) ** n), L(n ** (1 / n)), L(sp.factorial(n) ** (1 / n) / n), L((1 + 1 / (2 * n)) ** n)]
    right = [1, sp.sqrt(sp.E), sp.E, 1 / sp.E]
    key = [[sp.simplify(r - v) == 0 for r in right].index(True) + 1 for v in lims]
    assert key == [3, 1, 4, 2], key
    # match 2: even/odd subsequence limits -> (liminf, limsup)
    def ev_od(expr):
        e = L(expr.subs(n, 2 * n)); o = L(expr.subs(n, 2 * n - 1))
        return (sp.Min(e, o), sp.Max(e, o))
    right2 = [(0, oo), (-1, 1), (-oo, oo), (0, 2)]
    seqs = [(-1) ** n * (1 + 1 / n), 1 + (-1) ** n, (-1) ** n * n, n * (1 + (-1) ** n)]
    key2 = [right2.index(ev_od(s)) + 1 for s in seqs]
    assert key2 == [2, 4, 3, 1], key2
    # AR1
    eq(L((1 + 1 / n) ** n), sp.E, "ar1")
    # AR3: counterexample
    eq(L(2 ** (1 / (2 * n - 1))), 1, "ar3 odd root"); a3 = [2 if j % 2 else 1 for j in range(1, 41)]
    assert {sp.Rational(a3[i + 1], a3[i]) for i in range(39)} == {sp.Rational(1, 2), 2}, "ar3 ratios oscillate"
    # AR4
    eq(L(sp.harmonic(n) / n), 0, "ar4")
    # AR5: same bound as q18
    assert L(sp.harmonic(n)) == oo
    # notes examples
    eq(L((1 - 1 / n) ** n), 1 / sp.E, "notes e^-1")
    eq(L((1 + 1 / (2 * n)) ** n), sp.sqrt(sp.E), "notes sqrt e")
    eq(L(sp.log(n) / n), 0, "notes log n/n")
    eq(L(sp.factorial(n) / n**n), 0, "notes n!/n^n")
    eq(L(n**3 / 2**n), 0, "notes n^p x^n")
    x7 = [sp.Integer(1)]
    for _ in range(4):
        x7.append(1 / (1 + x7[-1]))
    assert x7[:4] == [1, sp.Rational(1, 2), sp.Rational(2, 3), sp.Rational(3, 5)]


T.write(check)
