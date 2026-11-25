# The Sphere

## General equation, centre and radius {#general-equation}

A **sphere** is the locus of points at a fixed distance $r$ (the radius) from a fixed point $C(a, b, c)$ (the centre):

$$(x - a)^2 + (y - b)^2 + (z - c)^2 = r^2.$$

Expanding gives the **general equation**

$$S \equiv x^2 + y^2 + z^2 + 2ux + 2vy + 2wz + d = 0,$$

with

$$\text{centre } (-u, -v, -w), \qquad \text{radius } \sqrt{u^2 + v^2 + w^2 - d}.$$

| $u^2 + v^2 + w^2 - d$ | The equation represents |
|:---|:---|
| $> 0$ | a real sphere |
| $= 0$ | a **point sphere** (only the centre) |
| $< 0$ | no real point (a "virtual" sphere) |

**When is a second-degree equation a sphere?** The equation

$$ax^2 + by^2 + cz^2 + 2fyz + 2gzx + 2hxy + 2ux + 2vy + 2wz + d = 0$$

represents a sphere (possibly a point or virtual sphere) if and only if

$$a = b = c \neq 0 \quad\text{and}\quad f = g = h = 0.$$

Then divide through by $a$ to get the standard form. The general equation has **four** independent constants $u, v, w, d$, so four independent conditions fix a sphere (for example, four non-coplanar points).

**Example.** $2x^2 + 2y^2 + 2z^2 - 4x + 8y - 12z - 2 = 0$. Divide by 2:

$$x^2 + y^2 + z^2 - 2x + 4y - 6z - 1 = 0,$$

so the centre is $(1, -2, 3)$ and the radius is $\sqrt{1 + 4 + 9 + 1} = \sqrt{15}$.

**Position of a point.** With $S$ in standard form (coefficient of $x^2$ equal to $1$), let $S_1 = S(x_1, y_1, z_1)$. Then $S_1 = CP^2 - r^2$, so $P$ is inside, on or outside the sphere according as $S_1 < 0$, $= 0$ or $> 0$.

:::caution
Read the centre and radius **only after** making the coefficient of $x^2$ equal to $1$. In $2x^2 + 2y^2 + 2z^2 - 4x + \dots$ the centre has $x$-coordinate $1$, not $2$. The centre is $(-u, -v, -w)$: half the coefficient of $x$, with the **sign changed**.
:::

:::exam-tip
A cross term such as $xy$ or unequal squared coefficients rule out a sphere at once. For instance, $x^2 + y^2 + z^2 + 2xy = 1$ is $(x + y)^2 + z^2 = 1$, a cylinder.
:::

## Spheres from given data {#given-data}

**Sphere on a diameter.** If $A(x_1, y_1, z_1)$ and $B(x_2, y_2, z_2)$ are ends of a diameter, then $P$ lies on the sphere iff $\angle APB = \frac\pi2$, i.e. $\vec{PA}\cdot\vec{PB} = 0$:

$$(x - x_1)(x - x_2) + (y - y_1)(y - y_2) + (z - z_1)(z - z_2) = 0.$$

Its centre is the midpoint of $AB$, and its radius is $\frac12 AB$.

**Sphere through four points.** Substitute each point in $x^2 + y^2 + z^2 + 2ux + 2vy + 2wz + d = 0$ and solve the four linear equations for $u, v, w, d$. A unique sphere exists iff the four points are **not coplanar**. (Four coplanar points lie on at most a circle, and then on infinitely many spheres, or on none.)

**Through the origin and three axis points.** The sphere through $O$, $(a, 0, 0)$, $(0, b, 0)$ and $(0, 0, c)$ is

$$x^2 + y^2 + z^2 - ax - by - cz = 0,$$

with centre $\left(\frac a2, \frac b2, \frac c2\right)$ and radius $\frac12\sqrt{a^2 + b^2 + c^2}$. Here $d = 0$ because the sphere passes through $O$, and each axis point then gives $a^2 + 2ua = 0$.

