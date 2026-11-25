import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from qlib import Topic, eq

T = Topic("math.vectors.vector-applications", exams=["slst-1112"])

# 1
T.single(1, ["work-moment"],
    r"A force $\vec F = 2\hat i + 3\hat j - \hat k$ moves its point of application from $A(1, -1, 2)$ to $B(3, 2, 4)$. The work done is",
    [r"$11$", r"$8$", r"$-11$", r"$5$"],
    r"""The displacement is $\vec d = \vec{AB} = (3 - 1, 2 + 1, 4 - 2) = (2, 3, 2)$. Then
$$W = \vec F\cdot\vec d = 4 + 9 - 2 = 11.$$

$8$ is $\vec F\cdot\vec{OB}$: it uses the position vector of the end point instead of the displacement. $-11$ uses $\vec{BA}$; $5$ uses $\vec a + \vec b$.""")

# 2
T.single(1, ["work-moment"],
    r"A force $\vec F = 3\hat i + 2\hat j - 4\hat k$ acts at the point $P(1, -1, 2)$. Its moment about the origin is",
    [r"$10\hat j + 5\hat k$", r"$-10\hat j - 5\hat k$", r"$-10\hat j + 5\hat k$", r"$8\hat i + 10\hat j + 5\hat k$"],
    r"""The moment about $O$ is $\vec r\times\vec F$ with $\vec r = \vec{OP} = (1, -1, 2)$:
$$\vec r\times\vec F = \begin{vmatrix}\hat i&\hat j&\hat k\\1&-1&2\\3&2&-4\end{vmatrix} = (4 - 4)\hat i - (-4 - 6)\hat j + (2 + 3)\hat k = 10\hat j + 5\hat k.$$

$-10\hat j - 5\hat k$ is $\vec F\times\vec r$ (wrong order). $-10\hat j + 5\hat k$ drops the minus sign of the $\hat j$ cofactor. Check: the answer is perpendicular to $\vec F$, since $\vec F\cdot(0, 10, 5) = 20 - 20 = 0$.""")

# 3
T.single(2, ["work-moment"],
    r"A force $\vec F = 2\hat i + \hat j - \hat k$ acts at $A(1, 2, 3)$. Its moment about the point $B(2, -1, 1)$ is",
    [r"$-5\hat i + 3\hat j - 7\hat k$", r"$5\hat i - 3\hat j + 7\hat k$", r"$-5\hat i + 7\hat j - 3\hat k$", r"$-5\hat i - 3\hat j - 7\hat k$"],
    r"""Use the vector **from** the reference point **to** the point of application: $\vec{BA} = (1 - 2, 2 + 1, 3 - 1) = (-1, 3, 2)$.
$$\vec{BA}\times\vec F = \begin{vmatrix}\hat i&\hat j&\hat k\\-1&3&2\\2&1&-1\end{vmatrix} = (-3 - 2)\hat i - (1 - 4)\hat j + (-1 - 6)\hat k = -5\hat i + 3\hat j - 7\hat k.$$

$5\hat i - 3\hat j + 7\hat k$ uses $\vec{AB}$ (or $\vec F\times\vec{BA}$). $-5\hat i + 7\hat j - 3\hat k$ is $\vec{OA}\times\vec F$, the moment about the origin.""")

# 4
T.single(3, ["work-moment"],
    r"A force $\vec F = 2\hat i + \hat j + \hat k$ acts at $P(1, -1, 2)$. Its moment $(\vec{AP}\times\vec F)\cdot\hat\ell$ about the line through $A(0, 1, 1)$ in the direction of $2\hat i + \hat j - 2\hat k$ is",
    [r"$-5$", r"$5$", r"$-15$", r"$-3$"],
    r"""$\vec{AP} = (1, -2, 1)$ and
$$\vec{AP}\times\vec F = \begin{vmatrix}\hat i&\hat j&\hat k\\1&-2&1\\2&1&1\end{vmatrix} = (-3, 1, 5).$$
With $\hat\ell = \frac13(2, 1, -2)$:
$$M_L = \frac{-6 + 1 - 10}{3} = -5.$$

$-15$ forgets to divide by $|\vec\ell| = 3$. $-3$ uses $\vec{OP}$ instead of $\vec{AP}$: the line does not pass through $O$. $5$ reverses the order in the cross product.""")

# 5
T.single(1, ["lines"],
    r"The Cartesian form of the line $\vec r = (\hat i - 3\hat j + 2\hat k) + t(4\hat i + \hat j - 2\hat k)$ is",
    [r"$\dfrac{x - 1}{4} = \dfrac{y + 3}{1} = \dfrac{z - 2}{-2}$", r"$\dfrac{x - 4}{1} = \dfrac{y - 1}{-3} = \dfrac{z + 2}{2}$",
     r"$\dfrac{x + 1}{4} = \dfrac{y - 3}{1} = \dfrac{z + 2}{-2}$", r"$\dfrac{x - 1}{4} = \dfrac{y + 3}{1} = \dfrac{z - 2}{2}$"],
    r"""The line passes through $(1, -3, 2)$ with direction ratios $4 : 1 : -2$, so
$$\frac{x - 1}{4} = \frac{y + 3}{1} = \frac{z - 2}{-2}.$$

The second option swaps point and direction. The third has the point's signs reversed. The fourth drops the sign of the last direction ratio.""")

