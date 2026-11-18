"""Questions for math.algebra.polynomials (Polynomials and Nature of Roots)."""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from qlib import Topic, eq

T = Topic("math.algebra.polynomials")

# ---------------------------------------------------------------- division
T.single(1, ["division"],
    r"The remainder when $x^4 - 3x^3 + 2x - 5$ is divided by $x - 2$ is",
    [r"$-9$", r"$31$", r"$-1$", r"$7$"],
    r"""By the remainder theorem the remainder is $f(2)$:
$$f(2) = 16 - 24 + 4 - 5 = -9.$$

$31 = f(-2)$ comes from substituting the wrong sign: for the divisor $x - a$ substitute $x = a$, not $-a$.""")

T.single(1, ["division"],
    r"Dividing $2x^3 - 3x^2 + 4x - 5$ by $x - 1$ using synthetic division gives",
    [r"quotient $2x^2 - x + 3$, remainder $-2$",
     r"quotient $2x^2 - 5x + 9$, remainder $-14$",
     r"quotient $2x^2 - x + 3$, remainder $2$",
     r"quotient $2x^2 - x - 3$, remainder $-2$"],
    r"""Use $1$ as the multiplier with the coefficients $2, -3, 4, -5$:

| | $2$ | $-3$ | $4$ | $-5$ |
|:---|:---:|:---:|:---:|:---:|
| $\times 1$ | | $2$ | $-1$ | $3$ |
| | $2$ | $-1$ | $3$ | $-2$ |

So the quotient is $2x^2 - x + 3$ and the remainder is $-2$. Check: $f(1) = 2 - 3 + 4 - 5 = -2$.

The option with remainder $-14$ is the result of using the multiplier $-1$, that is, dividing by $x + 1$.""")

T.single(1, ["division"],
    r"If $x - 3$ is a factor of $x^3 - 2x^2 + kx + 6$, then $k$ equals",
    [r"$-5$", r"$5$", r"$-13$", r"$13$"],
    r"""By the factor theorem, $f(3) = 0$:
$$27 - 18 + 3k + 6 = 0 \implies 3k = -15 \implies k = -5.$$

$-13$ comes from putting $x = -3$ instead of $x = 3$.""")

T.single(2, ["division"],
    r"A polynomial $f(x)$ leaves remainder $3$ when divided by $x - 1$ and remainder $5$ when divided by $x - 2$. The remainder when $f(x)$ is divided by $(x - 1)(x - 2)$ is",
    [r"$2x + 1$", r"$x + 2$", r"$2x - 1$", r"$3x + 5$"],
    r"""The divisor has degree 2, so the remainder is $ax + b$:
$$f(x) = (x - 1)(x - 2)q(x) + ax + b.$$
Put $x = 1$ and $x = 2$: $a + b = 3$ and $2a + b = 5$. So $a = 2$, $b = 1$, and the remainder is $2x + 1$.

Check: $2(1) + 1 = 3$ and $2(2) + 1 = 5$. The option $x + 2$ swaps $a$ and $b$; it gives $4$ at $x = 2$, not $5$.""")

T.single(2, ["division"],
    r"The remainder when $x^{101}$ is divided by $x^2 - 1$ is",
    [r"$x$", r"$1$", r"$-x$", r"$x + 1$"],
    r"""Write $x^{101} = (x^2 - 1)q(x) + ax + b$.

- $x = 1$: $1 = a + b$.
- $x = -1$: $-1 = -a + b$.

So $b = 0$, $a = 1$, and the remainder is $x$.

Fast check: $x^{101} = x\,(x^2)^{50}$, and $x^2 \equiv 1 \pmod{x^2 - 1}$, so $x^{101} \equiv x$. The answer $1$ is right for an even power such as $x^{100}$.""")

# ---------------------------------------------------------------- fundamental theorem
T.single(1, ["fundamental-theorem"],
    r"By the fundamental theorem of classical algebra, a polynomial equation of degree $n \ge 1$ with complex coefficients has",
    [r"exactly $n$ roots in $\C$, counted with multiplicity",
     r"exactly $n$ distinct roots in $\C$",
     r"at least $n$ real roots",
     r"at most $n - 1$ roots in $\C$"],
    r"""The theorem says every non-constant polynomial over $\C$ has at least one root in $\C$. Applying it repeatedly with the factor theorem gives
$$f(x) = a_0(x - \alpha_1)(x - \alpha_2)\cdots(x - \alpha_n),$$
so there are exactly $n$ roots **counted with multiplicity**.

The roots need not be distinct: $(x - 1)^2 = 0$ has degree 2 but only one distinct root.""")