**Given centre, touching a plane.** The radius is the perpendicular distance from the centre to the plane. For centre $(1, 2, 3)$ and plane $2x - y + 2z = 15$:

$$r = \frac{\lvert 2 - 2 + 6 - 15\rvert}{3} = 3, \qquad x^2 + y^2 + z^2 - 2x - 4y - 6z + 5 = 0.$$

**Touching a plane at a given point.** A sphere touching the plane $P = 0$ at $A(\alpha, \beta, \gamma)$ is

$$(x - \alpha)^2 + (y - \beta)^2 + (z - \gamma)^2 + \lambda P = 0,$$

the point sphere at $A$ plus $\lambda$ times the plane. One more condition (a point, or the radius) fixes $\lambda$.

**Example.** The sphere through $O$ touching $x + y + z = 3$ at $(1, 1, 1)$: at $O$, $3 + \lambda(-3) = 0$, so $\lambda = 1$, and the sphere is $x^2 + y^2 + z^2 - x - y - z = 0$.

:::exam-tip
Check a "sphere through given points" answer by substituting the points. It takes seconds and catches most sign slips.
:::

## Plane section: the circle {#plane-section}

A plane cuts a sphere in a **circle**, written as the pair of equations

$$S = 0, \qquad P \equiv lx + my + nz - p = 0.$$

Let $C$ be the centre and $r$ the radius of the sphere, and let $\delta$ be the distance from $C$ to the plane.

- The **centre of the circle** is the foot $N$ of the perpendicular from $C$ to the plane, because $CN$ is perpendicular to every chord through $N$.
- The **radius of the circle** is $\sqrt{r^2 - \delta^2}$ (Pythagoras in the triangle $CNQ$ with $Q$ on the circle).

| Distance $\delta$ | Section |
|:---|:---|
| $\delta < r$ | a real circle of radius $\sqrt{r^2 - \delta^2}$ |
| $\delta = r$ | a single point: the plane is a tangent plane |
| $\delta > r$ | no real points |
| $\delta = 0$ | a **great circle** (radius $r$) |

**Finding the centre.** Write the normal through $C$ parametrically, $(x, y, z) = C + t(l, m, n)$, and substitute into the plane to find $t$.

**Example.** The circle $x^2 + y^2 + z^2 - 2y - 4z - 11 = 0$, $x + 2y + 2z = 15$.

- The sphere has centre $C(0, 1, 2)$ and radius $\sqrt{1 + 4 + 11} = 4$.
- The distance is $\delta = \dfrac{\lvert 0 + 2 + 4 - 15\rvert}{3} = 3$, so the radius of the circle is $\sqrt{16 - 9} = \sqrt7$.
- The normal through $C$ is $(t,\ 1 + 2t,\ 2 + 2t)$. In the plane, $t + 2(1 + 2t) + 2(2 + 2t) = 9t + 6 = 15$, so $t = 1$. The centre of the circle is $(1, 3, 4)$, at distance $3$ from $C$ as expected.

:::caution
Normalise before dividing: the distance is $\dfrac{\lvert lx_0 + my_0 + nz_0 - p\rvert}{\sqrt{l^2 + m^2 + n^2}}$. Forgetting the denominator, or using $r^2 + \delta^2$ instead of $r^2 - \delta^2$, are the two standard slips.
:::

:::exam-tip
For a sphere centred at the origin and the plane $lx + my + nz = p$, the centre of the section is $\dfrac{p}{l^2 + m^2 + n^2}(l, m, n)$. For $x^2 + y^2 + z^2 = 25$, $x + 2y + 2z = 9$ this is $(1, 2, 2)$, and the radius is $\sqrt{25 - 9} = 4$.
:::

## Spheres through a circle; two spheres {#through-circle}

**The family $S + \lambda P = 0$.** If the circle is $S = 0$, $P = 0$, then for every $\lambda$

