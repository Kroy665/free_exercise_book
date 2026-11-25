# Tangents, Poles and Polars

## Tangency: point, slope and parametric forms {#tangency}

Throughout, $a, b > 0$ and the conics are in standard form: circle $x^2 + y^2 = a^2$, parabola $y^2 = 4ax$, ellipse $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$, hyperbola $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$. Reducing a general second-degree equation to these forms belongs to the topic on transformation of axes.

**Notation.** Write the conic as $S = 0$. For a point $P(x_1, y_1)$:

- $S_1 = S(x_1, y_1)$, the value of $S$ at $P$. With $S$ normalised as above (for example $S = \frac{x^2}{a^2} + \frac{y^2}{b^2} - 1$), $P$ is outside, on or inside the conic as $S_1 > 0$, $= 0$, $< 0$.
- $T = 0$ is obtained from $S$ by the **substitution rule**: $x^2 \to xx_1$, $y^2 \to yy_1$, $2xy \to xy_1 + x_1y$, $2x \to x + x_1$, $2y \to y + y_1$. For a circle $x^2 + y^2 + 2gx + 2fy + c = 0$: $T \equiv xx_1 + yy_1 + g(x + x_1) + f(y + y_1) + c$.

If $P$ lies on the conic, **$T = 0$ is the tangent at $P$**.

| Conic | Tangent at $(x_1, y_1)$ | Tangent at the parametric point | Slope form | $lx + my + n = 0$ touches iff |
|:---|:---|:---|:---|:---|
| circle | $xx_1 + yy_1 = a^2$ | $x\cos\theta + y\sin\theta = a$ | $y = mx \pm a\sqrt{1 + m^2}$ | $n^2 = a^2(l^2 + m^2)$ |
| parabola | $yy_1 = 2a(x + x_1)$ | $ty = x + at^2$ at $(at^2, 2at)$ | $y = mx + \frac{a}{m}$ | $ln = am^2$ |
| ellipse | $\frac{xx_1}{a^2} + \frac{yy_1}{b^2} = 1$ | $\frac{x\cos\theta}{a} + \frac{y\sin\theta}{b} = 1$ | $y = mx \pm\sqrt{a^2m^2 + b^2}$ | $a^2l^2 + b^2m^2 = n^2$ |
| hyperbola | $\frac{xx_1}{a^2} - \frac{yy_1}{b^2} = 1$ | $\frac{x\sec\theta}{a} - \frac{y\tan\theta}{b} = 1$ | $y = mx \pm\sqrt{a^2m^2 - b^2}$ | $a^2l^2 - b^2m^2 = n^2$ |

**Condition of tangency** for $y = mx + c$: substitute into the conic and set the discriminant of the resulting quadratic to zero. This gives

$$\text{circle: } c^2 = a^2(1 + m^2),\quad \text{parabola: } c = \frac am,\quad \text{ellipse: } c^2 = a^2m^2 + b^2,\quad \text{hyperbola: } c^2 = a^2m^2 - b^2.$$

Points of contact: $\left(\frac{a}{m^2}, \frac{2a}{m}\right)$ on the parabola, and $\left(-\frac{a^2m}{c}, \frac{b^2}{c}\right)$ on the ellipse.

For a general circle, the line touches iff the distance from the centre equals the radius. Example: $3x + 4y = k$ touches $x^2 + y^2 - 2x - 4y - 4 = 0$ (centre $(1, 2)$, radius $3$) iff $\frac{\lvert 11 - k\rvert}{5} = 3$, i.e. $k = 26$ or $k = -4$.

:::caution
For the hyperbola a real tangent of slope $m$ exists only when $a^2m^2 > b^2$, i.e. $\lvert m\rvert > \frac ba$. At $\lvert m\rvert = \frac ba$, $c = 0$ gives an **asymptote**, which is not a tangent at any finite point.
:::

Two focal properties of the ellipse are often examined: the feet of the perpendiculars from either focus to any tangent lie on the **auxiliary circle** $x^2 + y^2 = a^2$, and the product of the perpendiculars from the two foci to any tangent is $b^2$. For the parabola the foot of the perpendicular from the focus lies on the tangent at the vertex, $x = 0$.

