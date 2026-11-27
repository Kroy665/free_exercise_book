import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from qlib import Topic, eq

T = Topic("math.geometry.sphere", exams=["slst-1112"])

# ---------------------------------------------------------------- single (21)
# q1
T.single(1, ["general-equation"], r"The centre and radius of the sphere $x^2 + y^2 + z^2 - 2x + 4y - 6z - 11 = 0$ are",
         [r"$(1, -2, 3)$ and $5$", r"$(-1, 2, -3)$ and $5$", r"$(1, -2, 3)$ and $\sqrt3$", r"$(2, -4, 6)$ and $5$"],
         r"""Compare with $x^2 + y^2 + z^2 + 2ux + 2vy + 2wz + d = 0$: $u = -1$, $v = 2$, $w = -3$, $d = -11$.
$$\text{centre } (-u, -v, -w) = (1, -2, 3), \qquad r = \sqrt{1 + 4 + 9 + 11} = 5.$$
$(-1, 2, -3)$ forgets to change the sign; $\sqrt3$ comes from $u^2 + v^2 + w^2 + d$; $(2, -4, 6)$ forgets to halve the coefficients.""")

# q2
T.single(1, ["given-data"], r"The sphere having the points $(1, 2, 3)$ and $(3, -2, 1)$ as ends of a diameter is",
         [r"$x^2 + y^2 + z^2 - 4x - 4z + 2 = 0$", r"$x^2 + y^2 + z^2 - 4x - 4z - 2 = 0$",
          r"$x^2 + y^2 + z^2 + 4x + 4z + 2 = 0$", r"$x^2 + y^2 + z^2 - 4x - 4z - 16 = 0$"],
         r"""Use $(x - x_1)(x - x_2) + (y - y_1)(y - y_2) + (z - z_1)(z - z_2) = 0$:
$$(x - 1)(x - 3) + (y - 2)(y + 2) + (z - 3)(z - 1) = 0 \implies x^2 + y^2 + z^2 - 4x - 4z + 2 = 0.$$
Check: the centre $(2, 0, 2)$ is the midpoint, and $r^2 = 4 + 4 - 2 = 6 = \left(\tfrac12 AB\right)^2 = \tfrac{24}{4}$. The option with $-16$ uses $AB^2 = 24$ as $r^2$ instead of $\left(\tfrac12AB\right)^2$.""")

# q3
T.single(1, ["general-equation"],
         r"The equation $ax^2 + by^2 + cz^2 + 2fyz + 2gzx + 2hxy + 2ux + 2vy + 2wz + d = 0$ represents a sphere (real, point or virtual) if and only if",
         [r"$a = b = c \ne 0$ and $f = g = h = 0$", r"$a = b = c \ne 0$", r"$f = g = h = 0$ and $u = v = w$",
          r"$a + b + c = 0$ and $f = g = h = 0$"],
         r"""After dividing by $a$, a sphere's equation must be $x^2 + y^2 + z^2 + (\text{linear}) = 0$: the squared terms have equal nonzero coefficients and there are no product terms.
$$a = b = c \ne 0, \qquad f = g = h = 0.$$
Equal squared coefficients alone are not enough: $x^2 + y^2 + z^2 + 2xy = 1$ is $(x + y)^2 + z^2 = 1$, a cylinder. The linear coefficients $u, v, w$ only move the centre.""")

# q4
T.single(2, ["given-data"], r"The radius of the sphere through the four points $(0, 0, 0)$, $(2, 0, 0)$, $(0, 4, 0)$ and $(0, 0, 6)$ is",
         [r"$\sqrt{14}$", r"$14$", r"$2\sqrt{14}$", r"$\sqrt7$"],
         r"""Through the origin, $d = 0$; then $(a, 0, 0)$ gives $u = -\frac a2$, and so on:
$$x^2 + y^2 + z^2 - 2x - 4y - 6z = 0.$$
Centre $(1, 2, 3)$, radius $\sqrt{1 + 4 + 9} = \sqrt{14}$. $2\sqrt{14} = \sqrt{4 + 16 + 36}$ is the diameter, and $14$ is $r^2$.""")

# q5
T.single(2, ["plane-section"], r"The centre and radius of the circle $x^2 + y^2 + z^2 = 25$, $x + 2y + 2z = 9$ are",
         [r"$(1, 2, 2)$ and $4$", r"$(1, 2, 2)$ and $3$", r"$(3, 6, 6)$ and $4$", r"$(1, 2, 2)$ and $\sqrt{34}$"],
         r"""The sphere has centre $O$ and radius $5$. The distance from $O$ to the plane is $\delta = \frac{9}{\sqrt{1 + 4 + 4}} = 3$.
- Centre of the circle: the foot of the perpendicular from $O$, $t(1, 2, 2)$ with $9t = 9$, so $(1, 2, 2)$.
- Radius: $\sqrt{25 - 9} = 4$.

$3$ is the distance $\delta$, not the radius; $\sqrt{34}$ uses $r^2 + \delta^2$; $(3, 6, 6)$ takes $t = 9/3$ instead of $9/9$ (and is not even on the plane).""")

# q6
T.single(2, ["plane-section"], r"The radius of the circle in which the plane $x + 2y + 2z = 15$ cuts the sphere $x^2 + y^2 + z^2 - 2y - 4z - 11 = 0$ is",
         [r"$\sqrt7$", r"$5$", r"$1$", r"$\sqrt{13}$"],
         r"""The sphere has centre $(0, 1, 2)$ and radius $\sqrt{1 + 4 + 11} = 4$. The distance of the centre from the plane is
$$\delta = \frac{\lvert 0 + 2 + 4 - 15\rvert}{3} = 3, \qquad \rho = \sqrt{16 - 9} = \sqrt7.$$
$5 = \sqrt{16 + 9}$ adds instead of subtracting; $1 = 4 - 3$ subtracts the lengths instead of their squares.""")