# 6
T.single(1, ["planes"],
    r"The perpendicular distance of the origin from the plane $\vec r\cdot(2\hat i - \hat j + 2\hat k) = 9$ is",
    [r"$3$", r"$9$", r"$1$", r"$\dfrac{9}{\sqrt5}$"],
    r"""Divide by $|\vec n| = \sqrt{4 + 1 + 4} = 3$ to reach the normal form $\vec r\cdot\hat n = 3$. So the distance is
$$\frac{|d|}{|\vec n|} = \frac93 = 3.$$

$9$ forgets to normalise. $1$ divides by $|\vec n|^2$. $\frac{9}{\sqrt5}$ leaves out one component of $\vec n$.""")

# 7
T.single(2, ["planes"],
    r"The vector equation of the plane through $A(1, 0, 2)$, $B(2, 1, 1)$ and $C(0, 2, 3)$ is",
    [r"$\vec r\cdot(\hat i + \hat k) = 3$", r"$\vec r\cdot(\hat i + \hat k) = -3$",
     r"$\vec r\cdot(\hat i - \hat k) = -1$", r"$\vec r\cdot(3\hat i + 3\hat k) = 3$"],
    r"""$\vec{AB} = (1, 1, -1)$ and $\vec{AC} = (-1, 2, 1)$, so a normal is
$$\vec{AB}\times\vec{AC} = \begin{vmatrix}\hat i&\hat j&\hat k\\1&1&-1\\-1&2&1\end{vmatrix} = (3, 0, 3) \parallel (1, 0, 1).$$
Then $d = \vec a\cdot(1, 0, 1) = 1 + 2 = 3$, giving $\vec r\cdot(\hat i + \hat k) = 3$, i.e. $x + z = 3$.

Check: $B$ gives $2 + 1 = 3$ and $C$ gives $0 + 3 = 3$. The option $\vec r\cdot(3\hat i + 3\hat k) = 3$ scales the normal but not $d$ (it should be $9$).""")

# 8
T.single(2, ["planes"],
    r"The distance of the point $(3, -1, 2)$ from the plane $\vec r\cdot(2\hat i + \hat j - 2\hat k) = 4$ is",
    [r"$1$", r"$\dfrac53$", r"$3$", r"$\dfrac13$"],
    r"""$$d = \frac{|\vec p\cdot\vec n - 4|}{|\vec n|} = \frac{|6 - 1 - 4 - 4|}{3} = \frac{3}{3} = 1.$$

$\frac53$ comes from $|\vec p\cdot\vec n + 4|$ (sign of $d$). $3$ forgets to divide by $|\vec n|$; $\frac13$ divides by $|\vec n|^2$.""")

# 9
T.single(2, ["planes"],
    r"The angle between the line $\vec r = (\hat i - \hat j) + t(\hat i + 2\hat j + 2\hat k)$ and the plane $\vec r\cdot(2\hat i - \hat j + 2\hat k) = 5$ is",
    [r"$\sin^{-1}\dfrac49$", r"$\cos^{-1}\dfrac49$", r"$\sin^{-1}\dfrac{4}{81}$", r"$\cos^{-1}\dfrac{4}{81}$"],
    r"""With $\vec b = (1, 2, 2)$ and $\vec n = (2, -1, 2)$: $\vec b\cdot\vec n = 2 - 2 + 4 = 4$ and $|\vec b| = |\vec n| = 3$. The line makes the angle $\varphi$ with the plane, where
$$\sin\varphi = \frac{|\vec b\cdot\vec n|}{|\vec b|\,|\vec n|} = \frac49.$$

$\cos^{-1}\frac49$ is the angle between the line and the **normal**, the complement of $\varphi$. The $\frac{4}{81}$ options divide by the squares of the lengths.""")

# 10
T.single(2, ["planes"],
    r"The line $\vec r = (\hat i + \hat j) + t(2\hat i + \lambda\hat j + \hat k)$ is parallel to the plane $\vec r\cdot(3\hat i - 2\hat j + 4\hat k) = 7$ when $\lambda$ equals",
    [r"$5$", r"$-5$", r"$1$", r"$-1$"],
    r"""The line is parallel to the plane iff its direction is perpendicular to the normal:
$$(2, \lambda, 1)\cdot(3, -2, 4) = 6 - 2\lambda + 4 = 0 \Rightarrow \lambda = 5.$$

For $\lambda = 5$ the point $(1, 1, 0)$ gives $\vec a\cdot\vec n = 3 - 2 = 1 \ne 7$, so the line is parallel to the plane but does not lie in it. $-5$ comes from a sign slip in $-2\lambda$.""")

# 11
T.single(2, ["shortest-distance"],
    r"The shortest distance between the lines $\vec r = (\hat i + 2\hat j + 3\hat k) + t(\hat i - 3\hat j + 2\hat k)$ and $\vec r = (4\hat i + 5\hat j + 6\hat k) + s(2\hat i + 3\hat j + \hat k)$ is",
    [r"$\dfrac{3}{\sqrt{19}}$", r"$\dfrac{9}{\sqrt{19}}$", r"$\dfrac{1}{\sqrt{19}}$", r"$\dfrac{3}{19}$"],
    r"""$$\vec b_1\times\vec b_2 = \begin{vmatrix}\hat i&\hat j&\hat k\\1&-3&2\\2&3&1\end{vmatrix} = (-9, 3, 9), \qquad |\vec b_1\times\vec b_2| = \sqrt{171} = 3\sqrt{19}.$$
With $\vec a_2 - \vec a_1 = (3, 3, 3)$: $(3, 3, 3)\cdot(-9, 3, 9) = 9$. So
$$d = \frac{9}{3\sqrt{19}} = \frac{3}{\sqrt{19}}.$$

$\frac{9}{\sqrt{19}}$ uses $\sqrt{19}$ for $|\vec b_1\times\vec b_2|$, dropping the factor $3 = \sqrt9$.""")

