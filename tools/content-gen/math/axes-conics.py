import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from qlib import Topic, eq

T = Topic("math.geometry.axes-conics")
GEN = r"$ax^2 + 2hxy + by^2 + 2gx + 2fy + c = 0$"

# 1
T.single(1, ["translation"],
    r"The origin is shifted to $(2, -3)$ without rotating the axes. The point whose old coordinates are $(5, 1)$ has new coordinates",
    [r"$(3, 4)$", r"$(7, -2)$", r"$(3, -2)$", r"$(-3, -4)$"],
    r"""Under translation to $(\alpha, \beta)$: $X = x - \alpha$, $Y = y - \beta$. So
$$X = 5 - 2 = 3, \qquad Y = 1 - (-3) = 4.$$

$(7, -2)$ adds the shift instead of subtracting it. $(3, -2)$ subtracts $3$ from $y$ instead of $-3$. $(-3, -4)$ has both signs reversed (old − new swapped). Check: $(3, 4) + (2, -3) = (5, 1)$.""")

# 2
T.single(1, ["translation"],
    r"When the origin is shifted to $(1, 2)$, the equation $x^2 + y^2 - 2x - 4y + 1 = 0$ becomes",
    [r"$X^2 + Y^2 = 4$", r"$X^2 + Y^2 = 6$", r"$X^2 + Y^2 = 1$", r"$X^2 + Y^2 + 2X + 4Y = 4$"],
    r"""Put $x = X + 1$, $y = Y + 2$:
$$(X + 1)^2 + (Y + 2)^2 - 2(X + 1) - 4(Y + 2) + 1 = X^2 + Y^2 - 4.$$
So $X^2 + Y^2 = 4$: the circle of radius $2$ about the new origin.

$X^2 + Y^2 = 6$ adds $g^2 + f^2 = 5$ to $c = 1$ instead of subtracting $c$. $X^2 + Y^2 = 1$ takes the constant $c$ as the radius squared. Linear terms vanish because the new origin is the centre. Check: the radius $\sqrt{1 + 4 - 1} = 2$ does not change.""")

# 3
T.assertion_reason(1, ["translation", "invariants"],
    r"Under a translation of axes, the coefficient of $xy$ in a second-degree equation in general changes.",
    r"Under $x = X + \alpha$, $y = Y + \beta$, the second-degree terms $ax^2 + 2hxy + by^2$ keep their coefficients $a, h, b$.",
    3,
    r"""Substitute: $a(X + \alpha)^2 + 2h(X + \alpha)(Y + \beta) + b(Y + \beta)^2$. The only second-degree terms are
$$aX^2 + 2hXY + bY^2;$$
everything else is linear or constant. So the $xy$-coefficient **never** changes under translation: **A is false**, **R is true**.

Removing the $xy$-term needs a **rotation**; translation only removes linear terms (by moving to the centre).""")

# 4
T.single(1, ["rotation"],
    r"The axes are rotated anticlockwise through $45^\circ$ about the origin. The point with old coordinates $(2, 0)$ has new coordinates",
    [r"$(\sqrt2, -\sqrt2)$", r"$(\sqrt2, \sqrt2)$", r"$(-\sqrt2, \sqrt2)$", r"$(1, -1)$"],
    r"""$$X = x\cos\theta + y\sin\theta = 2\cdot\tfrac{1}{\sqrt2} = \sqrt2,\qquad Y = -x\sin\theta + y\cos\theta = -\sqrt2.$$

$(\sqrt2, \sqrt2)$ rotates the **point** anticlockwise instead of the axes (that is the same as rotating the axes clockwise). $(1, -1)$ forgets the factor $2$. Check: the distance from the origin stays $2$, and $\sqrt{2 + 2} = 2$.""")

# 5
T.single(2, ["rotation"],
    r"On rotating the axes anticlockwise through $45^\circ$, the curve $x^2 - y^2 = 2$ becomes",
    [r"$XY = -1$", r"$XY = 1$", r"$2XY = 1$", r"$X^2 - Y^2 = 2$"],
    r"""With $\theta = 45^\circ$: $x = \frac{X - Y}{\sqrt2}$, $y = \frac{X + Y}{\sqrt2}$, so
$$x^2 - y^2 = \frac{(X - Y)^2 - (X + Y)^2}{2} = -2XY.$$
Hence $-2XY = 2$, i.e. $XY = -1$.

$XY = 1$ is what a **clockwise** rotation of $45^\circ$ gives. $X^2 - Y^2 = 2$ would mean the curve is symmetric under a $45^\circ$ rotation, which it is not. Check with a point: $(\sqrt2, 0)$ has new coordinates $(1, -1)$, and $1\cdot(-1) = -1$.""")

# 6
T.single(1, ["invariants"],
    r"The angle through which the axes must be rotated (anticlockwise, $0 < \theta < \frac{\pi}{2}$) to remove the $xy$-term from $3x^2 + 2\sqrt3\,xy + y^2 = 4$ is",
    [r"$\dfrac{\pi}{6}$", r"$\dfrac{\pi}{3}$", r"$\dfrac{\pi}{4}$", r"$\dfrac{\pi}{12}$"],
    r"""Here $a = 3$, $b = 1$, $2h = 2\sqrt3$, so $h = \sqrt3$ and
$$\tan 2\theta = \frac{2h}{a - b} = \frac{2\sqrt3}{2} = \sqrt3 \ \Rightarrow\ 2\theta = \frac{\pi}{3},\ \theta = \frac{\pi}{6}.$$

$\frac{\pi}{3}$ is $2\theta$, not $\theta$. $\frac{\pi}{4}$ is correct only when $a = b$. $\frac{\pi}{12}$ halves the correct angle a second time. Check: with $\theta = \frac{\pi}{6}$, $h' = (b - a)\sin\theta\cos\theta + h\cos2\theta = -\frac{\sqrt3}{2} + \frac{\sqrt3}{2} = 0$.""")

