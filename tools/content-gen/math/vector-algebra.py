import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from qlib import Topic, eq

T = Topic("math.vectors.vector-algebra")

# q1
T.single(1, ["scalar-product"],
    r"The scalar projection (component) of $\vec a = 2\hat i - \hat j + 2\hat k$ on $\vec b = \hat i + 2\hat j - 2\hat k$ is",
    [r"$-\frac{4}{3}$", r"$\frac{4}{3}$", r"$-\frac{4}{9}$", r"$-4$"],
    r"""$$\vec a\cdot\vec b = 2 - 2 - 4 = -4, \qquad |\vec b| = \sqrt{1 + 4 + 4} = 3,$$
so the component of $\vec a$ along $\vec b$ is
$$\frac{\vec a\cdot\vec b}{|\vec b|} = -\frac{4}{3}.$$

$-\frac49$ divides by $|\vec b|^2$: that is the coefficient of $\vec b$ in the vector projection, not the scalar projection. $\frac43$ drops the sign; the negative sign says $\vec a$ leans against $\vec b$.""")

# q2
T.single(1, ["vector-product"],
    r"The area of the parallelogram with adjacent sides $\vec a = \hat i + 2\hat j + 3\hat k$ and $\vec b = 3\hat i - 2\hat j + \hat k$ is",
    [r"$8\sqrt{3}$", r"$4\sqrt{3}$", r"$14$", r"$192$"],
    r"""$$\vec a\times\vec b = \begin{vmatrix} \hat i & \hat j & \hat k \\ 1 & 2 & 3 \\ 3 & -2 & 1 \end{vmatrix} = 8\hat i + 8\hat j - 8\hat k,$$
$$|\vec a\times\vec b| = \sqrt{64 \cdot 3} = 8\sqrt3.$$

$4\sqrt3$ is the area of the **triangle** on these sides. $14 = |\vec a|\,|\vec b|$ forgets the factor $\sin\theta$, and $192$ is $|\vec a\times\vec b|^2$.

**Check:** $(8, 8, -8)\cdot(1, 2, 3) = 0$ and $(8, 8, -8)\cdot(3, -2, 1) = 0$.""")

# q3
T.single(1, ["scalar-triple-product"],
    r"The volume of the parallelepiped with coterminous edges $\hat i + 2\hat j + 3\hat k$, $\hat j + 2\hat k$ and $2\hat i + \hat k$ is",
    [r"$3$", r"$\frac{1}{2}$", r"$\frac{3}{2}$", r"$9$"],
    r"""The volume is the absolute value of the scalar triple product:
$$\begin{vmatrix} 1 & 2 & 3 \\ 0 & 1 & 2 \\ 2 & 0 & 1 \end{vmatrix} = 1(1 - 0) - 2(0 - 4) + 3(0 - 2) = 1 + 8 - 6 = 3.$$

$\frac12 = \frac{3}{6}$ is the volume of the **tetrahedron** on the same edges, and $\frac32$ wrongly halves as for a triangle. A parallelepiped takes no factor.""")

# q4
T.single(1, ["collinearity-coplanarity"],
    r"The points with position vectors $2\hat i - \hat j + 3\hat k$, $3\hat i - 5\hat j + \hat k$ and $-\hat i + \lambda\hat j + 9\hat k$ are collinear. Then $\lambda$ equals",
    [r"$11$", r"$-13$", r"$13$", r"$7$"],
    r"""$$\vec{AB} = \hat i - 4\hat j - 2\hat k, \qquad \vec{AC} = -3\hat i + (\lambda + 1)\hat j + 6\hat k.$$
The $\hat i$- and $\hat k$-components force $\vec{AC} = -3\,\vec{AB}$. Then the $\hat j$-component gives
$$\lambda + 1 = (-3)(-4) = 12 \;\Rightarrow\; \lambda = 11.$$

$-13$ comes from the sign slip $\lambda + 1 = -12$; $13$ from writing $\lambda - 1 = 12$.""")

# q5
T.single(1, ["vectors-basics"],
    r"The direction cosines of the vector $2\hat i - 3\hat j + 6\hat k$ are",
    [r"$\frac{2}{7}, -\frac{3}{7}, \frac{6}{7}$", r"$\frac{2}{7}, \frac{3}{7}, \frac{6}{7}$", r"$\frac{2}{5}, -\frac{3}{5}, \frac{6}{5}$", r"$\frac{2}{49}, -\frac{3}{49}, \frac{6}{49}$"],
    r"""$|\vec a| = \sqrt{4 + 9 + 36} = 7$, and the direction cosines are the components of $\hat a = \vec a/7$:
$$l, m, n = \frac27,\ -\frac37,\ \frac67, \qquad l^2 + m^2 + n^2 = \frac{4 + 9 + 36}{49} = 1.$$

Dropping the minus sign gives a different direction. Dividing by $2 - 3 + 6 = 5$ or by $|\vec a|^2 = 49$ fails the check $l^2 + m^2 + n^2 = 1$.""")

# q6
T.single(1, ["scalar-product"],
    r"The vectors $2\hat i + \lambda\hat j + \hat k$ and $\hat i - 2\hat j + 3\hat k$ are perpendicular when $\lambda$ equals",
    [r"$\frac{5}{2}$", r"$-\frac{5}{2}$", r"$\frac{1}{2}$", r"$5$"],
    r"""Perpendicular non-zero vectors have zero dot product:
$$2\cdot 1 + \lambda\cdot(-2) + 1\cdot 3 = 5 - 2\lambda = 0 \;\Rightarrow\; \lambda = \frac52.$$

$-\frac52$ forgets the sign of $-2$; $\frac12$ drops the term $3$ from $\hat k$.""")

