import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from qlib import Topic, eq

T = Topic("math.geometry.quadrics", exams=["slst-1112"])
GEN = r"$ax^2 + by^2 + cz^2 + 2fyz + 2gzx + 2hxy + 2ux + 2vy + 2wz + d = 0$"

# 1
T.single(1, ["standard-surfaces"],
    r"The surface $\dfrac{x^2}{4} + \dfrac{y^2}{9} - \dfrac{z^2}{16} = 1$ is",
    [r"a hyperboloid of one sheet", r"a hyperboloid of two sheets", r"an elliptic cone", r"an elliptic paraboloid"],
    r"""Count the positive squares on the left of $\ldots = 1$: there are **two** ($x^2$ and $y^2$), so it is a **hyperboloid of one sheet**.

- One positive square would give two sheets.
- A cone needs $0$ on the right.
- A paraboloid has a **linear** term in one variable.

Check: every section $z = k$ is the real ellipse $\frac{x^2}{4} + \frac{y^2}{9} = 1 + \frac{k^2}{16}$, so the surface is connected.""")

# 2
T.single(1, ["standard-surfaces", "non-central"],
    r"The surface $z = x^2 - y^2$ is",
    [r"a hyperbolic paraboloid", r"an elliptic paraboloid", r"a hyperbolic cylinder", r"a hyperboloid of one sheet"],
    r"""It has the form $\frac{x^2}{a^2} - \frac{y^2}{b^2} = \frac{2z}{c}$: two squares of **opposite** sign, equal to a linear term in the third variable. That is a **hyperbolic paraboloid** (saddle).

- An elliptic paraboloid needs both squares of the same sign.
- A cylinder would have a variable missing.
- A hyperboloid has all three squares and a constant.

The sections $z = k$ are hyperbolas, and the sections $x = k$ are parabolas.""")

# 3
T.single(1, ["general-equation"],
    r"The symmetric matrix $A$ of the quadratic part of $x^2 - 2y^2 + 3z^2 - 4yz + 6zx - 2xy + 4x - 6 = 0$ is",
    [r"$\begin{pmatrix} 1 & -1 & 3\\ -1 & -2 & -2\\ 3 & -2 & 3\end{pmatrix}$",
     r"$\begin{pmatrix} 1 & -2 & 6\\ -2 & -2 & -4\\ 6 & -4 & 3\end{pmatrix}$",
     r"$\begin{pmatrix} 1 & -1 & -2\\ -1 & -2 & 3\\ -2 & 3 & 3\end{pmatrix}$",
     r"$\begin{pmatrix} 1 & 1 & 3\\ 1 & -2 & -2\\ 3 & -2 & 3\end{pmatrix}$"],
    r"""Diagonal: $a = 1$, $b = -2$, $c = 3$. Halve each cross coefficient: $h = -1$ (from $-2xy$), $f = -2$ (from $-4yz$), $g = 3$ (from $6zx$). With $A = \begin{pmatrix} a & h & g\\ h & b & f\\ g & f & c\end{pmatrix}$:
$$A = \begin{pmatrix} 1 & -1 & 3\\ -1 & -2 & -2\\ 3 & -2 & 3\end{pmatrix}.$$

- The second matrix forgets to halve.
- The third puts $f$ and $g$ in each other's places: $g$ belongs at positions $(1,3)$ and $(3,1)$.
- The last has the sign of $h$ wrong: the term is $-2xy$, so $h = -1$.

The linear terms and the constant go only into the $4\times4$ matrix $E$.""")

# 4
T.single(1, ["invariants"],
    r"The axes are rotated about the origin, and " + GEN + r" becomes $a'X^2 + b'Y^2 + c'Z^2 + \cdots = 0$. Which of the following is always equal to its new value?",
    [r"$a + b + c$", r"$a + b$", r"$abc$", r"$f + g + h$"],
    r"""Under a rotation $A' = P^TAP$ with $P$ orthogonal, so $A'$ has the same eigenvalues as $A$. Hence the **trace**
$$a + b + c = \lambda_1 + \lambda_2 + \lambda_3$$
is invariant. (So are $J = bc + ca + ab - f^2 - g^2 - h^2$ and $D = \det A$.)

$a + b$ is invariant only for rotations about the $z$-axis. $abc$ is not $\det A$ unless $f = g = h = 0$. Example: $2xy$ (with $abc = 0$) becomes $X^2 - Y^2$ after a $45^\circ$ rotation about the $z$-axis, but $a + b + c = 0$ stays $0$.""")

# 5
T.single(1, ["standard-surfaces"],
    r"In three-dimensional space, the equation $4x^2 + 9y^2 = 36$ represents",
    [r"an elliptic cylinder with generators parallel to the $z$-axis", r"an ellipse in the plane $z = 0$", r"an ellipsoid", r"an elliptic cone with vertex at the origin"],
    r"""$z$ is absent, so if $(x, y, 0)$ satisfies the equation, so does $(x, y, z)$ for every $z$. The surface is the ellipse $\frac{x^2}{9} + \frac{y^2}{4} = 1$ moved along the $z$-axis: an **elliptic cylinder**.

An ellipse in space needs **two** equations, for example $4x^2 + 9y^2 = 36,\ z = 0$. An ellipsoid needs a $z^2$ term. A cone needs a homogeneous equation (constant $0$).""")

# 6
T.single(1, ["invariants", "standard-surfaces"],
    r"For the ellipsoid $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} + \dfrac{z^2}{c^2} = 1$, the value of the discriminant $\Delta$ (the determinant of the $4\times4$ matrix of the equation written as $\ldots - 1 = 0$) is",
    [r"$-\dfrac{1}{a^2b^2c^2}$", r"$\dfrac{1}{a^2b^2c^2}$", r"$0$", r"$-a^2b^2c^2$"],
    r"""Write it as $\frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} - 1 = 0$. There are no cross or linear terms, so
$$E = \operatorname{diag}\left(\tfrac{1}{a^2}, \tfrac{1}{b^2}, \tfrac{1}{c^2}, -1\right), \qquad \Delta = -\frac{1}{a^2b^2c^2}.$$

$0$ would mean a degenerate quadric (cone, cylinder, planes). The positive value forgets $d = -1$. $-a^2b^2c^2$ uses the semi-axes instead of the coefficients.

The sign agrees with the rule that a real ellipsoid has $\Delta < 0$.""")

