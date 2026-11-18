# Polynomials and Nature of Roots

## Division, remainder and factor theorems {#division}

A **polynomial of degree $n$** over a field $F$ ($\R$ or $\C$ here) is
$$f(x) = a_0x^n + a_1x^{n-1} + \cdots + a_{n-1}x + a_n, \qquad a_i \in F,\ a_0 \ne 0.$$
It is **monic** if $a_0 = 1$. A **root** (zero) of $f$ is an $\alpha$ with $f(\alpha) = 0$; the roots of the equation $f(x) = 0$ are the zeros of $f$.

**Division algorithm.** For polynomials $f, g$ over a field with $g \ne 0$, there are unique $q, r$ with
$$f(x) = g(x)\,q(x) + r(x), \qquad r = 0 \text{ or } \deg r < \deg g.$$

- **Remainder theorem:** the remainder when $f(x)$ is divided by $x - a$ is $f(a)$.
- **Factor theorem:** $x - a$ is a factor of $f(x)$ if and only if $f(a) = 0$.
- Dividing by $ax - b$ leaves remainder $f(b/a)$.
- Dividing by a quadratic leaves a remainder $px + q$: find $p, q$ by substituting the two roots of the divisor.

**Synthetic division** divides by $x - a$ using only the coefficients. Write every coefficient, with $0$ for missing powers. Bring down the first; then repeatedly multiply by $a$ and add to the next coefficient. The last number is the remainder $f(a)$; the others are the quotient's coefficients.

Example: $(3x^4 - 5x^3 + 0x^2 + 7x - 4) \div (x - 2)$.

| | $3$ | $-5$ | $0$ | $7$ | $-4$ |
|:---|:---:|:---:|:---:|:---:|:---:|
| $\times 2$ | | $6$ | $2$ | $4$ | $22$ |
| | $3$ | $1$ | $2$ | $11$ | $18$ |

Quotient $3x^3 + x^2 + 2x + 11$, remainder $18$. Check: $f(2) = 48 - 40 + 14 - 4 = 18$.

**Dividing by $ax - b$.** Divide synthetically by $x - \frac{b}{a}$, then divide the quotient (not the remainder) by $a$. For $(6x^3 - x^2 + 4x - 3) \div (2x - 1)$: dividing by $x - \frac12$ gives $6x^2 + 2x + 5$ with remainder $-\frac12$. So the quotient is $3x^2 + x + \frac52$ and the remainder is $-\frac12$.

:::caution
For the divisor $x + a$, the multiplier is $-a$. Using $+a$ is the commonest slip. It gives $f(a)$ instead of $f(-a)$, and such values are always among the options.
:::

:::exam-tip
Two quick root tests. If the sum of the coefficients is $0$, then $x = 1$ is a root. If the sum of the coefficients of the even powers equals that of the odd powers, then $x = -1$ is a root.
:::

## The fundamental theorem and its consequences {#fundamental-theorem}

:::keyfacts
- **Fundamental theorem of classical algebra** (statement only). Every polynomial equation of degree $n \ge 1$ with complex coefficients has at least one root in $\C$.
- **Consequence.** By the factor theorem and induction on $n$,
  $$f(x) = a_0(x - \alpha_1)(x - \alpha_2)\cdots(x - \alpha_n), \qquad \alpha_i \in \C.$$
  So a degree-$n$ equation has **exactly $n$ roots, counted with multiplicity**, and no others.
:::

If $(x - \alpha)^r$ divides $f$ but $(x - \alpha)^{r+1}$ does not, then $\alpha$ is a root of **multiplicity** $r$. It is simple if $r = 1$ and multiple if $r \ge 2$. Grouping equal roots, $f(x) = a_0\prod (x - \beta_j)^{r_j}$ with $\sum r_j = n$.

**Identity of polynomials.**

- A polynomial of degree $\le n$ with more than $n$ roots is the zero polynomial.
- If two polynomials of degree $\le n$ agree at $n + 1$ distinct points, they are identical: all their coefficients are equal.

