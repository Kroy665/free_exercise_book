# 3D Coordinates and Planes

## Coordinates, distance and section formula {#coordinates}

Fix three mutually perpendicular axes $OX$, $OY$, $OZ$ (right-handed). A point $P$ has coordinates $(x, y, z)$: its signed distances from the $yz$-, $zx$- and $xy$-planes. The three coordinate planes cut space into **eight octants**; the signs of $(x, y, z)$ tell you the octant.

- On the $x$-axis: $y = z = 0$. On the $yz$-plane: $x = 0$.
- The foot of the perpendicular from $P(x, y, z)$ to the $x$-axis is $(x, 0, 0)$, so the distance of $P$ from the $x$-axis is $\sqrt{y^2 + z^2}$.

**Distance.** For $P(x_1, y_1, z_1)$ and $Q(x_2, y_2, z_2)$,

$$PQ = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2}.$$

Example: $(1, 2, 3)$ to $(4, -2, 15)$: the differences are $3, -4, 12$, so $PQ = \sqrt{9 + 16 + 144} = 13$.

**Section formula.** The point dividing $PQ$ in the ratio $m : n$ is

$$\left(\frac{mx_2 + nx_1}{m + n},\ \frac{my_2 + ny_1}{m + n},\ \frac{mz_2 + nz_1}{m + n}\right),$$

internally for $m, n > 0$; for external division replace $n$ by $-n$. The **ratio in which a coordinate plane divides** $PQ$ comes from setting that coordinate to $0$: the $yz$-plane divides $PQ$ in the ratio $-x_1 : x_2$ (internally when $x_1, x_2$ have opposite signs).

**Centroids.**
- Triangle $ABC$: $G = \tfrac13(A + B + C)$ (coordinate-wise).
- Tetrahedron $ABCD$: $G = \tfrac14(A + B + C + D)$. It is the common point of the four lines joining each vertex to the centroid of the opposite face, and it divides each such line in the ratio $3 : 1$.

**Volume of a tetrahedron** with vertices $(x_i, y_i, z_i)$, $i = 1, \dots, 4$:

$$V = \frac16\left\lvert\det\begin{pmatrix} x_1 & y_1 & z_1 & 1\\ x_2 & y_2 & z_2 & 1\\ x_3 & y_3 & z_3 & 1\\ x_4 & y_4 & z_4 & 1\end{pmatrix}\right\rvert.$$

The four points are **coplanar** exactly when this determinant is $0$; equivalently, the $3 \times 3$ determinant of the vectors $\vec{AB}, \vec{AC}, \vec{AD}$ is $0$.

:::caution
For external division the denominators become $m - n$, not $m + n$. A negative ratio from "set the coordinate to zero" means the plane cuts $PQ$ **produced**, i.e. externally.
:::

## Direction cosines, angle between lines and projection {#direction-cosines}

If a directed line makes angles $\alpha, \beta, \gamma$ with $OX, OY, OZ$, its **direction cosines** (d.c.s) are

$$l = \cos\alpha, \quad m = \cos\beta, \quad n = \cos\gamma, \qquad l^2 + m^2 + n^2 = 1.$$

Reversing the line changes all three signs. Any triple $a, b, c$ proportional to $l, m, n$ is a set of **direction ratios** (d.r.s), and

$$l, m, n = \pm\frac{a}{\sqrt{a^2 + b^2 + c^2}},\ \pm\frac{b}{\sqrt{a^2 + b^2 + c^2}},\ \pm\frac{c}{\sqrt{a^2 + b^2 + c^2}}$$

(same sign throughout). The d.r.s of $PQ$ are $x_2 - x_1,\ y_2 - y_1,\ z_2 - z_1$.

Consequences of $\sum\cos^2\alpha = 1$: $\sum\sin^2\alpha = 2$ and $\sum\cos 2\alpha = -1$. A line equally inclined to the axes has $l = m = n = \pm\frac{1}{\sqrt3}$; no line makes $60^\circ$ with all three axes, since $3 \cdot \tfrac14 \ne 1$.

**Angle between two lines** with d.c.s $(l_1, m_1, n_1)$ and $(l_2, m_2, n_2)$:

$$\cos\theta = l_1l_2 + m_1m_2 + n_1n_2, \qquad \sin^2\theta = \sum (m_1n_2 - m_2n_1)^2.$$

With d.r.s, $\cos\theta = \dfrac{a_1a_2 + b_1b_2 + c_1c_2}{\sqrt{\sum a_1^2}\sqrt{\sum a_2^2}}$.

