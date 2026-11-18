import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from qlib import Topic, eq

T = Topic("math.algebra.number-theory")

# 1
T.single(1, ["division-algorithm", "exam-tips"],
    r"When $-17$ is divided by $5$ according to the division algorithm $a = bq + r$, $0 \le r < |b|$, the quotient $q$ and remainder $r$ are",
    [r"$q = -4,\ r = 3$", r"$q = -3,\ r = -2$", r"$q = -4,\ r = -3$", r"$q = 3,\ r = 2$"],
    r"""The remainder must satisfy $0 \le r < 5$. Take the quotient one step further from zero:
$$-17 = 5 \cdot (-4) + 3.$$
So $q = -4$, $r = 3$.

$-17 = 5(-3) - 2$ is true arithmetic, but $r = -2$ is negative, so it is not the division algorithm. Check: $5(-4) + 3 = -20 + 3 = -17$.""")

# 2
T.single(1, ["gcd"],
    r"$\gcd(252, 198)$ equals",
    [r"$18$", r"$36$", r"$54$", r"$6$"],
    r"""Euclidean algorithm:
$$252 = 1 \cdot 198 + 54,\quad 198 = 3 \cdot 54 + 36,\quad 54 = 1 \cdot 36 + 18,\quad 36 = 2 \cdot 18.$$
The last non-zero remainder is $18$.

$36$ and $54$ are intermediate remainders, not the gcd. Check: $252 = 18 \cdot 14$, $198 = 18 \cdot 11$, and $\gcd(14, 11) = 1$.""")

# 3
T.single(2, ["gcd"],
    r"Which pair $(x, y)$ satisfies $252x + 198y = \gcd(252, 198)$?",
    [r"$(4, -5)$", r"$(-4, 5)$", r"$(5, -4)$", r"$(3, -4)$"],
    r"""From the Euclidean algorithm, $54 = 252 - 198$, $36 = 198 - 3 \cdot 54$, $18 = 54 - 36$. Back-substitute:
$$18 = 54 - (198 - 3 \cdot 54) = 4 \cdot 54 - 198 = 4(252 - 198) - 198 = 4 \cdot 252 - 5 \cdot 198.$$
So $(x, y) = (4, -5)$. Check: $1008 - 990 = 18$.

$(-4, 5)$ gives $-18$ (a sign slip); $(5, -4)$ gives $468$; $(3, -4)$ gives $-36$.""")

# 4
T.single(1, ["coprime-lcm"],
    r"Two positive integers have gcd $12$ and product $4320$. Their lcm is",
    [r"$360$", r"$4320$", r"$51840$", r"$180$"],
    r"""For two positive integers, $\gcd(a, b)\cdot\operatorname{lcm}(a, b) = ab$. So
$$\operatorname{lcm} = \frac{4320}{12} = 360.$$
$51840 = 4320 \cdot 12$ multiplies instead of dividing. (An example pair: $a = 24$, $b = 180$.)""")

# 5
T.single(1, ["divisor-functions"],
    r"The number of positive divisors of $360$ is",
    [r"$24$", r"$23$", r"$12$", r"$30$"],
    r"""$360 = 2^3 \cdot 3^2 \cdot 5$, so
$$\tau(360) = (3 + 1)(2 + 1)(1 + 1) = 24.$$
$12 = 3 \cdot 2 \cdot 2$ multiplies the exponents without adding $1$; $23$ forgets the divisor $1$ (or $360$).""")

# 6
T.single(2, ["divisor-functions"],
    r"The sum of all positive divisors of $360$ is",
    [r"$1170$", r"$810$", r"$168$", r"$975$"],
    r"""$360 = 2^3 \cdot 3^2 \cdot 5$, so
$$\sigma(360) = (1 + 2 + 4 + 8)(1 + 3 + 9)(1 + 5) = 15 \cdot 13 \cdot 6 = 1170.$$
$810 = 1170 - 360$ is the sum of the **proper** divisors only. $168 = (1 + 2 + 4)(1 + 3)(1 + 5)$ stops each bracket one power too early.""")

