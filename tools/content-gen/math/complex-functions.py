import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from qlib import Topic, eq

T = Topic("math.algebra.complex-functions")

# ---------------------------------------------------------------- singles: easy
T.single(1, ["logarithm"], r"The principal value of $\log(-1)$ is",
         [r"$i\pi$", r"$-i\pi$", r"$0$", r"$\pi$"],
         r"""$\lvert -1\rvert = 1$ and $\operatorname{Arg}(-1) = \pi$, so
$$\operatorname{Log}(-1) = \ln 1 + i\pi = i\pi.$$
$-i\pi$ is also a value of $\log(-1)$, but its imaginary part $-\pi$ is not in $(-\pi, \pi]$, so it is not the principal value. $0$ would need $e^0 = -1$.""")

T.single(1, ["exponential", "exam-tips"], r"$\lvert e^{3 + 4i}\rvert$ equals",
         [r"$e^{3}$", r"$e^{5}$", r"$e^{4}$", r"$e^{7}$"],
         r"""$e^{x + iy} = e^x(\cos y + i\sin y)$ and $\lvert\cos y + i\sin y\rvert = 1$, so
$$\lvert e^{3 + 4i}\rvert = e^{3}.$$
$e^5$ wrongly uses $\lvert 3 + 4i\rvert = 5$; only the real part matters.""")

T.single(1, ["general-power"], r"The principal value of $i^{i}$ is",
         [r"$e^{-\pi/2}$", r"$e^{\pi/2}$", r"$e^{-\pi}$", r"$e^{-\pi/4}$"],
         r"""$\operatorname{Log} i = \frac{i\pi}{2}$, so
$$i^i = e^{i\operatorname{Log} i} = e^{i\cdot i\pi/2} = e^{-\pi/2} \approx 0.208.$$
$e^{\pi/2}$ forgets that $i \cdot i = -1$; it is the principal value of $i^{-i}$.""")

T.single(1, ["hyperbolic-functions"], r"For every complex $z$, $\sin(iz)$ equals",
         [r"$i\sinh z$", r"$-i\sinh z$", r"$\sinh z$", r"$i\cosh z$"],
         r"""$$\sin(iz) = \frac{e^{i\cdot iz} - e^{-i\cdot iz}}{2i} = \frac{e^{-z} - e^{z}}{2i} = \frac{-2\sinh z}{2i} = i\sinh z,$$
using $\frac{-1}{i} = i$. The sign slip $-i\sinh z$ comes from writing $\frac{1}{i} = i$.
Check: $\sin(i\cdot 1) \approx 1.175i$ and $\sinh 1 \approx 1.175$.""")

T.single(1, ["exponential"], r"The fundamental period of $e^{z}$, $z \in \C$, is",
         [r"$2\pi i$", r"$2\pi$", r"$\pi i$", r"$4\pi i$"],
         r"""$e^{z + w} = e^z$ for all $z$ iff $e^w = 1$ iff $w = 2n\pi i$. The smallest non-zero such $w$ (up to sign) is $2\pi i$.

$2\pi$ fails, since $e^{z + 2\pi} = e^{2\pi}e^z$. $\pi i$ fails, since $e^{z + \pi i} = -e^z$. $4\pi i$ is a period but not the fundamental one.""")

T.single(1, ["logarithm", "real-imaginary-parts"], r"The principal value of $\log(1 + i)$ is",
         [r"$\tfrac12\ln 2 + \tfrac{i\pi}{4}$", r"$\ln 2 + \tfrac{i\pi}{4}$", r"$\tfrac12\ln 2 - \tfrac{i\pi}{4}$", r"$\tfrac12\ln 2 + \tfrac{i\pi}{2}$"],
         r"""$\lvert 1 + i\rvert = \sqrt2$ and $\operatorname{Arg}(1 + i) = \frac{\pi}{4}$, so
$$\operatorname{Log}(1 + i) = \ln\sqrt2 + \frac{i\pi}{4} = \frac12\ln 2 + \frac{i\pi}{4}.$$
$\ln 2$ uses $\lvert z\rvert^2$ instead of $\lvert z\rvert$.""")

T.single(1, ["exponential"], r"$e^{\ln 2 + i\pi/3}$ equals",
         [r"$1 + i\sqrt3$", r"$\sqrt3 + i$", r"$2 + 2i\sqrt3$", r"$\tfrac12 + \tfrac{\sqrt3}{2}i$"],
         r"""$$e^{\ln 2 + i\pi/3} = e^{\ln 2}\left(\cos\frac{\pi}{3} + i\sin\frac{\pi}{3}\right) = 2\left(\frac12 + \frac{\sqrt3}{2}i\right) = 1 + i\sqrt3.$$
$\sqrt3 + i$ swaps $\cos$ and $\sin$; $\frac12 + \frac{\sqrt3}{2}i$ forgets the modulus $e^{\ln 2} = 2$.""")

