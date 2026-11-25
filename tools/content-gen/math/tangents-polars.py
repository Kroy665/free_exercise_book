import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from qlib import Topic, eq

T = Topic("math.geometry.tangents-polars")

# ---------------------------------------------------------------- single (21)
# q1
T.single(1, ["tangency"], r"The tangent to the circle $x^2 + y^2 = 25$ at the point $(3, 4)$ is",
         [r"$3x + 4y = 25$", r"$4x + 3y = 25$", r"$3x - 4y = 25$", r"$3x + 4y = 5$"],
         r"""Use $T = 0$: replace $x^2$ by $3x$ and $y^2$ by $4y$:
$$3x + 4y = 25.$$
Check: $(3, 4)$ gives $9 + 16 = 25$. $4x + 3y = 25$ swaps the coordinates: it is the tangent at $(4, 3)$ and does not pass through $(3,4)$. $3x + 4y = 5$ uses the radius instead of $a^2$.""")

# q2
T.single(1, ["tangency"], r"The line $y = x + c$ touches the ellipse $\dfrac{x^2}{9} + \dfrac{y^2}{4} = 1$ if and only if",
         [r"$c = \pm\sqrt{13}$", r"$c = \pm\sqrt5$", r"$c = \pm 13$", r"$c = \pm 5$"],
         r"""For the ellipse the condition is $c^2 = a^2m^2 + b^2$. Here $a^2 = 9$, $b^2 = 4$, $m = 1$:
$$c^2 = 9 + 4 = 13,\qquad c = \pm\sqrt{13}.$$
$\pm\sqrt5$ comes from the hyperbola condition $c^2 = a^2m^2 - b^2$; $\pm 13$ forgets the square root.""")

# q3
T.single(1, ["tangency"], r"The tangent to the parabola $y^2 = 8x$ with slope $2$ is",
         [r"$y = 2x + 1$", r"$y = 2x + 4$", r"$y = 2x - 1$", r"$y = 2x + \dfrac12$"],
         r"""Here $4a = 8$, so $a = 2$. The tangent of slope $m$ is $y = mx + \frac am$:
$$y = 2x + \frac22 = 2x + 1.$$
Check by substitution: $(2x + 1)^2 = 8x \iff 4x^2 - 4x + 1 = 0 \iff (2x - 1)^2 = 0$, a double root. $y = 2x + 4$ uses $am$ instead of $\frac am$.""")

# q4
T.single(2, ["tangency"], r"The line $3x + 4y = k$ touches the circle $x^2 + y^2 - 2x - 4y - 4 = 0$ for",
         [r"$k = 26$ or $k = -4$", r"$k = 4$ or $k = -26$", r"$k = 15$ or $k = -15$", r"$k = 11$ only"],
         r"""The centre is $(1, 2)$ and the radius is $\sqrt{1 + 4 + 4} = 3$. Tangency means distance from the centre = radius:
$$\frac{\lvert 3 + 8 - k\rvert}{5} = 3 \iff \lvert 11 - k\rvert = 15 \iff k = 26 \text{ or } k = -4.$$
$k = \pm 15$ is the answer for a circle centred at the origin; $k = 11$ is the line through the centre.""")

# q5
T.single(2, ["tangency"], r"The line $lx + my + n = 0$ touches the parabola $y^2 = 4ax$ $(a \ne 0,\ l \ne 0)$ if and only if",
         [r"$ln = am^2$", r"$mn = al^2$", r"$ln + am^2 = 0$", r"$n^2 = a(l^2 + m^2)$"],
         r"""Put $x = -\frac{my + n}{l}$ into $y^2 = 4ax$:
$$ly^2 + 4amy + 4an = 0.$$
Tangency means a double root: $16a^2m^2 - 16aln = 0$, i.e. $ln = am^2$.

Check with $y = mx + \frac am$, i.e. $mx - y + \frac am = 0$: $l = m$, $m \to -1$, $n = \frac am$, and $ln = a = a\cdot(-1)^2$. The sign-flipped option fails this check.""")

# q6
T.single(2, ["normals"], r"The normal to the parabola $y^2 = 4ax$ with slope $m$ is",
         [r"$y = mx - 2am - am^3$", r"$y = mx + 2am + am^3$", r"$y = mx - am - 2am^3$", r"$y = mx + \dfrac am$"],
         r"""The normal at $(at^2, 2at)$ is $y + tx = 2at + at^3$, of slope $-t$. Put $t = -m$:
$$y - mx = -2am - am^3 \implies y = mx - 2am - am^3,$$
with foot $(am^2, -2am)$. Check: $(am^2, -2am)$ satisfies it, since $am^3 - 2am - am^3 = -2am$. The option $y = mx + \frac am$ is the **tangent** of slope $m$.""")

# q7
T.single(2, ["normals"], r"The number of normals that can be drawn from the point $(5, 0)$ to the parabola $y^2 = 4x$ is",
         [r"$3$", r"$1$", r"$2$", r"$4$"],
         r"""With $a = 1$, the normal $y = mx - 2m - m^3$ passes through $(5, 0)$ iff
$$0 = 5m - 2m - m^3 \iff m(m^2 - 3) = 0 \iff m = 0, \pm\sqrt3.$$
Three real normals: the axis $y = 0$ and $y = \pm\sqrt3(x - 5)$. In general $(h, 0)$ gives three normals iff $h > 2a$; here $5 > 2$. Four is the bound for an ellipse, not a parabola.""")