# 7
T.single(3, ["diophantine"],
    r"The number of solutions of $5x + 3y = 52$ in positive integers $x, y$ is",
    [r"$3$", r"$2$", r"$4$", r"$5$"],
    r"""$3y = 52 - 5x$ must leave remainder $2$ on division by $5$, so $y$ leaves remainder $4$: $y = 4, 9, 14, \ldots$ Also $3y < 52$ forces $y \le 15$.
$$y = 4 \Rightarrow x = 8,\qquad y = 9 \Rightarrow x = 5,\qquad y = 14 \Rightarrow x = 2.$$
So there are $3$ solutions. Equivalently, the general solution is $x = 8 - 3t$, $y = 4 + 5t$, and $x, y > 0$ allow $t = 0, 1, 2$.

$4$ comes from also counting $t = -1$, which gives $y = -1$.""")

# 8
T.single(2, ["diophantine"],
    r"Which of the following equations has **no** solution in integers?",
    [r"$6x + 10y = 15$", r"$6x + 10y = 14$", r"$7x + 11y = 5$", r"$12x + 18y = 30$"],
    r"""$ax + by = c$ is solvable in integers if and only if $\gcd(a, b) \mid c$.

- $6x + 10y = 15$: $\gcd = 2$, and $2 \nmid 15$. **No solution** (the left side is always even).
- $6x + 10y = 14$: $2 \mid 14$; e.g. $(-1, 2)$.
- $7x + 11y = 5$: $\gcd = 1$; e.g. $(-15, 10)$.
- $12x + 18y = 30$: $\gcd = 6 \mid 30$; e.g. $(1, 1)$.""")

# 9
T.single(2, ["diophantine"],
    r"One solution of $3x + 5y = 1$ is $(2, -1)$. The general integer solution is ($t \in \mathbb{Z}$)",
    [r"$x = 2 + 5t,\ y = -1 - 3t$", r"$x = 2 + 3t,\ y = -1 - 5t$", r"$x = 2 + 5t,\ y = -1 + 3t$", r"$x = 2 + 10t,\ y = -1 - 6t$"],
    r"""With $d = \gcd(3, 5) = 1$, the general solution is $x = x_0 + \frac{b}{d}t$, $y = y_0 - \frac{a}{d}t$:
$$x = 2 + 5t, \qquad y = -1 - 3t.$$
Check: $3(2 + 5t) + 5(-1 - 3t) = 6 - 5 + 15t - 15t = 1$.

Swapping the steps ($x = 2 + 3t$) gives $3 \cdot 3t - 5 \cdot 5t \ne 0$; equal signs ($y = -1 + 3t$) give $30t \ne 0$. The family $x = 2 + 10t$, $y = -1 - 6t$ consists of solutions but misses half of them, e.g. $(7, -4)$.""")

# 10
T.single(2, ["divisor-functions", "exam-tips"],
    r"The product of all the positive divisors of $36$ is",
    [r"$6^9$", r"$6^8$", r"$6^{18}$", r"$6^{10}$"],
    r"""The divisors pair off as $d \leftrightarrow 36/d$, each pair having product $36$. With $\tau(36) = (2 + 1)(2 + 1) = 9$ divisors, the product is
$$36^{9/2} = 6^9.$$
$6^{18} = 36^9$ forgets to halve: it counts each pair twice. (Direct: $1 \cdot 2 \cdot 3 \cdot 4 \cdot 6 \cdot 9 \cdot 12 \cdot 18 \cdot 36 = 10077696 = 6^9$.)""")

# 11
T.single(3, ["coprime-lcm"],
    r"If $a, b$ are positive integers with $\gcd(a, b) = 1$, then $\gcd(a + b, a - b)$ (for $a \ne b$) is",
    [r"either $1$ or $2$", r"always $1$", r"always $2$", r"$1$, $2$ or $4$"],
    r"""Let $g = \gcd(a + b, a - b)$. Then $g$ divides the sum $2a$ and the difference $2b$, so
$$g \mid \gcd(2a, 2b) = 2\gcd(a, b) = 2.$$
So $g = 1$ or $2$, and both occur: $(a, b) = (2, 1)$ gives $\gcd(3, 1) = 1$; $(a, b) = (3, 1)$ gives $\gcd(4, 2) = 2$. Hence "always $1$" and "always $2$" are both wrong, and $4$ is impossible.""")