# q7
T.single(2, ["through-circle"], r"The sphere through the circle $x^2 + y^2 + z^2 = 9$, $2x + 3y + 4z = 5$ and the origin is",
         [r"$5(x^2 + y^2 + z^2) - 18x - 27y - 36z = 0$", r"$5(x^2 + y^2 + z^2) + 18x + 27y + 36z = 0$",
          r"$x^2 + y^2 + z^2 - 2x - 3y - 4z = 0$", r"$5(x^2 + y^2 + z^2) - 18x - 27y - 36z - 90 = 0$"],
         r"""Every sphere through the circle is $x^2 + y^2 + z^2 - 9 + \lambda(2x + 3y + 4z - 5) = 0$. At the origin, $-9 - 5\lambda = 0$, so $\lambda = -\frac95$. Multiply by $5$:
$$5(x^2 + y^2 + z^2) - 45 - 18x - 27y - 36z + 45 = 0 \implies 5(x^2 + y^2 + z^2) - 18x - 27y - 36z = 0.$$
Check: no constant term, so it passes through $O$. The option with $+18x$ takes $\lambda = +\frac95$; the one with $-90$ forgets the constant $-5$ in the plane.""")

# q8
T.single(3, ["through-circle"], r"The sphere having the circle $x^2 + y^2 + z^2 = 25$, $x + y + z = 3$ as a great circle is",
         [r"$x^2 + y^2 + z^2 - 2x - 2y - 2z - 19 = 0$", r"$x^2 + y^2 + z^2 + 2x + 2y + 2z - 31 = 0$",
          r"$x^2 + y^2 + z^2 - 2x - 2y - 2z - 25 = 0$", r"$x^2 + y^2 + z^2 - x - y - z - 22 = 0$"],
         r"""Take $x^2 + y^2 + z^2 - 25 + \lambda(x + y + z - 3) = 0$, with centre $\left(-\frac\lambda2, -\frac\lambda2, -\frac\lambda2\right)$. For a great circle the centre lies on the plane:
$$-\frac{3\lambda}{2} = 3 \implies \lambda = -2, \qquad x^2 + y^2 + z^2 - 2x - 2y - 2z - 19 = 0.$$
Check: centre $(1, 1, 1)$, $r^2 = 3 + 19 = 22$; and the circle's radius is $\sqrt{25 - 3} = \sqrt{22}$ (distance $\sqrt3$ from $O$), as it should be. $\lambda = +2$ gives the $-31$ option; the $-25$ option drops the term $-3\lambda$.""")

# q9
T.single(1, ["tangent-plane"], r"The tangent plane to the sphere $x^2 + y^2 + z^2 = 14$ at the point $(1, 2, 3)$ is",
         [r"$x + 2y + 3z = 14$", r"$x + 2y + 3z = 0$", r"$x + 2y + 3z = \sqrt{14}$", r"$3x + 2y + z = 14$"],
         r"""For $x^2 + y^2 + z^2 = a^2$ the tangent plane at $(x_1, y_1, z_1)$ is $xx_1 + yy_1 + zz_1 = a^2$:
$$x + 2y + 3z = 14.$$
Check: $(1, 2, 3)$ gives $1 + 4 + 9 = 14$. $x + 2y + 3z = 0$ is the parallel plane through the centre; $\sqrt{14}$ uses the radius in place of $a^2$.""")

# q10
T.single(2, ["tangent-plane"], r"The tangent plane at $(1, 1, 1)$ to the sphere $x^2 + y^2 + z^2 + 2x - 4y + 2z - 3 = 0$ is",
         [r"$2x - y + 2z - 3 = 0$", r"$x - y + z - 1 = 0$", r"$x + y + z - 3 = 0$", r"$y = 1$"],
         r"""Here $u = 1$, $v = -2$, $w = 1$, $d = -3$. Use $T = 0$:
$$x + y + z + (x + 1) - 2(y + 1) + (z + 1) - 3 = 0 \implies 2x - y + 2z - 3 = 0.$$
Check: the normal $(2, -1, 2)$ is $(x_1 + u, y_1 + v, z_1 + w)$, the direction from the centre $(-1, 2, -1)$ to the point. $x - y + z = 1$ comes from replacing $2ux$ by $2u(x + x_1)$; $x + y + z = 3$ keeps only $xx_1 + yy_1 + zz_1$.""")

# q11
T.single(2, ["tangent-plane"], r"The plane $2x - y + 2z = k$ touches the sphere $x^2 + y^2 + z^2 - 2x - 4y + 2z - 3 = 0$ if and only if",
         [r"$k = 7$ or $k = -11$", r"$k = 11$ or $k = -7$", r"$k = 9$ or $k = -9$", r"$k = 7$ only"],
         r"""Centre $(1, 2, -1)$, radius $\sqrt{1 + 4 + 1 + 3} = 3$. Tangency: distance from the centre $=$ radius.
$$\frac{\lvert 2 - 2 - 2 - k\rvert}{3} = 3 \iff \lvert k + 2\rvert = 9 \iff k = 7 \text{ or } k = -11.$$
Two parallel tangent planes always exist, so "7 only" is incomplete. $\pm 9$ is the answer for a sphere centred where $2x - y + 2z = 0$; $11, -7$ is the sign slip.""")

# q12
T.single(2, ["tangent-plane"], r"The plane $lx + my + nz = p$ touches the sphere $x^2 + y^2 + z^2 + 2ux + 2vy + 2wz + d = 0$ if and only if",
         [r"$(ul + vm + wn + p)^2 = (l^2 + m^2 + n^2)(u^2 + v^2 + w^2 - d)$",
          r"$(ul + vm + wn - p)^2 = (l^2 + m^2 + n^2)(u^2 + v^2 + w^2 - d)$",
          r"$(ul + vm + wn + p)^2 = (l^2 + m^2 + n^2)(u^2 + v^2 + w^2 + d)$",
          r"$(ul + vm + wn + p)^2 = u^2 + v^2 + w^2 - d$"],
         r"""The distance from the centre $(-u, -v, -w)$ to $lx + my + nz - p = 0$ must equal the radius:
$$\frac{\lvert -ul - vm - wn - p\rvert}{\sqrt{l^2 + m^2 + n^2}} = \sqrt{u^2 + v^2 + w^2 - d}.$$
Squaring gives $(ul + vm + wn + p)^2 = (l^2 + m^2 + n^2)(u^2 + v^2 + w^2 - d)$. The $-p$ version uses the centre as $(u, v, w)$; the last option forgets $\sqrt{l^2 + m^2 + n^2}$. Check with $u = v = w = 0$, $d = -a^2$: $p^2 = a^2(l^2 + m^2 + n^2)$.""")