- **Perpendicular:** $a_1a_2 + b_1b_2 + c_1c_2 = 0$.
- **Parallel:** $a_1 : b_1 : c_1 = a_2 : b_2 : c_2$.
- A line perpendicular to both has d.r.s $b_1c_2 - b_2c_1,\ c_1a_2 - c_2a_1,\ a_1b_2 - a_2b_1$ (the cross product).

Example: the diagonals of a unit cube have d.r.s $(1, 1, 1)$ and $(-1, 1, 1)$, so $\cos\theta = \tfrac13$. A diagonal and an edge give $\cos\theta = \tfrac{1}{\sqrt3}$.

**Projection.** The projection of the segment $PQ$ on a line with d.c.s $l, m, n$ is

$$(x_2 - x_1)l + (y_2 - y_1)m + (z_2 - z_1)n,$$

i.e. $PQ\cos\theta$. Use d.c.s, not raw d.r.s. The projection of $PQ$ on a **plane** has length $PQ\sin\theta$, where $\theta$ is the angle between $PQ$ and the normal. A plane area $A$ projects onto a plane at angle $\theta$ as $A\lvert\cos\theta\rvert$, and $A^2 = A_{yz}^2 + A_{zx}^2 + A_{xy}^2$.

:::exam-tip
Before using a projection formula, divide the d.r.s by their length. Projecting $(2, 3, -6)$ on d.r.s $(2, -6, 3)$ gives $\tfrac{4 - 18 - 18}{7} = -\tfrac{32}{7}$, not $-32$.
:::

## Forms of the equation of a plane {#plane-forms}

Every first-degree equation $ax + by + cz + d = 0$ ($a, b, c$ not all zero) is a plane, and every plane has such an equation. The coefficients $a, b, c$ are **direction ratios of the normal**.

| Form | Equation | Data |
|:---|:---|:---|
| General | $ax + by + cz + d = 0$ | normal d.r.s $a, b, c$ |
| Point–normal | $a(x - x_1) + b(y - y_1) + c(z - z_1) = 0$ | through $(x_1, y_1, z_1)$ |
| Intercept | $\dfrac{x}{\alpha} + \dfrac{y}{\beta} + \dfrac{z}{\gamma} = 1$ | cuts the axes at $\alpha, \beta, \gamma$ |
| Normal | $lx + my + nz = p$, $\ p \ge 0$ | $l, m, n$ d.c.s of the normal from $O$; $p$ = distance from $O$ |
| Three-point | $\det\begin{pmatrix} x - x_1 & y - y_1 & z - z_1\\ x_2 - x_1 & y_2 - y_1 & z_2 - z_1\\ x_3 - x_1 & y_3 - y_1 & z_3 - z_1\end{pmatrix} = 0$ | through three non-collinear points |

**To the normal form.** Move $d$ to the right so the right side is $-d$, and divide by $\sqrt{a^2 + b^2 + c^2}$ with the sign that makes the right side **non-negative**. For $2x - y + 2z + 9 = 0$: $2x - y + 2z = -9$; divide by $-3$:

$$-\tfrac23 x + \tfrac13 y - \tfrac23 z = 3, \qquad p = 3.$$

**Intercepts.** For $2x - 3y + 4z = 12$: divide by $12$, giving $\frac{x}{6} + \frac{y}{-4} + \frac{z}{3} = 1$; the intercepts are $6, -4, 3$. The tetrahedron cut off from the axes has volume $\tfrac16\lvert\alpha\beta\gamma\rvert$.

**Three points.** Through $A(2, 1, 0)$, $B(3, -2, -2)$, $C(3, 1, 7)$: $\vec{AB} = (1, -3, -2)$, $\vec{AC} = (1, 0, 7)$, and $\vec{AB} \times \vec{AC} = (-21, -9, 3) \parallel (7, 3, -1)$. So

$$7(x - 2) + 3(y - 1) - z = 0 \iff 7x + 3y - z = 17.$$

Check by substituting $B$ and $C$.

**Special positions.** A missing variable means the plane is parallel to that axis: $by + cz + d = 0$ is parallel to the $x$-axis. A missing constant means the plane passes through $O$. $z = k$ is parallel to the $xy$-plane.

:::caution
In the normal form, $p$ must be $\ge 0$. Dividing $2x - y + 2z + 9 = 0$ by $+3$ gives $\tfrac23x - \tfrac13y + \tfrac23z = -3$, which is **not** in normal form; changing $-3$ to $3$ without flipping the other signs gives a different plane.
:::