# 7
T.single(2, ["invariants"],
    r"By a rotation of axes through $45^\circ$, the equation $x^2 + 4xy + y^2 = 1$ becomes",
    [r"$3X^2 - Y^2 = 1$", r"$3X^2 + Y^2 = 1$", r"$5X^2 - 3Y^2 = 1$", r"$4X^2 - 2Y^2 = 1$"],
    r"""$a = b = 1$, $h = 2$. With $\theta = 45^\circ$:
$$a' = \frac{a + b}{2} + h\sin 90^\circ = 1 + 2 = 3, \qquad b' = (a + b) - a' = -1.$$
So $3X^2 - Y^2 = 1$, a hyperbola.

Invariant check: $a' + b' = 2 = a + b$ and $a'b' = -3 = ab - h^2 = 1 - 4$. $3X^2 + Y^2$ fails the product. $5X^2 - 3Y^2$ uses $h = 4$ (the unhalved coefficient). $4X^2 - 2Y^2$ has the right sum but product $-8$.""")

# 8
T.single(3, ["invariants", "rotation"],
    r"When the axes are rotated anticlockwise through $30^\circ$, the equation $7x^2 - 6\sqrt3\,xy + 13y^2 = 16$ becomes",
    [r"$\dfrac{X^2}{4} + Y^2 = 1$", r"$X^2 + \dfrac{Y^2}{4} = 1$", r"$\dfrac{X^2}{4} - Y^2 = 1$", r"$\dfrac{X^2}{16} + \dfrac{Y^2}{4} = 1$"],
    r"""$a = 7$, $b = 13$, $h = -3\sqrt3$. With $\cos^2 30^\circ = \frac34$, $\sin 30^\circ\cos 30^\circ = \frac{\sqrt3}{4}$, $\sin^2 30^\circ = \frac14$:
$$a' = 7\cdot\tfrac34 + 2(-3\sqrt3)\tfrac{\sqrt3}{4} + 13\cdot\tfrac14 = \tfrac{21 - 18 + 13}{4} = 4,$$
$$b' = (a + b) - a' = 16, \qquad h' = (b - a)\tfrac{\sqrt3}{4} + h\cos 60^\circ = \tfrac{3\sqrt3}{2} - \tfrac{3\sqrt3}{2} = 0.$$
So $4X^2 + 16Y^2 = 16$, i.e. $\frac{X^2}{4} + Y^2 = 1$.

$X^2 + \frac{Y^2}{4} = 1$ has the eigenvalues in the wrong order (that is the result of rotating through $120^\circ$). Check: $4\cdot16 = 64 = 91 - 27 = ab - h^2$.""")

# 9
T.single(3, ["invariants"],
    r"Under a rotation of axes, $x^2 + 6xy + y^2$ becomes $a'X^2 + 2h'XY + b'Y^2$ with $a' = 2$. Then",
    [r"$b' = 0,\ \lvert h'\rvert = 2\sqrt2$", r"$b' = 0,\ \lvert h'\rvert = \sqrt{10}$", r"$b' = 2,\ \lvert h'\rvert = 2\sqrt2$", r"$b' = -4,\ h' = 0$"],
    r"""Use the invariants $a + b$ and $ab - h^2$:
$$a' + b' = 1 + 1 = 2 \ \Rightarrow\ b' = 0,$$
$$a'b' - h'^2 = 1 - 9 = -8 \ \Rightarrow\ h'^2 = 8,\ \lvert h'\rvert = 2\sqrt2.$$

$\sqrt{10}$ uses $ab + h^2$. $b' = 2$ breaks $a' + b' = 2$. $h' = 0$ would need $a'$ to be an eigenvalue ($4$ or $-2$), and $2$ is not one.""")

# 10
T.statements(2, ["invariants"],
    r"For the equation " + GEN + r", consider:",
    [r"$a + b$ is unchanged by every rotation of axes about the origin.",
     r"$g^2 + f^2$ is unchanged by every rotation of axes about the origin.",
     r"$g^2 + f^2$ is unchanged by every translation of axes."],
    [r"1 and 2 only", r"1, 2 and 3", r"1 only", r"2 and 3 only"],
    r"""1. **True.** The matrix $\begin{pmatrix} a & h\\ h & b\end{pmatrix}$ becomes $P^TAP$ with $P$ orthogonal, so its trace $a + b$ is unchanged.
2. **True.** Under rotation, $g' = g\cos\theta + f\sin\theta$ and $f' = -g\sin\theta + f\cos\theta$: $(g, f)$ rotates like a vector, so $g'^2 + f'^2 = g^2 + f^2$.
3. **False.** Translation changes $g$ to $a\alpha + h\beta + g$. For example, $x^2 + y^2 = 1$ has $g = f = 0$; shifting the origin to $(1, 0)$ gives $X^2 + Y^2 + 2X = 0$ with $g' = 1$.

So 1 and 2 only.""")