# q8
T.single(2, ["pair-of-tangents"], r"The angle between the two tangents drawn from $(4, 0)$ to the circle $x^2 + y^2 = 4$ is",
         [r"$\dfrac{\pi}{3}$", r"$\dfrac{\pi}{6}$", r"$\dfrac{\pi}{2}$", r"$\dfrac{2\pi}{3}$"],
         r"""Distance to the centre $d = 4$, radius $2$. The half-angle $\alpha$ satisfies
$$\sin\alpha = \frac{2}{4} = \frac12 \implies \alpha = \frac{\pi}{6},$$
so the tangents meet at $2\alpha = \frac{\pi}{3}$. $\frac\pi6$ is only the half-angle. $\frac\pi2$ would need $d^2 = 2r^2 = 8$ (the director circle).""")

# q9
T.single(1, ["tangency"], r"The tangent to the ellipse $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$ at the point $(a\cos\theta, b\sin\theta)$ is",
         [r"$\dfrac{x\cos\theta}{a} + \dfrac{y\sin\theta}{b} = 1$", r"$\dfrac{x\cos\theta}{a} - \dfrac{y\sin\theta}{b} = 1$",
          r"$ax\sec\theta - by\csc\theta = a^2 - b^2$", r"$\dfrac{x\sec\theta}{a} - \dfrac{y\tan\theta}{b} = 1$"],
         r"""Put $x_1 = a\cos\theta$, $y_1 = b\sin\theta$ into $\frac{xx_1}{a^2} + \frac{yy_1}{b^2} = 1$:
$$\frac{x\cos\theta}{a} + \frac{y\sin\theta}{b} = 1.$$
$ax\sec\theta - by\csc\theta = a^2 - b^2$ is the **normal** at the same point, and $\frac{x\sec\theta}{a} - \frac{y\tan\theta}{b} = 1$ is the hyperbola's tangent.""")

# q10
T.single(1, ["chord-of-contact"], r"The chord of contact of the tangents from $(2, 3)$ to the circle $x^2 + y^2 = 4$ is",
         [r"$2x + 3y = 4$", r"$3x + 2y = 4$", r"$2x + 3y = 13$", r"$2x - 3y = 4$"],
         r"""The chord of contact is $T = 0$: $2x + 3y = 4$. ($S_1 = 9 > 0$, so $(2,3)$ is outside and two real tangents exist.)

$2x + 3y = 13$ is the chord **bisected** at $(2,3)$ ($T = S_1$ gives $2x + 3y - 4 = 9$); it is parallel to the chord of contact but different.""")

# q11
T.single(2, ["chord-of-contact"], r"The equation of the chord of the ellipse $\dfrac{x^2}{16} + \dfrac{y^2}{9} = 1$ whose midpoint is $(2, 1)$ is",
         [r"$9x + 8y = 26$", r"$9x + 8y = 72$", r"$8x + 9y = 25$", r"$9x - 8y = 10$"],
         r"""Use $T = S_1$:
$$\frac{2x}{16} + \frac{y}{9} - 1 = \frac{4}{16} + \frac19 - 1 \iff \frac x8 + \frac y9 = \frac{13}{36}.$$
Multiply by $72$: $9x + 8y = 26$. Check: $(2,1)$ gives $18 + 8 = 26$.

$9x + 8y = 72$ is $T = 0$, the polar of $(2, 1)$; it is parallel to the answer but does not pass through $(2,1)$.""")

# q12
T.single(2, ["poles-polars"], r"The pole of the line $2x + 3y = 6$ with respect to the ellipse $\dfrac{x^2}{9} + \dfrac{y^2}{4} = 1$ is",
         [r"$(3, 2)$", r"$(2, 3)$", r"$\left(\dfrac13, \dfrac12\right)$", r"$\left(\dfrac{2}{3}, \dfrac{3}{2}\right)$"],
         r"""The polar of $(h, k)$ is $\frac{hx}{9} + \frac{ky}{4} = 1$. The given line is $\frac x3 + \frac y2 = 1$. Comparing:
$$\frac h9 = \frac13,\quad \frac k4 = \frac12 \implies (h, k) = (3, 2).$$
Check with the table: $\left(-\frac{a^2l}{n}, -\frac{b^2m}{n}\right) = \left(-\frac{9\cdot2}{-6}, -\frac{4\cdot3}{-6}\right) = (3, 2)$. $\left(\frac13, \frac12\right)$ forgets to multiply by $a^2, b^2$.""")

# q13
T.single(2, ["poles-polars"], r"The pole of the line $lx + my + n = 0$ $(l \ne 0)$ with respect to the parabola $y^2 = 4ax$ is",
         [r"$\left(\dfrac nl, -\dfrac{2am}{l}\right)$", r"$\left(-\dfrac nl, \dfrac{2am}{l}\right)$",
          r"$\left(\dfrac nl, \dfrac{2am}{l}\right)$", r"$\left(-\dfrac{2an}{l}, -\dfrac ml\right)$"],
         r"""The polar of $(h, k)$ is $ky = 2a(x + h)$, i.e. $2ax - ky + 2ah = 0$. Compare with $lx + my + n = 0$:
$$\frac{2a}{l} = \frac{-k}{m} = \frac{2ah}{n} \implies h = \frac nl,\quad k = -\frac{2am}{l}.$$
Check: the tangent at the vertex $x = 0$ ($l = 1, m = 0, n = 0$) has pole $(0, 0)$, the vertex itself. The directrix $x + a = 0$ has pole $(a, 0)$, the focus. The sign-flipped option gives $(-a, 0)$ there.""")