# ---------------------------------------------------------------- singles: medium
T.single(2, ["inverse-functions"], r"$\sinh^{-1} z$ (general value) equals",
         [r"$\log\left(z + \sqrt{z^2 + 1}\right)$", r"$\log\left(z + \sqrt{z^2 - 1}\right)$",
          r"$\log\left(z + \sqrt{1 - z^2}\right)$", r"$\tfrac12\log\dfrac{1 + z}{1 - z}$"],
         r"""Let $\sinh w = z$. Then $e^{w} - e^{-w} = 2z$, so $e^{2w} - 2z e^{w} - 1 = 0$ and
$$e^{w} = z + \sqrt{z^2 + 1}, \qquad w = \log\left(z + \sqrt{z^2 + 1}\right).$$
$\log(z + \sqrt{z^2 - 1})$ is $\cosh^{-1} z$, and $\frac12\log\frac{1 + z}{1 - z}$ is $\tanh^{-1} z$.
Check at $z = 0$: $\sinh^{-1} 0$ must include $0 = \log 1$, and only the first option gives $\log 1$.""")

T.single(2, ["real-imaginary-parts"], r"For real $x, y$, $\sin(x + iy)$ equals",
         [r"$\sin x\cosh y + i\cos x\sinh y$", r"$\sin x\cosh y - i\cos x\sinh y$",
          r"$\sin x\cos y + i\cos x\sin y$", r"$\cos x\cosh y + i\sin x\sinh y$"],
         r"""By the addition formula,
$$\sin(x + iy) = \sin x\cos(iy) + \cos x\sin(iy) = \sin x\cosh y + i\cos x\sinh y,$$
using $\cos(iy) = \cosh y$ and $\sin(iy) = i\sinh y$.
The minus sign belongs to $\cos(x + iy) = \cos x\cosh y - i\sin x\sinh y$. Check at $y = 0$: only the first and second options reduce to $\sin x$, and at $x = 0$ only the first gives $i\sinh y$.""")

T.single(2, ["circular-functions"], r"For $z = x + iy$, $\lvert\sin z\rvert^2$ equals",
         [r"$\sin^2 x + \sinh^2 y$", r"$\sin^2 x + \cosh^2 y$", r"$\sin^2 x - \sinh^2 y$", r"$\cos^2 x + \sinh^2 y$"],
         r"""From $\sin z = \sin x\cosh y + i\cos x\sinh y$,
$$\lvert\sin z\rvert^2 = \sin^2 x\cosh^2 y + \cos^2 x\sinh^2 y = \sin^2 x(1 + \sinh^2 y) + \cos^2 x\sinh^2 y = \sin^2 x + \sinh^2 y.$$
$\cos^2 x + \sinh^2 y$ is $\lvert\cos z\rvert^2$. Check at $z = 0$: $\lvert\sin 0\rvert^2 = 0$ rules out $\sin^2 x + \cosh^2 y$.""")

T.single(2, ["general-power"], r"The set of all values of $1^{i}$ is",
         [r"$\{e^{2n\pi} : n \in \Z\}$", r"$\{1\}$", r"$\{e^{n\pi} : n \in \Z\}$", r"$\{e^{(2n + 1)\pi} : n \in \Z\}$"],
         r"""$\log 1 = 0 + 2n\pi i$, so
$$1^{i} = e^{i\log 1} = e^{i\cdot 2n\pi i} = e^{-2n\pi}, \qquad n \in \Z.$$
As $n$ runs over $\Z$, so does $-n$, so the set is $\{e^{2n\pi}\}$. The principal value ($n = 0$) is $1$, but $1^i$ is many-valued because $i$ is not rational; $\{1\}$ keeps only the principal value.""")

T.single(2, ["exponential"], r"All solutions of $e^{z} = -1$ are",
         [r"$z = (2n + 1)\pi i,\ n \in \Z$", r"$z = (2n + 1)\pi,\ n \in \Z$", r"$z = 2n\pi i,\ n \in \Z$", r"$z = n\pi i,\ n \in \Z$"],
         r"""$e^{x}(\cos y + i\sin y) = -1 = 1\cdot e^{i\pi}$ gives $e^x = 1$ and $y = \pi + 2n\pi$. So
$$z = (2n + 1)\pi i.$$
$2n\pi i$ gives $e^z = 1$, and $n\pi i$ includes those. $(2n + 1)\pi$ is real, and $e^{\text{real}} > 0$.""")

T.single(2, ["circular-functions", "inverse-functions"], r"All solutions of $\cos z = 2$ in $\C$ are",
         [r"$2n\pi \pm i\ln(2 + \sqrt3)$", r"$2n\pi \pm \ln(2 + \sqrt3)$", r"$n\pi \pm i\ln(2 + \sqrt3)$", r"there are none"],
         r"""With $z = x + iy$: $\cos x\cosh y - i\sin x\sinh y = 2$.
- Imaginary part: $\sin x\sinh y = 0$. $y = 0$ would need $\cos x = 2$, so $\sin x = 0$.
- Real part: $\cos x\cosh y = 2 > 0$ forces $\cos x = 1$, so $x = 2n\pi$ and $\cosh y = 2$, $y = \pm\ln(2 + \sqrt3)$.

$$z = 2n\pi \pm i\ln(2 + \sqrt3).$$
With $n\pi$, odd $n$ gives $\cos z = -2$. "None" is true only for real $z$.""")

