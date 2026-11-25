# Vector Algebra

## Vectors, components and linear combinations {#vectors-basics}

A **vector** has magnitude and direction and adds by the parallelogram (triangle) law; a **scalar** has magnitude only. A **free vector** may be drawn from any point; a **position vector** (p.v.) of a point $P$ is $\vec{OP}$ for a fixed origin $O$. For points $A, B$ with p.v. $\vec a, \vec b$:

$$\vec{AB} = \vec b - \vec a.$$

**Components.** With the right-handed orthonormal triad $\hat i, \hat j, \hat k$, every vector is uniquely $\vec a = a_1\hat i + a_2\hat j + a_3\hat k$, and

$$|\vec a| = \sqrt{a_1^2 + a_2^2 + a_3^2}, \qquad \hat a = \frac{\vec a}{|\vec a|}\ (\vec a \ne \vec 0).$$

The **direction cosines** of $\vec a$ are the components of $\hat a$: $l = a_1/|\vec a|$, $m = a_2/|\vec a|$, $n = a_3/|\vec a|$, with $l^2 + m^2 + n^2 = 1$. Example: $\vec a = 2\hat i - 3\hat j + 6\hat k$ has $|\vec a| = 7$ and direction cosines $\frac27, -\frac37, \frac67$.

**Addition and scalar multiplication** are componentwise. They are commutative, associative and distributive, so the vectors of space form the real vector space $\R^3$.

**Linear combination:** $\lambda_1\vec a_1 + \cdots + \lambda_n\vec a_n$. The vectors are **linearly dependent** if some combination with not all $\lambda_i = 0$ is $\vec 0$; otherwise they are **independent**.

| Number of vectors | Dependent $\iff$ |
|:---|:---|
| one, $\vec a$ | $\vec a = \vec 0$ |
| two, $\vec a, \vec b$ | collinear (parallel), i.e. $\vec a \times \vec b = \vec 0$ |
| three, $\vec a, \vec b, \vec c$ | coplanar, i.e. $[\vec a\,\vec b\,\vec c] = 0$ |
| four or more in space | always dependent |

**Basis theorem.** If $\vec a, \vec b, \vec c$ are non-coplanar, every vector $\vec r$ is **uniquely** $x\vec a + y\vec b + z\vec c$. By Cramer's rule,

$$x = \frac{[\vec r\,\vec b\,\vec c]}{[\vec a\,\vec b\,\vec c]},\quad y = \frac{[\vec a\,\vec r\,\vec c]}{[\vec a\,\vec b\,\vec c]},\quad z = \frac{[\vec a\,\vec b\,\vec r]}{[\vec a\,\vec b\,\vec c]}.$$

In practice, equate components and solve the $3\times 3$ system.

:::caution
"Coplanar" for three **vectors** means they are parallel to one plane (dependent), not that some particular arrows lie in a plane. Three coplanar vectors need not make one of a **chosen** pair a combination of the other two: $\hat i, 2\hat i, \hat j$ are coplanar, but $\hat j$ is not a combination of $\hat i$ and $2\hat i$. What is true is that **some** one of them is a combination of the others.
:::

## Collinearity, coplanarity and the section formula {#collinearity-coplanarity}

**Section formula.** The point $P$ dividing $AB$ in the ratio $m : n$ has p.v.

$$\text{internally: } \frac{m\vec b + n\vec a}{m + n}, \qquad \text{externally: } \frac{m\vec b - n\vec a}{m - n}\ (m \ne n).$$

The mid-point is $\frac12(\vec a + \vec b)$ and the centroid of triangle $ABC$ is $\frac13(\vec a + \vec b + \vec c)$.

**Collinear points.** $A, B, C$ are collinear $\iff \vec{AB} \parallel \vec{AC} \iff (\vec b - \vec a) \times (\vec c - \vec a) = \vec 0$. Equivalently, there are scalars, **not all zero**, with

$$x\vec a + y\vec b + z\vec c = \vec 0, \qquad x + y + z = 0.$$

**Coplanar points.** $A, B, C, D$ are coplanar $\iff \vec{AB}, \vec{AC}, \vec{AD}$ are coplanar vectors $\iff [\vec{AB}\ \vec{AC}\ \vec{AD}] = 0$. Equivalently, there are scalars, not all zero, with $x\vec a + y\vec b + z\vec c + w\vec d = \vec 0$ and $x + y + z + w = 0$.

