import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from qlib import Topic, eq

T = Topic("math.geometry.planes")

# 1
T.single(1, ["coordinates"],
    r"The distance between the points $(1, 2, 3)$ and $(4, -2, 15)$ is",
    [r"$13$", r"$\sqrt{349}$", r"$19$", r"$12$"],
    r"""The coordinate differences are $3$, $-4$, $12$:
$$d = \sqrt{3^2 + (-4)^2 + 12^2} = \sqrt{169} = 13.$$

$\sqrt{349}$ comes from adding $3$ and $15$ instead of subtracting for $z$. $19$ adds the absolute differences, which is not a Euclidean distance.""")

# 2
T.single(1, ["coordinates"],
    r"The point dividing the join of $A(2, -3, 4)$ and $B(8, 0, 10)$ internally in the ratio $1 : 2$ is",
    [r"$(4, -2, 6)$", r"$(6, -1, 8)$", r"$(-4, -6, -2)$", r"$(5, -\tfrac32, 7)$"],
    r"""With $m : n = 1 : 2$, the point is $\dfrac{mB + nA}{m + n}$:
$$\left(\frac{8 + 4}{3},\ \frac{0 - 6}{3},\ \frac{10 + 8}{3}\right) = (4, -2, 6).$$

$(6, -1, 8)$ swaps the weights (it divides in $2 : 1$); $(-4, -6, -2)$ is the external point; $(5, -\tfrac32, 7)$ is the midpoint. Check: $(4, -2, 6)$ is one third of the way from $A$ to $B$.""")

# 3
T.single(1, ["direction-cosines"],
    r"A line has direction ratios $2, -3, 6$. One set of its direction cosines is",
    [r"$\tfrac27, -\tfrac37, \tfrac67$", r"$\tfrac25, -\tfrac35, \tfrac65$", r"$-\tfrac27, \tfrac37, \tfrac67$", r"$\tfrac{2}{\sqrt7}, -\tfrac{3}{\sqrt7}, \tfrac{6}{\sqrt7}$"],
    r"""Divide by $\sqrt{2^2 + 3^2 + 6^2} = \sqrt{49} = 7$:
$$l, m, n = \tfrac27, -\tfrac37, \tfrac67, \qquad l^2 + m^2 + n^2 = \tfrac{4 + 9 + 36}{49} = 1.$$

Dividing by the sum $2 - 3 + 6 = 5$ is a common slip; its squares add to $\tfrac{49}{25}$. The set $-\tfrac27, \tfrac37, \tfrac67$ flips only two signs, so it is not proportional to $2, -3, 6$. Dividing by $\sqrt7$ forgets the square root of $49$.""")

# 4
T.single(2, ["direction-cosines"],
    r"The angle between the lines with direction ratios $1, 1, 2$ and $\sqrt3 - 1, -\sqrt3 - 1, 4$ is",
    [r"$\dfrac{\pi}{3}$", r"$\dfrac{\pi}{6}$", r"$\dfrac{\pi}{4}$", r"$\dfrac{\pi}{2}$"],
    r"""The dot product is $(\sqrt3 - 1) + (-\sqrt3 - 1) + 8 = 6$. The lengths are $\sqrt6$ and
$$\sqrt{(4 - 2\sqrt3) + (4 + 2\sqrt3) + 16} = \sqrt{24}.$$
So
$$\cos\theta = \frac{6}{\sqrt6\,\sqrt{24}} = \frac{6}{12} = \frac12, \qquad \theta = \frac{\pi}{3}.$$

$\tfrac{\pi}{6}$ reads $\tfrac12$ as a sine. The $\sqrt3$ terms cancel in the dot product but not in the length, so the lines are not perpendicular.""")

# 5 (pair of planes, Delta) hard
T.single(3, ["pair-of-planes"],
    r"The equation $x^2 - 2y^2 + z^2 - xy - yz + \lambda zx = 0$ represents a pair of planes. The positive value of $\lambda$ is",
    [r"$2$", r"$\dfrac52$", r"$4$", r"$1$"],
    r"""Here $a = 1$, $b = -2$, $c = 1$, $f = -\tfrac12$, $g = \tfrac{\lambda}{2}$, $h = -\tfrac12$. The condition is
$$\Delta = abc + 2fgh - af^2 - bg^2 - ch^2 = 0:$$
$$-2 + \frac{\lambda}{4} - \frac14 + \frac{\lambda^2}{2} - \frac14 = \frac{2\lambda^2 + \lambda - 10}{4} = \frac{(\lambda - 2)(2\lambda + 5)}{4} = 0.$$
So $\lambda = 2$ or $-\tfrac52$, and the positive value is $2$.

Check: $(x + y + z)(x - 2y + z) = x^2 - 2y^2 + z^2 - xy - yz + 2zx$. The value $\tfrac52$ is the other root with its sign lost; $\lambda = 4$ comes from taking $g = \lambda$ instead of $\lambda/2$.""")

# 6
T.single(2, ["direction-cosines"],
    r"The length of the projection of the segment joining $P(3, -1, 2)$ and $Q(5, 2, -4)$ on the line with direction ratios $2, -6, 3$ is",
    [r"$\dfrac{32}{7}$", r"$\dfrac47$", r"$32$", r"$7$"],
    r"""$\vec{PQ} = (2, 3, -6)$. The direction cosines of the line are $\tfrac27, -\tfrac67, \tfrac37$. So the projection is
$$2\cdot\tfrac27 + 3\cdot\left(-\tfrac67\right) + (-6)\cdot\tfrac37 = \frac{4 - 18 - 18}{7} = -\frac{32}{7},$$
of length $\tfrac{32}{7}$.

$32$ forgets to divide by $7$ (uses d.r.s instead of d.c.s). $7$ is the length $PQ$ itself, not its projection. $\tfrac47$ loses the sign of $-6$.""")

