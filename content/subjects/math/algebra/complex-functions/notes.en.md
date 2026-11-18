# Functions of a Complex Variable

## The exponential function {#exponential}

**Conventions used in this topic.** $z = x + iy$ with $x, y$ real; $\ln$ is the real natural logarithm; $\operatorname{Arg} z$ is the principal argument in $(-\pi, \pi]$; $\log z$ is the many-valued logarithm and $\operatorname{Log} z$ its principal value. Polar form and De Moivre's theorem are in the previous topic.

**Definition.** For $z = x + iy$,

$$e^z = \exp z = e^x(\cos y + i\sin y).$$

For real $z$ this is the usual $e^x$. For $z = iy$ it gives **Euler's formula**

$$e^{iy} = \cos y + i\sin y, \qquad\text{so}\quad \cos y = \frac{e^{iy} + e^{-iy}}{2},\quad \sin y = \frac{e^{iy} - e^{-iy}}{2i}.$$

Special values: $e^{i\pi} = -1$, $e^{i\pi/2} = i$, $e^{2\pi i} = 1$.

:::keyfacts
- $\lvert e^z\rvert = e^x = e^{\operatorname{Re} z}$, and $y = \operatorname{Im} z$ is an argument of $e^z$.
- $e^{z_1}e^{z_2} = e^{z_1 + z_2}$, $\;1/e^z = e^{-z}$, $\;\overline{e^z} = e^{\bar z}$.
- $e^z \neq 0$ for every $z$, because $\lvert e^z\rvert = e^x > 0$.
- **Periodic with period $2\pi i$:** $e^{z + 2\pi i} = e^z$. Every period is $2n\pi i$, $n \in \Z$; $2\pi i$ is the fundamental period.
- $e^z = 1 \iff z = 2n\pi i$, and hence $e^{z} = e^{w} \iff z - w = 2n\pi i$.
- $e^z$ takes every non-zero complex value, infinitely often.
:::

**Solving $e^z = w$.** Write $w = \lvert w\rvert e^{i\phi}$ and compare: $e^x = \lvert w\rvert$, $y = \phi + 2n\pi$. For example, $e^z = -1$ gives $x = 0$, $y = \pi + 2n\pi$, so $z = (2n + 1)\pi i$.

**Example.** $e^{\ln 2 + i\pi/3} = 2\left(\cos\frac{\pi}{3} + i\sin\frac{\pi}{3}\right) = 1 + i\sqrt3$.

**Example.** $\lvert e^{iz}\rvert$: since $iz = -y + ix$, $\lvert e^{iz}\rvert = e^{-y}$. So $e^{iz}$ is bounded in the upper half-plane, not on all of $\C$.

:::caution
$e^z$ is **not** one-to-one on $\C$: $e^{0} = e^{2\pi i}$. So "$e^{z} = e^{w} \Rightarrow z = w$" is false; only $z - w \in 2\pi i\Z$ follows. This is why $\log$ is many-valued.
:::

:::exam-tip
The real exponential has no period; the complex one has the **imaginary** period $2\pi i$. A distractor of $2\pi$ is the usual trap: $e^{z + 2\pi} = e^{2\pi}e^z \ne e^z$.
:::

## Circular functions sin z and cos z {#circular-functions}

Euler's formula suggests the definitions, for all complex $z$:

$$\sin z = \frac{e^{iz} - e^{-iz}}{2i}, \qquad \cos z = \frac{e^{iz} + e^{-iz}}{2}, \qquad \tan z = \frac{\sin z}{\cos z}.$$

$\sec z$, $\operatorname{cosec} z$ and $\cot z$ are defined as usual, wherever the denominator is non-zero.

**What survives from the real case.** All the algebraic identities carry over, because they follow from $e^{a}e^{b} = e^{a+b}$:

- $\sin^2 z + \cos^2 z = 1$;
- the addition formulae $\sin(z_1 \pm z_2)$, $\cos(z_1 \pm z_2)$ and $\tan(z_1 \pm z_2)$;
- $\sin(-z) = -\sin z$, $\cos(-z) = \cos z$;
- period $2\pi$ for $\sin$ and $\cos$, and period $\pi$ for $\tan$.

