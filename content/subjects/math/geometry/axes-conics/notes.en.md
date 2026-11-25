# Transformation of Axes and General Conics

Throughout, the **general second-degree equation** is written

$$S \equiv ax^2 + 2hxy + by^2 + 2gx + 2fy + c = 0,$$

with $a, h, b$ not all zero, and

$$\Delta = \begin{vmatrix} a & h & g\\ h & b & f\\ g & f & c\end{vmatrix} = abc + 2fgh - af^2 - bg^2 - ch^2, \qquad C = ab - h^2.$$

## Translation of axes {#translation}

**Shift the origin** to $O'(\alpha, \beta)$, keeping the axes parallel to the old ones. A point with old coordinates $(x, y)$ and new coordinates $(X, Y)$ satisfies

$$x = X + \alpha, \qquad y = Y + \beta \qquad (\text{so } X = x - \alpha,\ Y = y - \beta).$$

So: **new = old − new origin**. With the origin moved to $(2, -3)$, the point $(5, 1)$ becomes $(3, 4)$.

**Effect on $S$.** Substitute and collect:

- the second-degree part $aX^2 + 2hXY + bY^2$ is **unchanged** ($a, h, b$ keep their values);
- the new linear coefficients are $g' = a\alpha + h\beta + g$ and $f' = h\alpha + b\beta + f$;
- the new constant is $c' = S(\alpha, \beta)$, the value of the left side at the new origin.