# 12
T.single(3, ["shortest-distance"],
    r"The distance between the parallel lines $\vec r = (\hat i + \hat j) + t(\hat i + 2\hat j + 2\hat k)$ and $\vec r = (2\hat i + \hat j - \hat k) + s(\hat i + 2\hat j + 2\hat k)$ is",
    [r"$\dfrac{\sqrt{17}}{3}$", r"$\dfrac13$", r"$\sqrt{17}$", r"$\sqrt2$"],
    r"""The skew-line formula gives $\frac00$, so use $d = \dfrac{|(\vec a_2 - \vec a_1)\times\vec b|}{|\vec b|}$ with $\vec a_2 - \vec a_1 = (1, 0, -1)$ and $|\vec b| = 3$:
$$(1, 0, -1)\times(1, 2, 2) = (2, -3, 2), \qquad d = \frac{\sqrt{4 + 9 + 4}}{3} = \frac{\sqrt{17}}{3}.$$

$\frac13 = \frac{|(\vec a_2 - \vec a_1)\cdot\vec b|}{|\vec b|}$ is the projection **along** the lines, not across them. $\sqrt2 = |\vec a_2 - \vec a_1|$ is the distance between the two given points.""")

# 13
T.single(3, ["shortest-distance", "lines"],
    r"The lines $\vec r = (\hat i + 2\hat j + 3\hat k) + t(2\hat i + 3\hat j + 4\hat k)$ and $\vec r = (2\hat i + 4\hat j + 5\hat k) + s(\hat i + 2\hat j + k\hat k)$ intersect when $k$ equals",
    [r"$2$", r"$-2$", r"$4$", r"$\dfrac12$"],
    r"""The directions $(2, 3, 4)$ and $(1, 2, k)$ are never parallel ($2 : 3 \ne 1 : 2$), so the lines meet iff they are coplanar:
$$\begin{vmatrix} 1 & 2 & 2 \\ 2 & 3 & 4 \\ 1 & 2 & k \end{vmatrix} = 1(3k - 8) - 2(2k - 4) + 2(4 - 3) = 2 - k = 0 \Rightarrow k = 2.$$

Check: $t = 0$, $s = -1$ give the common point $(1, 2, 3)$ on both lines. $-2$ comes from a sign slip in the expansion.""")

# 14
T.single(2, ["tetrahedron"],
    r"The volume of the tetrahedron with vertices $A(1, 1, 1)$, $B(3, 2, 1)$, $C(2, 4, 2)$, $D(1, 2, 5)$ is",
    [r"$3$", r"$6$", r"$9$", r"$\dfrac{16}{3}$"],
    r"""The edges from $A$ are $\vec{AB} = (2, 1, 0)$, $\vec{AC} = (1, 3, 1)$, $\vec{AD} = (0, 1, 4)$:
$$[\vec{AB}\ \vec{AC}\ \vec{AD}] = \begin{vmatrix} 2 & 1 & 0 \\ 1 & 3 & 1 \\ 0 & 1 & 4 \end{vmatrix} = 2(12 - 1) - 1(4 - 0) = 18, \qquad V = \frac{18}{6} = 3.$$

$6$ and $9$ divide by $3$ and $2$. $\frac{16}{3}$ uses the position vectors of $B, C, D$, which gives the tetrahedron $OBCD$.""")

# 15
T.single(3, ["tetrahedron"],
    r"A tetrahedron has coterminous edges $\hat i + 2\hat j$, $\hat j + \lambda\hat k$ and $2\hat i + \hat k$, and volume $\dfrac32$. Then $\lambda$ is",
    [r"$2$ or $-\dfrac52$", r"$2$ only", r"$-2$ or $\dfrac52$", r"$\dfrac78$ or $-\dfrac{11}{8}$"],
    r"""$$[\vec a\,\vec b\,\vec c] = \begin{vmatrix} 1 & 2 & 0 \\ 0 & 1 & \lambda \\ 2 & 0 & 1 \end{vmatrix} = 1(1 - 0) - 2(0 - 2\lambda) + 0 = 1 + 4\lambda.$$
So $\frac16|1 + 4\lambda| = \frac32$, i.e. $1 + 4\lambda = \pm 9$, giving $\lambda = 2$ or $\lambda = -\frac52$.

"$2$ only" ignores the modulus. $-2$ or $\frac52$ comes from a sign slip in the middle cofactor ($1 - 4\lambda$). $\frac78$ or $-\frac{11}{8}$ uses $\frac13$ in place of $\frac16$.""")

# 16
T.single(1, ["velocity-acceleration"],
    r"A particle moves so that $\vec r = (t^2 + 1)\hat i + (4t - 3)\hat j + (2t^2 - 6t)\hat k$. Its speed at $t = 1$ is",
    [r"$2\sqrt6$", r"$2\sqrt5$", r"$\sqrt{21}$", r"$\sqrt6$"],
    r"""$\vec v = 2t\,\hat i + 4\hat j + (4t - 6)\hat k$, so $\vec v(1) = (2, 4, -2)$ and
$$|\vec v(1)| = \sqrt{4 + 16 + 4} = 2\sqrt6.$$

$2\sqrt5$ is $|\vec a| = |(2, 0, 4)|$. $\sqrt{21}$ is $|\vec r(1)| = |(2, 1, -4)|$, the distance from the origin.""")

