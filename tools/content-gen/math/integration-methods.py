import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from qlib import Topic, eq

T = Topic("math.integral.integration-methods")

# q1
T.single(1, ["standard-forms"],
    r"$\int\operatorname{cosec} x\,dx$ equals",
    [r"$\ln\left\lvert\tan\frac{x}{2}\right\rvert + C$", r"$\ln\lvert\operatorname{cosec} x + \cot x\rvert + C$", r"$\ln\lvert\sin x\rvert + C$", r"$-\operatorname{cosec} x\cot x + C$"],
    r"""Write $\operatorname{cosec} x = \dfrac{1}{2\sin\frac{x}{2}\cos\frac{x}{2}} = \dfrac{\frac12\sec^2\frac{x}{2}}{\tan\frac{x}{2}}$, which is $\frac{f'}{f}$ with $f = \tan\frac{x}{2}$:
$$\int\operatorname{cosec} x\,dx = \ln\left\lvert\tan\frac{x}{2}\right\rvert + C = \ln\lvert\operatorname{cosec} x - \cot x\rvert + C.$$

$\ln\lvert\operatorname{cosec} x + \cot x\rvert$ has the wrong sign: it equals $-\ln\lvert\tan\frac{x}{2}\rvert$, so its derivative is $-\operatorname{cosec} x$. $\ln\lvert\sin x\rvert$ is $\int\cot x\,dx$, and $-\operatorname{cosec} x\cot x$ is the **derivative** of $\operatorname{cosec} x$.""")

# q2
T.single(1, ["standard-forms"],
    r"$\int\frac{dx}{x^2 - 9}$ equals",
    [r"$\frac{1}{6}\ln\left\lvert\frac{x - 3}{x + 3}\right\rvert + C$", r"$\frac{1}{3}\ln\left\lvert\frac{x - 3}{x + 3}\right\rvert + C$", r"$\frac{1}{6}\ln\left\lvert\frac{x + 3}{x - 3}\right\rvert + C$", r"$\frac{1}{3}\tan^{-1}\frac{x}{3} + C$"],
    r"""$$\frac{1}{x^2 - 9} = \frac{1}{6}\left(\frac{1}{x - 3} - \frac{1}{x + 3}\right) \;\Rightarrow\; \int\frac{dx}{x^2 - 9} = \frac{1}{6}\ln\left\lvert\frac{x - 3}{x + 3}\right\rvert + C.$$

The factor is $\frac{1}{2a} = \frac16$, not $\frac1a$. The reversed fraction is $\int\frac{dx}{9 - x^2}$, which has the opposite sign. $\tan^{-1}$ belongs to $x^2 + 9$, not $x^2 - 9$.""")

# q3
T.single(1, ["substitution"],
    r"$\int\frac{\cos x}{(1 + \sin x)^2}\,dx$ equals",
    [r"$-\frac{1}{1 + \sin x} + C$", r"$\frac{1}{1 + \sin x} + C$", r"$\ln(1 + \sin x) + C$", r"$-\frac{1}{3(1 + \sin x)^3} + C$"],
    r"""Put $u = 1 + \sin x$, $du = \cos x\,dx$:
$$\int u^{-2}\,du = -u^{-1} + C = -\frac{1}{1 + \sin x} + C.$$

Dropping the minus sign is the usual slip; the logarithm would need power $1$ in the denominator, not $2$. The last option raises the power instead of lowering it.""")

# q4
T.single(1, ["by-parts"],
    r"$\int\ln x\,dx$ $(x > 0)$ equals",
    [r"$x\ln x - x + C$", r"$x\ln x + x + C$", r"$\frac{1}{x} + C$", r"$\frac{(\ln x)^2}{2} + C$"],
    r"""Take $u = \ln x$, $v' = 1$:
$$\int\ln x\,dx = x\ln x - \int x\cdot\frac{1}{x}\,dx = x\ln x - x + C.$$

**Check:** $\frac{d}{dx}(x\ln x - x) = \ln x + 1 - 1 = \ln x$. With $+x$ the derivative is $\ln x + 2$. $\frac{(\ln x)^2}{2}$ is $\int\frac{\ln x}{x}\,dx$, and $\frac1x$ is the derivative of $\ln x$.""")

# q5
T.single(2, ["by-parts"],
    r"$\int x^2 e^x\,dx$ equals",
    [r"$e^x(x^2 - 2x + 2) + C$", r"$e^x(x^2 + 2x + 2) + C$", r"$e^x(x^2 - 2x - 2) + C$", r"$\frac{x^3 e^x}{3} + C$"],
    r"""Parts twice, or the rule $\int p(x)e^x\,dx = e^x(p - p' + p'' - \cdots)$ with $p = x^2$:
$$\int x^2 e^x\,dx = e^x(x^2 - 2x + 2) + C.$$

**Check:** $\frac{d}{dx}\left[e^x(x^2 - 2x + 2)\right] = e^x(x^2 - 2x + 2 + 2x - 2) = x^2 e^x$. The signs must alternate, so $+2x$ is wrong, and $-2$ at the end gives $e^x(x^2 - 4)$ on differentiating.""")

# q6
T.single(3, ["by-parts"],
    r"$\int e^x\,\frac{1 + \sin x}{1 + \cos x}\,dx$ equals",
    [r"$e^x\tan\frac{x}{2} + C$", r"$e^x\cot\frac{x}{2} + C$", r"$-e^x\cot\frac{x}{2} + C$", r"$\frac{1}{2}e^x\sec^2\frac{x}{2} + C$"],
    r"""Use half-angles: $1 + \cos x = 2\cos^2\frac{x}{2}$ and $\sin x = 2\sin\frac{x}{2}\cos\frac{x}{2}$, so
$$\frac{1 + \sin x}{1 + \cos x} = \frac{1}{2}\sec^2\frac{x}{2} + \tan\frac{x}{2} = f + f', \qquad f = \tan\frac{x}{2}.$$
By $\int e^x(f + f')\,dx = e^x f$, the answer is $e^x\tan\frac{x}{2} + C$.

The $\cot$ options come from mixing up $1 + \cos x$ with $1 - \cos x = 2\sin^2\frac{x}{2}$. $\frac12 e^x\sec^2\frac{x}{2}$ uses $f'$ in place of $f$.""")