# q13
T.single(2, ["radical-plane"], r"The length of the tangent from the point $(1, 1, 1)$ to the sphere $x^2 + y^2 + z^2 - 2x + 4y - 6z + 5 = 0$ is",
         [r"$2$", r"$4$", r"$\sqrt{13}$", r"$\sqrt2$"],
         r"""The square of the tangent length is the power $S_1$:
$$S_1 = 1 + 1 + 1 - 2 + 4 - 6 + 5 = 4, \qquad \text{length} = 2.$$
Check: centre $(1, -2, 3)$, $r = 3$, $CP^2 = 0 + 9 + 4 = 13$, and $13 - 9 = 4$. $4$ is the power itself, not its square root; $\sqrt{13}$ is the distance to the centre.""")

# q14
T.single(1, ["radical-plane"], r"The radical plane of the spheres $x^2 + y^2 + z^2 + 2x + 2y + 2z - 2 = 0$ and $x^2 + y^2 + z^2 - 4x + 6y + 4 = 0$ is",
         [r"$3x - 2y + z - 3 = 0$", r"$3x - 2y + z + 3 = 0$", r"$3x - 2y + z - 1 = 0$", r"$x - 4y - z + 1 = 0$"],
         r"""Both are in standard form, so subtract:
$$S_1 - S_2 = 6x - 4y + 2z - 6 = 0 \implies 3x - 2y + z - 3 = 0.$$
Check: its normal $(3, -2, 1)$ is parallel to the line of centres $(-1, -1, -1) \to (2, -3, 0)$, direction $(3, -2, 1)$. The $+3$ option subtracts the constants the wrong way round.""")

# q15
T.single(3, ["radical-plane"],
         r"With $\Sigma = x^2 + y^2 + z^2$, the radical centre of the spheres $\Sigma - 2x - 7 = 0$, $\Sigma - 4y - 5 = 0$, $\Sigma - 6z - 3 = 0$ and $\Sigma - 9 = 0$ is",
         [r"$(1, 1, 1)$", r"$(-1, -1, -1)$", r"$(1, 2, 3)$", r"$(-4, -1, 2)$"],
         r"""Subtract the last sphere from each of the others:
$$-2x + 2 = 0,\quad -4y + 4 = 0,\quad -6z + 6 = 0 \implies (x, y, z) = (1, 1, 1).$$
Check: the power of $(1, 1, 1)$ is $3 - 2 - 7 = 3 - 4 - 5 = 3 - 6 - 3 = 3 - 9 = -6$ for all four. The centres $(1,0,0)$, $(0,2,0)$, $(0,0,3)$, $O$ are non-coplanar, so the radical centre is unique. $(1, 2, 3)$ collects the centres' coordinates; $(-1, -1, -1)$ is a sign slip.""")

# q16
T.single(2, ["orthogonal"], r"The spheres $x^2 + y^2 + z^2 - 2x - 4y - 6z + k = 0$ and $x^2 + y^2 + z^2 + 4x + 2y - 2z + 3 = 0$ cut orthogonally if $k$ equals",
         [r"$-5$", r"$5$", r"$-4$", r"$-7$"],
         r"""Orthogonality: $2(u_1u_2 + v_1v_2 + w_1w_2) = d_1 + d_2$, with $(u_1, v_1, w_1) = (-1, -2, -3)$ and $(u_2, v_2, w_2) = (2, 1, -1)$:
$$2(-2 - 2 + 3) = k + 3 \implies k = -5.$$
Check: $r_1^2 = 14 + 5 = 19$, $r_2^2 = 3$, and the distance between the centres $(1, 2, 3)$, $(-2, -1, 1)$ is $\sqrt{9 + 9 + 4} = \sqrt{22} = \sqrt{19 + 3}$. $k = -4$ drops the factor $2$; $k = 5$ is a sign slip.""")

# q17
T.single(3, ["through-circle", "plane-section"],
         r"The radius of the circle of intersection of the spheres $x^2 + y^2 + z^2 = 16$ and $x^2 + y^2 + z^2 - 6x - 8y + 9 = 0$ is",
         [r"$\dfrac{\sqrt{39}}{2}$", r"$\dfrac52$", r"$\dfrac{\sqrt{89}}{2}$", r"$2\sqrt3$"],
         r"""The plane of the circle is $S_1 - S_2 = 6x + 8y - 25 = 0$. Its distance from $O$ is $\frac{25}{10} = \frac52$, so
$$\rho = \sqrt{16 - \frac{25}{4}} = \frac{\sqrt{39}}{2}.$$
Check by symmetry: the second sphere has centre $(3, 4, 0)$ and radius $4$, equal to the first, so the plane bisects $OC_2$ (length $5$) at distance $\frac52$. $\frac52$ is that distance, not the radius; $\frac{\sqrt{89}}{2}$ adds the squares.""")

