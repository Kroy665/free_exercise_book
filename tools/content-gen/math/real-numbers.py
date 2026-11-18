import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from qlib import Topic, eq

T = Topic("math.analysis.real-numbers")

# ---------------------------------------------------------------- single (21)
# q1
T.single(1, ["sup-inf", "archimedean"], r"For $S = \left\{\dfrac1n : n \in \N\right\}$, the infimum of $S$ is",
         [r"$0$, and it is not attained in $S$", r"$0$, and it is the minimum of $S$", r"$1$", r"It does not exist"],
         r"""Every $\frac1n > 0$, so $0$ is a lower bound. No $\varepsilon > 0$ is a lower bound: by the Archimedean property there is an $n$ with $\frac1n < \varepsilon$. Hence
$$\inf S = 0,$$
but $\frac1n \ne 0$ for every $n$, so $0 \notin S$ and $S$ has no minimum.

$1$ is the supremum (and maximum), not the infimum. The set is bounded below, so the infimum exists by completeness.""")

# q2
T.single(1, ["rationals-irrationals"], r"Which of the following numbers is irrational?",
         [r"$\log_2 3$", r"$\log_2 8$", r"$\sqrt{2.25}$", r"$0.\overline{12}$"],
         r"""If $\log_2 3 = \frac pq$ with $p, q \in \N$, then $2^p = 3^q$: an even number equals an odd number, which is impossible. So $\log_2 3$ is irrational.

The others are rational: $\log_2 8 = 3$; $\sqrt{2.25} = \sqrt{\frac94} = \frac32$; and $0.\overline{12} = \frac{12}{99} = \frac{4}{33}$, since a recurring decimal is rational.""")

# q3
T.single(3, ["sup-inf"], r"For $S = \left\{(-1)^n + \dfrac1n : n \in \N\right\}$,",
         [r"$\sup S = \dfrac32$ and $\inf S = -1$", r"$\sup S = 2$ and $\inf S = -1$",
          r"$\sup S = \dfrac32$ and $\inf S = 0$", r"$\sup S = 1$ and $\inf S = -1$"],
         r"""Split by parity.

- Even $n = 2k$: $1 + \frac{1}{2k}$ gives $\frac32, \frac54, \frac76, \dots$, which decrease towards $1$. The largest is $\frac32$, at $n = 2$.
- Odd $n = 2k - 1$: $-1 + \frac{1}{2k-1}$ gives $0, -\frac23, -\frac45, \dots$, which decrease towards $-1$ and never reach it.

So $$\sup S = \max S = \frac32, \qquad \inf S = -1\ (\text{not attained}).$$

$2$ would be the value at $n = 1$ if $(-1)^1$ were $+1$; in fact the $n = 1$ term is $-1 + 1 = 0$. $\sup = 1$ confuses the supremum with the limit of the even terms.""")

# q4
T.single(1, ["decimals"], r"The recurring decimal $0.\overline{36}$ equals",
         [r"$\dfrac{4}{11}$", r"$\dfrac{9}{25}$", r"$\dfrac{4}{9}$", r"$\dfrac{36}{100}$"],
         r"""Let $x = 0.\overline{36}$. Then $100x = 36.\overline{36}$, so $99x = 36$ and
$$x = \frac{36}{99} = \frac{4}{11}.$$

$\frac{9}{25} = \frac{36}{100} = 0.36$ is the terminating decimal, which ignores the recurrence. Check: $\frac{4}{11} = 0.3636\ldots$""")

# q5
T.single(2, ["decimals"], r"The decimal $0.1\overline{6}$ (only the $6$ recurs) equals",
         [r"$\dfrac16$", r"$\dfrac{16}{99}$", r"$\dfrac{8}{45}$", r"$\dfrac{1}{9}$"],
         r"""Let $x = 0.1\overline6$. Then $100x = 16.\overline6$ and $10x = 1.\overline6$, so $90x = 15$ and
$$x = \frac{15}{90} = \frac16.$$
Rule: (all digits $16$) minus (non-recurring digits $1$), over one $9$ and one $0$.

$\frac{16}{99} = 0.\overline{16}$ makes both digits recur. $\frac{8}{45} = \frac{16}{90}$ forgets to subtract the non-recurring part.""")