# q7
T.single(2, ["vector-product"],
    r"A unit vector perpendicular to both $\hat i + \hat j + \hat k$ and $\hat i - \hat j$ is",
    [r"$\frac{1}{\sqrt6}(\hat i + \hat j - 2\hat k)$", r"$\frac{1}{\sqrt6}(\hat i + \hat j + 2\hat k)$", r"$\frac{1}{\sqrt6}(\hat i - \hat j + 2\hat k)$", r"$\frac{1}{\sqrt6}(2\hat i - \hat j - \hat k)$"],
    r"""$$\vec a\times\vec b = \begin{vmatrix} \hat i & \hat j & \hat k \\ 1 & 1 & 1 \\ 1 & -1 & 0 \end{vmatrix} = (0 + 1)\hat i - (0 - 1)\hat j + (-1 - 1)\hat k = \hat i + \hat j - 2\hat k,$$
with modulus $\sqrt6$. So the unit vectors are $\pm\frac{1}{\sqrt6}(\hat i + \hat j - 2\hat k)$.

**Check the others by dot products:** $(1, 1, 2)\cdot(1, 1, 1) = 4 \ne 0$; $(1, -1, 2)\cdot(1, -1, 0) = 2 \ne 0$; $(2, -1, -1)\cdot(1, -1, 0) = 3 \ne 0$. Each fails to be perpendicular to one of the vectors.""")

# q8
T.single(2, ["scalar-triple-product"],
    r"The vectors $2\hat i - \hat j + \hat k$, $\hat i + 2\hat j - 3\hat k$ and $3\hat i + \lambda\hat j + 5\hat k$ are coplanar if $\lambda$ equals",
    [r"$-4$", r"$4$", r"$-2$", r"$2$"],
    r"""Coplanar $\iff$ the scalar triple product is $0$:
$$\begin{vmatrix} 2 & -1 & 1 \\ 1 & 2 & -3 \\ 3 & \lambda & 5 \end{vmatrix} = 2(10 + 3\lambda) + (5 + 9) + (\lambda - 6) = 7\lambda + 28.$$
So $\lambda = -4$.

The middle term is $-(-1)(5 + 9) = +14$; $\lambda = 4$ is the root of $7\lambda - 28$, a sign slip when solving.""")

# q9
T.single(2, ["collinearity-coplanarity"],
    r"The position vector of the point dividing the join of the points with position vectors $2\vec a + \vec b$ and $\vec a - 3\vec b$ **externally** in the ratio $1 : 2$ is",
    [r"$3\vec a + 5\vec b$", r"$\frac{1}{3}(5\vec a - \vec b)$", r"$-3\vec a - 5\vec b$", r"$-7\vec b$"],
    r"""With $P = 2\vec a + \vec b$, $Q = \vec a - 3\vec b$ and ratio $m : n = 1 : 2$, the external point is
$$\frac{m\,Q - n\,P}{m - n} = \frac{(\vec a - 3\vec b) - 2(2\vec a + \vec b)}{1 - 2} = \frac{-3\vec a - 5\vec b}{-1} = 3\vec a + 5\vec b.$$

$\frac13(5\vec a - \vec b)$ is the **internal** point $\frac{Q + 2P}{3}$. $-3\vec a - 5\vec b$ forgets to divide by $m - n = -1$. $-7\vec b$ swaps the roles of the two end-points: $\frac{P - 2Q}{1 - 2}$.""")

# q10
T.single(2, ["vector-triple-product"],
    r"For $\vec a = \hat i + \hat j$, $\vec b = \hat j + \hat k$, $\vec c = \hat k + \hat i$, the vector $\vec a\times(\vec b\times\vec c)$ is",
    [r"$-\hat i + \hat j$", r"$\hat i - \hat j$", r"$-\hat i + \hat k$", r"$\hat j + \hat k$"],
    r"""Use $\vec a\times(\vec b\times\vec c) = (\vec a\cdot\vec c)\vec b - (\vec a\cdot\vec b)\vec c$. Here $\vec a\cdot\vec c = 1$ and $\vec a\cdot\vec b = 1$, so
$$\vec a\times(\vec b\times\vec c) = \vec b - \vec c = -\hat i + \hat j.$$

$-\hat i + \hat k$ is $(\vec a\times\vec b)\times\vec c = (\vec a\cdot\vec c)\vec b - (\vec b\cdot\vec c)\vec a = \vec b - \vec a$: the other bracketing. $\hat i - \hat j$ has the sign of the expansion reversed.

**Check:** the answer must be perpendicular to $\vec a$: $(-1, 1, 0)\cdot(1, 1, 0) = 0$.""")

# q11
T.assertion_reason(2, ["scalar-triple-product"],
    r"If $\vec a, \vec b, \vec c$ are coplanar, then $\vec a\times\vec b$, $\vec b\times\vec c$, $\vec c\times\vec a$ are also coplanar.",
    r"$[\vec a\times\vec b\ \ \vec b\times\vec c\ \ \vec c\times\vec a] = [\vec a\,\vec b\,\vec c]^2$ for all vectors $\vec a, \vec b, \vec c$.",
    0,
    r"""Both are true, and R explains A.

R is a standard identity: expand $(\vec b\times\vec c)\times(\vec c\times\vec a) = [\vec b\,\vec c\,\vec a]\,\vec c$ by the four-vector formula, then dot with $\vec a\times\vec b$ to get $[\vec a\,\vec b\,\vec c]^2$.

If $\vec a, \vec b, \vec c$ are coplanar, $[\vec a\,\vec b\,\vec c] = 0$, so by R the triple product of the cross products is $0$: they are coplanar. (Indeed all three cross products are then parallel to the common normal.)""")

# q12
T.single(2, ["vector-triple-product"],
    r"If $|\vec a| = 2$, $|\vec b| = 5$ and $\vec a\cdot\vec b = 6$, then $|\vec a\times\vec b|$ equals",
    [r"$8$", r"$64$", r"$2\sqrt{34}$", r"$4$"],
    r"""By Lagrange's identity,
$$|\vec a\times\vec b|^2 = |\vec a|^2|\vec b|^2 - (\vec a\cdot\vec b)^2 = 100 - 36 = 64,$$
so $|\vec a\times\vec b| = 8$.

$64$ forgets the square root; $2\sqrt{34} = \sqrt{136}$ adds $(\vec a\cdot\vec b)^2$ instead of subtracting it.""")