# 7
T.single(2, ["invariants"],
    r"For the quadric $3x^2 + 3y^2 + 2z^2 + 2xy = 4$, the invariant $J = bc + ca + ab - f^2 - g^2 - h^2$ equals",
    [r"$20$", r"$21$", r"$17$", r"$16$"],
    r"""$a = 3$, $b = 3$, $c = 2$, $f = g = 0$, and $h = 1$ (half of $2$):
$$J = 3\cdot2 + 2\cdot3 + 3\cdot3 - 1 = 20.$$

- $21$ forgets $h^2$.
- $17$ uses $h = 2$, without halving.
- $16$ is $D = \det A$.

Check: the eigenvalues are $4, 2, 2$, and $4\cdot2 + 2\cdot2 + 2\cdot4 = 20$.""")

# 8
T.single(2, ["central-reduction", "invariants"],
    r"By a rotation of axes, $3x^2 + 3y^2 + 2z^2 + 2xy = 4$ reduces to",
    [r"$4X^2 + 2Y^2 + 2Z^2 = 4$", r"$5X^2 + Y^2 + 2Z^2 = 4$", r"$4X^2 - 2Y^2 + 2Z^2 = 4$", r"$3X^2 + 3Y^2 + 2Z^2 = 4$"],
    r"""$A = \begin{pmatrix} 3 & 1 & 0\\ 1 & 3 & 0\\ 0 & 0 & 2\end{pmatrix}$. The $xy$-block has eigenvalues $3 \pm 1 = 4, 2$, and $z$ gives $2$. So
$$4X^2 + 2Y^2 + 2Z^2 = 4 \iff X^2 + \frac{Y^2}{2} + \frac{Z^2}{2} = 1,$$
a spheroid (an ellipsoid of revolution).

- $5, 1, 2$ come from the unhalved block $\begin{pmatrix} 3 & 2\\ 2 & 3\end{pmatrix}$. It has the right trace $8$, but its product is $10 \ne D = 16$.
- The form with $-2Y^2$ fails the trace test ($4 \ne 8$).
- The last option ignores the $xy$-term.""")

# 9
T.single(2, ["central-reduction"],
    r"The centre of the quadric $2x^2 + 2y^2 + z^2 + 2xy - 2x + 2y - 4z + 3 = 0$ is",
    [r"$(1, -1, 2)$", r"$(-1, 1, -2)$", r"$(2, -2, 4)$", r"$\left(\tfrac12, -\tfrac12, 1\right)$"],
    r"""The centre solves $\tfrac12F_x = \tfrac12F_y = \tfrac12F_z = 0$:
$$2x + y - 1 = 0, \qquad x + 2y + 1 = 0, \qquad z - 2 = 0.$$
The first two give $x = 1$, $y = -1$, and the third gives $z = 2$. The centre is $(1, -1, 2)$.

- $(-1, 1, -2)$ has every sign reversed: it solves $AX_0 = L$ instead of $AX_0 = -L$.
- $(2, -2, 4)$ forgets to halve the linear coefficients: it takes $(u, v, w) = (-2, 2, -4)$, i.e. solves $AX_0 = -2L$.
- The last option halves the answer.""")

# 10
T.single(3, ["central-reduction"],
    r"The quadric $2x^2 + 2y^2 + z^2 + 2xy - 2x + 2y - 4z + 3 = 0$ (centre $(1, -1, 2)$), referred to its principal axes through the centre, becomes",
    [r"$3X^2 + Y^2 + Z^2 = 3$", r"$3X^2 + Y^2 + Z^2 = 9$", r"$3X^2 + Y^2 + Z^2 + 3 = 0$", r"$2X^2 + 2Y^2 + Z^2 = 3$"],
    r"""**Constant.** Here $L = (u, v, w) = (-1, 1, -2)$ and $d = 3$, so
$$d' = ux_0 + vy_0 + wz_0 + d = -1 - 1 - 4 + 3 = -3.$$
Check: $D = 3$, $\Delta = -9$, and $\Delta/D = -3$.

**Eigenvalues.** The $xy$-block $\begin{pmatrix} 2 & 1\\ 1 & 2\end{pmatrix}$ gives $3, 1$, and $z$ gives $1$.

So $3X^2 + Y^2 + Z^2 - 3 = 0$, i.e. $X^2 + \frac{Y^2}{3} + \frac{Z^2}{3} = 1$: a spheroid.

- $= 9$ uses $\Delta$ instead of $\Delta/D$.
- $+3 = 0$ has the sign of $d'$ reversed (it has no real points).
- The last option ignores the $xy$-term.""")

# 11
T.single(2, ["classification", "central-reduction"],
    r"The surface $x^2 + 4yz = 4$ is",
    [r"a hyperboloid of one sheet", r"a hyperboloid of two sheets", r"a hyperbolic paraboloid", r"a hyperbolic cylinder"],
    r"""$A = \begin{pmatrix} 1 & 0 & 0\\ 0 & 0 & 2\\ 0 & 2 & 0\end{pmatrix}$, with eigenvalues $1$ and $\pm 2$ (the $yz$-block has eigenvalues $\pm f = \pm 2$). There are no linear terms, so the centre is $O$, and
$$X^2 + 2Y^2 - 2Z^2 = 4.$$
Two positive squares, so it is a **hyperboloid of one sheet**.

- Two sheets would need two negative eigenvalues.
- There is no linear term and $D = -4 \ne 0$, so it is not a paraboloid or a cylinder.

Check: $\Delta = D\cdot(-4) = 16 > 0$, as expected for a hyperboloid of one sheet.""")

# 12
T.single(1, ["tangent-planes"],
    r"The tangent plane to $x^2 + 2y^2 - z^2 = 2$ at $(1, 1, 1)$ is",
    [r"$x + 2y - z = 2$", r"$x + 2y - z = 0$", r"$x + 2y + z = 4$", r"$2x + 4y - 2z = 2$"],
    r"""Replace $x^2 \to x x_1$, and so on:
$$x\cdot1 + 2y\cdot1 - z\cdot1 = 2 \;\Rightarrow\; x + 2y - z = 2.$$
Check: $(1, 1, 1)$ lies on it ($1 + 2 - 1 = 2$).

- $x + 2y - z = 0$ passes through the centre, not through $P$.
- $x + 2y + z = 4$ has a sign slip in the $z^2$ term.
- $2x + 4y - 2z = 2$ uses the gradient but keeps the right-hand side $2$. It misses $P$, because $2 + 4 - 2 = 4 \ne 2$.""")

