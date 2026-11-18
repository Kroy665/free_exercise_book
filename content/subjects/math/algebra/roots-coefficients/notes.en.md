# Roots, Coefficients and Transformations

## Relations between roots and coefficients {#vieta}

Let

$$f(x) = a_0x^n + a_1x^{n-1} + a_2x^{n-2} + \cdots + a_n, \qquad a_0 \ne 0,$$

have roots $\alpha_1, \alpha_2, \ldots, \alpha_n$ in $\C$, each repeated as often as its multiplicity. By the fundamental theorem, $f(x) = a_0(x - \alpha_1)(x - \alpha_2)\cdots(x - \alpha_n)$. Expanding and comparing coefficients gives **Vieta's relations**. Write $S_r$ for the sum of all products of the roots taken $r$ at a time:

$$S_r = (-1)^r\,\frac{a_r}{a_0}, \qquad r = 1, 2, \ldots, n.$$

So $S_1 = \sum \alpha_i = -\dfrac{a_1}{a_0}$, $\;S_2 = \sum_{i<j}\alpha_i\alpha_j = \dfrac{a_2}{a_0}$, and the product of all the roots is $S_n = (-1)^n\dfrac{a_n}{a_0}$. The signs alternate, starting with minus.

| Equation | $\sum\alpha$ | $\sum\alpha\beta$ | $\sum\alpha\beta\gamma$ | product |
|:---|:---:|:---:|:---:|:---:|
| $ax^2 + bx + c = 0$ | $-b/a$ | $c/a$ (product) | | |
| $ax^3 + bx^2 + cx + d = 0$ | $-b/a$ | $c/a$ | $-d/a$ (product) | |
| $ax^4 + bx^3 + cx^2 + dx + e = 0$ | $-b/a$ | $c/a$ | $-d/a$ | $e/a$ |

For a quartic, $\sum\alpha\beta$ has $\binom42 = 6$ terms and $\sum\alpha\beta\gamma$ has 4 terms.

**Consequences.**
- $\sum \dfrac{1}{\alpha_i} = \dfrac{S_{n-1}}{S_n} = -\dfrac{a_{n-1}}{a_n}$ (when $a_n \ne 0$).
- $0$ is a root $\iff a_n = 0$. Two roots are $0$ $\iff a_n = a_{n-1} = 0$.
- If $f$ is monic with integer coefficients, every rational root is an integer dividing $a_n$.

**Example.** For $2x^4 - 3x^3 + 5x^2 - 7x + 4 = 0$: $\sum\alpha = \frac32$, $\sum\alpha\beta = \frac52$, $\sum\alpha\beta\gamma = \frac72$, $\alpha\beta\gamma\delta = 2$, and $\sum\frac1\alpha = \frac{7/2}{2} = \frac74$.

