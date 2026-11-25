# Quadrics

## The general equation and its matrices {#general-equation}

A **quadric** (conicoid) is the locus of a second-degree equation in $x, y, z$. Throughout, write it as

$$F \equiv ax^2 + by^2 + cz^2 + 2fyz + 2gzx + 2hxy + 2ux + 2vy + 2wz + d = 0.$$

The factors of $2$ are part of the convention: the coefficient of $yz$ is $2f$, of $x$ is $2u$, and so on.

**Matrix form.** With $X = (x, y, z)^T$ and $L = (u, v, w)^T$,

$$F = X^TAX + 2L^TX + d, \qquad A = \begin{pmatrix} a & h & g\\ h & b & f\\ g & f & c\end{pmatrix}.$$

$A$ is the matrix of the **quadratic part** (a real symmetric matrix; see Quadratic Forms). In homogeneous coordinates $\tilde X = (x, y, z, 1)^T$ the whole equation is $\tilde X^T E\,\tilde X = 0$ with the $4 \times 4$ symmetric matrix

$$E = \begin{pmatrix} a & h & g & u\\ h & b & f & v\\ g & f & c & w\\ u & v & w & d\end{pmatrix} = \begin{pmatrix} A & L\\ L^T & d\end{pmatrix}.$$

Write

$$D = \det A, \qquad \Delta = \det E.$$

**Partial derivatives.** $\tfrac12 F_x = ax + hy + gz + u$, $\tfrac12 F_y = hx + by + fz + v$, $\tfrac12 F_z = gx + fy + cz + w$. In matrix form, $\tfrac12\nabla F = AX + L$. These three linear expressions give both the centre and the tangent plane.

**Worked example.** For $x^2 - 2y^2 + 3z^2 - 4yz + 6zx - 2xy + 4x - 6 = 0$, halve the cross and linear coefficients:

$$A = \begin{pmatrix} 1 & -1 & 3\\ -1 & -2 & -2\\ 3 & -2 & 3\end{pmatrix}, \qquad L = \begin{pmatrix} 2\\ 0\\ 0\end{pmatrix}, \qquad d = -6.$$

:::caution
The most common slip is **not halving**. The $(1,2)$ entry of $A$ is $h$, which is *half* the coefficient of $xy$. The same goes for $u, v, w$ in the last column of $E$. Put an unhalved coefficient in and every invariant comes out wrong.
:::

**What the matrices control.**
- The **eigenvalues** of $A$ give the shape and the principal directions.
- The **rank** of $A$ tells whether there is a unique centre.
- $\Delta$ and the **rank of $E$** tell whether the quadric is degenerate: a cone, a cylinder or a pair of planes.

## The standard surfaces {#standard-surfaces}

Every real non-empty quadric is congruent (by a rotation and translation) to one of the forms below. Here $a, b, c > 0$.

| Canonical form | Surface | Centre |
|:---|:---|:---|
| $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} + \dfrac{z^2}{c^2} = 1$ | ellipsoid | origin |
| $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} - \dfrac{z^2}{c^2} = 1$ | hyperboloid of one sheet | origin |
| $\dfrac{x^2}{a^2} - \dfrac{y^2}{b^2} - \dfrac{z^2}{c^2} = 1$ | hyperboloid of two sheets | origin |
| $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} - \dfrac{z^2}{c^2} = 0$ | (elliptic) cone, vertex $O$ | origin |
| $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = \dfrac{2z}{c}$ | elliptic paraboloid | none |
| $\dfrac{x^2}{a^2} - \dfrac{y^2}{b^2} = \dfrac{2z}{c}$ | hyperbolic paraboloid | none |
| $\dfrac{x^2}{a^2} \pm \dfrac{y^2}{b^2} = 1$ | elliptic / hyperbolic cylinder | line of centres |
| $y^2 = 4ax$ | parabolic cylinder | none |
| $\dfrac{x^2}{a^2} - \dfrac{y^2}{b^2} = 0$, $\ x^2 = a^2$ | intersecting / parallel planes | line / plane of centres |

**Counting signs.** In a central form $\pm\frac{x^2}{a^2} \pm \frac{y^2}{b^2} \pm \frac{z^2}{c^2} = 1$, count the **positive** squares: three gives an ellipsoid, two a hyperboloid of **one** sheet, one a hyperboloid of **two** sheets, and none an imaginary ellipsoid (no real points).

**Sections (traces)** identify a surface quickly:

| Surface | Sections $z = k$ | Sections $x = k$ |
|:---|:---|:---|
| ellipsoid | ellipses for $\lvert k\rvert < c$ | ellipses for $\lvert k\rvert < a$ |
| hyperboloid of one sheet | ellipses for every $k$ | hyperbolas (a line pair at $\lvert k\rvert = a$) |
| hyperboloid of two sheets $\frac{x^2}{a^2} - \frac{y^2}{b^2} - \frac{z^2}{c^2} = 1$ | hyperbolas | ellipses only for $\lvert k\rvert > a$; none for $\lvert k\rvert < a$ |
| elliptic paraboloid | ellipses for $k > 0$ | parabolas |
| hyperbolic paraboloid | hyperbolas (a line pair at $k = 0$) | parabolas |

An equation in which **one variable is missing**, such as $4x^2 + 9y^2 = 36$, is a **cylinder** in space. Its generators are parallel to the axis of the missing variable, and its cross-section is the conic in the other two. So $4x^2 + 9y^2 = 36$ is an elliptic cylinder, not an ellipse.

:::exam-tip
The hyperboloid of one sheet and the hyperbolic paraboloid are the two **doubly ruled** non-degenerate quadrics: each contains two families of straight lines. The ellipsoid, the hyperboloid of two sheets and the elliptic paraboloid contain no real lines.
:::

## Invariants under change of rectangular axes {#invariants}

A change of rectangular axes is $X = PX' + t$, where $P$ is orthogonal (a rotation, possibly with a reflection) and $t$ is a translation. Under it:

- the quadratic part's matrix becomes $A' = P^TAP$, which has the **same eigenvalues** as $A$;
- the $4\times4$ matrix becomes $E' = T^TET$, with $T = \begin{pmatrix} P & t\\ 0 & 1\end{pmatrix}$ and $\det T = \pm 1$.

Hence the following are **invariants**:

$$I = a + b + c, \qquad J = bc + ca + ab - f^2 - g^2 - h^2, \qquad D = \det A, \qquad \Delta = \det E,$$

together with $\operatorname{rank} A$ and $\operatorname{rank} E$.

- $I$ is the trace of $A$, $J$ is the sum of its principal $2\times2$ minors, and $D$ is its determinant.
- They are the coefficients of the **discriminating cubic** (the characteristic equation of $A$):
  $$\lambda^3 - I\lambda^2 + J\lambda - D = 0, \qquad \lambda_1 + \lambda_2 + \lambda_3 = I,\ \ \sum\lambda_i\lambda_j = J,\ \ \lambda_1\lambda_2\lambda_3 = D.$$
- A **translation** alone leaves $a, b, c, f, g, h$ unchanged, so it changes nothing in $A$. It changes $u, v, w, d$, but not $\Delta$ (row and column operations with determinant $1$).
- A **rotation** changes the individual coefficients but not $I, J, D, \Delta$.

**Worked example.** For $3x^2 + 3y^2 + 2z^2 + 2xy = 4$: $a = 3$, $b = 3$, $c = 2$, $h = 1$, $f = g = 0$.

$$I = 8, \qquad J = (6 + 6 + 9) - 1 = 20, \qquad D = 2(9 - 1) = 16.$$

The cubic is $\lambda^3 - 8\lambda^2 + 20\lambda - 16 = (\lambda - 4)(\lambda - 2)^2$, with roots $4, 2, 2$. So the surface is $4X^2 + 2Y^2 + 2Z^2 = 4$, i.e. $X^2 + \frac{Y^2}{2} + \frac{Z^2}{2} = 1$: an ellipsoid of revolution (a spheroid) about the $X$-axis.

:::caution
$J$ uses $h$, not $2h$. In the example, taking $h = 2$ gives $J = 17$, and then the "eigenvalues" no longer add up to $I$ and multiply to $D$ consistently. Check every candidate reduced form against $I$ (sum of the new coefficients) first. That alone eliminates most wrong options.
:::

## Central quadrics: centre and reduction {#central-reduction}

A point $C$ is a **centre** if the quadric is symmetric about $C$. Shifting the origin to $C$ must kill the linear terms, so the centre satisfies

$$\tfrac12 F_x = \tfrac12 F_y = \tfrac12 F_z = 0, \qquad\text{i.e.}\qquad AX_0 + L = 0.$$

- If $D \ne 0$, there is a **unique centre** $X_0 = -A^{-1}L$. The quadric is called **central**.
- If $D = 0$, there is either no centre or a whole line or plane of centres.

**Reduction when $D \ne 0$.**

1. **Translate** to the centre. The linear terms vanish and the new constant is
   $$d' = F(X_0) = ux_0 + vy_0 + wz_0 + d = \frac{\Delta}{D}.$$
   The last form follows because $\Delta$ is invariant and becomes $D\cdot d'$ after the shift.