# q7
T.single(2, ["by-parts"],
    r"$\int e^{2x}\sin 3x\,dx$ equals",
    [r"$\frac{e^{2x}}{13}(2\sin 3x - 3\cos 3x) + C$", r"$\frac{e^{2x}}{13}(2\sin 3x + 3\cos 3x) + C$", r"$\frac{e^{2x}}{13}(3\sin 3x - 2\cos 3x) + C$", r"$\frac{e^{2x}}{5}(2\sin 3x - 3\cos 3x) + C$"],
    r"""With $a = 2$, $b = 3$ in
$$\int e^{ax}\sin bx\,dx = \frac{e^{ax}(a\sin bx - b\cos bx)}{a^2 + b^2},$$
the answer is $\frac{e^{2x}}{13}(2\sin 3x - 3\cos 3x) + C$.

**Check** by differentiating: $\frac{d}{dx}\left[e^{2x}(2\sin 3x - 3\cos 3x)\right] = e^{2x}(4\sin 3x - 6\cos 3x + 6\cos 3x + 9\sin 3x) = 13e^{2x}\sin 3x$. The $+3\cos 3x$ option fails this, and $5 = a + b$ is not $a^2 + b^2$.""")

# q8
T.single(2, ["by-parts"],
    r"$\int\tan^{-1}x\,dx$ equals",
    [r"$x\tan^{-1}x - \frac{1}{2}\ln(1 + x^2) + C$", r"$x\tan^{-1}x + \frac{1}{2}\ln(1 + x^2) + C$", r"$x\tan^{-1}x - \ln(1 + x^2) + C$", r"$\frac{1}{1 + x^2} + C$"],
    r"""Take $u = \tan^{-1}x$, $v' = 1$:
$$\int\tan^{-1}x\,dx = x\tan^{-1}x - \int\frac{x}{1 + x^2}\,dx = x\tan^{-1}x - \frac{1}{2}\ln(1 + x^2) + C.$$

$\int\frac{x\,dx}{1 + x^2} = \frac12\ln(1 + x^2)$: forgetting the $\frac12$ gives the third option, and a sign slip in the parts formula gives the second. $\frac{1}{1 + x^2}$ is the derivative of $\tan^{-1}x$.""")

# q9
T.single(1, ["partial-fractions"],
    r"$\int\frac{dx}{(x - 1)(x + 2)}$ equals",
    [r"$\frac{1}{3}\ln\left\lvert\frac{x - 1}{x + 2}\right\rvert + C$", r"$\frac{1}{3}\ln\left\lvert\frac{x + 2}{x - 1}\right\rvert + C$", r"$\ln\lvert(x - 1)(x + 2)\rvert + C$", r"$\frac{1}{3}\ln\lvert(x - 1)(x + 2)\rvert + C$"],
    r"""By cover-up, the coefficient of $\frac{1}{x - 1}$ is $\frac{1}{1 + 2} = \frac13$ and that of $\frac{1}{x + 2}$ is $\frac{1}{-2 - 1} = -\frac13$:
$$\int\left(\frac{1/3}{x - 1} - \frac{1/3}{x + 2}\right)dx = \frac13\ln\left\lvert\frac{x - 1}{x + 2}\right\rvert + C.$$

The two coefficients have **opposite** signs, so the answer is a log of a quotient, not of a product. The reversed quotient is the negative of the answer.""")

# q10
T.single(2, ["partial-fractions"],
    r"$\int\frac{dx}{x(x^2 + 1)}$ equals",
    [r"$\ln\lvert x\rvert - \frac{1}{2}\ln(x^2 + 1) + C$", r"$\ln\lvert x\rvert + \frac{1}{2}\ln(x^2 + 1) + C$", r"$\ln\lvert x\rvert - \ln(x^2 + 1) + C$", r"$\ln\lvert x\rvert - \tan^{-1}x + C$"],
    r"""$$\frac{1}{x(x^2 + 1)} = \frac{A}{x} + \frac{Bx + C}{x^2 + 1}: \quad A = 1\ (\text{cover-up at } x = 0),\quad 1 = (x^2 + 1) + (Bx + C)x \Rightarrow B = -1,\ C = 0.$$
So
$$\int\left(\frac1x - \frac{x}{x^2 + 1}\right)dx = \ln\lvert x\rvert - \frac12\ln(x^2 + 1) + C.$$

The $\tan^{-1}$ option takes a constant numerator over $x^2 + 1$; the numerator here is $-x$, which gives $-\frac12\ln(x^2 + 1)$, not $-\ln(x^2 + 1)$.""")

# q11
T.single(2, ["partial-fractions"],
    r"$\int\frac{dx}{x(x + 1)^2}$ equals",
    [r"$\ln\left\lvert\frac{x}{x + 1}\right\rvert + \frac{1}{x + 1} + C$", r"$\ln\left\lvert\frac{x}{x + 1}\right\rvert - \frac{1}{x + 1} + C$", r"$\ln\lvert x(x + 1)\rvert + \frac{1}{x + 1} + C$", r"$\ln\left\lvert\frac{x}{x + 1}\right\rvert + C$"],
    r"""The repeated factor needs two terms:
$$\frac{1}{x(x + 1)^2} = \frac{A}{x} + \frac{B}{x + 1} + \frac{D}{(x + 1)^2}.$$
Cover-up gives $A = 1$ (at $x = 0$) and $D = \frac{1}{-1} = -1$ (at $x = -1$). Comparing $x^2$ terms, $A + B = 0$, so $B = -1$. Then
$$\int = \ln\lvert x\rvert - \ln\lvert x + 1\rvert + \frac{1}{x + 1} + C,$$
since $\int -\frac{dx}{(x + 1)^2} = +\frac{1}{x + 1}$.

The option with $-\frac{1}{x + 1}$ makes a sign slip in this last step; the option without it ignores the repeated factor.""")

# q12
T.single(3, ["partial-fractions"],
    r"$\int\frac{x^2 + 1}{x^4 + 1}\,dx$ $(x > 0)$ equals",
    [r"$\frac{1}{\sqrt2}\tan^{-1}\frac{x^2 - 1}{\sqrt2\,x} + C$", r"$\frac{1}{\sqrt2}\tan^{-1}\frac{x^2 + 1}{\sqrt2\,x} + C$", r"$\sqrt2\tan^{-1}\frac{x^2 - 1}{\sqrt2\,x} + C$", r"$\frac{1}{2\sqrt2}\ln\left\lvert\frac{x^2 - \sqrt2\,x + 1}{x^2 + \sqrt2\,x + 1}\right\rvert + C$"],
    r"""Divide the numerator and denominator by $x^2$ and put $u = x - \frac1x$, $du = \left(1 + \frac{1}{x^2}\right)dx$:
$$\int\frac{1 + 1/x^2}{x^2 + 1/x^2}\,dx = \int\frac{du}{u^2 + 2} = \frac{1}{\sqrt2}\tan^{-1}\frac{u}{\sqrt2} = \frac{1}{\sqrt2}\tan^{-1}\frac{x^2 - 1}{\sqrt2\,x} + C.$$

The logarithm is the companion integral $\int\frac{x^2 - 1}{x^4 + 1}\,dx$ (substitute $x + \frac1x$). The $\frac{x^2 + 1}{\sqrt2\,x}$ option uses the wrong substitution, and $\sqrt2$ in front inverts the factor $\frac1a$.""")

