import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from qlib import Topic, eq

T = Topic("math.geometry.pair-of-lines")

# 1
T.single(1, ["angle"],
    r"The equation $6x^2 - 5xy - 6y^2 = 0$ represents",
    [r"a pair of perpendicular lines through the origin", r"a pair of coincident lines through the origin",
     r"a pair of lines through the origin inclined at $\dfrac{\pi}{4}$", r"only the origin (imaginary lines)"],
    r"""In the form $ax^2 + 2hxy + by^2 = 0$: $a = 6$, $b = -6$, so $a + b = 0$, and the lines are **perpendicular**. Also $h^2 - ab = \tfrac{25}{4} + 36 > 0$, so they are real.

Check by factorising: $$6x^2 - 5xy - 6y^2 = (3x + 2y)(2x - 3y),$$ with slopes $-\tfrac32$ and $\tfrac23$, whose product is $-1$.

Coincident lines would need $h^2 = ab$, which fails here since $ab < 0$.""")

# 2
T.single(1, ["angle"],
    r"The acute angle between the lines $x^2 - 4xy + y^2 = 0$ is",
    [r"$\dfrac{\pi}{3}$", r"$\dfrac{\pi}{6}$", r"$\dfrac{\pi}{4}$", r"$\tan^{-1}\sqrt{15}$"],
    r"""Here $a = b = 1$ and $2h = -4$, so $h = -2$:
$$\tan\theta = \frac{2\sqrt{h^2 - ab}}{\lvert a + b\rvert} = \frac{2\sqrt{4 - 1}}{2} = \sqrt3, \qquad \theta = \frac{\pi}{3}.$$

$\tan^{-1}\sqrt{15}$ comes from taking $h = -4$ (forgetting that the $xy$ coefficient is $2h$). $\frac{\pi}{6}$ inverts the tangent.""")

# 3
T.single(1, ["homogeneous"],
    r"The sum of the slopes of the lines $2x^2 + 5xy + 3y^2 = 0$ is",
    [r"$-\dfrac53$", r"$-\dfrac56$", r"$\dfrac53$", r"$\dfrac23$"],
    r"""For $ax^2 + 2hxy + by^2 = 0$ the slopes satisfy $bm^2 + 2hm + a = 0$, so
$$m_1 + m_2 = -\frac{2h}{b} = -\frac{5}{3}.$$

Check: $2x^2 + 5xy + 3y^2 = (2x + 3y)(x + y)$, with slopes $-\tfrac23$ and $-1$. $\tfrac23$ is the **product** $a/b$; $-\tfrac56$ uses $h$ in place of $2h$.""")

# 4
T.single(1, ["angle"],
    r"The lines $(\lambda - 3)x^2 + 4xy + (2\lambda + 1)y^2 = 0$ are perpendicular when $\lambda$ equals",
    [r"$\dfrac23$", r"$-\dfrac23$", r"$\dfrac32$", r"$2$"],
    r"""Perpendicular $\iff$ coefficient of $x^2$ + coefficient of $y^2 = 0$:
$$(\lambda - 3) + (2\lambda + 1) = 3\lambda - 2 = 0 \;\Rightarrow\; \lambda = \frac23.$$

When $a + b = 0$, $h^2 - ab = h^2 + a^2 > 0$, so the lines are automatically real. $-\tfrac23$ is a sign slip, and $\tfrac32$ inverts the answer.""")

# 5
T.single(1, ["angle", "homogeneous"],
    r"The equation $kx^2 + 12xy + 9y^2 = 0$ represents a pair of coincident lines when $k$ equals",
    [r"$4$", r"$16$", r"$-4$", r"$9$"],
    r"""Coincident $\iff h^2 = ab$. Here $h = 6$, $b = 9$:
$$36 = 9k \;\Rightarrow\; k = 4,$$
and then the equation is $(2x + 3y)^2 = 0$.

$k = 16$ comes from taking $h = 12$: then $144 = 9k$. That is the usual slip of forgetting that the $xy$ coefficient is $2h$.""")

# 6
T.single(2, ["bisectors"],
    r"The equation of the bisectors of the angles between the lines $2x^2 + 6xy + y^2 = 0$ is",
    [r"$3x^2 - xy - 3y^2 = 0$", r"$3x^2 + xy - 3y^2 = 0$", r"$x^2 - 3xy - y^2 = 0$", r"$6x^2 - xy - 6y^2 = 0$"],
    r"""The bisectors of $ax^2 + 2hxy + by^2 = 0$ are $h(x^2 - y^2) = (a - b)xy$. Here $a = 2$, $h = 3$, $b = 1$:
$$3(x^2 - y^2) = xy \;\Rightarrow\; 3x^2 - xy - 3y^2 = 0.$$

$x^2 - 3xy - y^2 = 0$ swaps the roles of $h$ and $a - b$. It is still a perpendicular pair, so the "coefficient sum $= 0$" check does not catch it. $6x^2 - xy - 6y^2$ uses $h = 6$.""")

# 7
T.single(2, ["general-condition"],
    r"Taking the general form $ax^2 + 2hxy + by^2 + 2gx + 2fy + c = 0$, the equation $\lambda x^2 - 10xy + 12y^2 + 5x - 16y - 3 = 0$ represents a pair of straight lines when $\lambda$ equals",
    [r"$2$", r"$-2$", r"$\dfrac12$", r"$4$"],
    r"""Here $a = \lambda$, $h = -5$, $b = 12$, $g = \tfrac52$, $f = -8$, $c = -3$. The condition is
$$\Delta = abc + 2fgh - af^2 - bg^2 - ch^2 = 0.$$
Substituting,
$$\Delta = -36\lambda + 2(-8)\left(\tfrac52\right)(-5) - 64\lambda - 12\cdot\tfrac{25}{4} + 3\cdot 25 = 200 - 100\lambda.$$
So $\lambda = 2$.

Check: $2x^2 - 10xy + 12y^2 + 5x - 16y - 3 = (x - 2y + 3)(2x - 6y - 1)$.""")