:::caution
The $n$ Vieta relations do **not** solve the equation by themselves. Eliminating the unknowns just reproduces $f(x) = 0$. They help only when some extra relation among the roots is known (see [root relations](#root-relations)).
:::

:::exam-tip
Sign pattern: $-, +, -, +, \ldots$ for $S_1, S_2, S_3, \ldots$. The product of the roots of an **odd**-degree equation is $-a_n/a_0$; of an **even**-degree equation, $+a_n/a_0$.
:::

## Symmetric functions and power sums {#symmetric-functions}

A function of the roots is **symmetric** if it is unchanged by every permutation of the roots. Every symmetric polynomial in the roots is a polynomial in $S_1, \ldots, S_n$, so it can be found from the coefficients without solving the equation.

**Notation.** $\sum\alpha^2\beta$ means the sum of **all distinct terms** of that shape. For three roots it has 6 terms: $\alpha^2\beta + \alpha^2\gamma + \beta^2\alpha + \beta^2\gamma + \gamma^2\alpha + \gamma^2\beta$.

**Standard results for a cubic** with roots $\alpha, \beta, \gamma$; write $e_1 = \sum\alpha$, $e_2 = \sum\alpha\beta$, $e_3 = \alpha\beta\gamma$:

| Symmetric function | In terms of $e_1, e_2, e_3$ |
|:---|:---|
| $\sum\alpha^2$ | $e_1^2 - 2e_2$ |
| $\sum\alpha^2\beta$ | $e_1e_2 - 3e_3$ |
| $\sum\alpha^3$ | $e_1^3 - 3e_1e_2 + 3e_3$ |
| $\sum\alpha^2\beta^2$ | $e_2^2 - 2e_1e_3$ |
| $(\alpha+\beta)(\beta+\gamma)(\gamma+\alpha)$ | $e_1e_2 - e_3$ |
| $\sum 1/\alpha$ | $e_2/e_3$ |
| $\sum 1/\alpha^2$ | $(e_2^2 - 2e_1e_3)/e_3^2$ |

For $(\alpha+\beta)(\beta+\gamma)(\gamma+\alpha)$, a quicker route: $\alpha + \beta = e_1 - \gamma$, so the product is $g(e_1)$, where $g(t) = (t-\alpha)(t-\beta)(t-\gamma)$.

**Newton's identities.** Let $s_k = \sum\alpha_i^k$ for the monic equation $x^n + c_1x^{n-1} + \cdots + c_n = 0$. Then

$$s_k + c_1s_{k-1} + \cdots + c_{k-1}s_1 + k\,c_k = 0 \quad (1 \le k \le n),$$

$$s_k + c_1s_{k-1} + \cdots + c_ns_{k-n} = 0 \quad (k > n).$$

The second line is just $\sum \alpha_i^{k-n} f(\alpha_i) = 0$.

**Example.** For $x^3 + px + q = 0$ ($c_1 = 0$, $c_2 = p$, $c_3 = q$):

$$s_1 = 0,\quad s_2 = -2p,\quad s_3 = -3q,\quad s_4 = -p\,s_2 = 2p^2,\quad s_5 = -p\,s_3 - q\,s_2 = 5pq.$$

:::exam-tip
A shortcut for $\sum\alpha^3$: since each root satisfies $\alpha^3 = -p\alpha - q$, summing gives $s_3 = -p\,s_1 - 3q$. The term $-3q$ is $q$ added three times, once per root, not once.
:::

:::caution
$\sum\alpha^2\beta^2 = e_2^2 - 2e_1e_3$ has a **minus** sign. The cross terms of $(\alpha\beta + \beta\gamma + \gamma\alpha)^2$ are $2\alpha\beta\gamma(\alpha + \beta + \gamma)$, and they must be subtracted.
:::

## Equations with a given relation among the roots {#root-relations}

An extra relation among the roots, added to Vieta's relations, lets you solve the equation. Choose the form of the roots so that one Vieta relation gives a root at once.

| Relation | Take the roots as | Use first |
|:---|:---|:---|
| AP (cubic) | $a - d,\ a,\ a + d$ | sum $= 3a$ |
| AP (quartic) | $a - 3d,\ a - d,\ a + d,\ a + 3d$ | sum $= 4a$ |
| GP (cubic) | $a/r,\ a,\ ar$ | product $= a^3$ |
| HP | reciprocals in AP | transform by $y = 1/x$ first |
| $\alpha + \beta = 0$ | $\pm k$ | $x^2 - k^2$ is a factor |

**AP example.** Solve $x^3 - 12x^2 + 39x - 28 = 0$, with roots in AP. The sum is $3a = 12$, so $a = 4$. The product is $(4 - d)\cdot4\cdot(4 + d) = 28$, so $16 - d^2 = 7$ and $d = \pm3$. The roots are $1, 4, 7$. Check: $\sum\alpha\beta = 4 + 7 + 28 = 39$.

**GP example.** Solve $x^3 - 14x^2 + 56x - 64 = 0$, with roots in GP. The product is $a^3 = 64$, so $a = 4$. Then $4\left(\frac1r + 1 + r\right) = 14$ gives $r + \frac1r = \frac52$, so $r = 2$. The roots are $2, 4, 8$.

**Conditions** for $ax^3 + bx^2 + cx + d = 0$:
- Roots in **AP** $\iff$ the middle root $-\frac{b}{3a}$ is a root $\iff 2b^3 - 9abc + 27a^2d = 0$.
- Roots in **GP** $\iff$ the middle root $-\frac{c}{b}$ is a root ($b \ne 0$) $\iff ac^3 = b^3d$.

**Two roots with sum zero.** For $x^3 + px^2 + qx + r = 0$, if $\alpha + \beta = 0$ then $\gamma = -p$. Hence $(x^2 + q)(x + p)$ is the cubic, and the condition is $r = pq$. Example: $x^3 - 2x^2 - 9x + 18 = 0$ has $pq = 18 = r$; the roots are $2, \pm3$.

**Quartic example.** $x^4 - 2x^3 + 4x^2 + 6x - 21 = 0$ has two roots with sum zero. Put

$$x^4 - 2x^3 + 4x^2 + 6x - 21 = (x^2 - k)(x^2 + ax + b).$$

Comparing coefficients: $a = -2$, then $-ak = 6$ gives $k = 3$, and $b - k = 4$ gives $b = 7$. The check is $-bk = -21$. So the roots are $\pm\sqrt3$ and $1 \pm i\sqrt6$.

:::exam-tip
In a GP cubic, the middle root is $-c/b$: divide $\sum\alpha\beta = a^2\left(r + 1 + \frac1r\right)$ by $\sum\alpha = a\left(r + 1 + \frac1r\right)$. Substitute it to check the condition.
:::

## Basic transformations {#basic-transformations}

To **transform** an equation is to find, without solving it, an equation whose roots are given functions of the roots of $f(x) = 0$. If the new roots are $y = \varphi(\alpha)$ and $x$ can be written as $x = \psi(y)$, then the new equation is $f(\psi(y)) = 0$, cleared of fractions.

| New roots | Substitute | Effect on $a_0, a_1, \ldots, a_n$ |
|:---|:---|:---|
| $-\alpha_i$ | $x \to -x$ | change the sign of alternate terms ($a_1, a_3, \ldots$) |
| $k\alpha_i$ ($k \ne 0$) | $x \to x/k$ | multiply $a_r$ by $k^r$ |
| $1/\alpha_i$ ($a_n \ne 0$) | $x \to 1/x$ | reverse the order: $a_n x^n + a_{n-1}x^{n-1} + \cdots + a_0$ |
| $\alpha_i - h$ | $x \to x + h$ | see [diminishing roots](#diminishing-roots) |

**Multiplying the roots by $k$.** From $f(y/k) = 0$, multiply by $k^n$:

$$a_0y^n + k\,a_1y^{n-1} + k^2a_2y^{n-2} + \cdots + k^na_n = 0.$$

This is used to remove fractional coefficients or to make the leading coefficient $1$. Example: for $x^3 - x^2 + 2x - 1 = 0$, roots times 3 give $y^3 - 3y^2 + 18y - 27 = 0$. For $x^3 - \frac12x^2 + \frac13x - 1 = 0$, roots times 6 give $y^3 - 3y^2 + 12y - 216 = 0$, with integer coefficients.

**Reciprocal roots.** $y = 1/x$ gives $x^nf(1/x) = 0$. Example: the roots of $2x^3 - 3x^2 + 5x - 7 = 0$ have reciprocals satisfying $-7y^3 + 5y^2 - 3y + 2 = 0$, that is, $7y^3 - 5y^2 + 3y - 2 = 0$.

A transformation helps with symmetric functions. Since the reciprocals satisfy a known equation, $\sum\frac{1}{\alpha^2}$ is just $\sum y^2$ for that equation.

:::caution
For roots multiplied by $k$, substitute $x = y/k$, **not** $x = ky$. Writing $f(kx) = 0$ gives the roots **divided** by $k$. Check with one coefficient: the new sum of roots must be $k$ times the old one.
:::

## Diminishing roots and removing the second term {#diminishing-roots}

The equation whose roots are $\alpha_i - h$ (the roots **diminished** by $h$) is $f(y + h) = 0$. Expand by Taylor's theorem:

$$f(y + h) = f(h) + f'(h)\,y + \frac{f''(h)}{2!}\,y^2 + \cdots + \frac{f^{(n)}(h)}{n!}\,y^n.$$

To **increase** the roots by $h$, diminish them by $-h$.

**Synthetic-division method.** Divide $f(x)$ by $x - h$ repeatedly. The successive remainders are the coefficients of the new equation, starting from the constant term. The last quotient is $a_0$.

**Example.** Diminish the roots of $x^3 - 6x^2 + 10x - 3 = 0$ by $2$:

| Step | Coefficients | Remainder |
|:---|:---|:---:|
| Start | $1,\ -6,\ 10,\ -3$ | |
| Divide by $x - 2$ | $1,\ -4,\ 2$ | $1$ |
| Divide again | $1,\ -2$ | $-2$ |
| Divide again | $1$ | $0$ |

So the new equation is $y^3 + 0\cdot y^2 - 2y + 1 = 0$, that is, $y^3 - 2y + 1 = 0$.

**Removing the second term.** In $f(y + h)$, the coefficient of $y^{n-1}$ is $n a_0 h + a_1$. It vanishes when

$$h = -\frac{a_1}{n\,a_0},$$

which is the mean of the roots. Diminishing every root by the mean makes the new roots sum to $0$. In the example, $h = 6/3 = 2$, and indeed the $y^2$ term is gone. For $x^4 - 8x^3 + x^2 - x + 3 = 0$, $h = 8/4 = 2$.

The same idea can remove the **third** term: choose $h$ so that the coefficient of $y^{n-2}$ vanishes. That is a quadratic condition in $h$, so $h$ may be irrational or non-real.

Removing the second term reduces a cubic to $y^3 + py + q = 0$. This is the starting point of Cardan's method, which belongs to the next topic.

:::exam-tip
Diminish by $h$: substitute $x = y + h$. Remove the second term: $h$ = sum of roots ÷ $n$. Increasing the roots by $h$ changes the sum of the roots by $+nh$.
:::

:::caution
"Diminished by $h$" means $f(x + h) = 0$, **not** $f(x - h) = 0$. If $\alpha$ is a root of $f$, then $\alpha - h$ is a root of $f(x + h)$, because $f((\alpha - h) + h) = f(\alpha) = 0$.
:::

## Squares of roots and the general transformation {#general-transformation}

**Squares of the roots.** Separate the even and odd powers: $f(x) = E(x^2) + x\,O(x^2)$. Then the roots of $f$ satisfy $E(x^2) = -x\,O(x^2)$. Squaring and putting $y = x^2$:

$$E(y)^2 - y\,O(y)^2 = 0.$$

For $x^3 + px^2 + qx + r = 0$: $x(x^2 + q) = -(px^2 + r)$, so $y(y + q)^2 = (py + r)^2$, that is,

$$y^3 + (2q - p^2)\,y^2 + (q^2 - 2pr)\,y - r^2 = 0.$$

Check: the sum of the new roots is $p^2 - 2q = \sum\alpha^2$. Example: for $x^3 - 2x^2 + 3x - 1 = 0$ the squares satisfy $y^3 + 2y^2 + 5y - 1 = 0$.

**General $y = \varphi(\alpha)$.** Eliminate $x$ between $f(x) = 0$ and $y = \varphi(x)$.
1. If $y = \varphi(x)$ can be solved as $x = \psi(y)$, substitute: the new equation is $f(\psi(y)) = 0$.
2. If $\varphi$ is a symmetric expression in the roots, first use Vieta to write it as a function of **one** root.

**Example 1.** Let $\alpha, \beta, \gamma$ be the roots of $x^3 + px + q = 0$ ($q \ne 0$). Find the equation whose roots are $\beta\gamma, \gamma\alpha, \alpha\beta$. Here $\beta\gamma = \frac{\alpha\beta\gamma}{\alpha} = -\frac{q}{\alpha}$, so put $y = -q/x$, that is, $x = -q/y$:

$$-\frac{q^3}{y^3} - \frac{pq}{y} + q = 0 \;\Longrightarrow\; y^3 - py^2 - q^2 = 0.$$

Check: the sum of the new roots is $\sum\alpha\beta = p$, and their product is $(\alpha\beta\gamma)^2 = q^2$.

**Example 2.** For $x^3 - x - 1 = 0$, find $\sum\frac{1 + \alpha}{1 - \alpha}$. Put $y = \frac{1 + x}{1 - x}$, so $x = \frac{y - 1}{y + 1}$. Substitute and multiply by $(y + 1)^3$:

$$(y - 1)^3 - (y - 1)(y + 1)^2 - (y + 1)^3 = 0 \;\Longrightarrow\; y^3 + 7y^2 - y + 1 = 0.$$

So the sum is $-7$.

Other common forms:
- $y = \alpha + \frac1\alpha$
- $y = \beta + \gamma - \alpha = e_1 - 2\alpha$, a linear substitution $x = \frac{e_1 - y}{2}$

:::exam-tip
Check any transformed equation with **one** Vieta relation, usually the sum or the product of the new roots. This catches most sign slips in a few seconds.
:::

## Reciprocal equations {#reciprocal-equations}

**Definition.** $f(x) = 0$ with $a_0a_n \ne 0$ is a **reciprocal equation** if $\frac1\alpha$ is a root, with the same multiplicity, whenever $\alpha$ is. Equivalently, $x^nf(1/x) = \lambda f(x)$. Comparing the end coefficients gives $\lambda^2 = 1$, so there are two classes:

- **First class** ($\lambda = 1$): $a_{n-r} = a_r$ for every $r$. Coefficients equidistant from the ends are equal.
- **Second class** ($\lambda = -1$): $a_{n-r} = -a_r$ for every $r$. Coefficients equidistant from the ends are equal in size and opposite in sign. If $n$ is even, the middle coefficient is $0$.

| Type | Root forced | Divide by | Quotient |
|:---|:---|:---|:---|
| first class, odd degree | $x = -1$ | $x + 1$ | first class, even degree |
| second class, odd degree | $x = 1$ | $x - 1$ | first class, even degree |
| second class, even degree | $x = \pm1$ | $x^2 - 1$ | first class, even degree |
| first class, even degree | none forced | | **standard form** |

So every reciprocal equation reduces to a **standard reciprocal equation**: first class, of even degree $2m$.

**Reduction of degree.** Divide the standard form by $x^m$ and group the terms in pairs, $a_r\left(x^{m-r} + x^{-(m-r)}\right)$. Then put $z = x + \frac1x$, using

$$x^2 + \frac1{x^2} = z^2 - 2, \qquad x^3 + \frac1{x^3} = z^3 - 3z, \qquad x^4 + \frac{1}{x^4} = z^4 - 4z^2 + 2.$$

The equation of degree $2m$ becomes one of degree $m$ in $z$. Each root $z_0$ then gives two roots of $x^2 - z_0x + 1 = 0$, a reciprocal pair.

**Example.** $x^4 - 5x^3 + 8x^2 - 5x + 1 = 0$. Dividing by $x^2$:

$$\left(x^2 + \frac1{x^2}\right) - 5\left(x + \frac1x\right) + 8 = 0 \;\Longrightarrow\; z^2 - 5z + 6 = 0.$$

So $z = 2$ or $z = 3$. Then $x + \frac1x = 2$ gives $x = 1$ (double), and $x + \frac1x = 3$ gives $x = \frac{3 \pm \sqrt5}{2}$.

**Odd example.** $x^5 + 4x^4 + x^3 + x^2 + 4x + 1 = 0$ is first class of odd degree, so $x + 1$ is a factor. The quotient is $x^4 + 3x^3 - 2x^2 + 3x + 1$, which gives $z^2 + 3z - 4 = 0$, so $z = 1$ or $z = -4$. Then:
- $z = 1$: $x = \frac{1 \pm i\sqrt3}{2}$
- $z = -4$: $x = -2 \pm \sqrt3$

:::caution
$x + \frac1x = z$ is real for real $x$ only when $|z| \ge 2$. A real $z$ with $|z| < 2$ gives a pair of **non-real** roots of modulus $1$.
:::

## Quick checks and traps {#exam-tips}

- **Vieta signs** alternate $-, +, -, \ldots$. The product of the roots is $(-1)^n a_n/a_0$.
- **$\sum\alpha^2 = e_1^2 - 2e_2$** can be negative. Then the roots are not all real: for $x^3 - 2x^2 + 3x - 4 = 0$, $\sum\alpha^2 = -2$.
- **$x^3 + px + q$:** $\sum\alpha^2 = -2p$, $\sum\alpha^3 = -3q$, $\sum\alpha^4 = 2p^2$, $\sum\frac1\alpha = -\frac pq$.
- **AP cubic:** start from the sum. **GP cubic:** start from the product. **Two roots summing to $0$** in $x^3 + px^2 + qx + r$: the condition is $r = pq$.
- **Transformations:**
  - negatives: change the signs of alternate terms
  - reciprocals: reverse the coefficients
  - roots times $k$: multiply $a_r$ by $k^r$
- **Diminish by $h$:** $f(x + h)$, by repeated synthetic division. To remove the second term, take $h = -a_1/(na_0)$.
- **Reciprocal equations:**
  - odd degree, first class: $-1$ is a root
  - odd degree, second class: $1$ is a root
  - even degree, second class: both $\pm1$ are roots
  - then put $z = x + 1/x$
- **Check every transformed equation** with the sum or the product of its roots.