**Example (collinear).** Find $\lambda$ so that $A(2, -1, 3)$, $B(3, -5, 1)$, $C(-1, \lambda, 9)$ are collinear. $\vec{AB} = (1, -4, -2)$ and $\vec{AC} = (-3, \lambda + 1, 6)$. The $x$- and $z$-components force $\vec{AC} = -3\,\vec{AB}$, so $\lambda + 1 = 12$, $\lambda = 11$.

**Example (coplanar).** $A(3,2,1)$, $B(4,\lambda,5)$, $C(4,2,-2)$, $D(6,5,-1)$:

$$\begin{vmatrix} 1 & \lambda - 2 & 4 \\ 1 & 0 & -3 \\ 3 & 3 & -2 \end{vmatrix} = 35 - 7\lambda = 0 \;\Rightarrow\; \lambda = 5.$$

:::exam-tip
For collinearity questions, match the components that contain no unknown first: they fix the scalar multiple at once, and the remaining component gives the unknown. Always check that the fixed multiple is consistent with **every** known component.
:::

:::caution
In the external section formula the denominator is $m - n$, and $\vec b$ (the second end-point) carries the coefficient $m$. Swapping the roles of $\vec a$ and $\vec b$ is the commonest slip.
:::

## Scalar product: angle and projection {#scalar-product}

$$\vec a \cdot \vec b = |\vec a|\,|\vec b|\cos\theta = a_1b_1 + a_2b_2 + a_3b_3, \qquad 0 \le \theta \le \pi.$$

**Properties.** Commutative; distributive over addition; $\vec a \cdot \vec a = |\vec a|^2$; $\hat i\cdot\hat i = 1$, $\hat i\cdot\hat j = 0$, and so on. For non-zero vectors, $\vec a \cdot \vec b = 0 \iff \vec a \perp \vec b$.

**Angle:** $\cos\theta = \dfrac{\vec a\cdot\vec b}{|\vec a|\,|\vec b|}$. The angle is acute, right or obtuse as $\vec a\cdot\vec b$ is $>0$, $=0$ or $<0$.

**Projection.** The scalar projection (component) of $\vec a$ on $\vec b$ and the vector projection are

$$\frac{\vec a\cdot\vec b}{|\vec b|}, \qquad \left(\frac{\vec a\cdot\vec b}{|\vec b|^2}\right)\vec b.$$

Example: $\vec a = 2\hat i - \hat j + 2\hat k$, $\vec b = \hat i + 2\hat j - 2\hat k$: $\vec a\cdot\vec b = -4$, $|\vec b| = 3$, so the component of $\vec a$ along $\vec b$ is $-\frac43$ (it points against $\vec b$).

**Useful identities:**

$$|\vec a \pm \vec b|^2 = |\vec a|^2 + |\vec b|^2 \pm 2\,\vec a\cdot\vec b, \qquad (\vec a + \vec b)\cdot(\vec a - \vec b) = |\vec a|^2 - |\vec b|^2.$$

Consequences: $|\vec a + \vec b| = |\vec a - \vec b| \iff \vec a \perp \vec b$ (the diagonals of a rectangle are equal); the diagonals of a rhombus are perpendicular.

**Cauchy–Schwarz:** $|\vec a\cdot\vec b| \le |\vec a|\,|\vec b|$, with equality iff $\vec a, \vec b$ are parallel. The triangle inequality $|\vec a + \vec b| \le |\vec a| + |\vec b|$ follows.

**Solved example.** If $\vec a + \vec b + \vec c = \vec 0$ with $|\vec a| = 3$, $|\vec b| = 5$, $|\vec c| = 7$, then $|\vec a + \vec b|^2 = |\vec c|^2$ gives $9 + 25 + 2\,\vec a\cdot\vec b = 49$, so $\vec a\cdot\vec b = \frac{15}{2}$ and $\cos\theta = \frac12$: the angle between $\vec a$ and $\vec b$ is $\frac{\pi}{3}$.

:::caution
In that example the vectors form a triangle **head to tail**, so the angle of the triangle between those sides is $\pi - \frac{\pi}{3} = \frac{2\pi}{3}$, not the angle between the vectors. Always compute $\theta$ from $\vec a\cdot\vec b$.
:::

:::exam-tip
"Collinear" means $\theta = 0$ **or** $\pi$. The condition $\vec a\cdot\vec b = |\vec a|\,|\vec b|$ alone gives only $\theta = 0$ (same direction).
:::

## Vector product: area and normals {#vector-product}

$$\vec a \times \vec b = |\vec a|\,|\vec b|\sin\theta\;\hat n = \begin{vmatrix} \hat i & \hat j & \hat k \\ a_1 & a_2 & a_3 \\ b_1 & b_2 & b_3 \end{vmatrix},$$