# q13
T.single(2, ["half-angle"],
    r"$\int\frac{dx}{5 + 4\cos x}$ $(-\pi < x < \pi)$ equals",
    [r"$\frac{2}{3}\tan^{-1}\left(\frac{1}{3}\tan\frac{x}{2}\right) + C$", r"$\frac{1}{3}\tan^{-1}\left(\frac{1}{3}\tan\frac{x}{2}\right) + C$", r"$\frac{2}{3}\tan^{-1}\left(3\tan\frac{x}{2}\right) + C$", r"$\frac{1}{3}\ln\left\lvert\frac{3 + \tan(x/2)}{3 - \tan(x/2)}\right\rvert + C$"],
    r"""With $t = \tan\frac{x}{2}$:
$$\int\frac{2\,dt}{5(1 + t^2) + 4(1 - t^2)} = \int\frac{2\,dt}{9 + t^2} = \frac{2}{3}\tan^{-1}\frac{t}{3} + C.$$
This matches $\frac{2}{\sqrt{a^2 - b^2}}\tan^{-1}\left(\sqrt{\frac{a - b}{a + b}}\tan\frac{x}{2}\right)$ with $a = 5$, $b = 4$.

Forgetting the $2$ from $dx = \frac{2\,dt}{1 + t^2}$ gives $\frac13$. The factor $\sqrt{\frac{a - b}{a + b}} = \frac13$ is easily inverted to $3$. Since $a > b$, there is no logarithm.""")

# q14
T.single(3, ["half-angle"],
    r"$\int\frac{dx}{3 + 5\cos x}$ equals (on an interval where it is defined)",
    [r"$\frac{1}{4}\ln\left\lvert\frac{2 + \tan(x/2)}{2 - \tan(x/2)}\right\rvert + C$", r"$\frac{1}{2}\ln\left\lvert\frac{2 + \tan(x/2)}{2 - \tan(x/2)}\right\rvert + C$", r"$\frac{1}{4}\ln\left\lvert\frac{2 - \tan(x/2)}{2 + \tan(x/2)}\right\rvert + C$", r"$\frac{1}{2}\tan^{-1}\left(\frac{1}{2}\tan\frac{x}{2}\right) + C$"],
    r"""With $t = \tan\frac{x}{2}$:
$$\int\frac{2\,dt}{3(1 + t^2) + 5(1 - t^2)} = \int\frac{2\,dt}{8 - 2t^2} = \int\frac{dt}{4 - t^2} = \frac{1}{4}\ln\left\lvert\frac{2 + t}{2 - t}\right\rvert + C.$$

Since $a = 3 < b = 5$, the coefficient of $t^2$ is negative and the answer is a **logarithm**, so the $\tan^{-1}$ option is wrong. $\int\frac{dt}{4 - t^2}$ has factor $\frac{1}{2\cdot 2} = \frac14$, and the reversed quotient has the wrong sign.""")

# q15
T.single(2, ["trig-quotients"],
    r"$\int\frac{\sin x}{\sin x + \cos x}\,dx$ equals",
    [r"$\frac{x}{2} - \frac{1}{2}\ln\lvert\sin x + \cos x\rvert + C$", r"$\frac{x}{2} + \frac{1}{2}\ln\lvert\sin x + \cos x\rvert + C$", r"$\frac{1}{2}\ln\lvert\sin x + \cos x\rvert + C$", r"$x - \ln\lvert\sin x + \cos x\rvert + C$"],
    r"""Write the numerator as $A(\text{den}) + B(\text{den})'$, with $(\text{den})' = \cos x - \sin x$:
$$\sin x = \frac12(\sin x + \cos x) - \frac12(\cos x - \sin x).$$
So
$$\int = \frac{x}{2} - \frac12\ln\lvert\sin x + \cos x\rvert + C.$$

The $+$ sign option is $\int\frac{\cos x}{\sin x + \cos x}\,dx$; the two integrals add up to $x$. That sum is a fast check.""")

# q16
T.single(3, ["trig-quotients"],
    r"$\int\frac{3\sin x + 2\cos x}{2\sin x + 3\cos x}\,dx$ equals",
    [r"$\frac{12}{13}x - \frac{5}{13}\ln\lvert 2\sin x + 3\cos x\rvert + C$", r"$\frac{12}{13}x + \frac{5}{13}\ln\lvert 2\sin x + 3\cos x\rvert + C$", r"$\frac{5}{13}x - \frac{12}{13}\ln\lvert 2\sin x + 3\cos x\rvert + C$", r"$x - \frac{5}{13}\ln\lvert 2\sin x + 3\cos x\rvert + C$"],
    r"""Put $3\sin x + 2\cos x = A(2\sin x + 3\cos x) + B(2\cos x - 3\sin x)$. Comparing coefficients:
$$\sin x:\ 2A - 3B = 3, \qquad \cos x:\ 3A + 2B = 2.$$
Solving, $A = \frac{12}{13}$ and $B = -\frac{5}{13}$. Hence
$$\int = \frac{12}{13}x - \frac{5}{13}\ln\lvert 2\sin x + 3\cos x\rvert + C.$$

**Check:** $\frac{12}{13}(2, 3) - \frac{5}{13}(-3, 2) = \left(\frac{24 + 15}{13}, \frac{36 - 10}{13}\right) = (3, 2)$ as (sin, cos) coefficients. The option with $\frac{5}{13}x$ swaps $A$ and $B$.""")

# q17
T.single(2, ["trig-quotients"],
    r"$\int\frac{dx}{\sin x + \cos x}$ equals",
    [r"$\frac{1}{\sqrt2}\ln\left\lvert\tan\left(\frac{x}{2} + \frac{\pi}{8}\right)\right\rvert + C$", r"$\sqrt2\ln\left\lvert\tan\left(\frac{x}{2} + \frac{\pi}{8}\right)\right\rvert + C$", r"$\frac{1}{\sqrt2}\ln\left\lvert\tan\left(\frac{x}{2} + \frac{\pi}{4}\right)\right\rvert + C$", r"$\frac{1}{\sqrt2}\ln\left\lvert\tan\left(\frac{x}{2} - \frac{\pi}{8}\right)\right\rvert + C$"],
    r"""$\sin x + \cos x = \sqrt2\sin\left(x + \frac{\pi}{4}\right)$, so
$$\int\frac{dx}{\sin x + \cos x} = \frac{1}{\sqrt2}\int\operatorname{cosec}\left(x + \frac{\pi}{4}\right)dx = \frac{1}{\sqrt2}\ln\left\lvert\tan\left(\frac{x}{2} + \frac{\pi}{8}\right)\right\rvert + C.$$

Halving the shift is the trap: $\frac{x + \pi/4}{2} = \frac{x}{2} + \frac{\pi}{8}$, not $\frac{x}{2} + \frac{\pi}{4}$. The $-\frac{\pi}{8}$ option integrates $\frac{1}{\sin x - \cos x}$. The factor is $\frac1r = \frac{1}{\sqrt2}$, not $\sqrt2$.""")