$$S + \lambda P = 0$$

is a sphere (the second-degree part is still $x^2 + y^2 + z^2$), and it contains every point of the circle. Every sphere through the circle is of this form. One more condition fixes $\lambda$.

**Example.** The sphere through the circle $x^2 + y^2 + z^2 = 9$, $x + y + z = 1$ and the point $(1, 1, 1)$:

$$(3 - 9) + \lambda(3 - 1) = 0 \implies \lambda = 3, \qquad x^2 + y^2 + z^2 + 3x + 3y + 3z - 12 = 0.$$

**Circle as a great circle.** The circle is a great circle of $S + \lambda P = 0$ iff the centre of that sphere lies on the plane $P = 0$. Substitute the centre $\left(-u - \frac{\lambda l}{2}, \dots\right)$ into $P$ and solve for $\lambda$.

**Intersection of two spheres.** Two spheres $S_1 = 0$, $S_2 = 0$ (both in standard form) meet in the circle

$$S_1 = 0, \qquad S_1 - S_2 = 0,$$

because $S_1 - S_2$ is linear: the squared terms cancel. The spheres through this circle are $S_1 + \lambda S_2 = 0$ ($\lambda \ne -1$), or equivalently $S_1 + \mu(S_1 - S_2) = 0$.

**Radius of the common circle.** Find the plane $S_1 - S_2 = 0$, then use the plane-section method on either sphere.

**Example.** $x^2 + y^2 + z^2 = 25$ and $x^2 + y^2 + z^2 - 12x + 11 = 0$ (centre $(6, 0, 0)$, radius $5$). The plane is $12x - 36 = 0$, i.e. $x = 3$. Its distance from $O$ is $3$, so the circle has radius $\sqrt{25 - 9} = 4$ and centre $(3, 0, 0)$.

:::caution
In $S + \lambda P = 0$ the plane must be written as $P = 0$ with everything on one side. Substituting a point into $P$ as "$lx + my + nz$" while forgetting the constant is a frequent slip.
:::

:::exam-tip
The circle $S = 0$, $P = 0$ is a great circle of $S$ itself iff the plane passes through the centre of $S$; then its radius equals the radius of the sphere.
:::

## Tangent plane, normal and tangency {#tangent-plane}

**Tangent plane at a point.** At $(x_1, y_1, z_1)$ on $S = 0$, the tangent plane is $T = 0$:

$$xx_1 + yy_1 + zz_1 + u(x + x_1) + v(y + y_1) + w(z + z_1) + d = 0.$$

(Replace $x^2$ by $xx_1$ and $2x$ by $x + x_1$, and so on.) It is the plane through the point perpendicular to the radius, with normal direction $(x_1 + u,\ y_1 + v,\ z_1 + w)$. For $x^2 + y^2 + z^2 = a^2$ it is $xx_1 + yy_1 + zz_1 = a^2$.

**Normal.** The normal at $(x_1, y_1, z_1)$ is the line through the point and the centre:

$$\frac{x - x_1}{x_1 + u} = \frac{y - y_1}{y_1 + v} = \frac{z - z_1}{z_1 + w}.$$

**Condition of tangency.** A plane touches a sphere iff its distance from the centre equals the radius. For the plane $lx + my + nz = p$:

| Sphere | Condition |
|:---|:---|
| $x^2 + y^2 + z^2 = a^2$ | $p^2 = a^2(l^2 + m^2 + n^2)$ |
| $x^2 + y^2 + z^2 + 2ux + 2vy + 2wz + d = 0$ | $(ul + vm + wn + p)^2 = (l^2 + m^2 + n^2)(u^2 + v^2 + w^2 - d)$ |

The **point of contact** is the foot of the perpendicular from the centre to the plane.

**Tangent planes parallel to a given plane.** There are exactly two. Write them as $lx + my + nz + k = 0$ and solve $\dfrac{\lvert \dots + k\rvert}{\sqrt{l^2 + m^2 + n^2}} = r$.

