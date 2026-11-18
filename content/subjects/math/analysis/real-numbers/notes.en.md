# The Real Number System

## Rationals and irrationals {#rationals-irrationals}

A real number is **rational** if it equals $\frac{p}{q}$ with $p \in \Z$ and $q \in \N$. Every rational can be put in lowest terms, with $\gcd(p, q) = 1$. A real number that is not rational is **irrational**. The irrationals are $\R \setminus \Q$.

**$\sqrt2$ is irrational.** Suppose $\sqrt2 = \frac pq$ in lowest terms. Then $p^2 = 2q^2$, so $2 \mid p^2$, and hence $2 \mid p$, because $2$ is prime. Write $p = 2k$. Then $q^2 = 2k^2$, so $2 \mid q$ as well, which contradicts $\gcd(p, q) = 1$.

The key lemma is: **if a prime $p$ divides $a^2$, then $p$ divides $a$.** The same argument proves:

- $\sqrt p$ is irrational for every prime $p$.
- For $n \in \N$, $\sqrt n$ is rational **if and only if** $n$ is a perfect square. So $\sqrt{12}$ and $\sqrt{50}$ are irrational, but $\sqrt{49} = 7$ is rational.

**$\log_2 3$ is irrational.** If $\log_2 3 = \frac pq$ with $p, q \in \N$, then $2^p = 3^q$. The left side is even and the right side is odd, which is impossible. By the same argument, $\log_m n$ is irrational whenever $m$ and $n$ have different sets of prime factors. Compare $\log_4 8 = \frac{\log_2 8}{\log_2 4} = \frac32$, which is rational.

**$\sqrt2 + \sqrt3$ is irrational.** Put $x = \sqrt2 + \sqrt3$. Then $x^2 = 5 + 2\sqrt6$, and so $(x^2 - 5)^2 = 24$, which gives $x^4 - 10x^2 + 1 = 0$. By the rational root test, the only possible rational roots are $\pm1$, and neither is a root. So $x$ is irrational.

**Arithmetic of rationals and irrationals.** Let $r, s \in \Q$, and let $\alpha, \beta$ be irrational.

| Combination | Always rational? | Example |
|:---|:---|:---|
| $r + s$, $rs$ | yes ($\Q$ is a field) | |
| $r + \alpha$ | always irrational | if $r + \alpha = s$, then $\alpha = s - r \in \Q$ |
| $r\alpha$, with $r \ne 0$ | always irrational | $\alpha = (r\alpha)/r$ |
| $\alpha + \beta$ | either | $\sqrt2 + (-\sqrt2) = 0$; $\sqrt2 + \sqrt3 \notin \Q$ |
| $\alpha\beta$ | either | $\sqrt2\cdot\sqrt8 = 4$; $\sqrt2\cdot\sqrt3 = \sqrt6 \notin \Q$ |

:::caution
"Irrational + irrational is irrational" is **false**, and so is "irrational × irrational is irrational". The irrationals are not closed under either operation. Also, $0 \cdot \alpha = 0$, so the condition $r \ne 0$ matters.
:::

The numbers $e$ and $\pi$ are also irrational. You only need these as facts; their proofs are not examined.

## R as a complete ordered field; the real line {#ordered-field}

$\R$ is a **field**: addition and multiplication are associative and commutative, $0$ and $1$ are identities, every element has an additive inverse, every nonzero element has a multiplicative inverse, and multiplication distributes over addition.

It is an **ordered field**: there is a relation $<$ such that

1. **trichotomy:** for each $a, b$, exactly one of $a < b$, $a = b$, $a > b$ holds;
2. **transitivity:** $a < b$ and $b < c$ imply $a < c$;
3. $a < b$ implies $a + c < b + c$;
4. $a < b$ and $c > 0$ imply $ac < bc$.

Some consequences: $a^2 \ge 0$ for every $a$, so $1 = 1^2 > 0$; if $a < b$ and $c < 0$, then $ac > bc$; if $0 < a < b$, then $\frac1b < \frac1a$.