# q18
T.single(3, ["trig-quotients"],
    r"$\int\frac{dx}{1 + 3\sin^2 x}$ $\left(-\frac{\pi}{2} < x < \frac{\pi}{2}\right)$ equals",
    [r"$\frac{1}{2}\tan^{-1}(2\tan x) + C$", r"$\frac{1}{2}\tan^{-1}\left(\frac{1}{2}\tan x\right) + C$", r"$\tan^{-1}(2\tan x) + C$", r"$\frac{1}{\sqrt3}\tan^{-1}\left(\sqrt3\tan x\right) + C$"],
    r"""Divide the numerator and denominator by $\cos^2 x$ and put $t = \tan x$:
$$\int\frac{\sec^2 x\,dx}{\sec^2 x + 3\tan^2 x} = \int\frac{dt}{1 + 4t^2} = \frac12\tan^{-1}(2t) + C = \frac12\tan^{-1}(2\tan x) + C.$$

The trap is writing $1 + 3t^2$ in the denominator, which gives the $\sqrt3$ option: $\sec^2 x = 1 + t^2$, so the denominator is $1 + t^2 + 3t^2 = 1 + 4t^2$.""")

# q19
T.single(1, ["irrational", "standard-forms"],
    r"$\int\frac{dx}{\sqrt{x^2 + 2x + 5}}$ equals",
    [r"$\ln\left\lvert x + 1 + \sqrt{x^2 + 2x + 5}\right\rvert + C$", r"$\ln\left\lvert x + \sqrt{x^2 + 2x + 5}\right\rvert + C$", r"$\sin^{-1}\frac{x + 1}{2} + C$", r"$\frac{1}{2}\tan^{-1}\frac{x + 1}{2} + C$"],
    r"""Complete the square: $x^2 + 2x + 5 = (x + 1)^2 + 2^2$. With $u = x + 1$,
$$\int\frac{du}{\sqrt{u^2 + 2^2}} = \ln\left\lvert u + \sqrt{u^2 + 4}\right\rvert + C = \ln\left\lvert x + 1 + \sqrt{x^2 + 2x + 5}\right\rvert + C.$$

$\sin^{-1}$ belongs to $\sqrt{a^2 - u^2}$, and $\tan^{-1}$ to $u^2 + a^2$ without a root. Dropping the $+1$ inside the log is the commonest slip.""")

# q20
T.single(2, ["irrational", "standard-forms"],
    r"$\int\sqrt{4 - x^2}\,dx$ $(\lvert x\rvert < 2)$ equals",
    [r"$\frac{x}{2}\sqrt{4 - x^2} + 2\sin^{-1}\frac{x}{2} + C$", r"$\frac{x}{2}\sqrt{4 - x^2} + 4\sin^{-1}\frac{x}{2} + C$", r"$\frac{x}{2}\sqrt{4 - x^2} - 2\sin^{-1}\frac{x}{2} + C$", r"$x\sqrt{4 - x^2} + 2\sin^{-1}\frac{x}{2} + C$"],
    r"""Use $\int\sqrt{a^2 - x^2}\,dx = \frac{x}{2}\sqrt{a^2 - x^2} + \frac{a^2}{2}\sin^{-1}\frac{x}{a}$ with $a = 2$:
$$\frac{x}{2}\sqrt{4 - x^2} + \frac{4}{2}\sin^{-1}\frac{x}{2} + C.$$

$4\sin^{-1}$ forgets the $\frac12$ on $a^2$. **Check:** over $[-2, 2]$ the key gives $2\left(\frac{\pi}{2} + \frac{\pi}{2}\right) = 2\pi$, the area of a semicircle of radius $2$.""")

# q21
T.single(3, ["irrational"],
    r"For $x > 1$, $\int\frac{dx}{(x + 1)\sqrt{x^2 - 1}}$ equals",
    [r"$\sqrt{\frac{x - 1}{x + 1}} + C$", r"$-\sqrt{\frac{x - 1}{x + 1}} + C$", r"$\sqrt{\frac{x + 1}{x - 1}} + C$", r"$\sec^{-1}x + C$"],
    r"""Put $x + 1 = \frac{1}{t}$, so $dx = -\frac{dt}{t^2}$ and $x^2 - 1 = \frac{1}{t}\left(\frac1t - 2\right) = \frac{1 - 2t}{t^2}$ (with $0 < t < \frac12$):
$$\int\frac{-dt/t^2}{\frac1t\cdot\frac{\sqrt{1 - 2t}}{t}} = -\int\frac{dt}{\sqrt{1 - 2t}} = \sqrt{1 - 2t} + C = \sqrt{\frac{x - 1}{x + 1}} + C.$$

**Check:** $\frac{d}{dx}\sqrt{\frac{x - 1}{x + 1}} = \frac12\sqrt{\frac{x + 1}{x - 1}}\cdot\frac{2}{(x + 1)^2} = \frac{1}{(x + 1)\sqrt{x^2 - 1}}$. The minus sign comes from losing the minus in $dx$ twice; $\sec^{-1}x$ is $\int\frac{dx}{x\sqrt{x^2 - 1}}$.""")

# q22
T.statements(1, ["standard-forms", "substitution"],
    r"Consider the following statements (each on a suitable interval):",
    [r"$\frac12\sin^2 x$ and $-\frac12\cos^2 x$ are both antiderivatives of $\sin x\cos x$.",
     r"$\int\frac{dx}{x} = \ln x + C$ for all $x \ne 0$.",
     r"$\int\tan x\,dx = \ln\lvert\sec x\rvert + C$."],
    [r"1 and 3 only", r"1, 2 and 3", r"3 only", r"2 and 3 only"],
    r"""**1 is true.** Both derivatives equal $\sin x\cos x$; the two functions differ by the constant $\frac12$, since $\frac12\sin^2 x - \left(-\frac12\cos^2 x\right) = \frac12$.

**2 is false.** $\ln x$ is not defined for $x < 0$. The correct form is $\ln\lvert x\rvert + C$.

**3 is true.** $\int\tan x\,dx = -\ln\lvert\cos x\rvert = \ln\lvert\sec x\rvert$.""")