**Example.** The sphere $x^2 + y^2 + z^2 - 2x - 4y + 2z - 3 = 0$ has centre $(1, 2, -1)$ and radius $3$. The plane $2x - y + 2z = k$ touches it iff $\lvert 2 - 2 - 2 - k\rvert = 9$, i.e. $k = 7$ or $k = -11$. For $k = 7$, the foot from the centre is $(1, 2, -1) + t(2, -1, 2)$ with $9t - 2 = 7$, so $t = 1$ and the point of contact is $(3, 1, 1)$.

**Tangent line.** A line touches the sphere iff its distance from the centre equals the radius. Equivalently, substituting the line's parametric form gives a quadratic with equal roots.

:::caution
The tangent plane is **perpendicular** to the radius at the point of contact, not parallel to it. And the half-coefficient rule matters: $2ux$ becomes $u(x + x_1)$, not $2u(x + x_1)$.
:::

## Power of a point and the radical plane {#radical-plane}

**Power.** With $S$ in standard form, the **power** of $P(x_1, y_1, z_1)$ with respect to $S = 0$ is

$$S_1 = S(x_1, y_1, z_1) = CP^2 - r^2.$$

If $P$ is outside, $S_1$ is the **square of the length of a tangent** from $P$ (every tangent line from $P$ has the same length $\sqrt{S_1}$). Any line through $P$ meeting the sphere at $A, B$ has $PA \cdot PB = \lvert S_1\rvert$.

**Radical plane.** The locus of points with equal powers with respect to $S_1 = 0$ and $S_2 = 0$ (both in standard form) is

$$S_1 - S_2 = 0, \qquad\text{i.e.}\quad 2(u_1 - u_2)x + 2(v_1 - v_2)y + 2(w_1 - w_2)z + (d_1 - d_2) = 0.$$

- Its normal is $(u_1 - u_2, v_1 - v_2, w_1 - w_2)$, so it is **perpendicular to the line of centres**.
- If the spheres meet, it is the plane of their common circle; if they touch, it is the common tangent plane.
- Concentric spheres ($u_1 = u_2$, etc.) have no radical plane.

**Radical line and centre.**

- Three spheres with **non-collinear** centres: the three radical planes taken in pairs pass through one line, the **radical line**. (If $S_1 = S_2$ and $S_2 = S_3$ at a point, then $S_1 = S_3$ there.)
- Four spheres with **non-coplanar** centres: the radical planes meet in one point, the **radical centre**, which has equal power with respect to all four.

**Example.** For $S_1 = \Sigma - 2x - 7$, $S_2 = \Sigma - 4y - 5$, $S_3 = \Sigma - 6z - 3$, $S_4 = \Sigma - 9$ (where $\Sigma = x^2 + y^2 + z^2$), the planes $S_i - S_4 = 0$ are $x = 1$, $y = 1$, $z = 1$. The radical centre is $(1, 1, 1)$.

**Coaxal system (for orientation).** All spheres $S + \lambda P = 0$ share the radical plane $P = 0$; such a family is called coaxal. It contains two point spheres (the **limiting points**) when the common plane misses the spheres. The syllabus does not list coaxal systems separately.

:::exam-tip
Before subtracting, make sure both equations have coefficient $1$ for $x^2$. Subtracting $2x^2 + \dots$ from $x^2 + \dots$ gives a quadric, not a plane.
:::

## Angle between spheres: orthogonal and touching spheres {#orthogonal}

Let the spheres have centres $C_1, C_2$, radii $r_1, r_2$, and let $\delta = C_1C_2$.

**Angle of intersection.** At a common point $Q$, the angle between the spheres is the angle between their tangent planes at $Q$, which equals the angle between the radii $C_1Q$ and $C_2Q$ (or its supplement). By the cosine rule in triangle $C_1QC_2$:

$$\cos\theta = \frac{r_1^2 + r_2^2 - \delta^2}{2r_1r_2}.$$

