import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from qlib import Topic, eq

T = Topic("math.geometry.lines-3d")

# 1
T.single(1, ["line-forms"],
    r"The direction ratios of the line $\dfrac{2x - 1}{3} = \dfrac{1 - y}{2} = \dfrac{z + 1}{4}$ are proportional to",
    [r"$3, -4, 8$", r"$3, 2, 4$", r"$3, -2, 4$", r"$3, 4, 8$"],
    r"""Make every numerator read "coordinate minus constant" with coefficient $+1$:
$$\frac{x - \frac12}{3/2} = \frac{y - 1}{-2} = \frac{z + 1}{4}.$$
So the direction ratios are $\tfrac32 : -2 : 4$, that is, $3 : -4 : 8$ after multiplying by $2$.

$3, 2, 4$ reads the denominators directly. $3, -2, 4$ fixes the sign of $y$ but forgets to divide by the coefficient $2$ of $x$.""")

# 2
T.single(1, ["line-forms"],
    r"The line $\dfrac{x - 1}{2} = \dfrac{y + 1}{3} = \dfrac{z - 2}{-1}$ meets the plane $z = 0$ at",
    [r"$(5, 5, 0)$", r"$(3, 2, 0)$", r"$(1, -1, 0)$", r"$(-3, -7, 0)$"],
    r"""The general point is $(1 + 2t,\ -1 + 3t,\ 2 - t)$. Setting $z = 0$ gives $t = 2$, so the point is
$$(1 + 4,\ -1 + 6,\ 0) = (5, 5, 0).$$

$(-3, -7, 0)$ uses $t = -2$ (the sign of the $z$ ratio dropped). $(1, -1, 0)$ just deletes the $z$-coordinate of the base point, and $(3, 2, 0)$ uses $t = 1$.""")

# 3
T.single(1, ["line-forms"],
    r"The equations of the line through $A(1, 2, 3)$ and $B(3, -1, 4)$ are",
    [r"$\dfrac{x - 1}{2} = \dfrac{y - 2}{-3} = \dfrac{z - 3}{1}$",
     r"$\dfrac{x - 1}{3} = \dfrac{y - 2}{-1} = \dfrac{z - 3}{4}$",
     r"$\dfrac{x - 1}{2} = \dfrac{y - 2}{3} = \dfrac{z - 3}{1}$",
     r"$\dfrac{x - 3}{2} = \dfrac{y + 1}{-3} = \dfrac{z - 4}{-1}$"],
    r"""The direction is $\overrightarrow{AB} = (3 - 1,\ -1 - 2,\ 4 - 3) = (2, -3, 1)$. Through $A$:
$$\frac{x - 1}{2} = \frac{y - 2}{-3} = \frac{z - 3}{1}.$$

Check: $t = 1$ gives $(3, -1, 4) = B$. The second option uses the coordinates of $B$ as the direction. The last option has the right point $B$ but a sign slip in the $z$ ratio.""")

# 4
T.single(1, ["line-and-plane"],
    r"The angle between the line $\dfrac{x - 1}{1} = \dfrac{y + 2}{1} = \dfrac{z - 3}{2}$ and the plane $2x - y + z = 5$ is",
    [r"$\dfrac{\pi}{6}$", r"$\dfrac{\pi}{3}$", r"$\dfrac{\pi}{4}$", r"$\sin^{-1}\dfrac13$"],
    r"""With $\vec b = (1, 1, 2)$ and $\vec n = (2, -1, 1)$:
$$\sin\theta = \frac{\lvert 2 - 1 + 2\rvert}{\sqrt6\,\sqrt6} = \frac{3}{6} = \frac12, \qquad \theta = \frac{\pi}{6}.$$

$\frac{\pi}{3}$ comes from using $\cos\theta$: that is the angle between the line and the **normal**, which is the complement of the required angle.""")

# 5
T.single(1, ["line-and-plane"],
    r"The line $\dfrac{x - 1}{2} = \dfrac{y - 2}{3} = \dfrac{z - 3}{k}$ is parallel to the plane $2x - y + z = 4$. Then $k$ equals",
    [r"$-1$", r"$1$", r"$5$", r"$-5$"],
    r"""Parallel to the plane means the direction is perpendicular to the normal:
$$2(2) + 3(-1) + k(1) = 0 \;\Rightarrow\; k = -1.$$
The point $(1, 2, 3)$ gives $2 - 2 + 3 = 3 \ne 4$, so the line is parallel to the plane and not in it.

$k = 1$ is a sign slip. $k = -5$ uses $\vec n = (1, 1, 1)$, that is, ignores the coefficients of the plane.""")

# 6
T.single(2, ["line-and-plane"],
    r"The line $\dfrac{x - 1}{1} = \dfrac{y - 2}{2} = \dfrac{z - 3}{1}$ lies in the plane $x + ay + bz = 6$. Then $(a, b)$ is",
    [r"$(-2, 3)$", r"$(2, -3)$", r"$(-1, 1)$", r"$(-2, -3)$"],
    r"""Two conditions are needed.

- Direction perpendicular to the normal: $1 + 2a + b = 0$.
- The point $(1, 2, 3)$ on the plane: $1 + 2a + 3b = 6$.

Subtracting, $2b = 6$, so $b = 3$ and $a = -2$. The plane is $x - 2y + 3z = 6$.

$(-1, 1)$ satisfies only the direction condition: then the line is parallel to $x - y + z = 6$ but not in it, since $1 - 2 + 3 = 2 \ne 6$.""")

