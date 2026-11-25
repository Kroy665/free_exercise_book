# Vector Applications and Calculus

## Work done and moment of a force {#work-moment}

The products themselves ($\cdot$, $\times$, $[\,\cdot\,\cdot\,\cdot\,]$) are in **Vector Algebra**; here they are applied.

**Work done.** A constant force $\vec F$ whose point of application moves from $A$ to $B$ does work

$$W = \vec F\cdot\vec d = \vec F\cdot(\vec b - \vec a), \qquad \vec d = \vec{AB}.$$

$W$ is a scalar; it is $0$ when the displacement is perpendicular to the force. For several forces acting on the same particle, the total work is $\left(\sum\vec F_i\right)\cdot\vec d$ = the work done by the resultant.

**Moment (torque) about a point.** If $\vec F$ acts at a point $P$, its moment about a point $O'$ is

$$\vec M_{O'} = \vec{O'P}\times\vec F = (\vec p - \vec o\,')\times\vec F.$$

- The order is **position vector first, then force**; $\vec F\times\vec r$ gives the negative.
- $\vec{O'P}$ may be taken to **any** point $P$ on the line of action: moving $P$ along $\vec F$ adds a multiple of $\vec F$, and $\vec F\times\vec F = \vec 0$.
- $\vec M_{O'} = \vec 0 \iff O'$ lies on the line of action (for $\vec F \ne \vec 0$).
- $|\vec M_{O'}| = |\vec F|\times$ (perpendicular distance of $O'$ from the line of action).
- **Varignon:** the moment of the resultant of concurrent forces equals the sum of their moments.

**Moment about a line.** Let $L$ pass through $A$ with **unit** vector $\hat\ell$. The moment of $\vec F$ (acting at $P$) about $L$ is the scalar

$$M_L = (\vec{AP}\times\vec F)\cdot\hat\ell = [\vec{AP}\ \ \vec F\ \ \hat\ell\,],$$

the resolved part along $L$ of the moment about any point of $L$. It does not depend on which point $A$ of $L$ is used. It is zero iff $\vec F$ and $L$ are coplanar (parallel or intersecting). Some books call the vector $M_L\hat\ell$ the moment about the line; the scalar is the same.

**Couple.** Forces $\vec F$ at $P$ and $-\vec F$ at $Q$ have moment $\vec{QP}\times\vec F$ about **every** point; it is called the moment of the couple.

**Example.** $\vec F = \hat i + 2\hat j + 3\hat k$ acts at $P(2, 0, 1)$. Its moment about $O$ is

$$\vec r\times\vec F = \begin{vmatrix}\hat i&\hat j&\hat k\\2&0&1\\1&2&3\end{vmatrix} = -2\hat i - 5\hat j + 4\hat k.$$

About the line through $O$ along $2\hat i - 2\hat j + \hat k$ (so $\hat\ell = \frac13(2, -2, 1)$): $M_L = \frac13(-4 + 10 + 4) = \frac{10}{3}$.

:::caution
For the moment about a line, divide by $|\vec\ell|$. Using $\vec\ell$ instead of $\hat\ell$ multiplies the answer by $|\vec\ell|$ (here it would give $10$).
:::

## Vector equation of a line {#lines}

| Line | Vector form | Cartesian form |
|:---|:---|:---|
| through $\vec a$, parallel to $\vec b$ | $\vec r = \vec a + t\vec b$ | $\dfrac{x - a_1}{b_1} = \dfrac{y - a_2}{b_2} = \dfrac{z - a_3}{b_3}$ |
| through $\vec a$ and $\vec c$ | $\vec r = \vec a + t(\vec c - \vec a)$ | $\dfrac{x - a_1}{c_1 - a_1} = \cdots$ |
| non-parametric | $(\vec r - \vec a)\times\vec b = \vec 0$, i.e. $\vec r\times\vec b = \vec a\times\vec b$ | |

The parameter $t$ runs over $\R$; $\vec b$ is any direction vector, so its direction ratios are $b_1 : b_2 : b_3$. When a denominator is $0$, read it as "that numerator is $0$".

**Angle between lines** $\vec r = \vec a_1 + t\vec b_1$ and $\vec r = \vec a_2 + s\vec b_2$: the acute angle $\theta$ with

$$\cos\theta = \frac{|\vec b_1\cdot\vec b_2|}{|\vec b_1|\,|\vec b_2|}.$$

They are perpendicular iff $\vec b_1\cdot\vec b_2 = 0$ and parallel iff $\vec b_1\times\vec b_2 = \vec 0$.

**Relative position of two lines.**

| Condition | Lines are |
|:---|:---|
| $\vec b_1\times\vec b_2 = \vec 0$ and $(\vec a_2 - \vec a_1)\times\vec b_1 = \vec 0$ | coincident |
| $\vec b_1\times\vec b_2 = \vec 0$, otherwise | parallel and distinct |
| $\vec b_1\times\vec b_2 \ne \vec 0$ and $[\vec a_2 - \vec a_1\ \ \vec b_1\ \ \vec b_2] = 0$ | intersecting |
| $[\vec a_2 - \vec a_1\ \ \vec b_1\ \ \vec b_2] \ne 0$ | **skew** (neither parallel nor intersecting) |

**Example.** The line through $A(1, 2, -1)$ and $B(3, 1, 2)$ is $\vec r = (\hat i + 2\hat j - \hat k) + t(2\hat i - \hat j + 3\hat k)$, i.e. $\dfrac{x - 1}{2} = \dfrac{y - 2}{-1} = \dfrac{z + 1}{3}$.

**Point of intersection.** Equate $\vec a_1 + t\vec b_1 = \vec a_2 + s\vec b_2$: three equations in $t, s$. Solve two of them and check the third. If the third fails, the lines are skew.

**Distance of a point $P$ from a line** $\vec r = \vec a + t\vec b$:

$$d = \frac{|(\vec p - \vec a)\times\vec b|}{|\vec b|}.$$

:::caution
$[\vec a_2 - \vec a_1\ \ \vec b_1\ \ \vec b_2] = 0$ says only that the lines are **coplanar**. Two distinct parallel lines also give $0$ (because $\vec b_1 \parallel \vec b_2$), yet they do not meet. "Intersect" needs, in addition, $\vec b_1\times\vec b_2 \ne \vec 0$.
:::

## Vector equation of a plane {#planes}

| Plane | Vector equation |
|:---|:---|
| normal form ($\hat n$ unit normal, $p \ge 0$) | $\vec r\cdot\hat n = p$ |
| general | $\vec r\cdot\vec n = d$ |
| through $\vec a$ with normal $\vec n$ | $(\vec r - \vec a)\cdot\vec n = 0$ |
| through $\vec a$, parallel to $\vec b$ and $\vec c$ | $[\vec r - \vec a\ \ \vec b\ \ \vec c] = 0$ |
| through $\vec a, \vec b, \vec c$ | $[\vec r - \vec a\ \ \vec b - \vec a\ \ \vec c - \vec a] = 0$ |
| through the line of intersection of $\vec r\cdot\vec n_1 = d_1$, $\vec r\cdot\vec n_2 = d_2$ | $\vec r\cdot(\vec n_1 + \lambda\vec n_2) = d_1 + \lambda d_2$ |

In the normal form, $p$ is the perpendicular distance of the origin from the plane. With $\vec n = (a, b, c)$, $\vec r\cdot\vec n = d$ is the Cartesian plane $ax + by + cz = d$.

**Distances and angles.**

- Distance of $P(\vec p)$ from $\vec r\cdot\vec n = d$: $\dfrac{|\vec p\cdot\vec n - d|}{|\vec n|}$. From the origin: $\dfrac{|d|}{|\vec n|}$.
- Angle between planes = angle between normals: $\cos\theta = \dfrac{|\vec n_1\cdot\vec n_2|}{|\vec n_1|\,|\vec n_2|}$.
- Angle $\varphi$ between the line $\vec r = \vec a + t\vec b$ and the plane: $\sin\varphi = \dfrac{|\vec b\cdot\vec n|}{|\vec b|\,|\vec n|}$ (the complement of the angle with the normal).
- The line is parallel to the plane iff $\vec b\cdot\vec n = 0$; it **lies in** the plane iff, in addition, $\vec a\cdot\vec n = d$.
- The line of intersection of two planes has direction $\vec n_1\times\vec n_2$.

**Example (three points).** $A(1, 1, 0)$, $B(1, 2, 1)$, $C(-2, 2, -1)$. A normal is

$$\vec{AB}\times\vec{AC} = (0, 1, 1)\times(-3, 1, -1) = (-2, -3, 3).$$

So $\vec r\cdot(2\hat i + 3\hat j - 3\hat k) = \vec a\cdot(2, 3, -3) = 5$, i.e. $2x + 3y - 3z = 5$.

**Example (distance).** $P(2, 1, -1)$ from $\vec r\cdot(\hat i - 2\hat j + 2\hat k) = 5$: $\dfrac{|2 - 2 - 2 - 5|}{3} = \dfrac73$.

:::exam-tip
Check a three-point plane by substituting each point: every one must satisfy it. A sign slip in the middle component of the cross product is caught at once.
:::

:::caution
The line–plane angle uses **sine**, not cosine, because $\vec n$ is perpendicular to the plane. $\cos^{-1}$ of the same ratio gives the angle with the normal.
:::

## Shortest distance between two lines {#shortest-distance}

For $L_1: \vec r = \vec a_1 + t\vec b_1$ and $L_2: \vec r = \vec a_2 + s\vec b_2$:

**Skew or intersecting lines** ($\vec b_1\times\vec b_2 \ne \vec 0$). The common perpendicular is along $\vec b_1\times\vec b_2$, and the shortest distance is the projection of $\vec a_2 - \vec a_1$ on it:

$$d = \frac{\left|(\vec a_2 - \vec a_1)\cdot(\vec b_1\times\vec b_2)\right|}{|\vec b_1\times\vec b_2|} = \frac{\left|[\vec a_2 - \vec a_1\ \ \vec b_1\ \ \vec b_2]\right|}{|\vec b_1\times\vec b_2|}.$$

$d = 0$ iff the lines intersect.

**Parallel lines** ($\vec b_1 = \vec b_2 = \vec b$). The formula above is $\frac00$; use the point-to-line distance instead:

$$d = \frac{|(\vec a_2 - \vec a_1)\times\vec b|}{|\vec b|}.$$

**Example (skew).** $\vec r = (\hat i + \hat j) + t(2\hat i - \hat j + \hat k)$ and $\vec r = (2\hat i + \hat j - \hat k) + s(3\hat i - 5\hat j + 2\hat k)$.

$$\vec b_1\times\vec b_2 = (2, -1, 1)\times(3, -5, 2) = (3, -1, -7), \qquad |\vec b_1\times\vec b_2| = \sqrt{59}.$$

$\vec a_2 - \vec a_1 = (1, 0, -1)$, so $(\vec a_2 - \vec a_1)\cdot(\vec b_1\times\vec b_2) = 3 + 7 = 10$ and $d = \dfrac{10}{\sqrt{59}}$.

**Example (parallel).** $\vec r = (\hat i + 2\hat j - 4\hat k) + t(2\hat i + 3\hat j + 6\hat k)$ and $\vec r = (3\hat i + 3\hat j - 5\hat k) + s(2\hat i + 3\hat j + 6\hat k)$. Here $|\vec b| = 7$, $\vec a_2 - \vec a_1 = (2, 1, -1)$ and

$$(\vec a_2 - \vec a_1)\times\vec b = (2, 1, -1)\times(2, 3, 6) = (9, -14, 4), \qquad d = \frac{\sqrt{293}}{7}.$$

**Condition to intersect.** Non-parallel lines meet iff $[\vec a_2 - \vec a_1\ \ \vec b_1\ \ \vec b_2] = 0$. In Cartesian form, $\frac{x - x_1}{l_1} = \frac{y - y_1}{m_1} = \frac{z - z_1}{n_1}$ and $\frac{x - x_2}{l_2} = \cdots$ meet iff

$$\begin{vmatrix} x_2 - x_1 & y_2 - y_1 & z_2 - z_1 \\ l_1 & m_1 & n_1 \\ l_2 & m_2 & n_2 \end{vmatrix} = 0.$$

The feet of the common perpendicular are found by making $\vec{PQ}$ (from $\vec a_1 + t\vec b_1$ to $\vec a_2 + s\vec b_2$) perpendicular to both $\vec b_1$ and $\vec b_2$: two linear equations in $t, s$.

:::exam-tip
Before computing, look at the direction vectors. If they are proportional, switch to the parallel-line formula; otherwise the numerator is just a $3\times 3$ determinant.
:::

## Volume of a tetrahedron {#tetrahedron}

A tetrahedron with coterminous edges $\vec a, \vec b, \vec c$ has base area $\frac12|\vec b\times\vec c|$ and height $|\vec a\cdot\widehat{(\vec b\times\vec c)}|$, so

$$V = \frac13\cdot\frac12|\vec b\times\vec c|\cdot\text{height} = \frac16\left|[\vec a\,\vec b\,\vec c]\right|.$$

It is **one-sixth** of the parallelepiped on the same edges (and one-third of the prism on the same triangle).

**From the four vertices** $A, B, C, D$:

$$V = \frac16\left|[\vec{AB}\ \ \vec{AC}\ \ \vec{AD}]\right| = \frac16\left|\begin{vmatrix} x_2 - x_1 & y_2 - y_1 & z_2 - z_1 \\ x_3 - x_1 & y_3 - y_1 & z_3 - z_1 \\ x_4 - x_1 & y_4 - y_1 & z_4 - z_1 \end{vmatrix}\right|.$$

Equivalently $V = \frac16\left|\det\begin{pmatrix} x_i & y_i & z_i & 1\end{pmatrix}_{i=1..4}\right|$. Any vertex may serve as the common vertex.

**Consequences.**
- $A, B, C, D$ are coplanar iff $V = 0$.
- The height from $D$ to face $ABC$ is $h = \dfrac{3V}{\text{area }ABC} = \dfrac{|[\vec{AB}\,\vec{AC}\,\vec{AD}]|}{|\vec{AB}\times\vec{AC}|}$.
- A regular tetrahedron of edge $a$ has $V = \dfrac{a^3}{6\sqrt2}$.

**Example.** $A(1, 1, 1)$, $B(2, 1, 3)$, $C(3, 2, 2)$, $D(3, 3, 4)$:

$$[\vec{AB}\ \vec{AC}\ \vec{AD}] = \begin{vmatrix} 1 & 0 & 2 \\ 2 & 1 & 1 \\ 2 & 2 & 3 \end{vmatrix} = 1(3 - 2) - 0 + 2(4 - 2) = 5, \qquad V = \frac56.$$

**Example (unknown).** If the edges $\hat i + \hat j + \hat k$, $\hat i - \hat j + \lambda\hat k$, $2\hat i + \hat j - \hat k$ give volume $1$, then $\frac16|5 + \lambda| = 1$, so $\lambda = 1$ or $\lambda = -11$. Both values must be listed, because of the modulus.

:::caution
Three traps: dividing by $3$ (or $2$) instead of $6$; using the **position vectors** of $B, C, D$ instead of the edges from $A$ (that is the tetrahedron $OBCD$); and dropping one root when the volume is given and $\lambda$ is unknown.
:::

## Differentiation of vector functions {#vector-differentiation}

A **vector function of a scalar variable** assigns a vector $\vec r(t) = f(t)\hat i + g(t)\hat j + h(t)\hat k$ to each $t$ in an interval. Limits and continuity are taken **componentwise**: $\vec r(t) \to \vec \ell$ iff $|\vec r(t) - \vec\ell| \to 0$ iff each component converges.

**Derivative:**

$$\frac{d\vec r}{dt} = \lim_{h\to 0}\frac{\vec r(t + h) - \vec r(t)}{h} = f'(t)\hat i + g'(t)\hat j + h'(t)\hat k,$$

provided each component is differentiable. Geometrically, $\vec r\,'(t)$ (if non-zero) is **tangent** to the curve traced by $\vec r$. The unit vectors $\hat i, \hat j, \hat k$ are constant, so they are not differentiated.

**Rules** ($\vec u, \vec v, \vec w$ differentiable vector functions, $\varphi$ a differentiable scalar function):

| Expression | Derivative |
|:---|:---|
| $\vec u + \vec v$ | $\vec u\,' + \vec v\,'$ |
| $\varphi\vec u$ | $\varphi'\vec u + \varphi\vec u\,'$ |
| $\vec u\cdot\vec v$ | $\vec u\,'\cdot\vec v + \vec u\cdot\vec v\,'$ |
| $\vec u\times\vec v$ | $\vec u\,'\times\vec v + \vec u\times\vec v\,'$ (keep the order) |
| $[\vec u\,\vec v\,\vec w]$ | $[\vec u\,'\,\vec v\,\vec w] + [\vec u\,\vec v\,'\,\vec w] + [\vec u\,\vec v\,\vec w\,']$ |
| $\vec u\times(\vec v\times\vec w)$ | $\vec u\,'\times(\vec v\times\vec w) + \vec u\times(\vec v\,'\times\vec w) + \vec u\times(\vec v\times\vec w\,')$ |
| $\vec u(\varphi(t))$ (chain rule) | $\dfrac{d\vec u}{d\varphi}\,\varphi'(t)$ |

**Standard consequences.**
- $\dfrac{d}{dt}(\vec r\times\vec r\,') = \vec r\,'\times\vec r\,' + \vec r\times\vec r\,'' = \vec r\times\vec r\,''$.
- $\dfrac{d}{dt}[\vec r\ \vec r\,'\ \vec r\,''] = [\vec r\ \vec r\,'\ \vec r\,''']$: the other two terms have a repeated vector.
- $\dfrac{d}{dt}(\vec r\cdot\vec r) = 2\vec r\cdot\vec r\,'$, so $\vec r\cdot\vec r\,' = |\vec r|\,\dfrac{d|\vec r|}{dt}$.

**Theorem (constant magnitude).** $|\vec r(t)|$ is constant $\iff \vec r\cdot\dfrac{d\vec r}{dt} = 0$ for all $t$. A vector of constant length is perpendicular to its derivative.

**Theorem (constant direction).** For $\vec r(t) \ne \vec 0$, $\vec r$ has constant direction $\iff \vec r\times\dfrac{d\vec r}{dt} = \vec 0$ for all $t$. (Write $\vec r = r\hat r$; then $\vec r\times\vec r\,' = r^2\,\hat r\times\hat r\,'$, and $\hat r\,' \perp \hat r$.)

**Example.** $\vec r = \cos t\,\hat i + \sin t\,\hat j + t\hat k$: $\vec r\,' = -\sin t\,\hat i + \cos t\,\hat j + \hat k$, so $\vec r\cdot\vec r\,' = t$. This is not $0$, consistent with $|\vec r| = \sqrt{1 + t^2}$ not being constant.

:::caution
$\left|\dfrac{d\vec r}{dt}\right|$ and $\dfrac{d|\vec r|}{dt}$ are different. For $\vec r = \cos t\,\hat i + \sin t\,\hat j$, the first is $1$ and the second is $0$.
:::

## Velocity and acceleration {#velocity-acceleration}

If $\vec r(t)$ is the position of a particle at time $t$:

$$\vec v = \frac{d\vec r}{dt}, \qquad \vec a = \frac{d\vec v}{dt} = \frac{d^2\vec r}{dt^2}, \qquad \text{speed} = |\vec v|.$$

The velocity is along the tangent to the path. Splitting the acceleration along the unit tangent $\hat T = \vec v/|\vec v|$ and perpendicular to it:

$$a_T = \frac{\vec v\cdot\vec a}{|\vec v|} = \frac{d|\vec v|}{dt}, \qquad a_N = \frac{|\vec v\times\vec a|}{|\vec v|}, \qquad |\vec a|^2 = a_T^2 + a_N^2.$$

So the speed is constant iff $\vec v\cdot\vec a = 0$. Radial–transverse and intrinsic ($v^2/\rho$) components are treated under Analytical Dynamics.

**Example.** $\vec r = e^{-t}\hat i + 2\cos 3t\,\hat j + 2\sin 3t\,\hat k$.

$$\vec v = -e^{-t}\hat i - 6\sin 3t\,\hat j + 6\cos 3t\,\hat k, \qquad \vec a = e^{-t}\hat i - 18\cos 3t\,\hat j - 18\sin 3t\,\hat k.$$

At $t = 0$: $|\vec v| = \sqrt{1 + 36} = \sqrt{37}$ and $|\vec a| = \sqrt{1 + 324} = 5\sqrt{13}$.

**Example (components).** $\vec r = t\hat i + t^2\hat j + t^3\hat k$ at $t = 1$: $\vec v = (1, 2, 3)$, $\vec a = (0, 2, 6)$. Then $a_T = \frac{22}{\sqrt{14}}$, and $\vec v\times\vec a = (6, -6, 2)$ gives $a_N = \frac{2\sqrt{19}}{\sqrt{14}}$. Check: $a_T^2 + a_N^2 = \frac{484 + 76}{14} = 40 = |\vec a|^2$.

**Uniform circular motion.** $\vec r = R(\cos\omega t\,\hat i + \sin\omega t\,\hat j)$ gives $\vec v \perp \vec r$, $|\vec v| = R\omega$ and $\vec a = -\omega^2\vec r$: the acceleration points to the centre with magnitude $R\omega^2 = v^2/R$.

**Integration** reverses differentiation componentwise: if $\vec a(t)$ is known, $\vec v = \int\vec a\,dt + \vec c$, with the constant **vector** fixed by the initial velocity.

The PG syllabus item V.2 lists only vector functions of a scalar variable, derivatives of sums and products, and velocity and acceleration. Gradient, divergence, curl and directional derivatives are not listed, so they are not covered here.

:::exam-tip
For "speed at $t = t_0$", differentiate once and substitute; for "magnitude of acceleration", differentiate twice. The common slip is to take $|\vec r(t_0)|$, the distance from the origin.
:::

## Quick checks and traps {#exam-tips}

- **Work** uses the displacement $\vec b - \vec a$, never the position vector of the end point.
- **Moment:** $\vec r\times\vec F$ with $\vec r$ **from** the point of reference **to** the line of action. Reversing either gives the negative.
- **Moment about a line:** project onto a **unit** vector along the line.
- **Line in Cartesian form:** the numerators carry the point, the denominators the direction; $\vec r = (2, -1, 3) + t(1, 2, -1)$ is $\frac{x - 2}{1} = \frac{y + 1}{2} = \frac{z - 3}{-1}$.
- **Plane through three points:** normal $\vec{AB}\times\vec{AC}$; check by substituting all three points.
- **Line–plane angle:** $\sin\varphi = \frac{|\vec b\cdot\vec n|}{|\vec b||\vec n|}$.
- **Line parallel to plane:** $\vec b\cdot\vec n = 0$, not $\vec b\times\vec n = \vec 0$ (that is "perpendicular to the plane").
- **Shortest distance:** skew-line formula only when $\vec b_1\times\vec b_2 \ne \vec 0$; for parallel lines use $|(\vec a_2 - \vec a_1)\times\vec b|/|\vec b|$.
- **Coplanar lines** need not intersect: they may be parallel.
- **Tetrahedron:** $\frac16$, edges from a common vertex, absolute value.
- **Derivatives:** keep the order in $\times$; $\frac{d}{dt}(\vec r\times\vec r\,') = \vec r\times\vec r\,''$ and $\frac{d}{dt}[\vec r\,\vec r\,'\,\vec r\,''] = [\vec r\,\vec r\,'\,\vec r\,''']$.
- **Constant length** $\Rightarrow \vec r\perp\vec r\,'$; **constant direction** $\iff \vec r\times\vec r\,' = \vec 0$.