# q13
T.single(2, ["scalar-product"],
    r"If $|\vec a| = 3$, $|\vec b| = 4$ and the angle between $\vec a$ and $\vec b$ is $\frac{\pi}{3}$, then $|\vec a + \vec b|$ equals",
    [r"$\sqrt{37}$", r"$\sqrt{13}$", r"$7$", r"$5$"],
    r"""$$|\vec a + \vec b|^2 = |\vec a|^2 + |\vec b|^2 + 2|\vec a||\vec b|\cos\frac{\pi}{3} = 9 + 16 + 12 = 37.$$

$\sqrt{13}$ is $|\vec a - \vec b|$; $7$ would need $\theta = 0$; $5$ would need $\theta = \frac{\pi}{2}$.""")

# q14
T.statements(1, ["vector-product"],
    r"For vectors $\vec a, \vec b, \vec c$ in space, consider the following statements:",
    [r"$\vec b\times\vec a = -\,\vec a\times\vec b$",
     r"$\vec a\times(\vec b\times\vec c) = (\vec a\times\vec b)\times\vec c$ for all $\vec a, \vec b, \vec c$",
     r"If $\vec a, \vec b$ are non-zero and $\vec a\times\vec b = \vec 0$, then $\vec a$ and $\vec b$ are parallel."],
    [r"1 and 3 only", r"1, 2 and 3", r"1 only", r"2 and 3 only"],
    r"""Statement 1 is anti-commutativity. Statement 3 holds because $|\vec a\times\vec b| = |\vec a||\vec b|\sin\theta = 0$ with non-zero lengths forces $\sin\theta = 0$, so $\theta = 0$ or $\pi$.

Statement 2 is false: the cross product is not associative. With $\vec a = \vec b = \hat i$, $\vec c = \hat j$:
$$\hat i\times(\hat i\times\hat j) = \hat i\times\hat k = -\hat j, \qquad (\hat i\times\hat i)\times\hat j = \vec 0.$$""")

# q15
T.single(2, ["scalar-triple-product"],
    r"If $[\vec a\,\vec b\,\vec c] = 3$, then $[\vec a + \vec b\ \ \vec b + \vec c\ \ \vec c + \vec a]$ equals",
    [r"$6$", r"$0$", r"$3$", r"$9$"],
    r"""Each new vector is a combination of $\vec a, \vec b, \vec c$ with coefficient rows $(1,1,0), (0,1,1), (1,0,1)$. So
$$[\vec a + \vec b\ \ \vec b + \vec c\ \ \vec c + \vec a] = \begin{vmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 1 \end{vmatrix}[\vec a\,\vec b\,\vec c] = 2 \cdot 3 = 6.$$

$0$ is the value for $[\vec a - \vec b\ \ \vec b - \vec c\ \ \vec c - \vec a]$, whose three vectors add to $\vec 0$. $3$ forgets the second surviving term $[\vec b\,\vec c\,\vec a]$ in the expansion.""")

# q16
T.match(2, ["scalar-product", "vector-product"],
    r"Let $\vec a = \hat i + 2\hat j + 2\hat k$ and $\vec b = 3\hat i + 4\hat k$. Match each quantity in List I with its value in List II.",
    [r"$\vec a\cdot\vec b$", r"the scalar projection of $\vec a$ on $\vec b$", r"the area of the triangle with sides $\vec a$, $\vec b$", r"the cosine of the angle between $\vec a$ and $\vec b$"],
    [r"$\frac{11}{15}$", r"$\sqrt{26}$", r"$11$", r"$\frac{11}{5}$"],
    [r"A-3, B-4, C-2, D-1", r"A-3, B-1, C-2, D-4", r"A-4, B-3, C-2, D-1", r"A-3, B-4, C-1, D-2"],
    r"""$|\vec a| = 3$, $|\vec b| = 5$ and $\vec a\cdot\vec b = 3 + 0 + 8 = 11$ (A-3).

- B: $\dfrac{\vec a\cdot\vec b}{|\vec b|} = \dfrac{11}{5}$ (B-4).
- C: $\vec a\times\vec b = 8\hat i + 2\hat j - 6\hat k$, $|\vec a\times\vec b| = \sqrt{104} = 2\sqrt{26}$, so the triangle has area $\sqrt{26}$ (C-2).
- D: $\cos\theta = \dfrac{11}{3\cdot 5} = \dfrac{11}{15}$ (D-1).

Swapping B and D confuses the projection (divide by $|\vec b|$) with the cosine (divide by $|\vec a||\vec b|$).""")

# q17
T.single(2, ["vector-triple-product"],
    r"For all vectors $\vec a, \vec b, \vec c, \vec d$, the product $(\vec a\times\vec b)\cdot(\vec c\times\vec d)$ equals",
    [r"$(\vec a\cdot\vec c)(\vec b\cdot\vec d) - (\vec a\cdot\vec d)(\vec b\cdot\vec c)$", r"$(\vec a\cdot\vec d)(\vec b\cdot\vec c) - (\vec a\cdot\vec c)(\vec b\cdot\vec d)$", r"$(\vec a\cdot\vec b)(\vec c\cdot\vec d) - (\vec a\cdot\vec d)(\vec b\cdot\vec c)$", r"$(\vec a\cdot\vec c)(\vec b\cdot\vec d) + (\vec a\cdot\vec d)(\vec b\cdot\vec c)$"],
    r"""Swap dot and cross, then expand the vector triple product:
$$(\vec a\times\vec b)\cdot(\vec c\times\vec d) = \vec a\cdot\big(\vec b\times(\vec c\times\vec d)\big) = \vec a\cdot\big((\vec b\cdot\vec d)\vec c - (\vec b\cdot\vec c)\vec d\big),$$
which is $\begin{vmatrix} \vec a\cdot\vec c & \vec a\cdot\vec d \\ \vec b\cdot\vec c & \vec b\cdot\vec d \end{vmatrix}$.

**Check with** $\vec c = \vec a$, $\vec d = \vec b$: the answer must give Lagrange's $|\vec a|^2|\vec b|^2 - (\vec a\cdot\vec b)^2 \ge 0$. The reversed option gives its negative, and the "$+$" option gives $|\vec a|^2|\vec b|^2 + (\vec a\cdot\vec b)^2$.""")