# q23
T.statements(2, ["half-angle", "partial-fractions"],
    r"Consider the following statements:",
    [r"For $a > 0$, $\int\frac{dx}{a + a\cos x} = \frac{1}{a}\tan\frac{x}{2} + C$ on $(-\pi, \pi)$.",
     r"If $P/Q$ is a proper rational function and $(x - a)$ is a simple (non-repeated) factor of $Q$, then the coefficient of $\frac{1}{x - a}$ in its partial fractions is $\frac{P(a)}{Q'(a)}$.",
     r"The partial-fraction form of $\frac{1}{(x - 1)^2(x^2 + 1)}$ is $\frac{A}{x - 1} + \frac{B}{(x - 1)^2} + \frac{Cx + D}{x^2 + 1}$."],
    [r"1, 2 and 3", r"1 and 2 only", r"2 and 3 only", r"1 and 3 only"],
    r"""**1 is true.** $a(1 + \cos x) = 2a\cos^2\frac{x}{2}$, so the integral is $\frac{1}{2a}\int\sec^2\frac{x}{2}\,dx = \frac1a\tan\frac{x}{2} + C$.

**2 is true.** Write $Q = (x - a)R$ with $R(a) \ne 0$. The coefficient is $\frac{P(a)}{R(a)}$ (cover-up), and $Q'(a) = R(a)$.

**3 is true.** The repeated linear factor gives two terms and the irreducible quadratic gives a linear numerator. Four unknowns match the degree $4$ of the denominator.""")

# q24
T.match(1, ["standard-forms"],
    r"Match each integral ($a > 0$) with its value (constants of integration omitted).",
    [r"$\int\frac{dx}{\sqrt{a^2 - x^2}}$", r"$\int\frac{dx}{a^2 + x^2}$", r"$\int\frac{dx}{\sqrt{x^2 - a^2}}$", r"$\int\frac{dx}{a^2 - x^2}$"],
    [r"$\ln\left\lvert x + \sqrt{x^2 - a^2}\right\rvert$", r"$\frac{1}{2a}\ln\left\lvert\frac{a + x}{a - x}\right\rvert$", r"$\sin^{-1}\frac{x}{a}$", r"$\frac{1}{a}\tan^{-1}\frac{x}{a}$"],
    [r"A-3, B-4, C-1, D-2", r"A-3, B-4, C-2, D-1", r"A-1, B-4, C-3, D-2", r"A-3, B-2, C-1, D-4"],
    r"""- A: $\frac{d}{dx}\sin^{-1}\frac{x}{a} = \frac{1}{\sqrt{a^2 - x^2}}$, so A-3.
- B: $\frac{d}{dx}\frac1a\tan^{-1}\frac{x}{a} = \frac{1}{a^2 + x^2}$, so B-4.
- C: $\frac{d}{dx}\ln\left(x + \sqrt{x^2 - a^2}\right) = \frac{1}{\sqrt{x^2 - a^2}}$, so C-1.
- D: $\frac{1}{a^2 - x^2} = \frac{1}{2a}\left(\frac{1}{a - x} + \frac{1}{a + x}\right)$, so D-2.

The roots go with $\sin^{-1}$ and the logarithm of $x + \sqrt{\cdot}$; the rational forms go with $\tan^{-1}$ and the log of a quotient.""")

# q25
T.match(3, ["half-angle"],
    r"Match each integral with its value, where $t = \tan\frac{x}{2}$ (on an interval where both sides are defined; constants omitted).",
    [r"$\int\frac{dx}{2 + \cos x}$", r"$\int\frac{dx}{1 + 2\cos x}$", r"$\int\frac{dx}{2 + 2\cos x}$", r"$\int\frac{dx}{2 - 2\cos x}$"],
    [r"$\frac{1}{2}\tan\frac{x}{2}$", r"$\frac{1}{\sqrt3}\ln\left\lvert\frac{\sqrt3 + t}{\sqrt3 - t}\right\rvert$", r"$-\frac{1}{2}\cot\frac{x}{2}$", r"$\frac{2}{\sqrt3}\tan^{-1}\frac{t}{\sqrt3}$"],
    [r"A-4, B-2, C-1, D-3", r"A-2, B-4, C-1, D-3", r"A-4, B-2, C-3, D-1", r"A-4, B-1, C-2, D-3"],
    r"""With $t = \tan\frac{x}{2}$, $\int\frac{dx}{a + b\cos x} = \int\frac{2\,dt}{(a + b) + (a - b)t^2}$.

- A ($a = 2 > b = 1$): $\int\frac{2\,dt}{3 + t^2} = \frac{2}{\sqrt3}\tan^{-1}\frac{t}{\sqrt3}$, so A-4.
- B ($a = 1 < b = 2$): $\int\frac{2\,dt}{3 - t^2} = \frac{1}{\sqrt3}\ln\left\lvert\frac{\sqrt3 + t}{\sqrt3 - t}\right\rvert$, so B-2.
- C ($a = b$): $2 + 2\cos x = 4\cos^2\frac{x}{2}$, giving $\frac12\tan\frac{x}{2}$, so C-1.
- D: $2 - 2\cos x = 4\sin^2\frac{x}{2}$, giving $\frac14\int\operatorname{cosec}^2\frac{x}{2}\,dx = -\frac12\cot\frac{x}{2}$, so D-3.

The first case to settle is which of $a, b$ is larger: $a > b$ gives $\tan^{-1}$, $a < b$ gives a logarithm.""")

# q26
T.assertion_reason(2, ["half-angle"],
    r"On $(-\pi, \pi)$, $\int\frac{dx}{2 + \cos x} = \frac{2}{\sqrt3}\tan^{-1}\left(\frac{1}{\sqrt3}\tan\frac{x}{2}\right) + C$.",
    r"With $t = \tan\frac{x}{2}$, $\cos x = \frac{1 - t^2}{1 + t^2}$ and $dx = \frac{2\,dt}{1 + t^2}$.",
    0,
    r"""Both are true, and R explains A.

By R,
$$\int\frac{dx}{2 + \cos x} = \int\frac{2\,dt}{2(1 + t^2) + (1 - t^2)} = \int\frac{2\,dt}{3 + t^2} = \frac{2}{\sqrt3}\tan^{-1}\frac{t}{\sqrt3} + C.$$
The interval $(-\pi, \pi)$ matters: $\tan\frac{x}{2}$ is undefined at $x = \pm\pi$, where this formula jumps.""")

# q27
T.assertion_reason(2, ["by-parts"],
    r"$\int e^x(\sin x + \cos x)\,dx = e^x\sin x + C$.",
    r"$\int e^x\sin x\,dx = \frac{1}{2}e^x(\sin x - \cos x) + C$.",
    1,
    r"""Both are true, but R does not explain A.

A follows from $\int e^x(f + f')\,dx = e^x f$ with $f = \sin x$, $f' = \cos x$.

R is the recurring-integral formula $\int e^{ax}\sin bx\,dx = \frac{e^{ax}(a\sin bx - b\cos bx)}{a^2 + b^2}$ with $a = b = 1$. It is correct, but it is not the reason for A: A needs no recurring integral at all.""")