**Zeros.** $\sin z = 0 \iff z = n\pi$, and $\cos z = 0 \iff z = \left(n + \tfrac12\right)\pi$, $n \in \Z$. **The only zeros are the real ones.** Proof idea: $\sin z = 0 \iff e^{2iz} = 1 \iff 2iz = 2n\pi i$.

**What fails: boundedness.** On the imaginary axis,

$$\cos(iy) = \frac{e^{-y} + e^{y}}{2} = \cosh y, \qquad \sin(iy) = \frac{e^{-y} - e^{y}}{2i} = i\sinh y.$$

Both grow like $\tfrac12 e^{\lvert y\rvert}$. So $\sin z$ and $\cos z$ are **unbounded** on $\C$, and equations like $\cos z = 2$ have solutions. More precisely,

$$\lvert\sin z\rvert^2 = \sin^2 x + \sinh^2 y, \qquad \lvert\cos z\rvert^2 = \cos^2 x + \sinh^2 y.$$

**Example: solve $\cos z = 2$.** Write $\cos z = \cos x\cosh y - i\sin x\sinh y = 2$.

- The imaginary part gives $\sin x\sinh y = 0$. If $y = 0$, then $\cos x = 2$, which is impossible. So $\sin x = 0$, i.e. $x = m\pi$.
- The real part gives $\cos x\cosh y = 2$. Since $\cosh y > 0$, $\cos x = 1$, so $x = 2n\pi$, and $\cosh y = 2$.
- $\cosh y = 2$ gives $y = \pm\ln(2 + \sqrt3)$.

So $z = 2n\pi \pm i\ln(2 + \sqrt3)$.

:::caution
$\lvert\sin z\rvert \le 1$ and $\lvert\cos z\rvert \le 1$ are true only for **real** $z$. For example, $\lvert\sin 2i\rvert = \sinh 2 \approx 3.63$.
:::

:::exam-tip
Liouville's theorem (a bounded entire function is constant) also explains why $\sin z$ must be unbounded. For an SLST question, quoting $\cos(iy) = \cosh y$ is enough.
:::

## Hyperbolic functions {#hyperbolic-functions}

For all complex $z$:

$$\sinh z = \frac{e^{z} - e^{-z}}{2}, \qquad \cosh z = \frac{e^{z} + e^{-z}}{2}, \qquad \tanh z = \frac{\sinh z}{\cosh z}.$$

**The bridge to circular functions.** Replace $z$ by $iz$ in the definitions:

| Circular of $iz$ | Hyperbolic of $iz$ |
|:---|:---|
| $\sin(iz) = i\sinh z$ | $\sinh(iz) = i\sin z$ |
| $\cos(iz) = \cosh z$ | $\cosh(iz) = \cos z$ |
| $\tan(iz) = i\tanh z$ | $\tanh(iz) = i\tan z$ |