# 12
T.single(2, ["primes"],
    r"Let $N = 2 \cdot 3 \cdot 5 \cdot 7 \cdot 11 \cdot 13 + 1 = 30031$. Then",
    [r"$N = 59 \times 509$ is composite", r"$N$ is prime, as Euclid's proof shows", r"$N$ is divisible by $13$", r"$N$ is divisible by $7$"],
    r"""Each of $2, 3, 5, 7, 11, 13$ leaves remainder $1$ on dividing $N$, so none of them divides $N$ (this rules out the last two options). But $N$ is not prime:
$$30031 = 59 \times 509.$$
Euclid's proof shows only that every prime factor of $N$ is **different** from the listed primes, not that $N$ itself is prime.""")

# 13
T.single(3, ["induction", "exam-tips"],
    r"The largest positive integer that divides $n^5 - n$ for every integer $n$ is",
    [r"$30$", r"$5$", r"$10$", r"$60$"],
    r"""At $n = 2$: $2^5 - 2 = 30$, so the answer is at most $30$.

Now $n^5 - n = (n - 1)n(n + 1)(n^2 + 1)$.
- $(n - 1)n(n + 1)$ is a product of three consecutive integers, so $6$ divides it.
- For $5$: if $n$ leaves remainder $0, 1, 4$ on division by $5$, one of $n, n - 1, n + 1$ is a multiple of $5$; if the remainder is $2$ or $3$, then $n^2 + 1$ is (e.g. $4 + 1$, $9 + 1$).

So $30 \mid n^5 - n$ always, and the answer is $30$. $60$ fails at $n = 2$.""")

# 14
T.single(3, ["induction"],
    r"The largest positive integer that divides $3^{2n+2} - 8n - 9$ for every positive integer $n$ is",
    [r"$64$", r"$8$", r"$16$", r"$32$"],
    r"""Let $f(n) = 3^{2n+2} - 8n - 9$. At $n = 1$: $f(1) = 81 - 17 = 64$, so the answer is at most $64$.

Induction shows $64 \mid f(n)$ for all $n$:
$$f(k + 1) - 9f(k) = -8k - 17 + 72k + 81 = 64(k + 1),$$
so $f(k + 1) = 9f(k) + 64(k + 1)$. Hence the answer is $64$.

$8$, $16$ and $32$ also divide every $f(n)$, but they are not the largest.""")

# 15
T.single(2, ["coprime-lcm"],
    r"If $a = 2^3 \cdot 3^2 \cdot 5$ and $b = 2^2 \cdot 3^4 \cdot 7$, then $\operatorname{lcm}(a, b)$ is",
    [r"$22680$", r"$2520$", r"$11340$", r"$36$"],
    r"""The lcm takes the **larger** exponent of each prime:
$$\operatorname{lcm}(a, b) = 2^3 \cdot 3^4 \cdot 5 \cdot 7 = 8 \cdot 81 \cdot 35 = 22680.$$
$36 = 2^2 \cdot 3^2$ is the gcd (smaller exponents). $2520 = 2^3 \cdot 3^2 \cdot 5 \cdot 7$ takes the smaller power of $3$; $11340$ takes the smaller power of $2$. Check: $\gcd \cdot \operatorname{lcm} = 36 \cdot 22680 = 816480 = 360 \cdot 2268 = ab$.""")

# 16
T.single(2, ["divisor-functions"],
    r"The number of **odd** positive divisors of $720$ is",
    [r"$6$", r"$30$", r"$24$", r"$5$"],
    r"""$720 = 2^4 \cdot 3^2 \cdot 5$. An odd divisor uses $2^0$ only, so it divides $3^2 \cdot 5 = 45$:
$$\tau(45) = (2 + 1)(1 + 1) = 6.$$
$30 = \tau(720)$ counts all divisors; $24 = 30 - 6$ counts the even ones.""")

# 17
T.single(3, ["divisor-functions"],
    r"The smallest positive integer with exactly $12$ positive divisors is",
    [r"$60$", r"$72$", r"$96$", r"$48$"],
    r"""$12 = (\alpha_1 + 1)(\alpha_2 + 1)\cdots$ can be split as $12$, $6 \cdot 2$, $4 \cdot 3$, $3 \cdot 2 \cdot 2$. Give the larger exponents to the smaller primes:
$$2^{11} = 2048,\quad 2^5 \cdot 3 = 96,\quad 2^3 \cdot 3^2 = 72,\quad 2^2 \cdot 3 \cdot 5 = 60.$$
The smallest is $60$. $48 = 2^4 \cdot 3$ has only $5 \cdot 2 = 10$ divisors; $72$ and $96$ have $12$ but are larger.""")