# q18
T.single(3, ["vector-triple-product"],
    r"For all vectors $\vec a, \vec b, \vec c, \vec d$, the vector $(\vec a\times\vec b)\times(\vec c\times\vec d)$ equals",
    [r"$[\vec a\,\vec b\,\vec d]\,\vec c - [\vec a\,\vec b\,\vec c]\,\vec d$", r"$[\vec a\,\vec b\,\vec c]\,\vec d - [\vec a\,\vec b\,\vec d]\,\vec c$", r"$[\vec b\,\vec c\,\vec d]\,\vec a - [\vec a\,\vec c\,\vec d]\,\vec b$", r"$[\vec a\,\vec b\,\vec d]\,\vec c + [\vec a\,\vec b\,\vec c]\,\vec d$"],
    r"""Treat $\vec u = \vec a\times\vec b$ as one vector: $\vec u\times(\vec c\times\vec d) = (\vec u\cdot\vec d)\vec c - (\vec u\cdot\vec c)\vec d$, and $\vec u\cdot\vec d = [\vec a\,\vec b\,\vec d]$, $\vec u\cdot\vec c = [\vec a\,\vec b\,\vec c]$. So
$$(\vec a\times\vec b)\times(\vec c\times\vec d) = [\vec a\,\vec b\,\vec d]\,\vec c - [\vec a\,\vec b\,\vec c]\,\vec d.$$

The other true form is $[\vec a\,\vec c\,\vec d]\,\vec b - [\vec b\,\vec c\,\vec d]\,\vec a$; the option $[\vec b\,\vec c\,\vec d]\vec a - [\vec a\,\vec c\,\vec d]\vec b$ is its **negative**.

**Check:** $\vec a = \hat i$, $\vec b = \hat j$, $\vec c = \hat k$, $\vec d = \hat i$ gives $\hat k\times\hat j = -\hat i$ on the left, and $0\cdot\hat k - 1\cdot\hat i = -\hat i$ from the key; the second option gives $+\hat i$.""")

# q19
T.single(3, ["vector-triple-product", "vector-product"],
    r"Let $\vec a = \hat i + 2\hat j$, $\vec b = \hat i + \hat k$ and $\vec c = \hat j + \hat k$. The vector $\vec r$ satisfying $\vec r\times\vec b = \vec a\times\vec b$ and $\vec r\cdot\vec c = 0$ is",
    [r"$-\hat i + 2\hat j - 2\hat k$", r"$3\hat i + 2\hat j + 2\hat k$", r"$-\hat i + 2\hat j + 2\hat k$", r"$\hat i + 2\hat j$"],
    r"""$(\vec r - \vec a)\times\vec b = \vec 0$, so $\vec r = \vec a + t\vec b$. Then
$$\vec r\cdot\vec c = \vec a\cdot\vec c + t\,\vec b\cdot\vec c = 2 + t = 0 \;\Rightarrow\; t = -2,$$
$$\vec r = (\hat i + 2\hat j) - 2(\hat i + \hat k) = -\hat i + 2\hat j - 2\hat k.$$

$3\hat i + 2\hat j + 2\hat k$ uses $t = +2$ (sign slip) and gives $\vec r\cdot\vec c = 4$. $\hat i + 2\hat j = \vec a$ satisfies the first equation only: $\vec a\cdot\vec c = 2 \ne 0$. $-\hat i + 2\hat j + 2\hat k$ fails the first equation, since it differs from $\vec a$ by $-2\hat i + 2\hat k$, which is not parallel to $\vec b$.""")

# q20
T.single(3, ["vectors-basics"],
    r"If $4\hat i + 3\hat j + 5\hat k = x(\hat i + \hat j) + y(\hat j + \hat k) + z(\hat k + \hat i)$, then $(x, y, z)$ is",
    [r"$(1, 2, 3)$", r"$(3, 2, 1)$", r"$(2, 1, 3)$", r"$(1, 3, 2)$"],
    r"""The three vectors are non-coplanar ($[\,\cdot\,] = 2$), so the expansion is unique. Compare components:
$$x + z = 4, \qquad x + y = 3, \qquad y + z = 5.$$
Adding, $x + y + z = 6$, so $x = 6 - 5 = 1$, $y = 6 - 4 = 2$, $z = 6 - 3 = 3$.

**Check:** $(1,1,0) + 2(0,1,1) + 3(1,0,1) = (4, 3, 5)$. The order $(3, 2, 1)$ pairs each coefficient with the wrong vector.""")

# q21
T.single(3, ["collinearity-coplanarity", "scalar-triple-product"],
    r"The four points $A(3, 2, 1)$, $B(4, \lambda, 5)$, $C(4, 2, -2)$ and $D(6, 5, -1)$ are coplanar. Then $\lambda$ equals",
    [r"$5$", r"$-5$", r"$3$", r"$7$"],
    r"""Coplanar points $\iff [\vec{AB}\ \vec{AC}\ \vec{AD}] = 0$, with $\vec{AB} = (1, \lambda - 2, 4)$, $\vec{AC} = (1, 0, -3)$, $\vec{AD} = (3, 3, -2)$:
$$\begin{vmatrix} 1 & \lambda - 2 & 4 \\ 1 & 0 & -3 \\ 3 & 3 & -2 \end{vmatrix} = 1(0 + 9) - (\lambda - 2)(-2 + 9) + 4(3 - 0) = 35 - 7\lambda.$$
So $\lambda = 5$.

$\lambda = -5$ solves $35 + 7\lambda = 0$, a sign slip in the middle term $-(\lambda - 2)\cdot 7$. Using the position vectors themselves instead of the differences $\vec{AB}, \vec{AC}, \vec{AD}$ tests the wrong thing (coplanarity with the origin).""")