# 7
T.single(2, ["direction-cosines", "exam-tips"],
    r"The acute angle between two body diagonals of a cube is",
    [r"$\cos^{-1}\dfrac13$", r"$\cos^{-1}\dfrac{1}{\sqrt3}$", r"$\cos^{-1}\dfrac23$", r"$\cos^{-1}\sqrt{\dfrac23}$"],
    r"""Take the unit cube with a vertex at $O$. The diagonals from $(0,0,0)$ to $(1,1,1)$ and from $(1,0,0)$ to $(0,1,1)$ have d.r.s $(1, 1, 1)$ and $(-1, 1, 1)$:
$$\cos\theta = \frac{-1 + 1 + 1}{\sqrt3\,\sqrt3} = \frac13.$$

$\cos^{-1}\tfrac{1}{\sqrt3}$ is the angle between a diagonal and an **edge**; $\cos^{-1}\sqrt{2/3}$ is between a body diagonal and a face diagonal.""")

# 8
T.single(1, ["plane-forms"],
    r"The intercepts made on the $x$-, $y$- and $z$-axes by the plane $2x - 3y + 4z = 12$ are",
    [r"$6, -4, 3$", r"$6, 4, 3$", r"$\tfrac16, -\tfrac14, \tfrac13$", r"$2, -3, 4$"],
    r"""Divide by $12$:
$$\frac{x}{6} + \frac{y}{-4} + \frac{z}{3} = 1,$$
so the intercepts are $6, -4, 3$. (Or put two coordinates zero: $y = z = 0$ gives $x = 6$, and so on.)

Dropping the sign gives $6, 4, 3$; the reciprocals are the coefficients after dividing, not the intercepts; $2, -3, 4$ are d.r.s of the normal.""")

# 9
T.single(2, ["plane-forms"],
    r"The normal form of the plane $2x - y + 2z + 9 = 0$ is",
    [r"$-\tfrac23x + \tfrac13y - \tfrac23z = 3$", r"$\tfrac23x - \tfrac13y + \tfrac23z = 3$", r"$-\tfrac29x + \tfrac19y - \tfrac29z = 1$", r"$-\tfrac23x + \tfrac13y - \tfrac23z = 1$"],
    r"""Write $2x - y + 2z = -9$ and divide by $-\sqrt{4 + 1 + 4} = -3$ so that the right side is positive:
$$-\tfrac23x + \tfrac13y - \tfrac23z = 3.$$
The distance from $O$ is $p = 3$, and the normal from $O$ has d.c.s $-\tfrac23, \tfrac13, -\tfrac23$.

$\tfrac23x - \tfrac13y + \tfrac23z = 3$ is the parallel plane on the other side of $O$ (the sign of the constant was changed alone). Dividing by $9$ does not give unit coefficients: $\tfrac{4 + 1 + 4}{81} \ne 1$.""")

# 10
T.single(2, ["plane-forms"],
    r"The plane through $A(2, 1, 0)$, $B(3, -2, -2)$ and $C(3, 1, 7)$ is",
    [r"$7x + 3y - z = 17$", r"$7x + 3y - z = 14$", r"$7x - 3y - z = 11$", r"$7x + 3y + z = 17$"],
    r"""$\vec{AB} = (1, -3, -2)$ and $\vec{AC} = (1, 0, 7)$. The normal is
$$\vec{AB} \times \vec{AC} = (-21, -9, 3) \parallel (7, 3, -1).$$
Through $A$: $7(x - 2) + 3(y - 1) - z = 0$, i.e. $7x + 3y - z = 17$.

Check: $B$ gives $21 - 6 + 2 = 17$ and $C$ gives $21 + 3 - 7 = 17$. The other options fail at least one point; for example, $7x + 3y + z = 17$ fails at $C$ ($31$).""")

# 11
T.single(2, ["coordinates", "plane-forms"],
    r"The points $A(0, -1, 0)$, $B(2, 1, -1)$, $C(1, 1, 1)$ and $D(4, 5, k)$ are coplanar when $k$ equals",
    [r"$1$", r"$-1$", r"$2$", r"$0$"],
    r"""Coplanar $\iff$ the determinant of $\vec{AB}, \vec{AC}, \vec{AD}$ vanishes:
$$\det\begin{pmatrix} 2 & 2 & -1\\ 1 & 2 & 1\\ 4 & 6 & k\end{pmatrix} = 2(2k - 6) - 2(k - 4) - (6 - 8) = 2k - 2 = 0.$$
So $k = 1$.

Check: the plane $ABC$ is $4x - 3y + 2z = 3$, and $D$ gives $16 - 15 + 2k = 3$, so $k = 1$.""")

# 12
T.single(1, ["distance-angle"],
    r"The distance of the point $(2, 3, -5)$ from the plane $x + 2y - 2z = 9$ is",
    [r"$3$", r"$\dfrac{11}{3}$", r"$9$", r"$6$"],
    r"""$$d = \frac{\lvert 2 + 6 - 2(-5) - 9\rvert}{\sqrt{1 + 4 + 4}} = \frac{9}{3} = 3.$$

$\tfrac{11}{3}$ takes $-2z$ as $-10$ (sign slip on $z = -5$). $9$ forgets the denominator, and $6$ forgets the constant $-9$.""")

# 13
T.single(2, ["distance-angle"],
    r"The distance between the parallel planes $2x - 2y + z + 3 = 0$ and $4x - 4y + 2z + 5 = 0$ is",
    [r"$\dfrac16$", r"$\dfrac23$", r"$\dfrac{11}{6}$", r"$\dfrac13$"],
    r"""First make the coefficients identical: the second plane is $2x - 2y + z + \tfrac52 = 0$. Then
$$d = \frac{\lvert 3 - \tfrac52\rvert}{\sqrt{4 + 4 + 1}} = \frac{1/2}{3} = \frac16.$$

$\tfrac23 = \tfrac{\lvert 3 - 5\rvert}{3}$ uses the constants without equalising the coefficients. $\tfrac{11}{6}$ adds the constants, as if the planes were on opposite sides of $O$ (they are on the same side, since $3$ and $\tfrac52$ have the same sign).""")