# 7
T.single(2, ["planes-to-line"],
    r"The symmetric form of the line $x + y + z = 6,\ x - y + 2z = 5$ is",
    [r"$\dfrac{x - 1}{3} = \dfrac{y - 2}{-1} = \dfrac{z - 3}{-2}$",
     r"$\dfrac{x - 1}{3} = \dfrac{y - 2}{1} = \dfrac{z - 3}{-2}$",
     r"$\dfrac{x - 1}{1} = \dfrac{y - 2}{-1} = \dfrac{z - 3}{2}$",
     r"$\dfrac{x - 1}{-3} = \dfrac{y - 2}{-1} = \dfrac{z - 3}{2}$"],
    r"""**Direction:** the cross product of the normals:
$$(1, 1, 1) \times (1, -1, 2) = (1\cdot2 - 1\cdot(-1),\ 1\cdot1 - 1\cdot2,\ 1\cdot(-1) - 1\cdot1) = (3, -1, -2).$$
**Point:** $(1, 2, 3)$ satisfies both planes ($1 + 2 + 3 = 6$, $1 - 2 + 6 = 5$).

The third option uses the second normal as the direction. Check: a direction must satisfy $\vec n_1\cdot\vec b = \vec n_2\cdot\vec b = 0$, and only $(3, -1, -2)$ does.""")

# 8
T.single(2, ["perpendicular-image"],
    r"The foot of the perpendicular from $P(1, 6, 3)$ to the line $\dfrac{x}{1} = \dfrac{y - 1}{2} = \dfrac{z - 2}{3}$ is",
    [r"$(1, 3, 5)$", r"$(1, 0, 7)$", r"$(2, 5, 8)$", r"$(0, 1, 2)$"],
    r"""Take $Q = (t,\ 1 + 2t,\ 2 + 3t)$, so $\overrightarrow{PQ} = (t - 1,\ 2t - 5,\ 3t - 1)$. Perpendicular to $(1, 2, 3)$:
$$(t - 1) + 2(2t - 5) + 3(3t - 1) = 14t - 14 = 0 \;\Rightarrow\; t = 1.$$
The foot is $Q = (1, 3, 5)$, and $PQ = \sqrt{0 + 9 + 4} = \sqrt{13}$.

$(1, 0, 7) = 2Q - P$ is the **image** of $P$, not the foot. $(0, 1, 2)$ is just the given point of the line.""")

# 9
T.single(2, ["perpendicular-image"],
    r"The perpendicular distance of the point $(3, -1, 11)$ from the line $\dfrac{x}{2} = \dfrac{y - 2}{3} = \dfrac{z - 3}{4}$ is",
    [r"$\sqrt{53}$", r"$\sqrt{29}$", r"$\sqrt{82}$", r"$53$"],
    r"""Take $Q = (2t,\ 2 + 3t,\ 3 + 4t)$, so $\overrightarrow{PQ} = (2t - 3,\ 3t + 3,\ 4t - 8)$. Then
$$2(2t - 3) + 3(3t + 3) + 4(4t - 8) = 29t - 29 = 0 \;\Rightarrow\; t = 1,$$
so the foot is $(2, 5, 7)$ and the distance is
$$\sqrt{1 + 36 + 16} = \sqrt{53}.$$

$\sqrt{82}$ is the distance from $(3, -1, 11)$ to the base point $(0, 2, 3)$, not to the line. $\sqrt{29}$ is the length of the **projection** of that segment on the line, $\frac{(3, -3, 8)\cdot(2, 3, 4)}{\sqrt{29}}$. Fast check by Pythagoras: $82 - 29 = 53$. $53$ forgets the square root.""")

# 10
T.single(3, ["perpendicular-image"],
    r"The image of the point $(5, 9, 3)$ in the line $\dfrac{x - 1}{2} = \dfrac{y - 2}{3} = \dfrac{z - 3}{4}$ is",
    [r"$(1, 1, 11)$", r"$(3, 5, 7)$", r"$(7, 13, -1)$", r"$(-1, -1, -1)$"],
    r"""Foot: $Q = (1 + 2t,\ 2 + 3t,\ 3 + 4t)$ with
$$2(2t - 4) + 3(3t - 7) + 4(4t) = 29t - 29 = 0 \;\Rightarrow\; t = 1,\quad Q = (3, 5, 7).$$
Image $= 2Q - P = (6 - 5,\ 10 - 9,\ 14 - 3) = (1, 1, 11)$.

$(3, 5, 7)$ is the foot. $(7, 13, -1) = 2P - Q$ reverses the roles of $P$ and $Q$. Check: the midpoint of $(5, 9, 3)$ and $(1, 1, 11)$ is $(3, 5, 7)$.""")

# 11
T.single(2, ["perpendicular-image"],
    r"The image of the point $(1, 3, 4)$ in the plane $2x - y + z + 3 = 0$ is",
    [r"$(-3, 5, 2)$", r"$(-1, 4, 3)$", r"$(5, 1, 6)$", r"$(-3, 1, 2)$"],
    r"""Here $2(1) - 3 + 4 + 3 = 6$ and $a^2 + b^2 + c^2 = 6$. So
$$\frac{x - 1}{2} = \frac{y - 3}{-1} = \frac{z - 4}{1} = -2\cdot\frac{6}{6} = -2,$$
which gives $(1 - 4,\ 3 + 2,\ 4 - 2) = (-3, 5, 2)$.

$(-1, 4, 3)$ uses the factor $-1$: that is the foot. $(5, 1, 6)$ has the sign of the factor wrong. Check: $(-3, 5, 2)$ gives $-6 - 5 + 2 + 3 = -6$, equal and opposite to $+6$.""")