# 17
T.single(2, ["vector-differentiation"],
    r"For $\vec r(t) = a\cos t\,\hat i + a\sin t\,\hat j + bt\,\hat k$ ($a, b$ constants), $\vec r\cdot\dfrac{d\vec r}{dt}$ equals",
    [r"$b^2 t$", r"$0$", r"$bt$", r"$a^2 + b^2 t$"],
    r"""$\dfrac{d\vec r}{dt} = -a\sin t\,\hat i + a\cos t\,\hat j + b\hat k$, so
$$\vec r\cdot\vec r\,' = -a^2\sin t\cos t + a^2\sin t\cos t + b^2 t = b^2 t.$$

$0$ would hold only if $|\vec r|$ were constant; here $|\vec r|^2 = a^2 + b^2t^2$, and indeed $\vec r\cdot\vec r\,' = \frac12\frac{d}{dt}|\vec r|^2 = b^2 t$.""")

# 18
T.single(2, ["vector-differentiation"],
    r"If $\vec r$ is a twice-differentiable vector function of $t$, then $\dfrac{d}{dt}\left(\vec r\times\dfrac{d\vec r}{dt}\right)$ equals",
    [r"$\vec r\times\dfrac{d^2\vec r}{dt^2}$", r"$\dfrac{d\vec r}{dt}\times\dfrac{d^2\vec r}{dt^2}$",
     r"$\dfrac{d^2\vec r}{dt^2}\times\vec r$", r"$\vec 0$"],
    r"""By the product rule, keeping the order:
$$\frac{d}{dt}(\vec r\times\vec r\,') = \vec r\,'\times\vec r\,' + \vec r\times\vec r\,'' = \vec r\times\vec r\,'',$$
since $\vec r\,'\times\vec r\,' = \vec 0$.

$\vec r\,''\times\vec r$ has the opposite sign. $\vec 0$ is wrong in general: for $\vec r = (t, t^2, t^3)$, $\vec r\times\vec r\,'' = (4t^3, -6t^2, 2t) \ne \vec 0$.""")

# 19
T.single(3, ["vector-differentiation"],
    r"If $\vec r$ is a thrice-differentiable vector function of $t$ and dashes denote $\frac{d}{dt}$, then $\dfrac{d}{dt}[\vec r\ \ \vec r\,'\ \ \vec r\,'']$ equals",
    [r"$[\vec r\ \ \vec r\,'\ \ \vec r\,''']$", r"$[\vec r\,'\ \ \vec r\,''\ \ \vec r\,''']$",
     r"$[\vec r\ \ \vec r\,''\ \ \vec r\,''']$", r"$0$"],
    r"""Differentiate each slot in turn:
$$\frac{d}{dt}[\vec r\,\vec r\,'\,\vec r\,''] = [\vec r\,'\,\vec r\,'\,\vec r\,''] + [\vec r\,\vec r\,''\,\vec r\,''] + [\vec r\,\vec r\,'\,\vec r\,'''].$$
The first two have a repeated vector and vanish, leaving $[\vec r\ \vec r\,'\ \vec r\,''']$.

$[\vec r\,'\,\vec r\,''\,\vec r\,''']$ differentiates every slot at once, which is not the product rule. Check with $\vec r = (t, t^2, t^4)$: the bracket is $\begin{vmatrix} t & t^2 & t^4\\ 1 & 2t & 4t^3\\ 0 & 2 & 12t^2\end{vmatrix} = 6t^4$, whose derivative $24t^3$ equals $[\vec r\,\vec r\,'\,\vec r\,''']$.""")

# 20
T.single(2, ["velocity-acceleration"],
    r"A particle has position $\vec r = t^2\hat i + 3\cos 2t\,\hat j + 3\sin 2t\,\hat k$. The magnitude of its acceleration at $t = 0$ is",
    [r"$2\sqrt{37}$", r"$\sqrt{40}$", r"$6$", r"$12$"],
    r"""$\vec v = 2t\,\hat i - 6\sin 2t\,\hat j + 6\cos 2t\,\hat k$ and
$$\vec a = 2\hat i - 12\cos 2t\,\hat j - 12\sin 2t\,\hat k.$$
At $t = 0$, $\vec a = (2, -12, 0)$, so $|\vec a| = \sqrt{4 + 144} = \sqrt{148} = 2\sqrt{37}$.

$\sqrt{40}$ applies the chain-rule factor $2$ only once ($-6\cos 2t$ in place of $-12\cos 2t$). $6$ is the speed at $t = 0$; $12$ ignores the $\hat i$ component.""")

# 21
T.single(3, ["velocity-acceleration"],
    r"For $\vec r = \cos t\,\hat i + \sin t\,\hat j + \dfrac{t^2}{2}\hat k$, the tangential component of acceleration at $t = 1$ is",
    [r"$\dfrac{1}{\sqrt2}$", r"$\sqrt{\dfrac32}$", r"$1$", r"$\sqrt2$"],
    r"""$\vec v = (-\sin t, \cos t, t)$ and $\vec a = (-\cos t, -\sin t, 1)$, so $\vec v\cdot\vec a = t$ and $|\vec v| = \sqrt{1 + t^2}$. At $t = 1$:
$$a_T = \frac{\vec v\cdot\vec a}{|\vec v|} = \frac{1}{\sqrt2}.$$
Check: $a_T = \frac{d}{dt}\sqrt{1 + t^2} = \frac{t}{\sqrt{1 + t^2}}$.

$\sqrt{3/2}$ is the **normal** component: $|\vec a|^2 = 2$, so $a_N = \sqrt{2 - \frac12}$. $\sqrt2$ is $|\vec a|$ itself; $1$ is $\vec v\cdot\vec a$ without dividing by the speed.""")