$\Q$ is **also** an ordered field. What separates $\R$ from $\Q$ is the **completeness axiom** (see below): every nonempty set that is bounded above has a least upper bound. $\R$ is a **complete ordered field**, and up to isomorphism it is the only one.

**The real line as a linear continuum.** Picture $\R$ as the points of a straight line, with $0$ and $1$ marked. The order of numbers matches left-to-right order. "Linear continuum" means the line is totally ordered, has no gaps, and between any two points there is another one.

:::keyfacts
- **Cantor–Dedekind axiom.** There is a one-one correspondence between the points of a straight line and the real numbers, and this correspondence preserves order.
- Each real number corresponds to exactly one point of the line, and each point to exactly one real number.
:::

The rational points alone do **not** fill the line. The point at distance $\sqrt2$ from $0$ (the diagonal of the unit square, swung down onto the line) corresponds to no rational. So $\Q$ "has gaps", and $\R$ fills them.

**Intervals.** For $a < b$, the intervals are $(a, b)$, $[a, b]$, $[a, b)$ and $(a, b]$, together with the rays $(a, \infty)$, $[a, \infty)$ and so on. The symbol $\infty$ is notation only; it is not a real number.

:::exam-tip
The GRAD syllabus asks for these properties "without proofs". Know each axiom by name, and know that $\Q$ satisfies every ordered-field axiom but **fails completeness**.
:::

## Bounded sets, supremum and infimum {#sup-inf}

Let $S \subseteq \R$ be nonempty.

- $u$ is an **upper bound** of $S$ if $x \le u$ for all $x \in S$. $S$ is **bounded above** if it has an upper bound. Lower bounds are defined in the same way. $S$ is **bounded** if it is bounded above and below.
- The **supremum** $\sup S$ is the *least* upper bound. The **infimum** $\inf S$ is the *greatest* lower bound.
- If $\sup S \in S$, it is the **maximum** of $S$. A set can have a supremum but no maximum: $\sup\,(0, 1) = 1 \notin (0, 1)$.

:::keyfacts
- **Completeness (least upper bound) axiom.** Every nonempty subset of $\R$ that is bounded above has a supremum in $\R$.
- **Consequence.** Every nonempty subset that is bounded below has an infimum, because $\inf S = -\sup(-S)$.
- **$\varepsilon$-characterisation.** $u = \sup S$ if and only if (i) $x \le u$ for all $x \in S$, and (ii) for each $\varepsilon > 0$ there is an $x \in S$ with $x > u - \varepsilon$.
:::

**Rules.** For nonempty sets $A, B$ that are bounded above:

$$\sup(A + B) = \sup A + \sup B, \qquad \sup(cA) = c\sup A\ (c > 0), \qquad \sup(-A) = -\inf A.$$

Here $A + B = \{a + b : a \in A,\ b \in B\}$, and $a$ and $b$ are chosen **independently**.

**Standard sets** ($n, m \in \N$):

| Set | $\sup$ | $\inf$ |
|:---|:---|:---|
| $\{1/n\}$ | $1$ (a maximum) | $0$ (not attained) |
| $\{1 - 1/n\}$ | $1$ (not attained) | $0$ (a minimum) |
| $\{(-1)^n + 1/n\}$ | $\frac32$ (at $n = 2$) | $-1$ (not attained) |
| $\{(-1)^n/n\}$ | $\frac12$ (at $n = 2$) | $-1$ (at $n = 1$) |
| $\{1/m + 1/n\}$ | $2$ (at $m = n = 1$) | $0$ (not attained) |
| $\{x \in \Q : x^2 < 2\}$ | $\sqrt2$ in $\R$; none in $\Q$ | $-\sqrt2$ in $\R$ |