# q18
T.single(3, ["given-data", "tangent-plane"], r"The sphere that touches the plane $x + y + z = 3$ at the point $(1, 1, 1)$ and passes through the origin is",
         [r"$x^2 + y^2 + z^2 - x - y - z = 0$", r"$x^2 + y^2 + z^2 - 2x - 2y - 2z = 0$",
          r"$x^2 + y^2 + z^2 - 3x - 3y - 3z + 6 = 0$", r"$x^2 + y^2 + z^2 + x + y + z - 6 = 0$"],
         r"""Point sphere at $(1, 1, 1)$ plus $\lambda$ times the plane:
$$(x - 1)^2 + (y - 1)^2 + (z - 1)^2 + \lambda(x + y + z - 3) = 0.$$
At the origin, $3 - 3\lambda = 0$, so $\lambda = 1$, giving $x^2 + y^2 + z^2 - x - y - z = 0$. Check: centre $\left(\frac12, \frac12, \frac12\right)$, $r = \frac{\sqrt3}{2}$, and its distance to the plane is $\frac{3/2}{\sqrt3} = \frac{\sqrt3}{2}$.

$x^2 + y^2 + z^2 - 2x - 2y - 2z = 0$ passes through $O$ and $(1,1,1)$, but its centre $(1,1,1)$ is on the plane, so it cuts the plane rather than touching it. The $+6$ option ($\lambda = -1$) misses $O$.""")

# q19
T.single(2, ["tangent-plane"], r"The tangent planes to the sphere $x^2 + y^2 + z^2 - 2x - 4y - 6z + 5 = 0$ parallel to the plane $2x - y + 2z = 0$ are",
         [r"$2x - y + 2z + 3 = 0$ and $2x - y + 2z - 15 = 0$", r"$2x - y + 2z - 3 = 0$ and $2x - y + 2z + 15 = 0$",
          r"$2x - y + 2z + 9 = 0$ and $2x - y + 2z - 9 = 0$", r"$2x - y + 2z - 3 = 0$ and $2x - y + 2z - 9 = 0$"],
         r"""Centre $(1, 2, 3)$, radius $\sqrt{14 - 5} = 3$. Write the planes as $2x - y + 2z + k = 0$:
$$\frac{\lvert 2 - 2 + 6 + k\rvert}{3} = 3 \iff \lvert 6 + k\rvert = 9 \iff k = 3 \text{ or } k = -15.$$
$\pm 9$ ignores the centre (correct only for a sphere centred at $O$); $k = -3, -9$ forgets to multiply by $\sqrt{4 + 1 + 4} = 3$; the second option is the sign slip.""")

# q20
T.single(2, ["tangent-plane"], r"The plane $x + 2y + 2z = 14$ touches the sphere $x^2 + y^2 + z^2 + 2x - 2y - 4z - 3 = 0$. The point of contact is",
         [r"$(0, 3, 4)$", r"$(-2, -1, 0)$", r"$(1, 5, 6)$", r"$\left(\dfrac{14}{9}, \dfrac{28}{9}, \dfrac{28}{9}\right)$"],
         r"""The point of contact is the foot of the perpendicular from the centre $(-1, 1, 2)$ (radius $3$). Move along the normal $(1, 2, 2)$:
$$(-1 + t,\ 1 + 2t,\ 2 + 2t):\quad 5 + 9t = 14 \implies t = 1 \implies (0, 3, 4).$$
Check: $0 + 9 + 16 + 0 - 6 - 16 - 3 = 0$, so it is on the sphere. $(-2, -1, 0)$ goes the wrong way ($t = -1$): it is the diametrically opposite point, on the sphere but not on the plane; $\left(\frac{14}{9}, \frac{28}{9}, \frac{28}{9}\right)$ is the foot from the **origin**, not from the centre.""")

# q21
T.single(3, ["orthogonal"], r"The spheres $x^2 + y^2 + z^2 = 4$ and $x^2 + y^2 + z^2 - 6x - 8y + k = 0$ touch each other externally when $k$ equals",
         [r"$16$", r"$-24$", r"$21$", r"$0$"],
         r"""Centres $O$ and $(3, 4, 0)$, so $\delta = 5$; radii $2$ and $\sqrt{25 - k}$. External contact: $\delta = r_1 + r_2$:
$$2 + \sqrt{25 - k} = 5 \implies 25 - k = 9 \implies k = 16.$$
$k = -24$ gives $r_2 = 7 = 5 + 2$: **internal** contact ($\delta = r_2 - r_1$). $k = 21$ gives equal radii $2$, which do not meet; $k = 0$ gives $r_2 = 5$, which passes through the other centre.""")

# ---------------------------------------------------------------- statements (2)
T.statements(2, ["plane-section", "radical-plane"], r"Consider the following statements:",
             [r"A plane at distance $\delta$ from the centre of a sphere of radius $r$ $(0 < \delta < r)$ cuts it in a circle of radius $r - \delta$.",
              r"The radical plane of two non-concentric spheres is perpendicular to the line joining their centres.",
              r"The centre of the circle $x^2 + y^2 + z^2 = 25$, $x + 2y + 2z = 9$ is $(1, 2, 2)$."],
             [r"2 and 3 only", r"3 only", r"1 and 2 only", r"1, 2 and 3"],
             r"""1. False: the radius is $\sqrt{r^2 - \delta^2}$ (Pythagoras), not $r - \delta$. For $r = 5$, $\delta = 3$ it is $4$, not $2$.
2. True: $S_1 - S_2 = 0$ has normal $(u_1 - u_2, v_1 - v_2, w_1 - w_2)$, which is the direction of the line of centres $(-u_1, -v_1, -w_1) \to (-u_2, -v_2, -w_2)$.
3. True: the foot of the perpendicular from $O$ is $t(1, 2, 2)$ with $9t = 9$, i.e. $(1, 2, 2)$, and it lies on the plane.""")

