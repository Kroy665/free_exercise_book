# Complex Numbers and De Moivre's Theorem

## Definition and algebra {#definition}

A **complex number** is an ordered pair $(a, b)$ of real numbers. The set $\C$ of all such pairs has two operations:

$$(a, b) + (c, d) = (a + c,\; b + d), \qquad (a, b)\cdot(c, d) = (ac - bd,\; ad + bc).$$

- $(a, 0)$ behaves exactly like the real number $a$, so $\R \subset \C$.
- Write $i = (0, 1)$. Then $i^2 = (0,1)(0,1) = (-1, 0) = -1$, and every $(a, b) = a + ib$.
- **Real part** $\operatorname{Re} z = a$; **imaginary part** $\operatorname{Im} z = b$ (a real number, not $ib$).
- Equality: $a + ib = c + id \iff a = c$ and $b = d$.

With these operations $\C$ is a **field**. The zero is $(0,0)$, and the inverse of $z = a + ib \neq 0$ is

$$z^{-1} = \frac{a - ib}{a^2 + b^2}.$$

To divide, multiply the numerator and denominator by the conjugate of the denominator:

$$\frac{3 + 4i}{1 - 2i} = \frac{(3 + 4i)(1 + 2i)}{1 + 4} = \frac{-5 + 10i}{5} = -1 + 2i.$$

**Powers of $i$** repeat with period 4: $i, -1, -i, 1$. So $i^n$ depends only on $n \bmod 4$, and $i^n + i^{n+1} + i^{n+2} + i^{n+3} = 0$.

:::caution
$\C$ **cannot be ordered**: no ordering makes it an ordered field. In an ordered field every nonzero square is positive. Then $1 = 1^2 > 0$ and $-1 = i^2 > 0$ would both hold, a contradiction. So "$z_1 < z_2$" has no meaning for non-real numbers; only moduli can be compared.
:::

:::exam-tip
The ordered-pair definition is examined directly: know the product rule $(a,b)(c,d) = (ac - bd,\, ad + bc)$ and that $i = (0, 1)$.
:::

## Conjugate, modulus and amplitude {#modulus-argument}

For $z = x + iy$:

- **Conjugate:** $\bar z = x - iy$ (reflection in the real axis).
- **Modulus:** $|z| = \sqrt{x^2 + y^2}$ (distance from the origin).
- **Amplitude (argument):** any $\theta$ with $x = |z|\cos\theta$, $y = |z|\sin\theta$. The **principal value** $\arg z$ is the one in $(-\pi, \pi]$. $\arg 0$ is undefined.

**Polar form:** $z = r(\cos\theta + i\sin\theta)$, with $r = |z|$. This is often shortened to $r\operatorname{cis}\theta$ or $re^{i\theta}$.

To find the principal argument, take $\alpha = \tan^{-1}\left|\frac{y}{x}\right|$ and place it by quadrant:

| Quadrant of $z$ | $\arg z$ |
|:---|:---|
| I ($x > 0, y \ge 0$) | $\alpha$ |
| II ($x < 0, y \ge 0$) | $\pi - \alpha$ |
| III ($x < 0, y < 0$) | $-\pi + \alpha$ |
| IV ($x > 0, y < 0$) | $-\alpha$ |

Example: $-1 - i\sqrt3$ is in quadrant III, $\alpha = \pi/3$, so $\arg = -2\pi/3$. (The value $4\pi/3$ is an amplitude but not the principal one.)

**Properties.** The modulus properties hold exactly; the argument properties hold only up to multiples of $2\pi$.

| Modulus | Argument (mod $2\pi$) |
|:---|:---|
| $\lvert z_1 z_2\rvert = \lvert z_1\rvert\,\lvert z_2\rvert$ | $\arg(z_1 z_2) \equiv \arg z_1 + \arg z_2$ |
| $\left\lvert z_1/z_2\right\rvert = \lvert z_1\rvert / \lvert z_2\rvert$ | $\arg(z_1/z_2) \equiv \arg z_1 - \arg z_2$ |
| $\lvert \bar z\rvert = \lvert z\rvert$, $\;z\bar z = \lvert z\rvert^2$ | $\arg \bar z = -\arg z$ (for $z$ not a negative real) |
| $\lvert z^n\rvert = \lvert z\rvert^n$ | $\arg z^n \equiv n \arg z$ |