# q6
T.single(2, ["decimals"], r"The real number $0.24\overline{9}$ (only the $9$ recurs) equals",
         [r"$\dfrac14$", r"$\dfrac{249}{1000}$", r"$\dfrac{249}{999}$", r"$\dfrac{247}{990}$"],
         r"""The tail is a geometric series:
$$0.24\overline9 = 0.24 + \sum_{k=3}^{\infty}\frac{9}{10^k} = 0.24 + \frac{9/1000}{1 - 1/10} = 0.24 + 0.01 = 0.25 = \frac14.$$
By the rule: $\frac{249 - 24}{900} = \frac{225}{900} = \frac14$.

$\frac{249}{1000} = 0.249$ stops the $9$s. A number with a terminating expansion ($0.25$) also has one ending in recurring $9$s.""")

# q7
T.single(1, ["decimals"], r"A real number is rational if and only if its decimal expansion is",
         [r"terminating or recurring", r"terminating", r"non-terminating", r"non-terminating and non-recurring"],
         r"""$\frac pq$ in lowest terms terminates if $q$ has no prime factors other than $2$ and $5$, and otherwise recurs. Conversely, a terminating or recurring decimal is a rational (a geometric series sums to a rational).

"Terminating" alone misses $\frac13 = 0.\overline3$. "Non-terminating and non-recurring" describes the **irrationals**.""")

# q8
T.single(2, ["sup-inf", "ordered-field"], r"Let $A = \{x \in \Q : x > 0,\ x^2 < 2\}$. Which statement is correct?",
         [r"$A$ is bounded above in $\Q$ but has no supremum in $\Q$; in $\R$, $\sup A = \sqrt2$",
          r"$A$ is not bounded above in $\Q$",
          r"$\sup A = 2$ in $\Q$",
          r"$A$ has a maximum element in $\Q$"],
         r"""$2$ (or $1.5$) is a rational upper bound, so $A$ is bounded above in $\Q$. In $\R$, completeness gives $\sup A$, and it equals $\sqrt2$: every rational $x$ with $x^2 < 2$ is below $\sqrt2$, and by density there are rationals in $A$ arbitrarily close to $\sqrt2$.

Since $\sqrt2 \notin \Q$, there is no least rational upper bound: any rational $r > \sqrt2$ has a smaller rational between $\sqrt2$ and $r$. This is why $\Q$ is not complete.

$2$ is an upper bound but not the least. There is no maximum: for $x \in A$ there is a rational between $x$ and $\sqrt2$.""")

# q9
T.single(2, ["archimedean"], r"The Archimedean property of $\R$ states that",
         [r"for every $x > 0$ and every $y \in \R$, there is $n \in \N$ with $nx > y$",
          r"for every $x, y \in \R$, there is $n \in \N$ with $nx > y$",
          r"for every $x > 0$ and every $y \in \R$, there is $n \in \N$ with $nx < y$",
          r"there is $x > 0$ such that $nx > y$ for every $n \in \N$ and every $y \in \R$"],
         r"""Archimedean property: given any positive $x$ (however small) and any $y$ (however large), some multiple $nx$ exceeds $y$. Equivalently, $\N$ is not bounded above.

The condition $x > 0$ is essential: with $x = -1$, $y = 0$, no $n$ gives $-n > 0$. The version with $nx < y$ fails for $y = -1$. The last option would make a single $x$ exceed every real $y$, which is absurd (take $n = 1$, $y = x$).""")

# q10
T.single(1, ["archimedean"], r"Between any two distinct real numbers there are",
         [r"infinitely many rationals and infinitely many irrationals",
          r"infinitely many rationals but possibly no irrational",
          r"at least one irrational but possibly no rational",
          r"only finitely many rationals"],
         r"""Density of $\Q$: if $a < b$, there is a rational $r \in (a, b)$; repeating in $(a, r)$, $(r, b)$, ... gives infinitely many.

Density of the irrationals: pick a rational $r$ with $a - \sqrt2 < r < b - \sqrt2$; then $r + \sqrt2 \in (a, b)$ is irrational. Again there are infinitely many.

So both kinds occur infinitely often in every interval.""")