# 14
T.single(1, ["distance-angle"],
    r"The acute angle between the planes $2x - y + 2z = 5$ and $x - y = 3$ is",
    [r"$\dfrac{\pi}{4}$", r"$\dfrac{\pi}{3}$", r"$\dfrac{\pi}{6}$", r"$\dfrac{\pi}{2}$"],
    r"""The normals are $(2, -1, 2)$ and $(1, -1, 0)$:
$$\cos\theta = \frac{2 + 1 + 0}{3\cdot\sqrt2} = \frac{1}{\sqrt2}, \qquad \theta = \frac{\pi}{4}.$$

The plane $x - y = 3$ has no $z$ term; its normal still has three components, with the last one $0$. Ignoring the $+1$ from $(-1)(-1)$ would give $\cos\theta = \tfrac{1}{3\sqrt2}$, not a standard angle.""")

# 15
T.single(2, ["distance-angle"],
    r"The image of the point $(1, 3, 4)$ in the plane $2x - y + z + 3 = 0$ is",
    [r"$(-3, 5, 2)$", r"$(-1, 4, 3)$", r"$(5, 1, 6)$", r"$(-7, 8, -1)$"],
    r"""Let $t = \dfrac{2(1) - 3 + 4 + 3}{2^2 + 1^2 + 1^2} = \dfrac{6}{6} = 1$. The image is
$$P' = P - 2t\,(2, -1, 1) = (1, 3, 4) - (4, -2, 2) = (-3, 5, 2).$$

$(-1, 4, 3)$ is the **foot** of the perpendicular (one step, not two). $(5, 1, 6)$ moves in the wrong direction. Check: the midpoint of $(1, 3, 4)$ and $(-3, 5, 2)$ is $(-1, 4, 3)$, which lies on the plane.""")

# 16
T.single(2, ["family"],
    r"The plane through the line of intersection of $x + y + z = 6$ and $2x + 3y + 4z + 5 = 0$ that passes through $(1, 1, 1)$ is",
    [r"$20x + 23y + 26z - 69 = 0$", r"$20x + 23y + 26z + 69 = 0$", r"$8x + 5y + 2z - 99 = 0$", r"$x + y + z - 3 = 0$"],
    r"""Take $(x + y + z - 6) + \lambda(2x + 3y + 4z + 5) = 0$. At $(1, 1, 1)$:
$$-3 + 14\lambda = 0, \qquad \lambda = \tfrac{3}{14}.$$
Multiplying by $14$:
$$14(x + y + z - 6) + 3(2x + 3y + 4z + 5) = 20x + 23y + 26z - 69 = 0.$$

$8x + 5y + 2z - 99 = 0$ uses $\lambda = -\tfrac{3}{14}$: it contains the line but not $(1, 1, 1)$. $x + y + z = 3$ passes through the point but does not contain the line.""")

# 17
T.single(3, ["family"],
    r"The plane through the line of intersection of $x + 2y + 3z - 4 = 0$ and $2x + y - z + 5 = 0$ and perpendicular to the plane $5x + 3y + 6z + 8 = 0$ is",
    [r"$51x + 15y - 50z + 173 = 0$", r"$65x + 43y - 8z + 117 = 0$", r"$51x + 15y - 50z - 173 = 0$", r"$51x - 15y + 50z + 173 = 0$"],
    r"""The family is $(x + 2y + 3z - 4) + \lambda(2x + y - z + 5) = 0$, with normal $(1 + 2\lambda,\ 2 + \lambda,\ 3 - \lambda)$. Perpendicular to $(5, 3, 6)$:
$$5(1 + 2\lambda) + 3(2 + \lambda) + 6(3 - \lambda) = 29 + 7\lambda = 0, \qquad \lambda = -\tfrac{29}{7}.$$
Then $7(x + 2y + 3z - 4) - 29(2x + y - z + 5) = 0$:
$$-51x - 15y + 50z - 173 = 0 \iff 51x + 15y - 50z + 173 = 0.$$

Check: $5(51) + 3(15) + 6(-50) = 0$. $65x + 43y - 8z + 117 = 0$ comes from $\lambda = +\tfrac{29}{7}$; it contains the line but is not perpendicular to the given plane.""")

# 18
T.single(2, ["bisectors"],
    r"The plane bisecting the angle between the planes $2x - y + 2z + 3 = 0$ and $3x - 2y + 6z + 8 = 0$ that contains the origin is",
    [r"$5x - y - 4z - 3 = 0$", r"$23x - 13y + 32z + 45 = 0$", r"$x - y + 4z + 5 = 0$", r"$5x - y - 4z + 3 = 0$"],
    r"""Both constants are positive, so the bisector of the angle containing $O$ takes the $+$ sign:
$$\frac{2x - y + 2z + 3}{3} = +\frac{3x - 2y + 6z + 8}{7}.$$
So $14x - 7y + 14z + 21 = 9x - 6y + 18z + 24$, i.e. $5x - y - 4z - 3 = 0$.

$23x - 13y + 32z + 45 = 0$ is the other bisector ($-$ sign). $x - y + 4z + 5 = 0$ equates the two left sides without dividing by the norms $3$ and $7$; it contains the common line but is not a bisector.""")