# 11
T.assertion_reason(1, ["invariants"],
    r"Rotating the axes through $45^\circ$ removes the $xy$-term from $3x^2 + 4xy + 3y^2 = 5$.",
    r"The $xy$-term is removed by a rotation $\theta$ with $\tan 2\theta = \frac{2h}{a - b}$, and $\theta = 45^\circ$ when $a = b$.",
    0,
    r"""$h' = (b - a)\sin\theta\cos\theta + h\cos 2\theta$. When $a = b$, this is $h\cos 2\theta$, which vanishes at $2\theta = 90^\circ$. So R is true, and it gives A directly: here $a = b = 3$.

Result: $5X^2 + Y^2 = 5$ (eigenvalues $3 \pm 2$). Both true and **R explains A**.""")

# 12
T.single(2, ["centre"],
    r"The centre of the conic $3x^2 + 2xy + 3y^2 - 2x + 10y + 3 = 0$ is",
    [r"$(1, -2)$", r"$(-1, 2)$", r"$\left(\tfrac13, -\tfrac53\right)$", r"$(2, -1)$"],
    r"""Here $a = 3$, $h = 1$, $b = 3$, $g = -1$, $f = 5$. Solve
$$3x + y - 1 = 0, \qquad x + 3y + 5 = 0.$$
From the first, $y = 1 - 3x$; then $x + 3 - 9x + 5 = 0$, so $x = 1$, $y = -2$.

$\left(\tfrac13, -\tfrac53\right)$ ignores $h$ (solves $3x - 1 = 0$, $3y + 5 = 0$). $(-1, 2)$ has the sign of $g, f$ reversed. Check: $3(1) + (-2) - 1 = 0$ and $1 + 3(-2) + 5 = 0$.""")

# 13
T.single(2, ["centre", "translation"],
    r"When the origin is shifted to the centre of $x^2 - 3xy + y^2 + 10x - 10y + 21 = 0$, the equation becomes",
    [r"$X^2 - 3XY + Y^2 + 1 = 0$", r"$X^2 - 3XY + Y^2 + 21 = 0$", r"$X^2 - 3XY + Y^2 - 1 = 0$", r"$X^2 - 3XY + Y^2 + 41 = 0$"],
    r"""Centre: $x - \frac32 y + 5 = 0$ and $-\frac32 x + y - 5 = 0$. Adding gives $-\frac12(x + y) = 0$, so $y = -x$, and then $x = -2$, $y = 2$.

The quadratic part is unchanged; the new constant is
$$c' = gx_0 + fy_0 + c = 5(-2) + (-5)(2) + 21 = 1.$$

Check with $\Delta$: $\Delta = -\frac54$ and $ab - h^2 = 1 - \frac94 = -\frac54$, so $c' = \frac{\Delta}{ab - h^2} = 1$. $+21$ forgets to change the constant. $+41$ uses $-gx_0 - fy_0 + c$.""")

# 14
T.single(3, ["canonical-form", "centre"],
    r"The canonical form of $3x^2 + 2xy + 3y^2 - 2x + 10y + 3 = 0$ (with the major axis along the new $X$-axis) is",
    [r"$\dfrac{X^2}{4} + \dfrac{Y^2}{2} = 1$", r"$X^2 + 5Y^2 = 8$", r"$\dfrac{X^2}{4} - \dfrac{Y^2}{2} = 1$", r"$2X^2 + 4Y^2 + 3 = 0$"],
    r"""1. **Centre** $(1, -2)$ (solve $3x + y - 1 = 0$, $x + 3y + 5 = 0$).
2. **New constant** $c' = gx_0 + fy_0 + c = -1 - 10 + 3 = -8$. (Check: $\Delta = -64$, $ab - h^2 = 8$.)
3. **Eigenvalues** of $\begin{pmatrix} 3 & 1\\ 1 & 3\end{pmatrix}$: $2$ and $4$.

So $2X^2 + 4Y^2 = 8$, i.e.
$$\frac{X^2}{4} + \frac{Y^2}{2} = 1.$$

$X^2 + 5Y^2 = 8$ uses $h = 2$ (unhalved). $2X^2 + 4Y^2 + 3 = 0$ keeps the old constant (and would be imaginary). A hyperbola is impossible since $ab - h^2 > 0$.""")

# 15
T.single(2, ["canonical-form"],
    r"The eccentricity of the conic $5x^2 + 6xy + 5y^2 = 8$ is",
    [r"$\dfrac{\sqrt3}{2}$", r"$\dfrac12$", r"$\dfrac{1}{\sqrt2}$", r"$\dfrac{\sqrt5}{2}$"],
    r"""The eigenvalues of $\begin{pmatrix} 5 & 3\\ 3 & 5\end{pmatrix}$ are $8$ and $2$, so the curve is
$$8X^2 + 2Y^2 = 8 \iff X^2 + \frac{Y^2}{4} = 1.$$
Semi-axes $2$ and $1$:
$$e^2 = 1 - \frac{1}{4} = \frac34, \qquad e = \frac{\sqrt3}{2}.$$

Quick form: $e^2 = 1 - \frac{\lambda_{\text{small}}}{\lambda_{\text{large}}} = 1 - \frac28$. $\frac12$ is the ratio of the axes $b/a$. $\frac{\sqrt5}{2}$ uses the hyperbola formula $1 + \frac{b^2}{a^2}$.""")