2. **Rotate** to the eigenvectors of $A$. The result is
   $$\lambda_1X^2 + \lambda_2Y^2 + \lambda_3Z^2 + \frac{\Delta}{D} = 0.$$

The **principal axes** of the quadric are the lines through the centre along the eigenvectors. For an ellipsoid $\lambda_1X^2 + \lambda_2Y^2 + \lambda_3Z^2 = K$ ($K > 0$), the semi-axis along the $\lambda_i$-eigenvector is $\sqrt{K/\lambda_i}$. So the **smallest eigenvalue gives the longest axis**.

**Worked example.** Reduce $7x^2 + 6y^2 + 5z^2 - 4yz - 4xy - 6x - 24y + 18z + 30 = 0$.

- $A = \begin{pmatrix} 7 & -2 & 0\\ -2 & 6 & -2\\ 0 & -2 & 5\end{pmatrix}$, $L = (-3, -12, 9)^T$, and $D = 162$.
- **Centre:** $7x - 2y = 3$, $-2x + 6y - 2z = 12$, $-2y + 5z = -9$. This gives $(1, 2, -1)$.
- **Constant:** $d' = (-3)(1) + (-12)(2) + 9(-1) + 30 = -6$. Check: $\Delta = -972$, and $\Delta/D = -6$.
- **Eigenvalues:** $I = 18$, $J = 99$, $D = 162$, so $\lambda^3 - 18\lambda^2 + 99\lambda - 162 = (\lambda - 3)(\lambda - 6)(\lambda - 9)$.

$$3X^2 + 6Y^2 + 9Z^2 = 6 \iff \frac{X^2}{2} + Y^2 + \frac{Z^2}{2/3} = 1:$$

an ellipsoid with centre $(1, 2, -1)$.

:::exam-tip
If two eigenvalues are equal, say $\lambda_2 = \lambda_3$, the central quadric is a **surface of revolution** about the axis of the simple eigenvalue $\lambda_1$. For example, $3x^2 + 3y^2 + 2z^2 + 2xy = 4$ (roots $4, 2, 2$) is a spheroid.
:::

## Non-central quadrics: paraboloids and cylinders {#non-central}

When $D = 0$, at least one eigenvalue is $0$.

**Rank $A = 2$** (eigenvalues $\lambda_1, \lambda_2 \ne 0$, $\lambda_3 = 0$). Rotate to the eigenvectors and complete the squares in $X$ and $Y$. What is left is

$$\lambda_1X^2 + \lambda_2Y^2 + 2pZ + q = 0.$$

- If $p \ne 0$, shift $Z$ to absorb $q$. This gives a **paraboloid** $\lambda_1X^2 + \lambda_2Y^2 + 2pZ = 0$. Computing $\Delta$ for this form gives
  $$\Delta = -\lambda_1\lambda_2\,p^2, \qquad\text{so}\qquad p^2 = -\frac{\Delta}{\lambda_1\lambda_2}.$$
  It is **elliptic** if $\lambda_1\lambda_2 > 0$ and **hyperbolic** if $\lambda_1\lambda_2 < 0$. Here $p = L\cdot n$, where $n$ is the unit eigenvector for $\lambda_3 = 0$. So the paraboloid case is exactly $\Delta \ne 0$.
- If $p = 0$ (so $\Delta = 0$), the equation is $\lambda_1X^2 + \lambda_2Y^2 + q = 0$:
  - an elliptic or hyperbolic **cylinder** if $q \ne 0$ (rank $E = 3$);
  - a **pair of intersecting planes** if $q = 0$ and $\lambda_1\lambda_2 < 0$ (rank $E = 2$).

**Rank $A = 1$** (the quadratic part is a perfect square $\lambda(\alpha x + \beta y + \gamma z)^2$):

- a **parabolic cylinder** if the linear part is not a multiple of $\alpha x + \beta y + \gamma z$ (rank $E = 3$);
- otherwise a **pair of parallel planes** (rank $E = 2$) or **coincident planes** (rank $E = 1$).

**Worked example.** $4y^2 + 4z^2 + 4yz - 2x - 14y - 22z + 33 = 0$.

- $A = \begin{pmatrix} 0 & 0 & 0\\ 0 & 4 & 2\\ 0 & 2 & 4\end{pmatrix}$ has eigenvalues $6, 2, 0$, so $D = 0$.
- $\Delta = -12 \ne 0$, so this is a paraboloid with $p^2 = -\dfrac{-12}{6\cdot2} = 1$.
- The reduced form is $6X^2 + 2Y^2 = 2Z$, i.e. $3X^2 + Y^2 = Z$: an **elliptic paraboloid** (both nonzero eigenvalues positive).