T.single(2, ["inverse-functions"], r"In logarithmic form, $\tan^{-1} z$ ($z \ne \pm i$) equals",
         [r"$\dfrac{1}{2i}\log\dfrac{1 + iz}{1 - iz}$", r"$\dfrac{1}{2i}\log\dfrac{1 - iz}{1 + iz}$",
          r"$\dfrac12\log\dfrac{1 + z}{1 - z}$", r"$\dfrac1i\log\dfrac{1 + iz}{1 - iz}$"],
         r"""Let $\tan w = z$, i.e. $\frac{e^{iw} - e^{-iw}}{i(e^{iw} + e^{-iw})} = z$. Then
$$e^{2iw} - 1 = iz(e^{2iw} + 1) \;\Rightarrow\; e^{2iw} = \frac{1 + iz}{1 - iz} \;\Rightarrow\; w = \frac{1}{2i}\log\frac{1 + iz}{1 - iz}.$$
The second option is the negative of this ($\tan^{-1}(-z)$). $\frac12\log\frac{1 + z}{1 - z}$ is $\tanh^{-1} z$. The fourth option drops the $2$ from $e^{2iw}$.""")

T.single(2, ["logarithm"], r"Let $z_1 = z_2 = -1 + i$. Then $\operatorname{Log} z_1 + \operatorname{Log} z_2 - \operatorname{Log}(z_1 z_2)$ equals",
         [r"$2\pi i$", r"$0$", r"$-2\pi i$", r"$\pi i$"],
         r"""$\operatorname{Log}(-1 + i) = \frac12\ln 2 + \frac{3\pi i}{4}$, so the sum is $\ln 2 + \frac{3\pi i}{2}$.
$z_1 z_2 = (-1 + i)^2 = -2i$, so $\operatorname{Log}(z_1 z_2) = \ln 2 - \frac{\pi i}{2}$.
$$\text{Difference} = \frac{3\pi i}{2} + \frac{\pi i}{2} = 2\pi i.$$
The answer $0$ assumes the law $\operatorname{Log}(z_1z_2) = \operatorname{Log} z_1 + \operatorname{Log} z_2$, which fails here because $\frac{3\pi}{2} > \pi$.""")

T.single(2, ["general-power"], r"The principal value of $2^{i}$ is",
         [r"$\cos(\ln 2) + i\sin(\ln 2)$", r"$\cos 2 + i\sin 2$", r"$\cos(\ln 2) - i\sin(\ln 2)$", r"$2(\cos 1 + i\sin 1)$"],
         r"""$\operatorname{Log} 2 = \ln 2$, so
$$2^{i} = e^{i\ln 2} = \cos(\ln 2) + i\sin(\ln 2),$$
a point on the unit circle. $\cos(\ln 2) - i\sin(\ln 2)$ is $2^{-i}$. $\cos 2 + i\sin 2$ is $e^{2i}$, which forgets the logarithm.""")

T.single(2, ["hyperbolic-functions"], r"All solutions of $\sinh z = i$ are ($n \in \Z$)",
         [r"$z = \dfrac{(4n + 1)\pi i}{2}$", r"$z = \dfrac{(2n + 1)\pi i}{2}$", r"$z = \dfrac{(4n + 1)\pi}{2}$", r"$z = n\pi + \dfrac{\pi i}{2}$"],
         r"""$\sinh z = -i\sin(iz)$, so $\sinh z = i$ means $\sin(iz) = -1$. Then $iz = -\frac{\pi}{2} + 2m\pi$, so
$$z = i\left(\frac{\pi}{2} - 2m\pi\right) = \frac{(4n + 1)\pi i}{2}.$$
$\frac{(2n + 1)\pi i}{2}$ includes $\frac{3\pi i}{2}$, where $\sinh = i\sin\frac{3\pi}{2} = -i$. For $n \ne 0$, $\sinh\left(n\pi + \frac{\pi i}{2}\right) = i\cosh n\pi \ne i$.""")

# ---------------------------------------------------------------- singles: hard
T.single(3, ["logarithm"], r"The principal value of $\log(\log i)$ is",
         [r"$\ln\dfrac{\pi}{2} + \dfrac{i\pi}{2}$", r"$\ln\dfrac{\pi}{2}$", r"$\ln\dfrac{\pi}{2} + i\pi$", r"$\ln\pi + \dfrac{i\pi}{2}$"],
         r"""First $\operatorname{Log} i = \frac{i\pi}{2}$. This is a positive multiple of $i$: its modulus is $\frac{\pi}{2}$ and its argument is $\frac{\pi}{2}$. So
$$\operatorname{Log}\frac{i\pi}{2} = \ln\frac{\pi}{2} + \frac{i\pi}{2}.$$
$\ln\frac{\pi}{2}$ alone treats $\frac{i\pi}{2}$ as if it were real.""")