# 16
T.single(3, ["canonical-form", "standard-conics"],
    r"The eccentricity of the conic $3x^2 + 10xy + 3y^2 + 8 = 0$ is",
    [r"$\dfrac{\sqrt5}{2}$", r"$\sqrt5$", r"$\dfrac{\sqrt3}{2}$", r"$2$"],
    r"""Eigenvalues of $\begin{pmatrix} 3 & 5\\ 5 & 3\end{pmatrix}$: $8$ and $-2$. The reduced equation is
$$8X^2 - 2Y^2 = -8 \iff \frac{Y^2}{4} - X^2 = 1.$$
The **transverse** axis is the $Y$-axis, with semi-axis $2$, and the conjugate semi-axis is $1$:
$$e^2 = 1 + \frac{1}{4} = \frac54, \qquad e = \frac{\sqrt5}{2}.$$

$\sqrt5$ takes the $X$-axis as transverse (it would be right for $3x^2 + 10xy + 3y^2 = 8$). $\frac{\sqrt3}{2}$ uses the ellipse formula. Check: $e^2 = 1 - \frac{\lambda_1}{\lambda_2}$ with $\lambda_1 = -2$ (same sign as $k = -8$), $\lambda_2 = 8$.""")

# 17
T.single(3, ["canonical-form"],
    r"The length of the latus rectum of the parabola $x^2 + 2xy + y^2 - 8x + 8y = 0$ is",
    [r"$4\sqrt2$", r"$8$", r"$2\sqrt2$", r"$4$"],
    r"""The equation is $(x + y)^2 = 8(x - y)$. The lines $x + y = 0$ and $x - y = 0$ are perpendicular, so they are the axis and the tangent at the vertex. Normalise: $Y = \frac{x + y}{\sqrt2}$, $X = \frac{x - y}{\sqrt2}$:
$$2Y^2 = 8\sqrt2\,X \iff Y^2 = 4\sqrt2\,X.$$
So the latus rectum is $4\sqrt2$.

Formula check: $a + b = 2$, $\Delta = -64$, and $\frac{2\sqrt{64}}{2^{3/2}} = \frac{16}{2\sqrt2} = 4\sqrt2$. $8$ reads the coefficient off without normalising the lines.""")

# 18
T.single(1, ["classification"],
    r"The equation $x^2 - 4xy + 4y^2 + 2x + y + 1 = 0$ represents",
    [r"a parabola", r"an ellipse", r"a hyperbola", r"a pair of straight lines"],
    r"""In the form """ + GEN + r""": $a = 1$, $h = -2$, $b = 4$, $g = 1$, $f = \frac12$, $c = 1$. Then $h^2 = ab = 4$, and
$$\Delta = abc + 2fgh - af^2 - bg^2 - ch^2 = 4 - 2 - \tfrac14 - 4 - 4 = -\tfrac{25}{4} \ne 0.$$
$h^2 = ab$ with $\Delta \ne 0$: a **parabola**.

It would be a pair of (parallel) lines only if $\Delta = 0$.""")

# 19
T.single(3, ["classification"],
    r"The equation $4x^2 + 4xy + y^2 - 12x - 6y + 5 = 0$ represents",
    [r"a pair of parallel straight lines", r"a parabola", r"a pair of intersecting straight lines", r"an ellipse"],
    r"""$a = 4$, $h = 2$, $b = 1$, so $h^2 = ab$. But
$$\Delta = 4\cdot1\cdot5 + 2(-3)(-6)(2) - 4\cdot 9 - 1\cdot36 - 5\cdot4 = 20 + 72 - 36 - 36 - 20 = 0.$$
Indeed, with $u = 2x + y$: $u^2 - 6u + 5 = 0$, so $u = 1$ or $5$. The lines $2x + y = 1$ and $2x + y = 5$ are **parallel**.

"Parabola" is the trap of looking only at $h^2 = ab$. Intersecting lines need $h^2 > ab$.""")

# 20
T.single(1, ["classification"],
    r"The equation $kx^2 + 4xy - 3y^2 + 2x + 3 = 0$ represents a rectangular hyperbola. Then $k =$",
    [r"$3$", r"$-3$", r"$2$", r"$4$"],
    r"""A non-degenerate conic is a rectangular hyperbola iff $a + b = 0$: $k - 3 = 0$, so $k = 3$.

Non-degeneracy check: with $a = 3$, $h = 2$, $b = -3$, $g = 1$, $f = 0$, $c = 3$,
$$\Delta = -27 + 0 - 0 - (-3)(1) - 3(4) = -36 \ne 0.$$
$k = -3$ makes $a = b$ (the circle-type condition, but $h \ne 0$). $k = 4$ uses $2h$ in place of $-b$.""")

# 21
T.statements(3, ["classification"],
    r"For the equation " + GEN + r" with $\Delta \ne 0$, consider:",
    [r"If $h^2 < ab$, the equation always has real points, so it is a real ellipse.",
     r"If $a = b \ne 0$ and $h = 0$, it is a circle (real or imaginary).",
     r"If $a + b = 0$, it is a rectangular hyperbola."],
    [r"2 and 3 only", r"1, 2 and 3", r"1 and 3 only", r"3 only"],
    r"""1. **False.** $x^2 + y^2 + 1 = 0$ has $h^2 < ab$ and $\Delta = 1 \ne 0$ but no real points. A real ellipse needs also $(a + b)\Delta < 0$.
2. **True.** $a(x^2 + y^2) + 2gx + 2fy + c = 0$ is a circle with radius squared $\frac{g^2 + f^2 - ac}{a^2}$. Here $\Delta = -a(g^2 + f^2 - ac)$, so $\Delta \ne 0$ rules out the point circle, leaving real or imaginary.
3. **True.** $a + b = 0$ gives $ab - h^2 = -a^2 - h^2 < 0$ (a hyperbola), and the asymptote directions $ax^2 + 2hxy - ay^2 = 0$ are perpendicular.

So 2 and 3 only.""")