Equivalently, $\sinh z = -i\sin(iz)$ and $\cosh z = \cos(iz)$. Any circular identity becomes a hyperbolic one by this substitution (**Osborn's rule**: change the sign of every term containing a product of two $\sinh$ factors). For example:

- $\cos^2 z + \sin^2 z = 1$ becomes $\cosh^2 z - \sinh^2 z = 1$;
- $\cos 2z = 1 - 2\sin^2 z$ becomes $\cosh 2z = 1 + 2\sinh^2 z$;
- $\sinh(z_1 + z_2) = \sinh z_1\cosh z_2 + \cosh z_1\sinh z_2$;
- $\cosh(z_1 + z_2) = \cosh z_1\cosh z_2 + \sinh z_1\sinh z_2$.

**Periods and zeros.** Because they are built from $e^{z}$:

- $\sinh z$ and $\cosh z$ have period $2\pi i$, and $\tanh z$ has period $\pi i$.
- $\sinh z = 0 \iff z = n\pi i$, and $\cosh z = 0 \iff z = \left(n + \tfrac12\right)\pi i$.

So the zeros of the hyperbolic functions lie on the **imaginary** axis; only $z = 0$ is real.

**Example: solve $\sinh z = i$.** $\sinh z = -i\sin(iz) = i$ gives $\sin(iz) = -1$. So $iz = -\frac{\pi}{2} + 2n\pi$, i.e.

$$z = i\left(\frac{\pi}{2} + 2n\pi\right) = \frac{(4n + 1)\pi i}{2}, \qquad n \in \Z.$$

Check: $\sinh\frac{\pi i}{2} = i\sin\frac{\pi}{2} = i$. Note that $\frac{3\pi i}{2}$ is **not** a solution: $\sinh\frac{3\pi i}{2} = -i$.

**Real arguments.** For real $x$, $\cosh x \ge 1$ and $\sinh x$ takes every real value. On the real line, $\sinh$ is one-to-one, and $\cosh$ is one-to-one on $[0, \infty)$. This is what makes the real inverses $\ln(x + \sqrt{x^2 + 1})$ and $\ln(x + \sqrt{x^2 - 1})$ single-valued.

:::caution
Watch the sign in $\cosh^2 z - \sinh^2 z = 1$ (minus) against $\cos^2 z + \sin^2 z = 1$ (plus). Also, $\sin(iz) = i\sinh z$, **not** $-i\sinh z$ and not $\sinh z$.
:::

## The logarithm {#logarithm}

**Definition.** For $z \neq 0$, a **logarithm** of $z$ is any $w$ with $e^w = z$. Writing $w = u + iv$ gives $e^u = \lvert z\rvert$ and $v \equiv \arg z \pmod{2\pi}$. So

$$\log z = \ln\lvert z\rvert + i\left(\operatorname{Arg} z + 2n\pi\right), \qquad n \in \Z.$$

$\log z$ is **many-valued**: its values are spaced $2\pi i$ apart on a vertical line. $\log 0$ is undefined, because $e^w \ne 0$.

**Principal value.** Take $n = 0$:

$$\operatorname{Log} z = \ln\lvert z\rvert + i\operatorname{Arg} z, \qquad -\pi < \operatorname{Arg} z \le \pi.$$

So $\operatorname{Im}\operatorname{Log} z \in (-\pi, \pi]$, and $\log z = \operatorname{Log} z + 2n\pi i$.

| $z$ | $\operatorname{Log} z$ | all values $\log z$ |
|:---|:---|:---|
| $-1$ | $i\pi$ | $(2n + 1)\pi i$ |
| $i$ | $\dfrac{i\pi}{2}$ | $\left(2n + \tfrac12\right)\pi i$ |
| $-i$ | $-\dfrac{i\pi}{2}$ | $\left(2n - \tfrac12\right)\pi i$ |
| $1 + i$ | $\tfrac12\ln 2 + \dfrac{i\pi}{4}$ | $\tfrac12\ln 2 + i\left(2n + \tfrac14\right)\pi$ |
| $-e$ | $1 + i\pi$ | $1 + (2n + 1)\pi i$ |

**Example.** $\operatorname{Log}(\operatorname{Log} i) = \operatorname{Log}\frac{i\pi}{2} = \ln\frac{\pi}{2} + \frac{i\pi}{2}$.

**Laws of logarithms.**

- **As sets, they hold:** $\log(z_1 z_2) = \log z_1 + \log z_2$ and $\log(z_1/z_2) = \log z_1 - \log z_2$. Every value on one side is a value on the other.
- **For principal values, they can fail:** $\operatorname{Log}(z_1 z_2) = \operatorname{Log} z_1 + \operatorname{Log} z_2 + 2k\pi i$, where $k \in \{-1, 0, 1\}$ is chosen to bring the imaginary part into $(-\pi, \pi]$.
- **Powers:** $\log(z^2)$ and $2\log z$ are **different sets**. $2\log z$ contains only the even multiples of $2\pi i$ added to $2\operatorname{Log} z$.

**Counterexample.** Take $z_1 = z_2 = -1 + i$. Then $\operatorname{Log} z_1 + \operatorname{Log} z_2 = \ln 2 + \frac{3\pi i}{2}$. But $z_1z_2 = -2i$, so $\operatorname{Log}(z_1z_2) = \ln 2 - \frac{\pi i}{2}$. The difference is $2\pi i$.

Similarly, with $z = i$: $\log(i^2) = \log(-1) = \{(2n + 1)\pi i\}$ contains $3\pi i$, but $2\log i = \{(4n + 1)\pi i\}$ does not.

:::caution
$e^{\operatorname{Log} z} = z$ always holds. But $\operatorname{Log}(e^z) = z$ holds **only** when $-\pi < \operatorname{Im} z \le \pi$. For example, $\operatorname{Log}(e^{2\pi i}) = \operatorname{Log} 1 = 0$.
:::

:::exam-tip
"Log" in a question means the principal value, while "log" may mean the general value. Read the options: if they contain $n$, the general value is wanted.
:::

## General powers a^z {#general-power}

**Definition.** For $a \neq 0$ and any complex $z$,

$$a^z = e^{z\log a} = e^{z(\operatorname{Log} a + 2n\pi i)}, \qquad n \in \Z.$$

The **principal value** takes $n = 0$: $a^z = e^{z\operatorname{Log} a}$. When $a$ is a positive real, the principal value is $e^{z\ln a}$; for $a = e$ the symbol $e^z$ always means $\exp z$.

**How many values?** The values differ by the factors $e^{2n\pi i z}$:

| Exponent $z$ | Number of distinct values of $a^z$ |
|:---|:---|
| an integer | one (the ordinary power) |
| rational $p/q$ in lowest terms, $q > 0$ | exactly $q$ (as in De Moivre) |
| irrational real, or non-real | infinitely many |

**$i^i$ is real.** $\log i = i\left(\frac{\pi}{2} + 2n\pi\right)$, so

$$i^i = e^{i\cdot i(\pi/2 + 2n\pi)} = e^{-\pi/2 - 2n\pi}, \qquad n \in \Z.$$

Every value is a positive real number, and the **principal value is $e^{-\pi/2} \approx 0.208$**.

**More examples (principal values).**

- $(-1)^i = e^{i\cdot i\pi} = e^{-\pi}$.
- $2^i = e^{i\ln 2} = \cos(\ln 2) + i\sin(\ln 2)$. Its modulus is $1$.
- $1^i = e^{i\cdot 2n\pi i} = e^{-2n\pi}$, so the principal value is $1$, but there are infinitely many other (real) values.
- $(1 + i)^i = e^{i(\frac12\ln 2 + i\pi/4)} = e^{-\pi/4}\left[\cos\left(\tfrac12\ln 2\right) + i\sin\left(\tfrac12\ln 2\right)\right]$.

**Modulus and argument of a principal power.** If $a^z = e^{z\operatorname{Log} a}$ with $z = p + iq$ and $\operatorname{Log} a = \ln\lvert a\rvert + i\theta$, then

$$\lvert a^z\rvert = e^{p\ln\lvert a\rvert - q\theta}, \qquad \arg a^z = q\ln\lvert a\rvert + p\theta.$$

:::caution
The usual index laws fail for principal values. $(a^{z})^{w} = a^{zw}$ and $a^z b^z = (ab)^z$ need not hold. Example: $\left((-1)^2\right)^{1/2} = 1$, but $(-1)^{2\cdot\frac12} = -1$. Only $a^{z}a^{w} = a^{z + w}$ (same base, same branch of $\log a$) is safe.
:::

:::exam-tip
To find $a^z$, compute $\operatorname{Log} a$ first, multiply by $z$, then exponentiate: $e^{u + iv} = e^u(\cos v + i\sin v)$. Most wrong options come from dropping the $i\cdot i = -1$ in the real part.
:::

## Inverse circular and hyperbolic functions {#inverse-functions}

**Definition.** $w = \sin^{-1} z$ means $\sin w = z$ (no restriction on $w$). Each inverse is many-valued and can be written with $\log$.

**Derivation for $\sin^{-1}$.** If $\sin w = z$, then $e^{iw} - e^{-iw} = 2iz$. So $e^{2iw} - 2iz\,e^{iw} - 1 = 0$, a quadratic in $e^{iw}$:

$$e^{iw} = iz \pm \sqrt{1 - z^2}, \qquad\text{so}\quad w = -i\log\left(iz + \sqrt{1 - z^2}\right).$$

The $\pm$ is absorbed by letting $\sqrt{\ }$ take both values. The same method gives all the formulas below.

| Function | Log form | Excluded points |
|:---|:---|:---|
| $\sin^{-1} z$ | $-i\log\left(iz + \sqrt{1 - z^2}\right)$ | none |
| $\cos^{-1} z$ | $-i\log\left(z + \sqrt{z^2 - 1}\right)$ | none |
| $\tan^{-1} z$ | $\dfrac{1}{2i}\log\dfrac{1 + iz}{1 - iz} = \dfrac{i}{2}\log\dfrac{i + z}{i - z}$ | $z = \pm i$ |
| $\sinh^{-1} z$ | $\log\left(z + \sqrt{z^2 + 1}\right)$ | none |
| $\cosh^{-1} z$ | $\log\left(z + \sqrt{z^2 - 1}\right)$ | none |
| $\tanh^{-1} z$ | $\dfrac12\log\dfrac{1 + z}{1 - z}$ | $z = \pm 1$ |

**Links.** $\sinh^{-1} z = -i\sin^{-1}(iz)$, $\;\tanh^{-1} z = -i\tan^{-1}(iz)$, and $\cosh^{-1} z = \pm i\cos^{-1} z$ (as sets of values).

**General values** in terms of one value ($n \in \Z$):

- $\sin^{-1} z = n\pi + (-1)^n w_0$, where $\sin w_0 = z$;
- $\cos^{-1} z = 2n\pi \pm w_0$, where $\cos w_0 = z$;
- $\tan^{-1} z = n\pi + w_0$, where $\tan w_0 = z$;
- for the hyperbolic inverses, replace $\pi$ by $\pi i$: $\sinh^{-1} z = n\pi i + (-1)^n w_0$, $\cosh^{-1} z = 2n\pi i \pm w_0$, $\tanh^{-1} z = n\pi i + w_0$.

**Examples.**

- $\cos^{-1} 2 = -i\log(2 \pm \sqrt3) = 2n\pi \pm i\ln(2 + \sqrt3)$, since $\ln(2 - \sqrt3) = -\ln(2 + \sqrt3)$. This matches the solution of $\cos z = 2$.
- $\sinh^{-1} i = \log(i + 0) = \log i$, with principal value $\dfrac{i\pi}{2}$.
- For real $x$: $\sinh^{-1} x = \ln\left(x + \sqrt{x^2 + 1}\right)$ and, for $\lvert x\rvert < 1$, $\tanh^{-1} x = \frac12\ln\frac{1 + x}{1 - x}$.

**Why $\tan z \ne \pm i$.** In $\tan^{-1} z$, the points $z = \pm i$ make the quotient $0$ or undefined, and $\log 0$ does not exist. Directly, $\tan z = i$ gives $e^{iz} - e^{-iz} = -(e^{iz} + e^{-iz})$, i.e. $2e^{iz} = 0$, which is impossible.

:::exam-tip
To recall a log form, check it at a real point. For $\sinh^{-1}$, $z = 0$ must give $\log 1 = 0$. That rules out $\log\left(z + \sqrt{z^2 - 1}\right)$, which gives $\log i \neq 0$.
:::

## Separating real and imaginary parts {#real-imaginary-parts}

Use the addition formulas together with $\cos iy = \cosh y$ and $\sin iy = i\sinh y$. For $z = x + iy$:

$$\sin(x + iy) = \sin x\cosh y + i\cos x\sinh y,$$
$$\cos(x + iy) = \cos x\cosh y - i\sin x\sinh y,$$
$$\sinh(x + iy) = \sinh x\cos y + i\cosh x\sin y,$$
$$\cosh(x + iy) = \cosh x\cos y + i\sinh x\sin y.$$

**Tangent.** Multiply the numerator and denominator by $2\cos(x - iy)$:

$$\tan(x + iy) = \frac{\sin 2x + i\sinh 2y}{\cos 2x + \cosh 2y}.$$

**Logarithm.** $\operatorname{Log}(x + iy) = \frac12\ln(x^2 + y^2) + i\operatorname{Arg}(x + iy)$. For example, $\operatorname{Log}(1 + i) = \frac12\ln 2 + \frac{i\pi}{4}$, and $\operatorname{Log}(-3) = \ln 3 + i\pi$.

**Inverse tangent.** Let $\tan^{-1}(x + iy) = \alpha + i\beta$. Then $\tan(\alpha \pm i\beta) = x \pm iy$, and

$$\tan 2\alpha = \tan\big[(\alpha + i\beta) + (\alpha - i\beta)\big] = \frac{2x}{1 - x^2 - y^2},$$
$$\tan 2i\beta = i\tanh 2\beta = \frac{2iy}{1 + x^2 + y^2}.$$

So the **real part** satisfies $\tan 2\alpha = \dfrac{2x}{1 - x^2 - y^2}$, and the **imaginary part** is

$$\beta = \frac12\tanh^{-1}\frac{2y}{1 + x^2 + y^2} = \frac14\ln\frac{x^2 + (1 + y)^2}{x^2 + (1 - y)^2}.$$

**Classic example.** If $\cos(\alpha + i\beta) = x + iy$, then $x = \cos\alpha\cosh\beta$ and $y = -\sin\alpha\sinh\beta$. Eliminate $\alpha$ or $\beta$:

$$\frac{x^2}{\cosh^2\beta} + \frac{y^2}{\sinh^2\beta} = 1 \quad(\text{an ellipse}), \qquad \frac{x^2}{\cos^2\alpha} - \frac{y^2}{\sin^2\alpha} = 1 \quad(\text{a hyperbola}).$$

So $\cos$ maps each horizontal line $\beta = c \ne 0$ to an ellipse, and each vertical line $\alpha = c$ (not a multiple of $\pi/2$) to a hyperbola; all these conics have foci $\pm 1$.

The same method works for $\sin(\alpha + i\beta) = x + iy$: here $x = \sin\alpha\cosh\beta$ and $y = \cos\alpha\sinh\beta$.

:::caution
In the first formula, keep the sign of the cross term: $\cos(x + iy)$ has $-i\sin x\sinh y$, but $\sin(x + iy)$ has $+i\cos x\sinh y$. And use $\cosh$, $\sinh$ of $y$, not $\cos y$, $\sin y$.
:::

:::exam-tip
Test any separation formula at $y = 0$: it must reduce to the real function. Test at $x = 0$ against $\sin iy = i\sinh y$ and $\cos iy = \cosh y$. These two checks eliminate most distractors.
:::

## Quick checks and traps {#exam-tips}

- **$\lvert e^{x + iy}\rvert = e^x$**, independent of $y$. So $\lvert e^{3 + 4i}\rvert = e^3$.
- **Periods:** $e^z$, $\sinh z$ and $\cosh z$ have period $2\pi i$; $\sin z$ and $\cos z$ have period $2\pi$; $\tan z$ has period $\pi$ and $\tanh z$ has period $\pi i$.
- **Zeros:** $e^z$ has none. The zeros of $\sin z$ and $\cos z$ are all real; those of $\sinh z$ and $\cosh z$ are all purely imaginary.
- **Unbounded:** $\lvert\sin z\rvert, \lvert\cos z\rvert \le 1$ only on the real line; $\cos(iy) = \cosh y \to \infty$.
- **Principal log:** imaginary part in $(-\pi, \pi]$. $\operatorname{Log}(-1) = i\pi$, not $-i\pi$.
- **Log laws:** true as sets for $\log$, false in general for $\operatorname{Log}$; the error is a multiple of $2\pi i$.
- **$i^i$:** all values $e^{-\pi/2 - 2n\pi}$ are real; the principal value is $e^{-\pi/2}$. Also $i^{-i} = e^{\pi/2}$ (principal).
- **$a^z$ has one value** only for integer $z$; $q$ values for $z = p/q$ in lowest terms; otherwise infinitely many.
- **Log forms:** $\sinh^{-1} z$ has $z^2 + 1$, while $\cosh^{-1} z$ has $z^2 - 1$; $\tanh^{-1} z$ has $\frac{1 + z}{1 - z}$, while $\tan^{-1} z$ has $\frac{1 + iz}{1 - iz}$ and a factor $\frac{1}{2i}$.
- **$\tan z = \pm i$ and $\tanh z = \pm 1$ have no solutions.**
- **Inverses of large values:** $\cos^{-1} 2 = 2n\pi \pm i\ln(2 + \sqrt3)$, and $\sin^{-1} 2 = \frac{\pi}{2} + 2n\pi \pm i\ln(2 + \sqrt3)$.