# 22 statements
T.statements(2, ["planes", "lines"],
    r"Consider the following statements about lines and planes in space:",
    [r"In $\vec r\cdot\hat n = p$ with $\hat n$ a unit vector and $p \ge 0$, $p$ is the perpendicular distance of the origin from the plane.",
     r"The line $\vec r = \vec a + t\vec b$ is parallel to the plane $\vec r\cdot\vec n = d$ if and only if $\vec b\times\vec n = \vec 0$.",
     r"The lines $\vec r = \vec a_1 + t\vec b_1$ and $\vec r = \vec a_2 + s\vec b_2$ intersect if and only if $[\vec a_2 - \vec a_1\ \ \vec b_1\ \ \vec b_2] = 0$."],
    [r"1 only", r"1 and 3 only", r"1 and 2 only", r"1, 2 and 3"],
    r"""1. True: the foot of the perpendicular from $O$ is $p\hat n$, at distance $p$.
2. False: parallel to the plane means $\vec b\perp\vec n$, i.e. $\vec b\cdot\vec n = 0$. The condition $\vec b\times\vec n = \vec 0$ means the line is **perpendicular** to the plane. Example: $\vec b = \hat i$, $\vec n = \hat k$.
3. False: the triple product vanishes for coplanar lines, which include distinct **parallel** lines. Example: the $x$-axis and the line $\vec r = \hat j + s\hat i$ give $[\hat j\ \hat i\ \hat i] = 0$ but never meet. Intersection needs also $\vec b_1\times\vec b_2 \ne \vec 0$.""")

# 23 statements
T.statements(3, ["vector-differentiation"],
    r"Let $\vec r(t)$ be a differentiable vector function. Consider the following statements:",
    [r"If $|\vec r(t)|$ is constant, then $\vec r\cdot\dfrac{d\vec r}{dt} = 0$ for all $t$.",
     r"If $\vec r(t) \ne \vec 0$ has constant direction, then $\vec r\times\dfrac{d\vec r}{dt} = \vec 0$ for all $t$.",
     r"$\left|\dfrac{d\vec r}{dt}\right| = \dfrac{d}{dt}|\vec r|$ wherever $\vec r \ne \vec 0$."],
    [r"1 and 2 only", r"1 only", r"2 and 3 only", r"1, 2 and 3"],
    r"""1. True: $\vec r\cdot\vec r = c$ gives $2\vec r\cdot\vec r\,' = 0$.
2. True: write $\vec r = f(t)\,\hat u$ with $\hat u$ constant; then $\vec r\,' = f'(t)\hat u$ is parallel to $\vec r$, so $\vec r\times\vec r\,' = \vec 0$.
3. False: for $\vec r = \cos t\,\hat i + \sin t\,\hat j$, $|\vec r\,'| = 1$ but $\frac{d}{dt}|\vec r| = 0$. The correct relation is $\frac{d}{dt}|\vec r| = \frac{\vec r\cdot\vec r\,'}{|\vec r|}$.""")

# 24 match
T.match(1, ["work-moment", "tetrahedron"],
    r"Match each quantity in List I with its vector expression in List II ($\vec F$ acts at $P$; $A, B, C, D$ are points; $\hat\ell$ is a unit vector along a line through $A$).",
    [r"Work done when the point of application moves from $A$ to $B$", r"Moment of $\vec F$ about the point $A$",
     r"Moment of $\vec F$ about the line through $A$ along $\hat\ell$", r"Volume of the tetrahedron $ABCD$"],
    [r"$\frac16\lvert[\vec{AB}\ \vec{AC}\ \vec{AD}]\rvert$", r"$\vec{AP}\times\vec F$",
     r"$\vec F\cdot\vec{AB}$", r"$(\vec{AP}\times\vec F)\cdot\hat\ell$"],
    [r"A-3, B-2, C-4, D-1", r"A-2, B-3, C-4, D-1", r"A-3, B-4, C-2, D-1", r"A-3, B-2, C-1, D-4"],
    r"""- Work is a scalar: $\vec F\cdot\vec{AB}$ (3).
- Moment about a point is a vector: $\vec{AP}\times\vec F$ (2).
- Moment about a line is the resolved part of that vector along the line: $(\vec{AP}\times\vec F)\cdot\hat\ell$ (4).
- Tetrahedron: $\frac16$ of the box product of three edges from one vertex (1).

So A-3, B-2, C-4, D-1. Mixing up the two moments (B and C) is the usual slip: only one of them is a scalar.""")

# 25 match
T.match(2, ["vector-differentiation", "velocity-acceleration"],
    r"For $\vec r(t) = 2t\,\hat i + t^2\hat j + \dfrac{t^3}{3}\hat k$, match each quantity at $t = 2$ in List I with its value in List II.",
    [r"$\lvert\vec r\,'\rvert$", r"$\lvert\vec r\,''\rvert$", r"$\vec r\,'\cdot\vec r\,''$", r"$\lvert\vec r\,'\times\vec r\,''\rvert$"],
    [r"$12$", r"$24$", r"$6$", r"$2\sqrt5$"],
    [r"A-3, B-4, C-2, D-1", r"A-3, B-4, C-1, D-2", r"A-4, B-3, C-2, D-1", r"A-3, B-2, C-4, D-1"],
    r"""$\vec r\,' = (2, 2t, t^2) = (2, 4, 4)$ and $\vec r\,'' = (0, 2, 2t) = (0, 2, 4)$ at $t = 2$.
- $|\vec r\,'| = \sqrt{4 + 16 + 16} = 6$ (3).
- $|\vec r\,''| = \sqrt{0 + 4 + 16} = 2\sqrt5$ (4).
- $\vec r\,'\cdot\vec r\,'' = 0 + 8 + 16 = 24$ (2).
- $\vec r\,'\times\vec r\,'' = (16 - 8, 0 - 8, 4 - 0) = (8, -8, 4)$, of length $12$ (1).

So A-3, B-4, C-2, D-1. Check with Lagrange: $|\vec r\,'\times\vec r\,''|^2 = 36\cdot 20 - 24^2 = 144$.""")

