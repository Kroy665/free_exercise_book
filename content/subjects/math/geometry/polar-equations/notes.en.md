# Polar Equations

## Polar coordinates and conversion {#polar-coordinates}

Fix a point $O$ (the **pole**) and a ray $OX$ from it (the **initial line**). A point $P$ has polar coordinates $(r, \theta)$ when $OP = r$ and the angle from $OX$ to $OP$, measured anticlockwise, is $\theta$. With $O$ as origin and $OX$ as the positive $x$-axis:

$$x = r\cos\theta,\quad y = r\sin\theta;\qquad r^2 = x^2 + y^2,\quad \tan\theta = \frac yx.$$

- Polar coordinates are **not unique**: $(r, \theta)$, $(r, \theta + 2k\pi)$ and $(-r, \theta + \pi)$ are the same point. A negative $r$ means "go a distance $\lvert r\rvert$ in the direction opposite to $\theta$".
- When a unique answer is wanted, take $r > 0$ and $\theta \in (-\pi, \pi]$ and **place $\theta$ by quadrant**, as with the argument of a complex number. For $(-1, -1)$: $r = \sqrt2$, $\theta = -\frac{3\pi}{4}$, not $\frac\pi4$ (which is what $\tan^{-1}\frac{-1}{-1}$ returns).

**Distance** between $P(r_1, \theta_1)$ and $Q(r_2, \theta_2)$ (cosine rule in triangle $OPQ$):

$$PQ^2 = r_1^2 + r_2^2 - 2r_1r_2\cos(\theta_1 - \theta_2).$$

**Area** of triangle $OPQ$: $\frac12 r_1r_2\sin(\theta_2 - \theta_1)$ (absolute value for the area). For three points, add the three such triangles with signs.

Example: $P(3, \frac\pi6)$, $Q(4, \frac\pi2)$ give $PQ^2 = 9 + 16 - 24\cos\frac\pi3 = 13$ and area $OPQ = \frac12\cdot 12\sin\frac\pi3 = 3\sqrt3$.

**Converting curves.** Replace $x, y$ by $r\cos\theta, r\sin\theta$, or use $r^2 = x^2 + y^2$, $r\cos\theta = x$, $r\sin\theta = y$ in the other direction:

| Cartesian | Polar |
|:---|:---|
| $x^2 + y^2 = a^2$ | $r = a$ |
| $x^2 + y^2 = 2ax$ | $r = 2a\cos\theta$ |
| $x^2 - y^2 = a^2$ | $r^2\cos 2\theta = a^2$ |
| $y = x\tan\alpha$ | $\theta = \alpha$ |

:::caution
When you divide by $r$ (e.g. $r^2 = 2ar\cos\theta \Rightarrow r = 2a\cos\theta$), check the pole is not lost. Here it is not: $\theta = \frac\pi2$ gives $r = 0$. Tracing polar curves and finding areas in polar coordinates ($\frac12\int r^2\,d\theta$) belong to the calculus topics.
:::

## The straight line {#straight-line}

**Normal form.** Let $p$ be the length of the perpendicular $ON$ from the pole to the line, and $\alpha$ the angle $XON$. For any point $P(r, \theta)$ of the line, triangle $ONP$ is right-angled at $N$, so

$$r\cos(\theta - \alpha) = p.$$

In Cartesian form this is $x\cos\alpha + y\sin\alpha = p$.

**General form.** Any line not through the pole can be written
$$\frac1r = A\cos\theta + B\sin\theta \quad(\Leftrightarrow\ Ax + By = 1),$$
and a line through the pole is $\theta = \text{const}$.

**Reducing to normal form.** Divide $r(a\cos\theta + b\sin\theta) = c$ ($c > 0$) by $\sqrt{a^2 + b^2}$: $p = \dfrac{c}{\sqrt{a^2 + b^2}}$ and $(\cos\alpha, \sin\alpha) = \dfrac{(a, b)}{\sqrt{a^2 + b^2}}$. Example: $r(\cos\theta + \sqrt3\sin\theta) = 3$ becomes $r\cos(\theta - \frac\pi3) = \frac32$.

**Related lines.** If $r\cos(\theta - \alpha) = p$ is given:

- a **parallel** line is $r\cos(\theta - \alpha) = p'$;
- a **perpendicular** line is $r\sin(\theta - \alpha) = p'$ (that is, $r\cos(\theta - \alpha \mp \frac\pi2) = \pm p'$).

**Line through two points** $(r_1, \theta_1)$ and $(r_2, \theta_2)$:

$$\frac{\sin(\theta_2 - \theta_1)}{r} = \frac{\sin(\theta - \theta_1)}{r_2} + \frac{\sin(\theta_2 - \theta)}{r_1}.$$