# q11
T.single(2, ["rationals-irrationals"], r"Let $a$ be a nonzero rational and $b$ an irrational number. Which of $a + b$ and $ab$ are necessarily irrational?",
         [r"Both $a + b$ and $ab$", r"$a + b$ only", r"$ab$ only", r"Neither"],
         r"""- If $a + b = s \in \Q$, then $b = s - a \in \Q$, a contradiction. So $a + b$ is irrational.
- If $ab = s \in \Q$, then $b = \frac sa \in \Q$ (dividing is allowed because $a \ne 0$), a contradiction. So $ab$ is irrational.

Example: $a = 2$, $b = \sqrt2$ gives $2 + \sqrt2$ and $2\sqrt2$, both irrational. The condition $a \ne 0$ is what saves the product; with $a = 0$, $ab = 0$.""")

# q12
T.single(1, ["absolute-value"], r"The set of real $x$ satisfying $|2x - 1| \le 5$ is",
         [r"$[-2, 3]$", r"$[-3, 2]$", r"$(-2, 3)$", r"$[-2, \infty)$"],
         r"""$$|2x - 1| \le 5 \iff -5 \le 2x - 1 \le 5 \iff -4 \le 2x \le 6 \iff -2 \le x \le 3.$$

The inequality is non-strict, so the endpoints belong: $[-2, 3]$, not $(-2, 3)$. $[-3, 2]$ comes from solving $|2x + 1| \le 5$. Check: at $x = 3$, $|5| = 5$.""")

# q13
T.single(2, ["absolute-value"], r"The set of all real $x$ with $|x - 1| + |x - 3| = 2$ is",
         [r"$[1, 3]$", r"$\{1, 3\}$", r"$\{2\}$", r"$\varnothing$"],
         r"""$|x - 1| + |x - 3|$ is the sum of the distances from $x$ to $1$ and to $3$.

- For $1 \le x \le 3$: $(x - 1) + (3 - x) = 2$.
- For $x > 3$: $2x - 4 > 2$. For $x < 1$: $4 - 2x > 2$.

So the equation holds exactly on $[1, 3]$. Testing only $x = 1$ and $x = 3$ (or the midpoint $2$) misses the whole interval.""")

# q14
T.single(3, ["absolute-value"], r"For real numbers $x$ and $y$, $|x + y| = |x| + |y|$ holds if and only if",
         [r"$xy \ge 0$", r"$xy > 0$", r"$x = y$", r"$x + y \ge 0$"],
         r"""Square both sides (both are non-negative):
$$x^2 + 2xy + y^2 = x^2 + 2|x||y| + y^2 \iff xy = |xy| \iff xy \ge 0.$$

$xy > 0$ wrongly excludes $x = 0$ or $y = 0$, where equality clearly holds. $x + y \ge 0$ fails for $x = 3$, $y = -1$: $|2| = 2 \ne 4$.""")

# q15
T.single(2, ["sup-inf"], r"Let $S = \{x \in \R : x^2 - 5x + 6 < 0\}$. Then",
         [r"$\sup S = 3$ and $S$ has no maximum", r"$\max S = 3$", r"$\sup S = 2$", r"$S$ is not bounded above"],
         r"""$x^2 - 5x + 6 = (x - 2)(x - 3) < 0 \iff 2 < x < 3$, so $S = (2, 3)$.

Every element is below $3$, and points $3 - \varepsilon$ belong to $S$ for small $\varepsilon > 0$. So $\sup S = 3$, but $3 \notin S$, so there is no maximum.

$2$ is the infimum, not the supremum.""")

# q16
T.single(3, ["sup-inf"], r"Let $S \subseteq \R$ be nonempty and let $u$ be an upper bound of $S$. Then $u = \sup S$ if and only if",
         [r"for every $\varepsilon > 0$ there is $x \in S$ with $x > u - \varepsilon$",
          r"for some $\varepsilon > 0$ there is $x \in S$ with $x > u - \varepsilon$",
          r"for every $\varepsilon > 0$ there is $x \in S$ with $x > u + \varepsilon$",
          r"$u \in S$"],
         r"""$u$ is the **least** upper bound exactly when no smaller number $u - \varepsilon$ is an upper bound, i.e. for every $\varepsilon > 0$ some $x \in S$ exceeds $u - \varepsilon$.

- "For some $\varepsilon$" is too weak: for $S = [0, 1]$, $u = 2$ and $\varepsilon = 5$ satisfy it, but $\sup S = 1$.
- $x > u + \varepsilon$ contradicts $u$ being an upper bound.
- $u \in S$ is sufficient but not necessary: $\sup(0, 1) = 1 \notin (0, 1)$.""")