# 26 AR: 0
T.assertion_reason(1, ["work-moment"],
    r"The moment of the force $\vec F = 2\hat i - \hat j + \hat k$ acting at $P(1, 1, 1)$ about the point $Q(3, 0, 2)$ is $\vec 0$.",
    r"The moment of a non-zero force about a point is $\vec 0$ if and only if the point lies on the line of action of the force.",
    0,
    r"""$\vec{QP} = (-2, 1, -1) = -\vec F$, so $Q$ lies on the line of action $\vec r = \vec p + t\vec F$ (at $t = 1$), and $\vec{QP}\times\vec F = -\vec F\times\vec F = \vec 0$.

The reason is true ($\vec{QP}\times\vec F = \vec 0 \iff \vec{QP}\parallel\vec F$) and it is exactly why the assertion holds.""")

# 27 AR: 1
T.assertion_reason(2, ["work-moment"],
    r"The work done by the force $\vec F = 2\hat i - \hat j + \hat k$ in moving its point of application from $(1, 2, 3)$ to $(3, 4, 5)$ is $4$.",
    r"The work done by the resultant of several forces acting on a particle equals the sum of the works done by the separate forces.",
    1,
    r"""Assertion: true. $\vec d = (2, 2, 2)$ and $\vec F\cdot\vec d = 4 - 2 + 2 = 4$.

Reason: true, because the dot product distributes over addition: $\left(\sum\vec F_i\right)\cdot\vec d = \sum\vec F_i\cdot\vec d$. But only one force acts here, so the reason does not explain the assertion; the explanation is $W = \vec F\cdot\vec d$.""")

# 28 AR: 2
T.assertion_reason(1, ["tetrahedron"],
    r"The volume of the tetrahedron with coterminous edges $\vec a, \vec b, \vec c$ is $\dfrac16\lvert[\vec a\,\vec b\,\vec c]\rvert$.",
    r"A tetrahedron has one-third the volume of the parallelepiped with the same three coterminous edges.",
    2,
    r"""Assertion: true. Volume $= \frac13\times$ base area $\times$ height $= \frac13\cdot\frac12|\vec b\times\vec c|\cdot\frac{\lvert[\vec a\,\vec b\,\vec c]\rvert}{|\vec b\times\vec c|} = \frac16\lvert[\vec a\,\vec b\,\vec c]\rvert$.

Reason: false. The parallelepiped has volume $\lvert[\vec a\,\vec b\,\vec c]\rvert$, so the tetrahedron is **one-sixth** of it. One-third is the ratio to the prism on the same triangular base, whose base area is half that of the parallelepiped.""")

# 29 AR: 3
T.assertion_reason(2, ["lines", "shortest-distance"],
    r"The lines $\vec r = t(\hat i + \hat j + \hat k)$ and $\vec r = \hat i + s(2\hat i + 2\hat j + 2\hat k)$ are skew.",
    r"Two lines are skew if and only if they are neither parallel nor intersecting.",
    3,
    r"""Assertion: false. The direction vectors are proportional, $(2, 2, 2) = 2(1, 1, 1)$, so the lines are **parallel**. They are distinct ($\hat i$ is not a multiple of $\hat i + \hat j + \hat k$), with distance $\frac{|\hat i\times(1, 1, 1)|}{\sqrt3} = \frac{\sqrt2}{\sqrt3}$.

Reason: true; this is the definition of skew lines. Equivalently, $[\vec a_2 - \vec a_1\ \vec b_1\ \vec b_2] \ne 0$, which fails here.""")

# 30 AR: 0
T.assertion_reason(3, ["vector-differentiation"],
    r"If $\vec a, \vec b$ are constant, perpendicular unit vectors and $\vec r(t) = \cos t\,\vec a + \sin t\,\vec b$, then $\dfrac{d\vec r}{dt}$ is perpendicular to $\vec r$ for every $t$.",
    r"If a differentiable vector function has constant magnitude, then it is perpendicular to its derivative wherever the derivative is non-zero.",
    0,
    r"""Assertion: true. $|\vec r|^2 = \cos^2 t + \sin^2 t + 2\sin t\cos t\,(\vec a\cdot\vec b) = 1$, a constant. Directly, $\vec r\,' = -\sin t\,\vec a + \cos t\,\vec b$ and $\vec r\cdot\vec r\,' = -\sin t\cos t + \sin t\cos t = 0$.

Reason: true, since $\frac{d}{dt}(\vec r\cdot\vec r) = 2\vec r\cdot\vec r\,' = 0$. The assertion follows from it once $|\vec r| = 1$ is noted, so the reason explains the assertion.""")