T.single(2, ["fundamental-theorem", "division"],
    r"A monic polynomial $f(x)$ of degree $4$ satisfies $f(1) = 1$, $f(2) = 2$, $f(3) = 3$ and $f(4) = 4$. Then $f(5)$ equals",
    [r"$29$", r"$5$", r"$24$", r"$30$"],
    r"""Let $g(x) = f(x) - x$. Then $g$ is monic of degree 4 and vanishes at $1, 2, 3, 4$. By the factor theorem
$$g(x) = (x - 1)(x - 2)(x - 3)(x - 4).$$
So $f(5) = g(5) + 5 = 4\cdot3\cdot2\cdot1 + 5 = 29$.

The answer $5$ assumes $f(x) = x$, which is not of degree 4. The answer $24$ forgets to add back the $x$.""")

# ---------------------------------------------------------------- conjugate and surd roots
T.single(2, ["conjugate-roots"],
    r"The monic cubic with real coefficients having $2$ and $1 + i$ as roots is",
    [r"$x^3 - 4x^2 + 6x - 4$", r"$x^3 - 2x - 4$", r"$x^3 - 2x + 4$", r"$x^3 - 4x^2 + 6x + 4$"],
    r"""Real coefficients force the conjugate $1 - i$ to be a root too. The pair gives the quadratic factor
$$(x - 1 - i)(x - 1 + i) = (x - 1)^2 + 1 = x^2 - 2x + 2.$$
So
$$f(x) = (x - 2)(x^2 - 2x + 2) = x^3 - 4x^2 + 6x - 4.$$

$x^3 - 2x - 4 = (x - 2)(x^2 + 2x + 2)$ has roots $-1 \pm i$, a sign slip in the quadratic factor. Check: the product of the roots is $2(1 + i)(1 - i) = 4 = -(-4)$.""")

T.single(2, ["conjugate-roots"],
    r"One root of $x^3 - 5x^2 + 5x - 1 = 0$ is $2 + \sqrt3$. The other two roots are",
    [r"$2 - \sqrt3$ and $1$", r"$2 - \sqrt3$ and $-1$", r"$-2 + \sqrt3$ and $-1$", r"$-2 - \sqrt3$ and $1$"],
    r"""The coefficients are rational, so $2 - \sqrt3$ is also a root. The pair gives
$$(x - 2)^2 - 3 = x^2 - 4x + 1.$$
Divide: $x^3 - 5x^2 + 5x - 1 = (x^2 - 4x + 1)(x - 1)$, so the third root is $1$.

Fast check: the sum of the coefficients is $1 - 5 + 5 - 1 = 0$, so $x = 1$ is a root at once. The surd partner changes the sign of the surd part only, not of the rational part, so $-2 + \sqrt3$ is wrong.""")

T.single(2, ["conjugate-roots"],
    r"If $1 + i$ is a root of $x^3 + ax + b = 0$, where $a, b$ are real, then $(a, b)$ is",
    [r"$(-2, 4)$", r"$(2, -4)$", r"$(-2, -4)$", r"$(4, -2)$"],
    r"""Since $a, b$ are real, $1 - i$ is also a root, so $x^2 - 2x + 2$ is a factor. The $x^2$ coefficient of the cubic is $0$, so the third root $\gamma$ satisfies $(1 + i) + (1 - i) + \gamma = 0$, giving $\gamma = -2$:
$$(x^2 - 2x + 2)(x + 2) = x^3 - 2x + 4.$$
So $a = -2$, $b = 4$.

Without the sum of roots: divide $x^3 + ax + b$ by $x^2 - 2x + 2$ and set the remainder $(a + 2)x + (b - 4)$ to zero.""")

