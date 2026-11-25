import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from qlib import Topic, eq

T = Topic("math.ode.ode-first-order")

# ---------------------------------------------------------------- order, degree, formation
# q1
T.single(1, ["order-degree"],
    r"The order and degree of $\left[1 + \left(\frac{dy}{dx}\right)^2\right]^{3/2} = \frac{d^2y}{dx^2}$ are respectively",
    [r"$2$ and $2$", r"$2$ and $1$", r"$2$ and $\frac{3}{2}$", r"$1$ and $3$"],
    r"""The highest derivative is $y''$, so the order is $2$. Make the equation polynomial in the derivatives by squaring:
$$\left(1 + y'^2\right)^3 = \left(y''\right)^2.$$
The highest-order derivative $y''$ now appears to the power $2$, so the degree is $2$.

Reading the degree before removing the radical gives $1$; $\frac32$ is not a degree at all (degree is a positive integer); $3$ is the power of $(1 + y'^2)$, which involves the lower derivative $y'$.""")

# q2
T.single(1, ["order-degree"],
    r"For the equation $\frac{d^2y}{dx^2} + \sin\left(\frac{dy}{dx}\right) = 0$,",
    [r"the order is $2$ and the degree is not defined", r"the order is $2$ and the degree is $1$", r"the order is $1$ and the degree is $1$", r"the order is $2$ and the degree is $2$"],
    r"""The order is $2$ (highest derivative $y''$). The degree is defined only when the equation can be written as a polynomial in **all** the derivatives. Here $y'$ sits inside $\sin$, and $\sin y'$ is not a polynomial in $y'$, so the degree is **not defined**.

Answering "degree $1$" looks only at $y''$ and ignores the requirement that the whole equation be polynomial in the derivatives.""")

# q3
T.single(1, ["order-degree"],
    r"Which of the following differential equations is linear?",
    [r"$\frac{d^2y}{dx^2} + x^2y = \sin x$", r"$y\frac{d^2y}{dx^2} + \frac{dy}{dx} = 0$", r"$\frac{d^2y}{dx^2} + \sin y = 0$", r"$\left(\frac{dy}{dx}\right)^2 + y = x$"],
    r"""An ODE is linear when $y$ and its derivatives appear only to the first power, are not multiplied together, and have coefficients depending on $x$ alone.

$y'' + x^2y = \sin x$ qualifies: the coefficient $x^2$ and the right side $\sin x$ involve only $x$.

The others fail: $yy''$ is a product of $y$ and $y''$; $\sin y$ is not first-degree in $y$; $(y')^2$ is a square.""")

# q4
T.single(1, ["formation"],
    r"The differential equation of the family $y = Ae^{2x} + Be^{-2x}$ ($A$, $B$ arbitrary constants) is",
    [r"$\frac{d^2y}{dx^2} - 4y = 0$", r"$\frac{d^2y}{dx^2} + 4y = 0$", r"$\frac{d^2y}{dx^2} - 2y = 0$", r"$\frac{d^2y}{dx^2} - 4\frac{dy}{dx} = 0$"],
    r"""Two constants, so differentiate twice:
$$y' = 2Ae^{2x} - 2Be^{-2x}, \qquad y'' = 4Ae^{2x} + 4Be^{-2x} = 4y.$$
So $y'' - 4y = 0$.

$y'' + 4y = 0$ has solutions $\cos 2x$, $\sin 2x$, not exponentials. $y'' - 2y = 0$ forgets that each differentiation brings a factor $2$. **Check:** $e^{2x}$ in $y'' - 4y'$ gives $4e^{2x} - 8e^{2x} \ne 0$.""")

# q5
T.single(2, ["formation"],
    r"The differential equation of all circles passing through the origin and having their centres on the $x$-axis is",
    [r"$2xy\frac{dy}{dx} = y^2 - x^2$", r"$2xy\frac{dy}{dx} = x^2 - y^2$", r"$xy\frac{dy}{dx} = y^2 - x^2$", r"$2xy\frac{dy}{dx} = x^2 + y^2$"],
    r"""The family is $x^2 + y^2 = 2ax$ (one constant). Differentiate: $2x + 2yy' = 2a$, so $a = x + yy'$. Substitute back:
$$x^2 + y^2 = 2x(x + yy') \;\Rightarrow\; 2xy\,y' = y^2 - x^2.$$

**Check:** the circle $x^2 + y^2 = 2x$ has a horizontal tangent at $(1, 1)$, so $y' = 0$ there, and indeed $y^2 - x^2 = 0$ at $(1, 1)$. The option $x^2 - y^2$ is the sign slip from moving $2x^2$ to the wrong side; $x^2 + y^2$ fails the same check, since it would need $y' = 1$ at $(1, 1)$. The option without the factor $2$ drops the $2$ from $2x(x + yy')$.""")

# ---------------------------------------------------------------- existence
# q6
T.single(3, ["existence"],
    r"The largest open interval containing $x = 0$ on which the solution of $\frac{dy}{dx} = y^2$, $y(0) = 1$, exists is",
    [r"$(-\infty, 1)$", r"$(-\infty, \infty)$", r"$(-1, 1)$", r"$(1, \infty)$"],
    r"""Separate: $\frac{dy}{y^2} = dx$, so $-\frac1y = x + C$. At $x = 0$, $y = 1$: $C = -1$. Hence
$$y = \frac{1}{1 - x}.$$
This is continuous on $(-\infty, 1)$ and blows up as $x \to 1^-$, so the maximal interval through $0$ is $(-\infty, 1)$.

$f(x, y) = y^2$ is smooth everywhere, but Picard's theorem is only **local**; smoothness of $f$ does not give a solution on all of $\R$. $(1, \infty)$ is the other branch, which does not contain $0$; nothing stops the solution at $x = -1$.""")