# 12
T.single(1, ["shortest-distance"],
    r"For the skew lines $\vec r = \vec a_1 + t\vec b_1$ and $\vec r = \vec a_2 + s\vec b_2$, the shortest distance is",
    [r"$\dfrac{\lvert(\vec a_2 - \vec a_1)\cdot(\vec b_1 \times \vec b_2)\rvert}{\lvert \vec b_1 \times \vec b_2\rvert}$",
     r"$\dfrac{\lvert(\vec a_2 - \vec a_1)\cdot(\vec b_1 \times \vec b_2)\rvert}{\lvert \vec b_1\rvert\,\lvert \vec b_2\rvert}$",
     r"$\dfrac{\lvert(\vec a_2 - \vec a_1)\times(\vec b_1 \times \vec b_2)\rvert}{\lvert \vec b_1 \times \vec b_2\rvert}$",
     r"$\dfrac{\lvert(\vec a_2 - \vec a_1)\times\vec b_1\rvert}{\lvert \vec b_1\rvert}$"],
    r"""The common perpendicular has direction $\vec n = \vec b_1 \times \vec b_2$. The shortest distance is the projection of $\vec a_2 - \vec a_1$ on $\vec n$:
$$\text{S.D.} = \frac{\lvert(\vec a_2 - \vec a_1)\cdot\vec n\rvert}{\lvert \vec n\rvert}.$$

Dividing by $\lvert \vec b_1\rvert\lvert \vec b_2\rvert$ is right only when the lines are perpendicular. The last option is the distance between **parallel** lines (or of a point from a line).""")

# 13
T.single(2, ["shortest-distance"],
    r"The shortest distance between the lines $\dfrac{x - 3}{1} = \dfrac{y - 5}{-2} = \dfrac{z - 7}{1}$ and $\dfrac{x + 1}{7} = \dfrac{y + 1}{-6} = \dfrac{z + 1}{1}$ is",
    [r"$2\sqrt{29}$", r"$\sqrt{29}$", r"$4\sqrt{29}$", r"$\dfrac{58}{\sqrt{129}}$"],
    r"""$\vec b_1 \times \vec b_2 = (1, -2, 1) \times (7, -6, 1) = (4, 6, 8)$, and $\vec a_2 - \vec a_1 = (-4, -6, -8)$. So
$$\text{S.D.} = \frac{\lvert -16 - 36 - 64\rvert}{\sqrt{16 + 36 + 64}} = \frac{116}{\sqrt{116}} = \sqrt{116} = 2\sqrt{29}.$$

$\frac{58}{\sqrt{129}}$ divides $116$ by $\lvert \vec b_1\rvert\lvert \vec b_2\rvert = \sqrt6\sqrt{86}$ instead of by $\lvert \vec b_1 \times \vec b_2\rvert$. $\sqrt{29}$ uses the halved normal $(2, 3, 4)$ in the numerator but not in the denominator; $4\sqrt{29}$ does the reverse.""")

# 14
T.single(3, ["shortest-distance"],
    r"The equations of the line of shortest distance between $\dfrac{x - 3}{1} = \dfrac{y - 5}{-2} = \dfrac{z - 7}{1}$ and $\dfrac{x + 1}{7} = \dfrac{y + 1}{-6} = \dfrac{z + 1}{1}$ are",
    [r"$\dfrac{x - 3}{2} = \dfrac{y - 5}{3} = \dfrac{z - 7}{4}$",
     r"$\dfrac{x - 3}{2} = \dfrac{y - 5}{-3} = \dfrac{z - 7}{4}$",
     r"$\dfrac{x - 3}{4} = \dfrac{y - 5}{3} = \dfrac{z - 7}{2}$",
     r"$\dfrac{x + 1}{2} = \dfrac{y + 1}{-3} = \dfrac{z + 1}{4}$"],
    r"""Take $P = (3 + t,\ 5 - 2t,\ 7 + t)$ and $Q = (-1 + 7s,\ -1 - 6s,\ -1 + s)$. Then
$$\overrightarrow{PQ} = (7s - t - 4,\ -6s + 2t - 6,\ s - t - 8).$$
Setting $\overrightarrow{PQ}\cdot(1, -2, 1) = 0$ and $\overrightarrow{PQ}\cdot(7, -6, 1) = 0$:
$$20s - 6t = 0, \qquad 86s - 20t = 0 \;\Rightarrow\; t = s = 0.$$
So the feet are $P = (3, 5, 7)$ and $Q = (-1, -1, -1)$, and $\overrightarrow{QP} = (4, 6, 8) \propto (2, 3, 4)$:
$$\frac{x - 3}{2} = \frac{y - 5}{3} = \frac{z - 7}{4}.$$

Check: the direction must be $\propto \vec b_1 \times \vec b_2 = (4, 6, 8)$, which rules out the second and third options. The last option passes through the right foot $(-1, -1, -1)$ but has the wrong direction.""")

# 15
T.single(2, ["coplanar-lines"],
    r"The lines $\dfrac{x - 1}{2} = \dfrac{y + 1}{3} = \dfrac{z - 1}{4}$ and $\dfrac{x - 3}{1} = \dfrac{y - k}{2} = \dfrac{z}{1}$ intersect when $k$ equals",
    [r"$\dfrac92$", r"$-\dfrac92$", r"$\dfrac29$", r"$\dfrac{11}{2}$"],
    r"""The lines are not parallel, so they intersect if and only if they are coplanar:
$$\begin{vmatrix} 2 & k + 1 & -1 \\ 2 & 3 & 4 \\ 1 & 2 & 1 \end{vmatrix} = 2(3 - 8) - (k + 1)(2 - 4) - (4 - 3) = 2k - 9 = 0.$$
So $k = \frac92$.

$\frac{11}{2}$ comes from using $k - 1$ in place of $k + 1$ in the first row ($\vec a_2 - \vec a_1$ has $y$-component $k - (-1)$).""")