## Normals {#normals}

The normal at a point is the line through it perpendicular to the tangent. For a circle every normal passes through the centre.

| Conic | Normal at $(x_1, y_1)$ | Normal at the parametric point |
|:---|:---|:---|
| parabola | $y - y_1 = -\frac{y_1}{2a}(x - x_1)$ | $y + tx = 2at + at^3$ |
| ellipse | $\frac{a^2x}{x_1} - \frac{b^2y}{y_1} = a^2 - b^2$ | $ax\sec\theta - by\csc\theta = a^2 - b^2$ |
| hyperbola | $\frac{a^2x}{x_1} + \frac{b^2y}{y_1} = a^2 + b^2$ | $ax\cos\theta + by\cot\theta = a^2 + b^2$ |

**Slope form for the parabola.** Put $m = -t$:

$$y = mx - 2am - am^3,\qquad \text{foot } (am^2, -2am).$$

**Normals from a point $(h, k)$ to $y^2 = 4ax$.** The line passes through $(h, k)$ iff

$$am^3 + (2a - h)m + k = 0.$$

- A cubic: **at most three normals** (co-normal points). There is no $m^2$ term, so $m_1 + m_2 + m_3 = 0$, and the feet have ordinates $-2am_i$ summing to **zero**.
- From $(h, 0)$: $m(am^2 + 2a - h) = 0$, so three real normals iff $h > 2a$. From $(5, 0)$ to $y^2 = 4x$: $m^3 - 3m = 0$, giving $m = 0, \pm\sqrt3$.

**Ellipse.** From a point there are **at most four** normals (the feet satisfy a quartic). A line $lx + my + n = 0$ is a normal iff

$$\frac{a^2}{l^2} + \frac{b^2}{m^2} = \frac{(a^2 - b^2)^2}{n^2}.$$

Proof idea: compare with $ax\sec\theta - by\csc\theta = a^2 - b^2$; then $\frac{a}{l}$ and $\frac{b}{m}$ are proportional to $\cos\theta$ and $\sin\theta$, and $\cos^2\theta + \sin^2\theta = 1$.

For the parabola the corresponding condition is $al^3 + 2alm^2 + m^2n = 0$.

:::exam-tip
Do not mix up the signs: the ellipse normal has $a^2 - b^2$ on the right and a minus between the terms; the hyperbola normal has $a^2 + b^2$ and a plus. Check by putting the foot back in: at $(a\cos\theta, b\sin\theta)$ the ellipse form gives $a^2 - b^2$, as it must, while the hyperbola-style form would give $a^2 + b^2$.
:::

:::caution
"At most three normals" holds for the parabola, but "at most three" is wrong for the ellipse and hyperbola, where the bound is four.
:::

## Pair of tangents and the director circle {#pair-of-tangents}

From a point $P(x_1, y_1)$ **outside** a conic two real tangents can be drawn; from a point on it, one; from a point inside, none. Their combined equation is

$$SS_1 = T^2.$$

**Why.** A point $Q$ is on a tangent from $P$ iff the line $PQ$ meets the conic in coincident points. Writing the points of $PQ$ in the ratio $\lambda : 1$ gives a quadratic in $\lambda$ whose discriminant is $T^2 - SS_1$ evaluated at $Q$.

**Example.** From the origin to $x^2 + y^2 - 6x - 4y + 9 = 0$: $S_1 = 9$ and $T = -3x - 2y + 9$. Then

$$9(x^2 + y^2 - 6x - 4y + 9) = (9 - 3x - 2y)^2 \iff 5y^2 - 12xy = 0,$$

so the tangents are $y = 0$ and $12x = 5y$.

**Angle between the tangents to a circle.** If $d$ is the distance of $P$ from the centre and $L = \sqrt{S_1}$ the tangent length, the half-angle $\alpha$ satisfies

$$\sin\alpha = \frac{a}{d},\qquad \tan\alpha = \frac{a}{L}.$$

From $(4, 0)$ to $x^2 + y^2 = 4$: $\sin\alpha = \frac12$, so the tangents meet at $\frac{\pi}{3}$.