# q22
T.single(3, ["scalar-product"],
    r"If $\vec a + \vec b + \vec c = \vec 0$ with $|\vec a| = 3$, $|\vec b| = 5$ and $|\vec c| = 7$, then the angle between $\vec a$ and $\vec b$ is",
    [r"$\frac{\pi}{3}$", r"$\frac{2\pi}{3}$", r"$\frac{\pi}{6}$", r"$\frac{\pi}{4}$"],
    r"""$\vec a + \vec b = -\vec c$, so
$$|\vec a|^2 + |\vec b|^2 + 2\,\vec a\cdot\vec b = |\vec c|^2 \;\Rightarrow\; 9 + 25 + 2\,\vec a\cdot\vec b = 49 \;\Rightarrow\; \vec a\cdot\vec b = \frac{15}{2}.$$
Then $\cos\theta = \dfrac{15/2}{3\cdot 5} = \dfrac12$, so $\theta = \dfrac{\pi}{3}$.

$\frac{2\pi}{3}$ is the **interior angle** of the triangle formed head to tail by $\vec a, \vec b, \vec c$ (by the cosine rule, opposite the side $7$). The angle between the vectors is its supplement.""")

# q23
T.single(3, ["scalar-triple-product"],
    r"$\vec a, \vec b, \vec c$ are unit vectors, and the angle between each pair is $\frac{\pi}{3}$. The volume of the parallelepiped with coterminous edges $\vec a, \vec b, \vec c$ is",
    [r"$\frac{1}{\sqrt2}$", r"$\frac{1}{2}$", r"$\frac{\sqrt3}{2}$", r"$\frac{1}{6\sqrt2}$"],
    r"""Use the Gram determinant, with every $\vec a\cdot\vec b = \cos\frac{\pi}{3} = \frac12$:
$$[\vec a\,\vec b\,\vec c]^2 = \begin{vmatrix} 1 & \frac12 & \frac12 \\ \frac12 & 1 & \frac12 \\ \frac12 & \frac12 & 1 \end{vmatrix} = 1\cdot\frac34 - \frac12\cdot\frac14 + \frac12\cdot\left(-\frac14\right) = \frac12.$$
So the volume is $\sqrt{1/2} = \frac{1}{\sqrt2}$.

$\frac12$ forgets that the Gram determinant gives the **square** of the volume. $\frac{1}{6\sqrt2}$ is the volume of the regular tetrahedron on these edges.""")

# q24
T.single(3, ["vector-triple-product"],
    r"For vectors $\vec a, \vec b, \vec c$, the equality $\vec a\times(\vec b\times\vec c) = (\vec a\times\vec b)\times\vec c$ holds if and only if",
    [r"$(\vec c\times\vec a)\times\vec b = \vec 0$", r"$\vec a$ is parallel to $\vec b$", r"$\vec a$ is perpendicular to $\vec c$", r"$\vec b$ is perpendicular to $\vec c$"],
    r"""Expand both sides:
$$\vec a\times(\vec b\times\vec c) = (\vec a\cdot\vec c)\vec b - (\vec a\cdot\vec b)\vec c, \qquad (\vec a\times\vec b)\times\vec c = (\vec a\cdot\vec c)\vec b - (\vec b\cdot\vec c)\vec a.$$
Their difference is $(\vec b\cdot\vec c)\vec a - (\vec a\cdot\vec b)\vec c = (\vec c\times\vec a)\times\vec b$. So the two are equal iff $(\vec c\times\vec a)\times\vec b = \vec 0$.

None of the other conditions is enough. Take $\vec a = \vec b = \hat i$, $\vec c = \hat j$: here $\vec a \parallel \vec b$, $\vec a \perp \vec c$ and $\vec b \perp \vec c$ all hold, yet $\hat i\times(\hat i\times\hat j) = -\hat j$ while $(\hat i\times\hat i)\times\hat j = \vec 0$.""")

# q25
T.assertion_reason(2, ["vector-triple-product", "vector-product"],
    r"For all vectors $\vec a, \vec b$: $|\vec a\times\vec b|^2 + (\vec a\cdot\vec b)^2 = |\vec a|^2|\vec b|^2$.",
    r"$\vec a\times\vec b$ is perpendicular to both $\vec a$ and $\vec b$.",
    1,
    r"""Both are true, but R does not explain A.

A is Lagrange's identity: with $\theta$ the angle between non-zero $\vec a, \vec b$,
$$|\vec a\times\vec b|^2 + (\vec a\cdot\vec b)^2 = |\vec a|^2|\vec b|^2(\sin^2\theta + \cos^2\theta) = |\vec a|^2|\vec b|^2,$$
and it is trivial if either vector is $\vec 0$. It rests on the **magnitudes** $|\vec a||\vec b|\sin\theta$ and $|\vec a||\vec b|\cos\theta$.

R is true (it fixes the **direction** of $\vec a\times\vec b$), but direction plays no role in A.""")

