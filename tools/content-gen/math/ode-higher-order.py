import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from qlib import Topic, eq

T = Topic("math.ode.ode-higher-order")

# ---------------------------------------------------------------- singles: easy
T.single(1, ["constant-coefficients"], r"The general solution of $y'' - 5y' + 6y = 0$ is",
         [r"$y = c_1e^{2x} + c_2e^{3x}$", r"$y = c_1e^{-2x} + c_2e^{-3x}$",
          r"$y = c_1e^{x} + c_2e^{6x}$", r"$y = c_1e^{2x} + c_2e^{-3x}$"],
         r"""Auxiliary equation:
$$m^2 - 5m + 6 = (m - 2)(m - 3) = 0 \;\Rightarrow\; m = 2, 3.$$
So $y = c_1e^{2x} + c_2e^{3x}$.
$e^{-2x}, e^{-3x}$ comes from a sign slip (those are the roots of $m^2 + 5m + 6$). $e^{x}, e^{6x}$ uses $1 \cdot 6 = 6$ but $1 + 6 \ne 5$. Check: the roots must add to $5$ and multiply to $6$.""")

T.single(1, ["constant-coefficients"], r"The general solution of $y'' + 4y = 0$ is",
         [r"$y = c_1\cos 2x + c_2\sin 2x$", r"$y = c_1e^{2x} + c_2e^{-2x}$",
          r"$y = (c_1 + c_2x)e^{2x}$", r"$y = c_1\cos 4x + c_2\sin 4x$"],
         r"""$m^2 + 4 = 0$ gives $m = \pm 2i$, so $\alpha = 0$, $\beta = 2$:
$$y = c_1\cos 2x + c_2\sin 2x.$$
$c_1e^{2x} + c_2e^{-2x}$ solves $y'' - 4y = 0$ (sign slip). $\cos 4x$ uses $\beta = 4$ instead of $\sqrt4$.""")

T.single(1, ["constant-coefficients"], r"The general solution of $y'' - 6y' + 9y = 0$ is",
         [r"$y = (c_1 + c_2x)e^{3x}$", r"$y = c_1e^{3x} + c_2e^{-3x}$",
          r"$y = (c_1 + c_2x)e^{-3x}$", r"$y = c_1\cos 3x + c_2\sin 3x$"],
         r"""$m^2 - 6m + 9 = (m - 3)^2 = 0$, so $m = 3$ is a double root. A repeated root needs the extra factor $x$:
$$y = (c_1 + c_2x)e^{3x}.$$
$(c_1 + c_2x)e^{-3x}$ is the sign slip; it solves $y'' + 6y' + 9y = 0$. $c_1e^{3x} + c_2e^{-3x}$ treats the root as $\pm 3$.""")

T.single(1, ["wronskian"], r"The Wronskian $W(e^{2x}, e^{3x})$ equals",
         [r"$e^{5x}$", r"$-e^{5x}$", r"$5e^{5x}$", r"$6e^{5x}$"],
         r"""$$W = \begin{vmatrix} e^{2x} & e^{3x} \\ 2e^{2x} & 3e^{3x} \end{vmatrix} = 3e^{5x} - 2e^{5x} = e^{5x}.$$
In general $W(e^{ax}, e^{bx}) = (b - a)e^{(a + b)x}$. $-e^{5x}$ takes $y_1'y_2 - y_1y_2'$ (wrong order). $5e^{5x}$ adds the exponents instead of subtracting them.""")

T.single(1, ["d-operator"], r"A particular integral of $(D^2 + 3D + 2)y = e^{3x}$, where $D = \frac{d}{dx}$, is",
         [r"$\dfrac{e^{3x}}{20}$", r"$\dfrac{e^{3x}}{2}$", r"$\dfrac{e^{3x}}{14}$", r"$\dfrac{e^{3x}}{11}$"],
         r"""Since $f(3) = 9 + 9 + 2 = 20 \ne 0$,
$$y_p = \frac{1}{f(D)}e^{3x} = \frac{e^{3x}}{f(3)} = \frac{e^{3x}}{20}.$$
$\frac{e^{3x}}{2}$ comes from $f(-3) = 9 - 9 + 2$ (sign slip). $\frac{e^{3x}}{11}$ forgets the $3D$ term. Check: $D^2 + 3D + 2$ applied to $e^{3x}$ gives $20e^{3x}$.""")

T.single(1, ["d-operator"], r"A particular integral of $(D^2 + 4)y = \sin x$ is",
         [r"$\dfrac{\sin x}{3}$", r"$-\dfrac{\sin x}{3}$", r"$\dfrac{\sin x}{5}$", r"$-\dfrac{\sin x}{5}$"],
         r"""Replace $D^2$ by $-a^2 = -1$:
$$y_p = \frac{1}{-1 + 4}\sin x = \frac{\sin x}{3}.$$
$\frac{\sin x}{5}$ replaces $D^2$ by $+1$. Check: $(\sin x/3)'' + 4\sin x/3 = (-1 + 4)\sin x/3 = \sin x$.""")

# ---------------------------------------------------------------- singles: medium
T.single(2, ["d-operator"], r"A particular integral of $(D^2 + 4)y = \cos 2x$ is",
         [r"$\dfrac{x\sin 2x}{4}$", r"$\dfrac{x\sin 2x}{2}$", r"$-\dfrac{x\cos 2x}{4}$", r"$\dfrac{x\cos 2x}{4}$"],
         r"""$\cos 2x$ lies in the CF, since $D^2 + 4$ vanishes at $D^2 = -4$. Use the resonance rule
$$\frac{1}{D^2 + a^2}\cos ax = \frac{x\sin ax}{2a} \;\Rightarrow\; y_p = \frac{x\sin 2x}{4}.$$
$-\frac{x\cos 2x}{4}$ is the PI for $\sin 2x$. $\frac{x\sin 2x}{2}$ forgets the factor $a = 2$ in $2a$.
Check: $D^2\left(\frac{x\sin 2x}{4}\right) = \cos 2x - x\sin 2x$, and adding $x\sin 2x$ leaves $\cos 2x$.""")