**Slopes from $(h, k)$.** Putting $(h, k)$ into the slope form gives a quadratic in $m$:

| Conic | Quadratic in $m$ | Product of slopes |
|:---|:---|:---|
| parabola | $hm^2 - km + a = 0$ | $\frac{a}{h}$ |
| ellipse | $(h^2 - a^2)m^2 - 2hkm + k^2 - b^2 = 0$ | $\frac{k^2 - b^2}{h^2 - a^2}$ |

**Director circle.** The locus of points from which the two tangents are **perpendicular** (product of slopes $-1$):

| Conic | Director circle |
|:---|:---|
| circle $x^2 + y^2 = a^2$ | $x^2 + y^2 = 2a^2$ |
| ellipse | $x^2 + y^2 = a^2 + b^2$ |
| hyperbola | $x^2 + y^2 = a^2 - b^2$ (real only if $a > b$) |
| parabola $y^2 = 4ax$ | the directrix $x = -a$ |

For the parabola, $\frac ah = -1$ gives $h = -a$: perpendicular tangents always meet on the directrix.

:::caution
The hyperbola's director circle has radius $\sqrt{a^2 - b^2}$, not $\sqrt{a^2 + b^2}$. For $b > a$ (e.g. $\frac{x^2}{9} - \frac{y^2}{16} = 1$) there is no real point with perpendicular tangents; for the rectangular hyperbola the "circle" shrinks to the centre.
:::

## Chord of contact and chord with a given midpoint {#chord-of-contact}

**Chord of contact.** If the tangents from an external point $P(x_1, y_1)$ touch the conic at $Q$ and $R$, then the chord $QR$ is

$$T = 0.$$

**Why.** The tangent at $Q(\alpha, \beta)$ is $T_Q = 0$ and passes through $P$; this relation is symmetric, so $Q$ satisfies $T_P = 0$, and so does $R$. Two points fix the line. Example: the chord of contact from $(2, 3)$ to $x^2 + y^2 = 4$ is $2x + 3y = 4$.

**Circle measurements.** For $x^2 + y^2 + 2gx + 2fy + c = 0$ (coefficients of $x^2, y^2$ equal to $1$) and an external point:

- tangent length $L = \sqrt{S_1}$;
- with radius $r$: length of chord of contact $= \dfrac{2rL}{\sqrt{r^2 + L^2}}$;
- area of the triangle formed by the two tangents and the chord of contact $= \dfrac{rL^3}{r^2 + L^2}$.

From $(4, 3)$ to $x^2 + y^2 = 9$: $L = 4$, $r = 3$, chord $= \frac{24}{5}$, area $= \frac{192}{25}$.

**Chord with a given midpoint.** The chord of $S = 0$ whose midpoint is $(x_1, y_1)$ is

$$T = S_1.$$

**Why.** For the ellipse, if $(x_1 \pm u, y_1 \pm v)$ are the ends, subtracting the two equations gives $\frac{x_1u}{a^2} + \frac{y_1v}{b^2} = 0$, so the chord has the direction of the line $\frac{xx_1}{a^2} + \frac{yy_1}{b^2} = \text{const}$, and it passes through $(x_1, y_1)$.

**Example.** The chord of $\frac{x^2}{16} + \frac{y^2}{9} = 1$ bisected at $(2, 1)$:

$$\frac{2x}{16} + \frac{y}{9} - 1 = \frac{4}{16} + \frac19 - 1 \iff \frac x8 + \frac y9 = \frac{13}{36} \iff 9x + 8y = 26.$$

**Diameters.** Letting $(x_1, y_1)$ vary over midpoints of chords of fixed slope $m$ gives a line through the centre, a **diameter**: $y = -\frac{b^2}{a^2m}x$ for the ellipse, $y = \frac{2a}{m}$ for the parabola.

:::exam-tip
$T = 0$ and $T = S_1$ have the same $x$- and $y$-coefficients: the chord of contact from $P$ and the chord bisected at $P$ are **parallel**. If a distractor has the right coefficients and the constant of $T = 0$, it is the chord of contact, not the bisected chord.
:::