T.single(3, ["conjugate-roots"],
    r"Given that $2 + i\sqrt3$ is a root of $x^4 - 2x^3 + 4x^2 - 6x + 35 = 0$, the remaining roots are",
    [r"$2 - i\sqrt3$ and $-1 \pm 2i$",
     r"$2 - i\sqrt3$ and $1 \pm 2i$",
     r"$-2 \pm i\sqrt3$ and $2 - i\sqrt3$",
     r"$2 - i\sqrt3$ and $-1 \pm i\sqrt2$"],
    r"""Real coefficients, so $2 - i\sqrt3$ is a root, and the pair gives
$$(x - 2)^2 + 3 = x^2 - 4x + 7.$$
Divide:
$$x^4 - 2x^3 + 4x^2 - 6x + 35 = (x^2 - 4x + 7)(x^2 + 2x + 5).$$
The roots of $x^2 + 2x + 5 = 0$ are $-1 \pm 2i$.

Check with the constant term: $7 \times 5 = 35$. The option $1 \pm 2i$ comes from $x^2 - 2x + 5$, which gives an $x^3$ coefficient of $-6$, not $-2$.""")

# ---------------------------------------------------------------- Descartes
T.single(2, ["descartes"],
    r"By Descartes' rule of signs, the number of negative real roots of $x^5 - 3x^3 + 2x^2 - x + 4 = 0$ is",
    [r"exactly $1$", r"$4$, $2$ or $0$", r"$3$ or $1$", r"$0$"],
    r"""Replace $x$ by $-x$:
$$f(-x) = -x^5 + 3x^3 + 2x^2 + x + 4.$$
The signs are $-,+,+,+,+$: one change. The number of negative roots is $1$ or less by an even number, and it cannot be negative, so it is exactly $1$.

"$4$, $2$ or $0$" is the count for **positive** roots: $f(x)$ itself has signs $+,-,+,-,+$, four changes.""")

T.single(2, ["descartes"],
    r"The number of non-real roots of $x^6 + 3x^2 - 5 = 0$ is",
    [r"$4$", r"$2$", r"$6$", r"$0$"],
    r"""Signs of $f(x)$: $+,+,-$, one change, so exactly one positive root.

$f(-x) = x^6 + 3x^2 - 5$ is the same, so exactly one negative root.

$f(0) = -5 \ne 0$, so $0$ is not a root. That accounts for $2$ real roots out of $6$, and the other $6 - 2 = 4$ are non-real (a conjugate-pair count, as it must be).""")

T.single(3, ["descartes", "general-properties"],
    r"The number of real roots of $x^5 - 6x^2 - 4x + 5 = 0$ is",
    [r"$3$", r"$1$", r"$5$", r"$2$"],
    r"""Signs of $f(x) = x^5 - 6x^2 - 4x + 5$: $+,-,-,+$, two changes, so $2$ or $0$ positive roots.

$f(-x) = -x^5 - 6x^2 + 4x + 5$: $-,-,+,+$, one change, so exactly $1$ negative root.

To decide between $2$ and $0$: $f(0) = 5 > 0$, $f(1) = 1 - 6 - 4 + 5 = -4 < 0$ and $f(2) = 32 - 24 - 8 + 5 = 5 > 0$. So there is a root in $(0, 1)$ and another in $(1, 2)$: two positive roots.

Total: $3$ real roots and $2$ non-real ones. A real quintic always has an odd number of real roots, so $2$ is impossible.""")

# ---------------------------------------------------------------- general properties
T.single(2, ["general-properties"],
    r"The roots of $2x^3 - 3x^2 - 3x + 2 = 0$ are",
    [r"$-1,\ \tfrac12,\ 2$", r"$1,\ -\tfrac12,\ -2$", r"$-1,\ -\tfrac12,\ 2$", r"$1,\ \tfrac12,\ -2$"],
    r"""By the rational root theorem a rational root $p/q$ has $p \mid 2$ and $q \mid 2$: try $\pm1, \pm2, \pm\tfrac12$.

$f(2) = 16 - 12 - 6 + 2 = 0$, so divide by $x - 2$:
$$2x^3 - 3x^2 - 3x + 2 = (x - 2)(2x^2 + x - 1) = (x - 2)(2x - 1)(x + 1).$$
The roots are $2, \tfrac12, -1$.

The option $1, -\tfrac12, -2$ is the root set of $f(-x) = 0$, a sign slip. Check: the product of the roots is $-\frac{2}{2} = -1$ and $2\cdot\tfrac12\cdot(-1) = -1$.""")