# 8
T.single(1, ["general-condition"],
    r"The equation $x^2 - 5xy + 4y^2 + x + 2y - 2 = 0$ represents the pair of lines",
    [r"$x - y - 1 = 0$ and $x - 4y + 2 = 0$", r"$x - y + 1 = 0$ and $x - 4y - 2 = 0$",
     r"$x - 4y - 1 = 0$ and $x - y + 2 = 0$", r"$x + y - 1 = 0$ and $x + 4y + 2 = 0$"],
    r"""The second-degree part factorises as $x^2 - 5xy + 4y^2 = (x - y)(x - 4y)$. So try $(x - y + p)(x - 4y + q)$. Matching the $x$ and $y$ terms:
$$p + q = 1, \qquad -4p - q = 2 \;\Rightarrow\; p = -1,\ q = 2.$$
The constant is $pq = -2$, as required. So the lines are $x - y - 1 = 0$ and $x - 4y + 2 = 0$.

The second option has the right $x, y$ parts but the wrong signs of the constants: its $x$ term is $-x$.""")

# 9
T.single(2, ["angle", "intersection"],
    r"The acute angle between the lines represented by $x^2 - 5xy + 4y^2 + x + 2y - 2 = 0$ is",
    [r"$\tan^{-1}\dfrac35$", r"$\tan^{-1}\dfrac{3}{10}$", r"$\tan^{-1}\dfrac53$", r"$\tan^{-1}\dfrac34$"],
    r"""The angle depends only on the second-degree terms. So use $a = 1$, $h = -\tfrac52$, $b = 4$:
$$\tan\theta = \frac{2\sqrt{\tfrac{25}{4} - 4}}{1 + 4} = \frac{2\cdot\tfrac32}{5} = \frac35.$$

Check with slopes $1$ and $\tfrac14$: $\dfrac{1 - \tfrac14}{1 + \tfrac14} = \dfrac35$. $\tfrac{3}{10}$ drops the factor $2$; $\tfrac53$ is the cotangent.""")

# 10
T.single(2, ["homogenisation"],
    r"The joint equation of the lines joining the origin to the points where $x + y = 1$ meets the circle $x^2 + y^2 = 4$ is",
    [r"$3x^2 + 8xy + 3y^2 = 0$", r"$3x^2 - 8xy + 3y^2 = 0$", r"$5x^2 + 8xy + 5y^2 = 0$", r"$3x^2 + 4xy + 3y^2 = 0$"],
    r"""Homogenise the circle with $(x + y) = 1$; the constant needs the factor twice:
$$x^2 + y^2 = 4(x + y)^2 \;\Rightarrow\; 3x^2 + 8xy + 3y^2 = 0.$$

$5x^2 + 8xy + 5y^2$ adds instead of subtracting. $3x^2 + 4xy + 3y^2$ forgets the $2$ in $(x + y)^2 = x^2 + 2xy + y^2$. Check: $h^2 - ab = 16 - 9 > 0$, so the lines are real, as they must be since the line cuts the circle.""")

# 11
T.single(2, ["homogenisation"],
    r"The line $y = 2x + c$ meets the circle $x^2 + y^2 = 10$ at $P$ and $Q$, and $\angle POQ = 90^\circ$, where $O$ is the origin. Then $c^2$ equals",
    [r"$25$", r"$50$", r"$10$", r"$5$"],
    r"""Homogenise with $\dfrac{y - 2x}{c} = 1$:
$$c^2(x^2 + y^2) = 10(y - 2x)^2.$$
$OP \perp OQ$ requires the $x^2$ and $y^2$ coefficients to add to $0$:
$$2c^2 - 10(4 + 1) = 0 \;\Rightarrow\; c^2 = 25.$$

This is the standard condition $2c^2 = r^2(1 + m^2)$. $c^2 = 50$ forgets the $2$ on the left.""")

# 12
T.single(2, ["homogenisation"],
    r"The chord $x = k$ ($k > 0$) of the parabola $y^2 = 4ax$ ($a > 0$) subtends a right angle at the vertex. Then $k$ equals",
    [r"$4a$", r"$2a$", r"$a$", r"$8a$"],
    r"""Homogenise $y^2 = 4ax$ with $\dfrac{x}{k} = 1$:
$$y^2 = 4ax\cdot\frac{x}{k} \;\Rightarrow\; 4ax^2 - ky^2 = 0.$$
A right angle at the vertex needs $4a - k = 0$, so $k = 4a$.

Direct check: the ends are $(4a, \pm 4a)$, and the vectors $(4a, 4a)$ and $(4a, -4a)$ have dot product $0$. $k = a$ gives the latus rectum, which subtends an obtuse angle.""")

# 13
T.single(3, ["intersection"],
    r"The distance between the parallel lines represented by $9x^2 - 24xy + 16y^2 - 12x + 16y - 12 = 0$ is",
    [r"$\dfrac85$", r"$\dfrac45$", r"$\dfrac65$", r"$\dfrac{8}{25}$"],
    r"""The second-degree part is $(3x - 4y)^2$. Put $u = 3x - 4y$:
$$u^2 - 4u - 12 = (u - 6)(u + 2) = 0.$$
So the lines are $3x - 4y - 6 = 0$ and $3x - 4y + 2 = 0$, and
$$d = \frac{\lvert -6 - 2\rvert}{\sqrt{9 + 16}} = \frac85.$$

The formula $2\sqrt{\dfrac{g^2 - ac}{a(a + b)}}$ with $g = -6$, $a = 9$, $b = 16$, $c = -12$ gives $2\cdot\tfrac{12}{15} = \tfrac85$, the same value. $\tfrac45$ forgets the factor $2$, and $\tfrac{8}{25}$ divides by $25$ instead of $5$.""")