# 19
T.single(3, ["bisectors"],
    r"The plane bisecting the acute angle between the planes $2x - y + 2z + 3 = 0$ and $2x + 3y - 6z + 14 = 0$ is",
    [r"$8x - 16y + 32z - 21 = 0$", r"$20x + 2y - 4z + 63 = 0$", r"$8x - 16y + 32z + 21 = 0$", r"$20x + 2y - 4z - 63 = 0$"],
    r"""The norms are $3$ and $7$, and both constants are positive. The bisectors are
$$7(2x - y + 2z + 3) = \pm 3(2x + 3y - 6z + 14).$$
- $+$: $8x - 16y + 32z - 21 = 0$ (the angle containing $O$).
- $-$: $20x + 2y - 4z + 63 = 0$.

Now $a_1a_2 + b_1b_2 + c_1c_2 = 4 - 3 - 12 = -11 < 0$, so the origin lies in the **acute** angle, and the $+$ bisector is the acute one.

Check: the normal $(1, -2, 4)$ of the answer makes with $(2, -1, 2)$ an angle with $\cos = \tfrac{12}{3\sqrt{21}} \approx 0.87$, which is less than $45^\circ$. So it lies in the acute angle. The plane $20x + 2y - 4z + 63 = 0$ bisects the obtuse angle.""")

# 20
T.single(3, ["coordinates", "plane-forms", "exam-tips"],
    r"A plane meets the coordinate axes at $A$, $B$, $C$, and the centroid of the tetrahedron $OABC$ is $(1, 2, 3)$. The plane is",
    [r"$6x + 3y + 2z = 24$", r"$6x + 3y + 2z = 18$", r"$6x + 3y + 2z = 6$", r"$x + 2y + 3z = 14$"],
    r"""Let the intercepts be $\alpha, \beta, \gamma$. The centroid of $O, A, B, C$ is $\left(\tfrac{\alpha}{4}, \tfrac{\beta}{4}, \tfrac{\gamma}{4}\right) = (1, 2, 3)$, so $\alpha = 4$, $\beta = 8$, $\gamma = 12$:
$$\frac{x}{4} + \frac{y}{8} + \frac{z}{12} = 1 \iff 6x + 3y + 2z = 24.$$

$6x + 3y + 2z = 18$ is the answer when $(1, 2, 3)$ is the centroid of the **triangle** $ABC$ (factor $3$). $6x + 3y + 2z = 6$ uses $1, 2, 3$ as the intercepts. $x + 2y + 3z = 14$ is the plane through $(1, 2, 3)$ normal to $OG$, which is a different condition.""")

# 21
T.single(3, ["distance-angle"],
    r"A variable plane stays at a constant distance $p$ from the origin and meets the axes at $A$, $B$, $C$. The locus of the centroid of the triangle $ABC$ is",
    [r"$x^{-2} + y^{-2} + z^{-2} = 9p^{-2}$", r"$x^{-2} + y^{-2} + z^{-2} = 16p^{-2}$", r"$x^{-2} + y^{-2} + z^{-2} = p^{-2}$", r"$x^2 + y^2 + z^2 = 9p^2$"],
    r"""Let the plane be $\dfrac{x}{\alpha} + \dfrac{y}{\beta} + \dfrac{z}{\gamma} = 1$. Its distance from $O$ is $p$:
$$\frac{1}{\alpha^2} + \frac{1}{\beta^2} + \frac{1}{\gamma^2} = \frac{1}{p^2}.$$
The centroid is $(x, y, z) = \left(\tfrac{\alpha}{3}, \tfrac{\beta}{3}, \tfrac{\gamma}{3}\right)$, so $\alpha = 3x$, etc.:
$$\frac{1}{9x^2} + \frac{1}{9y^2} + \frac{1}{9z^2} = \frac{1}{p^2} \iff x^{-2} + y^{-2} + z^{-2} = 9p^{-2}.$$

$16p^{-2}$ is the locus for the centroid of the **tetrahedron** $OABC$. $x^2 + y^2 + z^2 = 9p^2$ inverts wrongly: the relation is between reciprocals of squares.""")

# 22 statements: 1 and 3 only
T.statements(2, ["direction-cosines"],
    r"Consider the following statements about direction cosines:",
    [r"There is a line making angles $45^\circ$, $60^\circ$ and $120^\circ$ with the positive $x$-, $y$- and $z$-axes respectively.",
     r"There is a line making angles $30^\circ$, $45^\circ$ and $60^\circ$ with the positive $x$-, $y$- and $z$-axes respectively.",
     r"If $l, m, n$ are the direction cosines of a line, then $l + m + n \le \sqrt3$."],
    [r"1 and 3 only", r"1 only", r"2 and 3 only", r"1, 2 and 3"],
    r"""Angles $\alpha, \beta, \gamma$ are possible iff $\cos^2\alpha + \cos^2\beta + \cos^2\gamma = 1$.

1. True: $\tfrac12 + \tfrac14 + \tfrac14 = 1$.
2. False: $\tfrac34 + \tfrac12 + \tfrac14 = \tfrac32 \ne 1$.
3. True: by Cauchy–Schwarz, $l + m + n \le \sqrt3\sqrt{l^2 + m^2 + n^2} = \sqrt3$, with equality for $l = m = n = \tfrac{1}{\sqrt3}$.""")

# 23 statements: 2 and 3 only
T.statements(3, ["distance-angle"],
    r"Consider the plane $\Pi : x + 2y - 3z + 1 = 0$ and the following statements:",
    [r"The points $(1, 1, 1)$ and $(2, -1, 0)$ lie on opposite sides of $\Pi$.",
     r"$\Pi$ is perpendicular to the plane $3x + 3y + 3z = 7$.",
     r"The distance between $\Pi$ and the plane $2x + 4y - 6z + 9 = 0$ is $\dfrac{\sqrt{14}}{4}$."],
    [r"2 and 3 only", r"1 and 2 only", r"3 only", r"1, 2 and 3"],
    r"""1. False. $x + 2y - 3z + 1$ equals $1 + 2 - 3 + 1 = 1$ at $(1, 1, 1)$ and $2 - 2 - 0 + 1 = 1$ at $(2, -1, 0)$. Same sign, so the **same** side.
2. True. $(1, 2, -3)\cdot(3, 3, 3) = 3 + 6 - 9 = 0$.
3. True. Halve the second plane: $x + 2y - 3z + \tfrac92 = 0$. Then
$$d = \frac{\lvert\tfrac92 - 1\rvert}{\sqrt{14}} = \frac{7}{2\sqrt{14}} = \frac{\sqrt{14}}{4}.$$""")