This is used constantly. Example: if $f$ is monic of degree 3 with $f(1) = f(2) = f(3) = 0$, then $f(x) = (x - 1)(x - 2)(x - 3)$ exactly. And if a monic quartic $f$ has $f(k) = k$ for $k = 1, 2, 3, 4$, then $f(x) - x$ is a monic quartic with roots $1, 2, 3, 4$. So $f(x) = x + (x - 1)(x - 2)(x - 3)(x - 4)$.

**Over $\R$.** $\R$ is not algebraically closed: $x^2 + 1$ has no real root. Combining the theorem with conjugate pairs (next section) gives:

- Every real polynomial factors over $\R$ into **linear factors and irreducible quadratic factors** $x^2 + px + q$ with $p^2 < 4q$.
- The irreducible polynomials over $\R$ have degree 1 or 2. Over $\C$, only degree 1.

:::caution
"Exactly $n$ roots" counts multiplicity. $(x - 1)^3 = 0$ has three roots, all equal to $1$. The theorem says nothing about how many roots are **real**, and it does not give the roots by formula. General formulas exist only up to degree 4 (Cardan, Ferrari: a later topic).
:::

:::exam-tip
"How many roots does $x^n = a$ have?" Exactly $n$ in $\C$, by this theorem. How many are real depends on $n$ and the sign of $a$.
:::

## Conjugate and surd roots {#conjugate-roots}

**Complex roots of real equations.** If $f$ has **real** coefficients and $\alpha = p + iq$ ($q \ne 0$) is a root, then $\bar\alpha = p - iq$ is also a root, **with the same multiplicity**.

*Proof idea:* conjugating $f(\alpha) = 0$ gives $f(\bar\alpha) = \overline{f(\alpha)} = 0$, because the coefficients equal their own conjugates. The pair contributes the real quadratic factor
$$(x - \alpha)(x - \bar\alpha) = (x - p)^2 + q^2.$$

Consequences for a real equation of degree $n$:

- the number of non-real roots is even;
- an equation of **odd degree** has at least one real root;
- an equation of even degree may have no real root ($x^4 + 1 = 0$).

**Surd roots of rational equations.** If $f$ has **rational** coefficients and $a + \sqrt b$ is a root, where $a, b \in \Q$ and $\sqrt b$ is irrational, then $a - \sqrt b$ is also a root, with the same multiplicity. The pair contributes the rational factor $(x - a)^2 - b$.

Similarly, if $\sqrt2 + \sqrt3$ is a root of a rational equation, then so are all four numbers $\pm\sqrt2 \pm \sqrt3$. These are the roots of $x^4 - 10x^2 + 1 = 0$.

**Worked example.** Solve $x^4 - 4x^3 + 6x^2 - 4x + 5 = 0$, given that $i$ is a root.

Then $-i$ is a root too, so $x^2 + 1$ is a factor. Dividing:
$$x^4 - 4x^3 + 6x^2 - 4x + 5 = (x^2 + 1)(x^2 - 4x + 5).$$
The roots are $\pm i$ and $2 \pm i$.

**Building an equation.** The rational cubic with roots $1$ and $2 - \sqrt3$ is
$$(x - 1)\big[(x - 2)^2 - 3\big] = (x - 1)(x^2 - 4x + 1) = x^3 - 5x^2 + 5x - 1.$$

:::caution
The hypotheses matter.

- **Conjugate pairs need real coefficients.** $x^2 - (2 + i)x + 2i = (x - 2)(x - i)$ has the root $i$ but not $-i$.
- **Surd pairs need rational coefficients.** $x - \sqrt2$ has the root $\sqrt2$ but not $-\sqrt2$.
- The partner of $a + \sqrt b$ is $a - \sqrt b$, not $-a + \sqrt b$.
:::

## Descartes' rule of signs {#descartes}