# 13
T.single(2, ["tangent-planes"],
    r"The plane $x + y + z = k$ ($k > 0$) touches the ellipsoid $\dfrac{x^2}{4} + \dfrac{y^2}{9} + \dfrac{z^2}{12} = 1$ when $k$ equals",
    [r"$5$", r"$\dfrac23$", r"$25$", r"$\sqrt{13}$"],
    r"""For $\frac{x^2}{A^2} + \frac{y^2}{B^2} + \frac{z^2}{C^2} = 1$, the plane $lx + my + nz = p$ touches when $A^2l^2 + B^2m^2 + C^2n^2 = p^2$:
$$k^2 = 4 + 9 + 12 = 25 \;\Rightarrow\; k = 5.$$
The point of contact is $\left(\frac{4}{5}, \frac{9}{5}, \frac{12}{5}\right)$.

- $\frac23 = \sqrt{\frac14 + \frac19 + \frac1{12}}$ divides by the squares instead of multiplying.
- $25$ is $k^2$.
- $\sqrt{13}$ drops the $z$-term.""")

# 14
T.single(3, ["tangent-planes"],
    r"The point $(1, 1, 1)$ lies on $x^2 + 2y^2 - z^2 + 4xy - 2x + 2z - 6 = 0$. The tangent plane there is",
    [r"$x + 2y = 3$", r"$3x + 4y - z = 6$", r"$x + 2y = 0$", r"$2x + y = 3$"],
    r"""$\tfrac12F_x = x + 2y - 1$, $\tfrac12F_y = 2x + 2y$, $\tfrac12F_z = -z + 1$. At $(1, 1, 1)$ these are $2, 4, 0$. So the tangent plane is
$$2(x - 1) + 4(y - 1) + 0 = 0 \;\Rightarrow\; x + 2y = 3.$$
The substitution rule gives the same result: $x + 2y - z + 2(x + y) - (x + 1) + (z + 1) - 6 = 2x + 4y - 6 = 0$.

- $3x + 4y - z = 6$ uses only the quadratic part's gradient $(6, 8, -2)$ and forgets the linear terms.
- $x + 2y = 0$ does not pass through $P$.
- $2x + y = 3$ swaps the coefficients.""")

# 15
T.single(2, ["non-central"],
    r"The surface $x^2 + 2xy + y^2 - 4z = 0$ is",
    [r"a parabolic cylinder", r"an elliptic paraboloid", r"a hyperbolic paraboloid", r"a cone"],
    r"""The quadratic part is a perfect square: $(x + y)^2 = 4z$. So $A$ has rank $1$ (eigenvalues $2, 0, 0$).

Rotate so that $X = \frac{x + y}{\sqrt2}$. Then $2X^2 = 4z$: a parabola in the $Xz$-plane, extended along the direction $(1, -1, 0)$. This is a **parabolic cylinder**.

- A paraboloid needs rank $A = 2$.
- A cone needs $D \ne 0$ (or at least a homogeneous equation). The term $-4z$ makes this equation non-homogeneous.""")

# 16
T.single(3, ["non-central", "classification"],
    r"The quadric $x^2 + y^2 + z^2 + 2xy + 2x - 2y = 0$, referred to suitable rectangular axes, becomes",
    [r"$2X^2 + Y^2 = 2\sqrt2\,Z$", r"$2X^2 + Y^2 = 4Z$", r"$2X^2 - Y^2 = 2\sqrt2\,Z$", r"$2X^2 + Y^2 = 2Z$"],
    r"""$A = \begin{pmatrix} 1 & 1 & 0\\ 1 & 1 & 0\\ 0 & 0 & 1\end{pmatrix}$ has eigenvalues $2, 1, 0$, so $D = 0$. The unit eigenvector for $0$ is $n = \frac{1}{\sqrt2}(1, -1, 0)$.

$L = (1, -1, 0)$, so $p = L\cdot n = \sqrt2$. Check: $\Delta = -4$, and
$$p^2 = -\frac{\Delta}{\lambda_1\lambda_2} = -\frac{-4}{2} = 2.$$
Hence $2X^2 + Y^2 + 2\sqrt2\,Z' = 0$, i.e. (reversing $Z$) $2X^2 + Y^2 = 2\sqrt2\,Z$: an **elliptic paraboloid**.

- $4Z$ uses the non-unit vector $(1, -1, 0)$, so $p = 2$.
- The minus sign contradicts both nonzero eigenvalues being positive.
- $2Z$ takes $p = 1$.""")

# 17
T.single(2, ["classification"],
    r"The equation $x^2 + y^2 - z^2 - 2x + 4y + 2z + 4 = 0$ represents",
    [r"a cone with vertex $(1, -2, 1)$", r"a hyperboloid of one sheet with centre $(1, -2, 1)$", r"a hyperboloid of two sheets with centre $(1, -2, 1)$", r"a cone with vertex $(-1, 2, -1)$"],
    r"""Complete the squares:
$$(x - 1)^2 + (y + 2)^2 - (z - 1)^2 = -4 + 1 + 4 - 1 = 0.$$
The constant after the shift is $0$, i.e. $\Delta = 0$ with $D = -1 \ne 0$. So it is a **cone** with vertex at the centre $(1, -2, 1)$.

- Hyperboloids need a nonzero constant ($+1$ would give one sheet, $-1$ two sheets).
- $(-1, 2, -1)$ has the sign of the shift reversed.""")

# 18
T.single(2, ["non-central", "classification"],
    r"The equation $x^2 + y^2 + z^2 + 2xy + 2yz + 2zx = 1$ represents",
    [r"a pair of parallel planes", r"a pair of intersecting planes", r"a sphere", r"a parabolic cylinder"],
    r"""The left side is $(x + y + z)^2$, so the equation is $x + y + z = \pm 1$: **two parallel planes**.

In terms of ranks: $A$ is the all-ones matrix, with rank $1$, and $E$ has rank $2$.

- Intersecting planes need rank $A = 2$.
- A sphere has no cross terms.
- A parabolic cylinder (rank $E = 3$) needs a linear term that is not a multiple of $x + y + z$.""")