# 16
T.single(2, ["coplanar-lines"],
    r"The plane containing the lines $\dfrac{x + 1}{-3} = \dfrac{y - 3}{2} = \dfrac{z + 2}{1}$ and $\dfrac{x}{1} = \dfrac{y - 7}{-3} = \dfrac{z + 7}{2}$ is",
    [r"$x + y + z = 0$", r"$x - y + z + 6 = 0$", r"$x + y + z = 2$", r"$7x + 7y + 7z = 14$"],
    r"""Normal: $(-3, 2, 1) \times (1, -3, 2) = (4 + 3,\ 1 + 6,\ 9 - 2) = (7, 7, 7) \propto (1, 1, 1)$. Through $(-1, 3, -2)$:
$$x + y + z = -1 + 3 - 2 = 0.$$
The second point $(0, 7, -7)$ also satisfies $x + y + z = 0$, which confirms that the lines are coplanar.

$x - y + z + 6 = 0$ passes through $(-1, 3, -2)$ but does not contain the direction $(-3, 2, 1)$, since $-3 - 2 + 1 \ne 0$.""")

# 17
T.single(2, ["coplanar-lines"],
    r"The lines $\dfrac{x - 1}{2} = \dfrac{y - 2}{3} = \dfrac{z - 3}{4}$ and $\dfrac{x - 4}{5} = \dfrac{y - 1}{2} = \dfrac{z}{1}$ meet at",
    [r"$(-1, -1, -1)$", r"$(1, 1, 1)$", r"$(3, 5, 7)$", r"$(9, 3, 1)$"],
    r"""Equate the general points $(1 + 2t,\ 2 + 3t,\ 3 + 4t)$ and $(4 + 5s,\ 1 + 2s,\ s)$:
$$2t - 5s = 3, \qquad 3t - 2s = -1.$$
These give $t = s = -1$. The third equation, $3 + 4t = s$, also holds ($-1 = -1$), so the lines do meet, at
$$(1 - 2,\ 2 - 3,\ 3 - 4) = (-1, -1, -1).$$

$(3, 5, 7)$ and $(9, 3, 1)$ are the points with $t = 1$ on the first line and $s = 1$ on the second; each lies on only one line.""")

# 18
T.single(2, ["shortest-distance"],
    r"The distance between the parallel lines $\vec r = (1, 2, -4) + t(2, 3, 6)$ and $\vec r = (3, 3, -5) + s(2, 3, 6)$ is",
    [r"$\dfrac{\sqrt{293}}{7}$", r"$\sqrt6$", r"$\dfrac17$", r"$\dfrac{\sqrt{293}}{49}$"],
    r"""For parallel lines the skew-line formula gives $0/0$; use
$$d = \frac{\lvert(\vec a_2 - \vec a_1)\times\vec b\rvert}{\lvert \vec b\rvert}.$$
Here $(2, 1, -1) \times (2, 3, 6) = (6 + 3,\ -2 - 12,\ 6 - 2) = (9, -14, 4)$, of length $\sqrt{293}$, and $\lvert \vec b\rvert = 7$. So $d = \frac{\sqrt{293}}{7}$.

$\sqrt6$ is the distance between the two base points. $\frac17$ uses the dot product, which gives the projection **along** the lines. $\frac{\sqrt{293}}{49}$ divides by $\lvert \vec b\rvert^2$.""")

# 19
T.single(3, ["line-and-plane"],
    r"The distance of the point $(2, -1, 2)$ from the plane $x - y + z = 16$, measured parallel to the line $\dfrac{x}{3} = \dfrac{y}{4} = \dfrac{z}{12}$, is",
    [r"$13$", r"$\dfrac{11}{\sqrt3}$", r"$\dfrac{13}{\sqrt3}$", r"$1$"],
    r"""The line through $(2, -1, 2)$ in the given direction has general point $(2 + 3t,\ -1 + 4t,\ 2 + 12t)$. On the plane:
$$(2 + 3t) - (-1 + 4t) + (2 + 12t) = 5 + 11t = 16 \;\Rightarrow\; t = 1.$$
So it meets the plane at $(5, 3, 14)$, and the distance is
$$\lvert t\rvert\sqrt{9 + 16 + 144} = 13.$$

$\frac{11}{\sqrt3}$ is the **perpendicular** distance $\frac{\lvert 2 + 1 + 2 - 16\rvert}{\sqrt3}$, which ignores the given direction. $1$ is the parameter $t$, read off without multiplying by $\lvert \vec b\rvert$.""")

# 20
T.single(3, ["line-and-plane"],
    r"The projection of the line $\dfrac{x - 1}{2} = \dfrac{y + 1}{-1} = \dfrac{z - 3}{4}$ on the plane $x + 2y + z = 9$ is the line",
    [r"$x + 2y + z = 9,\ 9x - 2y - 5z + 4 = 0$",
     r"$x + 2y + z = 9,\ 9x - 2y - 5z - 4 = 0$",
     r"$x + 2y + z = 9,\ 9x + 2y - 5z + 8 = 0$",
     r"$x + 2y + z = 9,\ 2x - y + 4z - 15 = 0$"],
    r"""The projection lies in the given plane and in the plane through the line perpendicular to it. That plane's normal is
$$(2, -1, 4) \times (1, 2, 1) = (-1 - 8,\ 4 - 2,\ 4 + 1) = (-9, 2, 5).$$
Through $(1, -1, 3)$:
$$-9(x - 1) + 2(y + 1) + 5(z - 3) = 0 \;\Rightarrow\; 9x - 2y - 5z + 4 = 0.$$

Check: $(1, -1, 3)$ gives $9 + 2 - 15 + 4 = 0$. With $-4$ the plane misses the point. $2x - y + 4z - 15 = 0$ is the plane through the point with normal along the line itself, which is perpendicular to the line, not a plane containing it.""")