T.single(2, ["d-operator"], r"A particular integral of $(D^2 - 3D + 2)y = e^{x}$ is",
         [r"$-xe^{x}$", r"$xe^{x}$", r"$-\dfrac{x^2e^{x}}{2}$", r"$\dfrac{xe^{x}}{2}$"],
         r"""$f(1) = 1 - 3 + 2 = 0$, so $e^{x}$ is in the CF and the simple rule fails. With $f'(D) = 2D - 3$ and $f'(1) = -1 \ne 0$,
$$y_p = x\frac{e^{x}}{f'(1)} = -xe^{x}.$$
$xe^{x}$ drops the sign of $f'(1)$. The $x^2$ form is for a double root, but $1$ is a simple root ($f = (D - 1)(D - 2)$).""")

T.single(2, ["d-operator"], r"A particular integral of $(D^2 - 4)y = x^2$ is",
         [r"$-\dfrac{x^2}{4} - \dfrac18$", r"$-\dfrac{x^2}{4} + \dfrac18$", r"$\dfrac{x^2}{4} + \dfrac18$", r"$-\dfrac{x^2}{4} - \dfrac12$"],
         r"""$$\frac{1}{D^2 - 4}x^2 = -\frac14\left(1 - \frac{D^2}{4}\right)^{-1}x^2 = -\frac14\left(1 + \frac{D^2}{4}\right)x^2 = -\frac14\left(x^2 + \frac12\right).$$
So $y_p = -\frac{x^2}{4} - \frac18$. $+\frac18$ expands $(1 - u)^{-1}$ as $1 - u$. $-\frac12$ forgets the $\frac14$ in front.
Check: $D^2y_p = -\frac12$, and $-4y_p = x^2 + \frac12$; the sum is $x^2$.""")

T.single(2, ["d-operator"], r"A particular integral of $(D - 1)^2y = xe^{x}$ is",
         [r"$\dfrac{x^3e^{x}}{6}$", r"$\dfrac{x^3e^{x}}{3}$", r"$\dfrac{x^2e^{x}}{2}$", r"$\dfrac{x^3}{6}$"],
         r"""Exponential shift, $D \to D + 1$:
$$\frac{1}{(D - 1)^2}e^{x}x = e^{x}\frac{1}{D^2}x = e^{x}\cdot\frac{x^3}{6}.$$
$\frac{x^2e^{x}}{2}$ is the PI for $e^{x}$ alone. $\frac{x^3}{6}$ drops the factor $e^{x}$ after the shift. $\frac{x^3e^{x}}{3}$ integrates $x$ twice wrongly ($\iint x = \frac{x^3}{6}$).""")

T.single(2, ["wronskian"], r"Let $y_1, y_2$ be solutions of $y'' + 2y' + 5y = 0$ with Wronskian $W(0) = 3$. Then $W(x)$ equals",
         [r"$3e^{-2x}$", r"$3e^{2x}$", r"$3e^{-5x}$", r"$3$"],
         r"""Abel's formula for $y'' + Py' + Qy = 0$ gives $W(x) = W(0)e^{-\int_0^x P\,dt}$. Here $P = 2$, so
$$W(x) = 3e^{-2x}.$$
$3e^{2x}$ drops the minus sign. $3e^{-5x}$ uses $Q$ instead of $P$. Check with $y_1 = e^{-x}\cos 2x$, $y_2 = e^{-x}\sin 2x$: their Wronskian is $2e^{-2x}$, a constant multiple of $e^{-2x}$.""")

T.single(2, ["cauchy-euler"], r"For $x > 0$, the general solution of $x^2y'' - 2xy' + 2y = 0$ is",
         [r"$y = c_1x + c_2x^2$", r"$y = c_1x^{-1} + c_2x^{-2}$",
          r"$y = x\left[c_1\cos(\ln x) + c_2\sin(\ln x)\right]$", r"$y = c_1x + c_2x^3$"],
         r"""Try $y = x^m$:
$$m(m - 1) - 2m + 2 = m^2 - 3m + 2 = 0 \;\Rightarrow\; m = 1, 2.$$
So $y = c_1x + c_2x^2$. The $\cos(\ln x)$ option uses $x^2D^2 = \theta^2$, which gives $m^2 - 2m + 2 = 0$ and $m = 1 \pm i$. $x^{-1}, x^{-2}$ is a sign slip. Check: $y = x^2$ gives $2x^2 - 4x^2 + 2x^2 = 0$.""")

T.single(2, ["cauchy-euler"], r"For $x > 0$, the general solution of $x^2y'' + xy' + y = 0$ is",
         [r"$y = c_1\cos(\ln x) + c_2\sin(\ln x)$", r"$y = c_1\cos x + c_2\sin x$",
          r"$y = c_1x + c_2x^{-1}$", r"$y = c_1 + c_2\ln x$"],
         r"""With $x = e^{z}$: $\theta(\theta - 1) + \theta + 1 = \theta^2 + 1$, so $(\theta^2 + 1)y = 0$ and
$$y = c_1\cos z + c_2\sin z = c_1\cos(\ln x) + c_2\sin(\ln x).$$
$c_1x + c_2x^{-1}$ solves $x^2y'' + xy' - y = 0$. $c_1 + c_2\ln x$ solves $x^2y'' + xy' = 0$. $\cos x$ forgets to change back from $z$ to $\ln x$.""")

T.single(2, ["constant-coefficients"], r"The linear equation with constant coefficients whose general solution is $y = e^{x}(c_1\cos 2x + c_2\sin 2x)$ is",
         [r"$y'' - 2y' + 5y = 0$", r"$y'' + 2y' + 5y = 0$", r"$y'' - 2y' + 3y = 0$", r"$y'' - 2y' - 3y = 0$"],
         r"""The roots are $1 \pm 2i$. Their sum is $2$ and their product is $1 + 4 = 5$, so the auxiliary equation is $m^2 - 2m + 5 = 0$:
$$y'' - 2y' + 5y = 0.$$
$y'' + 2y' + 5y = 0$ has roots $-1 \pm 2i$ (the solutions decay). $y'' - 2y' + 3y = 0$ computes the product as $1 - 4$ wrongly.""")