# ---------------------------------------------------------------- separable
# q7
T.single(1, ["separable"],
    r"The general solution of $\frac{dy}{dx} = \frac{1 + y^2}{1 + x^2}$ is",
    [r"$\tan^{-1}y = \tan^{-1}x + C$", r"$\tan^{-1}y + \tan^{-1}x = C$", r"$\ln(1 + y^2) = \ln(1 + x^2) + C$", r"$y = x + C$"],
    r"""Separate the variables:
$$\int\frac{dy}{1 + y^2} = \int\frac{dx}{1 + x^2} \;\Rightarrow\; \tan^{-1}y = \tan^{-1}x + C.$$
Equivalently $\frac{y - x}{1 + xy} = k$.

The "$+$" option comes from putting both terms on one side without changing a sign. The logarithm option integrates $\frac{2y}{1 + y^2}$, not $\frac{1}{1 + y^2}$. **Check** $y = x + C$: its slope is $1$, but $\frac{1 + y^2}{1 + x^2} \ne 1$ unless $C = 0$.""")

# q8
T.single(2, ["separable"],
    r"The solution of $\frac{dy}{dx} = e^{x + y}$ with $y(0) = 0$ is",
    [r"$y = -\ln(2 - e^x)$", r"$y = \ln(2 - e^x)$", r"$y = -\ln(2 - e^{-x})$", r"$y = x$"],
    r"""$e^{-y}\,dy = e^x\,dx$, so $-e^{-y} = e^x + C$. At $(0, 0)$: $-1 = 1 + C$, $C = -2$. Then
$$e^{-y} = 2 - e^x \;\Rightarrow\; y = -\ln(2 - e^x) \qquad (x < \ln 2).$$

**Check:** $y' = \frac{e^x}{2 - e^x}$ and $e^{x + y} = \frac{e^x}{2 - e^x}$. The option without the minus sign has slope $-1$ at $0$, but the equation needs $y'(0) = e^0 = 1$. $y = x$ has slope $1$ everywhere, while $e^{2x}$ is not $1$.""")

# q9
T.single(2, ["separable"],
    r"The general solution of $\frac{dy}{dx} = (x + y + 1)^2$ is",
    [r"$\tan^{-1}(x + y + 1) = x + C$", r"$\tan^{-1}(x + y + 1) = y + C$", r"$x + y + 1 = \tan x + C$", r"$-\frac{1}{x + y + 1} = x + C$"],
    r"""Put $v = x + y + 1$. Then $\frac{dv}{dx} = 1 + \frac{dy}{dx} = 1 + v^2$, which is separable:
$$\int\frac{dv}{1 + v^2} = \int dx \;\Rightarrow\; \tan^{-1}(x + y + 1) = x + C,$$
i.e. $y = \tan(x + C) - x - 1$.

$-\frac1v = x + C$ forgets the $1$ in $v' = 1 + y'$. $v = \tan x + C$ puts the constant in the wrong place: $\tan^{-1}v = x + C$ gives $v = \tan(x + C)$.""")

# ---------------------------------------------------------------- homogeneous
# q10
T.single(2, ["homogeneous"],
    r"The general solution of $(x^2 + y^2)\,dx - 2xy\,dy = 0$ is",
    [r"$x^2 - y^2 = Cx$", r"$x^2 + y^2 = Cx$", r"$x^2 - y^2 = Cy$", r"$x^2 - y^2 = Cx^2$"],
    r"""Homogeneous of degree $2$. Put $y = vx$:
$$v + xv' = \frac{1 + v^2}{2v} \;\Rightarrow\; xv' = \frac{1 - v^2}{2v} \;\Rightarrow\; \int\frac{2v\,dv}{1 - v^2} = \ln\lvert x\rvert + c.$$
So $-\ln\lvert 1 - v^2\rvert = \ln\lvert x\rvert + c$, i.e. $x(1 - v^2) = C$, i.e. $x^2 - y^2 = Cx$.

**Check** with $u = \frac{x^2 - y^2}{x}$: the slope $-\frac{u_x}{u_y} = \frac{x^2 + y^2}{2xy}$, as required. $x^2 + y^2 = Cx$ (circles) solves $2xyy' = y^2 - x^2$ instead; $x^2 - y^2 = Cx^2$ is just a pair of lines $y = \pm kx$.""")

# q11
T.single(2, ["homogeneous"],
    r"The general solution of $\frac{dy}{dx} = \frac{y}{x} + \tan\frac{y}{x}$ is",
    [r"$\sin\frac{y}{x} = Cx$", r"$\cos\frac{y}{x} = Cx$", r"$\tan\frac{y}{x} = Cx$", r"$\sin\frac{y}{x} = \frac{C}{x}$"],
    r"""Put $y = vx$: $v + xv' = v + \tan v$, so
$$\int\cot v\,dv = \int\frac{dx}{x} \;\Rightarrow\; \ln\lvert\sin v\rvert = \ln\lvert x\rvert + c \;\Rightarrow\; \sin\frac{y}{x} = Cx.$$

$\int\cot v\,dv = \ln\lvert\sin v\rvert$, not $\ln\lvert\cos v\rvert$ (that would be $-\int\tan v\,dv$). $\frac{C}{x}$ comes from a sign slip in $\ln\lvert x\rvert$.""")

# q12
T.single(3, ["homogeneous"],
    r"The general solution of $\frac{dy}{dx} = \frac{x + y + 1}{2x + 2y + 3}$ is",
    [r"$6y - 3x + \ln\lvert 3x + 3y + 4\rvert = C$", r"$6y - 3x - \ln\lvert 3x + 3y + 4\rvert = C$", r"$6y + 3x + \ln\lvert 3x + 3y + 4\rvert = C$", r"$3y - 6x + \ln\lvert 3x + 3y + 4\rvert = C$"],
    r"""Here $a_1b_2 - a_2b_1 = 1\cdot 2 - 2\cdot 1 = 0$: the lines are parallel, so no shift of origin works. Put $z = x + y$:
$$\frac{dz}{dx} = 1 + \frac{z + 1}{2z + 3} = \frac{3z + 4}{2z + 3}.$$
Since $2z + 3 = \frac23(3z + 4) + \frac13$,
$$\int\left(\frac23 + \frac{1}{3(3z + 4)}\right)dz = x + c \;\Rightarrow\; \frac23 z + \frac19\ln\lvert 3z + 4\rvert = x + c.$$
Multiply by $9$: $6(x + y) + \ln\lvert 3z + 4\rvert = 9x + C$, i.e. $6y - 3x + \ln\lvert 3x + 3y + 4\rvert = C$.

**Check:** differentiating the key gives $6y' - 3 + \frac{3 + 3y'}{3x + 3y + 4} = 0$, which rearranges to the given equation. The other sign choices fail this test.""")