## Distance, sides and angle between planes {#distance-angle}

Let $\Pi : ax + by + cz + d = 0$ and $P(x_1, y_1, z_1)$. The **signed distance** of $P$ from $\Pi$ is

$$\delta = \frac{ax_1 + by_1 + cz_1 + d}{\sqrt{a^2 + b^2 + c^2}}, \qquad \text{distance} = \lvert\delta\rvert.$$

**Sides of a plane.** Two points lie on the **same side** of $\Pi$ iff $ax + by + cz + d$ has the same sign at both; on opposite sides iff the signs differ. The origin's side is the side where the expression has the sign of $d$.

**Parallel planes** $ax + by + cz + d_1 = 0$ and $ax + by + cz + d_2 = 0$ (same $a, b, c$!) are at distance

$$\frac{\lvert d_1 - d_2\rvert}{\sqrt{a^2 + b^2 + c^2}}.$$

For $2x - 2y + z + 3 = 0$ and $4x - 4y + 2z + 5 = 0$, first halve the second: $d_2 = \tfrac52$, distance $\dfrac{\lvert 3 - \tfrac52\rvert}{3} = \tfrac16$.

**Foot and image.** The foot $N$ of the perpendicular from $P$ and the image $P'$ of $P$ in $\Pi$ are

$$N = P - t\,(a, b, c), \quad P' = P - 2t\,(a, b, c), \qquad t = \frac{ax_1 + by_1 + cz_1 + d}{a^2 + b^2 + c^2}.$$

Example: $P(1, 3, 4)$ in $2x - y + z + 3 = 0$: $t = \tfrac{6}{6} = 1$, so $N = (-1, 4, 3)$ and $P' = (-3, 5, 2)$.

**Angle between two planes** = angle between their normals:

$$\cos\theta = \frac{\lvert a_1a_2 + b_1b_2 + c_1c_2\rvert}{\sqrt{\sum a_1^2}\sqrt{\sum a_2^2}} \quad (\text{acute angle}).$$

- **Perpendicular planes:** $a_1a_2 + b_1b_2 + c_1c_2 = 0$.
- **Parallel planes:** $a_1 : b_1 : c_1 = a_2 : b_2 : c_2$.

Example: $2x - y + 2z = 5$ and $x - y = 3$: $\cos\theta = \tfrac{3}{3\sqrt2}$, so $\theta = \tfrac{\pi}{4}$.

The angle between a **line** and a plane is the complement of the angle between the line and the normal; lines in space are treated in the next topic.

**Variable plane at distance $p$ from $O$.** If it meets the axes at $A(\alpha, 0, 0)$, $B$, $C$, then $\tfrac{1}{\alpha^2} + \tfrac{1}{\beta^2} + \tfrac{1}{\gamma^2} = \tfrac{1}{p^2}$. The centroid of $\triangle ABC$ is $(\alpha/3, \beta/3, \gamma/3)$, so its locus is $x^{-2} + y^{-2} + z^{-2} = 9p^{-2}$; for the tetrahedron $OABC$ the centroid is $(\alpha/4, \dots)$ and the constant is $16p^{-2}$.

:::exam-tip
Before using the parallel-plane distance, make the $x, y, z$ coefficients **identical**, not just proportional.
:::

## Planes through the intersection of two planes {#family}

Let $P_1 \equiv a_1x + b_1y + c_1z + d_1$ and $P_2 \equiv a_2x + b_2y + c_2z + d_2$ be non-parallel. Every plane through the line $P_1 = 0 = P_2$ is

$$P_1 + \lambda P_2 = 0 \qquad (\lambda \in \R),$$

except $P_2 = 0$ itself (the value $\lambda = \infty$). Fix $\lambda$ by the one extra condition:

| Extra condition | Equation for $\lambda$ |
|:---|:---|
| passes through $(x_1, y_1, z_1)$ | $P_1(x_1, y_1, z_1) + \lambda P_2(x_1, y_1, z_1) = 0$ |
| perpendicular to $ax + by + cz + d = 0$ | $a(a_1 + \lambda a_2) + b(b_1 + \lambda b_2) + c(c_1 + \lambda c_2) = 0$ |
| parallel to the $x$-axis | $a_1 + \lambda a_2 = 0$ |
| passes through $O$ | $d_1 + \lambda d_2 = 0$ |

**Example 1.** Through the line $x + y + z = 6$, $2x + 3y + 4z + 5 = 0$ and the point $(1, 1, 1)$:

$$(x + y + z - 6) + \lambda(2x + 3y + 4z + 5) = 0, \quad -3 + 14\lambda = 0, \quad \lambda = \tfrac{3}{14}.$$

Multiplying by $14$: $20x + 23y + 26z - 69 = 0$.

**Example 2.** Through the line $x + 2y + 3z - 4 = 0$, $2x + y - z + 5 = 0$ and perpendicular to $5x + 3y + 6z + 8 = 0$. The normal is $(1 + 2\lambda, 2 + \lambda, 3 - \lambda)$, and

$$5(1 + 2\lambda) + 3(2 + \lambda) + 6(3 - \lambda) = 29 + 7\lambda = 0 \Rightarrow \lambda = -\tfrac{29}{7}.$$

Then $7(x + 2y + 3z - 4) - 29(2x + y - z + 5) = 0$, i.e. $51x + 15y - 50z + 173 = 0$.

**Example 3.** Through $x + y + z = 1$, $2x + 3y - z + 4 = 0$ and parallel to the $x$-axis: $1 + 2\lambda = 0$, so $\lambda = -\tfrac12$, giving $y - 3z + 6 = 0$.

The same idea gives the plane through a given line and a given point; three planes have a common line iff one equation is a linear combination of the other two.

:::caution
A sign slip in $\lambda$ still gives a plane through the common line, so substituting points of the line will not catch it. Check the **extra** condition (the point, or the perpendicularity) in your final answer.
:::

## Bisector planes {#bisectors}

The planes bisecting the angles between $P_1 \equiv a_1x + b_1y + c_1z + d_1 = 0$ and $P_2 \equiv a_2x + b_2y + c_2z + d_2 = 0$ are the loci of points equidistant from them:

$$\frac{a_1x + b_1y + c_1z + d_1}{\sqrt{a_1^2 + b_1^2 + c_1^2}} = \pm\,\frac{a_2x + b_2y + c_2z + d_2}{\sqrt{a_2^2 + b_2^2 + c_2^2}}.$$

The two bisector planes are perpendicular to each other.

**Which is which.** First write both equations with $d_1, d_2$ **positive** (multiply by $-1$ if needed). Then:

:::keyfacts
- The **$+$ sign** gives the bisector of the angle **containing the origin**.
- If $a_1a_2 + b_1b_2 + c_1c_2 > 0$, the origin lies in the **obtuse** angle, so the $+$ bisector is the obtuse one.
- If $a_1a_2 + b_1b_2 + c_1c_2 < 0$, the origin lies in the **acute** angle, so the $+$ bisector is the acute one.
:::

**Reason.** With $d_1, d_2 > 0$, the origin lies in the region $\{P_1 > 0,\ P_2 > 0\}$, and the $+$ sign gives exactly the points where the signed distances agree in sign. The normals $n_1 = (a_1, b_1, c_1)$ and $n_2$ point into this region, so the region's dihedral angle is $\pi$ minus the angle between $n_1$ and $n_2$. Hence $n_1 \cdot n_2 > 0$ makes the origin's region obtuse.