# q17
T.single(3, ["sup-inf", "exam-tips"], r"Let $A = \left\{1 - \dfrac1n : n \in \N\right\}$, $B = \left\{2 + \dfrac1n : n \in \N\right\}$ and $A + B = \{a + b : a \in A,\ b \in B\}$. Then $\sup(A + B)$ is",
         [r"$4$", r"$3$", r"$\dfrac72$", r"$2$"],
         r"""$\sup A = 1$ (not attained) and $\sup B = 3$ (at $n = 1$). Since $a$ and $b$ are chosen independently,
$$\sup(A + B) = \sup A + \sup B = 1 + 3 = 4.$$
Directly: $\left(1 - \frac1m\right) + 3 \to 4$ as $m \to \infty$, and every sum is below $4$.

$3$ comes from using the **same** $n$ in both: $(1 - \frac1n) + (2 + \frac1n) = 3$. $\frac72$ is $A$ at $n = 2$ plus $B$ at $n = 1$; it is a value, not the supremum.""")

# q18
T.single(2, ["sup-inf"], r"If $\inf A = -3$ and $B = \{-2a : a \in A\}$, then $\sup B$ is",
         [r"$6$", r"$-6$", r"$3$", r"$-\dfrac32$"],
         r"""Multiplying by a negative number reverses the order, so it turns an infimum into a supremum:
$$\sup(-2A) = -2\inf A = -2(-3) = 6.$$

$-6$ uses $\sup(cA) = c\sup A$, which holds only for $c > 0$. Example: $A = [-3, 0]$ gives $B = [0, 6]$, with $\sup B = 6$.""")

# q19
T.single(2, ["nested-countable"], r"Which of the following sets is uncountable?",
         [r"$\R \setminus \Q$", r"$\Q$", r"$\Q \times \Q$", r"the set of algebraic numbers"],
         r"""$\Q$, $\Q \times \Q$ and the algebraic numbers are countable (each is a countable union of countable sets).

If $\R\setminus\Q$ were countable, then $\R = \Q \cup (\R\setminus\Q)$ would be a union of two countable sets, hence countable. But $\R$ is uncountable (Cantor). So the irrationals are uncountable.""")

# q20
T.single(1, ["ordered-field"], r"The Cantor–Dedekind axiom states that",
         [r"there is a one-one, order-preserving correspondence between the points of a straight line and the real numbers",
          r"there is a one-one correspondence between the points of a straight line and the rational numbers",
          r"every nonempty set of reals that is bounded above has a supremum",
          r"$\N$ is not bounded above in $\R$"],
         r"""Cantor–Dedekind: the real numbers and the points of a line correspond one-to-one, preserving order. This is what lets us call $\R$ "the real line", a linear continuum.

The rationals do not fill the line (the point $\sqrt2$ is missed). The third option is the least upper bound (completeness) axiom; the fourth is the Archimedean property.""")

# q21
T.single(2, ["rationals-irrationals"], r"Which of the following is rational?",
         [r"$\log_4 8$", r"$\log_2 6$", r"$\dfrac{\sqrt{12}}{\sqrt2}$", r"$\sqrt2 + \sqrt3$"],
         r"""$$\log_4 8 = \frac{\log_2 8}{\log_2 4} = \frac32.$$

The others are irrational:
- $\log_2 6 = 1 + \log_2 3$, a rational plus an irrational.
- $\frac{\sqrt{12}}{\sqrt2} = \sqrt6$, and $6$ is not a perfect square.
- $\sqrt2 + \sqrt3$ is a root of $x^4 - 10x^2 + 1$, which has no rational roots ($\pm1$ fail).""")

# ------------------------------------------------------------ statements (2)
T.statements(2, ["rationals-irrationals"], r"Consider the following statements:",
             [r"The sum of two irrational numbers is always irrational.",
              r"The product of a nonzero rational number and an irrational number is irrational.",
              r"$\sqrt2 + \sqrt3$ is irrational."],
             [r"2 and 3 only", r"1 and 2 only", r"3 only", r"1, 2 and 3"],
             r"""1. False: $\sqrt2$ and $-\sqrt2$ are irrational, but their sum is $0$.
2. True: if $r\alpha = s \in \Q$ with $r \ne 0$, then $\alpha = \frac sr \in \Q$.
3. True: $x = \sqrt2 + \sqrt3$ satisfies $x^4 - 10x^2 + 1 = 0$, whose only possible rational roots $\pm1$ are not roots.

So 2 and 3 only.""")