# 22
T.match(2, ["classification"],
    r"Match each equation with the curve it represents.",
    [r"A. $x^2 + 4xy + 4y^2 + 2x - 3 = 0$", r"B. $x^2 - y^2 + 2x + 3 = 0$",
     r"C. $2x^2 + xy + y^2 = 4$", r"D. $x^2 - 5xy + 6y^2 = 0$"],
    [r"1. an ellipse", r"2. a pair of intersecting straight lines", r"3. a parabola", r"4. a rectangular hyperbola"],
    [r"A-3, B-4, C-1, D-2", r"A-1, B-4, C-3, D-2", r"A-3, B-2, C-1, D-4", r"A-4, B-3, C-1, D-2"],
    r"""- **A:** $h^2 = 4 = ab$, and $\Delta = 1\cdot4\cdot(-3) - 4\cdot1 - (-3)\cdot4 = -4 \ne 0$: parabola (3).
- **B:** $a + b = 0$; $(x + 1)^2 - y^2 = -2$ with $\Delta = -2 \ne 0$: rectangular hyperbola (4).
- **C:** $h^2 = \frac14 < ab = 2$, and $(a + b)\Delta < 0$ ($\Delta = -7$): real ellipse (1).
- **D:** $\Delta = 0$ and $x^2 - 5xy + 6y^2 = (x - 2y)(x - 3y)$: two lines through the origin (2).

So A-3, B-4, C-1, D-2.""")

# 23
T.assertion_reason(2, ["classification", "invariants"],
    r"The equation $x^2 + y^2 + 2x + 4y + 6 = 0$ has no real points.",
    r"Under a rotation of axes about the origin, the constant term $c$ of a second-degree equation is unchanged.",
    1,
    r"""**A:** $(x + 1)^2 + (y + 2)^2 = 5 - 6 = -1 < 0$: no real points (an imaginary circle). True.

**R:** rotation substitutes linear expressions in $X, Y$ with no constant terms, so $c$ stays. True.

But R says nothing about why this circle is imaginary; that follows from $g^2 + f^2 - c < 0$. Both true, **R does not explain A**.""")

# 24
T.assertion_reason(2, ["classification", "canonical-form"],
    r"The equation $x^2 + xy + y^2 = 3$ represents an ellipse.",
    r"Every second-degree equation with $h^2 < ab$ and $\Delta \ne 0$ represents a real ellipse.",
    2,
    r"""**A:** $h = \frac12$, $h^2 = \frac14 < ab = 1$. The eigenvalues are $\frac12$ and $\frac32$, so the curve is $\frac12X^2 + \frac32Y^2 = 3$, a real ellipse. True.

**R:** false. $x^2 + y^2 + 1 = 0$ satisfies $h^2 < ab$ and $\Delta = 1 \ne 0$ but has no real points. The extra condition is $(a + b)\Delta < 0$ (here $\Delta = -\frac94$, $a + b = 2$).

So **A is true, R is false**.""")

# 25
T.single(2, ["standard-conics"],
    r"The length of the latus rectum of the ellipse $9x^2 + 16y^2 = 144$ is",
    [r"$\dfrac92$", r"$\dfrac{32}{3}$", r"$\dfrac94$", r"$9$"],
    r"""$\frac{x^2}{16} + \frac{y^2}{9} = 1$, so $a = 4$, $b = 3$ and
$$\text{latus rectum} = \frac{2b^2}{a} = \frac{18}{4} = \frac92.$$

$\frac{32}{3} = \frac{2a^2}{b}$ swaps the roles of $a$ and $b$. $\frac94 = \frac{b^2}{a}$ is the semi-latus rectum. $9 = b^2$ is not a length of any chord here.""")

# 26
T.single(2, ["standard-conics"],
    r"The focus of the parabola $y^2 - 4y - 8x + 28 = 0$ is",
    [r"$(5, 2)$", r"$(1, 2)$", r"$(3, 4)$", r"$(11, 2)$"],
    r"""Complete the square: $(y - 2)^2 = 8x - 24 = 8(x - 3)$. So the vertex is $(3, 2)$ and $4p = 8$, $p = 2$:
$$\text{focus} = (3 + 2,\ 2) = (5, 2), \qquad \text{directrix } x = 1.$$

$(1, 2)$ is on the directrix. $(3, 4)$ moves along the wrong axis. $(11, 2)$ adds $4p$ instead of $p$.""")

# 27
T.single(2, ["standard-conics"],
    r"The distance between the directrices of the hyperbola $\dfrac{x^2}{9} - \dfrac{y^2}{16} = 1$ is",
    [r"$\dfrac{18}{5}$", r"$10$", r"$\dfrac{32}{3}$", r"$\dfrac95$"],
    r"""$a = 3$, $b = 4$, $e^2 = 1 + \frac{16}{9} = \frac{25}{9}$, $e = \frac53$. The directrices are $x = \pm\frac{a}{e} = \pm\frac95$, so the distance is
$$\frac{2a}{e} = \frac{18}{5}.$$

$10 = 2ae$ is the distance between the foci. $\frac{32}{3} = \frac{2b^2}{a}$ is the latus rectum. $\frac95$ is half the answer.""")