# 18
T.single(3, ["divisor-functions"],
    r"The sum of the reciprocals of all the positive divisors of $360$ is",
    [r"$\dfrac{13}{4}$", r"$\dfrac{9}{4}$", r"$\dfrac{1}{15}$", r"$\dfrac{7}{2}$"],
    r"""As $d$ runs over the divisors of $n$, so does $n/d$. Hence
$$\sum_{d \mid n}\frac1d = \frac1n\sum_{d \mid n}\frac nd = \frac{\sigma(n)}{n} = \frac{1170}{360} = \frac{13}{4}.$$
$\frac94 = \frac{810}{360}$ uses only the proper divisors.""")

# 19
T.single(1, ["induction"],
    r"Under the usual order, which of the following sets has a least element?",
    [r"The set of positive even integers", r"The set of positive rational numbers", r"The set of negative integers", r"The open interval $(0, 1)$"],
    r"""By the well-ordering principle, every non-empty set of positive integers has a least element. The positive even integers form such a set; the least element is $2$.

The positive rationals and $(0, 1)$ have infimum $0$, which is not in the set. The negative integers are unbounded below.""")

# 20
T.single(2, ["division-algorithm", "exam-tips"],
    r"When $37$ is divided by $-7$ according to the division algorithm ($0 \le r < |b|$), the quotient and remainder are",
    [r"$q = -5,\ r = 2$", r"$q = 5,\ r = 2$", r"$q = -6,\ r = -5$", r"$q = -5,\ r = -2$"],
    r"""We need $37 = (-7)q + r$ with $0 \le r < 7$:
$$37 = (-7)(-5) + 2.$$
So $q = -5$, $r = 2$. With $q = 5$ the product is $-35$ and $-35 + 2 \ne 37$. Remainders $-5$ and $-2$ are negative, so they are not allowed.""")

# 21
T.single(1, ["primes"],
    r"Which of the following is prime?",
    [r"$223$", r"$221$", r"$217$", r"$209$"],
    r"""Test primes up to $\sqrt{n}$; here $\sqrt{223} < 15$, so try $2, 3, 5, 7, 11, 13$. None divides $223$, so $223$ is prime.

The others: $221 = 13 \cdot 17$, $217 = 7 \cdot 31$, $209 = 11 \cdot 19$.""")

# 22 statements
T.statements(2, ["coprime-lcm", "gcd"],
    r"Consider the following statements, where $a, b, c$ are non-zero integers:",
    [r"If $a \mid bc$ and $\gcd(a, b) = 1$, then $a \mid c$.",
     r"$\gcd(a, b) \cdot \operatorname{lcm}(a, b) = |ab|$.",
     r"$\gcd(a, b) = 1$ if and only if $ax + by = 1$ for some integers $x, y$."],
    [r"1, 2 and 3", r"1 and 3 only", r"1 and 2 only", r"2 and 3 only"],
    r"""All three are standard results.

1. Euclid's lemma: from $1 = ax + by$, $c = acx + bcy$, and $a$ divides both terms.
2. Exponent-wise, $\min(\alpha, \beta) + \max(\alpha, \beta) = \alpha + \beta$.
3. Bézout gives "only if". Conversely, any common divisor of $a, b$ divides $ax + by = 1$.

Note that 3 needs the value $1$: $ax + by = 2$ does **not** force $\gcd(a, b) = 2$ (e.g. $3 \cdot 4 + 5 \cdot (-2) = 2$, but $\gcd(3, 5) = 1$).""")

# 23 statements
T.statements(3, ["primes"],
    r"Consider the following statements about primes:",
    [r"If $p_1, p_2, \ldots, p_n$ are the first $n$ primes, then $p_1 p_2 \cdots p_n + 1$ is prime for every $n$.",
     r"If $p$ is prime and $p \mid ab$, then $p \mid a$ or $p \mid b$.",
     r"If an integer $n > 1$ has no prime divisor $p \le \sqrt n$, then $n$ is prime."],
    [r"2 and 3 only", r"1, 2 and 3", r"2 only", r"1 and 3 only"],
    r"""1. **False.** $2 \cdot 3 \cdot 5 \cdot 7 \cdot 11 \cdot 13 + 1 = 30031 = 59 \times 509$. Euclid's proof only shows that its prime factors are new primes.
2. **True.** This is Euclid's first theorem.
3. **True.** A composite $n = rs$ with $1 < r \le s$ has $r \le \sqrt n$, and any prime factor of $r$ is $\le \sqrt n$.

So 2 and 3 only.""")