**Orthogonal spheres** ($\theta = \frac\pi2$):

$$\delta^2 = r_1^2 + r_2^2 \iff 2(u_1u_2 + v_1v_2 + w_1w_2) = d_1 + d_2.$$

*Proof idea.* $\delta^2 = \sum(u_1 - u_2)^2$ and $r_1^2 + r_2^2 = \sum u_1^2 - d_1 + \sum u_2^2 - d_2$; equating them leaves $-2\sum u_1u_2 = -(d_1 + d_2)$.

Consequences:

- If the spheres are orthogonal, the power of $C_1$ with respect to $S_2$ is $\delta^2 - r_2^2 = r_1^2$: the radius of each is the tangent length from its centre to the other.
- Two spheres both through the origin ($d_1 = d_2 = 0$) are orthogonal iff $u_1u_2 + v_1v_2 + w_1w_2 = 0$, that is, iff their centres are at right angles at $O$. They are **not** orthogonal in general.

**Example.** For what $k$ are $x^2 + y^2 + z^2 - 2x - 4y - 6z + k = 0$ and $x^2 + y^2 + z^2 + 4x + 2y - 2z + 3 = 0$ orthogonal? Here $(u_1, v_1, w_1) = (-1, -2, -3)$ and $(u_2, v_2, w_2) = (2, 1, -1)$:

$$2(-2 - 2 + 3) = k + 3 \implies k = -5.$$

**Touching spheres.**

| Condition | Meaning |
|:---|:---|
| $\delta = r_1 + r_2$ | touch externally |
| $\delta = \lvert r_1 - r_2\rvert$ | touch internally |
| $\lvert r_1 - r_2\rvert < \delta < r_1 + r_2$ | meet in a real circle |

The point of contact divides $C_1C_2$ in the ratio $r_1 : r_2$ (internally for external contact).

:::caution
The orthogonality condition uses the **standard-form** coefficients and has $+$ on the right: $2\sum u_1u_2 = d_1 + d_2$. Writing $d_1d_2$ or $d_1 - d_2$ on the right, or forgetting the factor $2$ on the left, are the usual slips. (Using the centre coordinates $-u_i$ instead of $u_i$ is harmless here, since the products are unchanged.)
:::

## Quick checks and traps {#exam-tips}

- **Normalise first.** Every formula here (centre, radius, power, radical plane, orthogonality) assumes the coefficient of $x^2$ is $1$.
- **Centre** $(-u, -v, -w)$; **radius** $\sqrt{u^2 + v^2 + w^2 - d}$. If this is $0$ you have a point sphere.
- **Section radius:** $\sqrt{r^2 - \delta^2}$, never $r - \delta$ or $\sqrt{r^2 + \delta^2}$.
- **Section centre:** the foot of the perpendicular from the sphere's centre. Check it lies on the plane.
- **Through a circle:** $S + \lambda P = 0$; through the intersection of two spheres: $S_1 + \lambda S_2 = 0$.
- **Great circle:** the centre of $S + \lambda P$ lies on $P = 0$.
- **Tangent plane:** $T = 0$; check that the point satisfies it and that its normal is parallel to the radius.
- **Tangency:** distance from centre $=$ radius. Parallel tangent planes come in pairs.
- **Power:** $S(P) = CP^2 - r^2$; positive outside, and it is the square of the tangent length.
- **Radical plane** $S_1 - S_2 = 0$ is perpendicular to the line of centres; three spheres give a radical line, four give a radical centre.
- **Orthogonal:** $2\sum u_1u_2 = d_1 + d_2$, equivalently $\delta^2 = r_1^2 + r_2^2$.
- **Touching:** $\delta = r_1 + r_2$ (external) or $\lvert r_1 - r_2\rvert$ (internal).
- Planes and lines in space are covered in *3D Coordinates and Planes* and *Straight Lines in Space*; the general second-degree surface is in *Quadrics*.