# 28
T.single(3, ["standard-conics", "rotation"],
    r"The foci of the rectangular hyperbola $xy = 8$ are",
    [r"$(4, 4)$ and $(-4, -4)$", r"$(2\sqrt2, 2\sqrt2)$ and $(-2\sqrt2, -2\sqrt2)$",
     r"$(4\sqrt2, 0)$ and $(-4\sqrt2, 0)$", r"$(8, 8)$ and $(-8, -8)$"],
    r"""Rotate through $45^\circ$: $xy = \frac{X^2 - Y^2}{2}$, so $X^2 - Y^2 = 16$: $a = b = 4$, $e = \sqrt2$, $ae = 4\sqrt2$. The foci are on the $X$-axis (the line $y = x$) at distance $4\sqrt2$ from the origin:
$$(4, 4), \ (-4, -4).$$

General rule: for $xy = c^2$ the foci are $\pm(\sqrt2c, \sqrt2c)$; here $c = 2\sqrt2$. $\pm(2\sqrt2, 2\sqrt2)$ are the **vertices** $\pm(c, c)$. $(\pm4\sqrt2, 0)$ are the coordinates in the rotated frame, not converted back.""")

# 29
T.match(2, ["standard-conics"],
    r"For the ellipse $\dfrac{x^2}{25} + \dfrac{y^2}{16} = 1$, match each quantity with its value.",
    [r"A. eccentricity", r"B. length of latus rectum", r"C. distance between the foci", r"D. distance between the directrices"],
    [r"1. $6$", r"2. $\frac35$", r"3. $\frac{50}{3}$", r"4. $\frac{32}{5}$"],
    [r"A-2, B-4, C-1, D-3", r"A-2, B-3, C-1, D-4", r"A-2, B-4, C-3, D-1", r"A-1, B-4, C-2, D-3"],
    r"""$a = 5$, $b = 4$, $e^2 = 1 - \frac{16}{25} = \frac{9}{25}$, $e = \frac35$.
- **A:** $e = \frac35$ (2).
- **B:** $\frac{2b^2}{a} = \frac{32}{5}$ (4).
- **C:** $2ae = 6$ (1).
- **D:** $\frac{2a}{e} = \frac{50}{3}$ (3).

The second option swaps B and D. Check: the directrices lie outside the ellipse, so their distance must exceed $2a = 10$.""")

# 30
T.assertion_reason(2, ["standard-conics", "classification"],
    r"The eccentricity of every rectangular hyperbola is $\sqrt2$.",
    r"A rectangular hyperbola has perpendicular asymptotes, so in its standard form $a = b$ and $e^2 = 1 + \frac{b^2}{a^2} = 2$.",
    0,
    r"""The asymptotes of $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$ are $y = \pm\frac{b}{a}x$; they are perpendicular iff $\frac{b^2}{a^2} = 1$. Then $e^2 = 2$.

Every rectangular hyperbola, however placed (for example $xy = c^2$ or $x^2 - y^2 + 2x + 3 = 0$), reduces by a rigid motion to this form, and rigid motions keep $e$. Both true; **R explains A**.""")