# 14
T.single(2, ["homogeneous"],
    r"The pair of lines through the origin perpendicular to the lines $2x^2 - 5xy + 3y^2 = 0$ is",
    [r"$3x^2 + 5xy + 2y^2 = 0$", r"$3x^2 - 5xy + 2y^2 = 0$", r"$2x^2 + 5xy + 3y^2 = 0$", r"$3x^2 + 5xy - 2y^2 = 0$"],
    r"""The pair perpendicular to $ax^2 + 2hxy + by^2 = 0$ is $bx^2 - 2hxy + ay^2 = 0$:
$$3x^2 + 5xy + 2y^2 = 0.$$

Check: $2x^2 - 5xy + 3y^2 = (2x - 3y)(x - y)$ has slopes $\tfrac23, 1$. The answer $(3x + 2y)(x + y)$ has slopes $-\tfrac32, -1$, and each slope product is $-1$. $3x^2 - 5xy + 2y^2$ forgets to change the sign of $h$. $2x^2 + 5xy + 3y^2$ reflects the lines in the $x$-axis (slopes $-\tfrac23, -1$); the line of slope $-\tfrac23$ is perpendicular to neither given line.""")

# 15
T.single(3, ["bisectors", "intersection"],
    r"The pair of lines $x^2 - 5xy + 4y^2 + x + 2y - 2 = 0$ meets at $(2, 1)$. The equation of the bisectors of the angles between them is",
    [r"$5(x - 2)^2 - 6(x - 2)(y - 1) - 5(y - 1)^2 = 0$",
     r"$5(x - 2)^2 + 6(x - 2)(y - 1) - 5(y - 1)^2 = 0$",
     r"$5x^2 - 6xy - 5y^2 = 0$",
     r"$5(x - 1)^2 - 6(x - 1)(y - 2) - 5(y - 2)^2 = 0$"],
    r"""Shift the origin to $(2, 1)$: with $X = x - 2$, $Y = y - 1$ the pair is $X^2 - 5XY + 4Y^2 = 0$. Here $a = 1$, $h = -\tfrac52$, $b = 4$, and the bisectors are $h(X^2 - Y^2) = (a - b)XY$:
$$-\tfrac52(X^2 - Y^2) = -3XY \;\Rightarrow\; 5X^2 - 6XY - 5Y^2 = 0.$$

So the answer is $5(x - 2)^2 - 6(x - 2)(y - 1) - 5(y - 1)^2 = 0$. The option $5x^2 - 6xy - 5y^2 = 0$ gives the bisector **directions**, but through the origin. The option with $+6$ drops the sign of $h$. The last option centres the bisectors at $(1, 2)$.""")

# 16
T.single(3, ["homogeneous", "exam-tips"],
    r"The area of the triangle formed by the lines $x^2 - 4xy + y^2 = 0$ and the line $x + y = 3$ is",
    [r"$\dfrac{3\sqrt3}{2}$", r"$3\sqrt3$", r"$\dfrac{9\sqrt3}{2}$", r"$\dfrac{3\sqrt3}{4}$"],
    r"""Use $\text{Area} = \dfrac{n^2\sqrt{h^2 - ab}}{\lvert am^2 - 2hlm + bl^2\rvert}$ with $a = b = 1$, $h = -2$, $l = m = 1$, $n = -3$:
$$\text{Area} = \frac{9\sqrt{3}}{1 + 4 + 1} = \frac{3\sqrt3}{2}.$$

**Check.** The lines make $60^\circ$ with each other and are symmetric about $y = x$, which is perpendicular to $x + y = 3$. So the triangle is equilateral, with altitude $\tfrac{3}{\sqrt2}$ and side $\sqrt6$:
$$\text{Area} = \frac{\sqrt3}{4}\cdot 6 = \frac{3\sqrt3}{2}.$$
$3\sqrt3$ forgets the factor $\tfrac12$ in the area of a triangle.""")

# 17
T.single(1, ["general-condition"],
    r"The general second-degree equation $ax^2 + 2hxy + by^2 + 2gx + 2fy + c = 0$ represents a pair of straight lines only if",
    [r"$abc + 2fgh - af^2 - bg^2 - ch^2 = 0$", r"$abc + 2fgh - ag^2 - bf^2 - ch^2 = 0$",
     r"$abc - 2fgh - af^2 - bg^2 - ch^2 = 0$", r"$abc + 2fgh + af^2 + bg^2 + ch^2 = 0$"],
    r"""The condition is that the determinant vanishes:
$$\Delta = \begin{vmatrix} a & h & g\\ h & b & f\\ g & f & c\end{vmatrix} = abc + 2fgh - af^2 - bg^2 - ch^2 = 0.$$

Expanding along the first row gives $a(bc - f^2) - h(hc - fg) + g(hf - bg)$. So $a$ pairs with $f^2$ and $b$ with $g^2$. The second option swaps these pairs, which is the classic slip.""")

# 18
T.single(2, ["intersection"],
    r"The point of intersection of the lines $2x^2 + 5xy + 3y^2 + 6x + 7y + 4 = 0$ is",
    [r"$(1, -2)$", r"$(-1, 2)$", r"$(2, -1)$", r"$(-2, 1)$"],
    r"""Solve $\dfrac{\partial S}{\partial x} = 0$ and $\dfrac{\partial S}{\partial y} = 0$:
$$4x + 5y + 6 = 0, \qquad 5x + 6y + 7 = 0.$$
This gives $x = 1$, $y = -2$.

Check: $S = (2x + 3y + 4)(x + y + 1)$, and $(1, -2)$ lies on both lines: $2 - 6 + 4 = 0$ and $1 - 2 + 1 = 0$. The point $(-1, 2)$ comes from a sign slip in $g$ and $f$.""")