# 21
T.single(3, ["shortest-distance"],
    r"The shortest distance between the lines $\dfrac{x}{2} = \dfrac{y}{-3} = \dfrac{z}{1}$ and $\dfrac{x - 2}{3} = \dfrac{y - 1}{-5} = \dfrac{z + 2}{2}$ is",
    [r"$\dfrac{1}{\sqrt3}$", r"$\dfrac13$", r"$\sqrt3$", r"$\dfrac{5}{\sqrt3}$"],
    r"""$\vec b_1 \times \vec b_2 = (2, -3, 1) \times (3, -5, 2) = (-6 + 5,\ 3 - 4,\ -10 + 9) = (-1, -1, -1)$, and $\vec a_2 - \vec a_1 = (2, 1, -2)$. So
$$\text{S.D.} = \frac{\lvert -2 - 1 + 2\rvert}{\sqrt3} = \frac{1}{\sqrt3}.$$

$\frac{5}{\sqrt3}$ drops the sign of the $z$-component, using $+2$ in place of $-2$. $\frac13$ divides by $\lvert \vec n\rvert^2 = 3$.""")

# 22 statements: 1 and 3 only
T.statements(1, ["line-and-plane"],
    r"Let $L$ be the line $\dfrac{x - x_1}{l} = \dfrac{y - y_1}{m} = \dfrac{z - z_1}{n}$ and $\Pi$ the plane $ax + by + cz + d = 0$. Consider the following statements:",
    [r"If $al + bm + cn = 0$ and $ax_1 + by_1 + cz_1 + d = 0$, then $L$ lies in $\Pi$.",
     r"The angle $\theta$ between $L$ and $\Pi$ satisfies $\cos\theta = \dfrac{\lvert al + bm + cn\rvert}{\sqrt{a^2 + b^2 + c^2}\sqrt{l^2 + m^2 + n^2}}$.",
     r"If $\dfrac{l}{a} = \dfrac{m}{b} = \dfrac{n}{c}$, then $L$ is perpendicular to $\Pi$."],
    [r"1 and 3 only", r"1 only", r"2 and 3 only", r"1, 2 and 3"],
    r"""1. True. The line is parallel to the plane and has a point on it, so every point $(x_1 + lt, \dots)$ satisfies the plane: the left side changes by $t(al + bm + cn) = 0$.
2. False. That expression is $\cos$ of the angle with the **normal**. The angle with the plane is its complement, so the expression equals $\sin\theta$.
3. True. The line is parallel to the normal $(a, b, c)$.""")

# 23 statements: 2 only
T.statements(3, ["coplanar-lines", "shortest-distance"],
    r"Consider the following statements about two distinct lines $L_1, L_2$ in space, through $A_1, A_2$ with directions $\vec b_1, \vec b_2$:",
    [r"If $L_1$ and $L_2$ do not intersect, they are parallel.",
     r"If $L_1$ and $L_2$ are skew, there is exactly one line that meets both of them at right angles.",
     r"If $\left[\overrightarrow{A_1A_2},\ \vec b_1,\ \vec b_2\right] = 0$, then $L_1$ and $L_2$ intersect."],
    [r"2 only", r"2 and 3 only", r"1 and 2 only", r"1, 2 and 3"],
    r"""1. False. In space, non-intersecting lines may be **skew**. For example, the $x$-axis and the line $x = 0,\ z = 1$ (parallel to the $y$-axis) never meet and are not parallel.
2. True. The common perpendicular is unique for skew lines: its direction must be $\vec b_1 \times \vec b_2$, and the two perpendicularity conditions fix its feet uniquely.
3. False. A zero box product means the lines are **coplanar**. Distinct parallel lines also give $0$, since $\vec b_1 \parallel \vec b_2$, yet they never meet. The statement needs "non-parallel".""")

# 24 match: A-2, B-3, C-1, D-4
T.match(2, ["line-and-plane"],
    r"For the line $L: \dfrac{x - 1}{2} = \dfrac{y - 2}{-1} = \dfrac{z - 3}{2}$, match each plane in List I with the relation of $L$ to it in List II.",
    [r"$2x - y + 2z = 7$", r"$x + 2y = 3$", r"$x + 2y = 5$", r"$x + y + z = 1$"],
    [r"$L$ lies in the plane", r"$L$ is perpendicular to the plane", r"$L$ is parallel to the plane but not in it",
     r"$L$ meets the plane at an angle $\sin^{-1}\dfrac{1}{\sqrt3}$"],
    [r"A-2, B-3, C-1, D-4", r"A-2, B-1, C-3, D-4", r"A-4, B-3, C-1, D-2", r"A-2, B-3, C-4, D-1"],
    r"""Let $\vec b = (2, -1, 2)$ and the point $(1, 2, 3)$.
- A: the normal $(2, -1, 2) = \vec b$, so $L$ is perpendicular to the plane (2).
- B: $\vec b\cdot(1, 2, 0) = 0$, but $1 + 4 = 5 \ne 3$: parallel, not in the plane (3).
- C: the same normal, and $1 + 4 = 5$: $L$ lies in the plane (1).
- D: $\sin\theta = \dfrac{\lvert 2 - 1 + 2\rvert}{3\sqrt3} = \dfrac{1}{\sqrt3}$ (4).

Answer: A-2, B-3, C-1, D-4. B and C have the same normal; only the point test separates them.""")