# ---------------------------------------------------------------- multiple roots
T.single(1, ["multiple-roots"],
    r"If $\alpha$ is a root of multiplicity $4$ of a polynomial $f(x)$, then $\alpha$ is a root of $f'(x)$ of multiplicity",
    [r"$3$", r"$4$", r"$5$", r"$2$"],
    r"""Write $f(x) = (x - \alpha)^4 g(x)$ with $g(\alpha) \ne 0$. Then
$$f'(x) = (x - \alpha)^3\big[4g(x) + (x - \alpha)g'(x)\big],$$
and the bracket equals $4g(\alpha) \ne 0$ at $x = \alpha$. So the multiplicity drops by exactly one, to $3$.""")

T.single(2, ["multiple-roots"],
    r"The equation $x^3 - 3x + k = 0$ has a repeated root if and only if $k$ equals",
    [r"$\pm 2$", r"$\pm 1$", r"$\pm 3$", r"$0$"],
    r"""A repeated root is a common root of $f$ and $f'$. Here $f'(x) = 3x^2 - 3 = 0$ gives $x = \pm1$.

- $x = 1$: $1 - 3 + k = 0$, so $k = 2$.
- $x = -1$: $-1 + 3 + k = 0$, so $k = -2$.

So $k = \pm2$. The value $\pm1$ is the root of $f'$, not the value of $k$. For $k = 0$ the roots $0, \pm\sqrt3$ are distinct.""")

T.single(3, ["multiple-roots"],
    r"For $f(x) = x^4 - 6x^3 + 12x^2 - 10x + 3$, the monic $\gcd\big(f(x), f'(x)\big)$ is",
    [r"$(x - 1)^2$", r"$x - 1$", r"$(x - 1)^3$", r"$(x - 1)(x - 3)$"],
    r"""The sum of the coefficients is $1 - 6 + 12 - 10 + 3 = 0$, so $x = 1$ is a root. Repeated synthetic division by $x - 1$ gives
$$f(x) = (x - 1)^3(x - 3).$$
A root of multiplicity $r$ of $f$ is a root of multiplicity $r - 1$ of $f'$, and simple roots of $f$ are not roots of $f'$. So
$$\gcd(f, f') = (x - 1)^{3 - 1} = (x - 1)^2.$$

$(x - 1)^3$ is the factor of $f$, not the gcd. The simple root $3$ does not appear in the gcd.""")

# ---------------------------------------------------------------- Rolle and location
T.single(1, ["rolle-location"],
    r"If $f(x) = (x - 1)(x - 2)(x - 3)(x - 4)$, the number of real roots of $f'(x) = 0$ is",
    [r"$3$", r"$4$", r"$2$", r"$1$"],
    r"""$f$ has the four real roots $1, 2, 3, 4$. By Rolle's theorem $f'$ has a root in each of $(1,2)$, $(2,3)$ and $(3,4)$. Since $f'$ is a cubic, these are all its roots: exactly $3$ real roots.

$4$ is the degree of $f$; $f'$ has degree $3$.""")

T.single(1, ["rolle-location"],
    r"The real root of $x^3 - 2x - 5 = 0$ lies in the interval",
    [r"$(2, 3)$", r"$(1, 2)$", r"$(3, 4)$", r"$(-2, -1)$"],
    r"""Tabulate the signs:
$$f(1) = -6,\quad f(2) = 8 - 4 - 5 = -1,\quad f(3) = 27 - 6 - 5 = 16.$$
$f(2) < 0 < f(3)$, so a root lies in $(2, 3)$.

It is the only real root: $f'(x) = 3x^2 - 2$ vanishes at $\pm\sqrt{2/3}$, and the local maximum $f(-\sqrt{2/3}) \approx -3.9$ is negative, so $f < 0$ on $(-\infty, \sqrt{2/3}]$ and $f$ increases after that.

For $(1, 2)$: $f(1) = -6$ and $f(2) = -1$ have the same sign, so there is no sign change there.""")