# ---------------------------------------------------------------- exact
# q13
T.single(2, ["exact"],
    r"The equation $(3x^2 + kxy^2)\,dx + (2x^2y + 4y^3)\,dy = 0$ is exact when $k$ equals",
    [r"$2$", r"$4$", r"$1$", r"$-2$"],
    r"""Exactness needs $\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}$:
$$\frac{\partial}{\partial y}(3x^2 + kxy^2) = 2kxy, \qquad \frac{\partial}{\partial x}(2x^2y + 4y^3) = 4xy.$$
So $2k = 4$, $k = 2$. Then the solution is $x^3 + x^2y^2 + y^4 = C$.

$k = 4$ equates $kxy^2$ with $4xy$ without differentiating $y^2$.""")

# q14
T.single(2, ["exact"],
    r"The general solution of $(2xy + e^x)\,dx + (x^2 + \cos y)\,dy = 0$ is",
    [r"$x^2y + e^x + \sin y = C$", r"$2x^2y + e^x + \sin y = C$", r"$x^2y + e^x - \sin y = C$", r"$x^2y - e^x + \sin y = C$"],
    r"""$M_y = 2x = N_x$, so the equation is exact. Integrate $M$ with $y$ held constant: $x^2y + e^x$. The term of $N$ that does not contain $x$ is $\cos y$, which integrates to $\sin y$:
$$x^2y + e^x + \sin y = C.$$

$2x^2y$ comes from integrating the $x^2$ of $N$ a second time; that term is already accounted for in $x^2y$. **Check:** $\frac{\partial}{\partial y}(x^2y + e^x + \sin y) = x^2 + \cos y = N$.""")

# q15
T.single(2, ["exact"],
    r"The solution of $(ye^{xy} + 2x)\,dx + (xe^{xy} - 2y)\,dy = 0$ satisfying $y(0) = 1$ is",
    [r"$e^{xy} + x^2 - y^2 = 0$", r"$e^{xy} + x^2 - y^2 = 1$", r"$e^{xy} - x^2 - y^2 = 0$", r"$e^{xy} + x^2 + y^2 = 2$"],
    r"""$M_y = e^{xy} + xye^{xy} = N_x$, so it is exact, with
$$u = \int(ye^{xy} + 2x)\,dx + \int(-2y)\,dy = e^{xy} + x^2 - y^2.$$
At $(0, 1)$: $u = 1 + 0 - 1 = 0$, so $e^{xy} + x^2 - y^2 = 0$.

The "$= 1$" option forgets to evaluate $e^{xy}$ at the point; the other two pass through $(0, 1)$ but have the wrong signs, so their gradients are not $(M, N)$.""")

# ---------------------------------------------------------------- integrating factors
# q16
T.single(2, ["integrating-factors"],
    r"Which of the following is **not** an integrating factor of $y\,dx - x\,dy = 0$?",
    [r"$\frac{1}{xy^2}$", r"$\frac{1}{x^2}$", r"$\frac{1}{xy}$", r"$\frac{1}{x^2 + y^2}$"],
    r"""Three of them are standard:
$$\frac{y\,dx - x\,dy}{x^2} = -d\left(\frac{y}{x}\right), \quad \frac{y\,dx - x\,dy}{xy} = d\left(\ln\left\lvert\frac{x}{y}\right\rvert\right), \quad \frac{y\,dx - x\,dy}{x^2 + y^2} = -d\left(\tan^{-1}\frac{y}{x}\right).$$

For $\frac{1}{xy^2}$: $M = \frac{1}{xy}$, $N = -\frac{1}{y^2}$, so $M_y = -\frac{1}{xy^2}$ while $N_x = 0$. Not exact.

**Reason:** all IFs are $\mu\,g(u)$ with $\mu = \frac{1}{x^2}$, $u = \frac{y}{x}$, i.e. $\frac{1}{x^2}g\!\left(\frac{y}{x}\right)$, which are homogeneous of degree $-2$. $\frac{1}{xy^2}$ has degree $-3$.""")

# q17
T.single(2, ["integrating-factors"],
    r"An integrating factor of $\left(xy^2 - e^{1/x^3}\right)dx - x^2y\,dy = 0$ is",
    [r"$\frac{1}{x^4}$", r"$x^4$", r"$\frac{1}{x^2}$", r"$\frac{1}{y^2}$"],
    r"""$M_y = 2xy$ and $N_x = -2xy$. Then
$$\frac{M_y - N_x}{N} = \frac{4xy}{-x^2y} = -\frac4x,$$
a function of $x$ alone, so the IF is $e^{\int -4/x\,dx} = x^{-4}$.

After multiplying: $\left(\frac{y^2}{x^3} - \frac{e^{1/x^3}}{x^4}\right)dx - \frac{y}{x^2}\,dy = 0$, which is exact. $x^4$ is the result of dropping the minus sign in $-\frac4x$.""")

# q18
T.single(3, ["integrating-factors"],
    r"The general solution of $(x^2 + y^2 + x)\,dx + xy\,dy = 0$ is",
    [r"$3x^4 + 4x^3 + 6x^2y^2 = C$", r"$3x^4 + 4x^3 + 3x^2y^2 = C$", r"$x^3 + 3xy^2 + \frac{3}{2}x^2 = C$", r"$3x^4 - 4x^3 + 6x^2y^2 = C$"],
    r"""$\frac{M_y - N_x}{N} = \frac{2y - y}{xy} = \frac1x$, so the IF is $x$:
$$(x^3 + xy^2 + x^2)\,dx + x^2y\,dy = 0 \;\Rightarrow\; \frac{x^4}{4} + \frac{x^2y^2}{2} + \frac{x^3}{3} = c.$$
Multiply by $12$: $3x^4 + 6x^2y^2 + 4x^3 = C$.

The third option integrates the original (non-exact) $M$ directly. The option with $3x^2y^2$ loses the factor $2$ when clearing denominators.""")