# q14
T.single(1, ["chord-of-contact"], r"The length of the tangent from $(5, 3)$ to the circle $x^2 + y^2 - 4x + 2y - 4 = 0$ is",
         [r"$4$", r"$16$", r"$2$", r"$6$"],
         r"""$L = \sqrt{S_1}$:
$$S_1 = 25 + 9 - 20 + 6 - 4 = 16,\qquad L = 4.$$
$16$ is $L^2$. Check: centre $(2, -1)$, radius $3$, distance $5$; $L = \sqrt{25 - 9} = 4$.""")

# q15
T.single(3, ["chord-of-contact"], r"Tangents are drawn from $(4, 3)$ to the circle $x^2 + y^2 = 9$. The length of the chord of contact is",
         [r"$\dfrac{24}{5}$", r"$\dfrac{12}{5}$", r"$5$", r"$\dfrac{16}{5}$"],
         r"""$L = \sqrt{16 + 9 - 9} = 4$, $r = 3$, $d = 5$. The chord is
$$\frac{2rL}{\sqrt{r^2 + L^2}} = \frac{2\cdot3\cdot4}{5} = \frac{24}{5}.$$
Directly: the chord $4x + 3y = 9$ is at distance $\frac95$ from $O$, so its half-length is $\sqrt{9 - \frac{81}{25}} = \frac{12}{5}$. The option $\frac{12}{5}$ is only the half-chord.""")

# q16
T.single(3, ["poles-polars"], r"The locus of the poles, with respect to the circle $x^2 + y^2 = b^2$, of the tangents to the circle $x^2 + y^2 = a^2$ $(a, b > 0)$ is",
         [r"$x^2 + y^2 = \dfrac{b^4}{a^2}$", r"$x^2 + y^2 = \dfrac{a^4}{b^2}$", r"$x^2 + y^2 = ab$", r"$x^2 + y^2 = \dfrac{b^2}{a}$"],
         r"""The polar of $(h, k)$ with respect to $x^2 + y^2 = b^2$ is $hx + ky = b^2$. It touches $x^2 + y^2 = a^2$ iff its distance from $O$ is $a$:
$$\frac{b^2}{\sqrt{h^2 + k^2}} = a \iff h^2 + k^2 = \frac{b^4}{a^2}.$$
Check with $a = b$: the poles of tangents to a circle with respect to itself are the points of contact, on the same circle; $\frac{b^4}{a^2} = a^2$. The option $\frac{a^4}{b^2}$ swaps the roles of the circles.""")

# q17
T.single(3, ["poles-polars", "normals"], r"The locus of the poles of normal chords of the parabola $y^2 = 4ax$ $(a > 0)$ is",
         [r"$(x + 2a)y^2 + 4a^3 = 0$", r"$(x - 2a)y^2 + 4a^3 = 0$", r"$(x + 2a)y^2 = 4a^3$", r"$(x + a)y^2 + 2a^3 = 0$"],
         r"""The normal at $t$ is $tx + y - 2at - at^3 = 0$. Its pole $\left(\frac nl, -\frac{2am}{l}\right)$ with $l = t$, $m = 1$, $n = -2at - at^3$ is
$$h = -2a - at^2,\qquad k = -\frac{2a}{t}.$$
Then $t^2 = \frac{4a^2}{k^2}$ and $h + 2a = -\frac{4a^3}{k^2}$, so $(x + 2a)y^2 + 4a^3 = 0$.

Check: $h = -2a - at^2 < -2a$, so the locus lies left of $x = -2a$; the option $(x + 2a)y^2 = 4a^3$ would put it on the right.""")

# q18
T.single(2, ["conjugate"], r"The points $(1, 2)$ and $(k, 3)$ are conjugate with respect to the circle $x^2 + y^2 = 10$. Then $k =$",
         [r"$4$", r"$-4$", r"$16$", r"$2$"],
         r"""Conjugate means each lies on the polar of the other. The polar of $(1, 2)$ is $x + 2y = 10$; put in $(k, 3)$:
$$k + 6 = 10 \implies k = 4.$$
The sign slip $k + 6 = -10$, or forgetting that the right side is $a^2 = 10$, gives the wrong options.""")

# q19
T.single(2, ["conjugate"], r"The lines $l_1x + m_1y + n_1 = 0$ and $l_2x + m_2y + n_2 = 0$ are conjugate with respect to the ellipse $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$ if and only if",
         [r"$a^2l_1l_2 + b^2m_1m_2 = n_1n_2$", r"$a^2l_1l_2 - b^2m_1m_2 = n_1n_2$",
          r"$\dfrac{l_1l_2}{a^2} + \dfrac{m_1m_2}{b^2} = n_1n_2$", r"$a^2l_1m_1 + b^2l_2m_2 = n_1n_2$"],
         r"""The pole of the first line is $\left(-\frac{a^2l_1}{n_1}, -\frac{b^2m_1}{n_1}\right)$. It lies on the second iff
$$-\frac{a^2l_1l_2}{n_1} - \frac{b^2m_1m_2}{n_1} + n_2 = 0 \iff a^2l_1l_2 + b^2m_1m_2 = n_1n_2.$$
The minus-sign version is the hyperbola's condition. Dividing by $a^2, b^2$ is the conjugate-**points** pattern, not the lines pattern.""")

