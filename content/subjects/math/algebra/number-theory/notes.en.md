# Integers and Divisibility

## Well-ordering and induction {#induction}

**Well-ordering principle (WOP).** Every non-empty set of positive integers has a least element.

WOP is a property of $\N$ under its usual order. It fails for $\Z$ (the negative integers have no least element), for the positive rationals and for the interval $(0, 1)$. It does hold for any non-empty set of integers that is **bounded below**.

**First principle of induction.** Let $P(n)$ be a statement about positive integers. Suppose:

1. $P(1)$ is true, and
2. for every $k \ge 1$, $P(k) \Rightarrow P(k + 1)$.

Then $P(n)$ is true for all $n \ge 1$. The base may start at any integer $n_0$; the conclusion is then for all $n \ge n_0$.

**Second (strong) principle of induction.** Suppose $P(1)$ is true and, for every $k \ge 1$, the truth of $P(1), P(2), \dots, P(k)$ together implies $P(k + 1)$. Then $P(n)$ is true for all $n \ge 1$.

The WOP, the first principle and the second principle are **logically equivalent** (each can be proved from any other). Proof of the first principle from WOP: if the set $S$ of $n$ for which $P(n)$ fails were non-empty, take its least element $m$. Then $m > 1$ and $P(m - 1)$ is true, so $P(m)$ is true, a contradiction.

**Worked example (first principle).** Show $64 \mid 3^{2n+2} - 8n - 9$ for all $n \ge 1$.

- $n = 1$: $81 - 17 = 64$.
- Let $f(n) = 3^{2n+2} - 8n - 9$. Then $f(k + 1) - 9f(k) = -8(k + 1) - 9 + 72k + 81 = 64k + 64$.
- So $f(k + 1) = 9f(k) + 64(k + 1)$, and $64 \mid f(k)$ gives $64 \mid f(k + 1)$.

**Worked example (second principle).** Every integer $n \ge 2$ has a prime factor. If $n$ is prime, done. Otherwise $n = ab$ with $2 \le a < n$; by the hypothesis for $a$, $a$ has a prime factor, and it divides $n$. Here the step uses $P(a)$ for some smaller $a$, not just $P(n - 1)$, so the strong form is needed.

:::caution
Both steps are needed. "$P(k) \Rightarrow P(k + 1)$" alone proves nothing: $n = n + 1$ satisfies the inductive step but is never true.
:::

:::exam-tip
For divisibility results like $6 \mid n^3 - n$ or $30 \mid n^5 - n$, factor first: $n^3 - n = (n - 1)n(n + 1)$, a product of three consecutive integers. This is often quicker than induction.
:::

## Divisibility and the division algorithm {#division-algorithm}

For integers $a, b$, **$a$ divides $b$** (written $a \mid b$) if $b = ac$ for some integer $c$. Basic facts:

- $a \mid 0$ for every $a$; $0 \mid b$ only if $b = 0$; $\pm1 \mid b$ always.
- $a \mid b$ and $b \mid c \Rightarrow a \mid c$.
- $a \mid b$ and $a \mid c \Rightarrow a \mid (bx + cy)$ for all integers $x, y$.
- $a \mid b$ and $b \mid a \Rightarrow a = \pm b$.
- $a \mid b$ with $b \ne 0 \Rightarrow |a| \le |b|$.

:::keyfacts
- **Division algorithm.** Let $a, b$ be integers with $b \ne 0$. There exist **unique** integers $q, r$ with
  $$a = bq + r, \qquad 0 \le r < |b|.$$
:::

**Proof idea.** Existence: the set $\{a - bx : x \in \Z\} \cap \{0, 1, 2, \dots\}$ is non-empty, so by WOP it has a least element $r$; if $r \ge |b|$, subtracting $|b|$ gives a smaller element. Uniqueness: if $bq + r = bq' + r'$, then $|b| \cdot |q - q'| = |r' - r| < |b|$, so $q = q'$.

**The remainder is never negative.** This is where most errors occur with negative numbers.