# 25 match: A-3, B-1, C-2, D-4
T.match(3, ["shortest-distance"],
    r"Match each pair of lines in List I with the shortest distance between them in List II.",
    [r"the $x$-axis and the $y$-axis",
     r"the $x$-axis and the line $x = 0,\ z = 2$",
     r"$\dfrac{x}{1} = \dfrac{y}{2} = \dfrac{z}{2}$ and $\dfrac{x - 1}{2} = \dfrac{y}{-2} = \dfrac{z + 1}{1}$",
     r"$\vec r = t(1, 1, 0)$ and $\vec r = (1, 0, 0) + s(1, 1, 0)$"],
    [r"$2$", r"$\dfrac43$", r"$0$", r"$\dfrac{1}{\sqrt2}$"],
    [r"A-3, B-1, C-2, D-4", r"A-3, B-2, C-1, D-4", r"A-3, B-1, C-4, D-2", r"A-1, B-3, C-2, D-4"],
    r"""- A: the axes meet at the origin, so the distance is $0$ (3).
- B: the second line is parallel to the $y$-axis through $(0, 0, 2)$. With $\vec b_1 \times \vec b_2 = (1, 0, 0) \times (0, 1, 0) = (0, 0, 1)$ and $\vec a_2 - \vec a_1 = (0, 0, 2)$, the distance is $2$ (1).
- C: $(1, 2, 2) \times (2, -2, 1) = (6, 3, -6)$, of length $9$, and $(1, 0, -1)\cdot(6, 3, -6) = 12$. So the distance is $\frac{12}{9} = \frac43$ (2).
- D: the lines are parallel: $\dfrac{\lvert(1, 0, 0) \times (1, 1, 0)\rvert}{\sqrt2} = \dfrac{\lvert(0, 0, 1)\rvert}{\sqrt2} = \dfrac{1}{\sqrt2}$ (4).

Answer: A-3, B-1, C-2, D-4.""")

# 26 AR: 0
T.assertion_reason(1, ["line-and-plane"],
    r"The line $\dfrac{x}{1} = \dfrac{y}{2} = \dfrac{z}{3}$ is perpendicular to the plane $2x + 4y + 6z = 7$.",
    r"A line with direction ratios $l, m, n$ is perpendicular to the plane $ax + by + cz + d = 0$ if and only if $l : m : n = a : b : c$.",
    0,
    r"""Assertion: true, since $(2, 4, 6) = 2(1, 2, 3)$.

Reason: true; perpendicular to the plane means parallel to its normal $(a, b, c)$. The reason is exactly the test used, so it explains the assertion.""")

# 27 AR: 2
T.assertion_reason(2, ["coplanar-lines"],
    r"The lines $\dfrac{x - 1}{2} = \dfrac{y - 2}{3} = \dfrac{z - 3}{4}$ and $\dfrac{x - 2}{3} = \dfrac{y - 4}{4} = \dfrac{z - 5}{5}$ are skew.",
    r"Any two lines in space that are not parallel are skew.",
    2,
    r"""Assertion: true. The directions $(2, 3, 4)$ and $(3, 4, 5)$ are not proportional, and
$$\begin{vmatrix} 1 & 2 & 2 \\ 2 & 3 & 4 \\ 3 & 4 & 5 \end{vmatrix} = 1(15 - 16) - 2(10 - 12) + 2(8 - 9) = 1 \ne 0,$$
so the lines are not coplanar.

Reason: false. Non-parallel lines can **intersect**, for example the $x$- and $y$-axes. Skew needs non-parallel **and** non-coplanar.""")

# 28 AR: 3
T.assertion_reason(2, ["line-and-plane"],
    r"The line $\dfrac{x - 2}{1} = \dfrac{y - 3}{1} = \dfrac{z - 4}{-2}$ lies in the plane $x + y + z = 7$.",
    r"If the direction of a line is perpendicular to the normal of a plane, then the line is either parallel to the plane or lies in it.",
    3,
    r"""Assertion: false. The direction condition holds, $1 + 1 - 2 = 0$, but the point $(2, 3, 4)$ gives $2 + 3 + 4 = 9 \ne 7$. So the line is parallel to the plane and does not lie in it. (It lies in $x + y + z = 9$.)

Reason: true. $\vec b\cdot\vec n = 0$ means the line never crosses the plane transversally. Whether it lies in the plane depends on one point.""")

# 29 AR: 1
T.assertion_reason(3, ["coplanar-lines"],
    r"The lines $\dfrac{x + 1}{3} = \dfrac{y + 3}{5} = \dfrac{z + 5}{7}$ and $\dfrac{x - 2}{1} = \dfrac{y - 4}{3} = \dfrac{z - 6}{5}$ are coplanar.",
    r"Any two parallel lines are coplanar.",
    1,
    r"""Assertion: true.
$$\begin{vmatrix} 3 & 7 & 11 \\ 3 & 5 & 7 \\ 1 & 3 & 5 \end{vmatrix} = 3(25 - 21) - 7(15 - 7) + 11(9 - 5) = 12 - 56 + 44 = 0.$$
The lines in fact meet at $\left(\tfrac12, -\tfrac12, -\tfrac32\right)$.

Reason: true; two parallel lines span a plane. But the given lines are **not** parallel, since $(3, 5, 7) \not\propto (1, 3, 5)$. So the reason does not explain the assertion.""")

# 30 AR: 0
T.assertion_reason(2, ["perpendicular-image"],
    r"The image of the origin in the plane $x + y + z = 3$ is $(2, 2, 2)$.",
    r"The image of $(\alpha, \beta, \gamma)$ in $ax + by + cz + d = 0$ is given by $\dfrac{x - \alpha}{a} = \dfrac{y - \beta}{b} = \dfrac{z - \gamma}{c} = -\dfrac{2(a\alpha + b\beta + c\gamma + d)}{a^2 + b^2 + c^2}$.",
    0,
    r"""Assertion: true. The ratio is $-\dfrac{2(0 - 3)}{3} = 2$, so the image is $(2, 2, 2)$. Check: the midpoint $(1, 1, 1)$ lies on the plane, and $(2, 2, 2)$ is along the normal.

Reason: true; it is the standard image formula, and the assertion is obtained by substituting into it. So the reason explains the assertion.""")