Also: $z + \bar z = 2\operatorname{Re} z$, $\;z - \bar z = 2i\operatorname{Im} z$, $\;\overline{z_1 z_2} = \bar z_1 \bar z_2$, and $z$ is real $\iff z = \bar z$.

:::caution
With principal values, $\arg(z_1 z_2) = \arg z_1 + \arg z_2$ can **fail**. For $z_1 = z_2 = -1 + i$: $\arg z_1 + \arg z_2 = 3\pi/2$, but $z_1 z_2 = -2i$ has $\arg = -\pi/2$.
:::

## The Argand plane: distance and loci {#argand-geometry}

Plot $z = x + iy$ as the point $(x, y)$. Then:

- $|z_1 - z_2|$ is the **distance** between $z_1$ and $z_2$.
- The point dividing $z_1 z_2$ internally in the ratio $m:n$ is $\dfrac{m z_2 + n z_1}{m + n}$.
- **Triangle inequality:** $\big||z_1| - |z_2|\big| \le |z_1 \pm z_2| \le |z_1| + |z_2|$.
- **Parallelogram law:** $|z_1 + z_2|^2 + |z_1 - z_2|^2 = 2\left(|z_1|^2 + |z_2|^2\right)$.

**Standard loci** ($a, b$ fixed, $r, k > 0$):

| Condition | Locus |
|:---|:---|
| $\lvert z - a\rvert = r$ | circle, centre $a$, radius $r$ |
| $\lvert z - a\rvert = \lvert z - b\rvert$ | perpendicular bisector of the segment $ab$ |
| $\lvert z - a\rvert = k\lvert z - b\rvert,\ k \ne 1$ | a circle (circle of Apollonius) |
| $\lvert z - a\rvert + \lvert z - b\rvert = 2c > \lvert a - b\rvert$ | ellipse with foci $a, b$ |
| $\arg\dfrac{z - a}{z - b} = \alpha$ | arc of a circle through $a$ and $b$ |

**Rotation.** Multiplying by $e^{i\alpha} = \cos\alpha + i\sin\alpha$ rotates a point anticlockwise about the origin through $\alpha$, without changing its modulus. Multiplying by $i$ rotates through $\pi/2$: $i(1 + 2i) = -2 + i$.

Similarly, if $z_3 - z_1 = \dfrac{|z_3 - z_1|}{|z_2 - z_1|}\,e^{i\alpha}(z_2 - z_1)$, then the angle from the vector $z_1z_2$ to $z_1z_3$ is $\alpha$. Two consequences:

- $z_1, z_2, z_3$ are **collinear** $\iff \dfrac{z_3 - z_1}{z_2 - z_1}$ is real.
- They form an **equilateral triangle** $\iff z_1^2 + z_2^2 + z_3^2 = z_1z_2 + z_2z_3 + z_3z_1$.

:::exam-tip
For $|z - a| = k|z - b|$, square both sides with $z = x + iy$ and complete the square. For example, $|z - 1| = 2|z + 1|$ gives $x^2 + y^2 + \tfrac{10}{3}x + 1 = 0$: a circle with centre $(-\tfrac53, 0)$ and radius $\tfrac43$.
:::

## De Moivre's theorem {#de-moivre}

:::keyfacts
- **Integer index.** For every integer $n$: $(\cos\theta + i\sin\theta)^n = \cos n\theta + i\sin n\theta$.
- **Rational index.** For $p/q$ in lowest terms ($q > 0$), $(\cos\theta + i\sin\theta)^{p/q}$ has exactly **$q$ distinct values**:
  $$\cos\frac{p(\theta + 2k\pi)}{q} + i\sin\frac{p(\theta + 2k\pi)}{q}, \qquad k = 0, 1, \dots, q - 1.$$