T.single(3, ["rolle-location"],
    r"The number of distinct real roots of $3x^4 - 4x^3 - 12x^2 + 3 = 0$ is",
    [r"$4$", r"$2$", r"$0$", r"$3$"],
    r"""$f'(x) = 12x^3 - 12x^2 - 24x = 12x(x + 1)(x - 2)$, so the critical points are $-1, 0, 2$. Tabulate the signs:

| $x$ | $-\infty$ | $-1$ | $0$ | $2$ | $+\infty$ |
|:---|:---:|:---:|:---:|:---:|:---:|
| $f(x)$ | $+$ | $-2$ | $3$ | $-29$ | $+$ |

There are four sign changes, so a root lies in each of $(-\infty, -1)$, $(-1, 0)$, $(0, 2)$, $(2, \infty)$. Since $f$ is monotonic between consecutive critical points, each interval holds exactly one root: $4$ real roots.

Descartes alone gives only "$2$ or $0$ positive, $2$ or $0$ negative", so it cannot decide.""")

# ---------------------------------------------------------------- statements
T.statements(2, ["conjugate-roots", "general-properties"],
    r"Consider the following statements about polynomial equations:",
    [r"Every cubic equation with real coefficients has at least one real root.",
     r"If $\alpha$ is a non-real root of a polynomial equation with complex coefficients, then $\bar\alpha$ is also a root.",
     r"If $1 + \sqrt2$ is a root of a polynomial equation with rational coefficients, then $1 - \sqrt2$ is also a root."],
    [r"1 and 3 only", r"1 only", r"2 and 3 only", r"1, 2 and 3"],
    r"""1. True. Non-real roots of a real polynomial come in conjugate pairs, so the number of non-real roots is even and a cubic has at least one real root.
2. False. The conjugate-pair theorem needs **real** coefficients. Counterexample: $x - i = 0$ has the root $i$ but not $-i$.
3. True. With rational coefficients, $a + \sqrt b$ and $a - \sqrt b$ (with $\sqrt b$ irrational) occur together.""")

T.statements(3, ["descartes"],
    r"Let $f(x)$ be a polynomial with real coefficients and $f(0) \ne 0$. Consider the following statements about Descartes' rule of signs:",
    [r"The number of positive roots of $f(x) = 0$ equals the number of sign changes in its coefficients, or is less than it by an even number.",
     r"If the coefficients of $f(x)$ have exactly one sign change, then $f(x) = 0$ has exactly one positive root.",
     r"If the coefficients of $f(x)$ have exactly two sign changes, then $f(x) = 0$ has exactly two positive roots."],
    [r"1 and 2 only", r"1, 2 and 3", r"1 only", r"2 and 3 only"],
    r"""1. True: this is the rule (roots counted with multiplicity).
2. True: by statement 1 the count is $1$ or $1 - 2 < 0$, so it is exactly $1$.
3. False: the count may be $2$ or $0$. Counterexample: $x^2 - x + 1$ has signs $+,-,+$ (two changes) but no real root at all, since its discriminant is $-3$.""")

T.statements(3, ["multiple-roots", "rolle-location"],
    r"Let $f(x)$ be a polynomial of degree $n \ge 2$ with real coefficients. Consider the following statements:",
    [r"If $\alpha$ is a root of $f(x) = 0$ of multiplicity exactly $2$, then $f(\alpha) = f'(\alpha) = 0$ and $f''(\alpha) \ne 0$.",
     r"Between any two real roots of $f'(x) = 0$ there lies a real root of $f(x) = 0$.",
     r"If all $n$ roots of $f(x) = 0$ are real and distinct, then all roots of $f'(x) = 0$ are real and distinct."],
    [r"1 and 3 only", r"1, 2 and 3", r"1 only", r"2 and 3 only"],
    r"""1. True. $\alpha$ has multiplicity $r$ exactly when $f, f', \ldots, f^{(r-1)}$ vanish at $\alpha$ and $f^{(r)}(\alpha) \ne 0$.
2. False: Rolle's theorem goes the other way (a root of $f'$ between two roots of $f$). Counterexample: $f(x) = x^3 - 3x + 5$ has $f'(x) = 0$ at $\pm1$, but $f(-1) = 7$ and $f(1) = 3$ are both positive and $f$ is decreasing on $[-1, 1]$, so there is no root of $f$ in between.
3. True. Rolle gives a root of $f'$ in each of the $n - 1$ gaps between consecutive roots of $f$; these are distinct and $f'$ has degree $n - 1$, so they are all its roots.""")