T.single(3, ["real-imaginary-parts"], r"If $\tan^{-1}(x + iy) = \alpha + i\beta$ (with $x, y, \alpha, \beta$ real), then $\tan 2\alpha$ equals",
         [r"$\dfrac{2x}{1 - x^2 - y^2}$", r"$\dfrac{2x}{1 + x^2 + y^2}$", r"$\dfrac{2y}{1 - x^2 - y^2}$", r"$\dfrac{2y}{1 + x^2 + y^2}$"],
         r"""$\tan(\alpha + i\beta) = x + iy$ and, taking conjugates, $\tan(\alpha - i\beta) = x - iy$. Add the angles:
$$\tan 2\alpha = \frac{(x + iy) + (x - iy)}{1 - (x + iy)(x - iy)} = \frac{2x}{1 - x^2 - y^2}.$$
Subtracting the angles instead gives $\tan 2i\beta = \frac{2iy}{1 + x^2 + y^2}$, i.e. $\tanh 2\beta = \frac{2y}{1 + x^2 + y^2}$. That is the last option, which is for $\beta$, not $\alpha$.""")

T.single(3, ["real-imaginary-parts"], r"If $\cos(\alpha + i\beta) = x + iy$ ($\alpha, \beta, x, y$ real, $\beta \ne 0$), then",
         [r"$\dfrac{x^2}{\cosh^2\beta} + \dfrac{y^2}{\sinh^2\beta} = 1$", r"$\dfrac{x^2}{\cosh^2\beta} - \dfrac{y^2}{\sinh^2\beta} = 1$",
          r"$\dfrac{x^2}{\cos^2\alpha} + \dfrac{y^2}{\sin^2\alpha} = 1$", r"$\dfrac{x^2}{\sinh^2\beta} + \dfrac{y^2}{\cosh^2\beta} = 1$"],
         r"""$\cos(\alpha + i\beta) = \cos\alpha\cosh\beta - i\sin\alpha\sinh\beta$, so $x = \cos\alpha\cosh\beta$ and $y = -\sin\alpha\sinh\beta$. Then
$$\frac{x^2}{\cosh^2\beta} + \frac{y^2}{\sinh^2\beta} = \cos^2\alpha + \sin^2\alpha = 1.$$
Eliminating $\beta$ instead gives the hyperbola $\frac{x^2}{\cos^2\alpha} - \frac{y^2}{\sin^2\alpha} = 1$ (a minus sign, because $\cosh^2\beta - \sinh^2\beta = 1$). So the third option has the wrong sign.""")

T.single(3, ["general-power"], r"The principal value of $(1 + i)^{i}$ is",
         [r"$e^{-\pi/4}\left[\cos\left(\tfrac12\ln 2\right) + i\sin\left(\tfrac12\ln 2\right)\right]$",
          r"$e^{\pi/4}\left[\cos\left(\tfrac12\ln 2\right) + i\sin\left(\tfrac12\ln 2\right)\right]$",
          r"$e^{-\pi/4}\left[\cos(\ln 2) + i\sin(\ln 2)\right]$",
          r"$e^{-\pi/4}\left[\cos\left(\tfrac12\ln 2\right) - i\sin\left(\tfrac12\ln 2\right)\right]$"],
         r"""$\operatorname{Log}(1 + i) = \frac12\ln 2 + \frac{i\pi}{4}$. Multiply by $i$:
$$i\operatorname{Log}(1 + i) = -\frac{\pi}{4} + \frac{i}{2}\ln 2,$$
$$(1 + i)^{i} = e^{-\pi/4}\left[\cos\left(\tfrac12\ln 2\right) + i\sin\left(\tfrac12\ln 2\right)\right].$$
$e^{+\pi/4}$ forgets $i\cdot i = -1$; $\cos(\ln 2)$ uses $\ln\lvert z\rvert^2$ instead of $\ln\lvert z\rvert$.""")