# q19
T.single(3, ["integrating-factors"],
    r"An integrating factor of the homogeneous equation $y^2\,dx + (x^2 - xy - y^2)\,dy = 0$ is",
    [r"$\frac{1}{y(x^2 - y^2)}$", r"$\frac{1}{y(x^2 + y^2)}$", r"$\frac{1}{x(x^2 - y^2)}$", r"$\frac{1}{x^2y^2}$"],
    r"""$M$ and $N$ are homogeneous of degree $2$, so use $\frac{1}{Mx + Ny}$:
$$Mx + Ny = xy^2 + x^2y - xy^2 - y^3 = x^2y - y^3 = y(x^2 - y^2).$$
So the IF is $\frac{1}{y(x^2 - y^2)}$ (where $Mx + Ny \ne 0$).

The $x^2 + y^2$ option is a sign slip in $-y\cdot y^2$; the third option swaps the roles of $x$ and $y$.""")

# q20
T.single(3, ["integrating-factors"],
    r"An integrating factor of $y(xy + 2x^2y^2)\,dx + x(xy - x^2y^2)\,dy = 0$ is",
    [r"$\frac{1}{x^3y^3}$", r"$\frac{1}{x^2y^2}$", r"$x^3y^3$", r"$\frac{1}{xy}$"],
    r"""The equation has the form $y f_1(xy)\,dx + x f_2(xy)\,dy = 0$, so use $\frac{1}{Mx - Ny}$:
$$Mx - Ny = xy(xy + 2x^2y^2) - xy(xy - x^2y^2) = 3x^3y^3.$$
Hence $\frac{1}{3x^3y^3}$, or simply $\frac{1}{x^3y^3}$, is an IF. Multiplying gives
$$\left(\frac{1}{x^2y} + \frac{2}{x}\right)dx + \left(\frac{1}{xy^2} - \frac{1}{y}\right)dy = 0,$$
which is exact: both cross-derivatives equal $-\frac{1}{x^2y^2}$.

$\frac{1}{x^2y^2}$ cancels only the lowest terms and leaves a non-exact equation. The homogeneous rule does not apply here, because $M$ is not homogeneous.""")

# q21
T.single(3, ["integrating-factors"],
    r"An integrating factor of $(y^4 + 2y)\,dx + (xy^3 + 2y^4 - 4x)\,dy = 0$ is",
    [r"$\frac{1}{y^3}$", r"$y^3$", r"$\frac{1}{y^4}$", r"$e^{-3x}$"],
    r"""$M_y = 4y^3 + 2$ and $N_x = y^3 - 4$. Then
$$\frac{N_x - M_y}{M} = \frac{-3y^3 - 6}{y(y^3 + 2)} = -\frac{3}{y},$$
a function of $y$ alone, so the IF is $e^{\int -3/y\,dy} = y^{-3}$.

The equation becomes $\left(y + \frac{2}{y^2}\right)dx + \left(x + 2y - \frac{4x}{y^3}\right)dy = 0$, which is exact, with solution $xy + \frac{2x}{y^2} + y^2 = C$. Using $\frac{M_y - N_x}{M}$ (wrong sign) gives $y^3$.""")

# ---------------------------------------------------------------- statements
# q22
T.statements(1, ["order-degree", "formation"],
    r"Consider the following statements:",
    [r"The differential equation of the family $y = (A + B)e^{x + C}$ ($A$, $B$, $C$ arbitrary constants) is of order $1$.",
     r"The degree of $\left(\frac{d^3y}{dx^3}\right)^{2/3} = \frac{dy}{dx}$ is $2$.",
     r"The differential equation of all straight lines in the plane is $\frac{dy}{dx} = 0$."],
    [r"1 and 2 only", r"1, 2 and 3", r"2 only", r"1 and 3 only"],
    r"""**1 is true.** $(A + B)e^{x + C} = Ke^x$ with $K = (A + B)e^C$: only one essential constant, giving $y' = y$.

**2 is true.** Cube both sides: $\left(y'''\right)^2 = \left(y'\right)^3$. The highest derivative $y'''$ now has power $2$.

**3 is false.** $y = mx + c$ has two constants; differentiating twice gives $y'' = 0$. $y' = 0$ describes only horizontal lines.""")

# q23
T.statements(2, ["exact", "integrating-factors"],
    r"Consider the following statements about $M\,dx + N\,dy = 0$:",
    [r"$x\,dy - y\,dx = 0$ is exact.",
     r"If $\mu$ is an integrating factor and $u(x, y) = C$ is the resulting solution, then $\mu\,g(u)$ is also an integrating factor for every differentiable $g$.",
     r"$(x + y)\,dx + (x - y)\,dy = 0$ is exact."],
    [r"2 and 3 only", r"1 and 2 only", r"3 only", r"1, 2 and 3"],
    r"""**1 is false.** $M = -y$, $N = x$: $M_y = -1 \ne 1 = N_x$. (Its IFs include $\frac{1}{x^2}$, giving $d\left(\frac{y}{x}\right) = 0$.)

**2 is true.** $\mu M = u_x$ and $\mu N = u_y$, so $\mu g(u)M = g(u)u_x = \frac{\partial G(u)}{\partial x}$ and $\mu g(u)N = \frac{\partial G(u)}{\partial y}$, where $G' = g$. This is why IFs are never unique.

**3 is true.** $M_y = 1 = N_x$. The solution is $\frac{x^2}{2} + xy - \frac{y^2}{2} = C$.""")