T.statements(3, ["orthogonal"], r"Consider the following statements:",
             [r"Two spheres with radii $r_1, r_2$ and centres a distance $\delta$ apart cut orthogonally if and only if $\delta^2 = r_1^2 + r_2^2$.",
              r"If two spheres cut orthogonally, the power of the centre of the first with respect to the second equals the square of the radius of the first.",
              r"The spheres $x^2 + y^2 + z^2 = 9$ and $x^2 + y^2 + z^2 - 8x + 7 = 0$ cut orthogonally."],
             [r"1 and 2 only", r"1 only", r"2 and 3 only", r"1, 2 and 3"],
             r"""1. True: at a common point $Q$ the radii $C_1Q$, $C_2Q$ are normals to the two tangent planes; they are perpendicular iff $\delta^2 = r_1^2 + r_2^2$ (Pythagoras).
2. True: the power of $C_1$ with respect to $S_2$ is $\delta^2 - r_2^2 = r_1^2$.
3. False: centres $O$ and $(4, 0, 0)$, radii $3$ and $\sqrt{16 - 7} = 3$, so $r_1^2 + r_2^2 = 18 \ne 16 = \delta^2$. In coefficient form, $2(0) = 0 \ne d_1 + d_2 = -9 + 7 = -2$.""")

# ---------------------------------------------------------------- match (2)
T.match(1, ["given-data", "tangent-plane", "radical-plane", "through-circle"],
        r"Here $S \equiv x^2 + y^2 + z^2 + 2ux + 2vy + 2wz + d$, and $S_1 = 0$, $S_2 = 0$ are spheres in this standard form. Match each item in List I with its equation in List II.",
        [r"Sphere on the diameter joining $(x_1, y_1, z_1)$ and $(x_2, y_2, z_2)$",
         r"Tangent plane to $S = 0$ at its point $(x_1, y_1, z_1)$",
         r"Radical plane of $S_1 = 0$ and $S_2 = 0$",
         r"A sphere through the circle $S = 0$, $P = 0$"],
        [r"$S + \lambda P = 0$", r"$(x - x_1)(x - x_2) + (y - y_1)(y - y_2) + (z - z_1)(z - z_2) = 0$",
         r"$S_1 - S_2 = 0$", r"$xx_1 + yy_1 + zz_1 + u(x + x_1) + v(y + y_1) + w(z + z_1) + d = 0$"],
        [r"A-2, B-4, C-3, D-1", r"A-2, B-4, C-1, D-3", r"A-4, B-2, C-3, D-1", r"A-2, B-3, C-4, D-1"],
        r"""- A: $\angle APB = \frac\pi2$ on a diameter, i.e. $\vec{PA}\cdot\vec{PB} = 0$: 2.
- B: $T = 0$: 4.
- C: equal powers, $S_1 = S_2$: 3.
- D: $S + \lambda P$ vanishes wherever $S = 0$ and $P = 0$: 1.

Swapping C and D confuses the two linear-combination ideas: $S_1 - S_2$ is a plane, $S + \lambda P$ is a sphere.""")

T.match(3, ["radical-plane", "plane-section"],
        r"For the sphere $S \equiv x^2 + y^2 + z^2 - 2x - 4y + 4z - 16 = 0$, match each quantity in List I with its value in List II.",
        [r"Power of the origin with respect to $S$", r"Square of the length of the tangent from $(1, 2, 8)$",
         r"Radius of the circle cut by the plane $z = 1$", r"Largest $k$ for which the plane $z = k$ meets $S$"],
        [r"$3$", r"$4$", r"$-16$", r"$75$"],
        [r"A-3, B-4, C-2, D-1", r"A-3, B-4, C-1, D-2", r"A-4, B-3, C-2, D-1", r"A-3, B-2, C-4, D-1"],
        r"""The centre is $(1, 2, -2)$ and the radius is $\sqrt{1 + 4 + 4 + 16} = 5$.
- A: $S(0, 0, 0) = -16$ (negative: the origin is inside): 3.
- B: $S(1, 2, 8) = 1 + 4 + 64 - 2 - 8 + 32 - 16 = 75$; equivalently $CP^2 - r^2 = 100 - 25$: 4.
- C: the plane $z = 1$ is at distance $3$ from the centre, so the radius is $\sqrt{25 - 9} = 4$: 2.
- D: $z$ ranges over $[-2 - 5, -2 + 5]$, so the largest $k$ is $3$: 1.

Swapping C and D confuses the section radius $4$ with the top height $3$.""")

# ---------------------------------------------------------------- assertion-reason (5)
T.assertion_reason(1, ["general-equation"],
                   r"The equation $x^2 + y^2 + z^2 - 2x + 4y - 6z + 14 = 0$ is satisfied by exactly one real point.",
                   r"The sphere $x^2 + y^2 + z^2 + 2ux + 2vy + 2wz + d = 0$ has centre $(-u, -v, -w)$ and radius $\sqrt{u^2 + v^2 + w^2 - d}$.",
                   0,
                   r"""R is the standard result: complete the squares. For the equation in A, $u^2 + v^2 + w^2 - d = 1 + 4 + 9 - 14 = 0$, so
$$(x - 1)^2 + (y + 2)^2 + (z - 3)^2 = 0,$$
which holds only at $(1, -2, 3)$: a point sphere. A is true, and R gives exactly this radius computation, so R explains A.""")

T.assertion_reason(1, ["tangent-plane"],
                   r"The tangent plane to $x^2 + y^2 + z^2 = a^2$ at its point $(x_1, y_1, z_1)$ is $xx_1 + yy_1 + zz_1 = a^2$.",
                   r"The tangent plane at a point of a sphere is parallel to the radius through that point.",
                   2,
                   r"""A is true: the plane through $(x_1, y_1, z_1)$ with normal $(x_1, y_1, z_1)$ is $x_1(x - x_1) + y_1(y - y_1) + z_1(z - z_1) = 0$, i.e. $xx_1 + yy_1 + zz_1 = x_1^2 + y_1^2 + z_1^2 = a^2$.

R is false: the tangent plane is **perpendicular** to the radius at the point of contact. The radius is its normal.""")