def check():
    import sympy as sp
    M = sp.Matrix
    t, s, k, a, b = sp.symbols("t s k a b")
    x, y, z = sp.symbols("x y z")

    def same_line(p1, d1, p2, d2):
        return d1.cross(d2) == M([0, 0, 0]) and (p2 - p1).cross(d1) == M([0, 0, 0])

    def sd(a1, b1, a2, b2):
        n = b1.cross(b2)
        return sp.Abs((a2 - a1).dot(n)) / n.norm()

    def par_dist(a1, a2, bb):
        return (a2 - a1).cross(bb).norm() / bb.norm()

    def foot(P, A, B):
        tt = sp.solve((A + t * B - P).dot(B), t)[0]
        return A + tt * B

    def sin_angle(bb, n):
        return sp.Abs(bb.dot(n)) / (bb.norm() * n.norm())

    def image_plane(P, n, d):
        r = -2 * (n.dot(P) + d) / n.dot(n)
        return P + r * n

    # q1: direction of (2x-1)/3 = (1-y)/2 = (z+1)/4 : points at t=0, t=1
    pt = lambda tt: M([(3 * tt + 1) / sp.Integer(2), 1 - 2 * tt, 4 * tt - 1])
    d1 = pt(1) - pt(0)
    eq(d1.cross(M([3, -4, 8])).norm(), 0, "q1")
    assert d1.cross(M([3, 2, 4])).norm() != 0 and d1.cross(M([3, -2, 4])).norm() != 0 and d1.cross(M([3, 4, 8])).norm() != 0

    # q2
    P = M([1 + 2 * t, -1 + 3 * t, 2 - t]); ts = sp.solve(P[2], t)[0]
    assert P.subs(t, ts) == M([5, 5, 0])

    # q3
    A, B = M([1, 2, 3]), M([3, -1, 4])
    assert same_line(A, M([2, -3, 1]), A, B - A)
    assert not same_line(A, M([3, -1, 4]), A, B - A)
    assert not same_line(A, M([2, 3, 1]), A, B - A)
    assert not same_line(B, M([2, -3, -1]), A, B - A)

    # q4
    eq(sp.asin(sin_angle(M([1, 1, 2]), M([2, -1, 1]))), sp.pi / 6, "q4")

    # q5
    ks = sp.solve(M([2, 3, k]).dot(M([2, -1, 1])), k)
    assert ks == [-1]
    assert M([2, -1, 1]).dot(M([1, 2, 3])) != 4  # not in the plane

    # q6
    sol = sp.solve([1 + 2 * a + b, 1 + 2 * a + 3 * b - 6], [a, b])
    assert sol == {a: -2, b: 3}
    # distractor (-1,1) satisfies direction only
    assert 1 + 2 * (-1) + 1 == 0 and 1 + 2 * (-1) + 3 * 1 != 6

    # q7
    n1, n2 = M([1, 1, 1]), M([1, -1, 2])
    dd = n1.cross(n2)
    assert dd == M([3, -1, -2])
    p0 = M([1, 2, 3]); assert n1.dot(p0) == 6 and n2.dot(p0) == 5
    for wrong in ([3, 1, -2], [1, -1, 2], [-3, -1, 2]):
        assert dd.cross(M(wrong)).norm() != 0

    # q8
    F = foot(M([1, 6, 3]), M([0, 1, 2]), M([1, 2, 3]))
    assert F == M([1, 3, 5])
    eq((F - M([1, 6, 3])).norm(), sp.sqrt(13), "q8 dist")

    # q9
    P9, A9, B9 = M([3, -1, 11]), M([0, 2, 3]), M([2, 3, 4])
    F = foot(P9, A9, B9); assert F == M([2, 5, 7])
    eq((F - P9).norm(), sp.sqrt(53), "q9")
    eq(par_dist(A9, P9, B9), sp.sqrt(53), "q9 cross")
    eq((P9 - A9).norm(), sp.sqrt(82), "q9 d1")
    eq((P9 - A9).dot(B9) / B9.norm(), sp.sqrt(29), "q9 proj")

    # q10
    P10 = M([5, 9, 3]); F = foot(P10, M([1, 2, 3]), M([2, 3, 4]))
    assert F == M([3, 5, 7]) and 2 * F - P10 == M([1, 1, 11])

    # q11
    assert image_plane(M([1, 3, 4]), M([2, -1, 1]), 3) == M([-3, 5, 2])

    # q12: formula check on an example against brute-force minimum
    a1, b1, a2, b2 = M([0, 0, 0]), M([1, 0, 0]), M([0, 0, 2]), M([0, 1, 0])
    eq(sd(a1, b1, a2, b2), 2, "q12")

    # q13
    a1, b1, a2, b2 = M([3, 5, 7]), M([1, -2, 1]), M([-1, -1, -1]), M([7, -6, 1])
    eq(sd(a1, b1, a2, b2), 2 * sp.sqrt(29), "q13")
    eq(sp.Abs((a2 - a1).dot(b1.cross(b2))) / (b1.norm() * b2.norm()), 58 / sp.sqrt(129), "q13 distractor")

    # q14
    Pp, Qq = a1 + t * b1, a2 + s * b2
    sol = sp.solve([(Qq - Pp).dot(b1), (Qq - Pp).dot(b2)], [t, s])
    fp, fq = Pp.subs(sol), Qq.subs(sol)
    assert fp == M([3, 5, 7]) and fq == M([-1, -1, -1])
    assert same_line(M([3, 5, 7]), M([2, 3, 4]), fp, fq - fp)
    for p, d in (([3, 5, 7], [2, -3, 4]), ([3, 5, 7], [4, 3, 2]), ([-1, -1, -1], [2, -3, 4])):
        assert not same_line(M(p), M(d), fp, fq - fp)

    # q15
    det = M([[2, k + 1, -1], [2, 3, 4], [1, 2, 1]]).det()
    assert sp.solve(det, k) == [sp.Rational(9, 2)]
    sol = sp.solve(list(M([1, -1, 1]) + t * M([2, 3, 4]) - M([3, sp.Rational(9, 2), 0]) - s * M([1, 2, 1])), [t, s])
    assert sol  # they really meet

    # q16
    A1, B1, A2, B2 = M([-1, 3, -2]), M([-3, 2, 1]), M([0, 7, -7]), M([1, -3, 2])
    n = B1.cross(B2); assert n == M([7, 7, 7])
    plane = lambda p: p[0] + p[1] + p[2]
    assert plane(A1) == 0 and plane(A2) == 0 and M([1, 1, 1]).dot(B1) == 0 and M([1, 1, 1]).dot(B2) == 0
    assert M([1, -1, 1]).dot(B1) != 0  # distractor misses direction
    assert plane(A1) != 2

    # q17
    sol = sp.solve(list(M([1, 2, 3]) + t * M([2, 3, 4]) - M([4, 1, 0]) - s * M([5, 2, 1])), [t, s])
    assert sol == {t: -1, s: -1}
    assert (M([1, 2, 3]) + t * M([2, 3, 4])).subs(sol) == M([-1, -1, -1])

    # q18
    eq(par_dist(M([1, 2, -4]), M([3, 3, -5]), M([2, 3, 6])), sp.sqrt(293) / 7, "q18")

    # q19
    Pl = M([2 + 3 * t, -1 + 4 * t, 2 + 12 * t])
    tt = sp.solve(Pl[0] - Pl[1] + Pl[2] - 16, t)[0]
    assert Pl.subs(t, tt) == M([5, 3, 14])
    eq((Pl.subs(t, tt) - M([2, -1, 2])).norm(), 13, "q19")
    eq(sp.Abs(2 + 1 + 2 - 16) / sp.sqrt(3), 11 / sp.sqrt(3), "q19 perp")

    # q20
    bL, nP, p0 = M([2, -1, 4]), M([1, 2, 1]), M([1, -1, 3])
    nn = bL.cross(nP); assert nn == M([-9, 2, 5])
    Q = lambda X: 9 * X[0] - 2 * X[1] - 5 * X[2] + 4
    assert Q(p0) == 0 and Q(p0 + bL) == 0 and M([9, -2, -5]).dot(nP) == 0
    assert 9 * p0[0] - 2 * p0[1] - 5 * p0[2] - 4 != 0
    assert 9 * p0[0] + 2 * p0[1] - 5 * p0[2] + 8 != 0 or M([9, 2, -5]).dot(bL) != 0
    assert M([2, -1, 4]).dot(bL) != 0  # last distractor does not contain the line
    # projection line direction is perpendicular to nP and lies in both planes
    good = M([[1, 2, 1, -9], [9, -2, -5, 4]])
    for wrong in ([9, -2, -5, -4], [9, 2, -5, 8], [2, -1, 4, -15]):
        assert M.vstack(good, M([wrong])).rank() == 3  # not a plane through the projection line
    proj_dir = nP.cross(M([9, -2, -5]))
    assert proj_dir.dot(nP) == 0

    # q21
    eq(sd(M([0, 0, 0]), M([2, -3, 1]), M([2, 1, -2]), M([3, -5, 2])), 1 / sp.sqrt(3), "q21")

    # q22: statement 1 by example, statement 2 disproved by the q4 example (sin, not cos)
    bb, nv = M([1, 1, 2]), M([2, -1, 1])
    assert sp.cos(sp.pi / 6) != sin_angle(bb, nv)
    assert M([2, 4, 6]).cross(M([1, 2, 3])) == M([0, 0, 0])

    # q23: 1 false (x-axis vs line x=0,z=1 skew); 3 false (distinct parallel lines)
    eq(sd(M([0, 0, 0]), M([1, 0, 0]), M([0, 0, 1]), M([0, 1, 0])), 1, "q23 skew")
    assert M.hstack(M([0, 1, 0]), M([1, 0, 0]), M([1, 0, 0])).det() == 0

    # q24
    bL, pL = M([2, -1, 2]), M([1, 2, 3])
    assert bL.cross(M([2, -1, 2])) == M([0, 0, 0])
    assert bL.dot(M([1, 2, 0])) == 0 and pL[0] + 2 * pL[1] == 5
    eq(sin_angle(bL, M([1, 1, 1])), 1 / sp.sqrt(3), "q24 D")

    # q25
    eq(sd(M([0, 0, 0]), M([1, 0, 0]), M([0, 0, 0]), M([0, 1, 0])), 0, "q25 A")
    eq(sd(M([0, 0, 0]), M([1, 0, 0]), M([0, 0, 2]), M([0, 1, 0])), 2, "q25 B")
    eq(sd(M([0, 0, 0]), M([1, 2, 2]), M([1, 0, -1]), M([2, -2, 1])), sp.Rational(4, 3), "q25 C")
    eq(par_dist(M([0, 0, 0]), M([1, 0, 0]), M([1, 1, 0])), 1 / sp.sqrt(2), "q25 D")

    # q26
    assert M([1, 2, 3]).cross(M([2, 4, 6])) == M([0, 0, 0])

    # q27
    assert M([[1, 2, 2], [2, 3, 4], [3, 4, 5]]).det() == 1

    # q28
    assert M([1, 1, -2]).dot(M([1, 1, 1])) == 0 and 2 + 3 + 4 == 9

    # q29
    assert M([[3, 7, 11], [3, 5, 7], [1, 3, 5]]).det() == 0
    sol = sp.solve(list(M([-1, -3, -5]) + t * M([3, 5, 7]) - M([2, 4, 6]) - s * M([1, 3, 5])), [t, s])
    assert (M([-1, -3, -5]) + t * M([3, 5, 7])).subs(sol) == M([sp.Rational(1, 2), -sp.Rational(1, 2), -sp.Rational(3, 2)])
    assert M([3, 5, 7]).cross(M([1, 3, 5])) != M([0, 0, 0])

    # q30
    assert image_plane(M([0, 0, 0]), M([1, 1, 1]), -3) == M([2, 2, 2])


T.write(check)