:::caution
$L = \sqrt{S_1}$ needs the circle written with $x^2$ and $y^2$ coefficients equal to $1$. For $2x^2 + 2y^2 + \cdots = 0$, divide by $2$ first.
:::

## Poles and polars {#poles-polars}

**Definition.** The **polar** of a point $P(x_1, y_1)$ with respect to the conic $S = 0$ is the line $T = 0$. $P$ is the **pole** of that line.

Equivalent descriptions:

- If $P$ is outside, the polar is the chord of contact from $P$.
- If $P$ is on the conic, the polar is the tangent at $P$.
- If $P$ is inside, the polar is a real line that **does not meet** the conic. It is the locus of the intersections of the tangents at the ends of chords through $P$.
- In every case it is the locus of the **harmonic conjugate** of $P$ with respect to the two ends of a variable chord through $P$.

```plot
title: Tangents from $P(3, 4)$ to $\frac{x^2}{9} + \frac{y^2}{4} = 1$ and the polar of $P$
x: -5, 6
y: -3, 5
equal: true
implicit: x^2/9 + y^2/4 = 1 | ellipse
vline: 3
f: (x + 5)/2 | tangent $-x + 2y = 5$
f: 1 - x/3 | polar $\frac x3 + y = 1$
point: 3, 4 | $P$
point: 3, 0 | $Q$
point: -1.8, 1.6 | $R$
```

**Pole of a given line** $lx + my + n = 0$ ($n \ne 0$ where it divides). Compare it with the polar $T = 0$ of an unknown $(h, k)$:

| Conic | Pole of $lx + my + n = 0$ |
|:---|:---|
| circle $x^2 + y^2 = a^2$ | $\left(-\frac{a^2l}{n}, -\frac{a^2m}{n}\right)$ |
| parabola $y^2 = 4ax$ | $\left(\frac nl, -\frac{2am}{l}\right)$ |
| ellipse | $\left(-\frac{a^2l}{n}, -\frac{b^2m}{n}\right)$ |
| hyperbola | $\left(-\frac{a^2l}{n}, \frac{b^2m}{n}\right)$ |

Example: the pole of $2x + 3y = 6$ with respect to $\frac{x^2}{9} + \frac{y^2}{4} = 1$. The polar of $(h, k)$ is $\frac{hx}{9} + \frac{ky}{4} = 1$; matching $\frac x3 + \frac y2 = 1$ gives $(h, k) = (3, 2)$.

**Standard properties.**

1. **Reciprocity (La Hire).** If $Q$ lies on the polar of $P$, then $P$ lies on the polar of $Q$, because $T_P(Q) = T_Q(P)$.
2. The polar of a **focus** is the corresponding **directrix**: for $(ae, 0)$ on the ellipse, $\frac{x\cdot ae}{a^2} = 1$, i.e. $x = \frac ae$.
3. The polar of the **centre** of a central conic has no finite equation ($T = -1 = 0$): it is the line at infinity.
4. For a circle with centre $C$ and radius $a$, the polar of $P$ is **perpendicular to $CP$** at distance $\frac{a^2}{CP}$ from $C$ (it passes through the inverse point of $P$).
5. The poles of all lines through a fixed point $P$ lie on the polar of $P$.

**Locus problems.** To find the locus of the pole of a moving line, write the line as the polar of $(h, k)$ and impose the line's condition. Example: if the polar of $(h, k)$ with respect to $x^2 + y^2 = b^2$, namely $hx + ky = b^2$, touches $x^2 + y^2 = a^2$, then $\frac{b^4}{h^2 + k^2} = a^2$, so the poles lie on $x^2 + y^2 = \frac{b^4}{a^2}$.

## Conjugate points and conjugate lines {#conjugate}

**Conjugate points.** $P$ and $Q$ are **conjugate** with respect to a conic if $Q$ lies on the polar of $P$. By reciprocity this is symmetric. The condition is $T_P(Q) = 0$, i.e. $S_{12} = 0$:

| Conic | $(x_1, y_1)$ and $(x_2, y_2)$ conjugate iff |
|:---|:---|
| circle $x^2 + y^2 = a^2$ | $x_1x_2 + y_1y_2 = a^2$ |
| parabola $y^2 = 4ax$ | $y_1y_2 = 2a(x_1 + x_2)$ |
| ellipse | $\frac{x_1x_2}{a^2} + \frac{y_1y_2}{b^2} = 1$ |
| hyperbola | $\frac{x_1x_2}{a^2} - \frac{y_1y_2}{b^2} = 1$ |

Example: $(1, 2)$ and $(k, 3)$ are conjugate for $x^2 + y^2 = 10$ iff $k + 6 = 10$, i.e. $k = 4$. A point is **self-conjugate** iff it lies on the conic.

**Conjugate lines.** Two lines are conjugate if each passes through the pole of the other (one condition implies the other). With $L_i \equiv l_ix + m_iy + n_i = 0$, put the pole of $L_1$ into $L_2$:

| Conic | $L_1$, $L_2$ conjugate iff |
|:---|:---|
| circle $x^2 + y^2 = a^2$ | $a^2(l_1l_2 + m_1m_2) = n_1n_2$ |
| parabola $y^2 = 4ax$ | $l_1n_2 + l_2n_1 = 2am_1m_2$ |
| ellipse | $a^2l_1l_2 + b^2m_1m_2 = n_1n_2$ |
| hyperbola | $a^2l_1l_2 - b^2m_1m_2 = n_1n_2$ |

Derivation for the ellipse: the pole of $L_1$ is $\left(-\frac{a^2l_1}{n_1}, -\frac{b^2m_1}{n_1}\right)$; it lies on $L_2$ iff $-\frac{a^2l_1l_2}{n_1} - \frac{b^2m_1m_2}{n_1} + n_2 = 0$.

**Link with conjugate diameters.** For two lines through the centre ($n_1 = n_2 = 0$) the ellipse condition becomes $a^2l_1l_2 + b^2m_1m_2 = 0$; in slopes $\mu_i = -\frac{l_i}{m_i}$ this is $\mu_1\mu_2 = -\frac{b^2}{a^2}$, the familiar condition for **conjugate diameters**.

**Self-polar triangle.** A triangle in which each vertex is the pole of the opposite side. Any two of its vertices are conjugate points and any two of its sides are conjugate lines.

:::exam-tip
Every condition in this section is "the tangent-form $T$ with one point replaced by the other". Remember the four $T$-forms and you can regenerate both tables in seconds.
:::

:::caution
The circle condition has $a^2$ multiplying **both** $l_1l_2$ and $m_1m_2$. Writing $a^2l_1l_2 + m_1m_2 = n_1n_2$ is a common slip carried over from the ellipse with $b = 1$.
:::

## Quick checks and traps {#exam-tips}

- **Three formulas, one rule.** Tangent at a point, chord of contact and polar are all $T = 0$; the chord bisected at a point is $T = S_1$; the pair of tangents is $SS_1 = T^2$.
- **Tangency conditions:** $c^2 = a^2(1 + m^2)$, $c = \frac am$, $c^2 = a^2m^2 + b^2$, $c^2 = a^2m^2 - b^2$ for circle, parabola, ellipse, hyperbola. A sign slip between the last two is the standard distractor.
- **Director circles:** $2a^2$, $a^2 + b^2$, $a^2 - b^2$, directrix. If a point is on the director circle, the angle between the tangents is $\frac\pi2$ without any computation.
- **Pole of a line:** match coefficients with $T = 0$ of an unknown point rather than memorising four formulas.
- **Inside or outside:** $S_1 < 0$ means inside; then no real tangents, and the polar misses the conic.
- **Normals:** parabola at most $3$, ellipse at most $4$; for the parabola the ordinates of the three feet add to $0$.
- **Polar of a focus** is the directrix; the polar of the centre is the line at infinity.
- **Locus of poles of normal chords** of $y^2 = 4ax$: the normal at $t$ is $tx + y - 2at - at^3 = 0$, whose pole is $\left(-2a - at^2, -\frac{2a}{t}\right)$. Eliminating $t$ gives $(x + 2a)y^2 + 4a^3 = 0$.
- **Polar equations** of these conics (focus as pole) are treated in the polar-equations topic, and the condition for a second-degree equation to be a pair of lines in the pair-of-lines topic.