# ---------------------------------------------------------------- match
T.match(2, ["descartes", "rolle-location"],
    r"Match each equation in List I with the number of its real roots in List II.",
    [r"$x^3 + x + 1 = 0$", r"$x^4 + x^2 + 1 = 0$", r"$x^3 - 3x + 1 = 0$", r"$x^4 - 1 = 0$"],
    [r"no real root", r"exactly one real root", r"exactly two real roots", r"three real roots"],
    [r"A-2, B-1, C-4, D-3", r"A-4, B-1, C-2, D-3", r"A-2, B-3, C-4, D-1", r"A-2, B-1, C-3, D-4"],
    r"""- **A.** $f(x)$ has no sign change, $f(-x) = -x^3 - x + 1$ has one: exactly one (negative) real root. **(2)**
- **B.** All terms are positive for real $x$, so there is no real root. **(1)**
- **C.** $f'(x) = 3x^2 - 3$ vanishes at $\pm1$; $f(-1) = 3 > 0$ and $f(1) = -1 < 0$, with $f(\mp\infty) = \mp\infty$. Three sign changes, three real roots. **(4)**
- **D.** $x^4 - 1 = (x - 1)(x + 1)(x^2 + 1)$: two real roots $\pm1$. **(3)**""")

T.match(3, ["multiple-roots"],
    r"Match each polynomial in List I with the description of its roots in List II.",
    [r"$x^3 - 3x^2 + 3x - 1$", r"$x^3 - 3x - 2$", r"$x^3 - x^2 - x + 1$", r"$x^4 - 2x^2 + 1$"],
    [r"double roots at $1$ and at $-1$", r"double root $1$, simple root $-1$", r"triple root $1$",
     r"double root $-1$, simple root $2$"],
    [r"A-3, B-4, C-2, D-1", r"A-3, B-2, C-4, D-1", r"A-1, B-4, C-2, D-3", r"A-3, B-4, C-1, D-2"],
    r"""Factorise each one:
- **A.** $x^3 - 3x^2 + 3x - 1 = (x - 1)^3$. **(3)**
- **B.** $x^3 - 3x - 2$: $f(-1) = 0$ and $f'(-1) = 3 - 3 = 0$, so $-1$ is a double root, and $(x + 1)^2(x - 2)$. **(4)**
- **C.** $x^3 - x^2 - x + 1 = x^2(x - 1) - (x - 1) = (x - 1)^2(x + 1)$. **(2)**
- **D.** $x^4 - 2x^2 + 1 = (x^2 - 1)^2 = (x - 1)^2(x + 1)^2$. **(1)**

B and C are easily swapped: test $f'$ at the candidate root to see which one is double.""")

# ---------------------------------------------------------------- assertion-reason
T.assertion_reason(2, ["conjugate-roots"],
    r"Since $i$ is a root of $x^2 - (2 + i)x + 2i = 0$, the number $-i$ is also a root.",
    r"Non-real roots of a polynomial equation with real coefficients occur in conjugate pairs.",
    3,
    r"""A is false: $x^2 - (2 + i)x + 2i = (x - 2)(x - i)$, so the roots are $2$ and $i$, and $-i$ is not a root ($(-i)^2 + (2 + i)i + 2i = -1 + 2i - 1 + 2i = -2 + 4i \ne 0$).

R is true, but it does not apply: the coefficients $-(2 + i)$ and $2i$ are not real.""")

T.assertion_reason(1, ["descartes", "general-properties"],
    r"The equation $x^4 + 3x^2 + 2 = 0$ has no real root.",
    r"A polynomial equation of even degree with real coefficients need not have a real root.",
    1,
    r"""A is true: for real $x$, $x^4 + 3x^2 + 2 \ge 2 > 0$. (Descartes agrees: neither $f(x)$ nor $f(-x)$ has a sign change, and $f(0) \ne 0$.)

R is true ($x^2 + 1 = 0$ is an example), but "need not have" says nothing about this particular equation. So R does not explain A.""")

T.assertion_reason(2, ["multiple-roots"],
    r"The equation $x^3 - 3x + 2 = 0$ has a repeated root.",
    r"Every root of $f'(x) = 0$ is a repeated root of $f(x) = 0$.",
    2,
    r"""A is true: $x^3 - 3x + 2 = (x - 1)^2(x + 2)$, with $1$ a double root.

R is false. The correct statement is the converse: a repeated root of $f$ is a root of $f'$. Here $f'(x) = 3x^2 - 3$ has the root $-1$, but $f(-1) = -1 + 3 + 2 = 4 \ne 0$.""")