Let $f(x)$ have **real** coefficients. Write its non-zero coefficients in order of descending powers and count the **sign changes** (variations) between consecutive ones. Zero coefficients are skipped.

:::keyfacts
- **Positive roots.** The number of positive roots of $f(x) = 0$ (counted with multiplicity) is never more than the number of sign changes $V$ in $f(x)$. It is $V$, or $V - 2$, or $V - 4$, ….
- **Negative roots.** Apply the same rule to $f(-x)$.
- **Zero roots.** If $x^k$ divides $f$, then $0$ is a root of multiplicity $k$. Remove it first and apply the rule to $f(x)/x^k$.
:::

Older texts state only the "at most" form: "an equation cannot have more positive roots than there are changes of sign". The parity refinement is what decides most questions. In particular:

- **One sign change** means exactly one positive root.
- **No sign change** means no positive root. For example, if every coefficient is positive, there is no positive root.

**Counting non-real roots.** Suppose $f$ has degree $n$, $f(0) \ne 0$, $f(x)$ has $V^+$ sign changes and $f(-x)$ has $V^-$. Then there are at least $n - (V^+ + V^-)$ non-real roots.

| Equation | $V^+$ | $V^-$ | Conclusion |
|:---|:---:|:---:|:---|
| $x^8 + 3x^4 + 2x - 5 = 0$ | $1$ | $1$ | 1 positive, 1 negative, 6 non-real |
| $x^6 + x^2 + 1 = 0$ | $0$ | $0$ | all 6 roots non-real |
| $x^7 + 2x^3 - x = 0$ | $1$ | $1$ | root $0$; then 1 positive, 1 negative, 4 non-real |
| $x^4 - 3x^3 + 2x^2 + 5x - 3 = 0$ | $3$ | $1$ | 3 or 1 positive, exactly 1 negative |

For the last row Descartes cannot decide alone. Tabulating gives $f(0) = -3$, $f(1) = 2$, $f(-1) = -2$, $f(-2) = 35$, and further checks show there are exactly 2 real roots (1 positive, 1 negative). So the equation has 2 non-real roots.

:::caution
Descartes gives **upper bounds with parity**, not exact counts. $x^2 - x + 1$ has two sign changes and no real root. Also, a missing term is skipped, not counted as a sign. In $x^4 - 1$ the signs are $+, -$: one change, so exactly one positive root.
:::

:::exam-tip
To get $f(-x)$ quickly, flip the signs of the **odd-power** terms only.
:::

## General properties of real equations {#general-properties}

Let $f$ have real coefficients. Then $f$ is continuous, and these facts follow.

- **Intermediate values.** Suppose $f(a)$ and $f(b)$ are non-zero.
  - If they have **opposite signs**, $f(x) = 0$ has an **odd** number of roots in $(a, b)$, so at least one.
  - If they have the **same sign**, the number of roots in $(a, b)$ is even, possibly zero.
  - Roots are counted with multiplicity.
- **Behaviour at infinity.** For large $|x|$, the sign of $f(x)$ is the sign of its leading term $a_0x^n$.
- **Odd degree** means at least one real root, whose sign is opposite to that of $a_n/a_0$. For example, if $a_0 > 0$ and $a_n < 0$, there is a positive root.
- **Even degree with $a_0 a_n < 0$** means at least one positive and at least one negative root, because $f(0)$ and $f(\pm\infty)$ have opposite signs.
- **Rational root theorem.** Suppose $f$ has integer coefficients and $p/q$, in lowest terms, is a root. Then $p \mid a_n$ and $q \mid a_0$. So a **monic** integer polynomial has no rational roots except integers, and those integers divide $a_n$.

**Worked example.** Solve $2x^3 - x^2 - 7x + 6 = 0$.

- The candidates are $\pm1, \pm2, \pm3, \pm6, \pm\frac12, \pm\frac32$.
- The sum of the coefficients is $0$, so $x = 1$ is a root.
- Synthetic division gives $2x^2 + x - 6 = (2x - 3)(x + 2)$.
- The roots are $1, \frac32, -2$.