# 24 match: A-2, B-4, C-3, D-1
T.match(1, ["plane-forms", "distance-angle"],
    r"For the plane $2x + 3y + 6z = 14$, match each quantity in List I with its value in List II.",
    [r"distance of the plane from the origin", r"intercept on the $x$-axis", r"$n$, the third direction cosine of the normal from the origin", r"distance of the point $(1, 1, 1)$ from the plane"],
    [r"$\dfrac37$", r"$2$", r"$\dfrac67$", r"$7$"],
    [r"A-2, B-4, C-3, D-1", r"A-2, B-4, C-1, D-3", r"A-4, B-2, C-3, D-1", r"A-1, B-4, C-3, D-2"],
    r"""The norm of the normal is $\sqrt{4 + 9 + 36} = 7$, so the normal form is $\tfrac27x + \tfrac37y + \tfrac67z = 2$.
- A: $p = 2$ (2).
- B: $y = z = 0$ gives $x = 7$ (4).
- C: $n = \tfrac67$ (3).
- D: $\dfrac{\lvert 2 + 3 + 6 - 14\rvert}{7} = \dfrac37$ (1).

Answer: A-2, B-4, C-3, D-1.""")

# 25 match: A-4, B-2, C-3, D-1
T.match(2, ["pair-of-planes"],
    r"Each equation in List I represents a pair of planes through the origin. Match it with the acute angle between the planes in List II.",
    [r"$x^2 - y^2 = 0$", r"$z^2 + yz = 0$", r"$y^2 + xy + yz + zx = 0$", r"$\sqrt3\,x^2 + xy = 0$"],
    [r"$\dfrac{\pi}{6}$", r"$\dfrac{\pi}{4}$", r"$\dfrac{\pi}{3}$", r"$\dfrac{\pi}{2}$"],
    [r"A-4, B-2, C-3, D-1", r"A-4, B-3, C-2, D-1", r"A-2, B-4, C-3, D-1", r"A-4, B-2, C-1, D-3"],
    r"""Factorise and use the normals (or $\tan\theta = \dfrac{2\sqrt{f^2 + g^2 + h^2 - ab - bc - ca}}{\lvert a + b + c\rvert}$):
- A: $(x - y)(x + y)$; $a + b + c = 0$, so $\tfrac{\pi}{2}$ (4).
- B: $z(z + y)$; normals $(0, 0, 1)$, $(0, 1, 1)$: $\cos\theta = \tfrac{1}{\sqrt2}$, so $\tfrac{\pi}{4}$ (2).
- C: $(x + y)(y + z)$; normals $(1, 1, 0)$, $(0, 1, 1)$: $\cos\theta = \tfrac12$, so $\tfrac{\pi}{3}$ (3).
- D: $x(\sqrt3\,x + y)$; normals $(1, 0, 0)$, $(\sqrt3, 1, 0)$: $\cos\theta = \tfrac{\sqrt3}{2}$, so $\tfrac{\pi}{6}$ (1).

Answer: A-4, B-2, C-3, D-1.""")

# 26 AR: 0
T.assertion_reason(1, ["direction-cosines"],
    r"No line can make an angle of $60^\circ$ with each of the three coordinate axes.",
    r"The direction cosines $l, m, n$ of every line satisfy $l^2 + m^2 + n^2 = 1$.",
    0,
    r"""Reason: true; it is the basic identity for direction cosines.

Assertion: true. If $l = m = n = \cos 60^\circ = \tfrac12$, then $l^2 + m^2 + n^2 = \tfrac34 \ne 1$. The reason is exactly what rules it out, so it explains the assertion.""")

# 27 AR: 3
T.assertion_reason(2, ["bisectors"],
    r"The plane $5x - y - 4z - 3 = 0$ bisects the acute angle between the planes $2x - y + 2z + 3 = 0$ and $3x - 2y + 6z + 8 = 0$.",
    r"If $d_1, d_2 > 0$ and $a_1a_2 + b_1b_2 + c_1c_2 > 0$, then the origin lies in the obtuse angle between the planes $a_1x + b_1y + c_1z + d_1 = 0$ and $a_2x + b_2y + c_2z + d_2 = 0$.",
    3,
    r"""Reason: true; it is the standard test (the region containing $O$ has dihedral angle $\pi$ minus the angle between the normals).

Assertion: false. $5x - y - 4z - 3 = 0$ is the $+$ bisector $7(2x - y + 2z + 3) = 3(3x - 2y + 6z + 8)$, i.e. the one containing the origin. Since $6 + 2 + 12 = 20 > 0$, that angle is **obtuse**. The acute bisector is $23x - 13y + 32z + 45 = 0$.""")

# 28 AR: 1
T.assertion_reason(2, ["distance-angle"],
    r"The points $(1, -1, 2)$ and $(2, 1, 1)$ lie on the same side of the plane $x + y + z = 1$.",
    r"The plane $x + y + z = 1$ is equally inclined to the three coordinate axes.",
    1,
    r"""Assertion: true. $x + y + z - 1$ equals $1$ at $(1, -1, 2)$ and $3$ at $(2, 1, 1)$: both positive, so the same side.

Reason: true. The normal has d.c.s $\tfrac{1}{\sqrt3}, \tfrac{1}{\sqrt3}, \tfrac{1}{\sqrt3}$, so it makes equal angles with the axes, and so does the plane (each angle is the complement). But the inclination says nothing about which side two points lie on; the test is the sign of $x + y + z - 1$. So the reason does not explain the assertion.""")