where $\hat n$ is the unit vector perpendicular to both, such that $\vec a, \vec b, \hat n$ is right-handed.

**Properties.**
- **Anti-commutative:** $\vec b \times \vec a = -\,\vec a \times \vec b$; hence $\vec a \times \vec a = \vec 0$.
- Distributive over addition; $(\lambda\vec a)\times\vec b = \lambda(\vec a\times\vec b)$.
- **Not associative:** $\hat i \times (\hat i \times \hat j) = \hat i \times \hat k = -\hat j$, but $(\hat i \times \hat i)\times\hat j = \vec 0$.
- $\hat i\times\hat j = \hat k$, $\hat j\times\hat k = \hat i$, $\hat k\times\hat i = \hat j$ (cyclic).
- For non-zero $\vec a, \vec b$: $\vec a \times \vec b = \vec 0 \iff \vec a \parallel \vec b$.

**Geometric meaning.**

| Quantity | Formula |
|:---|:---|
| area of parallelogram, sides $\vec a, \vec b$ | $\lvert\vec a\times\vec b\rvert$ |
| area of triangle, sides $\vec a, \vec b$ | $\frac12\lvert\vec a\times\vec b\rvert$ |
| area of triangle $ABC$ | $\frac12\lvert\vec a\times\vec b + \vec b\times\vec c + \vec c\times\vec a\rvert$ |
| area of parallelogram with diagonals $\vec d_1, \vec d_2$ | $\frac12\lvert\vec d_1\times\vec d_2\rvert$ |
| unit vectors $\perp$ to $\vec a$ and $\vec b$ | $\pm\dfrac{\vec a\times\vec b}{\lvert\vec a\times\vec b\rvert}$ |
| $\sin\theta$ | $\dfrac{\lvert\vec a\times\vec b\rvert}{\lvert\vec a\rvert\lvert\vec b\rvert}$ |

**Example.** $\vec a = \hat i + 2\hat j + 3\hat k$, $\vec b = 3\hat i - 2\hat j + \hat k$:

$$\vec a\times\vec b = (2\cdot1 - 3\cdot(-2))\hat i - (1\cdot1 - 3\cdot3)\hat j + (1\cdot(-2) - 2\cdot3)\hat k = 8\hat i + 8\hat j - 8\hat k.$$

The parallelogram has area $8\sqrt3$; the triangle on the same sides has area $4\sqrt3$.

**Cancellation.** $\vec a\cdot\vec b = \vec a\cdot\vec c$ alone does not give $\vec b = \vec c$ (only $\vec a \perp (\vec b - \vec c)$), and $\vec a\times\vec b = \vec a\times\vec c$ alone gives only $\vec a \parallel (\vec b - \vec c)$. **Both together** with $\vec a \ne \vec 0$ force $\vec b = \vec c$, since a non-zero vector cannot be both parallel and perpendicular to $\vec a$.

:::caution
Watch the sign of the middle ($\hat j$) term in the determinant expansion: it is $-(a_1b_3 - a_3b_1)$. A quick check: the answer must be perpendicular to both $\vec a$ and $\vec b$.
:::

Moment of a force and the vector equations of lines and planes use the cross product but belong to **Vector Applications and Calculus**.

## Scalar triple product: volume and coplanarity {#scalar-triple-product}

$$[\vec a\,\vec b\,\vec c] = \vec a\cdot(\vec b\times\vec c) = \begin{vmatrix} a_1 & a_2 & a_3 \\ b_1 & b_2 & b_3 \\ c_1 & c_2 & c_3 \end{vmatrix}.$$

**Geometric meaning.** $\lvert[\vec a\,\vec b\,\vec c]\rvert$ is the **volume of the parallelepiped** with coterminous edges $\vec a, \vec b, \vec c$ (base area $|\vec b\times\vec c|$ times height $|\vec a|\,|\cos\varphi|$). The sign is $+$ iff $\vec a, \vec b, \vec c$ is a right-handed system. (The tetrahedron on the same edges has one-sixth of this volume; that application is in the next topic.)

**Properties** (all from determinant properties):
- **Cyclic invariance:** $[\vec a\,\vec b\,\vec c] = [\vec b\,\vec c\,\vec a] = [\vec c\,\vec a\,\vec b]$; swapping two vectors changes the sign: $[\vec a\,\vec c\,\vec b] = -[\vec a\,\vec b\,\vec c]$.
- **Dot and cross may be interchanged:** $\vec a\cdot(\vec b\times\vec c) = (\vec a\times\vec b)\cdot\vec c$.
- A repeated (or parallel) vector gives $0$: $[\vec a\,\vec a\,\vec b] = 0$.
- Linear in each slot, so $[\lambda\vec a\ \lambda\vec b\ \lambda\vec c] = \lambda^3[\vec a\,\vec b\,\vec c]$.
- $[\hat i\,\hat j\,\hat k] = 1$.