# ---------------------------------------------------------------- statements
T.statements(3, ["logarithm"],
             r"Consider the following statements, where $\log$ denotes the many-valued logarithm (viewed as a set) and $\operatorname{Log}$ its principal value:",
             [r"$\operatorname{Log}(z_1 z_2) = \operatorname{Log} z_1 + \operatorname{Log} z_2$ for all non-zero $z_1, z_2$.",
              r"$\log(z_1 z_2) = \log z_1 + \log z_2$ as sets, for all non-zero $z_1, z_2$.",
              r"$\log(z^2) = 2\log z$ as sets, for every non-zero $z$."],
             [r"2 only", r"1 and 2 only", r"2 and 3 only", r"1, 2 and 3"],
             r"""- **1 is false.** With $z_1 = z_2 = -1$: $\operatorname{Log} 1 = 0$, but $\operatorname{Log}(-1) + \operatorname{Log}(-1) = 2\pi i$.
- **2 is true.** Every value $\ln\lvert z_1\rvert + \ln\lvert z_2\rvert + i(\theta_1 + \theta_2 + 2(m + n)\pi)$ of the right side is a value of $\log(z_1z_2)$, and conversely (take $n = 0$ and vary $m$).
- **3 is false.** With $z = i$: $\log(i^2) = \log(-1) = \{(2k + 1)\pi i\}$ contains $3\pi i$. But $2\log i = \{(4k + 1)\pi i\}$ does not, since $4k + 1 = 3$ has no integer solution.

So only statement 2 is correct.""")

T.statements(3, ["exponential", "circular-functions", "hyperbolic-functions"],
             r"Consider the following statements about functions of a complex variable $z$:",
             [r"$e^{z} \ne 0$ for every $z \in \C$.",
              r"Every zero of $\sin z$ in $\C$ is real.",
              r"$\sinh z$ has no non-real zeros."],
             [r"1 and 2 only", r"1, 2 and 3", r"2 and 3 only", r"1 only"],
             r"""- **1 is true:** $\lvert e^{x + iy}\rvert = e^x > 0$.
- **2 is true:** $\sin z = 0 \iff e^{2iz} = 1 \iff 2iz = 2n\pi i \iff z = n\pi$. Equivalently, $\lvert\sin z\rvert^2 = \sin^2 x + \sinh^2 y = 0$ forces $y = 0$ and $x = n\pi$.
- **3 is false:** $\sinh z = -i\sin(iz)$ vanishes when $iz = n\pi$, i.e. $z = -n\pi i$. For example, $\sinh(i\pi) = i\sin\pi = 0$.

The zeros of $\sinh$ are imaginary, not real: that is the trap.""")

# ---------------------------------------------------------------- match
T.match(3, ["inverse-functions"], r"Match each function in List I with its logarithmic form in List II (general values).",
        [r"$\sin^{-1} z$", r"$\cos^{-1} z$", r"$\sinh^{-1} z$", r"$\tanh^{-1} z$"],
        [r"$\log\left(z + \sqrt{z^2 + 1}\right)$", r"$\tfrac12\log\dfrac{1 + z}{1 - z}$",
         r"$-i\log\left(iz + \sqrt{1 - z^2}\right)$", r"$-i\log\left(z + \sqrt{z^2 - 1}\right)$"],
        [r"A-3, B-4, C-1, D-2", r"A-4, B-3, C-1, D-2", r"A-3, B-4, C-2, D-1", r"A-1, B-4, C-3, D-2"],
        r"""- A: $\sin w = z$ gives $e^{2iw} - 2iz\,e^{iw} - 1 = 0$, so $e^{iw} = iz + \sqrt{1 - z^2}$ and $w = -i\log(iz + \sqrt{1 - z^2})$: **3**.
- B: $\cos w = z$ gives $e^{iw} = z + \sqrt{z^2 - 1}$: **4**.
- C: $\sinh w = z$ gives $e^{w} = z + \sqrt{z^2 + 1}$: **1**.
- D: $\tanh w = z$ gives $e^{2w} = \frac{1 + z}{1 - z}$: **2**.

So A-3, B-4, C-1, D-2. Swapping A and B is the common slip: only $\sin^{-1}$ has $iz$ inside the log.""")

T.match(2, ["logarithm", "general-power", "hyperbolic-functions"], r"Match each expression in List I with its principal value in List II.",
        [r"$\log(-i)$", r"$(-1)^{i}$", r"$\cos(i\ln 2)$", r"$\log(-e)$"],
        [r"$1 + i\pi$", r"$e^{-\pi}$", r"$-\dfrac{i\pi}{2}$", r"$\dfrac54$"],
        [r"A-3, B-2, C-4, D-1", r"A-3, B-4, C-2, D-1", r"A-1, B-2, C-4, D-3", r"A-3, B-1, C-4, D-2"],
        r"""- A: $\lvert -i\rvert = 1$ and $\operatorname{Arg}(-i) = -\frac{\pi}{2}$, so $\operatorname{Log}(-i) = -\frac{i\pi}{2}$: **3**.
- B: $(-1)^i = e^{i\operatorname{Log}(-1)} = e^{i\cdot i\pi} = e^{-\pi}$: **2**.
- C: $\cos(i\ln 2) = \cosh(\ln 2) = \frac{2 + \frac12}{2} = \frac54$: **4**.
- D: $\operatorname{Log}(-e) = \ln e + i\pi = 1 + i\pi$: **1**.

So A-3, B-2, C-4, D-1.""")