# 19
T.single(3, ["classification", "central-reduction"],
    r"The equation $2xy + 2yz + 2zx - 4z + k = 0$ represents a cone if $k$ equals",
    [r"$-2$", r"$2$", r"$0$", r"$-4$"],
    r"""$A = \begin{pmatrix} 0 & 1 & 1\\ 1 & 0 & 1\\ 1 & 1 & 0\end{pmatrix}$, with $D = 2 \ne 0$, so there is a unique centre. Solve $AX_0 = -L = (0, 0, 2)$:
$$y + z = 0, \qquad x + z = 0, \qquad x + y = 2.$$
This gives $(1, 1, -1)$. The constant after the shift is
$$d' = wz_0 + k = (-2)(-1) + k = k + 2.$$
It is a cone (with vertex $(1, 1, -1)$) exactly when $d' = 0$, i.e. $\Delta = 0$: $k = -2$.

- $k = 2$ has the sign of $wz_0$ reversed.
- $k = 0$ would be right only if the vertex were the origin.
- $k = -4$ forgets to halve $-4z$.""")

# 20
T.single(1, ["tangent-planes"],
    r"The plane $lx + my + nz = p$ touches the central conicoid $ax^2 + by^2 + cz^2 = 1$ if and only if",
    [r"$\dfrac{l^2}{a} + \dfrac{m^2}{b} + \dfrac{n^2}{c} = p^2$", r"$al^2 + bm^2 + cn^2 = p^2$", r"$\dfrac{l^2}{a} + \dfrac{m^2}{b} + \dfrac{n^2}{c} = p$", r"$al^2 + bm^2 + cn^2 = \dfrac{1}{p^2}$"],
    r"""The tangent plane at $(\alpha, \beta, \gamma)$ is $a\alpha x + b\beta y + c\gamma z = 1$. Matching it with $lx + my + nz = p$ gives $\alpha = \frac{l}{ap}$, $\beta = \frac{m}{bp}$, $\gamma = \frac{n}{cp}$. Substituting into $a\alpha^2 + b\beta^2 + c\gamma^2 = 1$:
$$\frac{l^2}{a} + \frac{m^2}{b} + \frac{n^2}{c} = p^2.$$

$al^2 + \cdots = p^2$ is the tempting slip. It is the right form only when written with semi-axes ($a = 1/A^2$). The other two options are not homogeneous of degree $2$ in $(l, m, n, p)$, as a tangency condition must be.""")

# 21
T.single(3, ["central-reduction"],
    r"The longest axis of the ellipsoid $2x^2 + 5y^2 + 3z^2 + 4xy = 6$ lies along the line",
    [r"$\dfrac{x}{2} = \dfrac{y}{-1}$, $z = 0$", r"$\dfrac{x}{1} = \dfrac{y}{2}$, $z = 0$", r"the $z$-axis", r"$x = y$, $z = 0$"],
    r"""$A = \begin{pmatrix} 2 & 2 & 0\\ 2 & 5 & 0\\ 0 & 0 & 3\end{pmatrix}$. The $xy$-block has $\lambda^2 - 7\lambda + 6 = 0$, so $\lambda = 1, 6$; the $z$-eigenvalue is $3$. The reduced form is
$$X^2 + 6Y^2 + 3Z^2 = 6,$$
with semi-axes $\sqrt6, 1, \sqrt2$. The longest one belongs to the **smallest** eigenvalue $\lambda = 1$. Its eigenvector solves $(2 - 1)x + 2y = 0$, giving $(2, -1, 0)$.

- $(1, 2, 0)$ is the eigenvector for $\lambda = 6$: the **shortest** axis.
- The $z$-axis carries the middle axis $\sqrt2$.
- $x = y$ is not an eigenvector, because $a \ne b$.""")

# 22
T.statements(2, ["invariants"],
    r"Consider " + GEN + r", with $A$ the matrix of its quadratic part, $D = \det A$ and $\Delta$ the determinant of its $4\times4$ matrix.",
    [r"$a + b + c$ is unchanged by any rotation of rectangular axes about the origin.",
     r"$\Delta$ is unchanged by any translation of the origin.",
     r"$D$ changes, in general, when the origin is translated."],
    [r"1 and 2 only", r"1 and 3 only", r"2 and 3 only", r"1, 2 and 3"],
    r"""1. **True.** $A' = P^TAP$, so the trace is preserved.
2. **True.** $E' = T^TET$ with $T = \begin{pmatrix} I & t\\ 0 & 1\end{pmatrix}$, and $\det T = 1$.
3. **False.** A translation $x = X + \alpha$, and so on, does not change the second-degree coefficients $a, b, c, f, g, h$. So $A$, and with it $D$, is unchanged. Only $u, v, w, d$ change.

For example, shifting $x^2 + y^2 - z^2 - 1 = 0$ to $(1, 2, 3)$ changes the linear terms, but $D = -1$ and $\Delta = 1$ both stay.""")

# 23
T.statements(3, ["central-reduction", "non-central", "standard-surfaces"],
    r"Consider the following statements about quadrics.",
    [r"If $D = \det A \ne 0$, the quadric has exactly one centre.",
     r"The elliptic paraboloid $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = \dfrac{2z}{c}$ has a unique centre.",
     r"The plane $x = k$ meets the hyperboloid $\dfrac{x^2}{a^2} - \dfrac{y^2}{b^2} - \dfrac{z^2}{c^2} = 1$ in a real curve only if $\lvert k\rvert \ge a$."],
    [r"1 and 3 only", r"1 and 2 only", r"2 and 3 only", r"1, 2 and 3"],
    r"""1. **True.** The centre solves $AX_0 = -L$, which has a unique solution when $\det A \ne 0$.
2. **False.** Here $\tfrac12F_z$ is the constant $-\frac{1}{c} \ne 0$, so the centre equations are inconsistent. A paraboloid has **no** centre ($D = 0$).
3. **True.** Putting $x = k$ gives $\frac{y^2}{b^2} + \frac{z^2}{c^2} = \frac{k^2}{a^2} - 1$. This has real points only when $\lvert k\rvert \ge a$, which is the gap between the two sheets.""")

# 24
T.match(2, ["standard-surfaces"],
    r"Match each equation ($a, b, c > 0$) with the surface it represents.",
    [r"A. $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} - \dfrac{z^2}{c^2} = 1$",
     r"B. $\dfrac{x^2}{a^2} - \dfrac{y^2}{b^2} - \dfrac{z^2}{c^2} = 1$",
     r"C. $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = \dfrac{2z}{c}$",
     r"D. $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} - \dfrac{z^2}{c^2} = 0$"],
    [r"1. elliptic paraboloid", r"2. hyperboloid of two sheets", r"3. elliptic cone", r"4. hyperboloid of one sheet"],
    [r"A-4, B-2, C-1, D-3", r"A-2, B-4, C-1, D-3", r"A-4, B-2, C-3, D-1", r"A-3, B-2, C-1, D-4"],
    r"""- **A:** two positive squares $= 1$, so a hyperboloid of **one** sheet (4).
- **B:** one positive square $= 1$, so **two** sheets (2).
- **C:** squares equal to a linear term, both the same sign, so an elliptic paraboloid (1).
- **D:** homogeneous, so a cone with vertex $O$ (3).

The common swap is A with B: count the **positive** squares, not the negative ones.""")