**Quick cases.**
- $z = xy$: eigenvalues $\pm\frac12, 0$ and $\Delta \ne 0$, so a **hyperbolic paraboloid** (rotate through $45^\circ$: $X^2 - Y^2 = 2Z$).
- $x^2 + 2xy + y^2 = 4z$: this is $(x + y)^2 = 4z$, with rank $A = 1$, so a **parabolic cylinder**.
- $(x + y + z)^2 = 1$: rank $A = 1$, rank $E = 2$, so the **parallel planes** $x + y + z = \pm 1$.

:::caution
$D = 0$ does **not** mean "paraboloid". It only says that there is no *unique* centre. A cylinder (for example $x^2 + y^2 = 1$, with a whole line of centres) also has $D = 0$. Decide with $\Delta$, or with the rank of $E$.
:::

## Classification table {#classification}

Combine the eigenvalues of $A$ with $\Delta$ (or the ranks of $A$ and $E$). For a central quadric write the reduced form as $\lambda_1X^2 + \lambda_2Y^2 + \lambda_3Z^2 = K$, with $K = -\Delta/D$.

| $\operatorname{rank} A$ | $\operatorname{rank} E$ | Condition | Real quadric |
|:---:|:---:|:---|:---|
| 3 | 4 | all $\lambda_i$ have the sign of $K$ | ellipsoid |
| 3 | 4 | two $\lambda_i$ have the sign of $K$ | hyperboloid of one sheet |
| 3 | 4 | one $\lambda_i$ has the sign of $K$ | hyperboloid of two sheets |
| 3 | 3 | $\Delta = 0$, $\lambda_i$ not all of one sign | cone, vertex at the centre |
| 2 | 4 | $\lambda_1\lambda_2 > 0$ / $< 0$ | elliptic / hyperbolic paraboloid |
| 2 | 3 | $\Delta = 0$ | elliptic / hyperbolic cylinder |
| 2 | 2 | $\lambda_1\lambda_2 < 0$ | pair of intersecting planes |
| 1 | 3 | — | parabolic cylinder |
| 1 | 2 or 1 | — | parallel or coincident planes |

- If all three $\lambda_i$ have the sign *opposite* to $K$, the quadric is an imaginary ellipsoid.
- In the cone row, if all $\lambda_i$ have the same sign, the locus is a single point (an imaginary cone).

**Cones.**
- A **homogeneous** second-degree equation in $x, y, z$ is a cone with vertex at the origin. If it holds at $(x, y, z)$, it holds at $(tx, ty, tz)$.
- In general, a quadric with $D \ne 0$ and $\Delta = 0$ is a cone with **vertex at the centre**, because the constant $\Delta/D$ vanishes after the shift.

*Example.* For $x^2 + y^2 - z^2 - 2x + 4y + 2z + 4 = 0$, the centre is $(1, -2, 1)$ and $d' = 4 - 1 - 4 + 1 = 0$. So it is the cone $(x - 1)^2 + (y + 2)^2 = (z - 1)^2$ with vertex $(1, -2, 1)$.

**Cylinders.** If a variable is missing, the surface is a cylinder whose generators are parallel to that axis (see the standard surfaces).

**Worked example.** $2yz + 2zx + 2xy = 1$. Here $A = J - I$, where $J$ is the all-ones matrix, so the eigenvalues are $2, -1, -1$. Then $D = 2$, $\Delta = -2$ and $K = 1$:

$$2X^2 - Y^2 - Z^2 = 1.$$

One positive square gives a **hyperboloid of two sheets**. Since $\lambda_2 = \lambda_3$, it is a surface of revolution about the line $x = y = z$.

:::exam-tip
For a real non-degenerate quadric (rank $E = 4$ with real points), $\Delta > 0$ exactly for the hyperboloid of one sheet and the hyperbolic paraboloid: the ruled ones. $\Delta < 0$ for the ellipsoid, the hyperboloid of two sheets and the elliptic paraboloid. Check: $x^2 + y^2 - z^2 = 1$ has $E = \operatorname{diag}(1, 1, -1, -1)$, so $\Delta = 1$. The imaginary ellipsoid also has $\Delta > 0$, so use this only once you know the surface is real.
:::

## Tangent planes to conicoids {#tangent-planes}

**General quadric.** If $P(x_1, y_1, z_1)$ lies on $F = 0$ and $\nabla F(P) \ne 0$, the tangent plane at $P$ is