T.single(2, ["d-operator-advanced"], r"The solution of $y'' + 4y = 4$ with $y(0) = 0$, $y'(0) = 0$ is",
         [r"$y = 1 - \cos 2x$", r"$y = 1 + \cos 2x$", r"$y = \dfrac{1 - \cos 2x}{4}$", r"$y = 1 - \cos 2x + \sin 2x$"],
         r"""PI: $\frac{1}{D^2 + 4}\,4 = 1$. The general solution is $y = c_1\cos 2x + c_2\sin 2x + 1$.
- $y(0) = c_1 + 1 = 0$ gives $c_1 = -1$.
- $y'(0) = 2c_2 = 0$ gives $c_2 = 0$.

So $y = 1 - \cos 2x$. $\frac{1 - \cos 2x}{4}$ takes the PI as $\frac14$ (it solves $y'' + 4y = 1$). $1 + \cos 2x$ fails $y(0) = 0$. The $+\sin 2x$ option fails $y'(0) = 0$.""")

# ---------------------------------------------------------------- singles: hard
T.single(3, ["d-operator"], r"A particular integral of $(D^2 - 2D + 5)y = e^{x}\cos 2x$ is",
         [r"$\dfrac{xe^{x}\sin 2x}{4}$", r"$\dfrac{xe^{x}\sin 2x}{2}$", r"$-\dfrac{xe^{x}\sin 2x}{4}$", r"$\dfrac{xe^{x}\cos 2x}{4}$"],
         r"""Shift $e^{x}$ through, $D \to D + 1$:
$$(D + 1)^2 - 2(D + 1) + 5 = D^2 + 4, \qquad y_p = e^{x}\frac{1}{D^2 + 4}\cos 2x = e^{x}\cdot\frac{x\sin 2x}{4}.$$
This is resonance: the roots $1 \pm 2i$ make $e^{x}\cos 2x$ part of the CF, so a factor $x$ must appear. $\frac{x\sin 2x}{2}$ forgets the $2a = 4$. $\frac{xe^{x}\cos 2x}{4}$ uses the $\sin$ rule pattern with the wrong function and sign.""")

T.single(3, ["d-operator-advanced"], r"A particular integral of $(D^2 + 1)y = x\sin x$ is",
         [r"$-\dfrac{x^2\cos x}{4} + \dfrac{x\sin x}{4}$", r"$-\dfrac{x^2\cos x}{4}$",
          r"$\dfrac{x^2\sin x}{4} + \dfrac{x\cos x}{4}$", r"$-\dfrac{x^2\cos x}{2} + \dfrac{x\sin x}{2}$"],
         r"""Write $x\sin x = \operatorname{Im}(xe^{ix})$ and shift:
$$\frac{1}{D^2 + 1}xe^{ix} = e^{ix}\frac{1}{2iD\left(1 + \frac{D}{2i}\right)}x = e^{ix}\frac{1}{2i}\left(\frac{x^2}{2} - \frac{x}{2i}\right) = e^{ix}\left(-\frac{ix^2}{4} + \frac{x}{4}\right).$$
The imaginary part is $-\frac{x^2\cos x}{4} + \frac{x\sin x}{4}$.
$-\frac{x^2\cos x}{4}$ alone drops the correction term from $\left(1 + \frac{D}{2i}\right)^{-1}$. Since $x\sin x$ is not in the CF, it cannot be omitted. Check by substitution: $(D^2 + 1)\left(-\frac{x^2\cos x}{4}\right) = x\sin x - \frac{\cos x}{2}$, and $(D^2 + 1)\frac{x\sin x}{4} = \frac{\cos x}{2}$.""")

T.single(3, ["variation-of-parameters"], r"By variation of parameters, a particular integral of $y'' + y = \sec x$ on $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$ is",
         [r"$x\sin x + \cos x\,\ln(\cos x)$", r"$x\sin x - \cos x\,\ln(\cos x)$",
          r"$x\cos x + \sin x\,\ln(\cos x)$", r"$-x\sin x + \cos x\,\ln(\cos x)$"],
         r"""$y_1 = \cos x$, $y_2 = \sin x$, $W = 1$, $R = \sec x$:
$$u_1' = -\frac{y_2R}{W} = -\tan x \Rightarrow u_1 = \ln(\cos x), \qquad u_2' = \frac{y_1R}{W} = 1 \Rightarrow u_2 = x.$$
$$y_p = \cos x\,\ln(\cos x) + x\sin x.$$
$x\sin x - \cos x\ln\cos x$ integrates $-\tan x$ as $-\ln\cos x$ (sign slip). $x\cos x + \sin x\ln\cos x$ attaches $u_1, u_2$ to the wrong functions.""")

T.single(3, ["cauchy-euler"], r"For $x > 0$, the general solution of $x^2y'' - xy' + y = \ln x$ is",
         [r"$y = (c_1 + c_2\ln x)x + \ln x + 2$", r"$y = (c_1 + c_2\ln x)x + \ln x - 2$",
          r"$y = (c_1 + c_2\ln x)x + \ln x$", r"$y = c_1x + c_2x^{-1} + \ln x + 2$"],
         r"""Put $x = e^{z}$: $\theta(\theta - 1) - \theta + 1 = (\theta - 1)^2$, so $(\theta - 1)^2y = z$.
- CF: double root $1$, so $(c_1 + c_2z)e^{z} = (c_1 + c_2\ln x)x$.
- PI: $(1 - \theta)^{-2}z = (1 + 2\theta + 3\theta^2 + \cdots)z = z + 2$.

So $y = (c_1 + c_2\ln x)x + \ln x + 2$. $\ln x - 2$ is the sign slip; $\ln x$ alone drops the $2\theta z$ term. Check: $y = \ln x + 2$ gives $-1 - 1 + \ln x + 2 = \ln x$.""")