T.assertion_reason(3, ["rolle-location", "general-properties"],
    r"The equation $x^5 + x - 1 = 0$ cannot have two distinct real roots.",
    r"$\frac{d}{dx}(x^5 + x - 1) = 5x^4 + 1$ has no real zero, and by Rolle's theorem a zero of $f'$ lies strictly between any two distinct real roots of $f$.",
    0,
    r"""Both are true, and R explains A.

R: $5x^4 + 1 \ge 1 > 0$ for all real $x$, and the Rolle statement is standard. A: if $a < b$ were two real roots, R would give a real zero of $5x^4 + 1$ in $(a, b)$, which is impossible.

(The degree is odd, so there is in fact exactly one real root: $f(0) = -1 < 0 < 1 = f(1)$.)""")


def check():
    import sympy as sp
    x, k = sp.symbols("x k"); a, b = sp.symbols("a b", real=True)

    def nreal(p, lo=-sp.oo, hi=sp.oo):
        return len([r for r in set(sp.real_roots(sp.Poly(p, x))) if lo < r < hi])

    # division
    eq((x**4 - 3*x**3 + 2*x - 5).subs(x, 2), -9, "q1")
    q, r = sp.div(2*x**3 - 3*x**2 + 4*x - 5, x - 1)
    eq(q, 2*x**2 - x + 3, "q2 quotient"); eq(r, -2, "q2 rem")
    q, r = sp.div(2*x**3 - 3*x**2 + 4*x - 5, x + 1)
    eq(q, 2*x**2 - 5*x + 9, "q2 distractor"); eq(r, -14, "q2 distractor rem")
    eq(sp.solve((x**3 - 2*x**2 + k*x + 6).subs(x, 3), k)[0], -5, "q3")
    sol = sp.solve([a + b - 3, 2*a + b - 5], [a, b]); eq(sol[a]*x + sol[b], 2*x + 1, "q4")
    eq(sp.rem(x**101, x**2 - 1), x, "q5")
    # fundamental theorem
    p = (x - 1)**2 * (x**2 + 1) * (x + 3)
    eq(sum(sp.roots(sp.Poly(p, x)).values()), 5, "q6 count with multiplicity")
    eq(len(sp.roots(sp.Poly(p, x))), 4, "q6 distinct fewer")
    f = (x - 1)*(x - 2)*(x - 3)*(x - 4) + x
    for t in range(1, 5): eq(f.subs(x, t), t, "q7 data")
    eq(f.subs(x, 5), 29, "q7")
    # conjugate and surd roots
    eq(sp.expand((x - 2)*(x - 1 - sp.I)*(x - 1 + sp.I)), x**3 - 4*x**2 + 6*x - 4, "q8")
    eq(sp.expand((x - 2)*(x**2 + 2*x + 2)), x**3 - 2*x - 4, "q8 distractor")
    p = x**3 - 5*x**2 + 5*x - 1
    eq(sp.Poly(p, x).count_roots(), 3, "q9 all real")
    assert set(sp.roots(p, x)) == {2 + sp.sqrt(3), 2 - sp.sqrt(3), 1}, "q9"
    p = x**3 + a*x + b
    sol = sp.solve([sp.re(sp.expand(p.subs(x, 1 + sp.I))), sp.im(sp.expand(p.subs(x, 1 + sp.I)))], [a, b])
    eq(sol[a], -2, "q10a"); eq(sol[b], 4, "q10b")
    p = x**4 - 2*x**3 + 4*x**2 - 6*x + 35
    assert set(sp.roots(p, x)) == {2 + sp.I*sp.sqrt(3), 2 - sp.I*sp.sqrt(3), -1 + 2*sp.I, -1 - 2*sp.I}, "q11"
    eq(sp.expand((x**2 - 4*x + 7)*(x**2 + 2*x + 5)), p, "q11 factor")
    # Descartes
    p = x**5 - 3*x**3 + 2*x**2 - x + 4
    eq(nreal(p, -sp.oo, 0), 1, "q12 negative roots")
    p = x**6 + 3*x**2 - 5
    eq(6 - nreal(p), 4, "q13 non-real")
    p = x**5 - 6*x**2 - 4*x + 5
    eq(nreal(p), 3, "q14"); eq(nreal(p, 0, sp.oo), 2, "q14 positive"); eq(p.subs(x, 1), -4, "q14 f(1)")
    # general properties
    p = 2*x**3 - 3*x**2 - 3*x + 2
    assert set(sp.roots(p, x)) == {-1, sp.Rational(1, 2), 2}, "q15"
    # multiple roots
    g = (x - 2)**4 * (x + 1)
    eq(sp.roots(sp.Poly(sp.diff(g, x), x))[2], 3, "q16")
    disc = sp.discriminant(x**3 - 3*x + k, x)
    assert set(sp.solve(disc, k)) == {2, -2}, "q17"
    p = x**4 - 6*x**3 + 12*x**2 - 10*x + 3
    eq(sp.expand((x - 1)**3*(x - 3)), p, "q18 factor")
    eq(sp.gcd(p, sp.diff(p, x)), (x - 1)**2, "q18")
    # Rolle and location
    eq(nreal(sp.diff((x - 1)*(x - 2)*(x - 3)*(x - 4), x)), 3, "q19")
    p = x**3 - 2*x - 5
    eq(nreal(p), 1, "q20 one real root"); eq(nreal(p, 2, 3), 1, "q20 in (2,3)")
    p = 3*x**4 - 4*x**3 - 12*x**2 + 3
    eq(nreal(p), 4, "q21")
    assert [p.subs(x, t) for t in (-1, 0, 2)] == [-2, 3, -29], "q21 table"
    # statements
    assert sp.Poly(x**3 + x + 1, x).count_roots() >= 1, "s1 cubic"
    assert sp.roots(x - sp.I, x) == {sp.I: 1}, "s1 counterexample"
    p = sp.expand((x**2 - 2*x - 1)*(x - 5))  # rational poly with root 1+sqrt2
    eq(p.subs(x, 1 + sp.sqrt(2)), 0, "s1.3a"); eq(p.subs(x, 1 - sp.sqrt(2)), 0, "s1.3b")
    eq(nreal(x**2 - x + 1), 0, "s2.3 counterexample")
    eq(nreal(x**3 - x**2 + 2*x - 5, 0, sp.oo), 1, "s2.2 one change -> one positive")
    p = (x - 3)**2 * (x + 1)
    eq(p.subs(x, 3), 0); eq(sp.diff(p, x).subs(x, 3), 0); assert sp.diff(p, x, 2).subs(x, 3) != 0, "s3.1"
    p = x**3 - 3*x + 5
    eq(nreal(p, -1, 1), 0, "s3.2 counterexample")
    p = (x - 1)*(x - 2)*(x - 4)*(x + 3)
    eq(nreal(sp.diff(p, x)), 3, "s3.3")
    # match 1
    for poly, n in [(x**3 + x + 1, 1), (x**4 + x**2 + 1, 0), (x**3 - 3*x + 1, 3), (x**4 - 1, 2)]:
        eq(nreal(poly), n, f"m1 {poly}")
    # match 2
    assert sp.roots(x**3 - 3*x**2 + 3*x - 1, x) == {1: 3}, "m2A"
    assert sp.roots(x**3 - 3*x - 2, x) == {-1: 2, 2: 1}, "m2B"
    assert sp.roots(x**3 - x**2 - x + 1, x) == {1: 2, -1: 1}, "m2C"
    assert sp.roots(x**4 - 2*x**2 + 1, x) == {1: 2, -1: 2}, "m2D"
    # assertion-reason
    p = x**2 - (2 + sp.I)*x + 2*sp.I
    eq(p.subs(x, sp.I), 0, "ar1 i root"); assert sp.expand(p.subs(x, -sp.I)) != 0, "ar1 -i not root"
    eq(nreal(x**4 + 3*x**2 + 2), 0, "ar2 A"); eq(nreal(x**2 + 1), 0, "ar2 R")
    assert sp.roots(x**3 - 3*x + 2, x) == {1: 2, -2: 1}, "ar3 A"
    eq((x**3 - 3*x + 2).subs(x, -1), 4, "ar3 R false")
    eq(nreal(x**5 + x - 1), 1, "ar4 A"); eq(nreal(5*x**4 + 1), 0, "ar4 f' no real root")


T.write(check)