**Worked example: $\{(-1)^n + \frac1n\}$.** The even terms $1 + \frac1{2k}$ are $\frac32, \frac54, \frac76, \dots$, which decrease towards $1$. The odd terms $-1 + \frac1{2k-1}$ are $0, -\frac23, -\frac45, \dots$, which decrease towards $-1$ and stay above it. So $\sup = \frac32$, a maximum, and $\inf = -1$, which is not attained.

```plot
title: Terms of $(-1)^n + \frac1n$: $\sup = \frac32$ (attained), $\inf = -1$ (not attained)
x: 0, 11
y: -1.5, 2
hline: 1.5
hline: -1
point: 1, 0
point: 2, 1.5 | $n = 2$
point: 3, -0.6667
point: 4, 1.25
point: 5, -0.8
point: 6, 1.1667
point: 7, -0.8571
point: 8, 1.125
point: 9, -0.8889
point: 10, 1.1
xlabel: n
```

:::caution
**$\{x \in \Q : x^2 < 2\}$ has no supremum in $\Q$.** Any rational upper bound $r$ satisfies $r > \sqrt2$, and there is a smaller rational between $\sqrt2$ and $r$. This set is the standard proof that $\Q$ is not complete.
:::

## The Archimedean property and density {#archimedean}

:::keyfacts
- **Archimedean property.** For every $x > 0$ and every $y \in \R$, there is an $n \in \N$ with $nx > y$.
- Equivalent forms: $\N$ is **not bounded above** in $\R$; and for every $\varepsilon > 0$ there is an $n \in \N$ with $\frac1n < \varepsilon$.
:::

**Proof idea (from completeness).** Suppose $\N$ were bounded above. Let $u = \sup\N$. Since $u - 1$ is not an upper bound, some $n \in \N$ satisfies $n > u - 1$. Then $n + 1 > u$ and $n + 1 \in \N$, a contradiction.

The form with $\frac1n < \varepsilon$ is exactly why $\inf\{1/n\} = 0$: no $\varepsilon > 0$ is a lower bound.

**Consequences.**

1. **Integer part.** For each real $x$ there is a unique integer $m = \lfloor x\rfloor$ with $m \le x < m + 1$.
2. **Density of $\Q$.** If $a < b$, there is a rational $r$ with $a < r < b$. To find it, choose $n$ with $n(b - a) > 1$ and put $m = \lfloor na\rfloor + 1$. Then $na < m \le na + 1 < nb$, so $r = \frac mn$ lies strictly between $a$ and $b$.
3. **Density of the irrationals.** If $a < b$, choose a rational $r$ with $a - \sqrt2 < r < b - \sqrt2$. Then $r + \sqrt2$ is irrational and lies in $(a, b)$.
4. Repeat 2 and 3 to get **infinitely many** rationals and **infinitely many** irrationals between any two distinct reals.

**Example.** The least $n \in \N$ with $\frac1n < 0.003$: we need $n > \frac{1}{0.003} = 333.\overline3$, so $n = 334$.

**Example.** A rational between $\sqrt2 \approx 1.41421$ and $1.415$: here $b - a \approx 0.0008$, so take $n = 10^4$. Then $m = \lfloor 14142.1\rfloor + 1 = 14143$, and $r = 1.4143$ works.

:::caution
$\Q$ is also Archimedean, so the Archimedean property does **not** characterise $\R$. Completeness does. Density says nothing about how *many* rationals there are: $\Q$ is countable, while every interval $(a, b)$ is uncountable.
:::

:::exam-tip
In "between any two reals" questions, the answer is always **infinitely many of both kinds**. Options like "at least one rational but possibly no irrational" are traps.
:::

## Decimal representation {#decimals}

Every real number $x \in [0, 1)$ has a decimal expansion

$$x = 0.d_1d_2d_3\ldots = \sum_{k=1}^{\infty}\frac{d_k}{10^k}, \qquad d_k \in \{0, 1, \dots, 9\}.$$

The series converges because its partial sums increase and are bounded by $1$. Its sum is their supremum, so this uses completeness.

