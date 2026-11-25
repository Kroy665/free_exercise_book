# Straight Lines in Space

## Symmetric and parametric forms {#line-forms}

Throughout, direction cosines (d.c.) and direction ratios (d.r.), the angle between two lines and the forms of a plane are taken from the topic on planes.

A line is fixed by a point $A(x_1, y_1, z_1)$ on it and a direction with ratios $l : m : n$ (not all zero).

**Symmetric (Cartesian) form**

$$\frac{x - x_1}{l} = \frac{y - y_1}{m} = \frac{z - z_1}{n}.$$

**Parametric form.** Put each fraction equal to $t$:

$$x = x_1 + lt, \qquad y = y_1 + mt, \qquad z = z_1 + nt, \qquad t \in \R.$$

So the **general point** of the line is $(x_1 + lt,\; y_1 + mt,\; z_1 + nt)$. This one fact solves most problems in the topic: write the general point, then impose the condition (lies on a plane, makes a right angle, is at a given distance).

If $l, m, n$ are the actual **direction cosines**, then $\lvert t\rvert$ is the distance of the point from $A$. With direction ratios, the distance is $\lvert t\rvert\sqrt{l^2 + m^2 + n^2}$.

**Two-point form.** Through $A(x_1, y_1, z_1)$ and $B(x_2, y_2, z_2)$:

$$\frac{x - x_1}{x_2 - x_1} = \frac{y - y_1}{y_2 - y_1} = \frac{z - z_1}{z_2 - z_1}.$$

**Vector form.** $\vec r = \vec a + t\vec b$, where $\vec a$ is the position vector of a point and $\vec b = (l, m, n)$.

**Zero denominators.** A $0$ in a denominator is a convention: it means the numerator is $0$. So $\dfrac{x - 1}{0} = \dfrac{y - 2}{3} = \dfrac{z}{4}$ is the line $x = 1$, $\dfrac{y - 2}{3} = \dfrac{z}{4}$, lying in the plane $x = 1$. The $x$-axis is $\dfrac{x}{1} = \dfrac{y}{0} = \dfrac{z}{0}$, that is, $y = 0,\ z = 0$.

**Reading off the direction.** The form must have coefficient $+1$ on $x$, $y$ and $z$ in the numerators before you read the denominators. For

$$\frac{2x - 1}{3} = \frac{1 - y}{2} = \frac{z + 1}{4}$$

rewrite as $\dfrac{x - \frac12}{3/2} = \dfrac{y - 1}{-2} = \dfrac{z + 1}{4}$. The direction ratios are $\tfrac32 : -2 : 4$, that is $3 : -4 : 8$, and a point is $(\tfrac12, 1, -1)$.

:::caution
Reading $3, 2, 4$ straight from the denominators above is the commonest slip. Clear the coefficient of $x$ (divide by $2$) and the sign of $y$ (since $1 - y = -(y - 1)$) first.
:::

## A line as the intersection of two planes {#planes-to-line}

Two non-parallel planes

$$a_1x + b_1y + c_1z + d_1 = 0, \qquad a_2x + b_2y + c_2z + d_2 = 0$$

meet in a line. This pair of equations is the **general (unsymmetric) form** of the line.

**Reduction to symmetric form.**

1. **Direction.** The line lies in both planes, so it is perpendicular to both normals:
   $$(l, m, n) \propto \vec n_1 \times \vec n_2 = (b_1c_2 - b_2c_1,\; c_1a_2 - c_2a_1,\; a_1b_2 - a_2b_1).$$
2. **A point.** Put one coordinate equal to a convenient value (usually $z = 0$, or $x = 0$) and solve the two equations for the other two. If that gives no solution, the line is parallel to that coordinate plane; set a different coordinate.

**Example.** Reduce $2x + y - z = 3,\ x - y + 2z = 0$.

- Direction: $(2, 1, -1) \times (1, -1, 2) = (1 \cdot 2 - (-1)(-1),\ (-1)(1) - 2 \cdot 2,\ 2(-1) - 1 \cdot 1) = (1, -5, -3)$.
- Point: $z = 0$ gives $2x + y = 3$, $x - y = 0$, so $x = y = 1$.

$$\frac{x - 1}{1} = \frac{y - 1}{-5} = \frac{z}{-3}.$$

Check: the point $t = 1$, $(2, -4, -3)$, satisfies both planes ($4 - 4 + 3 = 3$ and $2 + 4 - 6 = 0$).

**Alternative.** Find two points (put $z = 0$, then $y = 0$) and use the two-point form. It needs no cross product, but takes longer.

**Planes through a line.** Every plane through the line $P_1 = 0 = P_2$ (other than $P_2 = 0$ itself) is $P_1 + \lambda P_2 = 0$. For the symmetric form $\frac{x - x_1}{l} = \frac{y - y_1}{m} = \frac{z - z_1}{n}$, a plane $a(x - x_1) + b(y - y_1) + c(z - z_1) = 0$ contains the line exactly when $al + bm + cn = 0$.