# q26
T.assertion_reason(2, ["vector-product"],
    r"If $\vec a \ne \vec 0$, $\vec a\cdot\vec b = \vec a\cdot\vec c$ and $\vec a\times\vec b = \vec a\times\vec c$, then $\vec b = \vec c$.",
    r"If $\vec a \ne \vec 0$ and $\vec a\cdot\vec b = \vec a\cdot\vec c$, then $\vec b = \vec c$.",
    2,
    r"""A is true, R is false.

**A:** put $\vec d = \vec b - \vec c$. Then $\vec a\cdot\vec d = 0$ and $\vec a\times\vec d = \vec 0$, so $\vec d$ is both perpendicular and parallel to the non-zero $\vec a$. By Lagrange, $|\vec a|^2|\vec d|^2 = 0$, so $\vec d = \vec 0$.

**R** fails: $\vec a = \hat i$, $\vec b = \hat j$, $\vec c = \hat k$ give $\vec a\cdot\vec b = \vec a\cdot\vec c = 0$ but $\vec b \ne \vec c$. The dot product only says $\vec a \perp (\vec b - \vec c)$.""")

# q27
T.assertion_reason(1, ["scalar-triple-product"],
    r"The vectors $\hat i + \hat j$, $\hat j + \hat k$ and $\hat k + \hat i$ are coplanar.",
    r"Three vectors are coplanar if and only if their scalar triple product is zero.",
    3,
    r"""A is false, R is true.

R is the coplanarity test. Applying it,
$$\begin{vmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 1 \end{vmatrix} = 1(1 - 0) - 1(0 - 1) + 0 = 2 \ne 0,$$
so the vectors are **not** coplanar; they even form a basis of $\R^3$.""")

# q28
T.statements(2, ["scalar-triple-product"],
    r"For vectors $\vec a, \vec b, \vec c$ and a real number $\lambda$, consider the following statements:",
    [r"$[\vec a\,\vec b\,\vec c] = [\vec b\,\vec c\,\vec a]$",
     r"$[\vec a\,\vec c\,\vec b] = -[\vec a\,\vec b\,\vec c]$",
     r"$[\lambda\vec a\ \ \lambda\vec b\ \ \lambda\vec c] = \lambda[\vec a\,\vec b\,\vec c]$"],
    [r"1 and 2 only", r"1, 2 and 3", r"2 and 3 only", r"1 only"],
    r"""The scalar triple product is a $3\times3$ determinant with rows $\vec a, \vec b, \vec c$.

1. A cyclic permutation is two row swaps, so the value is unchanged. True.
2. One row swap changes the sign. True.
3. False: $\lambda$ comes out of **each** of the three rows, so
$$[\lambda\vec a\ \ \lambda\vec b\ \ \lambda\vec c] = \lambda^3[\vec a\,\vec b\,\vec c].$$
With $\hat i, \hat j, \hat k$ and $\lambda = 2$: the left side is $8$, not $2$.""")

# q29
T.statements(3, ["vectors-basics", "scalar-product"],
    r"Consider the following statements about non-zero vectors in $\R^3$:",
    [r"$\vec a$ and $\vec b$ are collinear if and only if $\vec a\cdot\vec b = |\vec a|\,|\vec b|$.",
     r"Any four vectors in $\R^3$ are linearly dependent.",
     r"If $\vec a, \vec b, \vec c$ are coplanar, then $\vec c$ is a linear combination of $\vec a$ and $\vec b$."],
    [r"2 only", r"1 and 2 only", r"2 and 3 only", r"1, 2 and 3"],
    r"""2. True: $\R^3$ has dimension $3$, so any four vectors are dependent.

1. False: $\vec a\cdot\vec b = |\vec a||\vec b|$ means $\cos\theta = 1$, i.e. the **same** direction. Collinear vectors may be opposite: $\vec a = \hat i$, $\vec b = -\hat i$ are collinear with $\vec a\cdot\vec b = -1$. The correct test is $|\vec a\cdot\vec b| = |\vec a||\vec b|$, or $\vec a\times\vec b = \vec 0$.

3. False: $\hat i, 2\hat i, \hat j$ are coplanar, but $\hat j$ is not a combination of $\hat i$ and $2\hat i$. Coplanarity only says that **some** one of the three is a combination of the other two (here $2\hat i = 2\cdot\hat i + 0\cdot\hat j$).""")

# q30
T.match(2, ["scalar-product", "vector-product", "scalar-triple-product", "exam-tips"],
    r"For non-zero vectors $\vec a, \vec b, \vec c$, match each condition in List I with its geometric meaning in List II.",
    [r"$\vec a\cdot\vec b = 0$", r"$\vec a\times\vec b = \vec 0$", r"$[\vec a\,\vec b\,\vec c] = 0$", r"$\lvert\vec a\times\vec b\rvert = \vec a\cdot\vec b$"],
    [r"$\vec a, \vec b, \vec c$ are coplanar", r"the angle between $\vec a$ and $\vec b$ is $\frac{\pi}{4}$", r"$\vec a$ is parallel to $\vec b$", r"$\vec a$ is perpendicular to $\vec b$"],
    [r"A-4, B-3, C-1, D-2", r"A-3, B-4, C-1, D-2", r"A-4, B-3, C-2, D-1", r"A-4, B-1, C-3, D-2"],
    r"""- A: $|\vec a||\vec b|\cos\theta = 0$ gives $\theta = \frac{\pi}{2}$ (A-4).
- B: $|\vec a||\vec b|\sin\theta = 0$ gives $\theta = 0$ or $\pi$: parallel (B-3).
- C: zero scalar triple product means zero volume: coplanar (C-1).
- D: $|\vec a||\vec b|\sin\theta = |\vec a||\vec b|\cos\theta$, so $\tan\theta = 1$ and $\theta = \frac{\pi}{4}$ (D-2).

Swapping A and B is the classic slip: the **dot** product vanishes for perpendicular vectors, the **cross** product for parallel ones.""")