It comes from splitting triangle $OP_1P_2$ into $OP_1P$ and $OPP_2$ by the area formula.

:::exam-tip
To read a polar line quickly, convert: $r\cos(\theta - \frac\pi3) = 4$ is $\frac12 x + \frac{\sqrt3}{2}y = 4$, i.e. $x + \sqrt3 y = 8$. The distance from the pole is $p = 4$ and the foot of the perpendicular is the point $(4, \frac\pi3)$.
:::

:::caution
In the normal form $p \ge 0$. If the right side comes out negative, add $\pi$ to $\alpha$ rather than leaving $p < 0$.
:::

## The circle {#circle}

**General circle.** Let the centre be $C(c, \alpha)$ and the radius $a$. The cosine rule in triangle $OCP$ gives

$$r^2 - 2cr\cos(\theta - \alpha) + c^2 - a^2 = 0.$$

For a given $\theta$ this is a quadratic in $r$. Its two roots are the distances from the pole to the two points where the ray meets the circle, and their product $c^2 - a^2$ is the **power of the pole** (constant, as in the intersecting-chords theorem).

**Special cases.**

| Circle | Polar equation |
|:---|:---|
| centre the pole, radius $a$ | $r = a$ |
| through the pole, centre $(a, \alpha)$ | $r = 2a\cos(\theta - \alpha)$ |
| through the pole, centre on the initial line | $r = 2a\cos\theta$ |
| through the pole, centre on $\theta = \frac\pi2$ | $r = 2a\sin\theta$ |

The diameter through the pole has length $2a$; any chord through the pole at angle $\theta$ has length $2a\cos(\theta - \alpha)$ (angle in a semicircle).

Example: $r = 6\sin\theta$ gives $x^2 + y^2 = 6y$, a circle with centre $(0, 3)$ (polar $(3, \frac\pi2)$) and radius $3$.

Example: a circle through the pole with centre on the initial line that passes through $(4, \frac\pi3)$: $4 = 2a\cos\frac\pi3 = a$, so $r = 8\cos\theta$.

**General form.** $r = A\cos\theta + B\sin\theta$ is the circle through the pole $x^2 + y^2 = Ax + By$, with centre $\left(\frac A2, \frac B2\right)$ and radius $\frac12\sqrt{A^2 + B^2}$. Through $(2, 0)$ and $(2, \frac\pi2)$: $r = 2\cos\theta + 2\sin\theta = 2\sqrt2\cos(\theta - \frac\pi4)$.

**Tangent to $r = 2a\cos\theta$** at the point with vectorial angle $\alpha$: the radius to that point makes angle $2\alpha$ with the initial line, so

$$r\cos(\theta - 2\alpha) = 2a\cos^2\alpha.$$