# q28
T.assertion_reason(2, ["partial-fractions", "standard-forms"],
    r"$\int\frac{dx}{x^2 + 2x + 2} = \tan^{-1}(x + 1) + C$.",
    r"$x^2 + 2x + 2$ has two distinct real roots, so its reciprocal splits into partial fractions over $\R$.",
    2,
    r"""A is true and R is false.

A: $x^2 + 2x + 2 = (x + 1)^2 + 1$, so the integral is $\tan^{-1}(x + 1) + C$.

R: the discriminant is $4 - 8 = -4 < 0$, so the quadratic is **irreducible** over $\R$. That is exactly why the answer is a $\tan^{-1}$ and not a logarithm.""")

# q29
T.assertion_reason(2, ["half-angle"],
    r"$\int\frac{dx}{1 + \cos x} = \frac{1}{2}\tan\frac{x}{2} + C$.",
    r"$1 + \cos x = 2\cos^2\frac{x}{2}$.",
    3,
    r"""A is false and R is true.

By R,
$$\int\frac{dx}{1 + \cos x} = \frac12\int\sec^2\frac{x}{2}\,dx = \frac12\cdot 2\tan\frac{x}{2} + C = \tan\frac{x}{2} + C.$$
A forgets the factor $2$ from integrating $\sec^2\frac{x}{2}$ (the chain rule in reverse). This is the case $a = b = 1$ of $\frac1a\tan\frac{x}{2}$.""")

# q30
T.assertion_reason(3, ["by-parts", "partial-fractions"],
    r"$\int\frac{x e^x}{(x + 1)^2}\,dx = \frac{e^x}{x + 1} + C$.",
    r"$\int e^x\left(f(x) + f'(x)\right)dx = e^x f(x) + C$.",
    0,
    r"""Both are true, and R explains A.

Split the rational factor:
$$\frac{x}{(x + 1)^2} = \frac{(x + 1) - 1}{(x + 1)^2} = \frac{1}{x + 1} - \frac{1}{(x + 1)^2} = f + f', \qquad f = \frac{1}{x + 1}.$$
By R the integral is $\frac{e^x}{x + 1} + C$. R itself holds because $\frac{d}{dx}(e^x f) = e^x(f + f')$.""")


