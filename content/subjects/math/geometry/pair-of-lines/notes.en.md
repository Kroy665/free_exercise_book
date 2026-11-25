# Pair of Straight Lines

## Homogeneous equation: lines through the origin {#homogeneous}

The equation

$$ax^2 + 2hxy + by^2 = 0 \qquad (a, h, b \text{ real, not all zero})$$

is **homogeneous** of degree 2. It always represents a pair of lines through the origin, which may be real or imaginary.

**Why.** If $b \ne 0$, divide by $x^2$ and put $m = y/x$:

$$bm^2 + 2hm + a = 0.$$

Its roots $m_1, m_2$ are the slopes, and the equation factorises as $b(y - m_1x)(y - m_2x) = 0$. (If $b = 0$, then $x = 0$ is one of the lines.)

| Condition | Lines |
|:---|:---|
| $h^2 > ab$ | two real, distinct lines through $O$ |
| $h^2 = ab$ | two coincident real lines (a perfect square) |
| $h^2 < ab$ | imaginary lines; the only real point is $O$ |

**Slopes** (for $b \ne 0$):

$$m_1 + m_2 = -\frac{2h}{b}, \qquad m_1 m_2 = \frac{a}{b}.$$

Example: $2x^2 + 5xy + 3y^2 = (2x + 3y)(x + y)$. The slopes are $-\tfrac23$ and $-1$, with sum $-\tfrac53 = -\tfrac{2h}{b}$ and product $\tfrac23 = \tfrac{a}{b}$.

**Related pairs through $O$:**
- The pair **perpendicular** to $ax^2 + 2hxy + by^2 = 0$ is $bx^2 - 2hxy + ay^2 = 0$. (Swap $a$ and $b$ and change the sign of $h$.)
- The product of the perpendiculars from $(\alpha, \beta)$ to the pair is
  $$\frac{\lvert a\alpha^2 + 2h\alpha\beta + b\beta^2\rvert}{\sqrt{(a - b)^2 + 4h^2}}.$$
- The pair and the line $lx + my + n = 0$ form a triangle of area
  $$\frac{n^2\sqrt{h^2 - ab}}{\lvert am^2 - 2hlm + bl^2\rvert}.$$

:::exam-tip
To test whether a given line $y = mx$ belongs to the pair, substitute it: $a + 2hm + bm^2 = 0$. For $6x^2 - xy + 4cy^2 = 0$ to contain $3x + 4y = 0$, put $m = -\tfrac34$: $6 + \tfrac34 + \tfrac{9c}{4} = 0$, so $c = -3$.
:::

## Angle between the lines {#angle}

If $\theta$ is an angle between the lines $ax^2 + 2hxy + by^2 = 0$, then

$$\tan\theta = \frac{2\sqrt{h^2 - ab}}{a + b}.$$

**Derivation.** $\tan\theta = \dfrac{m_1 - m_2}{1 + m_1m_2}$, with $(m_1 - m_2)^2 = (m_1 + m_2)^2 - 4m_1m_2 = \dfrac{4(h^2 - ab)}{b^2}$ and $1 + m_1m_2 = \dfrac{a + b}{b}$.

The **acute** angle uses $\lvert a + b\rvert$ in the denominator. Equivalently,

$$\cos\theta = \frac{\lvert a + b\rvert}{\sqrt{(a - b)^2 + 4h^2}}.$$

:::keyfacts
- **Perpendicular** $\iff a + b = 0$ (coefficient of $x^2$ + coefficient of $y^2$ = 0).
- **Coincident** $\iff h^2 = ab$.
- The angle depends only on $a, h, b$.
:::

When $a + b = 0$, we have $h^2 - ab = h^2 + a^2 \ge 0$. So the lines are automatically real; no separate reality check is needed.