T.statements(3, ["ordered-field", "sup-inf", "archimedean"], r"Consider the following statements:",
             [r"Every nonempty subset of $\R$ that is bounded below has an infimum in $\R$.",
              r"Every nonempty subset of $\Q$ that is bounded above in $\Q$ has a supremum in $\Q$.",
              r"$\Q$ is an ordered field with the Archimedean property."],
             [r"1 and 3 only", r"1 and 2 only", r"1 only", r"1, 2 and 3"],
             r"""1. True: $\inf S = -\sup(-S)$, and $-S$ is nonempty and bounded above, so completeness applies.
2. False: $\{x \in \Q : x^2 < 2\}$ is bounded above in $\Q$ but has no least rational upper bound, because $\sqrt2 \notin \Q$.
3. True: $\Q$ satisfies all the ordered-field axioms, and for rationals $x > 0$, $y$, some $n$ has $nx > y$.

So 1 and 3 only. Completeness, not the Archimedean property, separates $\R$ from $\Q$.""")

# ----------------------------------------------------------------- match (2)
T.match(3, ["nested-countable", "archimedean"], r"Match each set in List I with the set it equals in List II ($n$ runs over $\N$).",
        [r"$\displaystyle\bigcap_{n} \left[0, \tfrac1n\right]$", r"$\displaystyle\bigcap_{n} \left(0, \tfrac1n\right)$",
         r"$\displaystyle\bigcap_{n} \left[-\tfrac1n, 1 + \tfrac1n\right]$", r"$\displaystyle\bigcup_{n} \left[\tfrac1n, 1\right]$"],
        [r"$\varnothing$", r"$(0, 1]$", r"$\{0\}$", r"$[0, 1]$"],
        [r"A-3, B-1, C-4, D-2", r"A-3, B-3, C-4, D-2", r"A-1, B-3, C-4, D-2", r"A-3, B-1, C-2, D-4"],
        r"""- A: $0$ lies in every $[0, \frac1n]$; any $x > 0$ is excluded once $\frac1n < x$ (Archimedes). So $\{0\}$.
- B: $0$ is never in $(0, \frac1n)$, and any $x > 0$ is excluded as in A. So $\varnothing$; the nested interval theorem needs **closed** intervals.
- C: $x$ is in all of them iff $-\frac1n \le x \le 1 + \frac1n$ for all $n$, iff $0 \le x \le 1$. So $[0, 1]$.
- D: every $x \in (0, 1]$ has $\frac1n \le x$ for some $n$, but $0$ is in none. So $(0, 1]$.

So A-3, B-1, C-4, D-2.""")

T.match(3, ["sup-inf"], r"Match each set in List I with its supremum in List II ($m, n \in \N$).",
        [r"$\left\{1 - \tfrac1n\right\}$", r"$\{x \in \R : x^2 < 2\}$",
         r"$\left\{\tfrac1m + \tfrac1n\right\}$", r"$\left\{\tfrac{(-1)^n}{n}\right\}$"],
        [r"$\dfrac12$", r"$2$", r"$1$", r"$\sqrt2$"],
        [r"A-3, B-4, C-2, D-1", r"A-3, B-2, C-4, D-1", r"A-1, B-4, C-2, D-3", r"A-3, B-4, C-1, D-2"],
        r"""- A: $1 - \frac1n < 1$, and it gets within any $\varepsilon$ of $1$: $\sup = 1$ (not attained).
- B: the set is $(-\sqrt2, \sqrt2)$: $\sup = \sqrt2$.
- C: the largest value is at $m = n = 1$: $\sup = \max = 2$.
- D: the terms are $-1, \frac12, -\frac13, \frac14, \dots$; the positive terms $\frac{1}{2k}$ are largest at $n = 2$: $\sup = \frac12$.

So A-3, B-4, C-2, D-1. Taking $\sup = 1$ for D uses $\left|\frac{(-1)^n}{n}\right|$ at $n = 1$, but that term is $-1$.""")