# q20
T.single(3, ["pair-of-tangents"], r"The combined equation of the pair of tangents from the origin to the circle $x^2 + y^2 - 6x - 4y + 9 = 0$ is",
         [r"$5y^2 - 12xy = 0$", r"$5x^2 - 12xy = 0$", r"$5y^2 + 12xy = 0$", r"$4y^2 - 12xy = 0$"],
         r"""Use $SS_1 = T^2$ with $S_1 = 9$ and $T = -3x - 2y + 9$:
$$9(x^2 + y^2 - 6x - 4y + 9) = (9 - 3x - 2y)^2.$$
The right side is $81 + 9x^2 + 4y^2 - 54x - 36y + 12xy$. Cancelling gives $5y^2 - 12xy = 0$, i.e. $y = 0$ and $12x = 5y$.

Check: the centre $(3, 2)$ is at distance $2$ (= radius) from $y = 0$, and at distance $\frac{\lvert 36 - 10\rvert}{13} = 2$ from $12x - 5y = 0$.""")

# q21
T.single(3, ["normals"], r"The line $lx + my + n = 0$ is a normal to the ellipse $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$ $(a > b > 0)$ if and only if",
         [r"$\dfrac{a^2}{l^2} + \dfrac{b^2}{m^2} = \dfrac{(a^2 - b^2)^2}{n^2}$", r"$\dfrac{a^2}{l^2} - \dfrac{b^2}{m^2} = \dfrac{(a^2 + b^2)^2}{n^2}$",
          r"$a^2l^2 + b^2m^2 = n^2$", r"$\dfrac{l^2}{a^2} + \dfrac{m^2}{b^2} = \dfrac{(a^2 - b^2)^2}{n^2}$"],
         r"""The normal at $\theta$ is $ax\sec\theta - by\csc\theta = a^2 - b^2$. Comparing with $lx + my + n = 0$:
$$\frac{a\sec\theta}{l} = \frac{-b\csc\theta}{m} = \frac{a^2 - b^2}{-n} \implies \cos\theta = -\frac{an}{l(a^2 - b^2)},\ \sin\theta = \frac{bn}{m(a^2 - b^2)}.$$
Squaring and adding: $\frac{a^2}{l^2} + \frac{b^2}{m^2} = \frac{(a^2 - b^2)^2}{n^2}$.

$a^2l^2 + b^2m^2 = n^2$ is the **tangency** condition; the minus/plus version belongs to the hyperbola.""")

# ---------------------------------------------------------------- statements (2)
T.statements(2, ["normals"], r"Consider the following statements:",
             [r"At most three normals can be drawn to the parabola $y^2 = 4ax$ from any point.",
              r"If three normals are drawn from a point to $y^2 = 4ax$, the sum of the ordinates of their feet is zero.",
              r"At most four normals can be drawn to an ellipse from any point."],
             [r"1, 2 and 3", r"1 and 2 only", r"1 and 3 only", r"2 and 3 only"],
             r"""1. True: the normal $y = mx - 2am - am^3$ passes through $(h, k)$ iff $am^3 + (2a - h)m + k = 0$, a cubic in $m$.
2. True: the cubic has no $m^2$ term, so $m_1 + m_2 + m_3 = 0$; the feet have ordinates $-2am_i$, which add to $0$.
3. True: the feet are the intersections of the ellipse with a rectangular hyperbola (Apollonius), at most four points. For example, from $\left(\frac1{10}, \frac1{20}\right)$ to $\frac{x^2}{4} + y^2 = 1$ there are exactly four.

The tempting "1 and 2 only" comes from carrying the parabola's bound of three over to the ellipse.""")

T.statements(2, ["conjugate", "poles-polars", "pair-of-tangents"], r"Consider the following statements:",
             [r"The points $(x_1, y_1)$ and $(x_2, y_2)$ are conjugate with respect to $x^2 + y^2 = a^2$ if and only if $x_1x_2 + y_1y_2 = a^2$.",
              r"The polar of $(1, 2)$ with respect to $y^2 = 4x$ is $y = x + 1$.",
              r"The director circle of the hyperbola $\dfrac{x^2}{9} - \dfrac{y^2}{16} = 1$ is $x^2 + y^2 = 7$."],
             [r"1 and 2 only", r"1 only", r"2 and 3 only", r"1, 2 and 3"],
             r"""1. True: the polar of $(x_1, y_1)$ is $xx_1 + yy_1 = a^2$; conjugacy means $(x_2, y_2)$ lies on it.
2. True: the polar is $2y = 2(x + 1)$, i.e. $y = x + 1$. Since $(1, 2)$ is on the parabola, this is the tangent there.
3. False: the director circle of a hyperbola is $x^2 + y^2 = a^2 - b^2 = 9 - 16 = -7$, which has no real points. No point sees this hyperbola under a right angle. $x^2 + y^2 = 7$ comes from computing $b^2 - a^2$.""")