**Example 1.** $2x - y + 2z + 3 = 0$ and $3x - 2y + 6z + 8 = 0$ (norms $3$ and $7$, $d$'s positive):

$$7(2x - y + 2z + 3) = \pm 3(3x - 2y + 6z + 8).$$

- $+$: $5x - y - 4z - 3 = 0$, bisecting the angle containing $O$.
- $-$: $23x - 13y + 32z + 45 = 0$.

Here $a_1a_2 + b_1b_2 + c_1c_2 = 6 + 2 + 12 = 20 > 0$, so the origin's angle is obtuse and the **acute** bisector is $23x - 13y + 32z + 45 = 0$.

**Check without the rule.** A bisector makes the angle $\theta/2$ with each plane. Compute the angle between the bisector's normal and $n_1$: if it is less than $45^\circ$ the bisector lies in the acute angle (it is "close" to the planes on the acute side).

**Example 2.** $2x - y + 2z + 3 = 0$ and $2x + 3y - 6z + 14 = 0$: $n_1 \cdot n_2 = 4 - 3 - 12 = -11 < 0$, so the $+$ bisector $7(2x - y + 2z + 3) = 3(2x + 3y - 6z + 14)$, i.e. $8x - 16y + 32z - 21 = 0$, bisects the acute angle (which contains $O$).

:::caution
Forgetting to divide by the norms gives a plane through the common line, but not a bisector. And the sign test works only after both constants are made positive.
:::

## Pair of planes {#pair-of-planes}

A homogeneous second-degree equation

$$F \equiv ax^2 + by^2 + cz^2 + 2fyz + 2gzx + 2hxy = 0$$

represents a **pair of planes through the origin** iff $F$ factorises into two linear factors (possibly complex). The condition is

$$\Delta = \det\begin{pmatrix} a & h & g\\ h & b & f\\ g & f & c\end{pmatrix} = abc + 2fgh - af^2 - bg^2 - ch^2 = 0.$$

$\Delta = 0$ guarantees two planes, which may be imaginary; when $\Delta \ne 0$, $F = 0$ is a cone (e.g. $x^2 + y^2 - z^2 = 0$), not a pair of planes. So not every homogeneous quadratic in $x, y, z$ is a pair of planes, unlike the two-variable case.

**Angle.** If $F = (a_1x + b_1y + c_1z)(a_2x + b_2y + c_2z)$, then $a = a_1a_2$, $2f = b_1c_2 + b_2c_1$, and so on, and $\lvert n_1 \times n_2\rvert^2 = 4(f^2 + g^2 + h^2 - bc - ca - ab)$. Hence

$$\tan\theta = \frac{2\sqrt{f^2 + g^2 + h^2 - ab - bc - ca}}{a + b + c}.$$

- **Perpendicular planes:** $a + b + c = 0$ (given that $F = 0$ is a pair of planes).
- If $z$ is absent, $ax^2 + 2hxy + by^2 = 0$ is a pair of planes through the $z$-axis, with the same angle as the pair of lines in the $xy$-plane.

**Example.** $x^2 - 2y^2 + z^2 - xy - yz + \lambda zx = 0$:

$$\Delta = -2 + \tfrac{\lambda}{4} - \tfrac14 + \tfrac{\lambda^2}{2} - \tfrac14 = \tfrac14(2\lambda^2 + \lambda - 10) = \tfrac14(\lambda - 2)(2\lambda + 5).$$

For $\lambda = 2$ the equation factorises as $(x + y + z)(x - 2y + z) = 0$, and $a + b + c = 1 - 2 + 1 = 0$: the planes are perpendicular.

**Factorising.** Treat $F$ as a quadratic in $x$ and complete the square; when $\Delta = 0$ the discriminant is a perfect square in $y, z$.

The general second-degree equation in $x, y, z$ (quadrics) and the sphere are separate topics.

## Quick checks and traps {#exam-tips}

- **Direction cosines:** $l^2 + m^2 + n^2 = 1$, so $\sum\sin^2 = 2$ and $\sum\cos 2\alpha = -1$. Test any three given angles with this.
- **D.c.s from d.r.s:** divide by $\sqrt{a^2 + b^2 + c^2}$, never by $a + b + c$.
- **Angle between lines or planes:** $\cos\theta = \dfrac{\lvert n_1 \cdot n_2\rvert}{\lvert n_1\rvert\lvert n_2\rvert}$. Perpendicular: dot product $0$.
- **Cube:** two body diagonals, $\cos^{-1}\tfrac13$; diagonal and edge, $\cos^{-1}\tfrac{1}{\sqrt3}$; diagonal and face diagonal, $\cos^{-1}\sqrt{\tfrac23}$.
- **Normal form:** make the constant on the right **non-negative**; then $p$ is the distance from $O$.
- **Distance from a plane:** $\dfrac{\lvert ax_1 + by_1 + cz_1 + d\rvert}{\sqrt{a^2 + b^2 + c^2}}$. Watch the sign of each substituted term.
- **Parallel planes:** equalise the coefficients first, then $\dfrac{\lvert d_1 - d_2\rvert}{\sqrt{a^2 + b^2 + c^2}}$.
- **Image of a point:** twice the step to the foot. A quick check: the midpoint of $PP'$ lies on the plane.
- **Centroid given:** triangle $ABC$ on the axes with centroid $(x_0, y_0, z_0)$ gives intercepts $3x_0, 3y_0, 3z_0$; tetrahedron $OABC$ gives $4x_0, 4y_0, 4z_0$.
- **Family of planes:** $P_1 + \lambda P_2 = 0$; parallel to the $x$-axis means coefficient of $x$ is $0$.
- **Bisectors:** make $d_1, d_2 > 0$; the $+$ sign contains $O$; $n_1 \cdot n_2 > 0$ means that one is obtuse.
- **Pair of planes:** $\Delta = 0$; perpendicular iff $a + b + c = 0$.