# 19
T.single(3, ["homogenisation"],
    r"The angle between the lines joining the origin to the points of intersection of the curve $3x^2 + 5xy - 3y^2 + 2x + 3y = 0$ and the line $3x - 2y = 1$ is",
    [r"$\dfrac{\pi}{2}$", r"$\dfrac{\pi}{3}$", r"$\dfrac{\pi}{4}$", r"$\dfrac{\pi}{6}$"],
    r"""Homogenise the first-degree terms using $3x - 2y = 1$:
$$3x^2 + 5xy - 3y^2 + (2x + 3y)(3x - 2y) = 0 \;\Rightarrow\; 9x^2 + 10xy - 9y^2 = 0.$$
Here $a + b = 9 - 9 = 0$, so the lines are perpendicular, and the angle is $\dfrac{\pi}{2}$.

Note that the second-degree part $3x^2 + 5xy - 3y^2$ already has $a + b = 0$, and the added product $6x^2 + 5xy - 6y^2$ also has coefficient sum $0$.""")

# 20
T.single(2, ["homogeneous"],
    r"If $3x + 4y = 0$ is one of the lines represented by $6x^2 - xy + 4cy^2 = 0$, then $c$ equals",
    [r"$-3$", r"$3$", r"$-\dfrac13$", r"$1$"],
    r"""Substitute the slope $m = -\tfrac34$ of $3x + 4y = 0$, that is, put $y = -\tfrac34 x$:
$$6 + \frac34 + 4c\cdot\frac{9}{16} = 0 \;\Rightarrow\; \frac{27}{4} + \frac{9c}{4} = 0 \;\Rightarrow\; c = -3.$$

Check: $6x^2 - xy - 12y^2 = (3x + 4y)(2x - 3y)$. $c = 3$ comes from substituting $y = \tfrac34 x$ (a sign slip in the slope).""")

# 21
T.single(3, ["homogeneous", "exam-tips"],
    r"If the slope of one of the lines $ax^2 + 2hxy + by^2 = 0$ is twice the slope of the other, then",
    [r"$8h^2 = 9ab$", r"$9h^2 = 8ab$", r"$2h^2 = 9ab$", r"$4h^2 = 9ab$"],
    r"""Let the slopes be $m$ and $2m$. Then
$$3m = -\frac{2h}{b}, \qquad 2m^2 = \frac{a}{b}.$$
Eliminate $m$: $2\cdot\dfrac{4h^2}{9b^2} = \dfrac{a}{b}$, which gives $8h^2 = 9ab$.

In general, slopes in the ratio $k:1$ give $4kh^2 = (1 + k)^2ab$. $2h^2 = 9ab$ uses $m_1 + m_2 = -h/b$, forgetting the $2$. Check with $(y - x)(y - 2x) = 2x^2 - 3xy + y^2$: $a = 2$, $h = -\tfrac32$, $b = 1$, and $8\cdot\tfrac94 = 18 = 9\cdot 2$.""")

# 22 statements: 1 and 3 only
T.statements(2, ["homogeneous", "angle", "bisectors"],
    r"Consider the equation $ax^2 + 2hxy + by^2 = 0$, where $a, h, b$ are real and not all zero. Consider the following statements:",
    [r"If $a + b = 0$, the equation represents a pair of real, perpendicular lines.",
     r"If $h^2 < ab$, the equation represents two distinct real lines through the origin.",
     r"Whenever the equation represents two distinct real lines, the two bisectors of the angles between them are perpendicular to each other."],
    [r"1 and 3 only", r"1 only", r"2 and 3 only", r"1, 2 and 3"],
    r"""1. True. If $a + b = 0$, then $h^2 - ab = h^2 + a^2 > 0$ (not both zero, else $b = 0$ too), so the lines are real and $1 + m_1m_2 = 1 + \tfrac{a}{b} = 0$. (If $b = 0$, then $a = 0$, and the pair is $xy = 0$.)
2. False. $h^2 < ab$ gives imaginary lines; only the origin is real. For example, $x^2 + y^2 = 0$.
3. True. The bisectors are $hx^2 - (a - b)xy - hy^2 = 0$, whose $x^2$ and $y^2$ coefficients add to $0$.""")

# 23 statements: 3 only
T.statements(3, ["general-condition", "intersection"],
    r"Let $S \equiv ax^2 + 2hxy + by^2 + 2gx + 2fy + c$ and $\Delta = abc + 2fgh - af^2 - bg^2 - ch^2$. Consider the following statements:",
    [r"If $S = 0$ represents two intersecting lines, the angle between them depends on $g$, $f$ and $c$ as well as on $a$, $h$ and $b$.",
     r"If $\Delta = 0$, then $S = 0$ represents a pair of real straight lines.",
     r"If $S = 0$ represents two lines meeting at $(\alpha, \beta)$, then $a\alpha + h\beta + g = 0$ and $h\alpha + b\beta + f = 0$."],
    [r"3 only", r"2 and 3 only", r"1 and 3 only", r"1, 2 and 3"],
    r"""1. False. Shifting the origin to the point of intersection removes the linear terms and leaves $aX^2 + 2hXY + bY^2 = 0$. So the angle depends on $a, h, b$ only.
2. False. $\Delta = 0$ means a pair of lines, which may be **imaginary**. For $x^2 + y^2 = 0$, $\Delta = 0$, but its only real point is the origin.
3. True. The intersection point is where $\partial S/\partial x = \partial S/\partial y = 0$.""")

# 24 statements: 1, 2 and 3
T.statements(2, ["homogenisation"],
    r"The line $lx + my = n$ ($n \ne 0$) meets the circle $x^2 + y^2 = r^2$ at $P$ and $Q$, and $O$ is the origin. Consider the following statements:",
    [r"The joint equation of $OP$ and $OQ$ is $n^2(x^2 + y^2) = r^2(lx + my)^2$.",
     r"$\angle POQ = 90^\circ$ if and only if $2n^2 = r^2(l^2 + m^2)$.",
     r"$OP$ and $OQ$ coincide if and only if the line touches the circle."],
    [r"1, 2 and 3", r"1 and 2 only", r"1 only", r"2 and 3 only"],
    r"""1. True. Homogenise $x^2 + y^2 = r^2$ using $\dfrac{lx + my}{n} = 1$.
2. True. The coefficients of $x^2$ and $y^2$ are $n^2 - r^2l^2$ and $n^2 - r^2m^2$; their sum vanishes exactly when $2n^2 = r^2(l^2 + m^2)$.
3. True. For the joint equation,
$$h^2 - ab = n^2\left[r^2(l^2 + m^2) - n^2\right],$$
which is $0$ exactly when $n^2 = r^2(l^2 + m^2)$, the tangency condition (distance from $O$ equals $r$).""")