T.assertion_reason(2, ["tangent-plane"],
                   r"The plane $2x - y + 2z = 3$ touches the sphere $x^2 + y^2 + z^2 = 9$.",
                   r"A plane touches a sphere if and only if the perpendicular distance of the centre from the plane equals the radius.",
                   3,
                   r"""R is the standard condition of tangency, true. Apply it to A: the distance from $O$ is
$$\frac{\lvert -3\rvert}{\sqrt{4 + 1 + 4}} = 1 \ne 3,$$
so the plane cuts the sphere in a circle of radius $\sqrt{9 - 1} = 2\sqrt2$. A is false. (Comparing $3$ with the radius without dividing by $\sqrt{l^2 + m^2 + n^2}$ is the trap.) The tangent planes in this direction are $2x - y + 2z = \pm 9$.""")

T.assertion_reason(2, ["orthogonal", "radical-plane"],
                   r"The spheres $x^2 + y^2 + z^2 = 4$ and $x^2 + y^2 + z^2 - 6x + 4 = 0$ cut orthogonally.",
                   r"The radical plane of these two spheres is $x = \dfrac43$.",
                   1,
                   r"""A: here $(u_1, v_1, w_1) = (0, 0, 0)$, $d_1 = -4$ and $(u_2, v_2, w_2) = (-3, 0, 0)$, $d_2 = 4$. Then $2(u_1u_2 + v_1v_2 + w_1w_2) = 0 = d_1 + d_2$: orthogonal. Geometrically, $r_1^2 + r_2^2 = 4 + 5 = 9 = \delta^2$. A is true.

R: $S_1 - S_2 = 6x - 8 = 0$, i.e. $x = \frac43$. True. But the position of the radical plane says nothing about the angle between the spheres, so R does not explain A.""")

T.assertion_reason(3, ["through-circle", "plane-section"],
                   r"Every sphere through the circle $x^2 + y^2 + z^2 = 9$, $z = 0$ has its centre on the $z$-axis.",
                   r"The line joining the centre of a sphere to the centre of any of its plane sections is perpendicular to the plane of the section.",
                   0,
                   r"""R is true: the centre of a section is the foot of the perpendicular from the centre of the sphere.

For A, every sphere through the circle has the circle as a plane section, with section centre $O$ and section plane $z = 0$. By R its centre lies on the normal to $z = 0$ through $O$: the $z$-axis. Directly: $x^2 + y^2 + z^2 - 9 + \lambda z = 0$ has centre $\left(0, 0, -\frac\lambda2\right)$. Both true, and R explains A.""")