# ------------------------------------------------------- assertion-reason (5)
T.assertion_reason(1, ["rationals-irrationals"],
                   r"$\sqrt2$ is irrational.",
                   r"If a prime $p$ divides $a^2$ for an integer $a$, then $p$ divides $a$.",
                   0,
                   r"""Both are true, and R is the key step. From $\sqrt2 = \frac pq$ in lowest terms, $p^2 = 2q^2$, so $2 \mid p^2$; by R, $2 \mid p$. Then $2 \mid q$ too, contradicting lowest terms. So R explains A.""")

T.assertion_reason(2, ["archimedean", "nested-countable"],
                   r"$\Q$ is dense in $\R$.",
                   r"$\Q$ is countable.",
                   1,
                   r"""Both are true. A follows from the Archimedean property: for $a < b$, choose $n(b - a) > 1$; then $\frac{\lfloor na\rfloor + 1}{n} \in (a, b)$.

R is about the size of $\Q$, not about its position on the line; it does not explain A. (The irrationals are dense too, yet uncountable.)""")

T.assertion_reason(2, ["sup-inf", "ordered-field"],
                   r"The set $\{x \in \Q : x^2 < 2\}$ has a least upper bound in $\Q$.",
                   r"Every nonempty subset of $\R$ that is bounded above has a supremum in $\R$.",
                   3,
                   r"""A is false: the least upper bound in $\R$ is $\sqrt2$, which is irrational, and any rational upper bound $r > \sqrt2$ can be lowered to a rational between $\sqrt2$ and $r$. So no least rational upper bound exists.

R is true: it is the completeness axiom of $\R$. It holds in $\R$ but not in $\Q$.""")

T.assertion_reason(2, ["decimals"],
                   r"$0.999\ldots = 1$.",
                   r"Every real number has exactly one decimal expansion.",
                   2,
                   r"""A is true: $$\sum_{k=1}^{\infty}\frac{9}{10^k} = \frac{9/10}{1 - 1/10} = 1.$$

R is false, and A itself is a counterexample: $1 = 1.000\ldots = 0.999\ldots$. Every number with a terminating expansion has exactly two expansions (for example $0.5 = 0.4\overline9$).""")

T.assertion_reason(3, ["archimedean"],
                   r"$\N$ is not bounded above in $\R$.",
                   r"For every $x > 0$ and every $y \in \R$, there is $n \in \N$ with $nx > y$.",
                   0,
                   r"""Both are true. R (the Archimedean property) with $x = 1$ says: for every real $y$ there is $n \in \N$ with $n > y$. So no real $y$ is an upper bound of $\N$, which is A. R explains A.

(The two are equivalent; R in turn follows from completeness: if $\N$ had a supremum $u$, some $n > u - 1$, and then $n + 1 > u$.)""")