# ---------------------------------------------------------------- match (2)
T.match(1, ["tangency"], r"Match each conic in List I $(a, b > 0)$ with the condition in List II for the line $y = mx + c$ to touch it.",
        [r"$x^2 + y^2 = a^2$", r"$y^2 = 4ax$", r"$\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$", r"$\dfrac{x^2}{a^2} - \dfrac{y^2}{b^2} = 1$"],
        [r"$c^2 = a^2m^2 - b^2$", r"$c = \dfrac am$", r"$c^2 = a^2(1 + m^2)$", r"$c^2 = a^2m^2 + b^2$"],
        [r"A-3, B-2, C-4, D-1", r"A-3, B-2, C-1, D-4", r"A-4, B-2, C-3, D-1", r"A-2, B-3, C-4, D-1"],
        r"""Substitute $y = mx + c$ and set the discriminant to zero.
- A: $(1 + m^2)x^2 + 2mcx + c^2 - a^2 = 0$ gives $c^2 = a^2(1 + m^2)$: 3.
- B: $m^2x^2 + (2mc - 4a)x + c^2 = 0$ gives $mc = a$: 2.
- C: $c^2 = a^2m^2 + b^2$: 4.
- D: $c^2 = a^2m^2 - b^2$: 1.

The usual slip swaps C and D. A check: the ellipse with $b = a$ is the circle, and $a^2m^2 + a^2 = a^2(1 + m^2)$ agrees with A.""")

T.match(3, ["pair-of-tangents"], r"Match each curve in List I with the locus in List II of points from which two perpendicular tangents can be drawn to it.",
        [r"$\dfrac{x^2}{16} + \dfrac{y^2}{9} = 1$", r"$\dfrac{x^2}{16} - \dfrac{y^2}{9} = 1$", r"$y^2 = 8x$", r"$x^2 + y^2 = 8$"],
        [r"$x = -2$", r"$x^2 + y^2 = 16$", r"$x^2 + y^2 = 25$", r"$x^2 + y^2 = 7$"],
        [r"A-3, B-4, C-1, D-2", r"A-4, B-3, C-1, D-2", r"A-3, B-4, C-2, D-1", r"A-2, B-4, C-1, D-3"],
        r"""These are the director circles.
- A: ellipse, $x^2 + y^2 = a^2 + b^2 = 25$: 3.
- B: hyperbola, $x^2 + y^2 = a^2 - b^2 = 7$: 4 (real since $a > b$).
- C: parabola with $a = 2$: the directrix $x = -2$: 1.
- D: circle of radius $\sqrt8$: $x^2 + y^2 = 2\cdot 8 = 16$: 2.

Swapping A and B mixes up $a^2 \pm b^2$.""")

# ---------------------------------------------------------------- assertion-reason (5)
T.assertion_reason(1, ["poles-polars"],
                   r"The polar of the focus $(ae, 0)$ of the ellipse $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$ $(0 < e < 1)$ is the directrix $x = \dfrac ae$.",
                   r"The polar of $(x_1, y_1)$ with respect to $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$ is $\dfrac{xx_1}{a^2} + \dfrac{yy_1}{b^2} = 1$.",
                   0,
                   r"""R is the definition $T = 0$, true. Put $(x_1, y_1) = (ae, 0)$:
$$\frac{x\cdot ae}{a^2} = 1 \implies x = \frac ae,$$
the directrix on the same side. So A is true and follows directly from R.""")

T.assertion_reason(2, ["pair-of-tangents"],
                   r"The two tangents drawn from $(3, 1)$ to the circle $x^2 + y^2 = 5$ are perpendicular.",
                   r"Perpendicular tangents can be drawn to $x^2 + y^2 = a^2$ only from points of the circle $x^2 + y^2 = 4a^2$.",
                   2,
                   r"""A is true: $3^2 + 1^2 = 10 = 2\cdot5$, so $(3, 1)$ lies on the director circle $x^2 + y^2 = 2a^2$. Directly, $\sin\alpha = \frac{\sqrt5}{\sqrt{10}} = \frac{1}{\sqrt2}$, so the half-angle is $\frac\pi4$ and the angle is $\frac\pi2$.

R is false: the director circle has radius $a\sqrt2$, not $2a$. From a point at distance $2a$, $\sin\alpha = \frac12$ and the tangents meet at $\frac\pi3$.""")

T.assertion_reason(3, ["poles-polars", "tangency"],
                   r"The polar of $(1, 1)$ with respect to the ellipse $\dfrac{x^2}{4} + \dfrac{y^2}{2} = 1$ meets the ellipse in two real points.",
                   r"A point $(x_1, y_1)$ lies inside $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$ if and only if $\dfrac{x_1^2}{a^2} + \dfrac{y_1^2}{b^2} < 1$.",
                   3,
                   r"""R is true (the standard $S_1 < 0$ test).

A is false. $\frac14 + \frac12 < 1$, so $(1, 1)$ is inside, and the polar of an interior point does not meet the conic. Directly: the polar is $\frac x4 + \frac y2 = 1$, i.e. $x = 4 - 2y$. Substituting,
$$\frac{(4 - 2y)^2}{4} + \frac{y^2}{2} = 1 \iff 3y^2 - 8y + 6 = 0,$$
whose discriminant $64 - 72 < 0$. No real intersection.""")