**Coplanarity test.** $\vec a, \vec b, \vec c$ are coplanar $\iff [\vec a\,\vec b\,\vec c] = 0$.

**Standard results.**

$$[\vec a + \vec b\ \ \vec b + \vec c\ \ \vec c + \vec a] = 2[\vec a\,\vec b\,\vec c], \qquad [\vec a - \vec b\ \ \vec b - \vec c\ \ \vec c - \vec a] = 0,$$

$$[\vec a\times\vec b\ \ \vec b\times\vec c\ \ \vec c\times\vec a] = [\vec a\,\vec b\,\vec c]^2.$$

**Gram determinant.** Multiplying the determinant by its transpose,

$$[\vec a\,\vec b\,\vec c]^2 = \begin{vmatrix} \vec a\cdot\vec a & \vec a\cdot\vec b & \vec a\cdot\vec c \\ \vec b\cdot\vec a & \vec b\cdot\vec b & \vec b\cdot\vec c \\ \vec c\cdot\vec a & \vec c\cdot\vec b & \vec c\cdot\vec c \end{vmatrix}.$$

This gives the volume from lengths and angles alone. Example: unit vectors with every pairwise angle $\frac{\pi}{3}$ give $[\vec a\,\vec b\,\vec c]^2 = \frac12$, volume $\frac{1}{\sqrt2}$.

**Example (coplanar vectors).** $2\hat i - \hat j + \hat k$, $\hat i + 2\hat j - 3\hat k$, $3\hat i + \lambda\hat j + 5\hat k$ are coplanar iff

$$\begin{vmatrix} 2 & -1 & 1 \\ 1 & 2 & -3 \\ 3 & \lambda & 5 \end{vmatrix} = 7\lambda + 28 = 0 \iff \lambda = -4.$$

:::exam-tip
Expressions like $[\vec a + \vec b\ \ \vec b + \vec c\ \ \vec c + \vec a]$ are determinants of a coefficient matrix times $[\vec a\,\vec b\,\vec c]$: here $\det\begin{pmatrix}1&1&0\\0&1&1\\1&0&1\end{pmatrix} = 2$.
:::

## Vector triple product, Lagrange identity and four vectors {#vector-triple-product}

**Vector triple product** ("bac minus cab"):

$$\vec a\times(\vec b\times\vec c) = (\vec a\cdot\vec c)\,\vec b - (\vec a\cdot\vec b)\,\vec c, \qquad (\vec a\times\vec b)\times\vec c = (\vec a\cdot\vec c)\,\vec b - (\vec b\cdot\vec c)\,\vec a.$$

$\vec a\times(\vec b\times\vec c)$ lies in the plane of $\vec b$ and $\vec c$ and is perpendicular to $\vec a$. The two bracketings differ:

$$\vec a\times(\vec b\times\vec c) - (\vec a\times\vec b)\times\vec c = (\vec b\cdot\vec c)\,\vec a - (\vec a\cdot\vec b)\,\vec c = (\vec c\times\vec a)\times\vec b,$$

so they are equal **iff** $(\vec c\times\vec a)\times\vec b = \vec 0$, i.e. iff $\vec b$ and $\vec c\times\vec a$ are parallel (either may be $\vec 0$). In particular they are equal when $\vec a \parallel \vec c$, or when $\vec b$ is perpendicular to both $\vec a$ and $\vec c$.

**Jacobi identity:** $\vec a\times(\vec b\times\vec c) + \vec b\times(\vec c\times\vec a) + \vec c\times(\vec a\times\vec b) = \vec 0$.

**Products of four vectors.**

$$(\vec a\times\vec b)\cdot(\vec c\times\vec d) = \begin{vmatrix} \vec a\cdot\vec c & \vec a\cdot\vec d \\ \vec b\cdot\vec c & \vec b\cdot\vec d \end{vmatrix} = (\vec a\cdot\vec c)(\vec b\cdot\vec d) - (\vec a\cdot\vec d)(\vec b\cdot\vec c),$$

$$(\vec a\times\vec b)\times(\vec c\times\vec d) = [\vec a\,\vec b\,\vec d]\,\vec c - [\vec a\,\vec b\,\vec c]\,\vec d = [\vec a\,\vec c\,\vec d]\,\vec b - [\vec b\,\vec c\,\vec d]\,\vec a.$$