:::caution
In $r^2 - 2cr\cos(\theta - \alpha) + c^2 - a^2 = 0$, the constant term is $c^2 - a^2$ (pole's distance to centre squared minus radius squared), not $a^2 - c^2$. For $r^2 - 4r\cos\theta + 3 = 0$: $c = 2$, $c^2 - a^2 = 3$, so the radius is $1$.
:::

## The conic with a focus as pole {#conic-focus-pole}

Let a conic have focus $S$, eccentricity $e$ and directrix at distance $d$ from $S$. Take $S$ as pole and the axis as initial line, **directed from the focus towards that directrix**. For $P(r, \theta)$ the distance to the directrix is $d - r\cos\theta$, so $SP = e\cdot PM$ gives

$$r = e(d - r\cos\theta) \iff \boxed{\dfrac lr = 1 + e\cos\theta}, \qquad l = ed.$$

At $\theta = \pm\frac\pi2$, $r = l$: so $l$ is the **semi-latus rectum** and the latus rectum is $2l$. The directrix is $r\cos\theta = \frac le$, i.e. $\frac lr = e\cos\theta$.

**Other positions of the axis.**

| Axis direction (focus to directrix) | Equation |
|:---|:---|
| $\theta = 0$ | $\frac lr = 1 + e\cos\theta$ |
| $\theta = \pi$ | $\frac lr = 1 - e\cos\theta$ |
| $\theta = \gamma$ | $\frac lr = 1 + e\cos(\theta - \gamma)$ |
| $\theta = \frac\pi2$ | $\frac lr = 1 + e\sin\theta$ |

**Reading an equation.** Make the constant term $1$ first: $\frac{10}{r} = 3 - 2\cos\theta$ becomes $\frac{10/3}{r} = 1 - \frac23\cos\theta$, an ellipse with $e = \frac23$, $l = \frac{10}{3}$, latus rectum $\frac{20}{3}$.

**Ellipse** ($e < 1$). The vertices are at $r = \frac{l}{1 + e}$ ($\theta = 0$) and $r = \frac{l}{1 - e}$ ($\theta = \pi$), so
$$2a = \frac{2l}{1 - e^2},\qquad b = \frac{l}{\sqrt{1 - e^2}},\qquad l = \frac{b^2}{a}.$$
Example: $\frac6r = 2 + \cos\theta$ is $\frac3r = 1 + \frac12\cos\theta$: $e = \frac12$, $l = 3$, $a = 4$, $b = 2\sqrt3$, directrix $r\cos\theta = 6$.

**Parabola** ($e = 1$): $\frac lr = 1 + \cos\theta$ with $l = 2a$ for $y^2 = 4ax$. For example, $\frac2r = 1 + \cos\theta$ gives $2 = r + x$, so $y^2 = 4 - 4x$.

**Hyperbola** ($e > 1$): $r \to \infty$ when $\cos\theta = -\frac1e$, which gives the directions of the asymptotes. For $e = 2$ these are $\theta = \pm\frac{2\pi}{3}$.

```plot
title: $\frac 2r = 1 + e\cos\theta$ with the focus $S$ at the pole; directrices $x = 2/e$
x: -6, 5
y: -4, 4
equal: true
t: -pi, pi
polar: 2/(1 + 0.5cos(t)) | $e = \frac12$ (ellipse)
implicit: y^2 = 4 - 4x | $e = 1$ (parabola)
point: 0, 0 | $S$
vline: 2
vline: 4
```

:::caution
For a hyperbola, $\frac lr = 1 + e\cos\theta$ with $r > 0$ gives only the branch **nearer** to the chosen focus and directrix. The other branch appears with $r < 0$, i.e. for the $\theta$ where $1 + e\cos\theta < 0$.
:::

## Chord, tangent and normal {#chord-tangent-normal}

Work with $\frac lr = 1 + e\cos\theta$; a point of the conic is named by its vectorial angle.

**Chord** joining the points $\alpha - \beta$ and $\alpha + \beta$:

$$\frac lr = e\cos\theta + \sec\beta\cos(\theta - \alpha).$$

*Proof idea.* Every line not through the pole is $\frac lr = A\cos\theta + B\sin\theta$. Choose it as $e\cos\theta + k\cos(\theta - \alpha)$; at $\theta = \alpha \pm \beta$ the conic gives $\frac lr = 1 + e\cos\theta$, so $k\cos\beta = 1$.

**Tangent** at $\alpha$ (let $\beta \to 0$):

$$\frac lr = e\cos\theta + \cos(\theta - \alpha).$$

**Normal** at $\alpha$:

$$\frac{le\sin\alpha}{1 + e\cos\alpha}\cdot\frac1r = e\sin\theta + \sin(\theta - \alpha).$$

**Tangents at $\alpha$ and $\beta$** meet where $\cos(\theta - \alpha) = \cos(\theta - \beta)$, i.e. at
$$\theta = \frac{\alpha + \beta}{2},\qquad \frac lr = e\cos\frac{\alpha + \beta}{2} + \cos\frac{\alpha - \beta}{2}.$$

**Condition of tangency.** The tangent at $\alpha$ is $\frac lr = (e + \cos\alpha)\cos\theta + \sin\alpha\sin\theta$. So the line $\frac lr = A\cos\theta + B\sin\theta$ touches the conic if and only if
$$(A - e)^2 + B^2 = 1.$$

**Worked example.** Take $\frac2r = 1 + \cos\theta$, i.e. $y^2 = 4 - 4x$.

- The point $\alpha = \frac\pi2$ is $(0, 2)$. The tangent there is $\frac2r = \cos\theta + \sin\theta$, i.e. $x + y = 2$.
- The normal there is $\frac2r = \sin\theta - \cos\theta$, i.e. $y = x + 2$.
- The chord joining $\theta = 0$ and $\theta = \frac\pi2$ has $\alpha = \beta = \frac\pi4$: $\frac2r = \cos\theta + \sqrt2\cos(\theta - \frac\pi4) = 2\cos\theta + \sin\theta$, i.e. $2x + y = 2$.
- The tangents at $\pm\frac\pi3$ meet at $\theta = 0$, $\frac2r = 1 + \frac12$, i.e. at $(\frac43, 0)$.

:::exam-tip
Check any polar answer by converting: $\frac lr = A\cos\theta + B\sin\theta$ is simply $Ax + By = l$. Then test that the line passes through the point $\left(\frac{l\cos\alpha}{1 + e\cos\alpha}, \frac{l\sin\alpha}{1 + e\cos\alpha}\right)$.
:::

:::caution
The chord formula uses the **half-difference** $\beta$, not the difference: for the points $0$ and $\frac\pi2$, $\beta = \frac\pi4$ and $\sec\beta = \sqrt2$.
:::

## Focal chords {#focal-chords}

A **focal chord** is a chord through the focus. With the focus as pole, its ends are at $\theta$ and $\theta + \pi$:

$$SP = \frac{l}{1 + e\cos\theta},\qquad SQ = \frac{l}{1 - e\cos\theta}.$$

:::keyfacts
- **Harmonic mean property.** $\dfrac1{SP} + \dfrac1{SQ} = \dfrac2l$: the semi-latus rectum is the harmonic mean of the segments of every focal chord. So $l = \dfrac{2\,SP\cdot SQ}{SP + SQ}$.
- **Length** of the focal chord inclined at $\theta$ to the axis: $PQ = \dfrac{2l}{1 - e^2\cos^2\theta}$.
- **Ellipse:** $PQ$ is least when $\cos\theta = 0$ (the latus rectum, $2l$) and greatest along the axis (the major axis, $\frac{2l}{1 - e^2} = 2a$).
- **Parabola** ($e = 1$, $l = 2a$): $PQ = \dfrac{2l}{\sin^2\theta} = 4a\operatorname{cosec}^2\theta \ge 4a$.
- **Perpendicular focal chords** $PQ$ and $RT$: replacing $\theta$ by $\theta + \frac\pi2$,
  $$\frac1{PQ} + \frac1{RT} = \frac{2 - e^2}{2l},\qquad \frac1{SP\cdot SQ} + \frac1{SR\cdot ST} = \frac{2 - e^2}{l^2}.$$
- The **tangents at the ends of a focal chord** (points $\alpha$ and $\alpha + \pi$) meet on the corresponding **directrix**. Adding $\frac lr = e\cos\theta \pm \cos(\theta - \alpha)$ gives $\frac lr = e\cos\theta$. For the parabola they also meet at right angles.
:::

Example: a focal chord of a parabola has segments $3$ and $6$. Then $l = \frac{2\cdot 18}{9} = 4$ and the latus rectum is $8$.

Example: for $\frac6r = 2 + \cos\theta$ ($l = 3$, $e = \frac12$), the focal chord at $\frac\pi3$ to the axis has length $\dfrac{6}{1 - \frac14\cdot\frac14} = \dfrac{32}{5}$.

:::caution
The length formula has $\cos^2\theta$ where $\theta$ is measured from the **axis**. Using $\sin^2\theta$ gives the chord perpendicular to the one asked for. For a hyperbola, a focal chord whose ends lie on different branches has $1 - e^2\cos^2\theta < 0$; its length is $\frac{2l}{\lvert 1 - e^2\cos^2\theta\rvert}$, and the harmonic-mean relation then holds with a signed segment.
:::

## Quick checks and traps {#exam-tips}

- **Normalise first.** In $\frac kr = m + n\cos\theta$, divide by $m$: $e = \frac nm$, $l = \frac km$. Classify by $e$ only after this step. $\frac8r = 2 + 4\cos\theta$ has $e = 2$, not $4$.
- **Latus rectum is $2l$**, not $l$.
- **Sum of vertex distances** $\frac{l}{1 + e} + \frac{l}{1 - e} = 2a$ gives the major axis of an ellipse in one line.
- **Line:** $r\cos(\theta - \alpha) = p$ means distance $p$ from the pole, foot at $(p, \alpha)$. The general line $\frac lr = A\cos\theta + B\sin\theta$ is $Ax + By = l$.
- **Circle through the pole:** $r = 2a\cos(\theta - \alpha)$ has radius $a$, not $2a$; the centre is $(a, \alpha)$.
- **Tangent at $\alpha$:** $\frac lr = e\cos\theta + \cos(\theta - \alpha)$. The common slip is writing $1 + \cos(\theta - \alpha)$ (copying the conic).
- **Tangency test:** $(A - e)^2 + B^2 = 1$.
- **Focal chords:** $\frac1{SP} + \frac1{SQ} = \frac2l$; length $\frac{2l}{1 - e^2\cos^2\theta}$; perpendicular pair $\frac{2 - e^2}{2l}$.
- **Principal polar coordinates:** place $\theta$ by quadrant; $\tan^{-1}\frac yx$ alone is wrong in quadrants II and III.
- Cartesian forms of conics and their tangents are in the topics on transformation of axes and on tangents and polars.