T.single(3, ["cauchy-euler"], r"For $x > -1$, the general solution of $(1 + x)^2y'' + (1 + x)y' + y = 0$ is",
         [r"$y = c_1\cos\ln(1 + x) + c_2\sin\ln(1 + x)$", r"$y = c_1\cos(\ln x) + c_2\sin(\ln x)$",
          r"$y = c_1(1 + x) + c_2(1 + x)^{-1}$", r"$y = \left[c_1 + c_2\ln(1 + x)\right](1 + x)$"],
         r"""This is Legendre's linear equation. Put $1 + x = e^{z}$, so $(1 + x)D = \theta$ and $(1 + x)^2D^2 = \theta(\theta - 1)$:
$$\theta(\theta - 1) + \theta + 1 = \theta^2 + 1 \;\Rightarrow\; y = c_1\cos z + c_2\sin z, \quad z = \ln(1 + x).$$
$\cos(\ln x)$ substitutes $x = e^{z}$ instead of $1 + x = e^{z}$. $(1 + x)^{\pm1}$ solves the equation with $-y$ in place of $+y$.""")

T.single(3, ["constant-coefficients"], r"The general solution of $y''' - y = 0$ is",
         [r"$c_1e^{x} + e^{-x/2}\left(c_2\cos\frac{\sqrt3}{2}x + c_3\sin\frac{\sqrt3}{2}x\right)$",
          r"$c_1e^{-x} + e^{x/2}\left(c_2\cos\frac{\sqrt3}{2}x + c_3\sin\frac{\sqrt3}{2}x\right)$",
          r"$c_1e^{x} + e^{x/2}\left(c_2\cos\frac{\sqrt3}{2}x + c_3\sin\frac{\sqrt3}{2}x\right)$",
          r"$c_1e^{x} + c_2e^{-x} + c_3\cos x$"],
         r"""$m^3 - 1 = (m - 1)(m^2 + m + 1) = 0$, so $m = 1$ and $m = -\frac12 \pm \frac{\sqrt3}{2}i$. Hence
$$y = c_1e^{x} + e^{-x/2}\left(c_2\cos\tfrac{\sqrt3}{2}x + c_3\sin\tfrac{\sqrt3}{2}x\right).$$
The $e^{-x}, e^{x/2}$ option solves $y''' + y = 0$. The $e^{x}, e^{x/2}$ option takes the wrong sign of $\alpha$. Check: the three roots must sum to $0$ (no $m^2$ term): $1 - \frac12 - \frac12 = 0$.""")

# ---------------------------------------------------------------- statements
T.statements(1, ["linear-theory", "constant-coefficients"], r"Consider the following statements:",
             [r"$e^{x}$ and $xe^{x}$ are linearly independent solutions of $y'' - 2y' + y = 0$.",
              r"The only solution of $y'' + y = 0$ with $y(0) = 0$ and $y'(0) = 0$ is $y \equiv 0$.",
              r"Every solution of $y'' + 3y' + 2y = 0$ tends to $0$ as $x \to \infty$."],
             [r"1, 2 and 3", r"1 and 2 only", r"1 and 3 only", r"2 and 3 only"],
             r"""- **1 is true:** $m = 1$ is a double root, so $e^{x}$ and $xe^{x}$ are solutions, and $W(e^{x}, xe^{x}) = e^{2x} \ne 0$.
- **2 is true:** $y \equiv 0$ is a solution, and the existence and uniqueness theorem allows only one solution of an initial value problem.
- **3 is true:** the roots are $-1, -2$, so $y = c_1e^{-x} + c_2e^{-2x} \to 0$.

Do not confuse 2 with the **boundary** problem $y(0) = y(\pi) = 0$, which has the solutions $c\sin x$.""")

T.statements(2, ["wronskian"], r"Let $I$ be an open interval. Consider the following statements:",
             [r"If differentiable functions $y_1, y_2$ have $W(y_1, y_2)(x_0) \ne 0$ at some $x_0 \in I$, then $y_1, y_2$ are linearly independent on $I$.",
              r"If $W(y_1, y_2) \equiv 0$ on $I$ for differentiable $y_1, y_2$, then $y_1, y_2$ are linearly dependent on $I$.",
              r"If $y_1, y_2$ are solutions of $y'' + P(x)y' + Q(x)y = 0$ with $P, Q$ continuous on $I$, then $W(y_1, y_2)$ is either identically zero on $I$ or never zero on $I$."],
             [r"1 and 3 only", r"1 only", r"2 and 3 only", r"1, 2 and 3"],
             r"""- **1 is true:** if $c_1y_1 + c_2y_2 \equiv 0$, differentiating gives $c_1y_1' + c_2y_2' \equiv 0$. At $x_0$ this $2 \times 2$ system has determinant $W(x_0) \ne 0$, so $c_1 = c_2 = 0$.
- **2 is false:** $y_1 = x^2$ and $y_2 = x\lvert x\rvert$ on $(-1, 1)$ have $W \equiv 0$ but are independent.
- **3 is true:** by Abel's formula, $W(x) = W(x_0)e^{-\int_{x_0}^{x}P}$.

Statement 2 does hold when $y_1, y_2$ are solutions of such an equation, which is why it is tempting.""")

T.statements(2, ["d-operator"], r"Here $D = \frac{d}{dx}$ and $f$ is a polynomial with constant coefficients. Consider the following statements:",
             [r"$\dfrac{1}{D - a}X = e^{ax}\displaystyle\int e^{-ax}X\,dx$.",
              r"If $\phi(-a^2) \ne 0$, then $\dfrac{1}{\phi(D^2)}\sin ax = \dfrac{\sin ax}{\phi(-a^2)}$.",
              r"$\dfrac{1}{f(D)}e^{ax} = \dfrac{e^{ax}}{f(a)}$ holds whether or not $f(a) = 0$, after cancelling common factors."],
             [r"1 and 2 only", r"2 only", r"1 and 3 only", r"1, 2 and 3"],
             r"""- **1 is true:** $(D - a)y = X$ is first-order linear with integrating factor $e^{-ax}$: $(ye^{-ax})' = Xe^{-ax}$.
- **2 is true:** $D^2\sin ax = -a^2\sin ax$, so $\phi(D^2)\sin ax = \phi(-a^2)\sin ax$. Divide by $\phi(-a^2) \ne 0$.
- **3 is false:** if $f(a) = 0$, the formula divides by zero. For example, $(D - 1)y = e^{x}$ has PI $xe^{x}$, not $\frac{e^{x}}{0}$. The correct rule is $\frac{xe^{ax}}{f'(a)}$ when $a$ is a simple root.""")