:::exam-tip
A line **parallel to two planes** has direction $\vec n_1 \times \vec n_2$, the same as their line of intersection. Remember the cross product by the cyclic pattern: the $x$-component uses $b, c$; the $y$-component uses $c, a$; the $z$-component uses $a, b$.
:::

## A line and a plane {#line-and-plane}

Take the line $L: \dfrac{x - x_1}{l} = \dfrac{y - y_1}{m} = \dfrac{z - z_1}{n}$ and the plane $\Pi: ax + by + cz + d = 0$, with normal $(a, b, c)$.

**Angle.** The angle $\theta$ between a line and a plane is the complement of the angle between the line and the normal. So

$$\sin\theta = \frac{\lvert al + bm + cn\rvert}{\sqrt{a^2 + b^2 + c^2}\,\sqrt{l^2 + m^2 + n^2}}, \qquad 0 \le \theta \le \frac{\pi}{2}.$$

Example: the line with d.r. $(2, 1, 2)$ and the plane $3x + 4z = 1$ give $\sin\theta = \dfrac{6 + 8}{3 \cdot 5} = \dfrac{14}{15}$.

| Relation | Condition |
|:---|:---|
| $L$ perpendicular to $\Pi$ | $\dfrac{l}{a} = \dfrac{m}{b} = \dfrac{n}{c}$ |
| $L$ parallel to $\Pi$ (or lying in it) | $al + bm + cn = 0$ |
| $L$ lies in $\Pi$ | $al + bm + cn = 0$ **and** $ax_1 + by_1 + cz_1 + d = 0$ |
| $L$ parallel to $\Pi$, not in it | $al + bm + cn = 0$ and $ax_1 + by_1 + cz_1 + d \ne 0$ |
| $L$ meets $\Pi$ in one point | $al + bm + cn \ne 0$ |

**Point of intersection.** Substitute the general point into the plane:

$$a(x_1 + lt) + b(y_1 + mt) + c(z_1 + nt) + d = 0 \;\Rightarrow\; t = -\frac{ax_1 + by_1 + cz_1 + d}{al + bm + cn}.$$

**Distance measured along a line.** The distance of a point $A$ from a plane *measured parallel to a given line* is $\lvert AP\rvert$, where $P$ is where the line through $A$ with that direction meets the plane. It is not the perpendicular distance.

**Projection of a line on a plane.** The projection of $L$ on $\Pi$ is the intersection of $\Pi$ with the plane through $L$ perpendicular to $\Pi$. That plane passes through $(x_1, y_1, z_1)$ and has normal $(l, m, n) \times (a, b, c)$.

:::caution
The angle between a line and a plane uses **sine**, not cosine, because the normal is perpendicular to the plane. If $al + bm + cn = 0$, the angle is $0$ (parallel), not $\frac{\pi}{2}$.
:::

## Foot of the perpendicular, distance and image {#perpendicular-image}

**From a point to a line.** Let $P(\alpha, \beta, \gamma)$ and the line $\dfrac{x - x_1}{l} = \dfrac{y - y_1}{m} = \dfrac{z - z_1}{n}$.

1. Take the general point $Q = (x_1 + lt,\ y_1 + mt,\ z_1 + nt)$.
2. Impose $\overrightarrow{PQ} \perp$ the line:
   $$l(x_1 + lt - \alpha) + m(y_1 + mt - \beta) + n(z_1 + nt - \gamma) = 0.$$
3. Solve for $t$. Then $Q$ is the **foot**, $PQ$ is the **distance**, and the **image** of $P$ in the line is $P' = 2Q - P$.

Equivalently, with $A = (x_1, y_1, z_1)$ and $\vec b = (l, m, n)$,

$$\text{distance} = \frac{\lvert \overrightarrow{AP} \times \vec b\rvert}{\lvert \vec b\rvert}.$$

**Example.** $P(2, 4, -1)$ and the line $\dfrac{x + 5}{1} = \dfrac{y + 3}{4} = \dfrac{z - 6}{-9}$.

$Q = (-5 + t,\ -3 + 4t,\ 6 - 9t)$, and $\overrightarrow{PQ} = (t - 7,\ 4t - 7,\ 7 - 9t)$. Then

$$(t - 7) + 4(4t - 7) - 9(7 - 9t) = 98t - 98 = 0 \;\Rightarrow\; t = 1.$$

Foot $Q = (-4, 1, -3)$, distance $\sqrt{36 + 9 + 4} = 7$, image $(-10, -2, -5)$.

**From a point to a plane.** For $P(\alpha, \beta, \gamma)$ and $ax + by + cz + d = 0$, the perpendicular is $\dfrac{x - \alpha}{a} = \dfrac{y - \beta}{b} = \dfrac{z - \gamma}{c}$. The foot $N$ and the image $P'$ are