# ---------------------------------------------------------------- assertion-reason
T.assertion_reason(1, ["exponential"],
                   r"For complex numbers $z$ and $w$, $e^{z} = e^{w}$ if and only if $z - w = 2n\pi i$ for some integer $n$.",
                   r"$e^{\zeta} = 1$ if and only if $\zeta = 2n\pi i$ for some integer $n$.",
                   0,
                   r"""**R is true:** $e^{x}(\cos y + i\sin y) = 1$ forces $e^x = 1$ and $y = 2n\pi$, so $\zeta = 2n\pi i$.

**A is true, and R explains it:** $e^{z} = e^{w} \iff e^{z - w} = 1 \iff z - w = 2n\pi i$, by R with $\zeta = z - w$.""")

T.assertion_reason(3, ["inverse-functions", "circular-functions"],
                   r"The equation $\tan z = i$ has no solution in $\C$.",
                   r"$e^{\zeta} \ne 0$ for every $\zeta \in \C$.",
                   0,
                   r"""**R is true:** $\lvert e^{\zeta}\rvert = e^{\operatorname{Re}\zeta} > 0$.

**A is true, and R explains it:** $\tan z = \dfrac{e^{iz} - e^{-iz}}{i(e^{iz} + e^{-iz})} = i$ gives
$$e^{iz} - e^{-iz} = -(e^{iz} + e^{-iz}) \;\Rightarrow\; 2e^{iz} = 0,$$
which R rules out. (In log form, $\tan^{-1} i = \frac{1}{2i}\log\frac{1 + i\cdot i}{1 - i\cdot i} = \frac{1}{2i}\log 0$, which does not exist.)""")

T.assertion_reason(2, ["circular-functions"],
                   r"$\cos z$ is unbounded on $\C$.",
                   r"$\cos z$ is periodic with period $2\pi$.",
                   1,
                   r"""**A is true:** $\cos(iy) = \cosh y = \frac{e^{y} + e^{-y}}{2} \to \infty$ as $y \to \infty$.

**R is true:** $\cos(z + 2\pi) = \cos z$, since $e^{\pm 2\pi i} = 1$.

**But R does not explain A.** Periodicity says nothing about size; $\cos x$ on $\R$ is periodic and bounded. Unboundedness comes from the growth of $e^{\pm iz}$ along the imaginary axis.""")

T.assertion_reason(2, ["general-power", "logarithm"],
                   r"Every value of $i^{i}$ is a real number.",
                   r"$\operatorname{Log}(z_1 z_2) = \operatorname{Log} z_1 + \operatorname{Log} z_2$ for all non-zero complex $z_1, z_2$.",
                   2,
                   r"""**A is true:** $\log i = i\left(\frac{\pi}{2} + 2n\pi\right)$, so
$$i^i = e^{i\log i} = e^{-\pi/2 - 2n\pi},$$
which is real for every $n$.

**R is false:** with $z_1 = z_2 = -1$, $\operatorname{Log} 1 = 0$, but $2\operatorname{Log}(-1) = 2\pi i$. The principal values agree only up to a multiple of $2\pi i$.""")

T.assertion_reason(2, ["circular-functions", "exam-tips"],
                   r"$\lvert\sin z\rvert \le 1$ for every $z \in \C$.",
                   r"The only zeros of $\sin z$ in $\C$ are $z = n\pi$, $n \in \Z$.",
                   3,
                   r"""**A is false:** $\lvert\sin z\rvert^2 = \sin^2 x + \sinh^2 y$. For example, $\lvert\sin 2i\rvert = \lvert i\sinh 2\rvert = \sinh 2 \approx 3.63 > 1$.

**R is true:** $\sin z = 0 \iff e^{2iz} = 1 \iff z = n\pi$. The bound $\lvert\sin z\rvert \le 1$ holds only for real $z$.""")