# ---------------------------------------------------------------- match
T.match(1, ["constant-coefficients"], r"Match each equation in List I with its general solution in List II.",
        [r"$y'' - 4y = 0$", r"$y'' + 4y = 0$", r"$y'' - 4y' + 4y = 0$", r"$y'' - 4y' + 8y = 0$"],
        [r"$e^{2x}(c_1\cos 2x + c_2\sin 2x)$", r"$c_1e^{2x} + c_2e^{-2x}$", r"$c_1\cos 2x + c_2\sin 2x$", r"$(c_1 + c_2x)e^{2x}$"],
        [r"A-2, B-3, C-4, D-1", r"A-3, B-2, C-4, D-1", r"A-2, B-3, C-1, D-4", r"A-2, B-4, C-3, D-1"],
        r"""- A: $m^2 = 4$, $m = \pm 2$: **2**.
- B: $m^2 = -4$, $m = \pm 2i$: **3**.
- C: $(m - 2)^2 = 0$, double root $2$: **4**.
- D: $m = \frac{4 \pm \sqrt{16 - 32}}{2} = 2 \pm 2i$: **1**.

Matching C with 1 confuses a double root with a complex pair.""")

T.match(2, ["d-operator", "d-operator-advanced"], r"Match each expression in List I with a particular integral in List II ($D = \frac{d}{dx}$).",
        [r"$\dfrac{1}{D^2 + 1}e^{2x}$", r"$\dfrac{1}{D^2 + 1}\sin 2x$", r"$\dfrac{1}{D^2 + 1}x^2$", r"$\dfrac{1}{D^2 + 1}\cos x$"],
        [r"$\dfrac{x\sin x}{2}$", r"$x^2 - 2$", r"$\dfrac{e^{2x}}{5}$", r"$-\dfrac{\sin 2x}{3}$"],
        [r"A-3, B-4, C-2, D-1", r"A-3, B-1, C-2, D-4", r"A-4, B-3, C-2, D-1", r"A-3, B-4, C-1, D-2"],
        r"""- A: $\frac{e^{2x}}{4 + 1}$: **3**.
- B: $D^2 \to -4$: $\frac{\sin 2x}{-4 + 1} = -\frac{\sin 2x}{3}$: **4**.
- C: $(1 + D^2)^{-1}x^2 = (1 - D^2 + \cdots)x^2 = x^2 - 2$: **2**.
- D: resonance, $\frac{x\sin ax}{2a}$ with $a = 1$: **1**.

Check C: $(x^2 - 2)'' + (x^2 - 2) = 2 + x^2 - 2 = x^2$.""")

# ---------------------------------------------------------------- assertion-reason
T.assertion_reason(2, ["d-operator", "exam-tips"],
                   r"A particular integral of $(D^2 + 9)y = \cos 3x$ cannot be of the form $a\cos 3x + b\sin 3x$ with constants $a, b$; it must contain a factor $x$.",
                   r"$\cos 3x$ and $\sin 3x$ are solutions of the homogeneous equation $(D^2 + 9)y = 0$.",
                   0,
                   r"""**R is true:** the auxiliary roots are $\pm 3i$.

**A is true, and R explains it:** by R, $(D^2 + 9)(a\cos 3x + b\sin 3x) = 0 \ne \cos 3x$ for every $a, b$. So the PI must be different: $\frac{x\sin 3x}{6}$, with a factor $x$. This is resonance: the forcing term lies in the CF.""")

T.assertion_reason(3, ["wronskian"],
                   r"$x^2$ and $x\lvert x\rvert$ are linearly independent on $(-1, 1)$.",
                   r"The Wronskian of $x^2$ and $x\lvert x\rvert$ is not identically zero on $(-1, 1)$.",
                   2,
                   r"""**A is true:** if $c_1x^2 + c_2x\lvert x\rvert \equiv 0$, then $x = \frac12$ gives $c_1 + c_2 = 0$ and $x = -\frac12$ gives $c_1 - c_2 = 0$, so $c_1 = c_2 = 0$.

**R is false:** for $x \ge 0$ the functions are $x^2, x^2$; for $x < 0$ they are $x^2, -x^2$. In both cases the columns of $W$ are proportional, so $W \equiv 0$ (and $x\lvert x\rvert$ is differentiable at $0$, with derivative $2\lvert x\rvert$).

So $W \equiv 0$ does not imply dependence for arbitrary functions. It does for solutions of a common equation $y'' + Py' + Qy = 0$ with continuous coefficients.""")

T.assertion_reason(3, ["cauchy-euler"],
                   r"Every equation $x^2y'' + axy' + by = 0$ ($a, b$ real constants) has a solution of the form $y = x^m$ on $x > 0$ with $m$ real.",
                   r"On $x > 0$, the substitution $x = e^{z}$ turns $x^2y'' + axy' + by = 0$ into a linear equation with constant coefficients in $z$.",
                   3,
                   r"""**A is false:** $x^2y'' + xy' + y = 0$ has indicial equation $m^2 + 1 = 0$, with no real root. Its solutions are $c_1\cos(\ln x) + c_2\sin(\ln x)$, and no real power $x^m$ is among them.

**R is true:** $xD = \theta$ and $x^2D^2 = \theta(\theta - 1)$, so the equation becomes $\left[\theta^2 + (a - 1)\theta + b\right]y = 0$. Real powers $x^m$ come out only when this quadratic has real roots.""")