# ---------------------------------------------------------------- match
# q24
T.match(2, ["separable", "homogeneous"],
    r"Match each equation with the substitution or method that solves it most directly.",
    [r"$\frac{dy}{dx} = \frac{x^2 + y^2}{2xy}$", r"$\frac{dy}{dx} = \frac{x + y - 1}{x + y + 1}$", r"$\frac{dy}{dx} = \frac{x - y + 1}{x + y - 3}$", r"$e^x\tan y\,dx + (1 - e^x)\sec^2 y\,dy = 0$"],
    [r"separate the variables directly", r"put $y = vx$", r"put $x = X + 1$, $y = Y + 2$", r"put $z = x + y$"],
    [r"A-2, B-4, C-3, D-1", r"A-2, B-3, C-4, D-1", r"A-1, B-4, C-3, D-2", r"A-2, B-4, C-1, D-3"],
    r"""- A is homogeneous (degree $2$ over degree $2$): A-2.
- B: the lines $x + y - 1 = 0$ and $x + y + 1 = 0$ are parallel ($a_1b_2 - a_2b_1 = 0$), so no shift works; $z = x + y$ makes it separable: B-4.
- C: $x - y + 1 = 0$ and $x + y - 3 = 0$ meet at $(1, 2)$, and $a_1b_2 - a_2b_1 = 2 \ne 0$; shifting the origin there makes it homogeneous: C-3.
- D: divide by $(1 - e^x)\tan y$ to get $\frac{e^x}{1 - e^x}dx + \frac{\sec^2 y}{\tan y}dy = 0$: D-1.

Swapping B and C is the usual trap: the shift works only when the lines **intersect**.""")

# q25
T.match(3, ["integrating-factors"],
    r"Match each equation with an integrating factor.",
    [r"$(y + xy^2)\,dx - x\,dy = 0$", r"$x\,dy - y\,dx = (x^2 + y^2)\,dx$", r"$(x^2y - 2xy^2)\,dx - (x^3 - 3x^2y)\,dy = 0$", r"$(x + y)\,dx + dy = 0$"],
    [r"$e^x$", r"$\frac{1}{x^2y^2}$", r"$\frac{1}{y^2}$", r"$\frac{1}{x^2 + y^2}$"],
    [r"A-3, B-4, C-2, D-1", r"A-3, B-4, C-1, D-2", r"A-4, B-3, C-2, D-1", r"A-2, B-4, C-3, D-1"],
    r"""- A: $\frac{y\,dx - x\,dy}{y^2} + x\,dx = d\left(\frac{x}{y} + \frac{x^2}{2}\right)$: A-3.
- B: $\frac{x\,dy - y\,dx}{x^2 + y^2} = dx$ is $d\left(\tan^{-1}\frac{y}{x}\right) = dx$: B-4.
- C: homogeneous of degree $3$ with $Mx + Ny = x^3y - 2x^2y^2 - x^3y + 3x^2y^2 = x^2y^2$: C-2.
- D: $\frac{M_y - N_x}{N} = \frac{1 - 0}{1} = 1$, so the IF is $e^x$, giving $d\left(e^x(x + y - 1)\right) = 0$: D-1.

Each IF works for its own equation only; for example $\frac{1}{y^2}$ does not make B exact.""")

# ---------------------------------------------------------------- assertion-reason
# q26
T.assertion_reason(1, ["formation"],
    r"The differential equation of the family $y = c(x - c)^2$ has order $1$.",
    r"The family $y = c(x - c)^2$ contains exactly one essential arbitrary constant.",
    0,
    r"""Both are true, and R explains A.

The order of the ODE of a family equals the number of essential constants. Here there is one ($c$), so the ODE has order $1$. Eliminating $c$ gives
$$\left(y'\right)^3 = 4y\left(xy' - 2y\right),$$
which has order $1$ (and degree $3$).""")

# q27
T.assertion_reason(1, ["exact", "homogeneous"],
    r"$(2x + y)\,dx + (x + 2y)\,dy = 0$ is exact.",
    r"$(2x + y)\,dx + (x + 2y)\,dy = 0$ is a homogeneous equation.",
    1,
    r"""Both are true, but R does not explain A.

A: $M_y = 1 = N_x$, so it is exact, with solution $x^2 + xy + y^2 = C$.

R: $M$ and $N$ are both homogeneous of degree $1$. But homogeneity does not imply exactness: $y\,dx - x\,dy = 0$ is homogeneous and not exact. A holds because $M_y = N_x$.""")

# q28
T.assertion_reason(2, ["homogeneous"],
    r"$\frac{dy}{dx} = \frac{x + y + 1}{x + y - 1}$ can be made homogeneous by a shift of origin $x = X + h$, $y = Y + k$.",
    r"For $\frac{dy}{dx} = \frac{a_1x + b_1y + c_1}{a_2x + b_2y + c_2}$ with $a_1b_2 - a_2b_1 \ne 0$, the shift of origin to the intersection of $a_1x + b_1y + c_1 = 0$ and $a_2x + b_2y + c_2 = 0$ makes the equation homogeneous.",
    3,
    r"""A is false, R is true.

R is the standard method: at the intersection $(h, k)$ the constant terms vanish, leaving $\frac{dY}{dX} = \frac{a_1X + b_1Y}{a_2X + b_2Y}$.

In A, $a_1b_2 - a_2b_1 = 1\cdot 1 - 1\cdot 1 = 0$: the lines $x + y + 1 = 0$ and $x + y - 1 = 0$ are parallel, so there is no $(h, k)$ that kills both constants. The right method is $z = x + y$.""")

# q29
T.assertion_reason(2, ["existence"],
    r"The initial value problem $\frac{dy}{dx} = x^2 + y^2$, $y(0) = 0$, has a unique solution on some interval $\lvert x\rvert < h$, $h > 0$.",
    r"Whenever $f(x, y)$ is continuous near $(x_0, y_0)$, the problem $y' = f(x, y)$, $y(x_0) = y_0$, has a unique solution near $x_0$.",
    2,
    r"""A is true, R is false.

A: $f = x^2 + y^2$ and $\frac{\partial f}{\partial y} = 2y$ are continuous on every rectangle around $(0, 0)$, so Picard's theorem gives a unique local solution.

R: continuity gives only **existence** (Peano). For $y' = 3y^{2/3}$, $y(0) = 0$, the function $f$ is continuous, yet $y = 0$ and $y = x^3$ are two different solutions. Uniqueness needs a Lipschitz condition in $y$.""")