# 24 match
T.match(1, ["divisor-functions"],
    r"Match each number in List I with its number of positive divisors in List II.",
    [r"$12$", r"$36$", r"$64$", r"$30$"],
    [r"$7$", r"$8$", r"$6$", r"$9$"],
    [r"A-3, B-4, C-1, D-2", r"A-3, B-1, C-4, D-2", r"A-4, B-3, C-1, D-2", r"A-3, B-4, C-2, D-1"],
    r"""Use $\tau(n) = \prod(\alpha_i + 1)$:
- $12 = 2^2 \cdot 3$: $3 \cdot 2 = 6$
- $36 = 2^2 \cdot 3^2$: $3 \cdot 3 = 9$
- $64 = 2^6$: $7$
- $30 = 2 \cdot 3 \cdot 5$: $2 \cdot 2 \cdot 2 = 8$

So A-3, B-4, C-1, D-2. Check: the two perfect squares, $36$ and $64$, are the ones with an odd number of divisors.""")

# 25 match
T.match(2, ["gcd", "coprime-lcm"],
    r"Match each expression in List I with its value in List II.",
    [r"$\gcd(1001, 385)$", r"$\operatorname{lcm}(18, 24)$", r"$\gcd(-48, 180)$", r"$\operatorname{lcm}(21, 6)$"],
    [r"$72$", r"$12$", r"$42$", r"$77$"],
    [r"A-4, B-1, C-2, D-3", r"A-4, B-3, C-2, D-1", r"A-3, B-1, C-2, D-4", r"A-4, B-1, C-3, D-2"],
    r"""- $1001 = 7 \cdot 11 \cdot 13$, $385 = 5 \cdot 7 \cdot 11$: gcd $= 77$.
- $18 = 2 \cdot 3^2$, $24 = 2^3 \cdot 3$: lcm $= 2^3 \cdot 3^2 = 72$.
- $\gcd(-48, 180) = \gcd(48, 180) = 12$ (the gcd is always positive).
- $\operatorname{lcm}(21, 6) = \frac{21 \cdot 6}{3} = 42$, not $126$, since $\gcd(21, 6) = 3$.

So A-4, B-1, C-2, D-3.""")

# 26 AR
T.assertion_reason(2, ["primes"],
    r"There are infinitely many primes.",
    r"If $p_1, \ldots, p_n$ are primes, then no $p_i$ divides $p_1 p_2 \cdots p_n + 1$.",
    0,
    r"""Both are true, and R explains A.

R: each $p_i$ leaves remainder $1$ on dividing $N = p_1 \cdots p_n + 1$. Since $N > 1$, it has a prime factor, which by R is not in the list. So no finite list contains all primes, which is Euclid's second theorem.""")

# 27 AR
T.assertion_reason(2, ["coprime-lcm"],
    r"If $4 \mid n$ and $6 \mid n$, then $24 \mid n$.",
    r"If $a \mid n$, $b \mid n$ and $\gcd(a, b) = 1$, then $ab \mid n$.",
    3,
    r"""A is false: $n = 12$ is divisible by $4$ and $6$ but not by $24$. (In general we only get $\operatorname{lcm}(4, 6) = 12 \mid n$.)

R is true: write $n = ak$; then $b \mid ak$ with $\gcd(a, b) = 1$, so $b \mid k$ by Euclid's lemma, and $ab \mid n$. R does not apply to A because $\gcd(4, 6) = 2$.""")

# 28 AR
T.assertion_reason(2, ["diophantine"],
    r"The equation $6x + 9y = 21$ has a solution in integers.",
    r"A linear equation $ax + by = c$ has integer solutions only when $\gcd(a, b) = 1$.",
    2,
    r"""A is true: $\gcd(6, 9) = 3$ and $3 \mid 21$. Dividing by $3$, $2x + 3y = 7$ has the solution $(2, 1)$; check $12 + 9 = 21$.

R is false: the correct condition is $\gcd(a, b) \mid c$. Coprime coefficients are sufficient, not necessary. A itself is a counterexample to R.""")