T.assertion_reason(2, ["constant-coefficients"],
                   r"The roots of the auxiliary equation of $y'' + 2y' + 5y = 0$ are $-1 \pm 2i$.",
                   r"Every solution of $y'' + 2y' + 5y = 0$ tends to $0$ as $x \to \infty$.",
                   1,
                   r"""**A is true:** $m = \frac{-2 \pm \sqrt{4 - 20}}{2} = -1 \pm 2i$.

**R is true:** $y = e^{-x}(c_1\cos 2x + c_2\sin 2x)$ and $\lvert y\rvert \le (\lvert c_1\rvert + \lvert c_2\rvert)e^{-x} \to 0$.

**But R does not explain A:** R is a consequence of A (negative real parts give decay), not a reason for it. The roots come from the quadratic formula alone.""")


def check():
    import sympy as sp
    x = sp.symbols("x", positive=True)
    X = sp.symbols("x", real=True)
    y = sp.Function("y")
    c1, c2, c3 = sp.symbols("c1 c2 c3")
    D = lambda e, n=1: sp.diff(e, x, n)

    def ne(a, b, label):
        if sp.simplify(sp.sympify(a) - sp.sympify(b)) == 0:
            sys.exit(f"DISTRACTOR EQUALS KEY {label}: {a} vs {b}")

    def solves(ode, sol, label):
        ok, res = sp.checkodesol(ode, sp.Eq(y(x), sol))
        if not ok:
            sys.exit(f"CHECK FAILED {label}: {sol} does not solve {ode} (residual {res})")

    def not_solves(ode, sol, label):
        ok, _ = sp.checkodesol(ode, sp.Eq(y(x), sol))
        if ok:
            sys.exit(f"DISTRACTOR SOLVES {label}: {sol}")

    def L(coeffs, u):   # constant-coefficient operator sum c_k D^k, coeffs from highest order
        n = len(coeffs) - 1
        return sp.simplify(sum(c * D(u, n - k) if n - k else c * u for k, c in enumerate(coeffs)))

    def dsolve_eq(ode, key, label):
        """dsolve the ODE and check the key is the same family (every key basis function solves,
        and dsolve's solution has the same number of constants)."""
        s = sp.dsolve(ode, y(x)).rhs
        solves(ode, key, label)
        n_key = len(key.free_symbols & {c1, c2, c3})
        n_ds = len([s_ for s_ in s.free_symbols if s_.name.startswith("C")])
        assert n_key == n_ds, f"{label}: constants {n_key} vs {n_ds}"
        return s

    # q1
    ode = y(x).diff(x, 2) - 5 * y(x).diff(x) + 6 * y(x)
    dsolve_eq(ode, c1 * sp.exp(2 * x) + c2 * sp.exp(3 * x), "q1")
    for d in [sp.exp(-2 * x), sp.exp(6 * x), sp.exp(-3 * x)]:
        not_solves(ode, d, "q1")
    # q2
    ode = y(x).diff(x, 2) + 4 * y(x)
    dsolve_eq(ode, c1 * sp.cos(2 * x) + c2 * sp.sin(2 * x), "q2")
    for d in [sp.exp(2 * x), x * sp.exp(2 * x), sp.cos(4 * x)]:
        not_solves(ode, d, "q2")
    # q3
    ode = y(x).diff(x, 2) - 6 * y(x).diff(x) + 9 * y(x)
    dsolve_eq(ode, (c1 + c2 * x) * sp.exp(3 * x), "q3")
    for d in [sp.exp(-3 * x), x * sp.exp(-3 * x), sp.cos(3 * x)]:
        not_solves(ode, d, "q3")
    # q4
    eq(sp.wronskian([sp.exp(2 * x), sp.exp(3 * x)], x), sp.exp(5 * x), "q4")
    # q5
    eq(L([1, 3, 2], sp.exp(3 * x) / 20), sp.exp(3 * x), "q5")
    for d in [sp.exp(3 * x) / 2, sp.exp(3 * x) / 14, sp.exp(3 * x) / 11]:
        ne(L([1, 3, 2], d), sp.exp(3 * x), "q5")
    # q6
    eq(L([1, 0, 4], sp.sin(x) / 3), sp.sin(x), "q6")
    for d in [-sp.sin(x) / 3, sp.sin(x) / 5, -sp.sin(x) / 5]:
        ne(L([1, 0, 4], d), sp.sin(x), "q6")
    # q7
    eq(L([1, 0, 4], x * sp.sin(2 * x) / 4), sp.cos(2 * x), "q7")
    for d in [x * sp.sin(2 * x) / 2, -x * sp.cos(2 * x) / 4, x * sp.cos(2 * x) / 4]:
        ne(L([1, 0, 4], d), sp.cos(2 * x), "q7")
    # q8
    eq(L([1, -3, 2], -x * sp.exp(x)), sp.exp(x), "q8")
    for d in [x * sp.exp(x), -x**2 * sp.exp(x) / 2, x * sp.exp(x) / 2]:
        ne(L([1, -3, 2], d), sp.exp(x), "q8")
    # q9
    eq(L([1, 0, -4], -x**2 / 4 - sp.Rational(1, 8)), x**2, "q9")
    for d in [-x**2 / 4 + sp.Rational(1, 8), x**2 / 4 + sp.Rational(1, 8), -x**2 / 4 - sp.Rational(1, 2)]:
        ne(L([1, 0, -4], d), x**2, "q9")
    # q10
    eq(L([1, -2, 1], x**3 * sp.exp(x) / 6), x * sp.exp(x), "q10")
    for d in [x**3 * sp.exp(x) / 3, x**2 * sp.exp(x) / 2, x**3 / 6]:
        ne(L([1, -2, 1], d), x * sp.exp(x), "q10")
    # q11: Abel; W of a fundamental set is a constant multiple of e^{-2x}
    ode = y(x).diff(x, 2) + 2 * y(x).diff(x) + 5 * y(x)
    y1, y2 = sp.exp(-x) * sp.cos(2 * x), sp.exp(-x) * sp.sin(2 * x)
    solves(ode, y1, "q11"); solves(ode, y2, "q11")
    W = sp.simplify(sp.wronskian([y1, y2], x))
    eq(W, 2 * sp.exp(-2 * x), "q11")
    eq(sp.Rational(3, 2) * W, 3 * sp.exp(-2 * x), "q11 key with W(0)=3")
    # q12
    ode = x**2 * y(x).diff(x, 2) - 2 * x * y(x).diff(x) + 2 * y(x)
    dsolve_eq(ode, c1 * x + c2 * x**2, "q12")
    for d in [1 / x, x**-2, x * sp.cos(sp.log(x)), x**3]:
        not_solves(ode, d, "q12")
    # q13
    ode = x**2 * y(x).diff(x, 2) + x * y(x).diff(x) + y(x)
    dsolve_eq(ode, c1 * sp.cos(sp.log(x)) + c2 * sp.sin(sp.log(x)), "q13")
    for d in [sp.cos(x), 1 / x, sp.log(x)]:
        not_solves(ode, d, "q13")
    # q14
    sol = c1 * sp.exp(x) * sp.cos(2 * x) + c2 * sp.exp(x) * sp.sin(2 * x)
    solves(y(x).diff(x, 2) - 2 * y(x).diff(x) + 5 * y(x), sol, "q14")
    for (a, b) in [(2, 5), (-2, 3), (-2, -3)]:
        not_solves(y(x).diff(x, 2) + a * y(x).diff(x) + b * y(x), sp.exp(x) * sp.cos(2 * x), "q14")
    # q15: IVP
    ode = sp.Eq(y(x).diff(x, 2) + 4 * y(x), 4)
    s = sp.dsolve(ode, y(x), ics={y(0): 0, y(x).diff(x).subs(x, 0): 0}).rhs
    eq(s, 1 - sp.cos(2 * x), "q15")
    for d in [1 + sp.cos(2 * x), (1 - sp.cos(2 * x)) / 4, 1 - sp.cos(2 * x) + sp.sin(2 * x)]:
        ne(d, s, "q15")
    # q16
    f = sp.exp(x) * sp.cos(2 * x)
    eq(L([1, -2, 5], x * sp.exp(x) * sp.sin(2 * x) / 4), f, "q16")
    for d in [x * sp.exp(x) * sp.sin(2 * x) / 2, -x * sp.exp(x) * sp.sin(2 * x) / 4, x * sp.exp(x) * sp.cos(2 * x) / 4]:
        ne(L([1, -2, 5], d), f, "q16")
    s = sp.dsolve(sp.Eq(y(x).diff(x, 2) - 2 * y(x).diff(x) + 5 * y(x), f), y(x)).rhs
    solves(sp.Eq(y(x).diff(x, 2) - 2 * y(x).diff(x) + 5 * y(x), f), s, "q16 dsolve")
    # q17
    f = x * sp.sin(x)
    eq(L([1, 0, 1], -x**2 * sp.cos(x) / 4 + x * sp.sin(x) / 4), f, "q17")
    for d in [-x**2 * sp.cos(x) / 4, x**2 * sp.sin(x) / 4 + x * sp.cos(x) / 4, -x**2 * sp.cos(x) / 2 + x * sp.sin(x) / 2]:
        ne(L([1, 0, 1], d), f, "q17")
    # q18: variation of parameters (check by substitution on (-pi/2, pi/2), cos x > 0)
    t = sp.symbols("t", real=True)
    yp = t * sp.sin(t) + sp.cos(t) * sp.log(sp.cos(t))
    eq(sp.simplify(sp.diff(yp, t, 2) + yp - 1 / sp.cos(t)), 0, "q18")
    u1 = sp.integrate(-sp.tan(t), t); eq(sp.diff(u1 - sp.log(sp.cos(t)), t), 0, "q18 u1")
    for d in [t * sp.sin(t) - sp.cos(t) * sp.log(sp.cos(t)), t * sp.cos(t) + sp.sin(t) * sp.log(sp.cos(t)),
              -t * sp.sin(t) + sp.cos(t) * sp.log(sp.cos(t))]:
        r = sp.diff(d, t, 2) + d - 1 / sp.cos(t)
        assert abs(sp.N(r.subs(t, sp.Rational(1, 3)))) > 1e-6, "q18 distractor"
    # q19
    ode = sp.Eq(x**2 * y(x).diff(x, 2) - x * y(x).diff(x) + y(x), sp.log(x))
    dsolve_eq(ode, (c1 + c2 * sp.log(x)) * x + sp.log(x) + 2, "q19")
    for d in [(c1 + c2 * sp.log(x)) * x + sp.log(x) - 2, (c1 + c2 * sp.log(x)) * x + sp.log(x),
              c1 * x + c2 / x + sp.log(x) + 2]:
        not_solves(ode, d, "q19")
    # q20: Legendre
    ode = (1 + x)**2 * y(x).diff(x, 2) + (1 + x) * y(x).diff(x) + y(x)
    solves(ode, c1 * sp.cos(sp.log(1 + x)) + c2 * sp.sin(sp.log(1 + x)), "q20")
    # dsolve in the shifted variable s = 1 + x (a Cauchy-Euler equation): two constants
    sv = sp.symbols("s", positive=True); w = sp.Function("w")
    ds = sp.dsolve(sv**2 * w(sv).diff(sv, 2) + sv * w(sv).diff(sv) + w(sv), w(sv)).rhs
    eq(ds.subs({sp.Symbol("C1"): 1, sp.Symbol("C2"): 0}).subs(sv, 1 + x)**2
       + ds.subs({sp.Symbol("C1"): 0, sp.Symbol("C2"): 1}).subs(sv, 1 + x)**2, 1, "q20 dsolve basis cos/sin ln(1+x)")
    for d in [sp.cos(sp.log(x)), 1 + x, 1 / (1 + x), sp.log(1 + x) * (1 + x)]:
        not_solves(ode, d, "q20")
    # q21
    ode = y(x).diff(x, 3) - y(x)
    k = sp.sqrt(3) / 2
    dsolve_eq(ode, c1 * sp.exp(x) + sp.exp(-x / 2) * (c2 * sp.cos(k * x) + c3 * sp.sin(k * x)), "q21")
    for d in [sp.exp(-x), sp.exp(x / 2) * sp.cos(k * x), sp.exp(-x) + sp.cos(x)]:
        not_solves(ode, d, "q21")
    # q22 statements (all true)
    ode = y(x).diff(x, 2) - 2 * y(x).diff(x) + y(x)
    solves(ode, sp.exp(x), "q22.1"); solves(ode, x * sp.exp(x), "q22.1")
    eq(sp.wronskian([sp.exp(x), x * sp.exp(x)], x), sp.exp(2 * x), "q22.1")
    s = sp.dsolve(y(x).diff(x, 2) + y(x), y(x), ics={y(0): 0, y(x).diff(x).subs(x, 0): 0}).rhs
    eq(s, 0, "q22.2")
    s = sp.dsolve(y(x).diff(x, 2) + 3 * y(x).diff(x) + 2 * y(x), y(x)).rhs
    assert sp.limit(s, x, sp.oo) == 0, "q22.3"
    # BVP counterpart has nonzero solutions
    eq(sp.sin(X).subs(X, sp.pi), 0, "q22 bvp")
    # q23 Wronskian statements
    eq(sp.wronskian([sp.exp(x), sp.exp(2 * x)], x).subs(x, 0), 1, "q23.1 example")
    for xv in [sp.Rational(1, 2), sp.Rational(-1, 2)]:   # W(x^2, x|x|) = 0 on both sides
        w = sp.wronskian([X**2, X * sp.Abs(X)], X).subs(X, xv)
        eq(w, 0, "q23.2")
    M = sp.Matrix([[sp.Rational(1, 4), sp.Rational(1, 4)], [sp.Rational(1, 4), -sp.Rational(1, 4)]])
    assert M.det() != 0, "q23.2 independence"
    P = sp.Function("P")
    eq(sp.diff(sp.exp(-sp.integrate(2, (t, 0, x))), x) + 2 * sp.exp(-2 * x), 0, "q23.3 Abel W' = -PW")
    # q24 D-operator statements
    Xf = sp.sin(x) * x
    a = 3
    yp = sp.exp(a * x) * sp.integrate(sp.exp(-a * x) * Xf, x)
    eq(D(yp) - a * yp, Xf, "q24.1")
    eq(L([1, 0, 1], sp.sin(2 * x) / (1 - 4)), sp.sin(2 * x), "q24.2")
    eq(L([1, -1], x * sp.exp(x)), sp.exp(x), "q24.3 (D-1)y=e^x has PI x e^x")
    # q25 match constant coefficients
    pairs = {(0, -4): c1 * sp.exp(2 * x) + c2 * sp.exp(-2 * x), (0, 4): c1 * sp.cos(2 * x) + c2 * sp.sin(2 * x),
             (-4, 4): (c1 + c2 * x) * sp.exp(2 * x), (-4, 8): sp.exp(2 * x) * (c1 * sp.cos(2 * x) + c2 * sp.sin(2 * x))}
    for (p, q), sol in pairs.items():
        dsolve_eq(y(x).diff(x, 2) + p * y(x).diff(x) + q * y(x), sol, f"q25 {p},{q}")
    not_solves(y(x).diff(x, 2) - 4 * y(x).diff(x) + 4 * y(x), sp.exp(2 * x) * sp.cos(2 * x), "q25 C-1")
    # q26 match D-operator
    eq(L([1, 0, 1], sp.exp(2 * x) / 5), sp.exp(2 * x), "q26 A")
    eq(L([1, 0, 1], -sp.sin(2 * x) / 3), sp.sin(2 * x), "q26 B")
    eq(L([1, 0, 1], x**2 - 2), x**2, "q26 C")
    eq(L([1, 0, 1], x * sp.sin(x) / 2), sp.cos(x), "q26 D")
    ne(L([1, 0, 1], x * sp.sin(x) / 2), sp.sin(2 * x), "q26")
    # q27 AR resonance
    aa, bb = sp.symbols("a b")
    eq(L([1, 0, 9], aa * sp.cos(3 * x) + bb * sp.sin(3 * x)), 0, "q27 R")
    eq(L([1, 0, 9], x * sp.sin(3 * x) / 6), sp.cos(3 * x), "q27 A")
    # q28 AR Wronskian (checked in q23)
    eq(sp.diff(X * sp.Abs(X), X).subs(X, sp.Rational(-1, 3)), sp.Rational(2, 3), "q28 derivative 2|x|")
    # q29 AR Cauchy-Euler: x^2y''+xy'+y has complex indicial roots, no real x^m
    m = sp.symbols("m")
    assert all(not r.is_real for r in sp.solve(m * (m - 1) + m + 1, m)), "q29 A"
    z = sp.symbols("z")
    u = sp.Function("u")
    a_, b_ = 3, 2   # R: x^2 y'' + a x y' + b y with y = u(ln x) gives u'' + (a-1)u' + b u
    yy = u(sp.log(x))
    expr = sp.simplify(x**2 * sp.diff(yy, x, 2) + a_ * x * sp.diff(yy, x) + b_ * yy)
    expr = expr.subs(sp.log(x), z).subs(x, sp.exp(z))
    target = sp.diff(u(z), z, 2) + (a_ - 1) * sp.diff(u(z), z) + b_ * u(z)
    eq(sp.simplify(expr.doit() - target), 0, "q29 R")
    # q30 AR roots and decay
    assert set(sp.solve(m**2 + 2 * m + 5, m)) == {-1 + 2 * sp.I, -1 - 2 * sp.I}, "q30 A"
    s = sp.dsolve(y(x).diff(x, 2) + 2 * y(x).diff(x) + 5 * y(x), y(x)).rhs
    assert sp.limit(s, x, sp.oo) == 0, "q30 R"


T.write(check)