# 25
T.match(3, ["classification"],
    r"For a real quadric, $A$ is the $3\times3$ matrix of the quadratic part and $E$ the $4\times4$ matrix of the whole equation. Match the ranks with the type of quadric.",
    [r"A. $\operatorname{rank}A = 3$, $\operatorname{rank}E = 4$",
     r"B. $\operatorname{rank}A = 3$, $\operatorname{rank}E = 3$",
     r"C. $\operatorname{rank}A = 2$, $\operatorname{rank}E = 4$",
     r"D. $\operatorname{rank}A = 1$, $\operatorname{rank}E = 3$"],
    [r"1. parabolic cylinder", r"2. paraboloid", r"3. cone", r"4. ellipsoid or hyperboloid"],
    [r"A-4, B-3, C-2, D-1", r"A-4, B-2, C-3, D-1", r"A-3, B-4, C-2, D-1", r"A-4, B-3, C-1, D-2"],
    r"""- **A:** $D \ne 0$ (unique centre) and $\Delta \ne 0$ (non-degenerate): a central conicoid, i.e. an ellipsoid or hyperboloid (4).
- **B:** $D \ne 0$ but $\Delta = 0$: a cone with vertex at the centre (3).
- **C:** $D = 0$ with rank $A = 2$, and $\Delta \ne 0$: a paraboloid, e.g. $x^2 + y^2 = 2z$ (2).
- **D:** a perfect-square quadratic part with an independent linear term, e.g. $x^2 = 2z$: a parabolic cylinder (1).

Swapping B and C confuses "no centre" ($D = 0$) with "degenerate" ($\Delta = 0$).""")

# 26
T.assertion_reason(2, ["classification", "central-reduction"],
    r"The surface $2yz + 2zx + 2xy = 1$ is a hyperboloid of two sheets.",
    r"The matrix of $2yz + 2zx + 2xy$ has eigenvalues $2, -1, -1$, and the centre is the origin, so the equation reduces to $2X^2 - Y^2 - Z^2 = 1$.",
    0,
    r"""$A = J - I$, where $J$ is the all-ones matrix. $J$ has eigenvalues $3, 0, 0$, so $A$ has $2, -1, -1$. There are no linear terms, so the centre is $O$ and the constant stays $-1$:
$$2X^2 - Y^2 - Z^2 = 1.$$
Exactly one positive square gives two sheets. **Both are true, and R is exactly the reduction that proves A.**

(It is a surface of revolution about the line $x = y = z$.)""")

# 27
T.assertion_reason(2, ["non-central", "classification"],
    r"Every quadric with $D = \det A = 0$ is a paraboloid.",
    r"If $D = 0$, the quadric does not have a unique centre.",
    3,
    r"""**R is true:** the centre equations $AX_0 = -L$ have no solution, or infinitely many, when $\det A = 0$.

**A is false:** $D = 0$ also covers cylinders and pairs of planes. For example, the cylinder $x^2 + y^2 = 1$ has $D = 0$ and a whole line of centres (the $z$-axis). It is a paraboloid only when, in addition, $\Delta \ne 0$ with rank $A = 2$.""")

# 28
T.assertion_reason(2, ["tangent-planes"],
    r"The tangent plane to $x^2 + 2y^2 + 3z^2 = 6$ at $(1, 1, 1)$ is $x + 2y + 3z = 6$.",
    r"The normal to a central conicoid at any point of it passes through the centre.",
    2,
    r"""**A is true:** by the substitution rule $x^2 \to xx_1$, the tangent plane is $x + 2y + 3z = 6$. Also $1 + 2 + 3 = 6$, so $P$ is on it.

**R is false:** the normal at $(1, 1, 1)$ has direction $(1, 2, 3)$. The line from the centre $O$ to $P$ has direction $(1, 1, 1)$. These are not parallel, so the normal misses $O$. Normals pass through the centre for every point only on a sphere ($a = b = c$).""")

# 29
T.assertion_reason(2, ["non-central", "central-reduction"],
    r"The hyperbolic paraboloid $z = xy$ has no centre.",
    r"The hyperbolic paraboloid contains two families of straight lines.",
    1,
    r"""**A is true:** with $F = xy - z$, the centre equations are $\tfrac12F_x = \frac{y}{2} = 0$, $\tfrac12F_y = \frac{x}{2} = 0$ and $\tfrac12F_z = -\tfrac12 = 0$. The last is impossible, so there is no centre.

**R is true:** for example, the lines $x = \lambda$, $z = \lambda y$ lie on it for every $\lambda$, and so do $y = \mu$, $z = \mu x$.

But being ruled has nothing to do with having a centre: the hyperboloid of one sheet is ruled **and** central. So **both are true, but R does not explain A**.""")

# 30
T.assertion_reason(3, ["central-reduction", "invariants"],
    r"The quadric $3x^2 + 3y^2 + 2z^2 + 2xy = 4$ is a surface of revolution.",
    r"If the discriminating cubic of a central quadric $\lambda_1X^2 + \lambda_2Y^2 + \lambda_3Z^2 = K$ has $\lambda_2 = \lambda_3$, the quadric is a surface of revolution about the $X$-axis (the principal axis of $\lambda_1$).",
    0,
    r"""The cubic is $\lambda^3 - 8\lambda^2 + 20\lambda - 16 = (\lambda - 4)(\lambda - 2)^2$, so the reduced form is $4X^2 + 2(Y^2 + Z^2) = 4$.

**R is true:** $\lambda_1X^2 + \lambda_2(Y^2 + Z^2) = K$ depends on $Y, Z$ only through $Y^2 + Z^2$, so it is unchanged by rotations about the $X$-axis.

**A is true for exactly that reason:** the repeated root $2$ makes the surface a spheroid about the line $x = y$, $z = 0$ (the eigenvector of $\lambda = 4$). **Both are true, and R explains A.**""")