| Division | Correct form | $q$ | $r$ |
|:---|:---|:---:|:---:|
| $17 \div 5$ | $17 = 5 \cdot 3 + 2$ | $3$ | $2$ |
| $-17 \div 5$ | $-17 = 5 \cdot (-4) + 3$ | $-4$ | $3$ |
| $17 \div (-5)$ | $17 = (-5)(-3) + 2$ | $-3$ | $2$ |
| $-17 \div (-5)$ | $-17 = (-5) \cdot 4 + 3$ | $4$ | $3$ |

:::caution
$-17 = 5(-3) - 2$ is **not** the division algorithm, because $r = -2 < 0$. For a negative dividend, take the quotient one step further from zero and the remainder becomes $|b| - 2 = 3$.
:::

**Consequences.** Every integer is of the form $2k$ or $2k + 1$; of the form $3k, 3k + 1$ or $3k + 2$; and so on. For example, every square has the form $4k$ or $4k + 1$, so no integer of the form $4k + 3$ is a sum of two squares.

These remainder classes are the start of congruence modulo $n$, which is treated in modern algebra (sets, relations and congruence classes).

## GCD, Bézout and the Euclidean algorithm {#gcd}

Let $a, b$ be integers, not both zero. A positive integer $d$ is the **greatest common divisor**, $d = \gcd(a, b)$, if

1. $d \mid a$ and $d \mid b$, and
2. whenever $c \mid a$ and $c \mid b$, we have $c \mid d$.

:::keyfacts
- **Existence and Bézout's identity.** $\gcd(a, b)$ exists, and there are integers $x, y$ with
  $$\gcd(a, b) = ax + by.$$
  In fact $\gcd(a, b)$ is the **least positive** integer of the form $ax + by$.
- **Uniqueness.** If $d$ and $d'$ both satisfy the definition, then $d \mid d'$ and $d' \mid d$, so $d = d'$ (both are positive).
:::

**Proof idea.** $S = \{ax + by > 0 : x, y \in \Z\}$ is non-empty, so by WOP it has a least element $d = ax_0 + by_0$. Divide $a$ by $d$: the remainder $a - dq$ is again of the form $ax + by$ and is smaller than $d$, so it must be $0$. Hence $d \mid a$; similarly $d \mid b$. Any common divisor of $a$ and $b$ divides $ax_0 + by_0 = d$.

The integers $x, y$ are **not unique**: $(x + bt/d,\; y - at/d)$ also works for every integer $t$. Also, $\gcd(a, b) = \gcd(|a|, |b|)$ and $\gcd(a, 0) = |a|$.

**Euclidean algorithm.** If $a = bq + r$, then $\gcd(a, b) = \gcd(b, r)$. Repeat until the remainder is $0$; the last non-zero remainder is the gcd.

$$\begin{aligned}
252 &= 1 \cdot 198 + 54\\
198 &= 3 \cdot 54 + 36\\
54 &= 1 \cdot 36 + 18\\
36 &= 2 \cdot 18 + 0
\end{aligned}$$

So $\gcd(252, 198) = 18$.

**Back-substitution.** Work upwards, writing each remainder in terms of the previous two:

$$18 = 54 - 36 = 54 - (198 - 3 \cdot 54) = 4 \cdot 54 - 198 = 4(252 - 198) - 198 = 4 \cdot 252 - 5 \cdot 198.$$

Check: $1008 - 990 = 18$.

:::exam-tip
To test a claimed Bézout pair, just multiply out: $252 \cdot 4 - 198 \cdot 5 = 18$. A sign slip gives $-18$, which is a common distractor.
:::

**Useful rules.** For $m \ne 0$: $\gcd(ma, mb) = |m|\gcd(a, b)$. If $d = \gcd(a, b)$, then $\gcd\!\left(\tfrac{a}{d}, \tfrac{b}{d}\right) = 1$. And $\gcd(a, b) = \gcd(a, b + ka)$ for every integer $k$.

## Coprime integers and the lcm {#coprime-lcm}

$a$ and $b$ are **relatively prime (coprime)** if $\gcd(a, b) = 1$. By Bézout, and because $1$ is the least positive integer,

$$\gcd(a, b) = 1 \iff ax + by = 1 \text{ for some integers } x, y.$$