T.assertion_reason(3, ["tangency"],
                   r"The locus of the foot of the perpendicular from a focus to a variable tangent of the ellipse $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$ $(a > b > 0)$ is the auxiliary circle $x^2 + y^2 = a^2$.",
                   r"The product of the perpendiculars from the two foci to any tangent of the ellipse $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$ is $b^2$.",
                   1,
                   r"""Both are true. Take the tangent $y = mx + c$ with $c^2 = a^2m^2 + b^2$.

A: the perpendicular from $S(ae, 0)$ is $my + x = ae$. Squaring and adding $y - mx = c$ and $my + x = ae$:
$$(1 + m^2)(x^2 + y^2) = c^2 + a^2e^2 = a^2m^2 + b^2 + a^2 - b^2 = a^2(1 + m^2),$$
so $x^2 + y^2 = a^2$.

R: $p_1p_2 = \frac{\lvert(mae + c)(-mae + c)\rvert}{1 + m^2} = \frac{\lvert c^2 - m^2a^2e^2\rvert}{1 + m^2} = \frac{a^2m^2 + b^2 - m^2(a^2 - b^2)}{1 + m^2} = b^2$.

R is a different property; it does not give the locus in A. So the answer is "both true, R does not explain A".""")

T.assertion_reason(2, ["pair-of-tangents"],
                   r"The tangents to $y^2 = 4ax$ $(a > 0)$ drawn from any point of the directrix $x = -a$ are perpendicular.",
                   r"The slopes of the tangents to $y^2 = 4ax$ from $(h, k)$, $h \ne 0$, are the roots of $hm^2 - km + a = 0$.",
                   0,
                   r"""R is true: the tangent $y = mx + \frac am$ passes through $(h, k)$ iff $k = mh + \frac am$, i.e. $hm^2 - km + a = 0$.

By R the product of the slopes is $\frac ah$. On the directrix $h = -a$, so the product is $-1$: the tangents are perpendicular. (The discriminant $k^2 + 4a^2 > 0$, so both are real.) R explains A.""")