# 25 match: A-2, B-3, C-1, D-4
T.match(2, ["homogeneous", "angle"],
    r"Match each equation in List I with what it represents in List II.",
    [r"$x^2 - 2xy + y^2 = 0$", r"$x^2 + xy + y^2 = 0$", r"$2x^2 + 3xy - 2y^2 = 0$", r"$x^2 - 5xy + 6y^2 = 0$"],
    [r"two real perpendicular lines", r"two coincident lines", r"only the origin (imaginary lines)", r"two real, distinct, non-perpendicular lines"],
    [r"A-2, B-3, C-1, D-4", r"A-3, B-2, C-1, D-4", r"A-2, B-3, C-4, D-1", r"A-1, B-3, C-2, D-4"],
    r"""Compare $h^2$ with $ab$, and test $a + b$:
- A: $h = -1$, $h^2 = 1 = ab$: $(x - y)^2 = 0$, coincident (2).
- B: $h = \tfrac12$, $h^2 = \tfrac14 < 1 = ab$: imaginary (3).
- C: $a + b = 0$: perpendicular, $(2x - y)(x + 2y) = 0$ (1).
- D: $(x - 2y)(x - 3y) = 0$, slopes $\tfrac12, \tfrac13$, and $a + b = 7 \ne 0$ (4).

Answer: A-2, B-3, C-1, D-4.""")

# 26 match: A-3, B-2, C-1, D-4
T.match(3, ["angle"],
    r"Match each pair of lines in List I with the acute angle between them in List II.",
    [r"$x^2 - 4xy + y^2 = 0$", r"$x^2 + xy = 0$", r"$\sqrt3\,x^2 - xy = 0$", r"$6x^2 - 5xy - 6y^2 = 0$"],
    [r"$\dfrac{\pi}{6}$", r"$\dfrac{\pi}{4}$", r"$\dfrac{\pi}{3}$", r"$\dfrac{\pi}{2}$"],
    [r"A-3, B-2, C-1, D-4", r"A-1, B-2, C-3, D-4", r"A-3, B-1, C-2, D-4", r"A-3, B-2, C-4, D-1"],
    r"""Use $\tan\theta = \dfrac{2\sqrt{h^2 - ab}}{\lvert a + b\rvert}$:
- A: $a = b = 1$, $h = -2$: $\tan\theta = \sqrt3$, so $\tfrac{\pi}{3}$ (3).
- B: $x(x + y) = 0$, the lines $x = 0$ and $y = -x$: $\tfrac{\pi}{4}$ (2). By the formula, $a = 1$, $h = \tfrac12$, $b = 0$ give $\tan\theta = 1$.
- C: $x(\sqrt3\,x - y) = 0$, the lines $x = 0$ and $y = \sqrt3\,x$ (at $60^\circ$ to the $x$-axis): $\tfrac{\pi}{6}$ (1). By the formula, $\tan\theta = \dfrac{2\cdot\tfrac12}{\sqrt3} = \dfrac{1}{\sqrt3}$.
- D: $a + b = 0$: $\tfrac{\pi}{2}$ (4).

Answer: A-3, B-2, C-1, D-4.""")

# 27 AR: 0
T.assertion_reason(1, ["angle"],
    r"The equation $3x^2 + 8xy - 3y^2 = 0$ represents a pair of perpendicular lines.",
    r"The equation $ax^2 + 2hxy + by^2 = 0$ ($a, h, b$ not all zero) represents a pair of perpendicular lines if and only if $a + b = 0$.",
    0,
    r"""Assertion: true, because $3 + (-3) = 0$. Indeed, $3x^2 + 8xy - 3y^2 = (3x - y)(x + 3y)$, with slopes $3$ and $-\tfrac13$.

Reason: true; it is the standard condition, since $\tan\theta = \dfrac{2\sqrt{h^2 - ab}}{a + b}$ is undefined exactly when $a + b = 0$. The reason is exactly the test used, so it explains the assertion.""")

# 28 AR: 1
T.assertion_reason(2, ["angle", "general-condition"],
    r"The acute angle between the lines $x^2 - 5xy + 4y^2 + x + 2y - 2 = 0$ equals the acute angle between the lines $x^2 - 5xy + 4y^2 = 0$.",
    r"For the equation $x^2 - 5xy + 4y^2 + x + 2y - 2 = 0$, $\Delta = abc + 2fgh - af^2 - bg^2 - ch^2 = 0$.",
    1,
    r"""Assertion: true. The lines are $x - y - 1 = 0$ and $x - 4y + 2 = 0$, which are parallel to $x - y = 0$ and $x - 4y = 0$. So both angles are $\tan^{-1}\tfrac35$.

Reason: true. With $a = 1$, $h = -\tfrac52$, $b = 4$, $g = \tfrac12$, $f = 1$, $c = -2$:
$$\Delta = -8 - \tfrac52 - 1 - 1 + \tfrac{25}{2} = 0.$$
But $\Delta = 0$ only says the equation is a pair of lines. The equality of the angles comes from the second-degree terms being the same, so the reason does not explain the assertion.""")

# 29 AR: 2
T.assertion_reason(2, ["intersection", "general-condition"],
    r"The equation $x^2 + 2xy + y^2 - 2x - 2y - 3 = 0$ represents a pair of parallel straight lines.",
    r"Whenever $h^2 = ab$, the equation $ax^2 + 2hxy + by^2 + 2gx + 2fy + c = 0$ represents a pair of parallel straight lines.",
    2,
    r"""Assertion: true. Put $u = x + y$: $u^2 - 2u - 3 = (u - 3)(u + 1) = 0$, so the lines are $x + y = 3$ and $x + y = -1$.

Reason: false. $h^2 = ab$ makes the second-degree part a perfect square, but $\Delta = 0$ is also needed. The parabola $y^2 = 4x$ has $h^2 = ab = 0$ but $\Delta = -4 \ne 0$.""")