def check():
    import sympy as sp
    x, t = sp.symbols("x t", real=True)
    pts = [sp.Rational(3, 10), sp.Rational(7, 10), sp.Rational(6, 5), sp.Rational(-2, 5)]

    def anti(F, f, label, at=pts):
        """F is an antiderivative of f: symbolic simplify, else numeric at several points."""
        d = sp.simplify(sp.diff(F, x) - f)
        if d != 0:
            for p in at:
                v = complex(sp.N(sp.diff(F, x).subs(x, p) - f.subs(x, p), 30))
                if abs(v) > 1e-12:
                    sys.exit(f"CHECK FAILED {label}: F' - f = {v} at x = {p}")

    def wrong(F, f, label, at=pts):
        """F is NOT an antiderivative of f (derivative differs at some point)."""
        for p in at:
            v = complex(sp.N(sp.diff(F, x).subs(x, p) - f.subs(x, p), 30))
            if abs(v) > 1e-8:
                return
        sys.exit(f"CHECK FAILED {label}: distractor is also an antiderivative")

    def defint(F, f, a, b, label):
        """Numeric cross-check: F(b) - F(a) = integral of f over [a, b]."""
        eq(sp.N(F.subs(x, b) - F.subs(x, a), 20), sp.N(sp.Integral(f, (x, a, b)), 20), label)

    L, s, c = sp.log, sp.sin, sp.cos
    h = x / 2
    # q1
    f = 1 / s(x)
    anti(L(sp.tan(h)), f, "q1"); defint(L(sp.tan(h)), f, 0.5, 1.5, "q1 N")
    wrong(L(1 / s(x) + 1 / sp.tan(x)), f, "q1 d1"); wrong(L(s(x)), f, "q1 d2"); wrong(-1 / s(x) / sp.tan(x), f, "q1 d3")
    # q2
    f = 1 / (x**2 - 9); F = L((3 - x) / (x + 3)) / 6   # on |x| < 3
    anti(F, f, "q2"); eq(sp.diff(F - sp.integrate(f, x), x), 0, "q2 sympy")
    wrong(L((3 - x) / (x + 3)) / 3, f, "q2 d1"); wrong(L((x + 3) / (3 - x)) / 6, f, "q2 d2"); wrong(sp.atan(x / 3) / 3, f, "q2 d3")
    # q3
    f = c(x) / (1 + s(x))**2
    anti(-1 / (1 + s(x)), f, "q3"); wrong(1 / (1 + s(x)), f, "q3 d1"); wrong(L(1 + s(x)), f, "q3 d2"); wrong(-1 / (3 * (1 + s(x))**3), f, "q3 d3")
    # q4
    xp = [sp.Rational(1, 2), 2, 3]
    f = L(x)
    anti(x * L(x) - x, f, "q4", xp); eq(sp.integrate(f, x), x * L(x) - x, "q4 sympy")
    wrong(x * L(x) + x, f, "q4 d1", xp); wrong(1 / x, f, "q4 d2", xp); wrong(L(x)**2 / 2, f, "q4 d3", xp)
    # q5
    f = x**2 * sp.exp(x)
    anti(sp.exp(x) * (x**2 - 2 * x + 2), f, "q5"); eq(sp.integrate(f, x), sp.exp(x) * (x**2 - 2 * x + 2), "q5 sympy")
    wrong(sp.exp(x) * (x**2 + 2 * x + 2), f, "q5 d1"); wrong(sp.exp(x) * (x**2 - 2 * x - 2), f, "q5 d2"); wrong(x**3 * sp.exp(x) / 3, f, "q5 d3")
    # q6
    f = sp.exp(x) * (1 + s(x)) / (1 + c(x))
    anti(sp.exp(x) * sp.tan(h), f, "q6"); defint(sp.exp(x) * sp.tan(h), f, 0, 1, "q6 N")
    wrong(sp.exp(x) / sp.tan(h), f, "q6 d1"); wrong(-sp.exp(x) / sp.tan(h), f, "q6 d2"); wrong(sp.exp(x) / c(h)**2 / 2, f, "q6 d3")
    # q7
    f = sp.exp(2 * x) * s(3 * x)
    F = sp.exp(2 * x) * (2 * s(3 * x) - 3 * c(3 * x)) / 13
    anti(F, f, "q7"); eq(sp.integrate(f, x), F, "q7 sympy")
    wrong(sp.exp(2 * x) * (2 * s(3 * x) + 3 * c(3 * x)) / 13, f, "q7 d1"); wrong(sp.exp(2 * x) * (3 * s(3 * x) - 2 * c(3 * x)) / 13, f, "q7 d2"); wrong(sp.exp(2 * x) * (2 * s(3 * x) - 3 * c(3 * x)) / 5, f, "q7 d3")
    # q8
    f = sp.atan(x)
    anti(x * sp.atan(x) - L(1 + x**2) / 2, f, "q8"); eq(sp.integrate(f, x), x * sp.atan(x) - L(1 + x**2) / 2, "q8 sympy")
    wrong(x * sp.atan(x) + L(1 + x**2) / 2, f, "q8 d1"); wrong(x * sp.atan(x) - L(1 + x**2), f, "q8 d2"); wrong(1 / (1 + x**2), f, "q8 d3")
    # q9 (on -2 < x < 1)
    f = 1 / ((x - 1) * (x + 2))
    anti(L((1 - x) / (x + 2)) / 3, f, "q9"); eq(sp.apart(f, x), 1 / (3 * (x - 1)) - 1 / (3 * (x + 2)), "q9 apart")
    wrong(L((x + 2) / (1 - x)) / 3, f, "q9 d1"); wrong(L((1 - x) * (x + 2)), f, "q9 d2"); wrong(L((1 - x) * (x + 2)) / 3, f, "q9 d3")
    # q10 (x > 0)
    f = 1 / (x * (x**2 + 1))
    anti(L(x) - L(x**2 + 1) / 2, f, "q10", xp); eq(sp.apart(f, x), 1 / x - x / (x**2 + 1), "q10 apart")
    wrong(L(x) + L(x**2 + 1) / 2, f, "q10 d1", xp); wrong(L(x) - L(x**2 + 1), f, "q10 d2", xp); wrong(L(x) - sp.atan(x), f, "q10 d3", xp)
    # q11 (x > 0)
    f = 1 / (x * (x + 1)**2)
    anti(L(x / (x + 1)) + 1 / (x + 1), f, "q11", xp); eq(sp.apart(f, x), 1 / x - 1 / (x + 1) - 1 / (x + 1)**2, "q11 apart")
    wrong(L(x / (x + 1)) - 1 / (x + 1), f, "q11 d1", xp); wrong(L(x * (x + 1)) + 1 / (x + 1), f, "q11 d2", xp); wrong(L(x / (x + 1)), f, "q11 d3", xp)
    # q12 (x > 0)
    f = (x**2 + 1) / (x**4 + 1)
    F = sp.atan((x**2 - 1) / (sp.sqrt(2) * x)) / sp.sqrt(2)
    anti(F, f, "q12", xp); defint(F, f, 0.5, 3, "q12 N")
    wrong(sp.atan((x**2 + 1) / (sp.sqrt(2) * x)) / sp.sqrt(2), f, "q12 d1", xp); wrong(sp.sqrt(2) * sp.atan((x**2 - 1) / (sp.sqrt(2) * x)), f, "q12 d2", xp)
    G = L((x**2 - sp.sqrt(2) * x + 1) / (x**2 + sp.sqrt(2) * x + 1)) / (2 * sp.sqrt(2))
    wrong(G, f, "q12 d3", xp); anti(G, (x**2 - 1) / (x**4 + 1), "q12 companion", xp)
    # q13
    f = 1 / (5 + 4 * c(x))
    F = sp.Rational(2, 3) * sp.atan(sp.tan(h) / 3)
    anti(F, f, "q13"); defint(F, f, -2, 2.5, "q13 N")
    wrong(F / 2, f, "q13 d1"); wrong(sp.Rational(2, 3) * sp.atan(3 * sp.tan(h)), f, "q13 d2"); wrong(L((3 + sp.tan(h)) / (3 - sp.tan(h))) / 3, f, "q13 d3")
    eq((sp.integrate(2 / (9 + t**2), t)).subs(t, sp.tan(h)) - F, 0, "q13 t")
    # q14 on |x| < 2 acos(-3/5)... take x in (-1, 1) where 3 + 5cos x > 0 and tan(x/2) < 2
    f = 1 / (3 + 5 * c(x))
    F = L((2 + sp.tan(h)) / (2 - sp.tan(h))) / 4
    anti(F, f, "q14"); defint(F, f, -1, 1, "q14 N")
    wrong(2 * F, f, "q14 d1"); wrong(-F, f, "q14 d2"); wrong(sp.atan(sp.tan(h) / 2) / 2, f, "q14 d3")
    # q15 (sin x + cos x > 0 at test points)
    f = s(x) / (s(x) + c(x))
    anti(x / 2 - L(s(x) + c(x)) / 2, f, "q15")
    wrong(x / 2 + L(s(x) + c(x)) / 2, f, "q15 d1"); wrong(L(s(x) + c(x)) / 2, f, "q15 d2"); wrong(x - L(s(x) + c(x)), f, "q15 d3")
    # q16: A, B by the general formula and by solving
    l, m, n, p = 3, 2, 2, 3
    A, B = sp.symbols("A B")
    sol = sp.solve([A * n - B * p - l, A * p + B * n - m], [A, B])
    eq(sol[A], sp.Rational(12, 13), "q16 A"); eq(sol[B], sp.Rational(-5, 13), "q16 B")
    eq(sp.Rational(l * n + m * p, n * n + p * p), sol[A], "q16 A formula"); eq(sp.Rational(m * n - l * p, n * n + p * p), sol[B], "q16 B formula")
    f = (3 * s(x) + 2 * c(x)) / (2 * s(x) + 3 * c(x))
    D = 2 * s(x) + 3 * c(x)
    anti(sp.Rational(12, 13) * x - sp.Rational(5, 13) * L(D), f, "q16")
    wrong(sp.Rational(12, 13) * x + sp.Rational(5, 13) * L(D), f, "q16 d1"); wrong(sp.Rational(5, 13) * x - sp.Rational(12, 13) * L(D), f, "q16 d2"); wrong(x - sp.Rational(5, 13) * L(D), f, "q16 d3")
    # q17
    f = 1 / (s(x) + c(x))
    F = L(sp.tan(h + sp.pi / 8)) / sp.sqrt(2)
    anti(F, f, "q17"); defint(F, f, 0, 1, "q17 N")
    wrong(2 * F, f, "q17 d1"); wrong(L(sp.tan(h + sp.pi / 4)) / sp.sqrt(2), f, "q17 d2")
    wrong(L(sp.tan(h - sp.pi / 8)) / sp.sqrt(2), f, "q17 d3", [sp.Rational(3, 2), 2])
    anti(L(sp.tan(h - sp.pi / 8)) / sp.sqrt(2), 1 / (s(x) - c(x)), "q17 d3 is 1/(sin-cos)", [sp.Rational(3, 2), 2])
    # q18
    f = 1 / (1 + 3 * s(x)**2)
    F = sp.atan(2 * sp.tan(x)) / 2
    anti(F, f, "q18"); defint(F, f, -1, 1.2, "q18 N")
    wrong(sp.atan(sp.tan(x) / 2) / 2, f, "q18 d1"); wrong(2 * F, f, "q18 d2"); wrong(sp.atan(sp.sqrt(3) * sp.tan(x)) / sp.sqrt(3), f, "q18 d3")
    # q19
    f = 1 / sp.sqrt(x**2 + 2 * x + 5)
    anti(L(x + 1 + sp.sqrt(x**2 + 2 * x + 5)), f, "q19")
    wrong(L(x + sp.sqrt(x**2 + 2 * x + 5)), f, "q19 d1"); wrong(sp.asin((x + 1) / 2), f, "q19 d2"); wrong(sp.atan((x + 1) / 2) / 2, f, "q19 d3")
    # q20
    f = sp.sqrt(4 - x**2)
    F = x / 2 * sp.sqrt(4 - x**2) + 2 * sp.asin(x / 2)
    anti(F, f, "q20"); eq(F.subs(x, 2) - F.subs(x, -2), 2 * sp.pi, "q20 semicircle")
    wrong(x / 2 * sp.sqrt(4 - x**2) + 4 * sp.asin(x / 2), f, "q20 d1"); wrong(x / 2 * sp.sqrt(4 - x**2) - 2 * sp.asin(x / 2), f, "q20 d2"); wrong(x * sp.sqrt(4 - x**2) + 2 * sp.asin(x / 2), f, "q20 d3")
    # q21 (x > 1)
    xq = [sp.Rational(3, 2), 2, 5]
    f = 1 / ((x + 1) * sp.sqrt(x**2 - 1))
    F = sp.sqrt((x - 1) / (x + 1))
    anti(F, f, "q21", xq); defint(F, f, 2, 5, "q21 N")
    wrong(-F, f, "q21 d1", xq); wrong(1 / F, f, "q21 d2", xq); wrong(sp.asec(x), f, "q21 d3", xq)
    # q22
    anti(s(x)**2 / 2, s(x) * c(x), "q22 s1a"); anti(-c(x)**2 / 2, s(x) * c(x), "q22 s1b")
    assert L(sp.Integer(-2)).is_real is False, "q22 s2"  # ln x is not real for x < 0
    anti(L(-x), 1 / x, "q22 s2: ln|x| on x < 0", [-1, -2])
    anti(L(1 / c(x)), sp.tan(x), "q22 s3")
    # q23
    a = sp.Symbol("a", positive=True)
    anti(sp.tan(h) / a, 1 / (a + a * c(x)), "q23 s1")
    P, Q, r = 3 * x + 5, (x - 2) * (x + 1) * (x**2 + 1), 2
    coeff = sp.limit((x - r) * P / Q, x, r)
    eq(coeff, (P / sp.diff(Q, x)).subs(x, r), "q23 s2")
    ap = sp.apart(1 / ((x - 1)**2 * (x**2 + 1)), x)
    A1, B1, C1, D1 = sp.symbols("A1 B1 C1 D1")
    form = A1 / (x - 1) + B1 / (x - 1)**2 + (C1 * x + D1) / (x**2 + 1)
    num = sp.Poly(sp.expand(sp.cancel(form * (x - 1)**2 * (x**2 + 1))) - 1, x)
    sol4 = sp.solve(num.all_coeffs(), [A1, B1, C1, D1], dict=True)
    assert len(sol4) == 1, "q23 s3 unique solution"
    eq(form.subs(sol4[0]) - ap, 0, "q23 s3 form")
    eq(sp.apart(1 / ((x - 1)**2 * (x**2 + 1)), x), -1 / (2 * (x - 1)) + 1 / (2 * (x - 1)**2) + x / (2 * (x**2 + 1)), "q23 s3 form")
    # q24 (a = 2, x in range for each)
    aa = 2
    anti(sp.asin(x / aa), 1 / sp.sqrt(aa**2 - x**2), "q24 A")
    anti(sp.atan(x / aa) / aa, 1 / (aa**2 + x**2), "q24 B")
    anti(L(x + sp.sqrt(x**2 - aa**2)), 1 / sp.sqrt(x**2 - aa**2), "q24 C", [3, 5])
    anti(L((aa + x) / (aa - x)) / (2 * aa), 1 / (aa**2 - x**2), "q24 D")
    # q25
    T_ = sp.tan(h)
    anti(2 / sp.sqrt(3) * sp.atan(T_ / sp.sqrt(3)), 1 / (2 + c(x)), "q25 A")
    anti(L((sp.sqrt(3) + T_) / (sp.sqrt(3) - T_)) / sp.sqrt(3), 1 / (1 + 2 * c(x)), "q25 B")
    anti(T_ / 2, 1 / (2 + 2 * c(x)), "q25 C")
    anti(-1 / sp.tan(h) / 2, 1 / (2 - 2 * c(x)), "q25 D", [sp.Rational(1, 2), 1, 2])
    # q26
    anti(2 / sp.sqrt(3) * sp.atan(T_ / sp.sqrt(3)), 1 / (2 + c(x)), "q26 A")
    eq((1 - T_**2) / (1 + T_**2) - c(x), 0, "q26 R cos"); eq(sp.diff(2 * sp.atan(t), t), 2 / (1 + t**2), "q26 R dx")
    # q27
    anti(sp.exp(x) * s(x), sp.exp(x) * (s(x) + c(x)), "q27 A")
    anti(sp.exp(x) * (s(x) - c(x)) / 2, sp.exp(x) * s(x), "q27 R")
    # q28
    anti(sp.atan(x + 1), 1 / (x**2 + 2 * x + 2), "q28 A")
    eq(sp.discriminant(x**2 + 2 * x + 2, x), -4, "q28 R false"); eq(len(sp.real_roots(x**2 + 2 * x + 2)), 0, "q28 R no real roots")
    # q29: A false, R true
    wrong(sp.tan(h) / 2, 1 / (1 + c(x)), "q29 A false"); anti(sp.tan(h), 1 / (1 + c(x)), "q29 correct")
    eq(1 + c(x) - 2 * c(h)**2, 0, "q29 R")
    # q30
    f = x * sp.exp(x) / (x + 1)**2
    anti(sp.exp(x) / (x + 1), f, "q30 A", xp); eq(sp.apart(x / (x + 1)**2, x), 1 / (x + 1) - 1 / (x + 1)**2, "q30 split")
    g = sp.Function("g")
    eq(sp.diff(sp.exp(x) * g(x), x) - sp.exp(x) * (g(x) + sp.diff(g(x), x)), 0, "q30 R")


T.write(check)