**Irrational roots.** $x^2 - 2$ is monic with integer coefficients and has no integer root. So, by the rational root theorem, $\sqrt2$ is irrational. The same argument shows that $\sqrt[n]{m}$ is irrational unless $m$ is a perfect $n$th power.

The **relations between roots and coefficients**, symmetric functions, and transformations of equations (diminishing roots, reciprocal equations) form the next topic.

:::caution
The rational root theorem gives **candidates**, not roots. Test each by synthetic division. It also needs integer (or cleared rational) coefficients.
:::

:::exam-tip
A real equation whose terms are all positive for real $x$ has no real root. Examples: $x^4 + x^2 + 1 = 0$ and $x^6 + 3x^2 + 2 = 0$. Spot this before reaching for Descartes.
:::

## Multiple roots {#multiple-roots}

:::keyfacts
- If $\alpha$ is a root of multiplicity $r \ge 1$ of $f$, then it is a root of multiplicity **exactly $r - 1$** of $f'$. A simple root of $f$ is not a root of $f'$.
- Equivalently, $\alpha$ has multiplicity exactly $r$ if and only if
  $$f(\alpha) = f'(\alpha) = \cdots = f^{(r-1)}(\alpha) = 0, \qquad f^{(r)}(\alpha) \ne 0.$$
- The multiple roots of $f$ are exactly the roots of $\gcd(f, f')$. In particular, $f$ has a multiple root if and only if $f$ and $f'$ have a common root.
:::

*Proof idea:* if $f = (x - \alpha)^r g$ with $g(\alpha) \ne 0$, then
$$f' = (x - \alpha)^{r-1}\big[r\,g + (x - \alpha)g'\big],$$
and the bracket equals $r\,g(\alpha) \ne 0$ at $\alpha$.

**Method.** To find the multiple roots of $f$:

1. Compute $d = \gcd(f, f')$, by the Euclidean algorithm or by spotting a common root.
2. Each root of $d$ of multiplicity $s$ is a root of $f$ of multiplicity $s + 1$.
3. $f/d$ has the same roots as $f$, but all simple.

Example: $f(x) = x^4 - 5x^3 + 9x^2 - 7x + 2$. The sum of the coefficients is $0$, so $1$ is a root, and $f'(x) = 4x^3 - 15x^2 + 18x - 7$ also has the root $1$. Dividing repeatedly by $x - 1$ gives
$$f(x) = (x - 1)^3(x - 2), \qquad \gcd(f, f') = (x - 1)^2.$$

**Condition for a repeated root.** Eliminate $x$ between $f(x) = 0$ and $f'(x) = 0$. For $x^3 - 3x + k = 0$: $f'(x) = 0$ gives $x = \pm1$, and then $k = \mp2$. So there is a repeated root if and only if $k = \pm2$.

For the general cubic $x^3 + px + q = 0$, the condition is $4p^3 + 27q^2 = 0$: its discriminant vanishes.

| $f(x)$ | factorisation | multiple roots |
|:---|:---|:---|
| $x^3 + x^2 - 5x + 3$ | $(x - 1)^2(x + 3)$ | $1$ (double) |
| $x^3 - x^2 - 8x + 12$ | $(x - 2)^2(x + 3)$ | $2$ (double) |
| $x^4 - 2x^2 + 1$ | $(x - 1)^2(x + 1)^2$ | $\pm1$ (both double) |

:::caution
The converse fails: a root of $f'$ need not be a root of $f$ at all. For $f = x^3 - 3x + 2$, $f'$ vanishes at $\pm1$, but only $1$ is a (double) root of $f$.
:::

## Rolle's theorem and location of roots {#rolle-location}

**Rolle's theorem for polynomials.** If $f$ has real coefficients and $a < b$ are real roots of $f(x) = 0$, then $f'(x) = 0$ has at least one real root in $(a, b)$.

(The general theorem asks for $f$ continuous on $[a, b]$, differentiable on $(a, b)$, and $f(a) = f(b)$. Polynomials satisfy the first two automatically.)

**Consequences.**

- **Between two consecutive real roots of $f$** there is an **odd** number of roots of $f'$, counted with multiplicity.
- **Between two consecutive real roots of $f'$** there is **at most one** real root of $f$, because $f$ is monotonic there. There is exactly one if $f$ takes opposite signs at those two roots of $f'$.
- If $f$ has $m$ real roots (with multiplicity), then $f'$ has at least $m - 1$.
- If all roots of $f$ are real, so are all roots of $f'$, $f''$, ….
- If $f'$ has no real root, then $f$ has at most one real root. Example: $x^5 + x - 1$, where $f' = 5x^4 + 1 > 0$.

**Counting real roots by critical points.**

1. Solve $f'(x) = 0$ to get the real critical points $c_1 < c_2 < \cdots < c_k$.
2. Write the signs of $f(-\infty), f(c_1), \ldots, f(c_k), f(+\infty)$.
3. Each sign change marks exactly one real root in that interval. A zero value $f(c_i) = 0$ is a multiple root.

Example: $f(x) = x^3 - 6x^2 + 9x - 1$. Here $f'(x) = 3(x - 1)(x - 3)$.

| $x$ | $-\infty$ | $1$ | $3$ | $+\infty$ |
|:---|:---:|:---:|:---:|:---:|
| $f(x)$ | $-$ | $3$ | $-1$ | $+$ |

There are three changes, so there are three real roots: one in $(-\infty, 1)$ (in fact in $(0, 1)$, since $f(0) = -1$), one in $(1, 3)$ and one in $(3, \infty)$.

```plot
title: $y = x^3 - 6x^2 + 9x - 1$ has a root between each pair of sign changes
x: -0.5, 4.5
y: -3, 5
f: x^3 - 6x^2 + 9x - 1 | $y = f(x)$
point: 1, 3 | $f(1) = 3$
point: 3, -1 | $f(3) = -1$
```

**Locating a root.** Tabulate $f$ at integers until the sign changes. For $x^3 - 2x - 5$: $f(2) = -1$ and $f(3) = 16$, so the real root lies in $(2, 3)$. Refining by bisection or Newton–Raphson belongs to numerical analysis.

:::exam-tip
Rolle's theorem runs one way: from two roots of $f$ to a root of $f'$. To count the roots of $f$, use the sign table at the critical points, not Rolle alone.
:::

## Quick checks and traps {#exam-tips}

- **Remainder on division by $x - a$** is $f(a)$. For $x + a$, substitute $-a$.
- **Remainder on division by $x^2 - 1$:** find $px + q$ from $f(1)$ and $f(-1)$. For example, $x^{2k+1}$ leaves $x$ and $x^{2k}$ leaves $1$.
- **Exactly $n$ roots** means counted with multiplicity, in $\C$.
- **Conjugate pairs need real coefficients; surd pairs need rational coefficients.** A real polynomial of odd degree has a real root. A real quintic has 1, 3 or 5 real roots, never 2 or 4.
- **Descartes:** one sign change means exactly one positive root. Two changes means 2 **or 0**. Use $f(-x)$ for negative roots, by flipping the odd-power signs. Non-real roots $\ge n - V^+ - V^-$, once zero roots have been removed.
- **Multiplicity drops by one** on differentiating: multiplicity $r$ in $f$ becomes $r - 1$ in $f'$, so $\gcd(f, f')$ carries every multiple root once less.
- **Repeated root of $x^3 + px + q$** if and only if $4p^3 + 27q^2 = 0$.
- **Rolle's direction:** roots of $f$ trap roots of $f'$, not the other way round.
- **Count real roots** with a sign table at the critical points; check a quick value such as $f(0)$ or $f(1)$ to split "2 or 0".