def check():
    import sympy as sp
    x, y, X, Y, k, t = sp.symbols("x y X Y k t", real=True)
    S, R = sp.sqrt, sp.Rational

    def coefs(E):
        P = sp.Poly(sp.expand(E), x, y)
        m = P.coeff_monomial
        return m(x**2), m(x*y) / 2, m(y**2), m(x) / 2, m(y) / 2, m(1)

    def Delta(E):
        a, h, b, g, f, c = coefs(E)
        return sp.Matrix([[a, h, g], [h, b, f], [g, f, c]]).det()

    def rot(E, th):
        return sp.expand(E.subs({x: X*sp.cos(th) - Y*sp.sin(th), y: X*sp.sin(th) + Y*sp.cos(th)}, simultaneous=True))

    def shift(E, al, be):
        return sp.expand(E.subs({x: X + al, y: Y + be}, simultaneous=True))

    def centre(E):
        a, h, b, g, f, c = coefs(E)
        s = sp.solve([a*x + h*y + g, h*x + b*y + f], [x, y], dict=True)[0]
        return s[x], s[y]

    def classify(E):
        a, h, b, g, f, c = coefs(E)
        D, C = Delta(E), a*b - h**2
        if D == 0:
            return "lines-int" if C < 0 else ("point" if C > 0 else "lines-par")
        if C == 0:
            return "parabola"
        if C < 0:
            return "rect-hyperbola" if a + b == 0 else "hyperbola"
        return "ellipse" if (a + b)*D < 0 else "imag-ellipse"

    def ecc_central(E):
        """eccentricity of a non-degenerate central conic from eigenvalues."""
        a, h, b, g, f, c = coefs(E)
        kk = -Delta(E) / (a*b - h**2)
        l = list(sp.Matrix([[a, h], [h, b]]).eigenvals(multiple=True))
        if l[0]*l[1] > 0:
            l1, l2 = sorted(l, key=abs)
        else:
            l1 = [v for v in l if sp.sign(v) == sp.sign(kk)][0]
            l2 = [v for v in l if v != l1][0]
        return sp.sqrt(1 - l1/l2)

    # q1
    eq(5 - 2, 3, "q1x"); eq(1 - (-3), 4, "q1y")
    # q2
    eq(shift(x**2 + y**2 - 2*x - 4*y + 1, 1, 2), X**2 + Y**2 - 4, "q2")
    # q3: translation keeps quadratic part
    a_, h_, b_, g_, f_, c_, al, be = sp.symbols("a h b g f c alpha beta")
    G = a_*x**2 + 2*h_*x*y + b_*y**2 + 2*g_*x + 2*f_*y + c_
    Gs = sp.Poly(shift(G, al, be), X, Y)
    eq(Gs.coeff_monomial(X*Y), 2*h_, "q3")
    eq(Gs.coeff_monomial(X**2), a_, "q3a")
    # q4
    th = sp.pi/4
    eq(2*sp.cos(th) + 0*sp.sin(th), S(2), "q4X"); eq(-2*sp.sin(th), -S(2), "q4Y")
    # notes rotation table
    eq(1*sp.cos(sp.pi/3) + S(3)*sp.sin(sp.pi/3), 2, "tbl"); eq(-sp.sin(sp.pi/3) + S(3)*sp.cos(sp.pi/3), 0, "tbl2")
    # q5
    eq(rot(x**2 - y**2, sp.pi/4), -2*X*Y, "q5")
    eq(rot(x**2 - y**2, -sp.pi/4), 2*X*Y, "q5 clockwise distractor")
    # q6
    E6 = 3*x**2 + 2*S(3)*x*y + y**2
    eq(sp.Poly(rot(E6, sp.pi/6), X, Y).coeff_monomial(X*Y), 0, "q6")
    for bad in (sp.pi/3, sp.pi/4, sp.pi/12):
        assert sp.simplify(sp.Poly(rot(E6, bad), X, Y).coeff_monomial(X*Y)) != 0
    # q7
    eq(rot(x**2 + 4*x*y + y**2, sp.pi/4), 3*X**2 - Y**2, "q7")
    # q8
    E8 = 7*x**2 - 6*S(3)*x*y + 13*y**2
    eq(rot(E8, sp.pi/6), 4*X**2 + 16*Y**2, "q8")
    eq(rot(E8, 2*sp.pi/3), 16*X**2 + 4*Y**2, "q8 distractor at 120")
    # q9: general rotation of x^2+6xy+y^2; find theta with a'=2
    P9 = sp.Poly(rot(x**2 + 6*x*y + y**2, t), X, Y)
    ap, hp, bp = P9.coeff_monomial(X**2), P9.coeff_monomial(X*Y)/2, P9.coeff_monomial(Y**2)
    eq(ap + bp, 2, "q9 trace"); eq(ap*bp - hp**2, -8, "q9 det")
    ts = sp.solve(sp.Eq(sp.simplify(ap), 2), t)
    assert ts
    eq(bp.subs(t, ts[0]), 0, "q9 b'"); eq((hp**2).subs(t, ts[0]), 8, "q9 h'")
    # q10
    P10 = sp.Poly(rot(G, t), X, Y)
    gp, fp = P10.coeff_monomial(X)/2, P10.coeff_monomial(Y)/2
    eq(gp**2 + fp**2, g_**2 + f_**2, "q10 st2")
    eq(P10.coeff_monomial(X**2) + P10.coeff_monomial(Y**2), a_ + b_, "q10 st1")
    eq(P10.coeff_monomial(1), c_, "c unchanged under rotation")
    eq(shift(x**2 + y**2 - 1, 1, 0), X**2 + Y**2 + 2*X, "q10 st3 counterexample")
    # q11
    E11 = 3*x**2 + 4*x*y + 3*y**2 - 5
    eq(rot(E11, sp.pi/4), 5*X**2 + Y**2 - 5, "q11")
    # q12
    E12 = 3*x**2 + 2*x*y + 3*y**2 - 2*x + 10*y + 3
    c12 = centre(E12); eq(c12[0], 1, "q12x"); eq(c12[1], -2, "q12y")
    # q13
    E13 = x**2 - 3*x*y + y**2 + 10*x - 10*y + 21
    c13 = centre(E13); eq(c13[0], -2, "q13x"); eq(c13[1], 2, "q13y")
    eq(shift(E13, *c13), X**2 - 3*X*Y + Y**2 + 1, "q13")
    a, h, b, g, f, c = coefs(E13)
    eq(Delta(E13) / (a*b - h**2), 1, "q13 Delta/C")
    # q14
    eq(shift(E12, 1, -2), 3*X**2 + 2*X*Y + 3*Y**2 - 8, "q14 shift")
    eq(Delta(E12), -64, "q14 Delta")
    eq(rot(3*x**2 + 2*x*y + 3*y**2 - 8, -sp.pi/4), 2*X**2 + 4*Y**2 - 8, "q14 rotate")
    # q15
    E15 = 5*x**2 + 6*x*y + 5*y**2 - 8
    eq(rot(E15, sp.pi/4), 8*X**2 + 2*Y**2 - 8, "q15 rot")
    eq(ecc_central(E15), S(3)/2, "q15")
    # q16
    E16 = 3*x**2 + 10*x*y + 3*y**2 + 8
    eq(rot(E16, sp.pi/4), 8*X**2 - 2*Y**2 + 8, "q16 rot")
    eq(ecc_central(E16), S(5)/2, "q16")
    eq(ecc_central(3*x**2 + 10*x*y + 3*y**2 - 8), S(5), "q16 distractor conic")
    # q17
    E17 = x**2 + 2*x*y + y**2 - 8*x + 8*y
    assert classify(E17) == "parabola"
    Xn, Yn = (x - y)/S(2), (x + y)/S(2)
    eq(sp.expand(Yn**2 - 4*S(2)*Xn), sp.expand(E17/2), "q17 canonical")
    a, h, b, g, f, c = coefs(E17)
    eq(2*sp.sqrt(-Delta(E17)) / (a + b)**R(3, 2), 4*S(2), "q17 formula")
    # notes parabola example + y^2 = 4x sanity
    En = 9*x**2 - 24*x*y + 16*y**2 - 18*x - 101*y + 19
    eq(sp.expand((3*x - 4*y + 7)**2 - 15*(4*x + 3*y + 2)), En, "notes parabola")
    a, h, b, g, f, c = coefs(En)
    eq(2*sp.sqrt(-Delta(En)) / (a + b)**R(3, 2), 3, "notes LR")
    eq(2*sp.sqrt(-Delta(y**2 - 4*x)) / 1, 4, "LR formula sanity")
    # notes centre example
    Ec = 11*x**2 + 4*x*y + 14*y**2 - 26*x - 32*y + 23
    eq(centre(Ec)[0], 1, "notes c"); eq(Delta(Ec), -900, "notes D")
    eq(ecc_central(Ec), 1/S(3), "notes e")
    eq(shift(2*x**2 + 3*y**2 - 8*x + 6*y + 5, 2, -1), 2*X**2 + 3*Y**2 - 6, "notes translation")
    # q18
    E18 = x**2 - 4*x*y + 4*y**2 + 2*x + y + 1
    eq(Delta(E18), -R(25, 4), "q18 D"); assert classify(E18) == "parabola"
    # q19
    E19 = 4*x**2 + 4*x*y + y**2 - 12*x - 6*y + 5
    eq(Delta(E19), 0, "q19 D"); assert classify(E19) == "lines-par"
    eq(sp.expand((2*x + y - 1)*(2*x + y - 5)), E19, "q19 factor")
    # q20
    E20 = k*x**2 + 4*x*y - 3*y**2 + 2*x + 3
    ks = sp.solve(coefs(E20)[0] + coefs(E20)[2], k); assert ks == [3]
    eq(Delta(E20.subs(k, 3)), -36, "q20 D"); assert classify(E20.subs(k, 3)) == "rect-hyperbola"
    # q21
    assert classify(x**2 + y**2 + 1) == "imag-ellipse"; eq(Delta(x**2 + y**2 + 1), 1, "q21 st1")
    a_c = sp.Symbol("a", nonzero=True)
    eq(Delta(a_c*x**2 + a_c*y**2 + 2*g_*x + 2*f_*y + c_), -a_c*(g_**2 + f_**2 - a_c*c_), "q21 st2")
    eq((a_*(-a_) - h_**2), -(a_**2 + h_**2), "q21 st3")
    # q22
    E22 = {"A": x**2 + 4*x*y + 4*y**2 + 2*x - 3, "B": x**2 - y**2 + 2*x + 3,
           "C": 2*x**2 + x*y + y**2 - 4, "D": x**2 - 5*x*y + 6*y**2}
    want = {"A": "parabola", "B": "rect-hyperbola", "C": "ellipse", "D": "lines-int"}
    for kk_, E in E22.items():
        assert classify(E) == want[kk_], kk_
    eq(Delta(E22["A"]), -4, "q22A"); eq(Delta(E22["B"]), -2, "q22B"); eq(Delta(E22["C"]), -7, "q22C")
    # q23
    E23 = x**2 + y**2 + 2*x + 4*y + 6
    eq(shift(E23, -1, -2), X**2 + Y**2 + 1, "q23"); assert classify(E23) == "imag-ellipse"
    # q24
    E24 = x**2 + x*y + y**2 - 3
    assert classify(E24) == "ellipse"; eq(Delta(E24), -R(9, 4), "q24 D")
    assert sorted(sp.Matrix([[1, R(1, 2)], [R(1, 2), 1]]).eigenvals(multiple=True)) == [R(1, 2), R(3, 2)]
    # q25
    E25 = 9*x**2 + 16*y**2 - 144
    eq(ecc_central(E25), S(7)/4, "notes e")
    eq(2*R(9)/4, R(9, 2), "q25")
    # q26
    E26 = y**2 - 4*y - 8*x + 28
    eq(sp.expand((y - 2)**2 - 8*(x - 3)), E26, "q26 form")
    p26 = 2; eq(3 + p26, 5, "q26 focus")
    # focus-directrix check: |PF|^2 = dist(P, x=1)^2 on the curve
    yy = sp.Symbol("yy"); xx = sp.solve(E26.subs(y, yy), x)[0]
    eq((xx - 5)**2 + (yy - 2)**2 - (xx - 1)**2, 0, "q26 focus-directrix")
    # q27
    e27 = sp.sqrt(1 + R(16, 9)); eq(e27, R(5, 3), "q27 e"); eq(2*3/e27, R(18, 5), "q27")
    # q28
    eq(rot(x*y - 8, sp.pi/4), (X**2 - Y**2)/2 - 8, "q28 rot")
    F = (4*S(2)*sp.cos(sp.pi/4), 4*S(2)*sp.sin(sp.pi/4)); eq(F[0], 4, "q28x"); eq(F[1], 4, "q28y")
    # focal property: |PF - PF'| = 2a = 8 at a point of xy = 8, e.g. (2, 4)
    PF = sp.sqrt((2 - 4)**2 + (4 - 4)**2); PF2 = sp.sqrt((2 + 4)**2 + (4 + 4)**2)
    eq(sp.Abs(PF - PF2), 8, "q28 focal")
    # q29
    e29 = sp.sqrt(1 - R(16, 25))
    eq(e29, R(3, 5), "q29A"); eq(R(2*16, 5), R(32, 5), "q29B"); eq(2*5*e29, 6, "q29C"); eq(2*5/e29, R(50, 3), "q29D")
    # q30
    eq(ecc_central(x**2 - y**2 + 2*x + 3), S(2), "q30a"); eq(ecc_central(x*y - 8), S(2), "q30b")


T.write(check)