# 29 AR
T.assertion_reason(3, ["induction"],
    r"For every integer $n \ge 1$, $3$ divides $n^3 + 2n$.",
    r"The product of any two consecutive integers is even.",
    1,
    r"""Both are true, but R does not explain A.

A: $n^3 + 2n = (n^3 - n) + 3n = (n - 1)n(n + 1) + 3n$. A product of **three** consecutive integers is divisible by $3$, so $3$ divides the sum. (Induction also works: $f(k + 1) - f(k) = 3k^2 + 3k + 3$.)

R is true, but divisibility by $2$ says nothing about divisibility by $3$.""")

# 30 AR
T.assertion_reason(1, ["division-algorithm"],
    r"When $-17$ is divided by $5$, the remainder given by the division algorithm is $3$.",
    r"In the division algorithm $a = bq + r$ ($b \ne 0$), the remainder satisfies $0 \le r < |b|$.",
    0,
    r"""Both are true, and R explains A. $-17 = 5(-4) + 3$ with $0 \le 3 < 5$. R is exactly why $-2$ (from $-17 = 5(-3) - 2$) is rejected and $3$ is the remainder.""")


def check():
    import sympy as sp
    from sympy import gcd, lcm, divisor_count, divisor_sigma, divisors, isprime, factorint, Rational, primerange, prod
    from itertools import product as cart

    # q1, q30
    eq(-17 // 5, -4, "q1q"); eq(-17 % 5, 3, "q1r"); eq(5 * (-4) + 3, -17, "q1")
    # q2
    eq(gcd(252, 198), 18, "q2")
    # q3: key works, distractors do not
    eq(252 * 4 + 198 * (-5), 18, "q3")
    for x, y in [(-4, 5), (5, -4), (3, -4)]:
        assert 252 * x + 198 * y != 18, "q3 distractor"
    # q4
    eq(Rational(4320, 12), 360, "q4"); eq(gcd(24, 180), 12, "q4a"); eq(lcm(24, 180), 360, "q4b"); eq(24 * 180, 4320, "q4c")
    # q5, q6
    eq(divisor_count(360), 24, "q5")
    eq(divisor_sigma(360), 1170, "q6"); eq(divisor_sigma(360) - 360, 810, "q6d")
    # q7
    sols7 = [(x, y) for x in range(1, 60) for y in range(1, 60) if 5 * x + 3 * y == 52]
    eq(len(sols7), 3, "q7"); assert sols7 == [(2, 14), (5, 9), (8, 4)], sols7
    # q8: only the key is unsolvable (gcd test)
    assert 15 % gcd(6, 10) != 0
    for a, b, c, s in [(6, 10, 14, (-1, 2)), (7, 11, 5, (-15, 10)), (12, 18, 30, (1, 1))]:
        assert c % gcd(a, b) == 0 and a * s[0] + b * s[1] == c, "q8"
    # q9
    t = sp.Symbol("t", integer=True)
    eq(3 * (2 + 5 * t) + 5 * (-1 - 3 * t), 1, "q9")
    assert sp.simplify(3 * (2 + 3 * t) + 5 * (-1 - 5 * t) - 1) != 0
    assert sp.simplify(3 * (2 + 5 * t) + 5 * (-1 + 3 * t) - 1) != 0
    # 2+10t, -1-6t: solutions, but incomplete (misses (7, -4))
    eq(3 * (2 + 10 * t) + 5 * (-1 - 6 * t), 1, "q9d")
    assert 3 * 7 + 5 * (-4) == 1 and (7 - 2) % 10 != 0
    # q10
    eq(prod(divisors(36)), 6**9, "q10")
    # q11
    vals = {int(gcd(a + b, a - b)) for a in range(1, 40) for b in range(1, 40) if a != b and gcd(a, b) == 1}
    assert vals == {1, 2}, vals
    # q12
    eq(prod(list(primerange(2, 14))) + 1, 30031, "q12"); eq(59 * 509, 30031, "q12b")
    assert not isprime(30031) and 30031 % 13 and 30031 % 7
    # q13
    eq(sp.gcd_list([n**5 - n for n in range(2, 60)]), 30, "q13")
    # q14
    eq(sp.gcd_list([3**(2 * n + 2) - 8 * n - 9 for n in range(1, 40)]), 64, "q14")
    k = sp.Symbol("k", integer=True, positive=True)
    f = lambda m: 3**(2 * m + 2) - 8 * m - 9
    eq(sp.expand(f(k + 1) - 9 * f(k)), 64 * (k + 1), "q14 step")
    # q15
    a, b = 2**3 * 3**2 * 5, 2**2 * 3**4 * 7
    eq(lcm(a, b), 22680, "q15"); eq(gcd(a, b), 36, "q15g")
    # q16
    eq(len([d for d in divisors(720) if d % 2]), 6, "q16"); eq(divisor_count(720), 30, "q16b")
    # q17
    eq(next(n for n in range(1, 10000) if divisor_count(n) == 12), 60, "q17")
    eq(divisor_count(48), 10, "q17b"); eq(divisor_count(72), 12, "q17c"); eq(divisor_count(96), 12, "q17d")
    # q18
    eq(sum(Rational(1, d) for d in divisors(360)), Rational(13, 4), "q18")
    # q19: positive evens have min 2 (WOP); others have no min — conceptual
    eq(min(range(2, 100, 2)), 2, "q19")
    # q20
    q, r = -5, 2
    eq((-7) * q + r, 37, "q20"); assert 0 <= r < 7
    # q21
    assert isprime(223) and not isprime(221) and not isprime(217) and not isprime(209)
    eq(13 * 17, 221); eq(7 * 31, 217); eq(11 * 19, 209)
    # q22: brute force all three statements
    R = [x for x in range(-30, 31) if x]
    for a_, b_ in cart(R, R):
        g = gcd(a_, b_)
        eq(g * lcm(a_, b_), abs(a_ * b_), "q22-2")
        for c_ in range(-12, 13):
            if c_ and g == 1 and (b_ * c_) % a_ == 0:
                assert c_ % a_ == 0, "q22-1"
    eq(3 * 4 + 5 * (-2), 2); eq(gcd(3, 5), 1)
    # 3: gcd=1 iff a x + b y = 1 solvable  (sympy gcdex gives Bezout coefficients)
    for a_, b_ in cart(range(1, 25), range(1, 25)):
        x_, y_, g_ = sp.gcdex(a_, b_)
        eq(a_ * x_ + b_ * y_, g_, "q22-3")
    # q23
    for n in range(1, 7):
        val = prod(list(sp.primerange(2, sp.prime(n) + 1))) + 1
        if n == 6:
            assert not isprime(val)
    for n in range(2, 2000):
        no_small = all(n % p for p in primerange(2, int(n**0.5) + 1))
        assert no_small == isprime(n), "q23-3"
    for p in primerange(2, 30):
        for a_ in range(1, 40):
            for b_ in range(1, 40):
                if (a_ * b_) % p == 0:
                    assert a_ % p == 0 or b_ % p == 0, "q23-2"
    # q24
    right = [7, 8, 6, 9]
    key24 = {"A": 3, "B": 4, "C": 1, "D": 2}
    for lab, n in zip("ABCD", [12, 36, 64, 30]):
        eq(right[key24[lab] - 1], divisor_count(n), "q24" + lab)
    # q25
    right = [72, 12, 42, 77]
    vals25 = [gcd(1001, 385), lcm(18, 24), gcd(-48, 180), lcm(21, 6)]
    key25 = {"A": 4, "B": 1, "C": 2, "D": 3}
    for lab, v in zip("ABCD", vals25):
        eq(right[key25[lab] - 1], v, "q25" + lab)
    # q26: no p_i divides product+1
    ps = list(primerange(2, 50)); N = prod(ps) + 1
    assert all(N % p == 1 for p in ps)
    # q27: A false (n=12), R true (brute force)
    assert 12 % 4 == 0 and 12 % 6 == 0 and 12 % 24
    for a_ in range(1, 20):
        for b_ in range(1, 20):
            if gcd(a_, b_) == 1:
                for n in range(1, 400):
                    if n % a_ == 0 and n % b_ == 0:
                        assert n % (a_ * b_) == 0
    # q28: A true, R false
    eq(6 * 2 + 9 * 1, 21, "q28"); assert gcd(6, 9) != 1
    # q29
    n_ = sp.Symbol("n", integer=True)
    eq(sp.expand((n_ - 1) * n_ * (n_ + 1) + 3 * n_), n_**3 + 2 * n_, "q29")
    assert all((m**3 + 2 * m) % 3 == 0 for m in range(1, 300))
    assert all((m * (m + 1)) % 2 == 0 for m in range(-50, 50))
    # q30 covered by q1


T.write(check)