The second identity shows the vector lies along the line of intersection of the plane of $\vec a, \vec b$ and the plane of $\vec c, \vec d$. Equating the two forms gives the expansion of any $\vec d$ in a non-coplanar basis:

$$[\vec a\,\vec b\,\vec c]\,\vec d = [\vec d\,\vec b\,\vec c]\,\vec a + [\vec a\,\vec d\,\vec c]\,\vec b + [\vec a\,\vec b\,\vec d]\,\vec c.$$

**Lagrange's identity** (put $\vec c = \vec a$, $\vec d = \vec b$):

$$|\vec a\times\vec b|^2 = |\vec a|^2|\vec b|^2 - (\vec a\cdot\vec b)^2,$$

which is $\sin^2\theta + \cos^2\theta = 1$ in disguise. Example: $|\vec a| = 2$, $|\vec b| = 5$, $\vec a\cdot\vec b = 6$ give $|\vec a\times\vec b| = \sqrt{100 - 36} = 8$.

**Solving a vector equation.** Find $\vec r$ with $\vec r\times\vec b = \vec a\times\vec b$ and $\vec r\cdot\vec c = 0$ (where $\vec b\cdot\vec c \ne 0$). The first gives $\vec r = \vec a + t\vec b$; the second gives $t = -\dfrac{\vec a\cdot\vec c}{\vec b\cdot\vec c}$.

**Reciprocal system** (not named in the SLST syllabus; one line): for $[\vec a\,\vec b\,\vec c] \ne 0$, $\vec a' = \dfrac{\vec b\times\vec c}{[\vec a\,\vec b\,\vec c]}$ and cyclically, so that $\vec a\cdot\vec a' = 1$, $\vec a\cdot\vec b' = 0$, and $[\vec a'\,\vec b'\,\vec c'][\vec a\,\vec b\,\vec c] = 1$.

:::caution
In $(\vec a\times\vec b)\times(\vec c\times\vec d)$ the answer $[\vec a\,\vec b\,\vec d]\vec c - [\vec a\,\vec b\,\vec c]\vec d$ has $\vec d$ inside the **first** bracket. Check the order with $\vec a = \hat i$, $\vec b = \hat j$, $\vec c = \hat k$, $\vec d = \hat i$: the left side is $\hat k\times\hat j = -\hat i$, and the formula gives $0\cdot\hat k - 1\cdot\hat i = -\hat i$.
:::

## Quick checks and traps {#exam-tips}

- **Projection vs cosine:** the component of $\vec a$ on $\vec b$ divides $\vec a\cdot\vec b$ by $|\vec b|$ only; $\cos\theta$ divides by $|\vec a|\,|\vec b|$.
- **Triangle vs parallelogram:** area uses $\frac12|\vec a\times\vec b|$ for a triangle; volume of a parallelepiped is $\lvert[\vec a\,\vec b\,\vec c]\rvert$ with no factor.
- **Perpendicular check:** any computed $\vec a\times\vec b$ must have zero dot product with both $\vec a$ and $\vec b$.
- **Scaling:** $[\lambda\vec a\ \lambda\vec b\ \lambda\vec c] = \lambda^3[\vec a\,\vec b\,\vec c]$ and $[\vec a\times\vec b\ \ \vec b\times\vec c\ \ \vec c\times\vec a] = [\vec a\,\vec b\,\vec c]^2$, so this vanishes exactly when $\vec a, \vec b, \vec c$ are coplanar.
- **$|\vec a\times\vec b| = \vec a\cdot\vec b$** (both non-zero) means $\tan\theta = 1$, $\theta = \frac{\pi}{4}$.
- **Linear dependence:** four vectors in space are always dependent; three are dependent iff coplanar; two iff parallel.
- **Cyclic shortcut:** $\hat i\to\hat j\to\hat k\to\hat i$ gives $+$; going against the cycle gives $-$.
- **Vector triple product** is never associative in general; $\vec a\times(\vec b\times\vec c)$ lies in the plane of $\vec b, \vec c$, while $(\vec a\times\vec b)\times\vec c$ lies in the plane of $\vec a, \vec b$.
- **Non-coplanar check:** $\hat i + \hat j$, $\hat j + \hat k$, $\hat k + \hat i$ have triple product $2$, so they are **not** coplanar.
- **Out of scope here:** vector equations of lines and planes, work done, moment of a force, tetrahedron volume and differentiation of vector functions are in *Vector Applications and Calculus*.