**Examples.**
- $x^2 - 4xy + y^2 = 0$: $\tan\theta = \dfrac{2\sqrt{4 - 1}}{2} = \sqrt3$, so $\theta = \dfrac{\pi}{3}$.
- $6x^2 - 5xy - 6y^2 = 0$: $a + b = 0$, so the lines are perpendicular. Indeed, it equals $(3x + 2y)(2x - 3y)$.
- $kx^2 + 12xy + 9y^2 = 0$ is a pair of coincident lines when $36 = 9k$, that is, $k = 4$. The equation is then $(2x + 3y)^2 = 0$.

:::caution
In $ax^2 + 2hxy + by^2$, the $xy$ coefficient is $2h$, **not** $h$. For $x^2 - 4xy + y^2$, $h = -2$. Using $h = -4$ is the most common slip.
:::

The **same formula** gives the angle between the lines of a general pair $ax^2 + 2hxy + by^2 + 2gx + 2fy + c = 0$ (see [the general equation](#general-condition)). The first-degree terms only shift the lines parallel to themselves.

## Angle bisectors {#bisectors}

The bisectors of the angles between the lines $ax^2 + 2hxy + by^2 = 0$ are

$$\frac{x^2 - y^2}{a - b} = \frac{xy}{h}, \qquad\text{that is,}\qquad h(x^2 - y^2) = (a - b)xy.$$

**Derivation.** A point $(x, y) = r(\cos\phi, \sin\phi)$ lies on a bisector when $\phi = \tfrac12(\theta_1 + \theta_2)$ or this plus $\tfrac{\pi}{2}$, where $\tan\theta_{1}, \tan\theta_2$ are the slopes. Then $\tan 2\phi = \tan(\theta_1 + \theta_2) = \dfrac{m_1 + m_2}{1 - m_1m_2} = \dfrac{2h}{a - b}$. Since $\tan 2\phi = \dfrac{2xy}{x^2 - y^2}$, the result follows.

Facts:
- In $hx^2 - (a - b)xy - hy^2 = 0$, the $x^2$ and $y^2$ coefficients add to $0$. So the **two bisectors are always perpendicular**.
- If $h = 0$ (and $a \ne b$), the lines are symmetric about the axes, and the bisectors are $xy = 0$.
- If $a = b$ (and $h \ne 0$), the bisectors are $x^2 - y^2 = 0$, that is, $y = \pm x$.

Example: for $2x^2 + 6xy + y^2 = 0$, $h = 3$ and $a - b = 1$. So the bisectors are

$$3(x^2 - y^2) = xy, \qquad 3x^2 - xy - 3y^2 = 0.$$

```plot
title: $x^2 - 4xy + y^2 = 0$ (at $15^\circ$ and $75^\circ$) with its bisectors $x^2 - y^2 = 0$
x: -3, 3
y: -3, 3
equal: true
implicit: x^2 - 4xy + y^2 = 0 | $x^2 - 4xy + y^2 = 0$
implicit: x^2 - y^2 = 0 | bisectors $y = \pm x$
```

**Bisectors of a general pair** meeting at $(\alpha, \beta)$: shift the origin to $(\alpha, \beta)$:

$$h\left[(x - \alpha)^2 - (y - \beta)^2\right] = (a - b)(x - \alpha)(y - \beta).$$

:::caution
The bisector equation has $a - b$ next to $xy$ and $h$ next to $x^2 - y^2$. Swapping them gives a pair that is still perpendicular, so the "coefficient sum = 0" check will not catch the error. Test with $a = b$: the bisectors must be $y = \pm x$.
:::

## The general equation as a pair of lines {#general-condition}

The general second-degree equation is

$$S \equiv ax^2 + 2hxy + by^2 + 2gx + 2fy + c = 0.$$

**Theorem.** $S = 0$ represents a pair of straight lines (real or imaginary, possibly parallel or coincident) if and only if

$$\Delta = \begin{vmatrix} a & h & g\\ h & b & f\\ g & f & c \end{vmatrix} = abc + 2fgh - af^2 - bg^2 - ch^2 = 0.$$

For **real, intersecting** lines we also need $h^2 > ab$. If $h^2 = ab$, the lines are parallel or coincident; for $a \ne 0$ they are real exactly when $g^2 \ge ac$.

**Proof idea.** If $b \ne 0$, solve for $y$ as a quadratic. The two values of $y$ are linear in $x$ exactly when the discriminant, which is quadratic in $x$, is a perfect square. Its own discriminant vanishing is $\Delta = 0$. The determinant form is $\Delta = \det$ of the symmetric matrix of the quadratic form in $(x, y, 1)$.

**Example.** For which $\lambda$ is $\lambda x^2 - 10xy + 12y^2 + 5x - 16y - 3 = 0$ a pair of lines? Here $a = \lambda$, $h = -5$, $b = 12$, $g = \tfrac52$, $f = -8$, $c = -3$:

$$\Delta = -36\lambda + 200 - 64\lambda - 75 + 75 = 200 - 100\lambda = 0 \;\Rightarrow\; \lambda = 2.$$

**Factorising.** Treat $S$ as a quadratic in $x$ (or $y$), or match $(l_1x + m_1y + n_1)(l_2x + m_2y + n_2)$. The product of the $x, y$ parts must equal $ax^2 + 2hxy + by^2$. For example,

$$x^2 - 5xy + 4y^2 + x + 2y - 2 = (x - y - 1)(x - 4y + 2).$$

:::caution
$\Delta = 0$ alone does not guarantee **real** lines. For instance, $x^2 + y^2 = 0$ has $\Delta = 0$ but represents only the origin. Also, $h^2 = ab$ alone does not give parallel lines: $y^2 = 4x$ has $h^2 = ab = 0$, but it is a parabola.
:::

Classifying a general conic when $\Delta \ne 0$ (ellipse, parabola, hyperbola) belongs to *Transformation of Axes and General Conics*.

## Intersection point and parallel lines {#intersection}

**Point of intersection.** If $S = 0$ is a pair of intersecting lines, their common point $(\alpha, \beta)$ satisfies $\partial S/\partial x = 0$ and $\partial S/\partial y = 0$:

$$a\alpha + h\beta + g = 0, \qquad h\alpha + b\beta + f = 0,$$

$$(\alpha, \beta) = \left(\frac{hf - bg}{ab - h^2},\; \frac{gh - af}{ab - h^2}\right) \qquad (ab \ne h^2).$$

Shifting the origin to $(\alpha, \beta)$ removes the first-degree terms and leaves $aX^2 + 2hXY + bY^2 = 0$. So:
- the lines of $S = 0$ are **parallel** to the lines $ax^2 + 2hxy + by^2 = 0$, and
- the angle and bisector formulas carry over with $(x - \alpha, y - \beta)$ in place of $(x, y)$.

Example: for $2x^2 + 5xy + 3y^2 + 6x + 7y + 4 = 0$, solve $2x + \tfrac52 y + 3 = 0$ and $\tfrac52 x + 3y + \tfrac72 = 0$. This gives $(1, -2)$. Check: the pair is $(2x + 3y + 4)(x + y + 1)$.

**Parallel lines.** $S = 0$ is a pair of parallel lines when $\Delta = 0$ and $h^2 = ab$. Then also $bg^2 = af^2$ (equivalently $h/a = f/g$ when these are defined). The **distance** between them is

$$d = 2\sqrt{\frac{g^2 - ac}{a(a + b)}}.$$

Example: $9x^2 - 24xy + 16y^2 - 12x + 16y - 12 = 0$ is

$$(3x - 4y)^2 - 4(3x - 4y) - 12 = (3x - 4y - 6)(3x - 4y + 2) = 0.$$

The distance is $\dfrac{\lvert -6 - 2\rvert}{5} = \dfrac85$. The formula gives $2\sqrt{\tfrac{36 + 108}{9\cdot 25}} = 2\cdot\tfrac{12}{15} = \tfrac85$, the same value.

:::exam-tip
When the second-degree part is a perfect square $(px + qy)^2$, put $u = px + qy$. The equation becomes a quadratic in $u$, and the two roots give the two parallel lines at once.
:::

## Lines joining the origin to the intersections with a conic {#homogenisation}

Let the line $lx + my = n$ (with $n \ne 0$) meet the conic

$$ax^2 + 2hxy + by^2 + 2gx + 2fy + c = 0$$

at $P$ and $Q$. Write the line as $\dfrac{lx + my}{n} = 1$ and use it to make every term of the conic degree 2:

$$ax^2 + 2hxy + by^2 + 2(gx + fy)\frac{lx + my}{n} + c\left(\frac{lx + my}{n}\right)^2 = 0.$$

This is homogeneous, so it is a pair of lines through $O$. It is satisfied by $P$ and $Q$ (where both the conic and the line hold). So it is the joint equation of $OP$ and $OQ$. This step is called **homogenisation**.

**Circle example.** For $x^2 + y^2 = 4$ and $x + y = 1$:

$$x^2 + y^2 = 4(x + y)^2 \;\Rightarrow\; 3x^2 + 8xy + 3y^2 = 0.$$

**Right angle at the origin.** $\angle POQ = 90^\circ$ exactly when the $x^2$ and $y^2$ coefficients of the homogenised equation add to $0$.
- Chord $lx + my = n$ of $x^2 + y^2 = r^2$: $n^2(x^2 + y^2) = r^2(lx + my)^2$, so the condition is $2n^2 = r^2(l^2 + m^2)$. For $y = mx + c$, it is $2c^2 = r^2(1 + m^2)$.
- Chord $x = k$ of $y^2 = 4ax$: $ky^2 = 4ax\cdot x$, so $4ax^2 - ky^2 = 0$, and the condition is $k = 4a$.

Example: $3x^2 + 5xy - 3y^2 + 2x + 3y = 0$ and $3x - 2y = 1$ give

$$3x^2 + 5xy - 3y^2 + (2x + 3y)(3x - 2y) = 9x^2 + 10xy - 9y^2 = 0.$$

The coefficients satisfy $9 - 9 = 0$, so $OP \perp OQ$.

:::caution
Multiply **each** term by the right power of $\dfrac{lx + my}{n}$: degree-1 terms once, the constant twice. The degree-2 terms stay as they are. A common slip is to leave the constant $c$ multiplied only once.
:::

**Coincident case.** $OP$ and $OQ$ coincide exactly when $P = Q$, that is, when the line touches the conic. For the circle, this is $n^2 = r^2(l^2 + m^2)$. Tangents, chords of contact and polars belong to *Tangents, Poles and Polars*.

## Quick checks and traps {#exam-tips}

- **Read off $h$ correctly:** the $xy$ coefficient is $2h$.
- **Perpendicular:** $a + b = 0$. **Coincident:** $h^2 = ab$. **Real and distinct:** $h^2 > ab$.
- **Angle:** $\tan\theta = \dfrac{2\sqrt{h^2 - ab}}{\lvert a + b\rvert}$. It is the same for the general pair, since the linear terms do not affect it.
- **Bisectors:** $h(x^2 - y^2) = (a - b)xy$. They are always perpendicular. Check with $a = b \Rightarrow y = \pm x$.
- **Perpendicular pair through $O$:** $bx^2 - 2hxy + ay^2 = 0$.
- **One slope $k$ times the other:** $4kh^2 = (1 + k)^2ab$. For $k = 2$, this gives $8h^2 = 9ab$.
- **Pair of lines test:** $\Delta = abc + 2fgh - af^2 - bg^2 - ch^2 = 0$. Remember $f$ goes with $a$ and $g$ with $b$ ($af^2$, $bg^2$).
- **Intersection point:** solve $S_x = 0$, $S_y = 0$.
- **Equilateral-triangle check:** $x^2 - 4xy + y^2 = 0$ makes $60^\circ$ and is symmetric about $y = x$. So with $x + y = 3$ it forms an equilateral triangle of altitude $\tfrac{3}{\sqrt2}$ and area $\tfrac{3\sqrt3}{2}$.
- **Homogenisation:** a right angle at $O$ means the $x^2$ and $y^2$ coefficients add to $0$.