def check():
    import sympy as sp
    import math
    from fractions import Fraction as F
    n, m, k, x = sp.symbols("n m k x", positive=True, integer=False)
    N = sp.Symbol("N", integer=True, positive=True)
    K = sp.Symbol("K", integer=True, positive=True)

    # q1: inf {1/n} = 0, not attained
    eq(sp.limit(1 / N, N, sp.oo), 0, "q1")
    assert all(F(1, j) > 0 for j in range(1, 1000))

    # q2: log2 3 irrational (2^p even, 3^q odd); the rest rational
    for p in range(1, 60):
        for q in range(1, 40):
            assert 2**p != 3**q
    eq(sp.log(8, 2), 3, "q2a")
    eq(sp.sqrt(sp.Rational(9, 4)), sp.Rational(3, 2), "q2b")
    eq(sp.summation(12 / sp.Integer(100) ** K, (K, 1, sp.oo)), sp.Rational(4, 33), "q2c")

    # q3: sup 3/2 (n=2), inf -1 not attained
    terms = [(-1) ** j + sp.Rational(1, j) for j in range(1, 400)]
    eq(max(terms), sp.Rational(3, 2), "q3 sup")
    assert terms.index(max(terms)) == 1
    assert all(t > -1 for t in terms)
    eq(sp.limit(-1 + 1 / (2 * N - 1), N, sp.oo), -1, "q3 inf")

    # q4
    eq(sp.summation(36 / sp.Integer(100) ** K, (K, 1, sp.oo)), sp.Rational(4, 11), "q4")
    # q5
    eq(sp.Rational(1, 10) + sp.summation(6 / sp.Integer(10) ** K, (K, 2, sp.oo)), sp.Rational(1, 6), "q5")
    eq(sp.Rational(16 - 1, 90), sp.Rational(1, 6), "q5 rule")
    # q6
    eq(sp.Rational(24, 100) + sp.summation(9 / sp.Integer(10) ** K, (K, 3, sp.oo)), sp.Rational(1, 4), "q6")
    eq(sp.Rational(249 - 24, 900), sp.Rational(1, 4), "q6 rule")

    # q7: 1/3 non-terminating rational; 1/7 period 6; terminating iff q = 2^a 5^b
    eq(sp.n_order(10, 7), 6, "q7 period 1/7")
    for q in range(1, 200):
        fac = set(sp.factorint(q).keys())
        terminates = any((10**e) % q == 0 for e in range(0, 20))
        assert terminates == fac.issubset({2, 5}), q

    # q8: sqrt2 irrational; sup of truncations of sqrt2 is sqrt2
    assert sp.sqrt(2).is_rational is False
    for j in range(1, 15):
        r = sp.Rational(sp.floor(sp.sqrt(2) * 10**j), 10**j)
        assert r**2 < 2 and sp.sqrt(2) - r < sp.Rational(1, 10**j)

    # q9: Archimedean: n = floor(y/x)+1 works; x<0 counterexample
    for xv, yv in [(sp.Rational(1, 1000), 1000), (sp.Rational(3, 7), -5), (sp.Rational(1, 3), 10**6)]:
        nn = sp.floor(yv / xv) + 1
        nn = max(nn, 1)
        assert nn * xv > yv
    assert all(-j <= 0 for j in range(1, 100))  # x=-1, y=0 fails

    # q10: rational and irrational between sqrt2 and 1.415
    a, b = sp.sqrt(2), sp.Rational(1415, 1000)
    nn = 10**4
    mm = sp.floor(nn * a) + 1
    r = sp.Rational(mm, nn)
    eq(mm, 14143, "notes density example")
    assert a < r < b
    r2 = sp.Rational(sp.floor((a - sp.sqrt(2)) * 10**5) + 1, 10**5)  # a - sqrt2 = 0
    s = r2 + sp.sqrt(2)
    assert a < s < b and s.is_rational is False

    # q11
    assert (2 + sp.sqrt(2)).is_rational is False and (2 * sp.sqrt(2)).is_rational is False

    # q12
    xr = sp.Symbol("xr", real=True)
    assert sp.solve_univariate_inequality(sp.Abs(2 * xr - 1) <= 5, xr, relational=False) == sp.Interval(-2, 3)
    # q13
    assert sp.solveset(sp.Eq(sp.Abs(xr - 1) + sp.Abs(xr - 3), 2), xr, sp.S.Reals) == sp.Interval(1, 3)
    # notes: |x-2| > 3
    assert sp.solve_univariate_inequality(sp.Abs(xr - 2) > 3, xr, relational=False) == sp.Union(sp.Interval.open(-sp.oo, -1), sp.Interval.open(5, sp.oo))

    # q14: |x+y| = |x|+|y| iff xy >= 0
    import random
    rng = random.Random(1)
    for _ in range(2000):
        u, v = rng.choice([0, rng.randint(-9, 9)]), rng.randint(-9, 9)
        assert (abs(u + v) == abs(u) + abs(v)) == (u * v >= 0)
    assert abs(3 + -1) != abs(3) + abs(-1)

    # q15
    S15 = sp.solve_univariate_inequality(xr**2 - 5 * xr + 6 < 0, xr, relational=False)
    assert S15 == sp.Interval.open(2, 3)
    eq(S15.sup, 3, "q15")
    assert not S15.contains(3)

    # q16: counterexample for "some eps": S=[0,1], u=2, eps=5
    assert 0 > 2 - 5
    eq(sp.Interval.open(0, 1).sup, 1, "q16")

    # q17
    eq(sp.limit(1 - 1 / N, N, sp.oo) + (2 + 1), 4, "q17")
    eq(sp.simplify((1 - 1 / N) + (2 + 1 / N)), 3, "q17 same-n trap")
    # q18
    A18 = sp.Interval(-3, 0)
    eq(sp.imageset(sp.Lambda(xr, -2 * xr), A18).sup, 6, "q18")

    # q19: Cantor pairing is a bijection N x N -> N (on a sample)
    seen = set()
    for i in range(60):
        for j in range(60):
            c = (i + j) * (i + j + 1) // 2 + j
            assert c not in seen
            seen.add(c)
    assert set(range(60 * 61 // 2)).issubset(seen)

    # q21
    eq(sp.log(8) / sp.log(4), sp.Rational(3, 2), "q21")
    eq(sp.sqrt(12) / sp.sqrt(2), sp.sqrt(6), "q21b")
    assert sp.sqrt(6).is_rational is False
    y = sp.Symbol("y")
    eq(sp.minimal_polynomial(sp.sqrt(2) + sp.sqrt(3), y), y**4 - 10 * y**2 + 1, "q21c")
    assert sp.Poly(y**4 - 10 * y**2 + 1).eval(1) != 0 and sp.Poly(y**4 - 10 * y**2 + 1).eval(-1) != 0

    # S1
    eq(sp.sqrt(2) + (-sp.sqrt(2)), 0, "S1-1")
    assert (sp.Rational(3, 5) * sp.sqrt(2)).is_rational is False
    # S2: Q-sup fails (sqrt2 irrational); inf = -sup(-S) on example
    S = sp.Interval(-1, 4)
    eq(S.inf, -sp.imageset(sp.Lambda(xr, -xr), S).sup, "S2-1")

    # M1
    eq(sp.limit(1 / N, N, sp.oo), 0, "M1")
    j = 10**6
    assert sp.Interval(0, sp.Rational(1, j)).contains(0) and not sp.Interval.open(0, sp.Rational(1, j)).contains(0)
    inter = sp.Intersection(*[sp.Interval(-sp.Rational(1, i), 1 + sp.Rational(1, i)) for i in range(1, 50)])
    assert inter == sp.Interval(-sp.Rational(1, 49), 1 + sp.Rational(1, 49))
    eq(sp.limit(-1 / N, N, sp.oo), 0, "M1 C left"); eq(sp.limit(1 + 1 / N, N, sp.oo), 1, "M1 C right")
    uni = sp.Union(*[sp.Interval(sp.Rational(1, i), 1) for i in range(1, 50)])
    assert uni == sp.Interval(sp.Rational(1, 49), 1)

    # M2
    eq(sp.limit(1 - 1 / N, N, sp.oo), 1, "M2 A")
    eq(sp.solve_univariate_inequality(xr**2 < 2, xr, relational=False).sup, sp.sqrt(2), "M2 B")
    eq(max(sp.Rational(1, a_) + sp.Rational(1, b_) for a_ in range(1, 30) for b_ in range(1, 30)), 2, "M2 C")
    eq(max(sp.Rational((-1) ** i, i) for i in range(1, 300)), sp.Rational(1, 2), "M2 D")

    # AR1: p | a^2 => p | a
    for p in sp.primerange(2, 50):
        for a_ in range(1, 300):
            if (a_ * a_) % p == 0:
                assert a_ % p == 0
    # AR3
    assert sp.sqrt(2).is_rational is False
    # AR4
    eq(sp.summation(9 / sp.Integer(10) ** K, (K, 1, sp.oo)), 1, "AR4")
    eq(sp.Rational(4, 10) + sp.summation(9 / sp.Integer(10) ** K, (K, 2, sp.oo)), sp.Rational(1, 2), "AR4b")
    # AR5 / notes: least n with 1/n < 0.003
    nmin = next(i for i in range(1, 10**4) if sp.Rational(1, i) < sp.Rational(3, 1000))
    eq(nmin, 334, "notes 334")

    # notes examples
    eq(sp.Rational(36, 99), sp.Rational(4, 11), "notes 0.36")
    eq((10**6 - 1) * sp.Rational(1, 7), 142857, "notes 1/7 period")
    eq(sp.Max(2, 7), (2 + 7 + abs(2 - 7)) / sp.Integer(2), "notes max")
    eq(sp.sqrt(2) * sp.sqrt(8), 4, "notes sqrt2 sqrt8")


T.write(check)