def check():
    import sympy as sp
    M = sp.Matrix
    i, j, k = M([1, 0, 0]), M([0, 1, 0]), M([0, 0, 1])
    def trip(a, b, c): return M.hstack(a, b, c).T.det()
    def cr(a, b): return a.cross(b)
    def zero(v, label):
        assert v == sp.zeros(*v.shape) or all(sp.simplify(e) == 0 for e in v), f"CHECK FAILED {label}: {v}"
    def nonzero(v, label):
        assert any(sp.simplify(e) != 0 for e in v), f"CHECK FAILED {label} (should be nonzero)"
    # generic vectors
    a = M(sp.symbols("a1:4")); b = M(sp.symbols("b1:4")); c = M(sp.symbols("c1:4")); d = M(sp.symbols("d1:4"))
    lam = sp.symbols("lam")

    # q1
    A, B = M([2, -1, 2]), M([1, 2, -2])
    eq(A.dot(B) / B.norm(), sp.Rational(-4, 3), "q1")
    eq(A.dot(B) / B.norm()**2, sp.Rational(-4, 9), "q1 distractor")
    # q2
    A, B = M([1, 2, 3]), M([3, -2, 1])
    assert cr(A, B) == M([8, 8, -8]), "q2 cross"
    eq(cr(A, B).norm(), 8 * sp.sqrt(3), "q2")
    eq(A.norm() * B.norm(), 14, "q2 distractor")
    # q3
    eq(abs(trip(M([1, 2, 3]), M([0, 1, 2]), M([2, 0, 1]))), 3, "q3")
    # q4
    P, Q, R = M([2, -1, 3]), M([3, -5, 1]), M([-1, lam, 9])
    sol = sp.solve(list(cr(Q - P, R - P)), lam, dict=True)
    assert sol == [{lam: 11}], f"q4 {sol}"
    # q5
    A = M([2, -3, 6])
    assert A / A.norm() == M([sp.Rational(2, 7), sp.Rational(-3, 7), sp.Rational(6, 7)]), "q5"
    # q6
    assert sp.solve(M([2, lam, 1]).dot(M([1, -2, 3])), lam) == [sp.Rational(5, 2)], "q6"
    # q7
    A, B = M([1, 1, 1]), M([1, -1, 0])
    n = cr(A, B) / cr(A, B).norm()
    assert n == M([1, 1, -2]) / sp.sqrt(6), "q7"
    for wrong in (M([1, 1, 2]), M([1, -1, 2]), M([2, -1, -1])):
        assert wrong.dot(A) != 0 or wrong.dot(B) != 0, "q7 distractor perpendicular"
    # q8
    assert sp.solve(trip(M([2, -1, 1]), M([1, 2, -3]), M([3, lam, 5])), lam) == [-4], "q8"
    eq(trip(M([2, -1, 1]), M([1, 2, -3]), M([3, lam, 5])), 7 * lam + 28, "q8 poly")
    # q9 (linear in a, b: treat as generic vectors)
    P, Q = 2 * a + b, a - 3 * b
    zero((1 * Q - 2 * P) / (1 - 2) - (3 * a + 5 * b), "q9")
    zero((1 * Q + 2 * P) / 3 - (5 * a - b) / 3, "q9 internal distractor")
    nonzero((2 * Q - 1 * P) / (2 - 1) - (3 * a + 5 * b), "q9 swapped distractor differs")
    zero((P - 2 * Q) / (1 - 2) - (-7 * b), "q9 swapped distractor value")
    # q10
    A, B, C = M([1, 1, 0]), M([0, 1, 1]), M([1, 0, 1])
    assert cr(A, cr(B, C)) == M([-1, 1, 0]), "q10"
    assert cr(cr(A, B), C) == M([-1, 0, 1]), "q10 other bracketing"
    # vector triple product identities (generic)
    zero(cr(a, cr(b, c)) - (a.dot(c) * b - a.dot(b) * c), "bac-cab")
    zero(cr(cr(a, b), c) - (a.dot(c) * b - b.dot(c) * a), "bac-cab 2")
    # q11
    eq(trip(cr(a, b), cr(b, c), cr(c, a)), trip(a, b, c)**2, "q11 R")
    cop = (M([1, 2, 0]), M([0, 1, 3]), M([1, 3, 3]))  # c = a + b, coplanar
    eq(trip(*cop), 0, "q11 setup")
    eq(trip(cr(cop[0], cop[1]), cr(cop[1], cop[2]), cr(cop[2], cop[0])), 0, "q11 A")
    # q12 Lagrange
    eq(cr(a, b).dot(cr(a, b)), a.dot(a) * b.dot(b) - a.dot(b)**2, "lagrange")
    eq(sp.sqrt(2**2 * 5**2 - 6**2), 8, "q12")
    A12, B12 = M([2, 0, 0]), M([3, 4, 0])  # |a|=2, |b|=5, a.b=6
    eq(cr(A12, B12).norm(), 8, "q12 concrete")
    # q13
    A13, B13 = M([3, 0, 0]), M([2, 2 * sp.sqrt(3), 0])
    eq(B13.norm(), 4, "q13 setup"); eq(A13.dot(B13) / 12, sp.Rational(1, 2), "q13 angle")
    eq((A13 + B13).norm(), sp.sqrt(37), "q13"); eq((A13 - B13).norm(), sp.sqrt(13), "q13 distractor")
    # q14
    zero(cr(b, a) + cr(a, b), "q14 s1")
    assert cr(i, cr(i, j)) == -j and cr(cr(i, i), j) == sp.zeros(3, 1), "q14 s2 counterexample"
    zero(cr(a, 3 * a), "q14 s3 parallel gives zero")
    # q15
    eq(trip(a + b, b + c, c + a), 2 * trip(a, b, c), "q15 identity")
    eq(2 * 3, 6, "q15")
    eq(trip(a - b, b - c, c - a), 0, "q15 distractor")
    # q16
    A, B = M([1, 2, 2]), M([3, 0, 4])
    eq(A.dot(B), 11, "q16 A"); eq(A.dot(B) / B.norm(), sp.Rational(11, 5), "q16 B")
    eq(cr(A, B).norm() / 2, sp.sqrt(26), "q16 C"); eq(A.dot(B) / (A.norm() * B.norm()), sp.Rational(11, 15), "q16 D")
    # q17
    eq(cr(a, b).dot(cr(c, d)), a.dot(c) * b.dot(d) - a.dot(d) * b.dot(c), "q17")
    for wrong in (a.dot(d) * b.dot(c) - a.dot(c) * b.dot(d), a.dot(b) * c.dot(d) - a.dot(d) * b.dot(c),
                  a.dot(c) * b.dot(d) + a.dot(d) * b.dot(c)):
        assert sp.expand(cr(a, b).dot(cr(c, d)) - wrong) != 0, "q17 distractor true"
    # q18
    lhs = cr(cr(a, b), cr(c, d))
    zero(lhs - (trip(a, b, d) * c - trip(a, b, c) * d), "q18")
    zero(lhs - (trip(a, c, d) * b - trip(b, c, d) * a), "q18 other form")
    for wrong in (trip(a, b, c) * d - trip(a, b, d) * c, trip(b, c, d) * a - trip(a, c, d) * b,
                  trip(a, b, d) * c + trip(a, b, c) * d):
        nonzero((lhs - wrong).applyfunc(sp.expand), "q18 distractor")
    assert cr(cr(i, j), cr(k, i)) == -i, "q18 check example"
    # q19
    A, B, C = M([1, 2, 0]), M([1, 0, 1]), M([0, 1, 1])
    r = M([-1, 2, -2])
    assert cr(r, B) == cr(A, B) and r.dot(C) == 0, "q19"
    for wrong in (M([3, 2, 2]), M([-1, 2, 2]), M([1, 2, 0])):
        assert cr(wrong, B) != cr(A, B) or wrong.dot(C) != 0, "q19 distractor works"
    # q20
    x, y, z = sp.symbols("x y z")
    s = sp.solve(list(x * M([1, 1, 0]) + y * M([0, 1, 1]) + z * M([1, 0, 1]) - M([4, 3, 5])), [x, y, z])
    assert s == {x: 1, y: 2, z: 3}, f"q20 {s}"
    # basis expansion identity (notes)
    zero(trip(a, b, c) * d - (trip(d, b, c) * a + trip(a, d, c) * b + trip(a, b, d) * c), "basis expansion")
    # q21
    Pa, Pb, Pc, Pd = M([3, 2, 1]), M([4, lam, 5]), M([4, 2, -2]), M([6, 5, -1])
    eq(trip(Pb - Pa, Pc - Pa, Pd - Pa), 35 - 7 * lam, "q21 poly")
    assert sp.solve(trip(Pb - Pa, Pc - Pa, Pd - Pa), lam) == [5], "q21"
    # q22
    A, B = M([3, 0, 0]), M([sp.Rational(5, 2), 5 * sp.sqrt(3) / 2, 0])
    Cv = -(A + B)
    eq(B.norm(), 5, "q22 b"); eq(Cv.norm(), 7, "q22 c")
    eq(sp.acos(A.dot(B) / (A.norm() * B.norm())), sp.pi / 3, "q22")
    # q23
    h = sp.Rational(1, 2)
    G = M([[1, h, h], [h, 1, h], [h, h, 1]])
    eq(sp.sqrt(G.det()), 1 / sp.sqrt(2), "q23")
    eq((M.hstack(a, b, c).T * M.hstack(a, b, c)).det(), trip(a, b, c)**2, "gram identity")
    # q24
    zero(cr(a, cr(b, c)) - cr(cr(a, b), c) - cr(cr(c, a), b), "q24 identity")
    assert cr(i, cr(i, j)) != cr(cr(i, i), j), "q24 counterexample to distractors"
    assert cr(i, j) != sp.zeros(3, 1) and i.dot(j) == 0, "q24 distractor conditions hold"
    # q25
    eq(cr(a, b).dot(cr(a, b)) + a.dot(b)**2, a.dot(a) * b.dot(b), "q25 A")
    eq(cr(a, b).dot(a), 0, "q25 R1"); eq(cr(a, b).dot(b), 0, "q25 R2")
    # q26: R counterexample; A via Lagrange with d = b - c
    assert i.dot(j) == i.dot(k) and j != k, "q26 R false"
    eq(cr(a, d).dot(cr(a, d)) + a.dot(d)**2, a.dot(a) * d.dot(d), "q26 A (Lagrange on d)")
    # q27
    eq(trip(i + j, j + k, k + i), 2, "q27")
    # q28
    eq(trip(a, b, c) - trip(b, c, a), 0, "q28 s1")
    eq(trip(a, c, b) + trip(a, b, c), 0, "q28 s2")
    eq(trip(lam * a, lam * b, lam * c), lam**3 * trip(a, b, c), "q28 s3 true form")
    eq(trip(2 * i, 2 * j, 2 * k), 8, "q28 s3 counterexample")
    # q29
    eq(i.dot(-i), -1, "q29 s1 counterexample"); assert cr(i, -i) == sp.zeros(3, 1)
    e = sp.symbols("e1:4"); e4 = M(e)
    assert M.hstack(i, j, k, e4).rank() <= 3 and M.hstack(a, b, c, d).shape[1] > 3, "q29 s2"
    eq(trip(i, 2 * i, j), 0, "q29 s3 coplanar")
    assert M.hstack(i, 2 * i).rank() < M.hstack(i, 2 * i, j).rank(), "q29 s3 j not in span"
    # q30
    assert i.dot(j) == 0 and cr(i, 2 * i) == sp.zeros(3, 1), "q30 A,B"
    eq(trip(i, j, i + j), 0, "q30 C")
    A, B = M([1, 0, 0]), M([1, 1, 0])
    eq(cr(A, B).norm(), A.dot(B), "q30 D setup")
    eq(sp.acos(A.dot(B) / (A.norm() * B.norm())), sp.pi / 4, "q30 D")


T.write(check)