def check():
    import sympy as sp
    x, y, m, c, t, th, k, l, n, h = sp.symbols("x y m c t theta k l n h", real=True)
    a, b = sp.symbols("a b", positive=True)
    l1, m1, n1, l2, m2, n2 = sp.symbols("l1 m1 n1 l2 m2 n2", real=True)

    def disc_line(S, line_y):
        """discriminant of S(x, mx+c) in x."""
        P = sp.Poly(sp.expand(S.subs(y, line_y)), x)
        A, B, C = [P.coeff_monomial(x**i) for i in (2, 1, 0)]
        return sp.expand(B**2 - 4 * A * C)

    def touches(S, L):
        """line L(x,y)=0 (with y-coeff nonzero) touches conic S: discriminant zero."""
        ysol = sp.solve(L, y)[0]
        return sp.simplify(disc_line(S, ysol)) == 0

    def Tform(S, P):
        """polar T of P w.r.t. second-degree S (via gradient: T = (x-x1)Sx(P)/2 + ... + S(P))."""
        x1, y1 = P
        Sx = sp.diff(S, x).subs({x: x1, y: y1}); Sy = sp.diff(S, y).subs({x: x1, y: y1})
        return sp.expand(((x - x1) * Sx + (y - y1) * Sy) / 2 + S.subs({x: x1, y: y1}))

    def same_line(L1, L2):
        P1 = sp.Poly(L1, x, y); P2 = sp.Poly(L2, x, y)
        v1 = [P1.coeff_monomial(mm) for mm in (x, y, 1)]
        v2 = [P2.coeff_monomial(mm) for mm in (x, y, 1)]
        return sp.Matrix([v1, v2]).rank() == 1

    # q1
    C25 = x**2 + y**2 - 25
    assert same_line(Tform(C25, (3, 4)), 3 * x + 4 * y - 25)
    assert touches(C25, 3 * x + 4 * y - 25) and (4 * x + 3 * y - 25).subs({x: 3, y: 4}) != 0
    # q2
    E94 = x**2 / 9 + y**2 / 4 - 1
    assert sorted(sp.solve(disc_line(E94, x + c), c)) == sorted([-sp.sqrt(13), sp.sqrt(13)])
    # q3
    P8 = y**2 - 8 * x
    assert sp.solve(disc_line(P8, 2 * x + c), c) == [1]
    # q4
    Cq4 = x**2 + y**2 - 2 * x - 4 * y - 4
    ks = sp.solve(disc_line(Cq4, (k - 3 * x) / 4), k)
    assert sorted(ks) == [-4, 26], ks
    # q5 general: l y^2 + 4 a m y + 4 a n disc
    Py = sp.expand((y**2 - 4 * a * x).subs(x, -(m * y + n) / l) * l)
    P = sp.Poly(Py, y)
    D = sp.expand(P.coeff_monomial(y)**2 - 4 * P.coeff_monomial(y**2) * P.coeff_monomial(1))
    eq(sp.factor(D / (16 * a)), a * m**2 - l * n, "q5")
    # q6 normal slope form passes through foot (am^2,-2am) perpendicular to tangent there
    foot = (a * m**2, -2 * a * m)
    tslope = (-sp.diff(y**2 - 4 * a * x, x) / sp.diff(y**2 - 4 * a * x, y)).subs({x: foot[0], y: foot[1]})
    eq(tslope * m, -1, "q6 perp")
    eq((m * x - 2 * a * m - a * m**3).subs(x, foot[0]), foot[1], "q6")
    # q7
    roots = sp.solve(5 * m - 2 * m - m**3, m)
    assert len([r for r in roots if r.is_real]) == 3
    assert len([r for r in sp.solve(1 * m - 2 * m - m**3, m) if r.is_real]) == 1  # (1,0) gives one
    # q8
    eq(2 * sp.asin(sp.Rational(2, 4)), sp.pi / 3, "q8")
    # q9 tangent at param point: passes, and touches
    E = x**2 / a**2 + y**2 / b**2 - 1
    Tq9 = Tform(E, (a * sp.cos(th), b * sp.sin(th)))
    eq(Tq9 - (x * sp.cos(th) / a + y * sp.sin(th) / b - 1), 0, "q9")
    # q10
    assert same_line(Tform(x**2 + y**2 - 4, (2, 3)), 2 * x + 3 * y - 4)
    # q11 T = S1: line, and check midpoint via intersection
    E169 = x**2 / 16 + y**2 / 9 - 1
    Lq11 = Tform(E169, (2, 1)) - E169.subs({x: 2, y: 1})
    assert same_line(Lq11, 9 * x + 8 * y - 26)
    pts = sp.solve([E169, 9 * x + 8 * y - 26], [x, y])
    eq(sum(p[0] for p in pts) / 2, 2, "q11 mx"); eq(sum(p[1] for p in pts) / 2, 1, "q11 my")
    # q12 pole
    hk = sp.solve([sp.Eq(h / 9, sp.Rational(1, 3)), sp.Eq(k / 4, sp.Rational(1, 2))], [h, k])
    assert hk == {h: 3, k: 2}
    assert same_line(Tform(E94, (3, 2)), 2 * x + 3 * y - 6)
    # q13
    Pa = y**2 - 4 * a * x
    ratio = sp.simplify(Tform(Pa, (n / l, -2 * a * m / l)) / (l * x + m * y + n))
    assert not ratio.has(x) and not ratio.has(y), ratio
    # q14
    Cq14 = x**2 + y**2 - 4 * x + 2 * y - 4
    eq(sp.sqrt(Cq14.subs({x: 5, y: 3})), 4, "q14")
    # q15 chord of contact length, directly from contact points
    pts = sp.solve([x**2 + y**2 - 9, 4 * x + 3 * y - 9], [x, y])
    eq(sp.sqrt((pts[0][0] - pts[1][0])**2 + (pts[0][1] - pts[1][1])**2), sp.Rational(24, 5), "q15")
    # q16: polar hx+ky=b^2 touches x^2+y^2=a^2
    D16 = sp.factor(disc_line(x**2 + y**2 - a**2, (b**2 - h * x) / k))
    sol = sp.solve(D16, h**2)
    eq(sol[0] + k**2, b**4 / a**2, "q16")
    # q17 pole of normal chord
    Lt = t * x + y - 2 * a * t - a * t**3
    pole = (-2 * a - a * t**2, -2 * a / t)
    ratio = sp.simplify(Tform(Pa, pole) / Lt)
    assert not ratio.has(x) and not ratio.has(y), ratio
    eq(sp.simplify((pole[0] + 2 * a) * pole[1]**2 + 4 * a**3), 0, "q17")
    # q18
    assert sp.solve(Tform(x**2 + y**2 - 10, (1, 2)).subs({x: k, y: 3}), k) == [4]
    # q19 conjugate lines ellipse
    pole1 = (-a**2 * l1 / n1, -b**2 * m1 / n1)
    eq(sp.expand((l2 * pole1[0] + m2 * pole1[1] + n2) * (-n1)), a**2 * l1 * l2 + b**2 * m1 * m2 - n1 * n2, "q19")
    # numeric: a=3,b=2: line1 x+y=1 pole; find line2 through it
    r19 = sp.simplify(Tform(E, pole1) / (l1 * x + m1 * y + n1))
    assert not r19.has(x) and not r19.has(y)
    # q20 SS1 = T^2
    Sq20 = x**2 + y**2 - 6 * x - 4 * y + 9
    pair = sp.expand(Sq20 * Sq20.subs({x: 0, y: 0}) - Tform(Sq20, (0, 0))**2)
    eq(pair, 5 * y**2 - 12 * x * y, "q20")
    assert touches(Sq20, 12 * x - 5 * y) and touches(Sq20, y)
    assert not touches(Sq20, 12 * x + 5 * y)
    # q21 normal condition: from param normal
    lth, mth, nth = a / sp.cos(th), -b / sp.sin(th), -(a**2 - b**2)
    eq(sp.simplify(a**2 / lth**2 + b**2 / mth**2 - (a**2 - b**2)**2 / nth**2), 0, "q21")
    assert sp.simplify(a**2 * lth**2 + b**2 * mth**2 - nth**2) != 0
    # normal at theta really is normal: passes through foot and perpendicular to tangent
    Nth = a * x / sp.cos(th) - b * y / sp.sin(th) - (a**2 - b**2)
    eq(Nth.subs({x: a * sp.cos(th), y: b * sp.sin(th)}), 0, "q21 foot")
    gradT = (sp.cos(th) / a, sp.sin(th) / b)
    eq(sp.simplify(sp.diff(Nth, x) * gradT[0] + sp.diff(Nth, y) * gradT[1]), 0, "q21 perp")
    # parabola normal condition in notes: a l^3 + 2 a l m^2 + m^2 n = 0 for y = Mx - 2aM - aM^3
    M = sp.symbols("M")
    eq(sp.expand(a * M**3 + 2 * a * M * 1 + 1 * (-2 * a * M - a * M**3)), 0, "notes parabola normal")

    # statements 1: (1) cubic (2) no m^2 term (3) four normals to x^2/4+y^2=1 from (1/10,1/20)
    hh, kk = sp.symbols("hh kk")
    cub = sp.Poly(a * m**3 + (2 * a - hh) * m + kk, m)
    assert cub.degree() == 3 and cub.coeff_monomial(m**2) == 0
    E41 = x**2 / 4 + y**2 - 1
    H0, K0 = sp.Rational(1, 10), sp.Rational(1, 20)
    cond = sp.expand((H0 - x) * sp.diff(E41, y) - (K0 - y) * sp.diff(E41, x))
    # rational parametrisation of the ellipse; t = oo (point (-2, 0)) checked separately
    tx, ty = 2 * (1 - t**2) / (1 + t**2), 2 * t / (1 + t**2)
    num = sp.numer(sp.together(cond.subs({x: tx, y: ty})))
    nreal = len(sp.real_roots(sp.Poly(num, t)))
    at_inf = cond.subs({x: -2, y: 0}) == 0
    assert nreal + int(at_inf) == 4, (nreal, at_inf)
    assert sp.Poly(num, t).degree() <= 4
    # statements 2: (2) polar of (1,2) wrt y^2=4x; (3) a^2-b^2 = -7
    assert same_line(Tform(y**2 - 4 * x, (1, 2)), y - x - 1)
    assert 9 - 16 == -7
    # check perpendicular tangents impossible for that hyperbola: slopes quadratic product -1 => h^2+k^2 = -7
    H = x**2 / 9 - y**2 / 16 - 1
    cc = sp.solve(disc_line(H, m * x + c), c)
    assert set(sp.simplify(ci**2) for ci in cc) == {9 * m**2 - 16}
    # match 1
    for S, want in ((x**2 + y**2 - a**2, a**2 * (1 + m**2)), (E, a**2 * m**2 + b**2),
                    (x**2 / a**2 - y**2 / b**2 - 1, a**2 * m**2 - b**2)):
        cs = sp.solve(disc_line(S, m * x + c), c)
        assert all(sp.simplify(ci**2 - want) == 0 for ci in cs), (S, cs)
    assert sp.solve(disc_line(y**2 - 4 * a * x, m * x + c), c) == [a / m]
    # match 2: director circles via product of slopes -1
    def director(S):
        Q = sp.Poly(sp.expand(disc_line(S, m * (x - h) + k)), m)  # tangents through (h,k)
        A2, A0 = Q.coeff_monomial(m**2), Q.coeff_monomial(1)
        return sp.factor(A2 + A0)  # product of roots = -1 <=> A0 = -A2
    d1 = sp.Poly(director(x**2 / 16 + y**2 / 9 - 1), h, k)
    assert sp.simplify(d1.as_expr() / d1.LC() - (h**2 + k**2 - 25)) == 0, d1
    d2 = sp.Poly(director(x**2 / 16 - y**2 / 9 - 1), h, k)
    assert sp.simplify(d2.as_expr() / d2.LC() - (h**2 + k**2 - 7)) == 0, d2
    d4 = sp.Poly(director(x**2 + y**2 - 8), h, k)
    assert sp.simplify(d4.as_expr() / d4.LC() - (h**2 + k**2 - 16)) == 0, d4
    # parabola y^2=8x: tangents y = m x + 2/m through (h,k): h m^2 - k m + 2 = 0 -> product 2/h = -1 -> h=-2
    assert sp.solve(sp.Rational(2, 1) / h + 1, h) == [-2]

    # AR1
    e = sp.symbols("e", positive=True)
    assert sp.solve(Tform(E, (a * e, 0)), x) == [a / e]
    # AR2
    eq(3**2 + 1**2, 2 * 5, "AR2 A")
    eq(2 * sp.asin(sp.sqrt(5) / sp.sqrt(10)), sp.pi / 2, "AR2 A angle")
    eq(2 * sp.asin(sp.Rational(1, 2)), sp.pi / 3, "AR2 R false")
    # AR3
    Eq3 = x**2 / 4 + y**2 / 2 - 1
    assert Eq3.subs({x: 1, y: 1}) < 0
    assert [s for s in sp.solve([Eq3, Tform(Eq3, (1, 1))], [x, y]) if all(sp.im(v) == 0 for v in s)] == []
    eq(sp.discriminant(3 * y**2 - 8 * y + 6, y), -8, "AR3")
    # AR4: foot from (ae,0) on y = m x + c with c^2 = a^2 m^2 + b^2, a^2 e^2 = a^2 - b^2
    cc = sp.sqrt(a**2 * m**2 + b**2); ae = sp.sqrt(a**2 - b**2)
    ft = sp.solve([y - m * x - cc, m * y + x - ae], [x, y])
    eq(sp.simplify(ft[x]**2 + ft[y]**2), a**2, "AR4 A")
    p1 = (m * ae + cc) / sp.sqrt(1 + m**2); p2 = (-m * ae + cc) / sp.sqrt(1 + m**2)
    eq(sp.simplify(p1 * p2), b**2, "AR4 R")
    # AR5
    Q5 = sp.Poly(sp.expand((k - m * h - a / m) * m), m)
    eq(sp.simplify(Q5.coeff_monomial(1) / Q5.coeff_monomial(m**2)).subs(h, -a), -1, "AR5")


T.write(check)