So $\gcd(n, n + 1) = 1$ (take $x = -1$, $y = 1$), and $\gcd(2n + 1, 3n + 1) = 1$ (use $3(2n + 1) - 2(3n + 1) = 1$).

:::keyfacts
- **Euclid's lemma.** If $a \mid bc$ and $\gcd(a, b) = 1$, then $a \mid c$.
- If $a \mid c$, $b \mid c$ and $\gcd(a, b) = 1$, then $ab \mid c$.
- If $\gcd(a, b) = \gcd(a, c) = 1$, then $\gcd(a, bc) = 1$.
:::

Proof of Euclid's lemma: $1 = ax + by$, so $c = acx + bcy$; $a$ divides both terms, so $a \mid c$.

:::caution
The coprimality hypothesis matters. $4 \mid 12$ and $6 \mid 12$, but $24 \nmid 12$. Similarly $6 \mid 4 \cdot 9$, yet $6 \nmid 4$ and $6 \nmid 9$.
:::

**Least common multiple.** For non-zero $a, b$, $\operatorname{lcm}(a, b)$ is the positive integer $m$ with $a \mid m$, $b \mid m$, and $m \mid n$ for every common multiple $n$.

$$\gcd(a, b) \cdot \operatorname{lcm}(a, b) = |ab|.$$

So $\operatorname{lcm}(a, b) = |ab|$ exactly when $a, b$ are coprime. Example: $\gcd(252, 198) = 18$, so $\operatorname{lcm} = \frac{252 \cdot 198}{18} = 2772$.

**From factorisations.** If $a = \prod p_i^{\alpha_i}$ and $b = \prod p_i^{\beta_i}$ (exponents $\ge 0$), then

$$\gcd(a, b) = \prod p_i^{\min(\alpha_i, \beta_i)}, \qquad \operatorname{lcm}(a, b) = \prod p_i^{\max(\alpha_i, \beta_i)}.$$

Since $\min + \max = \alpha_i + \beta_i$, this proves $\gcd \cdot \operatorname{lcm} = ab$ for positive $a, b$.

:::exam-tip
If $\gcd(a, b) = 1$, then $\gcd(a + b, a - b)$ is $1$ or $2$: any common divisor divides the sum $2a$ and the difference $2b$, hence divides $\gcd(2a, 2b) = 2$. Both values occur ($a, b = 2, 1$ gives $1$; $a, b = 3, 1$ gives $2$).
:::

## Primes and unique factorisation {#primes}

An integer $p > 1$ is **prime** if its only positive divisors are $1$ and $p$; an integer $n > 1$ that is not prime is **composite**. $1$ is neither.

:::keyfacts
- **Euclid's first theorem.** If $p$ is prime and $p \mid ab$, then $p \mid a$ or $p \mid b$. More generally, $p \mid a_1 a_2 \cdots a_n \Rightarrow p \mid a_i$ for some $i$.
- **Euclid's second theorem.** There are infinitely many primes.
- **Fundamental theorem of arithmetic.** Every integer $n > 1$ is a product of primes, and this factorisation is unique apart from the order of the factors:
  $$n = p_1^{\alpha_1} p_2^{\alpha_2} \cdots p_k^{\alpha_k}, \qquad p_1 < p_2 < \cdots < p_k,\ \alpha_i \ge 1.$$
:::

**First theorem.** If $p \nmid a$, then $\gcd(p, a) = 1$ (the only positive divisors of $p$ are $1$ and $p$), and Euclid's lemma gives $p \mid b$. The property characterises primes: for composite $n = rs$ ($1 < r, s < n$), $n \mid rs$ but $n \nmid r$ and $n \nmid s$.

**Second theorem.** Suppose $p_1, \dots, p_n$ were all the primes. Let $N = p_1 p_2 \cdots p_n + 1$. $N > 1$, so it has a prime factor $p$. Each $p_i$ leaves remainder $1$ on dividing $N$, so $p \ne p_i$ for every $i$: a contradiction.

:::caution
The proof does **not** say $N$ is prime. $2 \cdot 3 \cdot 5 \cdot 7 \cdot 11 \cdot 13 + 1 = 30031 = 59 \times 509$. It only says every prime factor of $N$ is a new prime.
:::