def check():
    import sympy as sp
    M = sp.Matrix
    t, s, k, lam, a, b = sp.symbols("t s k lambda a b", real=True)
    V = lambda *x: M(x)
    box = lambda u, v, w: M.hstack(u, v, w).det()
    # q1
    F = V(2, 3, -1); A, B = V(1, -1, 2), V(3, 2, 4)
    eq(F.dot(B - A), 11, "q1"); eq(F.dot(B), 8, "q1 d"); eq(F.dot(A + B), 5, "q1 d2")
    # q2
    r = V(1, -1, 2); F = V(3, 2, -4)
    assert r.cross(F) == V(0, 10, 5), "q2"
    # q3
    F = V(2, 1, -1); A, B = V(1, 2, 3), V(2, -1, 1)
    assert (A - B).cross(F) == V(-5, 3, -7), "q3"
    assert A.cross(F) == V(-5, 7, -3), "q3 d"
    # q4
    F = V(2, 1, 1); P, A, l = V(1, -1, 2), V(0, 1, 1), V(2, 1, -2)
    eq((P - A).cross(F).dot(l) / l.norm(), -5, "q4")
    eq(P.cross(F).dot(l) / l.norm(), -3, "q4 d")
    # q5: point (1,-3,2) on the line, direction (4,1,-2)
    pt = V(1, -3, 2) + t * V(4, 1, -2)
    eq((pt[0] - 1) / 4 - (pt[1] + 3) / 1, 0, "q5a"); eq((pt[1] + 3) / 1 - (pt[2] - 2) / -2, 0, "q5b")
    # q6
    n = V(2, -1, 2); eq(9 / n.norm(), 3, "q6")
    # q7
    A, B, C = V(1, 0, 2), V(2, 1, 1), V(0, 2, 3)
    nn = (B - A).cross(C - A); assert nn == V(3, 0, 3), "q7 normal"
    for X in (A, B, C):
        eq(X.dot(V(1, 0, 1)), 3, "q7")
        assert X.dot(V(3, 0, 3)) != 3
    assert any(X.dot(V(1, 0, -1)) != -1 for X in (A, B, C)), "q7 d"
    # q8
    eq(abs(V(3, -1, 2).dot(V(2, 1, -2)) - 4) / 3, 1, "q8")
    # q9
    bb, n = V(1, 2, 2), V(2, -1, 2)
    eq(abs(bb.dot(n)) / (bb.norm() * n.norm()), sp.Rational(4, 9), "q9")
    # q10
    sol = sp.solve(V(2, lam, 1).dot(V(3, -2, 4)), lam); assert sol == [5], "q10"
    eq(V(1, 1, 0).dot(V(3, -2, 4)), 1, "q10 not in plane")
    # q11
    b1, b2 = V(1, -3, 2), V(2, 3, 1); dA = V(4, 5, 6) - V(1, 2, 3)
    eq(abs(dA.dot(b1.cross(b2))) / b1.cross(b2).norm(), 3 / sp.sqrt(19), "q11")
    # q12
    bb = V(1, 2, 2); dA = V(2, 1, -1) - V(1, 1, 0)
    eq(dA.cross(bb).norm() / bb.norm(), sp.sqrt(17) / 3, "q12")
    eq(abs(dA.dot(bb)) / bb.norm(), sp.Rational(1, 3), "q12 d"); eq(dA.norm(), sp.sqrt(2), "q12 d2")
    # q13
    a1, b1, a2 = V(1, 2, 3), V(2, 3, 4), V(2, 4, 5)
    b2 = V(1, 2, k)
    assert sp.solve(box(a2 - a1, b1, b2), k) == [2], "q13"
    b2 = b2.subs(k, 2); assert b1.cross(b2) != sp.zeros(3, 1)
    ss = sp.solve(list(a1 + t * b1 - a2 - s * b2), [t, s], dict=True); assert ss, "q13 meet"
    assert ss[0] == {t: 0, s: -1} and (a1 + t * b1).subs(ss[0]) == V(1, 2, 3)
    # q14
    A, B, C, D = V(1, 1, 1), V(3, 2, 1), V(2, 4, 2), V(1, 2, 5)
    eq(abs(box(B - A, C - A, D - A)) / 6, 3, "q14"); eq(abs(box(B, C, D)) / 6, sp.Rational(16, 3), "q14 d")
    # q15
    vol = box(V(1, 2, 0), V(0, 1, lam), V(2, 0, 1))
    eq(vol, 1 + 4 * lam, "q15 det")
    assert set(sp.solve(sp.Eq(sp.Abs(vol) / 6, sp.Rational(3, 2)), lam)) == {2, sp.Rational(-5, 2)}, "q15"
    assert set(sp.solve(sp.Eq(sp.Abs(vol) / 3, sp.Rational(3, 2)), lam)) == {sp.Rational(7, 8), sp.Rational(-11, 8)}, "q15 d"
    # q16
    r = V(t**2 + 1, 4 * t - 3, 2 * t**2 - 6 * t)
    eq(r.diff(t).subs(t, 1).norm(), 2 * sp.sqrt(6), "q16"); eq(r.diff(t, 2).norm(), 2 * sp.sqrt(5), "q16 d")
    eq(r.subs(t, 1).norm(), sp.sqrt(21), "q16 d2")
    # q17
    r = V(a * sp.cos(t), a * sp.sin(t), b * t)
    eq(r.dot(r.diff(t)), b**2 * t, "q17")
    # q18, q19: generic functions
    f = [sp.Function(c)(t) for c in "fgh"]
    r = M(f); r1, r2, r3 = r.diff(t), r.diff(t, 2), r.diff(t, 3)
    assert sp.simplify(r.cross(r1).diff(t) - r.cross(r2)) == sp.zeros(3, 1), "q18"
    rr = V(t, t**2, t**3); assert sp.expand(rr.cross(rr.diff(t, 2))) == V(4 * t**3, -6 * t**2, 2 * t), "q18 d"
    eq(box(r, r1, r2).diff(t), box(r, r1, r3), "q19")
    rr = V(t, t**2, t**4)
    eq(box(rr, rr.diff(t), rr.diff(t, 2)), 6 * t**4, "q19 ex")
    eq(box(rr, rr.diff(t), rr.diff(t, 3)), 24 * t**3, "q19 ex2")
    assert sp.simplify(box(rr.diff(t), rr.diff(t, 2), rr.diff(t, 3)) - 24 * t**3) != 0, "q19 d"
    # q20
    r = V(t**2, 3 * sp.cos(2 * t), 3 * sp.sin(2 * t))
    eq(r.diff(t, 2).subs(t, 0).norm(), 2 * sp.sqrt(37), "q20"); eq(r.diff(t).subs(t, 0).norm(), 6, "q20 d")
    # q21
    r = V(sp.cos(t), sp.sin(t), t**2 / 2); v, acc = r.diff(t), r.diff(t, 2)
    aT = (v.dot(acc) / v.norm()).subs(t, 1); aN = (v.cross(acc).norm() / v.norm()).subs(t, 1)
    eq(aT, 1 / sp.sqrt(2), "q21"); eq(aN, sp.sqrt(sp.Rational(3, 2)), "q21 aN")
    eq(acc.norm().subs(t, 1)**2, aT**2 + aN**2, "q21 sum")
    # q22: 2 false, 3 false
    bb, n = V(1, 0, 0), V(0, 0, 1); assert bb.dot(n) == 0 and bb.cross(n) != sp.zeros(3, 1), "q22 s2"
    assert box(V(0, 1, 0), V(1, 0, 0), V(1, 0, 0)) == 0
    assert sp.solve(list(t * V(1, 0, 0) - V(0, 1, 0) - s * V(1, 0, 0)), [t, s]) == [], "q22 s3"
    # q23: 1, 2 true; 3 false
    r = V(sp.cos(t), sp.sin(t), 0)
    eq(r.dot(r.diff(t)), 0, "q23 s1"); eq(r.diff(t).norm(), 1, "q23 s3"); eq(sp.diff(r.norm(), t), 0, "q23 s3b")
    ff = sp.Function("f")(t); u = V(1, 2, 3)
    assert sp.simplify((ff * u).cross((ff * u).diff(t))) == sp.zeros(3, 1), "q23 s2"
    # q25
    r = V(2 * t, t**2, t**3 / 3); r1, r2 = r.diff(t).subs(t, 2), r.diff(t, 2).subs(t, 2)
    eq(r1.norm(), 6, "q25 A"); eq(r2.norm(), 2 * sp.sqrt(5), "q25 B")
    eq(r1.dot(r2), 24, "q25 C"); eq(r1.cross(r2).norm(), 12, "q25 D")
    # q26
    F, P, Q = V(2, -1, 1), V(1, 1, 1), V(3, 0, 2)
    assert (P - Q).cross(F) == sp.zeros(3, 1), "q26"
    # q27
    eq(V(2, -1, 1).dot(V(3, 4, 5) - V(1, 2, 3)), 4, "q27")
    # q28: tetra = 1/6 of box; ratio to parallelepiped is 1/6 not 1/3
    aa, bb, cc = V(1, 0, 0), V(0, 1, 0), V(0, 0, 1)
    # unit cube corner tetrahedron: volume 1/6 by integration
    x, y, z = sp.symbols("x y z")
    vol = sp.integrate(1, (z, 0, 1 - x - y), (y, 0, 1 - x), (x, 0, 1))
    eq(vol, sp.Rational(1, 6) * abs(box(aa, bb, cc)), "q28")
    # q29
    b1, b2, dA = V(1, 1, 1), V(2, 2, 2), V(1, 0, 0)
    assert b1.cross(b2) == sp.zeros(3, 1) and dA.cross(b1) != sp.zeros(3, 1), "q29 parallel distinct"
    eq(dA.cross(b1).norm() / b1.norm(), sp.sqrt(2) / sp.sqrt(3), "q29 dist")
    # q30
    r = sp.cos(t) * V(1, 0, 0) + sp.sin(t) * V(0, 1, 0)
    eq(r.dot(r.diff(t)), 0, "q30")
    # notes examples
    assert V(2, 0, 1).cross(V(1, 2, 3)) == V(-2, -5, 4)
    eq(V(-2, -5, 4).dot(V(2, -2, 1)) / 3, sp.Rational(10, 3), "notes moment line")
    assert V(0, 1, 1).cross(V(-3, 1, -1)) == V(-2, -3, 3) and V(1, 1, 0).dot(V(2, 3, -3)) == 5
    eq(abs(V(2, 1, -1).dot(V(1, -2, 2)) - 5) / 3, sp.Rational(7, 3), "notes dist")
    b1, b2 = V(2, -1, 1), V(3, -5, 2); assert b1.cross(b2) == V(3, -1, -7)
    eq(abs(V(1, 0, -1).dot(b1.cross(b2))) / b1.cross(b2).norm(), 10 / sp.sqrt(59), "notes SD")
    assert V(2, 1, -1).cross(V(2, 3, 6)) == V(9, -14, 4); eq(V(9, -14, 4).norm() / 7, sp.sqrt(293) / 7, "notes par")
    eq(box(V(1, 0, 2), V(2, 1, 1), V(2, 2, 3)), 5, "notes tetra")
    eq(box(V(1, 1, 1), V(1, -1, lam), V(2, 1, -1)), 5 + lam, "notes tetra lam")
    r = V(sp.exp(-t), 2 * sp.cos(3 * t), 2 * sp.sin(3 * t))
    eq(r.diff(t).subs(t, 0).norm(), sp.sqrt(37), "notes v"); eq(r.diff(t, 2).subs(t, 0).norm(), 5 * sp.sqrt(13), "notes a")
    r = V(t, t**2, t**3); v, acc = r.diff(t).subs(t, 1), r.diff(t, 2).subs(t, 1)
    assert v.cross(acc) == V(6, -6, 2); eq(v.dot(acc), 22, "notes aT"); eq(acc.norm()**2, 40, "notes a2")


T.write(check)