:::keyfacts
- $x$ is **rational** $\iff$ its decimal expansion **terminates or recurs**.
- $\frac pq$ in lowest terms **terminates** $\iff$ $q$ has no prime factors other than $2$ and $5$.
- Otherwise the expansion recurs. For $\gcd(q, 10) = 1$, the period is the order of $10$ modulo $q$; for example, $\frac17 = 0.\overline{142857}$ has period $6$.
:::

**Converting recurring decimals.** Shift the decimal point and subtract:

$$0.\overline{36} = \frac{36}{99} = \frac{4}{11}, \qquad 0.1\overline{6} = \frac{16 - 1}{90} = \frac{15}{90} = \frac16.$$

The rule for $0.a_1\ldots a_k\overline{b_1\ldots b_m}$ is: (all the digits) minus (the non-recurring digits), over $m$ nines followed by $k$ zeros.

**$0.\overline{9} = 1$.** As a geometric series,

$$0.999\ldots = \sum_{k=1}^{\infty}\frac{9}{10^k} = \frac{9/10}{1 - 1/10} = 1.$$

Alternatively, $x = 0.\overline9$ gives $10x - x = 9$, so $x = 1$. Similarly $0.24\overline9 = 0.25$.

**Non-uniqueness.** A number has **two** decimal expansions exactly when it has a terminating one: $0.5 = 0.4\overline9$. Every other real has exactly one. Books often get uniqueness by convention, ruling out expansions that end in recurring $9$s.

**Irrational decimals.** An expansion like $0.1010010001\ldots$, where the blocks of zeros keep growing, never recurs, so it is irrational.

:::caution
"Non-terminating" does **not** mean irrational: $\frac13 = 0.333\ldots$ never terminates. Irrational means **non-terminating and non-recurring**.
:::

## Absolute value and basic inequalities {#absolute-value}

$|x| = x$ if $x \ge 0$, and $|x| = -x$ if $x < 0$. Equivalently, $|x| = \max(x, -x) = \sqrt{x^2}$, and $|x - a|$ is the distance from $x$ to $a$ on the line.

**Properties.**

- $|x| \ge 0$, with equality iff $x = 0$; $|xy| = |x||y|$; and $-|x| \le x \le |x|$.
- For $a > 0$: $|x| < a \iff -a < x < a$, and $|x| > a \iff x > a$ or $x < -a$.
- So $|x - c| < \varepsilon \iff x \in (c - \varepsilon, c + \varepsilon)$, the **$\varepsilon$-neighbourhood** of $c$.

:::keyfacts
- **Triangle inequality:** $|x + y| \le |x| + |y|$, with **equality iff $xy \ge 0$**.
- **Reverse triangle inequality:** $\big||x| - |y|\big| \le |x - y|$.
- $\max(a, b) = \dfrac{a + b + |a - b|}{2}$ and $\min(a, b) = \dfrac{a + b - |a - b|}{2}$.
:::

**Proof idea.** Add $-|x| \le x \le |x|$ and $-|y| \le y \le |y|$ to get $-(|x| + |y|) \le x + y \le |x| + |y|$. This is the triangle inequality.

**Solved examples.**

1. $|2x - 1| \le 5 \iff -5 \le 2x - 1 \le 5 \iff -2 \le x \le 3$. So the solution set is $[-2, 3]$.
2. $|x - 1| + |x - 3|$ is the sum of the distances from $x$ to $1$ and to $3$. For $x \in [1, 3]$ this equals $3 - 1 = 2$. Outside $[1, 3]$ it is larger. So the minimum value is $2$, attained on all of $[1, 3]$.
3. $|x - 2| > 3 \iff x > 5$ or $x < -1$.

```plot
title: $y = \lvert x-1\rvert + \lvert x-3\rvert$ is flat at height $2$ on $[1, 3]$
x: -1, 5
y: 0, 7
f: abs(x - 1) + abs(x - 3) | $\lvert x-1\rvert+\lvert x-3\rvert$
hline: 2
```