# 29 AR: 2
T.assertion_reason(3, ["pair-of-planes"],
    r"The equation $x^2 - 2y^2 + z^2 - xy - yz + 2zx = 0$ represents a pair of perpendicular planes.",
    r"Every homogeneous equation of the second degree in $x, y, z$ represents a pair of planes through the origin.",
    2,
    r"""Assertion: true. It factorises as $(x + y + z)(x - 2y + z) = 0$, and the normals satisfy $(1, 1, 1)\cdot(1, -2, 1) = 0$. (Equivalently, $a + b + c = 1 - 2 + 1 = 0$.)

Reason: false. A homogeneous quadratic is a pair of planes only when $\Delta = abc + 2fgh - af^2 - bg^2 - ch^2 = 0$. For example, $x^2 + y^2 - z^2 = 0$ has $\Delta = -1 \ne 0$; it is a cone. (In two variables every homogeneous quadratic is a pair of lines, which is the source of this trap.)""")

# 30 AR: 0
T.assertion_reason(3, ["family"],
    r"The plane through the line of intersection of $x + y + z = 1$ and $2x + 3y - z + 4 = 0$ that is parallel to the $x$-axis is $y - 3z + 6 = 0$.",
    r"A plane $ax + by + cz + d = 0$ is parallel to the $x$-axis if and only if $a = 0$.",
    0,
    r"""Reason: true. The plane is parallel to the $x$-axis iff its normal $(a, b, c)$ is perpendicular to $(1, 0, 0)$, i.e. $a = 0$.

Assertion: true. In $(x + y + z - 1) + \lambda(2x + 3y - z + 4) = 0$, the coefficient of $x$ is $1 + 2\lambda$. Setting it to $0$ gives $\lambda = -\tfrac12$:
$$(x + y + z - 1) - \tfrac12(2x + 3y - z + 4) = -\tfrac12 y + \tfrac32 z - 3 = 0 \iff y - 3z + 6 = 0.$$
The reason is the condition used, so it explains the assertion.""")