def check():
    import sympy as sp
    x, y, z, k, t = sp.symbols("x y z k t", real=True)
    S, R = sp.sqrt, sp.Rational

    def mats(F):
        P = sp.Poly(sp.expand(F), x, y, z)
        m = P.coeff_monomial
        a, b, c = m(x**2), m(y**2), m(z**2)
        f, g, h = m(y*z) / 2, m(z*x) / 2, m(x*y) / 2
        u, v, w, d = m(x) / 2, m(y) / 2, m(z) / 2, m(1)
        A = sp.Matrix([[a, h, g], [h, b, f], [g, f, c]])
        E = sp.Matrix([[a, h, g, u], [h, b, f, v], [g, f, c, w], [u, v, w, d]])
        return A, E

    def eigs(F):
        return sorted(mats(F)[0].eigenvals(multiple=True))

    def centre(F):
        sol = sp.solve([sp.diff(F, s) for s in (x, y, z)], [x, y, z], dict=True)
        return sol

    def grad(F, P):
        return [sp.diff(F, s).subs(dict(zip((x, y, z), P))) for s in (x, y, z)]

    def same_plane(p1, p2):
        # p1, p2 are expressions = 0; proportional?
        c1 = [sp.Poly(p1, x, y, z).coeff_monomial(mm) for mm in (x, y, z, 1)]
        c2 = [sp.Poly(p2, x, y, z).coeff_monomial(mm) for mm in (x, y, z, 1)]
        return sp.Matrix([c1, c2]).rank() == 1

    def classify(F):
        A, E = mats(F)
        rA, rE = A.rank(), E.rank()
        if rA == 3:
            D, De = A.det(), E.det()
            K = -De / D
            lam = A.eigenvals(multiple=True)
            if K == 0:
                return "cone" if len({sp.sign(l) for l in lam}) > 1 else "point"
            same = sum(1 for l in lam if sp.sign(l) == sp.sign(K))
            return {3: "ellipsoid", 2: "hyp1", 1: "hyp2", 0: "imaginary"}[same]
        if rA == 2:
            nz = [l for l in A.eigenvals(multiple=True) if l != 0]
            if rE == 4:
                return "ell-parab" if nz[0] * nz[1] > 0 else "hyp-parab"
            if rE == 3:
                return "cylinder"
            return "planes-int" if nz[0] * nz[1] < 0 else "line"
        if rA == 1:
            return {3: "parab-cyl", 2: "planes-par", 1: "planes-coinc"}[rE]

    # q1
    F1 = x**2 / 4 + y**2 / 9 - z**2 / 16 - 1
    assert classify(F1) == "hyp1", "q1"
    eq(mats(F1)[1].det(), R(1, 4 * 9 * 16), "q1 Delta>0")
    # q2
    assert classify(z - x**2 + y**2) == "hyp-parab", "q2"
    # q3
    A3, E3 = mats(x**2 - 2*y**2 + 3*z**2 - 4*y*z + 6*z*x - 2*x*y + 4*x - 6)
    assert A3 == sp.Matrix([[1, -1, 3], [-1, -2, -2], [3, -2, 3]]), "q3"
    assert A3 != sp.Matrix([[1, -1, -2], [-1, -2, 3], [-2, 3, 3]]) and A3 != sp.Matrix([[1, 1, 3], [1, -2, -2], [3, -2, 3]]), "q3 distractor"
    eq(E3[0, 3], 2, "q3 u"); eq(E3[3, 3], -6, "q3 d")
    # q4: rotation invariance of trace; abc and a+b not invariant
    th = sp.Symbol("th", real=True)
    Rz = sp.Matrix([[sp.cos(th), -sp.sin(th), 0], [sp.sin(th), sp.cos(th), 0], [0, 0, 1]])
    Rx = sp.Matrix([[1, 0, 0], [0, sp.cos(th), -sp.sin(th)], [0, sp.sin(th), sp.cos(th)]])
    Ag = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f"m{min(i, j)}{max(i, j)}"))
    eq(sp.simplify((Rz.T * Ag * Rz).trace() - Ag.trace()), 0, "q4 trace z")
    eq(sp.simplify((Rx.T * Ag * Rx).trace() - Ag.trace()), 0, "q4 trace x")
    A4 = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]])  # 2xy
    A4r = (Rz.T * A4 * Rz).subs(th, sp.pi / 4)
    assert A4r[:2, :2] == sp.Matrix([[1, 0], [0, -1]]), "q4 2xy -> X^2 - Y^2"
    A4b = sp.Matrix([[1, 1, 0], [1, 1, 0], [0, 0, 1]])
    A4br = (Rz.T * A4b * Rz).subs(th, sp.pi / 4)
    assert sp.simplify(A4br[0, 0] * A4br[1, 1] * A4br[2, 2] - 1) != 0, "q4 abc not invariant"
    A4d = sp.diag(1, 2, 3)
    A4cr = (Rx.T * A4d * Rx).subs(th, sp.pi / 4)
    assert sp.simplify(A4cr[0, 0] + A4cr[1, 1] - 3) != 0, "q4 a+b not invariant"
    assert sp.simplify(A4cr[0, 1] + A4cr[0, 2] + A4cr[1, 2]) != 0, "q4 f+g+h not invariant"
    # q5
    assert classify(4*x**2 + 9*y**2 - 36) == "cylinder", "q5"
    # q6
    a, b, c = sp.symbols("a b c", positive=True)
    E6 = sp.diag(1 / a**2, 1 / b**2, 1 / c**2, -1)
    eq(E6.det(), -1 / (a**2 * b**2 * c**2), "q6")
    # q7, q8, q30
    F7 = 3*x**2 + 3*y**2 + 2*z**2 + 2*x*y - 4
    A7, E7 = mats(F7)
    J7 = sum(A7.extract([i, j], [i, j]).det() for i, j in [(0, 1), (1, 2), (0, 2)])
    eq(J7, 20, "q7")
    eq(A7.det(), 16, "q7 D distractor")
    assert eigs(F7) == [2, 2, 4], "q8"
    eq(sp.Matrix([[3, 2], [2, 3]]).det() * 2 - 16, -6, "q8 distractor product 10 != 16")
    lam = sp.Symbol("lam")
    eq(sp.expand(A7.charpoly(lam).as_expr() - (lam - 4) * (lam - 2)**2), 0, "q30 cubic")
    assert classify(F7) == "ellipsoid", "q8 class"
    # q9, q10
    F9 = 2*x**2 + 2*y**2 + z**2 + 2*x*y - 2*x + 2*y - 4*z + 3
    c9 = centre(F9)
    assert c9 == [{x: 1, y: -1, z: 2}], "q9"
    A9_ = mats(F9)[0]
    assert A9_.solve(-2 * mats(F9)[1][:3, 3]) == sp.Matrix([2, -2, 4]), "q9 distractor"
    A9, E9 = mats(F9)
    eq(F9.subs({x: 1, y: -1, z: 2}), -3, "q10 d'")
    eq(E9.det() / A9.det(), -3, "q10 Delta/D")
    eq(E9.det(), -9, "q10 Delta")
    assert eigs(F9) == [1, 1, 3], "q10 eig"
    assert classify(F9) == "ellipsoid", "q10 class"
    # q11
    F11 = x**2 + 4*y*z - 4
    assert eigs(F11) == [-2, 1, 2], "q11"
    assert classify(F11) == "hyp1", "q11 class"
    eq(mats(F11)[1].det(), 16, "q11 Delta")
    # q12
    F12 = x**2 + 2*y**2 - z**2 - 2
    eq(F12.subs({x: 1, y: 1, z: 1}), 0, "q12 on")
    g12 = grad(F12, (1, 1, 1))
    tp12 = g12[0] * (x - 1) + g12[1] * (y - 1) + g12[2] * (z - 1)
    assert same_plane(tp12, x + 2*y - z - 2), "q12"
    assert not same_plane(tp12, 2*x + 4*y - 2*z - 2), "q12 d"
    # q13: tangency via discriminant of substitution
    F13 = x**2 / 4 + y**2 / 9 + z**2 / 12 - 1
    eq(sp.sqrt(4 + 9 + 12), 5, "q13")
    # independent: plane x+y+z=5 meets ellipsoid in exactly one point (min of F on plane is 0)
    sol = sp.solve([sp.diff(F13, x) - t, sp.diff(F13, y) - t, sp.diff(F13, z) - t, x + y + z - 5], [x, y, z, t], dict=True)
    eq(F13.subs(sol[0]), 0, "q13 contact")
    for s_, v_ in zip((x, y, z), (R(4, 5), R(9, 5), R(12, 5))):
        eq(sol[0][s_], v_, "q13 point")
    eq(sp.sqrt(R(1, 4) + R(1, 9) + R(1, 12)), R(2, 3), "q13 distractor")
    # q14
    F14 = x**2 + 2*y**2 - z**2 + 4*x*y - 2*x + 2*z - 6
    eq(F14.subs({x: 1, y: 1, z: 1}), 0, "q14 on")
    g14 = grad(F14, (1, 1, 1))
    tp14 = g14[0] * (x - 1) + g14[1] * (y - 1) + g14[2] * (z - 1)
    assert same_plane(tp14, x + 2*y - 3), "q14"
    Fq = x**2 + 2*y**2 - z**2 + 4*x*y
    gq = grad(Fq, (1, 1, 1))
    assert same_plane(gq[0] * (x - 1) + gq[1] * (y - 1) + gq[2] * (z - 1), 3*x + 4*y - z - 6), "q14 distractor"
    # q15
    F15 = x**2 + 2*x*y + y**2 - 4*z
    assert classify(F15) == "parab-cyl", "q15"
    # q16
    F16 = x**2 + y**2 + z**2 + 2*x*y + 2*x - 2*y
    A16, E16 = mats(F16)
    assert eigs(F16) == [0, 1, 2], "q16 eig"
    eq(E16.det(), -4, "q16 Delta")
    p2 = -E16.det() / 2
    eq(p2, 2, "q16 p^2")
    n = sp.Matrix([1, -1, 0]) / S(2)
    eq((sp.Matrix([1, -1, 0]).T * n)[0], S(2), "q16 p")
    assert classify(F16) == "ell-parab", "q16 class"
    # verify by explicit orthogonal change: X along eig2, Y along eig1 (z), Z along n
    e2 = sp.Matrix([1, 1, 0]) / S(2); e1 = sp.Matrix([0, 0, 1])
    X_, Y_, Z_ = sp.symbols("X_ Y_ Z_")
    sub = X_ * e2 + Y_ * e1 + Z_ * n
    G = sp.expand(F16.subs({x: sub[0], y: sub[1], z: sub[2]}, simultaneous=True))
    eq(G - (2 * X_**2 + Y_**2 + 2 * S(2) * Z_), 0, "q16 reduced")
    # q17
    F17 = x**2 + y**2 - z**2 - 2*x + 4*y + 2*z + 4
    assert centre(F17) == [{x: 1, y: -2, z: 1}], "q17 centre"
    assert classify(F17) == "cone", "q17"
    eq(sp.expand(F17 - ((x - 1)**2 + (y + 2)**2 - (z - 1)**2)), 0, "q17 form")
    # q18
    F18 = (x + y + z)**2 - 1
    A18, E18 = mats(F18)
    assert (A18.rank(), E18.rank()) == (1, 2), "q18"
    assert classify(F18) == "planes-par", "q18 class"
    # q19
    F19 = 2*x*y + 2*y*z + 2*z*x - 4*z + k
    A19, E19 = mats(F19)
    eq(A19.det(), 2, "q19 D")
    ks = sp.solve(E19.det(), k)
    assert ks == [-2], "q19"
    assert centre(F19) == [{x: 1, y: 1, z: -1}], "q19 centre"
    assert classify(F19.subs(k, -2)) == "cone", "q19 class"
    # q20: tangency formula, check on a numeric instance (a,b,c)=(1,2,3)
    aa, bb, cc = 1, 2, 3
    l, m, nn = 1, 1, 1
    pp = sp.sqrt(R(l**2, aa) + R(m**2, bb) + R(nn**2, cc))
    Fc = aa * x**2 + bb * y**2 + cc * z**2 - 1
    pt = {x: l / (aa * pp), y: m / (bb * pp), z: nn / (cc * pp)}
    eq(Fc.subs(pt), 0, "q20 contact on surface")
    eq((l * x + m * y + nn * z).subs(pt), pp, "q20 contact on plane")
    g20 = grad(Fc, (pt[x], pt[y], pt[z]))
    assert sp.Matrix([g20, [l, m, nn]]).rank() == 1, "q20 tangent"
    assert sp.simplify(aa * l**2 + bb * m**2 + cc * nn**2 - pp**2) != 0, "q20 distractor"
    # q21
    F21 = 2*x**2 + 5*y**2 + 3*z**2 + 4*x*y - 6
    A21 = mats(F21)[0]
    ev = {val: vecs for val, mult, vecs in A21.eigenvects()}
    assert sorted(ev) == [1, 3, 6], "q21 eig"
    assert sp.Matrix.hstack(ev[1][0], sp.Matrix([2, -1, 0])).rank() == 1, "q21"
    assert sp.Matrix.hstack(ev[6][0], sp.Matrix([1, 2, 0])).rank() == 1, "q21 distractor"
    semi = {lv: sp.sqrt(sp.Integer(6) / lv) for lv in (1, 3, 6)}
    assert max(semi, key=lambda kk: semi[kk]) == 1, "q21 longest"
    # q22
    al, be, ga = 1, 2, 3
    F22 = x**2 + y**2 - z**2 - 1
    F22s = sp.expand(F22.subs({x: x + al, y: y + be, z: z + ga}, simultaneous=True))
    A22, E22 = mats(F22); A22s, E22s = mats(F22s)
    assert A22 == A22s, "q22 st3 false"
    eq(E22.det(), E22s.det(), "q22 st2")
    eq(E22.det(), 1, "q22 Delta")
    # q23
    assert len(centre(F9)) == 1, "q23 st1"
    a_, b_, c_ = 2, 3, 5
    Fpar = x**2 / a_**2 + y**2 / b_**2 - 2 * z / c_
    assert centre(Fpar) == [], "q23 st2 false"
    Fh2 = x**2 / a_**2 - y**2 / b_**2 - z**2 / c_**2 - 1
    # on x = k: y^2/b^2 + z^2/c^2 = k^2/a^2 - 1
    eq(sp.expand(Fh2.subs(x, k) + y**2 / b_**2 + z**2 / c_**2), k**2 / a_**2 - 1, "q23 st3")
    assert sp.solve([Fh2.subs(x, 1), z], [y, z], dict=True) == [], "q23 st3 gap (real y, z)"
    assert len(sp.solve([Fh2.subs(x, 3), z], [y, z], dict=True)) == 2, "q23 st3 beyond vertex"
    # q24
    assert classify(x**2 / 4 + y**2 / 9 - z**2 - 1) == "hyp1", "q24 A"
    assert classify(x**2 / 4 - y**2 / 9 - z**2 - 1) == "hyp2", "q24 B"
    assert classify(x**2 / 4 + y**2 / 9 - 2 * z) == "ell-parab", "q24 C"
    assert classify(x**2 / 4 + y**2 / 9 - z**2) == "cone", "q24 D"
    # q25
    for F, ranks, kind in [(x**2 + 2*y**2 + 3*z**2 - 1, (3, 4), "ellipsoid"),
                           (x**2 + y**2 - z**2 - 1, (3, 4), "hyp1"),
                           (x**2 + y**2 - z**2, (3, 3), "cone"),
                           (x**2 + y**2 - 2*z, (2, 4), "ell-parab"),
                           (x**2 - y**2 - 2*z, (2, 4), "hyp-parab"),
                           (x**2 - 2*z, (1, 3), "parab-cyl")]:
        A_, E_ = mats(F)
        assert (A_.rank(), E_.rank()) == ranks and classify(F) == kind, ("q25", F)
    # rank-2/rank-3 is a cylinder, not a paraboloid (distractor check)
    assert classify(x**2 + y**2 - 1) == "cylinder", "q25 cyl"
    # q26
    F26 = 2*y*z + 2*z*x + 2*x*y - 1
    assert eigs(F26) == [-1, -1, 2], "q26 eig"
    A26, E26 = mats(F26)
    eq(-E26.det() / A26.det(), 1, "q26 K")
    assert classify(F26) == "hyp2", "q26"
    # q27: cylinder has D = 0 but is not a paraboloid; and infinitely many centres
    Fc27 = x**2 + y**2 - 1
    eq(mats(Fc27)[0].det(), 0, "q27 D")
    assert classify(Fc27) == "cylinder", "q27 A false"
    assert centre(Fc27) == [{x: 0, y: 0}], "q27 line of centres"
    # q28
    F28 = x**2 + 2*y**2 + 3*z**2 - 6
    g28 = grad(F28, (1, 1, 1))
    assert same_plane(g28[0] * (x - 1) + g28[1] * (y - 1) + g28[2] * (z - 1), x + 2*y + 3*z - 6), "q28 A"
    assert sp.Matrix([g28, [1, 1, 1]]).rank() == 2, "q28 R false"
    # q29
    F29 = x*y - z
    assert centre(F29) == [], "q29 A"
    lm = sp.Symbol("lm")
    eq(F29.subs({x: lm, z: lm * y}), 0, "q29 R family 1")
    eq(F29.subs({y: lm, z: lm * x}), 0, "q29 R family 2")
    assert classify(F29) == "hyp-parab", "q29 class"
    assert classify(x**2 + y**2 - z**2 - 1) == "hyp1" and len(centre(x**2 + y**2 - z**2 - 1)) == 1, "q29 ruled and central"
    # q30: axis of revolution along eigenvector of 4
    ev7 = {val: vecs for val, mult, vecs in A7.eigenvects()}
    assert len(ev7[2]) == 2 and sp.Matrix.hstack(ev7[4][0], sp.Matrix([1, 1, 0])).rank() == 1, "q30"

    # notes examples
    Fn1 = 7*x**2 + 6*y**2 + 5*z**2 - 4*y*z - 4*x*y - 6*x - 24*y + 18*z + 30
    An1, En1 = mats(Fn1)
    assert centre(Fn1) == [{x: 1, y: 2, z: -1}] and eigs(Fn1) == [3, 6, 9], "notes ex1"
    eq(En1.det() / An1.det(), -6, "notes ex1 const")
    Fn2 = 4*y**2 + 4*z**2 + 4*y*z - 2*x - 14*y - 22*z + 33
    An2, En2 = mats(Fn2)
    assert eigs(Fn2) == [0, 2, 6] and classify(Fn2) == "ell-parab", "notes ex2"
    eq(-En2.det() / 12, 1, "notes ex2 p^2")
    eq(mats(x**2 + y**2 - z**2 - 1)[1].det(), 1, "notes Delta hyp1")
    eq(mats(x**2 + y**2 + z**2 + 1)[1].det(), 1, "notes Delta imaginary")
    eq(mats(x**2 - y**2 - 2*z)[1].det(), 1, "notes Delta hyp-parab")
    eq(mats(x**2 + y**2 - 2*z)[1].det(), -1, "notes Delta ell-parab")
    eq(mats(x**2 - y**2 - z**2 - 1)[1].det(), -1, "notes Delta hyp2")


T.write(check)