$$\frac{x - \alpha}{a} = \frac{y - \beta}{b} = \frac{z - \gamma}{c} = -\frac{a\alpha + b\beta + c\gamma + d}{a^2 + b^2 + c^2}\times\begin{cases}1 & \text{(foot)}\\ 2 & \text{(image)}\end{cases}$$

Example: for $P(1, 2, 3)$ and $x + 2y + 2z = 2$, the ratio is $-\dfrac{9}{9} = -1$. The foot is $(0, 0, 1)$ and the image is $(-1, -2, -1)$.

:::exam-tip
Check a foot by two facts: it lies on the line (or plane), and $\overrightarrow{PQ}$ is perpendicular to the direction. Check an image by the midpoint: $\frac12(P + P')$ must be the foot.
:::

## Coplanar and intersecting lines {#coplanar-lines}

Let

$$L_1: \frac{x - x_1}{l_1} = \frac{y - y_1}{m_1} = \frac{z - z_1}{n_1}, \qquad L_2: \frac{x - x_2}{l_2} = \frac{y - y_2}{m_2} = \frac{z - z_2}{n_2}.$$

Two lines in space are of exactly one of three kinds: **parallel** (directions proportional), **intersecting**, or **skew** (neither, so not coplanar).

**Condition for coplanarity.** $L_1$ and $L_2$ lie in one plane if and only if the vectors $\overrightarrow{A_1A_2}$, $\vec b_1$, $\vec b_2$ are coplanar:

$$\begin{vmatrix} x_2 - x_1 & y_2 - y_1 & z_2 - z_1 \\ l_1 & m_1 & n_1 \\ l_2 & m_2 & n_2 \end{vmatrix} = 0.$$

For **non-parallel** lines this is the condition for them to **intersect**. Parallel lines always satisfy it (and are always coplanar).

**The plane containing them** (non-parallel case):

$$\begin{vmatrix} x - x_1 & y - y_1 & z - z_1 \\ l_1 & m_1 & n_1 \\ l_2 & m_2 & n_2 \end{vmatrix} = 0,$$

that is, the plane through $A_1$ with normal $\vec b_1 \times \vec b_2$.

**Point of intersection.** Equate the general points: $x_1 + l_1t = x_2 + l_2s$, and so on. Solve two of the three equations for $t, s$; the third must then hold (this is the coplanarity check in disguise).

**Example.** $L_1: \dfrac{x - 2}{1} = \dfrac{y - 1}{1} = \dfrac{z}{2}$ and $L_2: \dfrac{x - 2}{1} = \dfrac{y - 3}{-1} = \dfrac{z - 1}{1}$.

$$\begin{vmatrix} 0 & 2 & 1 \\ 1 & 1 & 2 \\ 1 & -1 & 1 \end{vmatrix} = 0 - 2(1 - 2) + 1(-1 - 1) = 0,$$

so they are coplanar, and they are not parallel. Normal: $(1, 1, 2) \times (1, -1, 1) = (3, 1, -2)$, so the plane is $3x + y - 2z = 7$. From $2 + t = 2 + s$ and $1 + t = 3 - s$ we get $t = s = 1$, and the lines meet at $(3, 2, 2)$.

**Lines in general form.** The line $P_1 = 0 = P_2$ and the line $\dfrac{x - x_1}{l} = \dfrac{y - y_1}{m} = \dfrac{z - z_1}{n}$ are coplanar if and only if some plane $P_1 + \lambda P_2 = 0$ contains the second line. This needs both its point and its direction to satisfy the plane condition. Eliminating $\lambda$ gives
$$\frac{a_1x_1 + b_1y_1 + c_1z_1 + d_1}{a_1l + b_1m + c_1n} = \frac{a_2x_1 + b_2y_1 + c_2z_1 + d_2}{a_2l + b_2m + c_2n}.$$

## Skew lines and the shortest distance {#shortest-distance}

For skew lines $\vec r = \vec a_1 + t\vec b_1$ and $\vec r = \vec a_2 + s\vec b_2$ there is **exactly one** line meeting both at right angles: the **line of shortest distance** (the common perpendicular). Its direction is $\vec b_1 \times \vec b_2$, and the length of the segment between its feet is the **shortest distance** (S.D.):

$$\text{S.D.} = \frac{\lvert(\vec a_2 - \vec a_1)\cdot(\vec b_1 \times \vec b_2)\rvert}{\lvert \vec b_1 \times \vec b_2\rvert} = \frac{\left\lvert\begin{vmatrix} x_2 - x_1 & y_2 - y_1 & z_2 - z_1 \\ l_1 & m_1 & n_1 \\ l_2 & m_2 & n_2 \end{vmatrix}\right\rvert}{\sqrt{\sum (m_1n_2 - m_2n_1)^2}}.$$

It is the projection of $\overrightarrow{A_1A_2}$ on the common normal. S.D. $= 0$ exactly when the (non-parallel) lines intersect.

**Parallel lines** ($\vec b_1 = \vec b_2 = \vec b$): the formula fails since $\vec b \times \vec b = \vec 0$. Use the distance of $A_2$ from $L_1$:

$$d = \frac{\lvert(\vec a_2 - \vec a_1) \times \vec b\rvert}{\lvert \vec b\rvert}.$$

**Equations of the line of shortest distance.**

- *Method 1 (feet).* Take general points $P$ on $L_1$ and $Q$ on $L_2$. Solve $\overrightarrow{PQ}\cdot\vec b_1 = 0$ and $\overrightarrow{PQ}\cdot\vec b_2 = 0$ for $t, s$. Then $PQ$ is the S.D., $P$ and $Q$ are the feet, and the line is the line $PQ$.
- *Method 2 (planes).* With $\vec n = \vec b_1 \times \vec b_2$, the S.D. line is the intersection of the plane through $L_1$ containing $\vec n$ and the plane through $L_2$ containing $\vec n$.

**Example.** $L_1: \dfrac{x - 1}{1} = \dfrac{y - 2}{-1} = \dfrac{z - 3}{1}$ and $L_2: \dfrac{x - 2}{2} = \dfrac{y + 1}{1} = \dfrac{z + 1}{-1}$.

$\vec b_1 \times \vec b_2 = (1, -1, 1) \times (2, 1, -1) = (0, 3, 3)$, and $\vec a_2 - \vec a_1 = (1, -3, -4)$:

$$\text{S.D.} = \frac{\lvert 0 - 9 - 12\rvert}{3\sqrt2} = \frac{7}{\sqrt2}.$$

For the feet, $P = (1 + t, 2 - t, 3 + t)$ and $Q = (2 + 2s, -1 + s, -1 - s)$. The two perpendicularity conditions give $t = 0$ and $s = -\tfrac12$, so $P = (1, 2, 3)$ and $Q = (1, -\tfrac32, -\tfrac12)$. The S.D. line is $x = 1,\ y - 2 = z - 3$, that is, $\dfrac{x - 1}{0} = \dfrac{y - 2}{1} = \dfrac{z - 3}{1}$, along $(0, 1, 1)$ as expected.

:::caution
Do not drop the modulus, and divide by $\lvert \vec b_1 \times \vec b_2\rvert$, not by $\lvert \vec b_1\rvert\,\lvert \vec b_2\rvert$. Those are equal only when the lines are perpendicular.
:::

## Quick checks and traps {#exam-tips}

| Task | Key formula or step |
|:---|:---|
| Direction of $P_1 = 0 = P_2$ | $\vec n_1 \times \vec n_2$ |
| Angle between line and plane | $\sin\theta = \dfrac{\lvert \vec b\cdot\vec n\rvert}{\lvert \vec b\rvert\,\lvert \vec n\rvert}$ |
| Line lies in plane | $\vec b\cdot\vec n = 0$ and one point on the plane |
| Image in a plane | ratio $= -2\dfrac{a\alpha + b\beta + c\gamma + d}{a^2 + b^2 + c^2}$ |
| Coplanarity | $[\overrightarrow{A_1A_2},\ \vec b_1,\ \vec b_2] = 0$ |
| Skew-line S.D. | $\dfrac{\lvert[\overrightarrow{A_1A_2},\ \vec b_1,\ \vec b_2]\rvert}{\lvert \vec b_1 \times \vec b_2\rvert}$ |
| Parallel-line distance | $\dfrac{\lvert \overrightarrow{A_1A_2} \times \vec b\rvert}{\lvert \vec b\rvert}$ |

- **Normalise the form first.** Numerators must read $x - x_1$, $y - y_1$, $z - z_1$ with coefficient $+1$.
- **Non-intersecting does not mean parallel.** In space, lines that do not meet may be skew.
- **Determinant zero** means coplanar: intersecting *or* parallel. Check the directions before saying "they meet".
- **Image = 2 × foot − point.** Halving or forgetting the factor $2$ gives the foot instead of the image.
- **Two equations, not one.** A line in general form needs both plane equations; a single linear equation in $x, y, z$ is a plane.
- **The line of S.D. is unique** for skew lines, but the same line can be written from either foot, so equations that look different may agree. Test a point and the direction.
- **Fast check on an S.D.** The two feet must differ by a multiple of $\vec b_1 \times \vec b_2$, and their distance must equal the formula's value.

:::exam-tip
Most one-minute questions reduce to one of three moves: write the general point and substitute; take a cross product; or evaluate one $3 \times 3$ determinant. Decide which before you calculate.
:::