def check():
    import sympy as sp
    x, y, z, lam, k, t = sp.symbols("x y z lambda k t")
    V = sp.Matrix
    X = V([x, y, z])

    def ang(u, v):
        return sp.acos(sp.Abs(u.dot(v)) / (u.norm() * v.norm()))

    def normal(P):
        P = sp.expand(P)
        return V([P.coeff(x), P.coeff(y), P.coeff(z)])

    def val(P, pt):
        return P.subs({x: pt[0], y: pt[1], z: pt[2]})

    def dist(P, pt):
        return sp.Abs(val(P, pt)) / normal(P).norm()

    def same_plane(P, Q):
        """P = 0 and Q = 0 are the same plane (Q a nonzero multiple of P)."""
        M = V([[sp.expand(P).coeff(v) for v in (x, y, z)] + [sp.expand(P).subs({x: 0, y: 0, z: 0})],
               [sp.expand(Q).coeff(v) for v in (x, y, z)] + [sp.expand(Q).subs({x: 0, y: 0, z: 0})]])
        return M.rank() == 1

    def contains_line(P, P1, P2):
        """P is in the pencil of P1, P2."""
        rows = [[sp.expand(E).coeff(v) for v in (x, y, z)] + [sp.expand(E).subs({x: 0, y: 0, z: 0})] for E in (P, P1, P2)]
        return V(rows).rank() == 2

    def Delta3(F):
        F = sp.expand(F)
        H = sp.hessian(F, (x, y, z)) / 2
        return H.det()

    def is_bisector(B, P1, P2):
        """B is equidistant from P1, P2 (as a plane): signed-distance ratio identity."""
        n1, n2 = normal(P1).norm(), normal(P2).norm()
        return any(same_plane(B, P1 / n1 - s * P2 / n2) for s in (1, -1))

    # q1
    eq(sp.sqrt(3**2 + 4**2 + 12**2), 13, "q1")
    eq((V([4, -2, 15]) - V([1, 2, 3])).norm(), 13, "q1 norm")
    eq(sp.sqrt(9 + 16 + 18**2), sp.sqrt(349), "q1 distractor")
    # q2
    A, B = V([2, -3, 4]), V([8, 0, 10])
    assert (1 * B + 2 * A) / 3 == V([4, -2, 6]), "q2"
    assert (2 * B + 1 * A) / 3 == V([6, -1, 8])
    assert (1 * B - 2 * A) / (1 - 2) == V([-4, -6, -2])
    # q3
    d = V([2, -3, 6]); dc = d / d.norm()
    assert dc == V([sp.Rational(2, 7), sp.Rational(-3, 7), sp.Rational(6, 7)]), "q3"
    eq(sum(c**2 for c in dc), 1, "q3 unit")
    eq(sum((c / 5)**2 for c in d), sp.Rational(49, 25), "q3 distractor")
    # q4
    eq(ang(V([1, 1, 2]), V([sp.sqrt(3) - 1, -sp.sqrt(3) - 1, 4])), sp.pi / 3, "q4")
    # q5
    F5 = x**2 - 2*y**2 + z**2 - x*y - y*z + lam*z*x
    roots = sp.solve(Delta3(F5), lam)
    assert set(roots) == {2, sp.Rational(-5, 2)}, roots
    assert [r for r in roots if r > 0] == [2], "q5"
    eq(sp.expand((x + y + z) * (x - 2*y + z)), F5.subs(lam, 2), "q5 factor")
    for wrong in (sp.Rational(5, 2), 4, 1):
        assert Delta3(F5.subs(lam, wrong)) != 0
    # q6
    PQ = V([5, 2, -4]) - V([3, -1, 2]); u = V([2, -6, 3]) / 7
    eq(sp.Abs(PQ.dot(u)), sp.Rational(32, 7), "q6")
    eq(PQ.norm(), 7, "q6 distractor PQ")
    # q7
    eq(ang(V([1, 1, 1]), V([-1, 1, 1])), sp.acos(sp.Rational(1, 3)), "q7")
    eq(ang(V([1, 1, 1]), V([1, 0, 0])), sp.acos(1 / sp.sqrt(3)), "q7 edge")
    eq(ang(V([1, 1, 1]), V([1, 1, 0])), sp.acos(sp.sqrt(sp.Rational(2, 3))), "q7 face")
    # q8
    P8 = 2*x - 3*y + 4*z - 12
    assert [sp.solve(P8.subs({y: 0, z: 0}), x)[0], sp.solve(P8.subs({x: 0, z: 0}), y)[0],
            sp.solve(P8.subs({x: 0, y: 0}), z)[0]] == [6, -4, 3], "q8"
    # q9
    P9 = 2*x - y + 2*z + 9
    N9 = -sp.Rational(2, 3)*x + sp.Rational(1, 3)*y - sp.Rational(2, 3)*z - 3
    assert same_plane(P9, N9), "q9 same plane"
    eq(normal(N9).norm(), 1, "q9 unit"); eq(dist(P9, (0, 0, 0)), 3, "q9 p")
    assert not same_plane(P9, sp.Rational(2, 3)*x - sp.Rational(1, 3)*y + sp.Rational(2, 3)*z - 3)
    assert not same_plane(P9, N9 + 2)
    # q10
    A, B, C = V([2, 1, 0]), V([3, -2, -2]), V([3, 1, 7])
    n = (B - A).cross(C - A)
    P10 = n.dot(X - A)
    assert same_plane(P10, 7*x + 3*y - z - 17), "q10"
    for wrong in (7*x + 3*y - z - 14, 7*x - 3*y - z - 11, 7*x + 3*y + z - 17):
        assert not all(val(wrong, p) == 0 for p in (A, B, C))
    # q11
    A, B, C = V([0, -1, 0]), V([2, 1, -1]), V([1, 1, 1])
    D = V([4, 5, k])
    sol = sp.solve(V.hstack(B - A, C - A, D - A).det(), k)
    assert sol == [1], "q11"
    assert same_plane((B - A).cross(C - A).dot(X - A), 4*x - 3*y + 2*z - 3), "q11 plane"
    # q12
    eq(dist(x + 2*y - 2*z - 9, (2, 3, -5)), 3, "q12")
    # q13
    p1, p2 = 2*x - 2*y + z + 3, 4*x - 4*y + 2*z + 5
    pt = (0, 0, -3)  # on p1
    eq(val(p1, pt), 0, "q13 pt"); eq(dist(p2, pt), sp.Rational(1, 6), "q13")
    # q14
    eq(ang(V([2, -1, 2]), V([1, -1, 0])), sp.pi / 4, "q14")
    # q15
    P15 = 2*x - y + z + 3
    P0 = V([1, 3, 4]); nn = normal(P15)
    tt = val(P15, P0) / nn.dot(nn)
    img = P0 - 2 * tt * nn; foot = P0 - tt * nn
    assert img == V([-3, 5, 2]) and foot == V([-1, 4, 3]), "q15"
    eq(val(P15, (P0 + img) / 2), 0, "q15 midpoint")
    assert (img - P0).cross(nn) == V([0, 0, 0]), "q15 perpendicular"
    # q16
    Q1, Q2 = x + y + z - 6, 2*x + 3*y + 4*z + 5
    ans = 20*x + 23*y + 26*z - 69
    assert contains_line(ans, Q1, Q2) and val(ans, (1, 1, 1)) == 0, "q16"
    for wrong in (20*x + 23*y + 26*z + 69, 8*x + 5*y + 2*z - 99, x + y + z - 3):
        assert not (contains_line(wrong, Q1, Q2) and val(wrong, (1, 1, 1)) == 0)
    # q17
    Q1, Q2 = x + 2*y + 3*z - 4, 2*x + y - z + 5
    ans = 51*x + 15*y - 50*z + 173
    assert contains_line(ans, Q1, Q2), "q17 pencil"
    eq(normal(ans).dot(V([5, 3, 6])), 0, "q17 perp")
    lsol = sp.solve(normal(Q1 + lam*Q2).dot(V([5, 3, 6])), lam); assert lsol == [sp.Rational(-29, 7)]
    for wrong in (65*x + 43*y - 8*z + 117, 51*x + 15*y - 50*z - 173, 51*x - 15*y + 50*z + 173):
        assert not (contains_line(wrong, Q1, Q2) and normal(wrong).dot(V([5, 3, 6])) == 0)
    # q18
    P1, P2 = 2*x - y + 2*z + 3, 3*x - 2*y + 6*z + 8
    b_plus, b_minus = 5*x - y - 4*z - 3, 23*x - 13*y + 32*z + 45
    assert same_plane(7*P1 - 3*P2, b_plus) and same_plane(7*P1 + 3*P2, b_minus), "q18"
    assert is_bisector(b_plus, P1, P2) and is_bisector(b_minus, P1, P2)
    # origin side: signed distances of O agree in sign on the + bisector region
    assert val(P1, (0, 0, 0)) > 0 and val(P2, (0, 0, 0)) > 0
    for wrong in (x - y + 4*z + 5, 5*x - y - 4*z + 3):
        assert not is_bisector(wrong, P1, P2)
    # q19 and q27: acute vs obtuse bisector, by the angle between normals (< pi/4 means acute)
    def acute_bisector(B, P1):
        return sp.N(ang(normal(B), normal(P1))) < sp.N(sp.pi / 4)
    assert not acute_bisector(b_plus, P1) and acute_bisector(b_minus, P1), "q27 (+ is obtuse)"
    assert normal(P1).dot(normal(P2)) == 20
    R1, R2 = 2*x - y + 2*z + 3, 2*x + 3*y - 6*z + 14
    c_plus, c_minus = 8*x - 16*y + 32*z - 21, 20*x + 2*y - 4*z + 63
    assert same_plane(7*R1 - 3*R2, c_plus) and same_plane(7*R1 + 3*R2, c_minus), "q19"
    assert is_bisector(c_plus, R1, R2) and is_bisector(c_minus, R1, R2)
    assert acute_bisector(c_plus, R1) and not acute_bisector(c_minus, R1), "q19 acute"
    assert normal(R1).dot(normal(R2)) == -11
    for wrong in (8*x - 16*y + 32*z + 21, 20*x + 2*y - 4*z - 63):
        assert not is_bisector(wrong, R1, R2)
    # q20
    al, be, ga = 4 * 1, 4 * 2, 4 * 3
    P20 = x / al + y / be + z / ga - 1
    assert same_plane(P20, 6*x + 3*y + 2*z - 24), "q20"
    assert same_plane(x / 3 + y / 6 + z / 9 - 1, 6*x + 3*y + 2*z - 18), "q20 triangle distractor"
    # q21
    p, X0, Y0, Z0 = sp.symbols("p X0 Y0 Z0", positive=True)
    a_, b_, c_ = 3 * X0, 3 * Y0, 3 * Z0
    planeE = x / a_ + y / b_ + z / c_ - 1
    dist0 = 1 / sp.sqrt(1 / a_**2 + 1 / b_**2 + 1 / c_**2)
    eq(dist(planeE, (0, 0, 0)), dist0, "q21 distance")
    eq(sp.simplify(1 / dist0**2), (X0**-2 + Y0**-2 + Z0**-2) / 9, "q21 locus")
    # numeric instance: plane x + 2y + 2z = 6 (p = 2), centroid (2, 1, 1)
    eq(dist(x + 2*y + 2*z - 6, (0, 0, 0)), 2, "q21 p")
    eq(sp.Rational(1, 4) + 1 + 1, sp.Rational(9, 4), "q21 numeric 9/p^2")
    # q22
    def cos2sum(a1, a2, a3):
        return sum(sp.cos(sp.rad(v))**2 for v in (a1, a2, a3))
    eq(cos2sum(45, 60, 120), 1, "q22 s1")
    eq(cos2sum(30, 45, 60), sp.Rational(3, 2), "q22 s2 false")
    l, m, n = sp.symbols("l m n", real=True)
    eq(3 * (l**2 + m**2 + n**2) - (l + m + n)**2, (l - m)**2 + (m - n)**2 + (n - l)**2, "q22 s3 identity")
    # q23
    Pi = x + 2*y - 3*z + 1
    assert val(Pi, (1, 1, 1)) == 1 and val(Pi, (2, -1, 0)) == 1, "q23 s1 false"
    eq(normal(Pi).dot(V([3, 3, 3])), 0, "q23 s2")
    eq(dist(2*x + 4*y - 6*z + 9, (-1, 0, 0)), sp.sqrt(14) / 4, "q23 s3")
    eq(val(Pi, (-1, 0, 0)), 0, "q23 s3 pt")
    # q24
    P24 = 2*x + 3*y + 6*z - 14
    eq(dist(P24, (0, 0, 0)), 2, "q24 A"); assert sp.solve(P24.subs({y: 0, z: 0}), x) == [7], "q24 B"
    eq(normal(P24)[2] / normal(P24).norm(), sp.Rational(6, 7), "q24 C")
    eq(dist(P24, (1, 1, 1)), sp.Rational(3, 7), "q24 D")
    # q25 and q29
    def pair_angle(F):
        F = sp.expand(F)
        a, b, c = F.coeff(x, 2), F.coeff(y, 2), F.coeff(z, 2)
        f2, g2, h2 = F.coeff(y).coeff(z), F.coeff(z).coeff(x), F.coeff(x).coeff(y)
        f, g, h = f2 / 2, g2 / 2, h2 / 2
        if a + b + c == 0:
            return sp.pi / 2
        return sp.atan(sp.Abs(2 * sp.sqrt(f**2 + g**2 + h**2 - a*b - b*c - c*a) / (a + b + c)))
    pairs = {"A": ((x - y), (x + y), sp.pi / 2), "B": (z, (z + y), sp.pi / 4),
             "C": ((x + y), (y + z), sp.pi / 3), "D": (x, (sp.sqrt(3)*x + y), sp.pi / 6)}
    given = {"A": x**2 - y**2, "B": z**2 + y*z, "C": y**2 + x*y + y*z + z*x, "D": sp.sqrt(3)*x**2 + x*y}
    for key, (L1, L2, want) in pairs.items():
        eq(sp.expand(L1 * L2), given[key], f"q25 {key} factor")
        eq(Delta3(given[key]), 0, f"q25 {key} Delta")
        eq(ang(normal(L1), normal(L2)), want, f"q25 {key} angle")
        eq(pair_angle(given[key]), want, f"q25 {key} formula")
    # q26
    eq(3 * sp.Rational(1, 4), sp.Rational(3, 4), "q26"); assert sp.Rational(3, 4) != 1
    # q28
    S = x + y + z - 1
    assert val(S, (1, -1, 2)) == 1 and val(S, (2, 1, 1)) == 3, "q28 A"
    nS = normal(S) / normal(S).norm()
    assert nS[0] == nS[1] == nS[2], "q28 R"
    # q29
    F29 = x**2 - 2*y**2 + z**2 - x*y - y*z + 2*z*x
    eq(sp.expand((x + y + z) * (x - 2*y + z)), F29, "q29 factor")
    eq(V([1, 1, 1]).dot(V([1, -2, 1])), 0, "q29 perp")
    eq(Delta3(x**2 + y**2 - z**2), -1, "q29 R counterexample")
    # q30
    U1, U2 = x + y + z - 1, 2*x + 3*y - z + 4
    lsol = sp.solve(normal(U1 + lam*U2)[0], lam); assert lsol == [sp.Rational(-1, 2)]
    assert same_plane(U1 + lsol[0]*U2, y - 3*z + 6), "q30"
    assert contains_line(y - 3*z + 6, U1, U2)


T.write(check)