:::

**Proof idea.** For $n \ge 0$ use induction: multiplying moduli and adding angles gives $\operatorname{cis}\theta \cdot \operatorname{cis} n\theta = \operatorname{cis}(n + 1)\theta$. For negative $n = -m$, use $\dfrac{1}{\operatorname{cis}\theta} = \operatorname{cis}(-\theta)$.

Useful consequences:

- $(\cos\theta - i\sin\theta)^n = \cos n\theta - i\sin n\theta$.
- $(\cos\alpha + i\sin\alpha)(\cos\beta + i\sin\beta) = \cos(\alpha + \beta) + i\sin(\alpha + \beta)$.
- If $z = \cos\theta + i\sin\theta$, then
  $$z^n + \frac{1}{z^n} = 2\cos n\theta, \qquad z^n - \frac{1}{z^n} = 2i\sin n\theta.$$

**Powers via polar form.** Convert, apply the theorem, convert back:

$$(1 + i)^{10} = \left(\sqrt2\right)^{10}\left(\cos\frac{10\pi}{4} + i\sin\frac{10\pi}{4}\right) = 32\left(\cos\frac{\pi}{2} + i\sin\frac{\pi}{2}\right) = 32i.$$

$$\left(\frac{1 + i\sqrt3}{1 - i\sqrt3}\right)^{6} = \left(\frac{2\operatorname{cis}(\pi/3)}{2\operatorname{cis}(-\pi/3)}\right)^{6} = \operatorname{cis}\,4\pi = 1.$$

:::caution
$(\cos\theta + i\sin\theta)^{1/q}$ is **many-valued**. "Find all values" means listing all $q$ of them. Rules like $(z^a)^b = z^{ab}$ need care for non-integer exponents.
:::

## nth roots and roots of unity {#roots}

The equation $z^n = w$, with $w = R\operatorname{cis}\phi \neq 0$, has exactly $n$ roots:

$$z_k = R^{1/n}\operatorname{cis}\frac{\phi + 2k\pi}{n}, \qquad k = 0, 1, \dots, n - 1.$$

They lie on the circle $|z| = R^{1/n}$ and form a **regular $n$-gon**.

**Roots of unity.** The roots of $z^n = 1$ are $1, \alpha, \alpha^2, \dots, \alpha^{n-1}$, where $\alpha = \operatorname{cis}(2\pi/n)$. They satisfy:

- **Sum:** $1 + \alpha + \cdots + \alpha^{n-1} = 0$ (for $n \ge 2$).
- **Product of all $n$ roots:** $(-1)^{n-1}$.
- **Power sums:** $\sum_{k=0}^{n-1}\alpha^{km} = n$ if $n \mid m$, and $0$ otherwise.
- $z^n - 1 = \prod_{k=0}^{n-1}(z - \alpha^k)$. Dividing by $z - 1$ and putting $z = 1$ gives $\prod_{k=1}^{n-1}(1 - \alpha^k) = n$.
- They form a **cyclic group under multiplication**, not under addition.

**Cube roots of unity:** $1,\ \omega = \dfrac{-1 + i\sqrt3}{2},\ \omega^2 = \dfrac{-1 - i\sqrt3}{2}$.

$$1 + \omega + \omega^2 = 0,\quad \omega^3 = 1,\quad \bar\omega = \omega^2,\quad 1 + \omega = -\omega^2,\quad (1 - \omega)(1 - \omega^2) = 3.$$

Reduce powers using $\omega^{3k} = 1$, so $\omega^{100} = \omega^{99}\cdot\omega = \omega$.