**Unique factorisation.** Existence: by strong induction (a composite $n = ab$ with smaller $a, b$). Uniqueness: if $p_1 \cdots p_r = q_1 \cdots q_s$, then $p_1$ divides some $q_j$ by the first theorem, so $p_1 = q_j$; cancel and repeat.

**Primality test.** If $n > 1$ is composite, it has a prime factor $p \le \sqrt n$. So to test $n$, try only the primes up to $\sqrt n$. For $223$: $\sqrt{223} < 15$, and none of $2, 3, 5, 7, 11, 13$ divides it, so $223$ is prime. But $221 = 13 \cdot 17$ and $209 = 11 \cdot 19$.

**Irrationality.** Unique factorisation shows $\sqrt p$ is irrational for every prime $p$: from $a^2 = p b^2$, the exponent of $p$ is even on the left and odd on the right.

## Number and sum of divisors {#divisor-functions}

Let $n = p_1^{\alpha_1} p_2^{\alpha_2} \cdots p_k^{\alpha_k}$. By unique factorisation, the positive divisors of $n$ are exactly the numbers $p_1^{\beta_1} \cdots p_k^{\beta_k}$ with $0 \le \beta_i \le \alpha_i$.

:::keyfacts
- **Number of divisors:** $\tau(n) = (\alpha_1 + 1)(\alpha_2 + 1) \cdots (\alpha_k + 1)$.
- **Sum of divisors:** $\sigma(n) = \displaystyle\prod_{i=1}^{k} \left(1 + p_i + \cdots + p_i^{\alpha_i}\right) = \prod_{i=1}^{k} \frac{p_i^{\alpha_i + 1} - 1}{p_i - 1}$.
- **Product of divisors:** $n^{\tau(n)/2}$.
:::

(Some books write $d(n)$ for $\tau(n)$.)

**Worked example.** $360 = 2^3 \cdot 3^2 \cdot 5$.

$$\tau(360) = 4 \cdot 3 \cdot 2 = 24, \qquad \sigma(360) = (1 + 2 + 4 + 8)(1 + 3 + 9)(1 + 5) = 15 \cdot 13 \cdot 6 = 1170.$$

| $n$ | Factorisation | $\tau(n)$ | $\sigma(n)$ |
|:---|:---|:---:|:---:|
| $12$ | $2^2 \cdot 3$ | $6$ | $28$ |
| $28$ | $2^2 \cdot 7$ | $6$ | $56$ |
| $36$ | $2^2 \cdot 3^2$ | $9$ | $91$ |
| $100$ | $2^2 \cdot 5^2$ | $9$ | $217$ |
| $p$ prime | $p$ | $2$ | $p + 1$ |

**Facts used in questions.**

- $\tau(n)$ is odd $\iff$ $n$ is a perfect square (the divisors pair off as $d \leftrightarrow n/d$, except $d = \sqrt n$).
- $\tau$ and $\sigma$ are **multiplicative**: $\tau(mn) = \tau(m)\tau(n)$ and $\sigma(mn) = \sigma(m)\sigma(n)$ when $\gcd(m, n) = 1$. They are not completely multiplicative: $\sigma(4) = 7 \ne \sigma(2)^2 = 9$.
- **Odd divisors:** count the divisors of the odd part. $720 = 2^4 \cdot 3^2 \cdot 5$ has $3 \cdot 2 = 6$ odd divisors and $30 - 6 = 24$ even ones.
- **Sum of reciprocals of the divisors:** $\sum_{d \mid n} \frac1d = \frac{\sigma(n)}{n}$.
- $n$ is **perfect** if $\sigma(n) = 2n$: $6, 28, 496$.

:::exam-tip
For "the smallest $n$ with exactly $k$ divisors", write $k$ as a product $(\alpha_1 + 1)(\alpha_2 + 1)\cdots$ in every way, and give the **largest exponents to the smallest primes**. For $k = 12$: $2^{11}$, $2^5 \cdot 3$, $2^3 \cdot 3^2$, $2^2 \cdot 3 \cdot 5$. The smallest is $2^2 \cdot 3 \cdot 5 = 60$.
:::