# q30
T.assertion_reason(3, ["integrating-factors"],
    r"$\frac{1}{x^2 + y^2}$ is an integrating factor of $(x + y)\,dx - (x - y)\,dy = 0$.",
    r"If $M\,dx + N\,dy = 0$ is homogeneous and $Mx + Ny \ne 0$, then $\frac{1}{Mx + Ny}$ is an integrating factor.",
    0,
    r"""Both are true, and R explains A.

$M = x + y$ and $N = -(x - y)$ are homogeneous of degree $1$, and
$$Mx + Ny = x^2 + xy - xy + y^2 = x^2 + y^2 \ne 0.$$
So by R the IF is $\frac{1}{x^2 + y^2}$. Indeed
$$\frac{x\,dx + y\,dy}{x^2 + y^2} - \frac{x\,dy - y\,dx}{x^2 + y^2} = d\left(\tfrac12\ln(x^2 + y^2) - \tan^{-1}\frac{y}{x}\right),$$
so the solution is $\tfrac12\ln(x^2 + y^2) - \tan^{-1}\frac{y}{x} = C$.""")


def check():
    import sympy as sp
    x, y, C, k = sp.symbols("x y C k")
    p, q, r3 = sp.symbols("p q r3")      # y', y'', y'''
    Y = sp.Function("Y")

    def slope(u):
        return -sp.diff(u, x) / sp.diff(u, y)

    def sol(u, f, label):           # u(x, y) = C solves y' = f
        eq(sp.simplify(slope(u) - f), 0, label)

    def notsol(u, f, label):
        d = sp.simplify(slope(u) - f)
        if d == 0:
            sys.exit(f"CHECK FAILED {label}: distractor is a solution")

    def exact(M, N):
        return sp.simplify(sp.diff(M, y) - sp.diff(N, x)) == 0

    def isexact(M, N, label):
        if not exact(M, N):
            sys.exit(f"CHECK FAILED {label}: not exact")

    def notexact(M, N, label):
        if exact(M, N):
            sys.exit(f"CHECK FAILED {label}: unexpectedly exact")

    def deg(expr, var):
        return sp.Poly(sp.expand(expr), var).degree()

    def ishom(F, n):
        t = sp.symbols("t", positive=True)
        return sp.simplify(F.subs({x: t * x, y: t * y}, simultaneous=True) - t**n * F) == 0

    # q1: square -> (1+p^2)^3 = q^2, degree 2 in q
    eq(deg((1 + p**2)**3 - q**2, q), 2, "q1")
    # q2: sin(p) not polynomial
    assert not sp.sin(p).is_polynomial(p), "q2"
    # q3: linear in (y, p, q) iff all second partials vanish
    def linear(E):
        vs = [y, p, q]
        return all(sp.diff(E, a, b) == 0 for a in vs for b in vs)
    assert linear(q + x**2 * y - sp.sin(x)), "q3 key"
    assert not linear(y * q + p) and not linear(q + sp.sin(y)) and not linear(p**2 + y - x), "q3 distractors"
    # q4
    A, B = sp.symbols("A B")
    yy = A * sp.exp(2 * x) + B * sp.exp(-2 * x)
    eq(sp.diff(yy, x, 2) - 4 * yy, 0, "q4")
    assert sp.simplify(sp.diff(yy, x, 2) + 4 * yy) != 0 and sp.simplify(sp.diff(yy, x, 2) - 4 * sp.diff(yy, x)) != 0, "q4 d"
    # q5: x^2 + y^2 = 2 a x  ->  u = (x^2+y^2)/x
    u5 = (x**2 + y**2) / x
    sol(u5, (y**2 - x**2) / (2 * x * y), "q5")
    notsol(u5, (x**2 - y**2) / (2 * x * y), "q5 d1"); notsol(u5, (y**2 - x**2) / (x * y), "q5 d2"); notsol(u5, (x**2 + y**2) / (2 * x * y), "q5 d3")
    # q6
    s6 = sp.dsolve(sp.Eq(Y(x).diff(x), Y(x)**2), Y(x), ics={Y(0): 1})
    eq(s6.rhs, 1 / (1 - x), "q6 solution")
    assert sp.solve(sp.denom(sp.together(s6.rhs)), x) == [1], "q6 blow-up"
    # q7
    sol(sp.atan(y) - sp.atan(x), (1 + y**2) / (1 + x**2), "q7")
    notsol(sp.atan(y) + sp.atan(x), (1 + y**2) / (1 + x**2), "q7 d1")
    notsol(sp.log(1 + y**2) - sp.log(1 + x**2), (1 + y**2) / (1 + x**2), "q7 d2")
    notsol(y - x, (1 + y**2) / (1 + x**2), "q7 d3")
    # q8
    ode8 = sp.Eq(Y(x).diff(x), sp.exp(x + Y(x)))
    key8 = -sp.log(2 - sp.exp(x))
    assert sp.checkodesol(ode8, sp.Eq(Y(x), key8))[0], "q8"
    eq(key8.subs(x, 0), 0, "q8 ic")
    for d in [sp.log(2 - sp.exp(x)), -sp.log(2 - sp.exp(-x)), x]:
        assert not sp.checkodesol(ode8, sp.Eq(Y(x), d))[0], "q8 distractor"
    # q9
    f9 = (x + y + 1)**2
    sol(sp.atan(x + y + 1) - x, f9, "q9")
    assert sp.checkodesol(sp.Eq(Y(x).diff(x), (x + Y(x) + 1)**2), sp.Eq(Y(x), sp.tan(x + C) - x - 1))[0], "q9 explicit"
    notsol(sp.atan(x + y + 1) - y, f9, "q9 d1"); notsol(x + y + 1 - sp.tan(x), f9, "q9 d2"); notsol(-1 / (x + y + 1) - x, f9, "q9 d3")
    # q10
    f10 = (x**2 + y**2) / (2 * x * y)
    assert ishom(x**2 + y**2, 2) and ishom(2 * x * y, 2), "q10 hom"
    sol((x**2 - y**2) / x, f10, "q10")
    notsol((x**2 + y**2) / x, f10, "q10 d1"); notsol((x**2 - y**2) / y, f10, "q10 d2"); notsol((x**2 - y**2) / x**2, f10, "q10 d3")
    # q11
    f11 = y / x + sp.tan(y / x)
    sol(sp.sin(y / x) / x, f11, "q11")
    notsol(sp.cos(y / x) / x, f11, "q11 d1"); notsol(sp.tan(y / x) / x, f11, "q11 d2"); notsol(x * sp.sin(y / x), f11, "q11 d3")
    # q12
    f12 = (x + y + 1) / (2 * x + 2 * y + 3)
    eq(1 * 2 - 2 * 1, 0, "q12 parallel")
    sol(6 * y - 3 * x + sp.log(3 * x + 3 * y + 4), f12, "q12")
    notsol(6 * y - 3 * x - sp.log(3 * x + 3 * y + 4), f12, "q12 d1")
    notsol(6 * y + 3 * x + sp.log(3 * x + 3 * y + 4), f12, "q12 d2")
    notsol(3 * y - 6 * x + sp.log(3 * x + 3 * y + 4), f12, "q12 d3")
    # q13
    eq(sp.solve(sp.diff(3 * x**2 + k * x * y**2, y) - sp.diff(2 * x**2 * y + 4 * y**3, x), k)[0], 2, "q13")
    u13 = x**3 + x**2 * y**2 + y**4
    eq(sp.diff(u13, x), 3 * x**2 + 2 * x * y**2, "q13 u_x"); eq(sp.diff(u13, y), 2 * x**2 * y + 4 * y**3, "q13 u_y")
    # q14
    M14, N14 = 2 * x * y + sp.exp(x), x**2 + sp.cos(y)
    isexact(M14, N14, "q14 exact")
    u14 = x**2 * y + sp.exp(x) + sp.sin(y)
    eq(sp.diff(u14, x), M14, "q14 ux"); eq(sp.diff(u14, y), N14, "q14 uy")
    for d in [2 * x**2 * y + sp.exp(x) + sp.sin(y), x**2 * y + sp.exp(x) - sp.sin(y), x**2 * y - sp.exp(x) + sp.sin(y)]:
        notsol(d, -M14 / N14, "q14 d")
    # q15
    M15, N15 = y * sp.exp(x * y) + 2 * x, x * sp.exp(x * y) - 2 * y
    isexact(M15, N15, "q15 exact")
    u15 = sp.exp(x * y) + x**2 - y**2
    eq(sp.diff(u15, x), M15, "q15 ux"); eq(sp.diff(u15, y), N15, "q15 uy")
    eq(u15.subs({x: 0, y: 1}), 0, "q15 ic")
    notsol(sp.exp(x * y) - x**2 - y**2, -M15 / N15, "q15 d1"); notsol(sp.exp(x * y) + x**2 + y**2, -M15 / N15, "q15 d2")
    eq((sp.exp(x * y) - x**2 - y**2).subs({x: 0, y: 1}), 0, "q15 d1 passes ic")
    # q16
    for mu in [1 / x**2, 1 / (x * y), 1 / (x**2 + y**2)]:
        isexact(mu * y, -mu * x, f"q16 {mu}")
    notexact(y / (x * y**2), -x / (x * y**2), "q16 key")
    # q17
    M17, N17 = x * y**2 - sp.exp(1 / x**3), -x**2 * y
    eq(sp.simplify((sp.diff(M17, y) - sp.diff(N17, x)) / N17), -4 / x, "q17 ratio")
    isexact(M17 / x**4, N17 / x**4, "q17")
    for mu in [x**4, 1 / x**2, 1 / y**2]:
        notexact(mu * M17, mu * N17, f"q17 d {mu}")
    # q18
    M18, N18 = x**2 + y**2 + x, x * y
    eq(sp.simplify((sp.diff(M18, y) - sp.diff(N18, x)) / N18), 1 / x, "q18 ratio")
    isexact(x * M18, x * N18, "q18 exact")
    sol(3 * x**4 + 4 * x**3 + 6 * x**2 * y**2, -M18 / N18, "q18")
    notsol(3 * x**4 + 4 * x**3 + 3 * x**2 * y**2, -M18 / N18, "q18 d1")
    notsol(x**3 + 3 * x * y**2 + sp.Rational(3, 2) * x**2, -M18 / N18, "q18 d2")
    notsol(3 * x**4 - 4 * x**3 + 6 * x**2 * y**2, -M18 / N18, "q18 d3")
    # q19
    M19, N19 = y**2, x**2 - x * y - y**2
    assert ishom(M19, 2) and ishom(N19, 2), "q19 hom"
    eq(sp.factor(M19 * x + N19 * y), y * (x**2 - y**2), "q19 Mx+Ny")
    isexact(M19 / (y * (x**2 - y**2)), N19 / (y * (x**2 - y**2)), "q19")
    for mu in [1 / (y * (x**2 + y**2)), 1 / (x * (x**2 - y**2)), 1 / (x**2 * y**2)]:
        notexact(mu * M19, mu * N19, f"q19 d {mu}")
    # q20
    M20, N20 = y * (x * y + 2 * x**2 * y**2), x * (x * y - x**2 * y**2)
    eq(sp.expand(M20 * x - N20 * y), 3 * x**3 * y**3, "q20 Mx-Ny")
    isexact(M20 / (x**3 * y**3), N20 / (x**3 * y**3), "q20")
    for mu in [1 / (x**2 * y**2), x**3 * y**3, 1 / (x * y)]:
        notexact(mu * M20, mu * N20, f"q20 d {mu}")
    # q21
    M21, N21 = y**4 + 2 * y, x * y**3 + 2 * y**4 - 4 * x
    eq(sp.simplify((sp.diff(N21, x) - sp.diff(M21, y)) / M21), -3 / y, "q21 ratio")
    isexact(M21 / y**3, N21 / y**3, "q21")
    sol(x * y + 2 * x / y**2 + y**2, -M21 / N21, "q21 solution")
    for mu in [y**3, 1 / y**4, sp.exp(-3 * x)]:
        notexact(mu * M21, mu * N21, f"q21 d {mu}")
    # q22
    Kc = sp.symbols("K")
    eq(sp.diff(Kc * sp.exp(x), x) - Kc * sp.exp(x), 0, "q22 s1")
    eq(deg(q**2 - p**3, q), 2, "q22 s2")                       # (y''')^2 = (y')^3, degree 2 (q stands for y''')
    assert sp.diff(x, x) != 0, "q22 s3: y = x is a line with y' != 0"
    m_, c_ = sp.symbols("m c")
    eq(sp.diff(m_ * x + c_, x, 2), 0, "q22 s3 y''=0")
    # q23
    notexact(-y, x, "q23 s1")
    isexact(x + y, x - y, "q23 s3")
    sol(x**2 / 2 + x * y - y**2 / 2, -(x + y) / (x - y), "q23 s3 sol")
    g = sp.Function("g")
    mu, uu = 1 / x**2, -y / x          # y dx - x dy: mu M = u_x, mu N = u_y
    eq(sp.diff(uu, x) - mu * y, 0, "q23 s2a"); eq(sp.diff(uu, y) + mu * x, 0, "q23 s2b")
    isexact(mu * g(uu) * y, -mu * g(uu) * x, "q23 s2 general g")
    # q24
    assert ishom(x**2 + y**2, 2) and ishom(2 * x * y, 2), "q24 A"
    eq(1 * 1 - 1 * 1, 0, "q24 B parallel")
    hk = sp.solve([x - y + 1, x + y - 3], [x, y]); eq(hk[x], 1, "q24 C h"); eq(hk[y], 2, "q24 C k")
    eq(1 * 1 - 1 * (-1), 2, "q24 C det")
    isexact(sp.exp(x) / (1 - sp.exp(x)), 1 / sp.tan(y) * sp.sec(y)**2, "q24 D separated")
    sol(sp.tan(y) / (1 - sp.exp(x)), -sp.exp(x) * sp.tan(y) / ((1 - sp.exp(x)) * sp.sec(y)**2), "q24 D solution")
    # q25: only the key pairing makes each equation exact
    eqs = {"A": (y + x * y**2, -x), "B": (-(x**2 + y**2) - y, x),
           "C": (x**2 * y - 2 * x * y**2, -(x**3 - 3 * x**2 * y)), "D": (x + y, sp.Integer(1))}
    ifs = {1: sp.exp(x), 2: 1 / (x**2 * y**2), 3: 1 / y**2, 4: 1 / (x**2 + y**2)}
    works = {L: [n for n, m in ifs.items() if exact(m * M, m * N)] for L, (M, N) in eqs.items()}
    assert works == {"A": [3], "B": [4], "C": [2], "D": [1]}, f"q25 {works}"
    sol(sp.exp(x) * (x + y - 1), -(x + y), "q25 D sol")
    M, N = eqs["C"]; eq(sp.expand(M * x + N * y), x**2 * y**2, "q25 C Mx+Ny")
    # q26: y = c(x-c)^2 -> (y')^3 = 4y(xy' - 2y)
    c = sp.symbols("c")
    y26 = c * (x - c)**2
    eq(sp.diff(y26, x)**3 - 4 * y26 * (x * sp.diff(y26, x) - 2 * y26), 0, "q26")
    # q27
    isexact(2 * x + y, x + 2 * y, "q27 A")
    assert ishom(2 * x + y, 1) and ishom(x + 2 * y, 1), "q27 R"
    notexact(y, -x, "q27 hom but not exact")
    sol(x**2 + x * y + y**2, -(2 * x + y) / (x + 2 * y), "q27 sol")
    # q28
    eq(1 * 1 - 1 * 1, 0, "q28 A false")
    assert sp.solve([x + y + 1, x + y - 1], [x, y]) == [], "q28 no intersection"
    X, Yv = sp.symbols("X Yv")
    eq(sp.expand((x - y + 1).subs({x: X + 1, y: Yv + 2})), X - Yv, "q28 R example num")
    eq(sp.expand((x + y - 3).subs({x: X + 1, y: Yv + 2})), X + Yv, "q28 R example den")
    # q29
    fA = x**2 + y**2
    assert sp.diff(fA, y) == 2 * y, "q29 A"
    ode29 = sp.Eq(Y(x).diff(x), 3 * Y(x)**sp.Rational(2, 3))
    xp = sp.symbols("xp", positive=True)
    eq(sp.diff(xp**3, xp) - 3 * (xp**3)**sp.Rational(2, 3), 0, "q29 R counterexample x^3 (x>0)")
    xn = sp.symbols("xn", negative=True)
    eq(sp.diff(xn**3, xn) - 3 * ((xn**3)**2)**sp.Rational(1, 3), 0, "q29 R counterexample x^3 (x<0, y^(2/3) as real cube root of y^2)")
    eq(sp.diff(sp.Integer(0), x) - 3 * sp.Integer(0)**sp.Rational(2, 3), 0, "q29 R y=0")
    # q30
    M30, N30 = x + y, -(x - y)
    assert ishom(M30, 1) and ishom(N30, 1), "q30 hom"
    eq(sp.expand(M30 * x + N30 * y), x**2 + y**2, "q30 Mx+Ny")
    isexact(M30 / (x**2 + y**2), N30 / (x**2 + y**2), "q30 exact")
    sol(sp.log(x**2 + y**2) / 2 - sp.atan(y / x), -M30 / N30, "q30 sol")


T.write(check)