def check():
    import sympy as sp
    x, y, z, t, lam, k = sp.symbols("x y z t lambda k", real=True)
    X = sp.Matrix([x, y, z])
    Sig = x**2 + y**2 + z**2

    def cr(S):
        """centre and r^2 of a standard-form sphere."""
        P = sp.Poly(sp.expand(S), x, y, z)
        assert P.coeff_monomial(x**2) == P.coeff_monomial(y**2) == P.coeff_monomial(z**2) == 1
        assert P.coeff_monomial(x * y) == P.coeff_monomial(y * z) == P.coeff_monomial(x * z) == 0
        u, v, w = [P.coeff_monomial(s) / 2 for s in (x, y, z)]
        d = P.coeff_monomial(1)
        return sp.Matrix([-u, -v, -w]), u**2 + v**2 + w**2 - d

    def dist(pt, plane):
        P = sp.Poly(plane, x, y, z)
        n = sp.Matrix([P.coeff_monomial(s) for s in (x, y, z)])
        return sp.Abs(plane.subs(dict(zip((x, y, z), pt)))) / sp.sqrt(n.dot(n))

    def at(E, pt):
        return E.subs(dict(zip((x, y, z), pt)))

    def same(E1, E2):
        """E1 = c*E2 for some nonzero constant."""
        P1, P2 = sp.Poly(sp.expand(E1), x, y, z), sp.Poly(sp.expand(E2), x, y, z)
        c = P1.LC() / P2.LC()
        return sp.expand(E1 - c * E2) == 0

    def tangent(S, p):
        g = sp.Matrix([sp.diff(S, s) for s in (x, y, z)]).subs(dict(zip((x, y, z), p)))
        return g.dot(X - sp.Matrix(p))

    # q1
    C, r2 = cr(Sig - 2 * x + 4 * y - 6 * z - 11)
    assert list(C) == [1, -2, 3]; eq(sp.sqrt(r2), 5, "q1")
    # q2
    S2 = sp.expand((x - 1) * (x - 3) + (y - 2) * (y + 2) + (z - 3) * (z - 1))
    assert sp.expand(S2 - (Sig - 4 * x - 4 * z + 2)) == 0
    C, r2 = cr(S2); eq(r2, sp.Rational(24, 4), "q2 r")
    assert at(S2, (1, 2, 3)) == 0 and at(S2, (3, -2, 1)) == 0
    # q3: a=b=c, f=g=h=0 -> sphere form; cross term -> cylinder (contains the whole line x=-y, z=±1? no: z^2 + (x+y)^2 = 1)
    cyl = Sig + 2 * x * y - 1
    assert sp.expand(cyl - ((x + y)**2 + z**2 - 1)) == 0
    assert at(cyl, (t, -t, 1)) == 0  # unbounded set of points: not a sphere
    # q4
    u, v, w, d = sp.symbols("u v w d")
    G = Sig + 2 * u * x + 2 * v * y + 2 * w * z + d
    sol = sp.solve([at(G, p) for p in [(0, 0, 0), (2, 0, 0), (0, 4, 0), (0, 0, 6)]], [u, v, w, d], dict=True)[0]
    C, r2 = cr(G.subs(sol)); eq(sp.sqrt(r2), sp.sqrt(14), "q4")
    # q5
    Pl = x + 2 * y + 2 * z - 9
    eq(dist((0, 0, 0), Pl), 3, "q5 d"); eq(sp.sqrt(25 - 9), 4, "q5 r")
    ts = sp.solve(at(Pl, (t, 2 * t, 2 * t)), t); assert ts == [1]
    # q6
    C, r2 = cr(Sig - 2 * y - 4 * z - 11)
    dd = dist(list(C), x + 2 * y + 2 * z - 15)
    eq(sp.sqrt(r2 - dd**2), sp.sqrt(7), "q6")
    # q7
    fam = Sig - 9 + lam * (2 * x + 3 * y + 4 * z - 5)
    l7 = sp.solve(at(fam, (0, 0, 0)), lam)[0]; eq(l7, sp.Rational(-9, 5), "q7 lam")
    assert sp.expand(5 * fam.subs(lam, l7) - (5 * Sig - 18 * x - 27 * y - 36 * z)) == 0
    # q8
    fam = Sig - 25 + lam * (x + y + z - 3)
    Cl, _ = cr(fam)
    l8 = sp.solve(sum(Cl) - 3, lam)[0]; eq(l8, -2, "q8 lam")
    S8 = sp.expand(fam.subs(lam, l8)); assert sp.expand(S8 - (Sig - 2 * x - 2 * y - 2 * z - 19)) == 0
    C, r2 = cr(S8); eq(r2, 22, "q8 r"); eq(25 - dist((0, 0, 0), x + y + z - 3)**2, 22, "q8 circle")
    # q9
    assert same(tangent(Sig - 14, (1, 2, 3)), x + 2 * y + 3 * z - 14)
    # q10
    S10 = Sig + 2 * x - 4 * y + 2 * z - 3
    assert at(S10, (1, 1, 1)) == 0
    assert same(tangent(S10, (1, 1, 1)), 2 * x - y + 2 * z - 3)
    # q11
    C, r2 = cr(Sig - 2 * x - 4 * y + 2 * z - 3)
    ks = sp.solve(sp.Eq(at(2 * x - y + 2 * z - k, list(C))**2, 9 * r2), k)
    assert set(ks) == {7, -11}, ks
    # q12: derive generically and test distractors numerically
    l, m, n, p = sp.symbols("l m n p")
    Cg = (-u, -v, -w)
    lhs = (l * Cg[0] + m * Cg[1] + n * Cg[2] - p)**2
    rhs = (l**2 + m**2 + n**2) * (u**2 + v**2 + w**2 - d)
    assert sp.expand(lhs - (u * l + v * m + w * n + p)**2) == 0
    # numeric: sphere centre (1,2,-1) r=3 (u,v,w,d)=(-1,-2,1,-3), plane 2x-y+2z=7 tangent
    vals = {u: -1, v: -2, w: 1, d: -3, l: 2, m: -1, n: 2, p: 7}
    assert (lhs - rhs).subs(vals) == 0
    assert (((u * l + v * m + w * n - p)**2) - rhs).subs(vals) != 0
    assert (((u * l + v * m + w * n + p)**2) - (l**2 + m**2 + n**2) * (u**2 + v**2 + w**2 + d)).subs(vals) != 0
    # q13
    S13 = Sig - 2 * x + 4 * y - 6 * z + 5
    eq(sp.sqrt(at(S13, (1, 1, 1))), 2, "q13")
    C, r2 = cr(S13); eq((sp.Matrix([1, 1, 1]) - C).dot(sp.Matrix([1, 1, 1]) - C) - r2, 4, "q13 b")
    # q14
    A14, B14 = Sig + 2 * x + 2 * y + 2 * z - 2, Sig - 4 * x + 6 * y + 4
    assert same(sp.expand(A14 - B14), 3 * x - 2 * y + z - 3)
    # q15
    Ss = [Sig - 2 * x - 7, Sig - 4 * y - 5, Sig - 6 * z - 3, Sig - 9]
    sol = sp.solve([sp.expand(Ss[i] - Ss[3]) for i in range(3)], [x, y, z], dict=True)
    assert sol == [{x: 1, y: 1, z: 1}]
    assert len({at(S, (1, 1, 1)) for S in Ss}) == 1
    cens = [cr(S)[0] for S in Ss]
    assert sp.Matrix.hstack(*[c - cens[3] for c in cens[:3]]).det() != 0
    # q16
    kk = sp.symbols("kk")
    A16, B16 = Sig - 2 * x - 4 * y - 6 * z + kk, Sig + 4 * x + 2 * y - 2 * z + 3
    (C1, r1), (C2, r22) = cr(A16), cr(B16)
    k16 = sp.solve(sp.Eq((C1 - C2).dot(C1 - C2), r1 + r22), kk); assert k16 == [-5], k16
    assert r1.subs(kk, -5) > 0 and r22 > 0
    # q17
    A17, B17 = Sig - 16, Sig - 6 * x - 8 * y + 9
    pl = sp.expand(A17 - B17)
    eq(sp.sqrt(16 - dist((0, 0, 0), pl)**2), sp.sqrt(39) / 2, "q17")
    # cross-check: actual intersection points at y = 0 slice
    pts = sp.solve([A17, B17, z], [x, y, z], dict=True)
    assert len(pts) == 2
    eq(sp.sqrt(((sp.Matrix([pts[0][x], pts[0][y], 0]) - sp.Matrix([pts[1][x], pts[1][y], 0])).norm() / 2)**2), sp.sqrt(39) / 2, "q17 chord")
    # q18
    fam = (x - 1)**2 + (y - 1)**2 + (z - 1)**2 + lam * (x + y + z - 3)
    l18 = sp.solve(at(fam, (0, 0, 0)), lam)[0]; eq(l18, 1, "q18")
    S18 = sp.expand(fam.subs(lam, l18)); assert sp.expand(S18 - (Sig - x - y - z)) == 0
    C, r2 = cr(S18); eq(dist(list(C), x + y + z - 3)**2, r2, "q18 tangency")
    C, r2 = cr(Sig - 2 * x - 2 * y - 2 * z); assert dist(list(C), x + y + z - 3) == 0  # distractor cuts
    # q19
    C, r2 = cr(Sig - 2 * x - 4 * y - 6 * z + 5); eq(r2, 9, "q19 r")
    ks = sp.solve(sp.Eq(at(2 * x - y + 2 * z + k, list(C))**2, 9 * r2), k); assert set(ks) == {3, -15}, ks
    # q20
    S20 = Sig + 2 * x - 2 * y - 4 * z - 3
    C, r2 = cr(S20); eq(r2, 9, "q20 r")
    P20 = x + 2 * y + 2 * z - 14
    eq(dist(list(C), P20)**2, r2, "q20 tangent")
    sol = sp.solve([S20, P20], [x, y, z], dict=True)
    assert all(s == {x: 0, y: 3, z: 4} for s in sol if all(v.is_real for v in s.values()))
    assert at(S20, (0, 3, 4)) == 0 and at(P20, (0, 3, 4)) == 0
    for wrong in [(-2, -1, 0), (1, 5, 6), (sp.Rational(14, 9), sp.Rational(28, 9), sp.Rational(28, 9))]:
        assert at(S20, wrong) != 0 or at(P20, wrong) != 0
    assert at(P20, (-2, -1, 0)) != 0 and at(S20, (-2, -1, 0)) == 0  # antipodal point
    # q21
    k21 = sp.solve(sp.Eq(2 + sp.sqrt(25 - kk), 5), kk); assert k21 == [16]
    assert sp.solve(sp.Eq(sp.sqrt(25 - kk) - 2, 5), kk) == [-24]

    # statements 1
    eq(sp.sqrt(5**2 - 3**2), 4, "S1.1"); assert 5 - 3 != 4
    u1, v1, w1, d1, u2, v2, w2, d2 = sp.symbols("u1 v1 w1 d1 u2 v2 w2 d2")
    rp = sp.expand((Sig + 2 * u1 * x + 2 * v1 * y + 2 * w1 * z + d1) - (Sig + 2 * u2 * x + 2 * v2 * y + 2 * w2 * z + d2))
    nrm = sp.Matrix([rp.coeff(s) for s in (x, y, z)])
    linec = sp.Matrix([-u2 + u1, -v2 + v1, -w2 + w1])
    assert sp.simplify(nrm.cross(linec)) == sp.zeros(3, 1)
    assert at(x + 2 * y + 2 * z - 9, (1, 2, 2)) == 0
    # statements 2: identity d^2 - r1^2 - r2^2 = -(2 sum u1u2 - d1 - d2)
    dd2 = (u1 - u2)**2 + (v1 - v2)**2 + (w1 - w2)**2
    r1s, r2s = u1**2 + v1**2 + w1**2 - d1, u2**2 + v2**2 + w2**2 - d2
    assert sp.expand(dd2 - r1s - r2s + 2 * (u1 * u2 + v1 * v2 + w1 * w2) - d1 - d2) == 0
    assert sp.expand((dd2 - r2s).subs(d1, sp.solve(dd2 - r1s - r2s, d1)[0]) - r1s.subs(d1, sp.solve(dd2 - r1s - r2s, d1)[0])) == 0
    (C1, r1), (C2, r22) = cr(Sig - 9), cr(Sig - 8 * x + 7)
    assert (C1 - C2).dot(C1 - C2) != r1 + r22
    # match 1: diameter form, tangent plane, radical plane linear, S + lam P contains circle
    x1, y1, z1, x2, y2, z2 = sp.symbols("x1 y1 z1 x2 y2 z2")
    D = (x - x1) * (x - x2) + (y - y1) * (y - y2) + (z - z1) * (z - z2)
    Cd, rd = cr(D)
    assert sp.simplify(Cd - sp.Matrix([(x1 + x2) / 2, (y1 + y2) / 2, (z1 + z2) / 2])) == sp.zeros(3, 1)
    assert sp.simplify(4 * rd - ((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)) == 0
    Sg = Sig + 2 * u * x + 2 * v * y + 2 * w * z + d
    Tg = x * x1 + y * y1 + z * z1 + u * (x + x1) + v * (y + y1) + w * (z + z1) + d
    grad = sp.Matrix([sp.diff(Sg, s) for s in (x, y, z)]).subs({x: x1, y: y1, z: z1})
    # Tg - Sg(x1) is (1/2) grad . (X - X1)
    assert sp.expand(Tg - at(Sg, (x1, y1, z1)) - grad.dot(X - sp.Matrix([x1, y1, z1])) / 2) == 0
    assert sp.Poly(rp, x, y, z).total_degree() == 1
    # match 2
    S = Sig - 2 * x - 4 * y + 4 * z - 16
    C, r2 = cr(S); eq(r2, 25, "M2 r")
    eq(at(S, (0, 0, 0)), -16, "M2 A"); eq(at(S, (1, 2, 8)), 75, "M2 B")
    eq(sp.sqrt(r2 - dist(list(C), z - 1)**2), 4, "M2 C")
    zs = sp.solve(S.subs({x: 1, y: 2}), z); eq(max(zs), 3, "M2 D")

    # AR1
    C, r2 = cr(Sig - 2 * x + 4 * y - 6 * z + 14); eq(r2, 0, "AR1")
    assert sp.expand(Sig - 2 * x + 4 * y - 6 * z + 14 - ((x - 1)**2 + (y + 2)**2 + (z - 3)**2)) == 0
    # AR2: normal of tangent plane is parallel to radius (so R false)
    assert same(tangent(Sig - 14, (1, 2, 3)), x + 2 * y + 3 * z - 14)
    # AR3
    eq(dist((0, 0, 0), 2 * x - y + 2 * z - 3), 1, "AR3")
    # AR4
    (C1, r1), (C2, r22) = cr(Sig - 4), cr(Sig - 6 * x + 4)
    eq((C1 - C2).dot(C1 - C2), r1 + r22, "AR4 A")
    assert sp.solve(sp.expand((Sig - 4) - (Sig - 6 * x + 4)), x) == [sp.Rational(4, 3)]
    # AR5
    C, _ = cr(Sig - 9 + lam * z); assert C[0] == 0 and C[1] == 0


T.write(check)