# 30 AR: 3
T.assertion_reason(3, ["homogenisation"],
    r"The chord $x + 2y = 2$ of the circle $x^2 + y^2 = 4$ subtends a right angle at the origin.",
    r"The chord $lx + my = n$ of the circle $x^2 + y^2 = r^2$ subtends a right angle at the origin if and only if $2n^2 = r^2(l^2 + m^2)$.",
    3,
    r"""Reason: true. Homogenising gives $n^2(x^2 + y^2) = r^2(lx + my)^2$, and the $x^2$ and $y^2$ coefficients add to $2n^2 - r^2(l^2 + m^2)$.

Assertion: false. Here $2n^2 = 8$ but $r^2(l^2 + m^2) = 4\cdot 5 = 20$. Directly: the chord meets the circle at $(2, 0)$ and $\left(-\tfrac65, \tfrac85\right)$, and the dot product of these vectors is $-\tfrac{12}{5} \ne 0$.""")


def check():
    import sympy as sp
    x, y, X, Y, k, lam, c, m, A, H, B = sp.symbols("x y X Y k lambda c m A H B")

    def coeffs(expr):
        """(a, h, b, g, f, c) of a second-degree expression in x, y."""
        P = sp.Poly(sp.expand(expr), x, y)
        g = lambda i, j: P.coeff_monomial(x**i * y**j)
        return g(2, 0), g(1, 1) / 2, g(0, 2), g(1, 0) / 2, g(0, 1) / 2, g(0, 0)

    def Delta(expr):
        a, h, b, gg, f, cc = coeffs(expr)
        return sp.Matrix([[a, h, gg], [h, b, f], [gg, f, cc]]).det()

    def tan_acute(expr):
        a, h, b = coeffs(expr)[:3]
        return sp.simplify(2 * sp.sqrt(h**2 - a * b) / sp.Abs(a + b))

    def line_dirs(expr):
        """Direction vectors of the real lines of a homogeneous quadratic."""
        a, h, b = coeffs(expr)[:3]
        if b != 0:
            return [sp.Matrix([1, r]) for r in sp.solve(b * m**2 + 2 * h * m + a, m)]
        dirs = [sp.Matrix([0, 1])]
        if a != 0:
            dirs.append(sp.Matrix([-2 * h, a]))  # a x + 2h y = 0
        else:
            dirs.append(sp.Matrix([1, 0]))
        return dirs

    def acute_angle(u, v):
        return sp.acos(sp.Abs(u.dot(v)) / (u.norm() * v.norm()))

    def is_bisector_pair(pair, bis):
        d1, d2 = line_dirs(pair)
        bd = line_dirs(bis)
        assert len(bd) == 2
        for u in bd:
            if abs(sp.N(acute_angle(u, d1) - acute_angle(u, d2), 30)) > 1e-20:
                return False
        return sp.simplify(bd[0].dot(bd[1])) == 0

    # q1
    e1 = 6*x**2 - 5*x*y - 6*y**2
    eq(sp.expand((3*x + 2*y)*(2*x - 3*y)), e1, "q1 factor")
    d = line_dirs(e1); eq(d[0].dot(d[1]), 0, "q1 perpendicular")
    # q2
    eq(sp.atan(tan_acute(x**2 - 4*x*y + y**2)), sp.pi/3, "q2")
    eq(2*sp.sqrt(16 - 1)/2, sp.sqrt(15), "q2 distractor h=-4")
    # q3
    e3 = 2*x**2 + 5*x*y + 3*y**2
    eq(sp.expand((2*x + 3*y)*(x + y)), e3, "q3 factor")
    sl = [d[1]/d[0] for d in line_dirs(e3)]
    eq(sum(sl), sp.Rational(-5, 3), "q3"); eq(sl[0]*sl[1], sp.Rational(2, 3), "q3 product")
    # q4
    sol = sp.solve((lam - 3) + (2*lam + 1), lam); assert sol == [sp.Rational(2, 3)], "q4"
    e4 = coeffs(((lam - 3)*x**2 + 4*x*y + (2*lam + 1)*y**2).subs(lam, sp.Rational(2, 3)))
    assert e4[1]**2 - e4[0]*e4[2] > 0
    d = line_dirs(((lam - 3)*x**2 + 4*x*y + (2*lam + 1)*y**2).subs(lam, sp.Rational(2, 3)))
    eq(d[0].dot(d[1]), 0, "q4 perp")
    # q5
    assert sp.solve(6**2 - k*9, k) == [4], "q5"
    eq(sp.expand((2*x + 3*y)**2), 4*x**2 + 12*x*y + 9*y**2, "q5 square")
    # q6
    pair6 = 2*x**2 + 6*x*y + y**2
    assert is_bisector_pair(pair6, 3*x**2 - x*y - 3*y**2), "q6"
    for wrong in (3*x**2 + x*y - 3*y**2, x**2 - 3*x*y - y**2, 6*x**2 - x*y - 6*y**2):
        assert not is_bisector_pair(pair6, wrong)
    # q7
    e7 = lam*x**2 - 10*x*y + 12*y**2 + 5*x - 16*y - 3
    eq(sp.expand(Delta(e7)), 200 - 100*lam, "q7 Delta")
    assert sp.solve(Delta(e7), lam) == [2], "q7"
    eq(sp.expand((x - 2*y + 3)*(2*x - 6*y - 1)), e7.subs(lam, 2), "q7 factor")
    # q8
    e8 = x**2 - 5*x*y + 4*y**2 + x + 2*y - 2
    eq(sp.expand((x - y - 1)*(x - 4*y + 2)), e8, "q8")
    for wrong in ((x - y + 1)*(x - 4*y - 2), (x - 4*y - 1)*(x - y + 2), (x + y - 1)*(x + 4*y + 2)):
        assert sp.expand(wrong - e8) != 0
    # q9
    eq(tan_acute(e8), sp.Rational(3, 5), "q9")
    eq((1 - sp.Rational(1, 4))/(1 + sp.Rational(1, 4)), sp.Rational(3, 5), "q9 slopes")
    # q10
    e10 = sp.expand(x**2 + y**2 - 4*(x + y)**2)
    eq(-e10, 3*x**2 + 8*x*y + 3*y**2, "q10")
    pts = sp.solve([x**2 + y**2 - 4, x + y - 1], [x, y])
    for p in pts:
        eq((3*x**2 + 8*x*y + 3*y**2).subs({x: p[0], y: p[1]}), 0, "q10 points")
    # q11
    hom = sp.expand(c**2*(x**2 + y**2) - 10*(y - 2*x)**2)
    a_, h_, b_ = coeffs(hom)[:3]
    assert set(sp.solve(a_ + b_, c)) == {-5, 5}, "q11"
    P = sp.solve([x**2 + y**2 - 10, y - 2*x - 5], [x, y])
    eq(P[0][0]*P[1][0] + P[0][1]*P[1][1], 0, "q11 direct")
    # q12
    a = sp.symbols("a", positive=True)
    hom = sp.expand(y**2*k - 4*a*x*x)  # k y^2 = 4 a x^2 after multiplying by k
    a_, h_, b_ = coeffs(hom)[:3]
    assert sp.solve(a_ + b_, k) == [4*a], "q12"
    eq(sp.Matrix([4*a, 4*a]).dot(sp.Matrix([4*a, -4*a])), 0, "q12 direct")
    assert sp.Matrix([a, 2*a]).dot(sp.Matrix([a, -2*a])) < 0  # latus rectum: obtuse
    # q13
    e13 = 9*x**2 - 24*x*y + 16*y**2 - 12*x + 16*y - 12
    eq(sp.expand((3*x - 4*y - 6)*(3*x - 4*y + 2)), e13, "q13 factor")
    eq(sp.Abs(-6 - 2)/sp.sqrt(9 + 16), sp.Rational(8, 5), "q13")
    aa, hh, bb, gg, ff, cc = coeffs(e13)
    eq(2*sp.sqrt((gg**2 - aa*cc)/(aa*(aa + bb))), sp.Rational(8, 5), "q13 formula")
    eq(Delta(e13), 0, "q13 Delta"); eq(hh**2 - aa*bb, 0, "q13 parallel")
    # q14
    e14 = 2*x**2 - 5*x*y + 3*y**2
    ans14 = 3*x**2 + 5*x*y + 2*y**2
    d1, d2 = line_dirs(e14); p1, p2 = line_dirs(ans14)
    # each line of ans14 is perpendicular to one line of e14
    assert {sp.simplify(p1.dot(d1)) == 0 or sp.simplify(p1.dot(d2)) == 0,
            sp.simplify(p2.dot(d1)) == 0 or sp.simplify(p2.dot(d2)) == 0} == {True}, "q14"
    eq(sp.expand((3*x + 2*y)*(x + y)), ans14, "q14 factor")
    q1_, q2_ = line_dirs(2*x**2 + 5*x*y + 3*y**2)
    w = [v for v in (q1_, q2_) if v[1]/v[0] == sp.Rational(-2, 3)][0]
    assert w.dot(d1) != 0 and w.dot(d2) != 0  # slope -2/3 perpendicular to neither
    # q15
    sol = sp.solve([sp.diff(e8, x), sp.diff(e8, y)], [x, y]); assert sol == {x: 2, y: 1}, "q15 point"
    shifted = sp.expand(e8.subs({x: X + 2, y: Y + 1}))
    eq(shifted, X**2 - 5*X*Y + 4*Y**2, "q15 shift")
    assert is_bisector_pair(x**2 - 5*x*y + 4*y**2, 5*x**2 - 6*x*y - 5*y**2), "q15"
    assert not is_bisector_pair(x**2 - 5*x*y + 4*y**2, 5*x**2 + 6*x*y - 5*y**2)
    # the key, centred at (2,1); the last option is centred at (1,2), not the intersection point
    key15 = 5*(x - 2)**2 - 6*(x - 2)*(y - 1) - 5*(y - 1)**2
    eq(key15.subs({x: 2, y: 1}), 0, "q15 centre")
    assert sp.solve([sp.diff(key15, x), sp.diff(key15, y)], [x, y]) == {x: 2, y: 1}
    # q16
    vs = [sp.Matrix([0, 0])]
    for dvec in line_dirs(x**2 - 4*x*y + y**2):
        t = sp.symbols("t")
        tt = sp.solve(t*dvec[0] + t*dvec[1] - 3, t)[0]
        vs.append(sp.simplify(tt*dvec))
    area = sp.Abs(sp.Matrix([[vs[1][0], vs[1][1]], [vs[2][0], vs[2][1]]]).det())/2
    eq(area, 3*sp.sqrt(3)/2, "q16")
    eq(9*sp.sqrt(4 - 1)/(1*1 - 2*(-2)*1*1 + 1*1), 3*sp.sqrt(3)/2, "q16 formula")
    # q17
    a, h, b, g, f, cc = sp.symbols("a h b g f c")
    eq(sp.Matrix([[a, h, g], [h, b, f], [g, f, cc]]).det(), a*b*cc + 2*f*g*h - a*f**2 - b*g**2 - cc*h**2, "q17")
    a = sp.symbols("a", positive=True)
    # q18
    e18 = 2*x**2 + 5*x*y + 3*y**2 + 6*x + 7*y + 4
    eq(Delta(e18), 0, "q18 Delta")
    eq(sp.expand((2*x + 3*y + 4)*(x + y + 1)), e18, "q18 factor")
    assert sp.solve([sp.diff(e18, x), sp.diff(e18, y)], [x, y]) == {x: 1, y: -2}, "q18"
    # q19
    hom19 = sp.expand(3*x**2 + 5*x*y - 3*y**2 + (2*x + 3*y)*(3*x - 2*y))
    eq(hom19, 9*x**2 + 10*x*y - 9*y**2, "q19 hom")
    P = sp.solve([3*x**2 + 5*x*y - 3*y**2 + 2*x + 3*y, 3*x - 2*y - 1], [x, y])
    assert len(P) == 2
    eq(P[0][0]*P[1][0] + P[0][1]*P[1][1], 0, "q19 direct")
    # q20
    assert sp.solve((6*x**2 - x*y + 4*c*y**2).subs(y, -sp.Rational(3, 4)*x)/x**2, c) == [-3], "q20"
    eq(sp.expand((3*x + 4*y)*(2*x - 3*y)), 6*x**2 - x*y - 12*y**2, "q20 factor")
    # q21: general k-ratio and the k = 2 case
    mm, kk = sp.symbols("mm kk")
    a, h, b = sp.symbols("a h b")
    # slopes m and k m: roots of b t^2 + 2h t + a
    rel = sp.simplify((kk*(-2*h/(b*(1 + kk)))**2) - a/b)
    eq(sp.simplify(rel*b**2*(1 + kk)**2), 4*kk*h**2 - (1 + kk)**2*a*b, "q21 general")
    eq((4*kk*h**2 - (1 + kk)**2*a*b).subs(kk, 2), 8*h**2 - 9*a*b, "q21")
    aa, hh, bb = coeffs(sp.expand((y - x)*(y - 2*x)))[:3]
    eq(8*hh**2, 9*aa*bb, "q21 example")
    # q22
    a = sp.symbols("a", real=True)
    eq(sp.expand(h**2 - a*(-a)), h**2 + a**2, "q22 s1")
    d = line_dirs(3*x**2 + 4*x*y - 3*y**2); eq(d[0].dot(d[1]), 0, "q22 s1 example")
    assert all(not r.is_real for r in sp.solve(m**2 + 1, m)), "q22 s2 counterexample"
    aa_, hh_, bb_ = sp.symbols("aa hh bb")
    bis = hh_*x**2 - (aa_ - bb_)*x*y - hh_*y**2
    eq(sum(coeffs(bis)[i] for i in (0, 2)), 0, "q22 s3")
    # q23
    eq(tan_acute(e8), tan_acute(x**2 - 5*x*y + 4*y**2), "q23 s1 false")
    eq(Delta(x**2 + y**2), 0, "q23 s2 counterexample")
    assert sp.solve([sp.diff(e18, x), sp.diff(e18, y)], [x, y]) == {x: 1, y: -2}  # s3 example
    eq(e18.subs({x: 1, y: -2}), 0, "q23 s3 on curve")
    # q24
    l, mq, n, r = sp.symbols("l mq n r", positive=True)
    joint = sp.expand(n**2*(x**2 + y**2) - r**2*(l*x + mq*y)**2)
    ja, jh, jb = coeffs(joint)[:3]
    eq(ja + jb, 2*n**2 - r**2*(l**2 + mq**2), "q24 s2")
    eq(sp.factor(jh**2 - ja*jb), sp.factor(n**2*(r**2*(l**2 + mq**2) - n**2)), "q24 s3")
    # q25
    assert coeffs(x**2 - 2*x*y + y**2)[1]**2 == 1  # h^2 = ab
    a_, h_, b_ = coeffs(x**2 + x*y + y**2)[:3]; assert h_**2 < a_*b_, "q25 B"
    d = line_dirs(2*x**2 + 3*x*y - 2*y**2); eq(d[0].dot(d[1]), 0, "q25 C")
    eq(sp.expand((2*x - y)*(x + 2*y)), 2*x**2 + 3*x*y - 2*y**2, "q25 C factor")
    d = line_dirs(x**2 - 5*x*y + 6*y**2); assert d[0].dot(d[1]) != 0, "q25 D"
    eq(sp.expand((x - 2*y)*(x - 3*y)), x**2 - 5*x*y + 6*y**2, "q25 D factor")
    # q26
    for expr, want in ((x**2 - 4*x*y + y**2, sp.pi/3), (x**2 + x*y, sp.pi/4),
                       (sp.sqrt(3)*x**2 - x*y, sp.pi/6), (6*x**2 - 5*x*y - 6*y**2, sp.pi/2)):
        d1, d2 = line_dirs(expr)
        eq(acute_angle(d1, d2), want, f"q26 {expr}")
    # q27
    eq(sp.expand((3*x - y)*(x + 3*y)), 3*x**2 + 8*x*y - 3*y**2, "q27")
    d = line_dirs(3*x**2 + 8*x*y - 3*y**2); eq(d[0].dot(d[1]), 0, "q27 perp")
    # q28
    eq(Delta(e8), 0, "q28 reason")
    eq(tan_acute(e8), tan_acute(x**2 - 5*x*y + 4*y**2), "q28 assertion")
    # q29
    e29 = x**2 + 2*x*y + y**2 - 2*x - 2*y - 3
    eq(sp.expand((x + y - 3)*(x + y + 1)), e29, "q29 assertion")
    pa, ph, pb = coeffs(y**2 - 4*x)[:3]
    eq(ph**2 - pa*pb, 0, "q29 parabola h^2=ab"); eq(Delta(y**2 - 4*x), -4, "q29 reason false")
    # q30
    P = sp.solve([x**2 + y**2 - 4, x + 2*y - 2], [x, y])
    assert set(P) == {(2, 0), (sp.Rational(-6, 5), sp.Rational(8, 5))}
    eq(P[0][0]*P[1][0] + P[0][1]*P[1][1], sp.Rational(-12, 5), "q30 assertion false")
    eq(2*2**2 - 4*(1 + 4), -12, "q30 condition fails")
    # notes examples
    eq(sp.expand((3*x - 4*y)**2 - 4*(3*x - 4*y) - 12), e13, "notes parallel")
    eq(sp.solve((6 + sp.Rational(3, 4) + 4*c*sp.Rational(9, 16)), c)[0], -3, "notes tip")


T.write(check)