## Linear Diophantine equations {#diophantine}

A **linear Diophantine equation** is $ax + by = c$ with integers $a, b, c$ ($a, b$ not both zero), to be solved in integers $x, y$.

:::keyfacts
- **Solvability.** Let $d = \gcd(a, b)$. The equation has an integer solution **if and only if** $d \mid c$.
- **General solution.** If $(x_0, y_0)$ is one solution, all solutions are
  $$x = x_0 + \frac{b}{d}\,t, \qquad y = y_0 - \frac{a}{d}\,t, \qquad t \in \Z.$$
:::

**Why.** $d$ divides $ax + by$, so $d \nmid c$ means no solution. If $c = dk$ and $d = ax' + by'$, then $(kx', ky')$ is a solution. If $(x, y)$ is another, then $a(x - x_0) = -b(y - y_0)$. Divide by $d$: $\frac ad (x - x_0) = -\frac bd (y - y_0)$ with $\gcd(\frac ad, \frac bd) = 1$. Euclid's lemma gives $\frac bd \mid x - x_0$.

**Method.**

1. Find $d$ by the Euclidean algorithm; check $d \mid c$.
2. Back-substitute to write $d = ax' + by'$; multiply by $c/d$.
3. Write the general solution. For positive solutions, impose $x > 0$, $y > 0$ and count the integers $t$.

**Worked example.** $172x + 20y = 1000$.

- $172 = 8 \cdot 20 + 12$, $20 = 12 + 8$, $12 = 8 + 4$, $8 = 2 \cdot 4$. So $d = 4$, and $4 \mid 1000$.
- $4 = 12 - 8 = 12 - (20 - 12) = 2 \cdot 12 - 20 = 2(172 - 8 \cdot 20) - 20 = 2 \cdot 172 - 17 \cdot 20$.
- Multiply by $250$: $x_0 = 500$, $y_0 = -4250$.
- General solution: $x = 500 + 5t$, $y = -4250 - 43t$.
- $y > 0 \Rightarrow t \le -99$; $x > 0 \Rightarrow t \ge -99$. So $t = -99$ gives the only positive solution, $(x, y) = (5, 7)$. Check: $860 + 140 = 1000$.

**Small cases by remainders.** For $5x + 3y = 52$ in positive integers: $3y = 52 - 5x$ must leave remainder $2$ on division by $5$, so $y$ must leave remainder $4$. So $y = 4, 9, 14$ give $x = 8, 5, 2$: three solutions.

:::caution
In the general solution the steps are $\frac bd$ and $\frac ad$, **not** $b$ and $a$. Using $b$ and $a$ misses solutions whenever $d > 1$. The signs must also be opposite: $x$ goes up when $y$ goes down.
:::

## Quick checks and traps {#exam-tips}

- **Remainder is never negative:** $-17 = 5(-4) + 3$, so $r = 3$, not $-2$. With a negative divisor, $37 = (-7)(-5) + 2$.
- **Least positive value** of $ax + by$ is $\gcd(a, b)$. For $84x + 60y$ it is $12$. Every value is a multiple of $12$.
- **gcd × lcm = $|ab|$** for two numbers only. It fails for three: $\gcd(2, 4, 6) \cdot \operatorname{lcm}(2, 4, 6) = 2 \cdot 12 \ne 48$.
- **Coprimality is needed** to combine divisors: $4 \mid n$ and $6 \mid n$ give only $12 \mid n$.
- **$p_1 \cdots p_n + 1$ need not be prime** ($30031 = 59 \cdot 509$).
- **"Largest integer dividing $f(n)$ for all $n$":** compute $f$ at the first one or two values. The answer cannot exceed $\gcd(f(1), f(2))$. For $n^5 - n$: $f(2) = 30$, and $30 \mid n^5 - n$ always, so the answer is $30$.
- **Product of the divisors of $n$** is $n^{\tau(n)/2}$. For $36$: $36^{9/2} = 6^9$.
- **Diophantine solvability** depends only on $\gcd(a, b) \mid c$, not on $a, b$ being coprime.