```plot
title: The sixth roots of unity form a regular hexagon on $|z| = 1$
x: -1.6, 1.6
y: -1.4, 1.4
equal: true
implicit: x^2 + y^2 = 1 | $|z| = 1$
point: 1, 0 | 1
point: 0.5, sqrt(3)/2 | $\alpha$
point: -0.5, sqrt(3)/2 | $\alpha^2$
point: -1, 0 | $-1$
point: -0.5, -sqrt(3)/2 | $\alpha^4$
point: 0.5, -sqrt(3)/2 | $\alpha^5$
xlabel: Re
ylabel: Im
```

:::exam-tip
Cube roots of $-8$: $-8 = 8\operatorname{cis}\pi$, so the roots are $2\operatorname{cis}\frac{\pi + 2k\pi}{3}$. These are $1 + i\sqrt3$, $-2$ and $1 - i\sqrt3$. Check a candidate quickly by cubing its polar form.
:::

## Multiple-angle expansions {#trig-expansions}

**$\cos n\theta$ and $\sin n\theta$ in powers.** Expand $(\cos\theta + i\sin\theta)^n$ binomially and compare real and imaginary parts. Write $c = \cos\theta$, $s = \sin\theta$:

$$\cos 3\theta = 4c^3 - 3c, \qquad \sin 3\theta = 3s - 4s^3,$$
$$\cos 5\theta = 16c^5 - 20c^3 + 5c, \qquad \frac{\sin 5\theta}{\sin\theta} = 16c^4 - 12c^2 + 1.$$

In general:

$$\cos n\theta = c^n - \binom n2 c^{n-2}s^2 + \binom n4 c^{n-4}s^4 - \cdots,$$
$$\sin n\theta = \binom n1 c^{n-1}s - \binom n3 c^{n-3}s^3 + \cdots.$$

$$\tan n\theta = \frac{\binom n1 t - \binom n3 t^3 + \cdots}{1 - \binom n2 t^2 + \binom n4 t^4 - \cdots}, \qquad t = \tan\theta.$$

**Powers in multiple angles.** With $z = \operatorname{cis}\theta$, we have $2\cos\theta = z + z^{-1}$ and $2i\sin\theta = z - z^{-1}$. Expand, then pair $z^k$ with $z^{-k}$:

$$2^4\cos^4\theta = (z + z^{-1})^4 = (z^4 + z^{-4}) + 4(z^2 + z^{-2}) + 6 = 2\cos 4\theta + 8\cos 2\theta + 6,$$

$$\text{so}\quad \cos^4\theta = \frac{\cos 4\theta + 4\cos 2\theta + 3}{8}.$$

Similarly, $\sin^3\theta = \dfrac{3\sin\theta - \sin 3\theta}{4}$ and $\cos^3\theta = \dfrac{3\cos\theta + \cos 3\theta}{4}$.

:::exam-tip
Check any expansion at $\theta = 0$. Since $\frac{\sin 5\theta}{\sin\theta} \to 5$, the formula must give $16 - 12 + 1 = 5$. This eliminates most wrong options in seconds.
:::

## Quick checks and traps {#exam-tips}

- **Modulus first.** $\left|\frac{3 + 4i}{1 - i}\right| = \frac{5}{\sqrt2}$, with no division needed.
- **Principal argument:** state it in $(-\pi, \pi]$; $4\pi/3$ is not principal.
- **If $|z| = 1$,** then $\bar z = 1/z$, and $\frac{z - 1}{z + 1} = i\tan\frac{\theta}{2}$ is purely imaginary (for $z \ne -1$).
- **Sums of powers of $i$:** every block of 4 consecutive powers sums to $0$. So $i + i^2 + \cdots + i^{2026}$ = the last two terms = $i + i^2 = -1 + i$.
- **Product of all values of $(-1)^{1/4}$:** these are the roots of $z^4 + 1 = 0$, so the product is the constant term $= 1$.
- **Rational powers:** $(\ldots)^{p/q}$ in lowest terms has $q$ values. For example, $(1 + i)^{2/3}$ has 3 values.
- **Group facts:** the $n$th roots of unity form a cyclic group of order $n$ under multiplication.