$$(x - x_1)F_x(P) + (y - y_1)F_y(P) + (z - z_1)F_z(P) = 0.$$

Equivalently, use the substitution rule $x^2 \to xx_1$, $2yz \to yz_1 + y_1z$, $2x \to x + x_1$, and so on:

$$axx_1 + byy_1 + czz_1 + f(yz_1 + y_1z) + g(zx_1 + z_1x) + h(xy_1 + x_1y) + u(x + x_1) + v(y + y_1) + w(z + z_1) + d = 0.$$

The **normal** at $P$ has direction ratios $F_x : F_y : F_z$ at $P$.

**Example.** On $x^2 + 2y^2 - z^2 + 4xy - 2x + 2z - 6 = 0$ at $(1, 1, 1)$:

$$\tfrac12 F_x = x + 2y - 1 = 2, \qquad \tfrac12 F_y = 2x + 2y = 4, \qquad \tfrac12 F_z = -z + 1 = 0.$$

The tangent plane is $2(x - 1) + 4(y - 1) = 0$, i.e. $x + 2y = 3$. Dropping the linear terms of $F$ would wrongly give $3x + 4y - z = 6$.

**Central conicoid $ax^2 + by^2 + cz^2 = 1$.**

- The tangent plane at $(\alpha, \beta, \gamma)$ is $a\alpha x + b\beta y + c\gamma z = 1$.
- The plane $lx + my + nz = p$ **touches** it if and only if
  $$\frac{l^2}{a} + \frac{m^2}{b} + \frac{n^2}{c} = p^2.$$
  The point of contact is $\left(\frac{l}{ap}, \frac{m}{bp}, \frac{n}{cp}\right)$.
- For the ellipsoid $\frac{x^2}{A^2} + \frac{y^2}{B^2} + \frac{z^2}{C^2} = 1$ the condition reads $A^2l^2 + B^2m^2 + C^2n^2 = p^2$.

*Example.* The planes $x + y + z = k$ touching $\frac{x^2}{4} + \frac{y^2}{9} + \frac{z^2}{12} = 1$ satisfy $k^2 = 4 + 9 + 12 = 25$, so $k = \pm 5$.

**Proof idea.** Write the plane as $lx + my + nz = p$ and match it with $a\alpha x + b\beta y + c\gamma z = 1$. This gives $\alpha = \frac{l}{ap}$, and so on. Substituting into $a\alpha^2 + b\beta^2 + c\gamma^2 = 1$ gives the condition.

:::caution
The normal to a central conicoid at $P$ is along $(a\alpha, b\beta, c\gamma)$, **not** along $CP = (\alpha, \beta, \gamma)$. The two agree only when $a = b = c$ (a sphere). So, unlike for the sphere, the normal does not in general pass through the centre.
:::

Enveloping cones, enveloping cylinders and generating lines are not listed in the SLST syllabus. Only the ruled/unruled fact above is worth knowing.

## Quick checks and traps {#exam-tips}

- **Halve first.** $A$ has $h, g, f$ (half the cross coefficients), and $E$ has $u, v, w$ (half the linear coefficients).
- **Trace test.** Any reduced form $\lambda_1X^2 + \lambda_2Y^2 + \lambda_3Z^2$ must have $\lambda_1 + \lambda_2 + \lambda_3 = a + b + c$ and $\lambda_1\lambda_2\lambda_3 = D$.
- **Constant after shifting to the centre** $= \Delta/D = ux_0 + vy_0 + wz_0 + d$. Do not use $\Delta$ itself.
- **Degenerate iff $\Delta = 0$:** a cone ($D \ne 0$), a cylinder or a pair of planes ($D = 0$).
- **$D = 0$, $\Delta \ne 0$** means a paraboloid: elliptic if the two nonzero eigenvalues have the same sign, hyperbolic otherwise.
- **Sign count for $\pm X^2 \pm Y^2 \pm Z^2 = 1$:** $+++$ ellipsoid, $++-$ one sheet, $+--$ two sheets.
- **Classic surfaces:** $yz + zx + xy = a^2$ is a hyperboloid of two sheets; $z = xy$ is a hyperbolic paraboloid; $x^2 + 4yz = 4$ is a hyperboloid of one sheet (eigenvalues $1, 2, -2$).
- **Missing variable** means a cylinder; a **homogeneous** equation means a cone with vertex $O$.
- **Tangency to $ax^2 + by^2 + cz^2 = 1$:** $\sum l^2/a = p^2$. Do not write $\sum al^2$.
- **Longest axis** of an ellipsoid lies along the eigenvector of the **smallest** eigenvalue.