:::caution
$|x + y| = |x| + |y|$ needs $xy \ge 0$, **not** $xy > 0$. If one of $x, y$ is $0$, equality holds too.
:::

## Nested intervals and countability {#nested-countable}

**Nested interval property.** Let $I_n = [a_n, b_n]$ be **closed, bounded** intervals with $I_1 \supseteq I_2 \supseteq \cdots$. Then $\bigcap_n I_n \ne \varnothing$. If, in addition, $b_n - a_n \to 0$, the intersection is a **single point**.

**Proof idea.** The left endpoints $a_n$ are bounded above by every $b_m$. Let $\xi = \sup_n a_n$. Then $a_n \le \xi \le b_n$ for all $n$.

Together with the Archimedean property, this property is equivalent to completeness. The full treatment, with monotone sequences, comes in the next topic.

Both hypotheses are needed:

| Family | Intersection | Why |
|:---|:---|:---|
| $[0, \frac1n]$ | $\{0\}$ | closed, bounded, lengths $\to 0$ |
| $(0, \frac1n)$ | $\varnothing$ | open: by Archimedes, every $x > 0$ has $\frac1n < x$ for some $n$ |
| $[n, \infty)$ | $\varnothing$ | closed but unbounded |
| $[-\frac1n, 1 + \frac1n]$ | $[0, 1]$ | lengths do not tend to $0$ |

For comparison, the **union** $\bigcup_n [\frac1n, 1] = (0, 1]$: $0$ is never included.

**Countability (statements only).** A set is **countable** if it is finite or in bijection with $\N$.

- $\N$, $\Z$, $\Q$ and $\Q \times \Q$ are countable. A countable union of countable sets is countable, and the set of algebraic numbers is countable.
- $\R$ is **uncountable** (Cantor), and so is every interval $(a, b)$ with $a < b$.
- So $\R \setminus \Q$ is uncountable: if it were countable, $\R = \Q \cup (\R\setminus\Q)$ would be countable. In the same way, transcendental numbers exist, and there are uncountably many of them.

Open and closed sets, limit points and Bolzano–Weierstrass belong to the later topic on point sets.

:::exam-tip
"$\Q$ is dense in $\R$" and "$\Q$ is countable" are both true and independent of each other. A set can be dense and countable ($\Q$) or dense and uncountable (the irrationals).
:::

## Quick checks and traps {#exam-tips}

- **Sup vs max.** Always ask whether the supremum is attained. $\sup\{1 - \frac1n\} = 1$ is not attained; $\sup\{\frac1n\} = 1$ is attained at $n = 1$.
- **Alternating sets.** Split $(-1)^n$ sets into even and odd terms, then find the bound of each part separately.
- **$\sup(A + B)$** uses independent choices. For $A = \{1 - \frac1n\}$ and $B = \{2 + \frac1n\}$, $\sup(A + B) = 1 + 3 = 4$, not the value $3$ you get by using the same $n$ in both.
- **$\sup(cA)$ with $c < 0$** flips to an infimum: $\sup(-2A) = -2\inf A$.
- **Completeness is the dividing line.** $\Q$ is an Archimedean ordered field, but it is not complete.
- **Closure of irrationals:** $r + \alpha$ and $r\alpha$ ($r \ne 0$) are irrational, but $\alpha + \beta$ and $\alpha\beta$ can be rational.
- **Recurring decimals:** $0.\overline{ab} = \frac{ab}{99}$; $0.\overline9 = 1$; numbers with a terminating expansion have exactly two expansions.
- **$\sqrt n \in \Q$ iff $n$ is a perfect square**; $\log_m n \notin \Q$ when $m$ and $n$ have different prime factors.
- **Nested intervals** need *closed* and *bounded* intervals: $\bigcap (0, \frac1n) = \varnothing$.
- **Cantor–Dedekind** concerns points of a line and real numbers. The least upper bound axiom is a separate axiom.