**Removing the first-degree terms.** Choose $(\alpha, \beta)$ with $g' = f' = 0$, that is, at the **centre** (see [Centre](#centre)).

Example: $2x^2 + 3y^2 - 8x + 6y + 5 = 0$. Complete squares: $2(x - 2)^2 + 3(y + 1)^2 = 6$. Shifting the origin to $(2, -1)$ gives

$$2X^2 + 3Y^2 = 6, \quad\text{i.e.}\quad \frac{X^2}{3} + \frac{Y^2}{2} = 1.$$

Check: $c' = S(2, -1) = 8 + 3 - 16 - 6 + 5 = -6$.

:::caution
The sign trap: shifting the origin to $(\alpha, \beta)$ means substituting $x = X + \alpha$, **not** $x = X - \alpha$. A circle $x^2 + y^2 - 2x - 4y + 1 = 0$ with the origin shifted to its centre $(1, 2)$ becomes $X^2 + Y^2 = 4$; the radius never changes under a change of axes.
:::

## Rotation of axes {#rotation}

**Rotate the axes** anticlockwise through $\theta$ about the origin. Then

$$x = X\cos\theta - Y\sin\theta, \qquad y = X\sin\theta + Y\cos\theta,$$

$$X = x\cos\theta + y\sin\theta, \qquad Y = -x\sin\theta + y\cos\theta.$$

The matrix $\begin{pmatrix}\cos\theta & -\sin\theta\\ \sin\theta & \cos\theta\end{pmatrix}$ is orthogonal with determinant $1$, so distances, angles and areas are preserved.

| Old point | $\theta$ | New coordinates |
|:---|:---:|:---|
| $(2, 0)$ | $45^\circ$ | $(\sqrt2, -\sqrt2)$ |
| $(1, \sqrt3)$ | $60^\circ$ | $(2, 0)$ |
| $(0, 1)$ | $90^\circ$ | $(1, 0)$ |

**Effect on the quadratic part.** $ax^2 + 2hxy + by^2$ becomes $a'X^2 + 2h'XY + b'Y^2$ with

$$a' = a\cos^2\theta + 2h\sin\theta\cos\theta + b\sin^2\theta,$$
$$b' = a\sin^2\theta - 2h\sin\theta\cos\theta + b\cos^2\theta,$$
$$h' = (b - a)\sin\theta\cos\theta + h\cos 2\theta.$$

A useful form: $a' = \tfrac{a + b}{2} + \tfrac{a - b}{2}\cos 2\theta + h\sin 2\theta$.

**The linear part** rotates like a vector: $g' = g\cos\theta + f\sin\theta$, $f' = -g\sin\theta + f\cos\theta$. The constant $c$ is unchanged.

**Combined change.** Translation to $(\alpha, \beta)$ followed by rotation through $\theta$:

$$x = \alpha + X\cos\theta - Y\sin\theta, \qquad y = \beta + X\sin\theta + Y\cos\theta.$$

Example: rotating through $45^\circ$, $x = \frac{X - Y}{\sqrt2}$, $y = \frac{X + Y}{\sqrt2}$, so

$$x^2 - y^2 = \frac{(X - Y)^2 - (X + Y)^2}{2} = -2XY.$$

Thus $x^2 - y^2 = 2$ becomes $XY = -1$: a rectangular hyperbola referred to its asymptotes.

:::exam-tip
Check any rotated equation by a point. $(\sqrt2, 0)$ lies on $x^2 - y^2 = 2$; its new coordinates for $\theta = 45^\circ$ are $(1, -1)$, and indeed $XY = -1$. The sign of the answer depends on the direction of rotation, so read "anticlockwise" carefully.
:::

## Invariants and removing the xy-term {#invariants}

:::keyfacts
- Under **any rotation**: $a' + b' = a + b$, $\;a'b' - h'^2 = ab - h^2$, $\;g'^2 + f'^2 = g^2 + f^2$, $\;c' = c$.
- Under **any translation**: $a, h, b$ are unchanged (so $a + b$ and $ab - h^2$ trivially are), but $g, f, c$ change.
- Under **both**, $\Delta$ is invariant.
:::

**Why.** The quadratic part has matrix $A = \begin{pmatrix} a & h\\ h & b\end{pmatrix}$, and rotation replaces $A$ by $P^TAP$ with $P$ orthogonal. So the trace $a + b$, the determinant $ab - h^2$ and the eigenvalues are unchanged. The $3\times3$ matrix of $\Delta$ is replaced by $T^T M T$ with $\det T = 1$, so $\Delta$ is unchanged under both moves.

**Removing the $xy$-term.** Set $h' = 0$:

$$\tan 2\theta = \frac{2h}{a - b}\quad (a \ne b), \qquad \theta = \frac{\pi}{4}\ \text{ if } a = b.$$

Then $a'$ and $b'$ are the **eigenvalues** $\lambda_1, \lambda_2$ of $A$, the roots of

$$\lambda^2 - (a + b)\lambda + (ab - h^2) = 0.$$

Which root is $a'$ depends on the angle chosen; find it from the formula for $a'$.

Example: $7x^2 - 6\sqrt3\,xy + 13y^2 = 16$. Here $\tan 2\theta = \frac{-6\sqrt3}{-6} = \sqrt3$, so $\theta = 30^\circ$. Then

$$a' = 7\cdot\tfrac34 - 6\sqrt3\cdot\tfrac{\sqrt3}{4} + 13\cdot\tfrac14 = 4,\qquad b' = (a + b) - a' = 16,$$

and the curve is $4X^2 + 16Y^2 = 16$, i.e. $\frac{X^2}{4} + Y^2 = 1$. Check: $4 \cdot 16 = 64 = 91 - 27 = ab - h^2$.

:::exam-tip
Invariants answer "find $b'$ and $h'$" questions without trigonometry. If $x^2 + 6xy + y^2$ becomes $a'X^2 + 2h'XY + b'Y^2$ with $a' = 2$, then $b' = 2 - 2 = 0$ and $h'^2 = a'b' - (1 - 9) = 8$.
:::

:::caution
$g^2 + f^2$ is invariant under rotation but **not** under translation; $a - b$ and $h$ are not invariant under rotation at all.
:::

## The centre of a conic {#centre}

A **centre** is a point that bisects every chord through it. For $S = 0$ the centre $(x_0, y_0)$ satisfies

$$\frac{\partial S}{\partial x} = 0,\ \frac{\partial S}{\partial y} = 0 \iff \begin{cases} ax_0 + hy_0 + g = 0,\\ hx_0 + by_0 + f = 0.\end{cases}$$

- If $C = ab - h^2 \ne 0$: a **unique centre** (ellipse, hyperbola, intersecting lines): the **central conics**.
- If $C = 0$: no centre (parabola) or a whole line of centres (parallel lines).

**Shifting to the centre** removes the linear terms, and the new constant is

$$c' = gx_0 + fy_0 + c = \frac{\Delta}{ab - h^2}.$$

(The first equality follows from Euler's theorem: $S(x_0, y_0) = x_0S_x/2 + y_0S_y/2 + gx_0 + fy_0 + c$, and $S_x = S_y = 0$ there.) So the equation becomes

$$aX^2 + 2hXY + bY^2 + \frac{\Delta}{C} = 0.$$

**Worked example.** $11x^2 + 4xy + 14y^2 - 26x - 32y + 23 = 0$.

1. Centre: $11x + 2y - 13 = 0$, $2x + 14y - 16 = 0$, giving $(1, 1)$.
2. $c' = gx_0 + fy_0 + c = -13 - 16 + 23 = -6$. (Check: $\Delta = -900$, $C = 150$, and $-900/150 = -6$.)
3. Shifted: $11X^2 + 4XY + 14Y^2 = 6$.

:::caution
Do not drop $h$ when solving for the centre. Using $ax + g = 0$ and $by + f = 0$ only works when $h = 0$.
:::

## Reduction to canonical form {#canonical-form}

### Central conics ($C \ne 0$)

Translate to the centre, then rotate to remove $XY$. With $\lambda_1, \lambda_2$ the eigenvalues of $A$:

$$\lambda_1 X^2 + \lambda_2 Y^2 + \frac{\Delta}{C} = 0.$$

Continuing the worked example: $\lambda^2 - 25\lambda + 150 = 0$ gives $10, 15$, so $10X^2 + 15Y^2 = 6$, an ellipse with $e^2 = 1 - \frac{10}{15} = \frac13$.

**Eccentricity from the eigenvalues.** Write the reduced equation as $\lambda_1X^2 + \lambda_2Y^2 = k$, labelling so that $\lambda_1$ belongs to the **major or transverse** axis (for a hyperbola: $\lambda_1$ has the same sign as $k$; for an ellipse: $|\lambda_1| < |\lambda_2|$). Then

$$e^2 = 1 - \frac{\lambda_1}{\lambda_2}.$$

Example: $5x^2 + 6xy + 5y^2 = 8$. The eigenvalues are $8$ (direction $y = x$) and $2$ (direction $y = -x$). Rotating through $45^\circ$: $8X^2 + 2Y^2 = 8$, i.e. $X^2 + \frac{Y^2}{4} = 1$, with $e = \frac{\sqrt3}{2}$ and the major axis along $y = -x$.

```plot
title: $5x^2 + 6xy + 5y^2 = 8$ with its principal axes $y = x$ and $y = -x$
x: -2.5, 2.5
y: -2.5, 2.5
equal: true
implicit: 5x^2 + 6xy + 5y^2 = 8 | ellipse
f: x | $X$-axis: $y = x$
f: -x | $Y$-axis: $y = -x$
```

### The parabola ($C = 0$, $\Delta \ne 0$)

The quadratic part is a perfect square $(\alpha x + \beta y)^2$. Write

$$(\alpha x + \beta y + \lambda)^2 = 2(\alpha\lambda - g)x + 2(\beta\lambda - f)y + \lambda^2 - c,$$

and choose $\lambda$ so that the two lines $\alpha x + \beta y + \lambda = 0$ (the **axis**) and the right side $= 0$ (the **tangent at the vertex**) are perpendicular. Normalising both lines gives $Y^2 = \ell X$ with latus rectum $\ell$. In general (with $a + b > 0$)

$$\text{latus rectum} = \frac{2\sqrt{-\Delta}}{(a + b)^{3/2}}.$$

Example: $9x^2 - 24xy + 16y^2 - 18x - 101y + 19 = 0$. The perpendicularity condition gives $\lambda = 7$:

$$(3x - 4y + 7)^2 = 15(4x + 3y + 2).$$

With $Y = \frac{3x - 4y + 7}{5}$ and $X = \frac{4x + 3y + 2}{5}$: $Y^2 = 3X$, so the latus rectum is $3$. Check: $\Delta = -\frac{140625}{4}$, and $\frac{2\cdot 375/2}{125} = 3$.

## Classification of conics {#classification}

For $S = 0$ with $C = ab - h^2$:

| | $\Delta \ne 0$ (non-degenerate) | $\Delta = 0$ (degenerate) |
|:---|:---|:---|
| $C > 0$ ($h^2 < ab$) | ellipse: real if $(a + b)\Delta < 0$, imaginary if $(a + b)\Delta > 0$ | a single real point (pair of imaginary lines) |
| $C = 0$ ($h^2 = ab$) | parabola | pair of parallel lines (distinct, coincident or imaginary) |
| $C < 0$ ($h^2 > ab$) | hyperbola | pair of intersecting real lines |

Special cases:

- **Circle:** $a = b \ne 0$ and $h = 0$ (real, a point, or imaginary according to $g^2 + f^2 - ac$).
- **Rectangular hyperbola:** $\Delta \ne 0$ and $a + b = 0$. Then $C = -a^2 - h^2 < 0$ automatically, and the asymptotes are perpendicular because the asymptote directions satisfy $ax^2 + 2hxy + by^2 = 0$ with $a + b = 0$.

**Examples.**

- $x^2 - 4xy + 4y^2 + 2x + y + 1 = 0$: $h^2 = ab = 4$ and $\Delta = -\frac{25}{4} \ne 0$, so a parabola.
- $4x^2 + 4xy + y^2 - 12x - 6y + 5 = 0$: $h^2 = ab$ but $\Delta = 0$. Indeed $(2x + y)^2 - 6(2x + y) + 5 = 0$ gives $2x + y = 1$ or $5$: two parallel lines.
- $x^2 - y^2 + 2x + 3 = 0$: $a + b = 0$, $\Delta = -2$: a rectangular hyperbola.

:::caution
$h^2 = ab$ alone does **not** mean parabola, and $h^2 < ab$ alone does not mean a real ellipse: always look at $\Delta$ (and, for an ellipse, its sign). $x^2 + y^2 + 1 = 0$ has $h^2 < ab$ and $\Delta = 1 \ne 0$, but no real points.
:::

The details of the degenerate case (the angle between the lines, their point of intersection, bisectors) belong to the topic Pair of Straight Lines; tangents and polars, and polar equations of conics, are separate topics.

## Standard properties of the conics {#standard-conics}

**Focus–directrix definition.** A conic is the locus of a point whose distance from a fixed point (focus) is $e$ times its distance from a fixed line (directrix): ellipse $e < 1$, parabola $e = 1$, hyperbola $e > 1$.

| | Ellipse $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$, $a > b$ | Hyperbola $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$ | Parabola $y^2 = 4ax$ |
|:---|:---|:---|:---|
| eccentricity | $e^2 = 1 - \frac{b^2}{a^2}$ | $e^2 = 1 + \frac{b^2}{a^2}$ | $e = 1$ |
| foci | $(\pm ae, 0)$ | $(\pm ae, 0)$ | $(a, 0)$ |
| directrices | $x = \pm\frac{a}{e}$ | $x = \pm\frac{a}{e}$ | $x = -a$ |
| latus rectum | $\frac{2b^2}{a}$ | $\frac{2b^2}{a}$ | $4a$ |
| focal distances | $SP + S'P = 2a$ | $\lvert SP - S'P\rvert = 2a$ | $SP = x + a$ |

More facts:

- Distance between foci $2ae$; between directrices $\frac{2a}{e}$.
- Hyperbola asymptotes $y = \pm\frac{b}{a}x$. The **conjugate hyperbola** $\frac{x^2}{a^2} - \frac{y^2}{b^2} = -1$ has eccentricity $e'$ with $\frac{1}{e^2} + \frac{1}{e'^2} = 1$.
- **Rectangular hyperbola** ($a = b$): $e = \sqrt2$. The form $xy = c^2$ is $X^2 - Y^2 = 2c^2$ rotated through $45^\circ$. Its vertices are $(c, c)$ and $(-c, -c)$, its foci $(\sqrt2c, \sqrt2c)$ and $(-\sqrt2c, -\sqrt2c)$, and its latus rectum $2\sqrt2\,c$.
- Shifted forms: $(y - k)^2 = 4p(x - h_0)$ has vertex $(h_0, k)$, focus $(h_0 + p, k)$ and directrix $x = h_0 - p$.

Example: $9x^2 + 16y^2 = 144$, i.e. $\frac{x^2}{16} + \frac{y^2}{9} = 1$. Then $e = \frac{\sqrt7}{4}$, the foci are $(\pm\sqrt7, 0)$, the directrices are $x = \pm\frac{16}{\sqrt7}$, and the latus rectum is $\frac{2\cdot 9}{4} = \frac92$.

:::exam-tip
For a hyperbola from a general equation, decide **which axis is transverse** before using $e^2 = 1 + \frac{b^2}{a^2}$. $8X^2 - 2Y^2 = -8$ is $\frac{Y^2}{4} - X^2 = 1$: the transverse semi-axis is $2$, so $e = \frac{\sqrt5}{2}$, not $\sqrt5$.
:::

## Quick checks and traps {#exam-tips}

- **New = old − origin** under translation; under rotation, $X = x\cos\theta + y\sin\theta$, $Y = -x\sin\theta + y\cos\theta$.
- **Translation keeps $a, h, b$.** Only the linear terms and the constant change; $c' = S(\alpha, \beta)$.
- **Rotation keeps $c$, $a + b$, $ab - h^2$, $g^2 + f^2$.** After removing $xy$, the coefficients are the eigenvalues: their sum is $a + b$ and their product $ab - h^2$.
- **Angle:** $\tan 2\theta = \frac{2h}{a - b}$; if $a = b$, $\theta = 45^\circ$.
- **Centre constant:** $c' = \frac{\Delta}{ab - h^2}$; it equals $gx_0 + fy_0 + c$.
- **Classify with both $C$ and $\Delta$.** $h^2 = ab$ with $\Delta = 0$ is a pair of parallel lines, not a parabola.
- **Rectangular hyperbola:** $a + b = 0$ (and $\Delta \ne 0$); $e = \sqrt2$; for $xy = c^2$ the foci are $\pm(\sqrt2c, \sqrt2c)$.
- **Parabola from the general equation:** latus rectum $\frac{2\sqrt{-\Delta}}{(a + b)^{3/2}}$; do not read it off a coefficient.
- **Eccentricity of a central conic:** $e^2 = 1 - \lambda_1/\lambda_2$ with $\lambda_1$ on the major/transverse axis.