def check():
    import sympy as sp
    I, pi, E = sp.I, sp.pi, sp.E
    ln = sp.log
    x, y = sp.symbols("x y", real=True)
    zs = [sp.Rational(3, 10) + sp.Rational(7, 10) * I, -sp.Rational(6, 5) + sp.Rational(2, 5) * I,
          sp.Rational(1, 2) - sp.Rational(9, 10) * I]

    def num(e):
        return complex(sp.N(e, 30))

    def ne(a, b, label):
        if abs(num(a) - num(b)) < 1e-9:
            sys.exit(f"DISTRACTOR EQUALS KEY {label}: {a} vs {b}")

    def ident(f, g, label, pts=zs):
        for p in pts:
            eq(sp.N(f(p), 30), sp.N(g(p), 30), label)

    def xy_ident(lhs, rhs, label, also_ne=()):
        for xv, yv in [(0.3, 0.7), (-1.1, 0.4), (2.0, -0.5)]:
            s = {x: sp.Float(xv, 30), y: sp.Float(yv, 30)}
            eq(sp.N(lhs.subs(s)), sp.N(rhs.subs(s)), label)
        s = {x: sp.Float(0.3, 30), y: sp.Float(0.7, 30)}
        for d in also_ne:
            ne(lhs.subs(s), d.subs(s), label)

    # q1
    eq(ln(-1), I * pi, "q1"); ne(ln(-1), -I * pi, "q1")
    # q2
    eq(sp.Abs(sp.exp(3 + 4 * I)), sp.exp(3), "q2")
    # q3
    eq(I**I, sp.exp(-pi / 2), "q3"); eq(I**(-I), sp.exp(pi / 2), "q3b")
    # q4
    ident(lambda z: sp.sin(I * z).rewrite(sp.exp), lambda z: I * sp.sinh(z), "q4")
    ne(sp.sin(I), -I * sp.sinh(1), "q4"); ne(sp.sin(I), I * sp.cosh(1), "q4")
    # q5
    ident(lambda z: sp.exp(z + 2 * pi * I), lambda z: sp.exp(z), "q5")
    ne(sp.exp(1 + 2 * pi), sp.exp(1), "q5"); ne(sp.exp(1 + pi * I), sp.exp(1), "q5")
    # q6
    eq(ln(1 + I), ln(2) / 2 + I * pi / 4, "q6")
    # q7
    eq(sp.exp(ln(2) + I * pi / 3), 1 + I * sp.sqrt(3), "q7")
    # q8
    ident(lambda z: sp.sinh(ln(z + sp.sqrt(z**2 + 1))), lambda z: z, "q8")
    ne(sp.sinh(ln(zs[0] + sp.sqrt(zs[0]**2 - 1))), zs[0], "q8")
    # q9
    xy_ident(sp.expand_complex(sp.sin(x + I * y)), sp.sin(x) * sp.cosh(y) + I * sp.cos(x) * sp.sinh(y), "q9",
             [sp.sin(x) * sp.cosh(y) - I * sp.cos(x) * sp.sinh(y), sp.sin(x) * sp.cos(y) + I * sp.cos(x) * sp.sin(y),
              sp.cos(x) * sp.cosh(y) + I * sp.sin(x) * sp.sinh(y)])
    # q10
    xy_ident(sp.Abs(sp.sin(x + I * y))**2, sp.sin(x)**2 + sp.sinh(y)**2, "q10",
             [sp.sin(x)**2 + sp.cosh(y)**2, sp.sin(x)**2 - sp.sinh(y)**2, sp.cos(x)**2 + sp.sinh(y)**2])
    # q11: values of 1^i = exp(i*(2 n pi i)) = exp(-2 n pi)
    for n in range(-2, 3):
        eq(sp.exp(I * (ln(1) + 2 * n * pi * I)), sp.exp(-2 * n * pi), "q11")
    ne(sp.exp(I * 2 * pi * I), 1, "q11")
    # q12
    for n in range(-2, 3):
        eq(sp.exp((2 * n + 1) * pi * I), -1, "q12")
    ne(sp.exp(2 * pi * I), -1, "q12"); ne(sp.exp(pi), -1, "q12")
    # q13
    c = ln(2 + sp.sqrt(3))
    for n in range(-2, 3):
        for s in (1, -1):
            eq(sp.cos(2 * n * pi + s * I * c), 2, "q13")
    ne(sp.cos(pi + I * c), 2, "q13"); ne(sp.cos(c), 2, "q13")
    eq(sp.acosh(2), c, "q13b")
    # q14
    ident(lambda z: sp.tan(ln((1 + I * z) / (1 - I * z)) / (2 * I)), lambda z: z, "q14")
    ne(sp.tan(ln((1 - I * zs[0]) / (1 + I * zs[0])) / (2 * I)), zs[0], "q14")
    ne(sp.tan(ln((1 + I * zs[0]) / (1 - I * zs[0])) / I), zs[0], "q14")
    # q15
    z1 = -1 + I
    eq(ln(z1) + ln(z1) - ln(sp.expand(z1 * z1)), 2 * pi * I, "q15")
    # q16
    eq(sp.Integer(2)**I, sp.cos(ln(2)) + I * sp.sin(ln(2)), "q16")
    ne(sp.Integer(2)**I, sp.cos(ln(2)) - I * sp.sin(ln(2)), "q16")
    # q17
    for n in range(-2, 3):
        eq(sp.sinh((4 * n + 1) * pi * I / 2), I, "q17")
    ne(sp.sinh(3 * pi * I / 2), I, "q17"); ne(sp.sinh(pi + pi * I / 2), I, "q17")
    # q18
    eq(ln(ln(I)), ln(pi / 2) + I * pi / 2, "q18")
    # q19
    for p in zs:
        a = sp.re(sp.atan(p)); xv, yv = sp.re(p), sp.im(p)
        eq(sp.tan(2 * a), 2 * xv / (1 - xv**2 - yv**2), "q19")
        b = sp.im(sp.atan(p))
        eq(sp.tanh(2 * b), 2 * yv / (1 + xv**2 + yv**2), "q19b")
        eq(b, sp.log((xv**2 + (1 + yv)**2) / (xv**2 + (1 - yv)**2)) / 4, "q19c")
        ne(sp.tan(2 * a), 2 * xv / (1 + xv**2 + yv**2), "q19")
    # q20
    for al, be in [(0.4, 0.9), (2.2, -0.3)]:
        al, be = sp.Float(al, 30), sp.Float(be, 30)
        w = sp.cos(al + I * be); X, Y = sp.re(w), sp.im(w)
        eq(X**2 / sp.cosh(be)**2 + Y**2 / sp.sinh(be)**2, 1, "q20")
        eq(X**2 / sp.cos(al)**2 - Y**2 / sp.sin(al)**2, 1, "q20b")
        ne(X**2 / sp.cos(al)**2 + Y**2 / sp.sin(al)**2, 1, "q20")
        ne(X**2 / sp.cosh(be)**2 - Y**2 / sp.sinh(be)**2, 1, "q20")
        ne(X**2 / sp.sinh(be)**2 + Y**2 / sp.cosh(be)**2, 1, "q20")
    # q21
    key = sp.exp(-pi / 4) * (sp.cos(ln(2) / 2) + I * sp.sin(ln(2) / 2))
    eq((1 + I)**I, key, "q21")
    ne((1 + I)**I, sp.exp(-pi / 4) * (sp.cos(ln(2)) + I * sp.sin(ln(2))), "q21")
    # q22 statements: 1 false, 2 true, 3 false
    ne(ln(1), 2 * ln(-1), "q22-1")
    # 2: sample values of log z1 + log z2 lie in log(z1 z2)
    for m in range(-2, 3):
        v = ln(z1) + ln(2 * I) + 2 * m * pi * I
        eq(sp.exp(v), z1 * 2 * I, "q22-2")
    # 3: 3*pi*i is a value of log(-1) but not of 2 log i = (4k+1) pi i
    eq(sp.exp(3 * pi * I), -1, "q22-3")
    k = sp.symbols("k", integer=True)
    assert sp.solve(sp.Eq(4 * k + 1, 3), k) == [], "q22-3"
    # q23 statements: 1 true, 2 true, 3 false
    eq(sp.Abs(sp.exp(x + I * y)), sp.exp(x), "q23-1")
    for n in range(-2, 3):
        eq(sp.sin(n * pi), 0, "q23-2")
    eq(sp.sin(t := sp.Symbol("t")).rewrite(sp.exp), (sp.exp(2 * I * t) - 1) / (2 * I * sp.exp(I * t)), "q23-2b")
    eq(sp.sinh(I * pi), 0, "q23-3")
    # q24 match 1: A-3, B-4, C-1, D-2
    ident(lambda z: sp.sin(-I * ln(I * z + sp.sqrt(1 - z**2))), lambda z: z, "q24A")
    ident(lambda z: sp.cos(-I * ln(z + sp.sqrt(z**2 - 1))), lambda z: z, "q24B")
    ident(lambda z: sp.sinh(ln(z + sp.sqrt(z**2 + 1))), lambda z: z, "q24C")
    ident(lambda z: sp.tanh(ln((1 + z) / (1 - z)) / 2), lambda z: z, "q24D")
    ne(sp.sin(-I * ln(zs[0] + sp.sqrt(zs[0]**2 - 1))), zs[0], "q24")
    # q25 match 2: A-3, B-2, C-4, D-1
    eq(ln(-I), -I * pi / 2, "q25A")
    eq((-1)**I, sp.exp(-pi), "q25B")
    eq(sp.cos(I * ln(2)), sp.Rational(5, 4), "q25C")
    eq(ln(-E), 1 + I * pi, "q25D")
    # q26 AR 0
    eq(sp.exp(2 * pi * I), 1, "q26"); ident(lambda z: sp.exp(z + 6 * pi * I) - sp.exp(z), lambda z: 0, "q26")
    # q27 AR 0: tan z = i  <=>  2 e^{iz} = 0
    t = sp.symbols("t")
    eu, ed = sp.exp(I * t), sp.exp(-I * t)
    eq((eu - ed) - I * (I * (eu + ed)), 2 * eu, "q27")   # i(e^{it}+e^{-it})(tan t - i) = 2e^{it}
    assert sp.solve(sp.tan(t) - I, t) == [], "q27"
    # q28 AR 1
    assert sp.N(sp.Abs(sp.cos(10 * I))) > 10000, "q28"
    eq(sp.cos(zs[1] + 2 * pi), sp.cos(zs[1]), "q28")
    # q29 AR 2
    for n in range(-2, 3):
        assert sp.im(sp.exp(I * I * (pi / 2 + 2 * n * pi))) == 0, "q29"
    ne(ln((-1) * (-1)), ln(-1) + ln(-1), "q29")
    # q30 AR 3
    eq(sp.Abs(sp.sin(2 * I)), sp.sinh(2), "q30"); assert sp.sinh(2) > 1, "q30"


T.write(check)
