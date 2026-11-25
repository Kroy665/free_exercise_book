import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from qlib import Topic, eq

T = Topic("math.ode.ode-linear-clairaut")

# ---------------------------------------------------------------- linear equations
# q1
T.single(1, ["linear-equations", "exam-tips"],
         r"An integrating factor of $x\dfrac{dy}{dx} - 2y = x^3$ $(x > 0)$ is",
         [r"$\dfrac{1}{x^2}$", r"$x^2$", r"$e^{-2x}$", r"$\dfrac1x$"],
         r"""Standard form: $\dfrac{dy}{dx} - \dfrac{2}{x}y = x^2$, so $P = -\dfrac2x$ and
$$\text{IF} = e^{\int -2/x\,dx} = e^{-2\ln x} = \frac{1}{x^2}.$$
$x^2$ ignores the minus sign in $P$; $e^{-2x}$ forgets to divide by $x$ before reading off $P$.""")

# q2
T.single(1, ["linear-equations"],
         r"An integrating factor of $\dfrac{dy}{dx} + y\tan x = \sec x$ on $\left(-\dfrac\pi2, \dfrac\pi2\right)$ is",
         [r"$\sec x$", r"$\cos x$", r"$e^{\tan x}$", r"$e^{\sec x}$"],
         r"""$$\text{IF} = e^{\int \tan x\,dx} = e^{\ln\sec x} = \sec x.$$
Then $y\sec x = \int\sec^2x\,dx = \tan x + C$, so $y = \sin x + C\cos x$.

$\cos x$ comes from $\int\tan x\,dx = \ln\cos x$ (wrong sign); $e^{\tan x}$ forgets to integrate $P$.""")

# q3
T.single(1, ["linear-equations", "exam-tips"],
         r"The general solution of $\dfrac{dy}{dx} + 2y = e^{-x}$ is",
         [r"$y = e^{-x} + Ce^{-2x}$", r"$y = -e^{-x} + Ce^{-2x}$", r"$y = e^{-x} + Ce^{2x}$",
          r"$y = xe^{-2x} + Ce^{-2x}$"],
         r"""IF $= e^{2x}$:
$$ye^{2x} = \int e^{-x}e^{2x}\,dx = e^{x} + C \implies y = e^{-x} + Ce^{-2x}.$$
Check: for $y = e^{-x}$, $y' + 2y = -e^{-x} + 2e^{-x} = e^{-x}$. The constant part must solve $y' + 2y = 0$, so it is $Ce^{-2x}$, not $Ce^{2x}$. The form $xe^{-2x}$ would be needed only if the right side were $e^{-2x}$.""")

# q4
T.single(2, ["linear-equations"],
         r"The general solution of $x\dfrac{dy}{dx} + 2y = x^2$ $(x > 0)$ is",
         [r"$y = \dfrac{x^2}{4} + \dfrac{C}{x^2}$", r"$y = \dfrac{x^2}{3} + \dfrac{C}{x^2}$",
          r"$y = \dfrac{x^2}{4} + Cx^2$", r"$y = \dfrac{x^2}{2} + \dfrac{C}{x^2}$"],
         r"""Standard form: $y' + \dfrac{2}{x}y = x$, so IF $= x^2$ and
$$x^2y = \int x^3\,dx = \frac{x^4}{4} + C \implies y = \frac{x^2}{4} + \frac{C}{x^2}.$$
$\dfrac{x^2}{3}$ integrates $x^2$ instead of $x^3$ (forgetting to divide the equation by $x$); $Cx^2$ multiplies by the IF instead of dividing.""")

# q5
T.single(2, ["linear-equations"],
         r"If $\dfrac{dy}{dx} + y = 1$ and $y(0) = 0$, then $y(\ln 2)$ equals",
         [r"$\dfrac12$", r"$\dfrac32$", r"$1$", r"$\dfrac14$"],
         r"""IF $= e^x$: $ye^x = e^x + C$, so $y = 1 + Ce^{-x}$. From $y(0) = 0$, $C = -1$:
$$y = 1 - e^{-x}, \qquad y(\ln 2) = 1 - \tfrac12 = \tfrac12.$$
$\frac32$ comes from $C = +1$ (sign slip); $1$ is the limit as $x \to \infty$, not the value at $\ln 2$.""")

# q6
T.single(2, ["linear-equations"],
         r"The general solution of $y\,dx = (x + y^2)\,dy$ $(y > 0)$ is",
         [r"$x = y^2 + Cy$", r"$x = y^2 + \dfrac{C}{y}$", r"$y = x^2 + Cx$", r"$x = \dfrac{y^2}{2} + Cy$"],
         r"""The equation is linear in $x$:
$$\frac{dx}{dy} - \frac{x}{y} = y, \qquad \text{IF} = e^{-\int dy/y} = \frac1y.$$
Then $\dfrac{x}{y} = \int y\cdot\dfrac1y\,dy = y + C$, so $x = y^2 + Cy$.

$\dfrac{C}{y}$ uses IF $y$ (sign slip in $P$); $y = x^2 + Cx$ swaps the roles of $x$ and $y$. Check: $x = y^2 + Cy$ gives $\frac{dx}{dy} = 2y + C = \frac{x}{y} + y$.""")

# ---------------------------------------------------------------- Bernoulli
# q7
T.single(1, ["bernoulli", "exam-tips"],
         r"The equation $\dfrac{dy}{dx} + \dfrac{y}{x} = xy^3$ becomes linear under the substitution",
         [r"$v = y^{-2}$", r"$v = y^{-3}$", r"$v = y^{2}$", r"$v = y^{-4}$"],
         r"""This is Bernoulli with $n = 3$, and the substitution is $v = y^{1-n} = y^{-2}$. It gives
$$\frac{dv}{dx} - \frac{2}{x}v = -2x.$$
$y^{-3}$ uses $y^{-n}$ (the factor you divide by), not $y^{1-n}$.""")

# q8
T.single(2, ["bernoulli"],
         r"The general solution of $\dfrac{dy}{dx} + y = xy^2$ (apart from $y = 0$) is",
         [r"$\dfrac1y = x + 1 + Ce^{x}$", r"$\dfrac1y = x - 1 + Ce^{x}$", r"$\dfrac1y = x + 1 + Ce^{-x}$",
          r"$y = x + 1 + Ce^{x}$"],
         r"""Bernoulli with $n = 2$: put $v = \dfrac1y$, so $v' = -\dfrac{y'}{y^2}$. Dividing the equation by $-y^2$:
$$v' - v = -x, \qquad \text{IF } e^{-x}, \qquad ve^{-x} = \int -xe^{-x}\,dx = (x + 1)e^{-x} + C.$$
So $\dfrac1y = x + 1 + Ce^{x}$.

$Ce^{-x}$ forgets that the factor $(1 - n) = -1$ flips the sign of $P$; $x - 1$ is an integration-by-parts slip.""")

# q9
T.single(3, ["bernoulli"],
         r"The general solution of $\sec^2 y\,\dfrac{dy}{dx} + 2x\tan y = x^3$ is",
         [r"$\tan y = \dfrac{x^2 - 1}{2} + Ce^{-x^2}$", r"$\tan y = \dfrac{x^2 + 1}{2} + Ce^{-x^2}$",
          r"$\tan y = \dfrac{x^2 - 1}{2} + Ce^{x^2}$", r"$\tan y = \dfrac{x^4}{4} + Ce^{-x^2}$"],
         r"""Put $v = \tan y$, so $v' = \sec^2 y\,y'$:
$$v' + 2xv = x^3, \qquad \text{IF} = e^{x^2}.$$
With $t = x^2$: $\displaystyle\int x^3e^{x^2}dx = \tfrac12\int te^t\,dt = \tfrac12(x^2 - 1)e^{x^2}$. So
$$\tan y = \frac{x^2 - 1}{2} + Ce^{-x^2}.$$
$x^2 + 1$ is a sign slip in $\int te^t\,dt$; $\frac{x^4}{4}$ integrates $x^3$ without the IF.""")

# ---------------------------------------------------------------- higher degree
# q10
T.single(2, ["higher-degree"],
         r"The general solution of $p^2 - (x + y)p + xy = 0$, where $p = \dfrac{dy}{dx}$, is",
         [r"$(2y - x^2 - c)(y - ce^{x}) = 0$", r"$(2y - x^2 - c)(y - ce^{-x}) = 0$",
          r"$(y - x^2 - c)(y - ce^{x}) = 0$", r"$(2y + x^2 - c)(y - ce^{x}) = 0$"],
         r"""The equation factorises: $(p - x)(p - y) = 0$.
- $p = x$ gives $y = \frac{x^2}{2} + \frac{c}{2}$, i.e. $2y - x^2 - c = 0$.
- $p = y$ gives $y = ce^x$.

So the general solution is $(2y - x^2 - c)(y - ce^x) = 0$, with one constant. $ce^{-x}$ solves $p = -y$; $y - x^2$ forgets the $\frac12$ in $\int x\,dx$.""")

# q11
T.single(3, ["higher-degree"],
         r"For $y = 2px + p^2$, where $p = \dfrac{dy}{dx}$, differentiating with respect to $x$ and solving gives $x$ in terms of the parameter $p$ as",
         [r"$x = \dfrac{c}{p^2} - \dfrac{2p}{3}$", r"$x = \dfrac{c}{p^2} + \dfrac{2p}{3}$",
          r"$x = cp^2 - \dfrac{2p}{3}$", r"$x = \dfrac{c}{p} - p$"],
         r"""Differentiating, $p = 2p + (2x + 2p)\dfrac{dp}{dx}$, so $-p\,\dfrac{dx}{dp} = 2x + 2p$:
$$\frac{dx}{dp} + \frac{2}{p}x = -2.$$
This is linear in $x$ with IF $p^2$: $xp^2 = \int -2p^2\,dp = -\frac{2p^3}{3} + c$. So
$$x = \frac{c}{p^2} - \frac{2p}{3}, \qquad y = 2px + p^2.$$
$cp^2$ multiplies by the IF instead of dividing; $+\frac{2p}{3}$ loses the minus sign.""")

# q12
T.single(2, ["singular-solutions"],
         r"The singular solution of $p^2 + y^2 = 1$, where $p = \dfrac{dy}{dx}$, is",
         [r"$y = \pm1$", r"$y = 0$", r"$x = \pm1$", r"there is none"],
         r"""The $p$-discriminant: $\partial F/\partial p = 2p = 0$ with $F = 0$ gives $y^2 = 1$.

The general solution is $y = \sin(x + c)$ (from $\frac{dy}{\sqrt{1 - y^2}} = \pm dx$). The lines $y = \pm1$ satisfy the equation ($p = 0$, $0 + 1 = 1$), but no value of $c$ gives them. So they are singular solutions: the envelope of the sine curves.

$y = 0$ does not satisfy the equation: it would need $p^2 = 1$, but $p = 0$.""")

# ---------------------------------------------------------------- Clairaut
# q13
T.single(1, ["clairaut"],
         r"The general solution of $y = px + p^2$, where $p = \dfrac{dy}{dx}$, is",
         [r"$y = cx + c^2$", r"$y = cx^2 + c$", r"$y = cx + c$", r"$x^2 + 4y = 0$"],
         r"""This is Clairaut's equation $y = px + f(p)$ with $f(p) = p^2$. Differentiating gives $(x + 2p)\,\frac{dp}{dx} = 0$. Then $\frac{dp}{dx} = 0$ gives $p = c$:
$$y = cx + c^2.$$
$x^2 + 4y = 0$ is the **singular** solution (from $x + 2p = 0$), not the general one.""")

# q14
T.single(2, ["clairaut", "singular-solutions"],
         r"The singular solution of $y = px + p^2$, where $p = \dfrac{dy}{dx}$, is",
         [r"$x^2 + 4y = 0$", r"$x^2 - 4y = 0$", r"$y^2 + 4x = 0$", r"$4x^2 + y = 0$"],
         r"""Eliminate $p$ from $y = px + p^2$ and $x + 2p = 0$. With $p = -\frac{x}{2}$:
$$y = -\frac{x^2}{2} + \frac{x^2}{4} = -\frac{x^2}{4} \implies x^2 + 4y = 0.$$
Check: $y = -\frac{x^2}{4}$ has $p = -\frac{x}{2}$, and $px + p^2 = -\frac{x^2}{2} + \frac{x^2}{4} = y$. $x^2 - 4y = 0$ has the wrong sign: the lines $y = cx + c^2$ touch a downward parabola.""")

# q15
T.single(3, ["clairaut"],
         r"The singular solution of $y = px - e^{p}$, where $p = \dfrac{dy}{dx}$, is",
         [r"$y = x\ln x - x$", r"$y = x\ln x + x$", r"$y = x\ln x$", r"$y = x - x\ln x$"],
         r"""Clairaut with $f(p) = -e^p$. The singular solution comes from $x + f'(p) = 0$:
$$x - e^p = 0 \implies p = \ln x \;(x > 0), \qquad y = x\ln x - e^{\ln x} = x\ln x - x.$$
Check: $y' = \ln x$, and $px - e^p = x\ln x - x = y$.

$x\ln x + x$ comes from $f(p) = +e^p$; $x\ln x$ drops the $-e^p$ term.""")

# q16
T.single(3, ["clairaut", "singular-solutions"],
         r"The singular solution of $y = px + \sqrt{a^2p^2 + b^2}$ $(a, b > 0)$, where $p = \dfrac{dy}{dx}$, is",
         [r"$\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$", r"$\dfrac{x^2}{a^2} - \dfrac{y^2}{b^2} = 1$",
          r"$x^2 + y^2 = a^2 + b^2$", r"$\dfrac{x^2}{b^2} + \dfrac{y^2}{a^2} = 1$"],
         r"""The general solution is $y = cx + \sqrt{a^2c^2 + b^2}$. These are exactly the tangents of slope $c$ to the ellipse $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$, so their envelope is that ellipse.

Directly: $x + \dfrac{a^2p}{\sqrt{a^2p^2 + b^2}} = 0$ gives $x = -\dfrac{a^2p}{s}$ and $y = px + s = \dfrac{b^2}{s}$, where $s = \sqrt{a^2p^2 + b^2}$. Then
$$\frac{x^2}{a^2} + \frac{y^2}{b^2} = \frac{a^2p^2 + b^2}{s^2} = 1.$$
The hyperbola has tangents $y = mx \pm\sqrt{a^2m^2 - b^2}$ (minus sign); $x^2 + y^2 = a^2 + b^2$ is the director circle.""")

# q17
T.single(3, ["clairaut"],
         r"Using $X = x^2$, $Y = y^2$, the general solution of $x^2(y - px) = yp^2$, where $p = \dfrac{dy}{dx}$, is",
         [r"$y^2 = cx^2 + c^2$", r"$y = cx^2 + c^2$", r"$y^2 = cx + c^2$", r"$y^2 = cx^2 + c$"],
         r"""With $P = \dfrac{dY}{dX} = \dfrac{2y\,dy}{2x\,dx} = \dfrac{yp}{x}$, we have $p = \dfrac{xP}{y}$. Substituting and multiplying by $y$:
$$x^2y^2 - x^4P = x^2P^2 \implies Y = PX + P^2.$$
This is Clairaut in $X, Y$, so $Y = cX + c^2$, i.e. $y^2 = cx^2 + c^2$.

$y = cx^2 + c^2$ forgets to convert $Y$ back to $y^2$; $y^2 = cx^2 + c$ uses the wrong $f(P)$.""")

# ---------------------------------------------------------------- orthogonal trajectories
# q18
T.single(2, ["orthogonal-trajectories"],
         r"The orthogonal trajectories of the family $y = cx^2$ are",
         [r"$x^2 + 2y^2 = k$", r"$2x^2 + y^2 = k$", r"$x^2 - 2y^2 = k$", r"$x^2 + y^2 = k$"],
         r"""Eliminate $c$: $p = 2cx = \dfrac{2y}{x}$. Replace $p$ by $-\dfrac1p$:
$$-\frac{dx}{dy} = \frac{2y}{x} \implies x\,dx + 2y\,dy = 0 \implies x^2 + 2y^2 = k.$$
$2x^2 + y^2 = k$ belongs to the family $y^2 = cx$ (the roles of $x$ and $y$ swapped); $x^2 - 2y^2$ forgets the minus sign in $-\frac1p$.""")

# q19
T.single(3, ["orthogonal-trajectories"],
         r"The orthogonal trajectories of the cardioids $r = a(1 + \cos\theta)$ are",
         [r"$r = b(1 - \cos\theta)$", r"$r = b(1 + \sin\theta)$", r"$r = b(1 + \cos\theta)$", r"$r^2 = b\cos\theta$"],
         r"""$\dfrac1r\dfrac{dr}{d\theta} = \dfrac{-\sin\theta}{1 + \cos\theta} = -\tan\dfrac\theta2$. Replace $\dfrac1r\dfrac{dr}{d\theta}$ by $-r\dfrac{d\theta}{dr}$:
$$r\frac{d\theta}{dr} = \tan\frac\theta2 \implies \frac{dr}{r} = \cot\frac\theta2\,d\theta \implies \ln r = 2\ln\sin\frac\theta2 + \text{const}.$$
So $r = b\sin^2\frac\theta2$, i.e. $r = b(1 - \cos\theta)$.

$r = b(1 + \cos\theta)$ is the original family; $r = b(1 + \sin\theta)$ is only the family rotated by $90^\circ$, which does not cut it orthogonally.""")

# q20
T.single(1, ["orthogonal-trajectories"],
         r"To find orthogonal trajectories of a family given in polar form $F\left(r, \theta, \dfrac{dr}{d\theta}\right) = 0$, replace $\dfrac{dr}{d\theta}$ by",
         [r"$-r^2\dfrac{d\theta}{dr}$", r"$r^2\dfrac{d\theta}{dr}$", r"$-\dfrac{d\theta}{dr}$", r"$-\dfrac{1}{r^2}\dfrac{d\theta}{dr}$"],
         r"""The angle $\psi$ from the radius vector to the tangent satisfies $\tan\psi = r\dfrac{d\theta}{dr}$. For orthogonal curves at the same point, $\tan\psi_1\tan\psi_2 = -1$:
$$r\frac{d\theta}{dr}\bigg|_{\text{new}} = -\frac{1}{r\,d\theta/dr}\bigg|_{\text{old}} \implies \frac{dr}{d\theta}\bigg|_{\text{old}} = -r^2\frac{d\theta}{dr}\bigg|_{\text{new}}.$$
$-\dfrac{d\theta}{dr}$ is the Cartesian rule $p \to -1/p$ copied blindly; it ignores the factor $r$ in $\tan\psi$.""")

# ---------------------------------------------------------------- statements
# q21
T.statements(2, ["linear-equations", "bernoulli"],
             r"Consider the following statements.",
             [r"$\dfrac{dy}{dx} + xy^2 = x$ is a linear equation in $y$.",
              r"For $\dfrac{dy}{dx} + Py = Qy^n$ $(n \ne 0, 1)$, the substitution $v = y^{1-n}$ gives $\dfrac{dv}{dx} + (1 - n)Pv = (1 - n)Q$.",
              r"An integrating factor of $\dfrac{dx}{dy} + P(y)\,x = Q(y)$ is $e^{\int P(y)\,dy}$."],
             [r"2 and 3 only", r"1 and 2 only", r"3 only", r"1, 2 and 3"],
             r"""1. **False.** The term $xy^2$ is quadratic in $y$. (It is in fact separable: $\frac{dy}{dx} = x(1 - y^2)$.)
2. **True.** $v' = (1 - n)y^{-n}y'$. Dividing the equation by $y^n$ gives $y^{-n}y' + Pv = Q$, and multiplying by $(1 - n)$ gives the stated linear form.
3. **True.** It is linear with $x$ dependent and $y$ independent, so the IF is $e^{\int P\,dy}$.""")

# q22
T.statements(3, ["singular-solutions", "clairaut"],
             r"Consider the following statements about a first-order equation $F(x, y, p) = 0$ with general solution $\phi(x, y, c) = 0$.",
             [r"The general solution of a Clairaut equation $y = px + f(p)$ is a family of straight lines.",
              r"A singular solution is obtained from the general solution by giving the constant $c$ a suitable particular value.",
              r"An envelope appears once in the $c$-discriminant, a node locus twice and a cusp locus three times."],
             [r"1 and 3 only", r"1 and 2 only", r"2 and 3 only", r"1 only"],
             r"""1. **True.** It is $y = cx + f(c)$.
2. **False.** That is the definition of a *particular* solution. A singular solution satisfies the equation but is not obtained for any $c$ (e.g. $x^2 + 4y = 0$ for $y = px + p^2$).
3. **True.** Schematically, the $c$-discriminant is $E\,N^2C^3 = 0$, while the $p$-discriminant is $E\,T^2C = 0$.""")

# q23
T.statements(2, ["orthogonal-trajectories"],
             r"Consider the following statements about orthogonal trajectories.",
             [r"The family of parabolas $y^2 = 4a(x + a)$ is self-orthogonal.",
              r"The orthogonal trajectories of the circles $x^2 + y^2 = 2cx$ are the circles $x^2 + y^2 = 2ky$.",
              r"The orthogonal trajectories of $y = ce^{x}$ are $y = ke^{-x}$."],
             [r"1 and 2 only", r"2 and 3 only", r"1 and 3 only", r"1, 2 and 3"],
             r"""1. **True.** Eliminating $a$ (with $2yp = 4a$) gives $y = 2xp + yp^2$. Replacing $p$ by $-\frac1p$ and multiplying by $p^2$ gives back the same equation.
2. **True.** For $x^2 + y^2 = 2cx$, $p = \dfrac{y^2 - x^2}{2xy}$. For $x^2 + y^2 = 2ky$, $p = \dfrac{2xy}{x^2 - y^2}$, which is exactly $-\frac1p$ of the first.
3. **False.** For $y = ce^x$, $p = y$; the trajectories satisfy $p = -\frac1y$, so $y^2 = k - 2x$ (parabolas). $y = ke^{-x}$ would come from $p = -y$.""")

# ---------------------------------------------------------------- match
# q24
T.match(1, ["linear-equations"],
        r"Match each equation with an integrating factor.",
        [r"$\dfrac{dy}{dx} + \dfrac{y}{x} = x^2$", r"$\dfrac{dy}{dx} - \dfrac{y}{x} = x$",
         r"$\dfrac{dy}{dx} + y\cot x = \cos x$", r"$\dfrac{dy}{dx} + 2xy = x$"],
        [r"$\sin x$", r"$e^{x^2}$", r"$x$", r"$\dfrac1x$"],
        [r"A-3, B-4, C-1, D-2", r"A-4, B-3, C-1, D-2", r"A-3, B-4, C-2, D-1", r"A-1, B-4, C-3, D-2"],
        r"""IF $= e^{\int P\,dx}$ (take $x > 0$ and $0 < x < \pi$):
- A: $P = \frac1x$, IF $= x$.
- B: $P = -\frac1x$, IF $= \frac1x$.
- C: $P = \cot x$, IF $= e^{\ln\sin x} = \sin x$.
- D: $P = 2x$, IF $= e^{x^2}$.

Swapping A and B is the sign slip in $P$.""")

# q25
T.match(2, ["orthogonal-trajectories"],
        r"Match each family with its orthogonal trajectories.",
        [r"$y = cx$", r"$xy = c$", r"$y^2 = cx$", r"$r = a\cos\theta$"],
        [r"$x^2 - y^2 = k$", r"$x^2 + y^2 = k$", r"$r = b\sin\theta$", r"$2x^2 + y^2 = k$"],
        [r"A-2, B-1, C-4, D-3", r"A-2, B-1, C-3, D-4", r"A-1, B-2, C-4, D-3", r"A-2, B-4, C-1, D-3"],
        r"""- A: $p = \frac yx$; trajectories $\frac{dy}{dx} = -\frac xy$, so $x^2 + y^2 = k$.
- B: $p = -\frac yx$; trajectories $\frac{dy}{dx} = \frac xy$, so $x^2 - y^2 = k$.
- C: $2yp = c = \frac{y^2}{x}$, so $p = \frac{y}{2x}$; trajectories $y\,dy = -2x\,dx$, so $2x^2 + y^2 = k$.
- D: $\frac1r\frac{dr}{d\theta} = -\tan\theta$; then $r\frac{d\theta}{dr} = \tan\theta$, so $\frac{dr}{r} = \cot\theta\,d\theta$ and $r = b\sin\theta$.

The circles through the origin tangent to the $y$-axis are cut orthogonally by those tangent to the $x$-axis.""")

# ---------------------------------------------------------------- assertion-reason
# q26 (answer 0)
T.assertion_reason(2, ["clairaut", "singular-solutions"],
                   r"The equation $y = px + \dfrac1p$, where $p = \dfrac{dy}{dx}$, has the singular solution $y^2 = 4x$.",
                   r"The singular solution of Clairaut's equation $y = px + f(p)$ is the envelope of the family of lines $y = cx + f(c)$.",
                   0,
                   r"""**A is true.** From $x - \frac{1}{p^2} = 0$, $p = \frac{1}{\sqrt x}$, and $y = \sqrt x + \sqrt x = 2\sqrt x$, so $y^2 = 4x$.

**R is true** and it is exactly why A holds: $y = cx + \frac1c$ is the tangent of slope $c$ to the parabola $y^2 = 4x$, so the envelope of these lines is that parabola.""")

# q27 (answer 1)
T.assertion_reason(1, ["bernoulli", "linear-equations"],
                   r"$\dfrac{dy}{dx} + \dfrac{y}{x} = y^2$ $(x > 0)$ is a Bernoulli equation.",
                   r"Every first-order linear equation is a Bernoulli equation with $n = 0$.",
                   1,
                   r"""**A is true:** it has the form $y' + Py = Qy^n$ with $P = \frac1x$, $Q = 1$, $n = 2$.

**R is true:** with $n = 0$, $Qy^0 = Q$. But R is about $n = 0$, and A has $n = 2$, so R does not explain A.""")

# q28 (answer 2)
T.assertion_reason(2, ["singular-solutions", "higher-degree"],
                   r"The equation $y = px + p^2$, where $p = \dfrac{dy}{dx}$, has a singular solution.",
                   r"Every first-order equation of degree greater than one in $p$ has a singular solution.",
                   2,
                   r"""**A is true:** $x^2 + 4y = 0$ satisfies it and is not a member of $y = cx + c^2$.

**R is false.** $p^2 - 5p + 6 = 0$ has degree 2, but its $p$-discriminant $25 - 24 = 1$ never vanishes. Its solutions are only the lines $y = 2x + c$ and $y = 3x + c$, and there is no singular solution.""")

# q29 (answer 3)
T.assertion_reason(3, ["orthogonal-trajectories"],
                   r"The orthogonal trajectories of the family $y^2 = 4a(x + a)$ form a family different from the given one.",
                   r"In Cartesian coordinates, orthogonal trajectories are found by replacing $\dfrac{dy}{dx}$ by $-\dfrac{dx}{dy}$ in the differential equation of the family.",
                   3,
                   r"""**A is false.** The family's equation is $y = 2xp + yp^2$. Replace $p$ by $-\frac1p$: $y = -\frac{2x}{p} + \frac{y}{p^2}$. Multiplying by $p^2$ gives $yp^2 = -2xp + y$, i.e. $y = 2xp + yp^2$ again. The family (confocal parabolas) is **self-orthogonal**.

**R is true:** this is the standard rule, since slopes of perpendicular curves multiply to $-1$.""")

# q30 (answer 0)
T.assertion_reason(2, ["linear-equations", "singular-solutions"],
                   r"The linear equation $\dfrac{dy}{dx} + P(x)\,y = Q(x)$, with $P$ and $Q$ continuous on an interval $I$, has no singular solution on $I$.",
                   r"For such an equation there is exactly one solution through each point $(x_0, y_0)$ with $x_0 \in I$, and $y\,e^{\int P\,dx} = \int Qe^{\int P\,dx}\,dx + C$ gives all solutions.",
                   0,
                   r"""**R is true:** this is the existence and uniqueness theorem for linear equations. Every solution through $(x_0, y_0)$ is the member of the general solution with the matching $C$.

**A follows from R:** a singular solution would be a solution not in the family $y\mu = \int Q\mu + C$, and uniqueness rules that out. So both are true and R explains A.""")


def check():
    import sympy as sp
    x, y, p, c, k, C, a, b, t = sp.symbols("x y p c k C a b t")
    X = sp.symbols("x", positive=True)
    Y = sp.Function("y")

    def ode_ok(expr_y, lhs_minus_rhs, var=x, label=""):
        """expr_y: candidate y(var); lhs_minus_rhs: function of (y, y') that must vanish."""
        r = sp.simplify(lhs_minus_rhs(expr_y, sp.diff(expr_y, var)))
        eq(r, 0, label)

    def implicit_slope(phi):
        return sp.simplify(-sp.diff(phi, x) / sp.diff(phi, y))

    # q1: IF of y' - 2y/x = x^2
    mu = sp.exp(sp.integrate(-2 / X, X))
    eq(mu, 1 / X**2, "q1")
    ode_ok(X**3 + C * X**2, lambda f, fp: X * fp - 2 * f - X**3, X, "q1 sol")  # notes example
    # q2
    xs = sp.symbols("x")
    mu2 = sp.exp(sp.integrate(sp.tan(xs), xs))
    eq(sp.simplify(mu2 - 1 / sp.cos(xs)), 0, "q2")
    ode_ok(sp.sin(xs) + C * sp.cos(xs), lambda f, fp: fp + f * sp.tan(xs) - 1 / sp.cos(xs), xs, "q2 sol")
    # q3
    ode_ok(sp.exp(-x) + C * sp.exp(-2 * x), lambda f, fp: fp + 2 * f - sp.exp(-x), x, "q3")
    r = sp.simplify((lambda f: sp.diff(f, x) + 2 * f - sp.exp(-x))(-sp.exp(-x)))
    assert r != 0
    # q4
    ode_ok(X**2 / 4 + C / X**2, lambda f, fp: X * fp + 2 * f - X**2, X, "q4")
    assert sp.simplify(X * sp.diff(X**2 / 3, X) + 2 * X**2 / 3 - X**2) != 0
    # q5
    s5 = sp.dsolve(sp.Eq(Y(x).diff(x) + Y(x), 1), ics={Y(0): 0}).rhs
    eq(s5.subs(x, sp.log(2)), sp.Rational(1, 2), "q5")
    # q6: x as function of y: dx/dy = (x + y^2)/y
    yv = sp.symbols("y", positive=True)
    xf = yv**2 + C * yv
    eq(sp.diff(xf, yv) - (xf + yv**2) / yv, 0, "q6")
    xf_bad = yv**2 + C / yv
    assert sp.simplify(sp.diff(xf_bad, yv) - (xf_bad + yv**2) / yv) != 0
    # q7: Bernoulli n=3 -> v = y^(-2) gives linear eq
    v = Y(x) ** (-2)
    yp = -Y(x) / x + x * Y(x) ** 3
    dv = sp.diff(v, x).subs(Y(x).diff(x), yp)
    eq(sp.expand(dv - (2 / x) * v), -2 * x, "q7")
    # q8
    s8 = 1 / (x + 1 + C * sp.exp(x))
    ode_ok(s8, lambda f, fp: fp + f - x * f**2, x, "q8")
    s8b = 1 / (x + 1 + C * sp.exp(-x))
    assert sp.simplify(sp.diff(s8b, x) + s8b - x * s8b**2) != 0
    # q9
    s9 = sp.atan((x**2 - 1) / 2 + C * sp.exp(-x**2))
    ode_ok(s9, lambda f, fp: fp / sp.cos(f) ** 2 + 2 * x * sp.tan(f) - x**3, x, "q9")
    # q10
    eq(sp.factor(p**2 - (x + y) * p + x * y) - (p - x) * (p - y), 0, "q10 factor")
    ode_ok((x**2 + C) / 2, lambda f, fp: fp - x, x, "q10a")
    ode_ok(C * sp.exp(x), lambda f, fp: fp - f, x, "q10b")
    # q11: parametric x(p), y(p) must satisfy dy/dp = p dx/dp and the ODE
    xp = c / p**2 - 2 * p / 3
    yp_ = 2 * p * xp + p**2
    eq(sp.diff(yp_, p) - p * sp.diff(xp, p), 0, "q11")
    xb = c / p**2 + 2 * p / 3
    assert sp.simplify(sp.diff(2 * p * xb + p**2, p) - p * sp.diff(xb, p)) != 0
    # q12: p^2 + y^2 = 1
    F = p**2 + y**2 - 1
    pd = sp.solve([F, sp.diff(F, p)], [p, y], dict=True)
    assert {d[y] for d in pd} == {1, -1}
    ode_ok(sp.sin(x + C), lambda f, fp: fp**2 + f**2 - 1, x, "q12 general")
    ode_ok(sp.Integer(1), lambda f, fp: fp**2 + f**2 - 1, x, "q12 y=1")
    assert sp.simplify((lambda f, fp: fp**2 + f**2 - 1)(sp.Integer(0), sp.Integer(0))) != 0
    # q13
    ode_ok(c * x + c**2, lambda f, fp: f - fp * x - fp**2, x, "q13")
    # q14
    ode_ok(-x**2 / 4, lambda f, fp: f - fp * x - fp**2, x, "q14")
    assert sp.simplify((lambda f: f - sp.diff(f, x) * x - sp.diff(f, x) ** 2)(x**2 / 4)) != 0
    # q15
    ode_ok(X * sp.log(X) - X, lambda f, fp: f - fp * X + sp.exp(fp), X, "q15")
    ode_ok(c * X - sp.exp(c), lambda f, fp: f - fp * X + sp.exp(fp), X, "q15 general")
    assert sp.simplify((lambda f: f - sp.diff(f, X) * X + sp.exp(sp.diff(f, X)))(X * sp.log(X) + X)) != 0
    # q16: eliminate p; check ellipse
    A, B = sp.symbols("a b", positive=True)
    s = sp.sqrt(A**2 * p**2 + B**2)
    xs16 = -A**2 * p / s
    ys16 = p * xs16 + s
    eq(xs16**2 / A**2 + ys16**2 / B**2, 1, "q16")
    eq(xs16 + sp.diff(s, p), 0, "q16 x+f'(p)=0")
    # and the ellipse satisfies the ODE on its upper half
    ye = B * sp.sqrt(1 - X**2 / A**2)
    pe = sp.diff(ye, X)
    val = (ye - pe * X - sp.sqrt(A**2 * pe**2 + B**2)).subs({A: 2, B: 1, X: sp.Rational(-1, 2)})
    assert abs(sp.N(val)) < 1e-12
    # q17
    ycand = sp.sqrt(c * X**2 + c**2)
    pc = sp.diff(ycand, X)
    eq(sp.simplify(X**2 * (ycand - pc * X) - ycand * pc**2), 0, "q17")
    ybad = sp.sqrt(c * X**2 + c)
    pb = sp.diff(ybad, X)
    assert sp.simplify(X**2 * (ybad - pb * X) - ybad * pb**2) != 0
    # q18: product of slopes = -1
    fam = y - c * x**2
    m1 = implicit_slope(fam).subs(c, y / x**2)
    m2 = implicit_slope(x**2 + 2 * y**2 - k)
    eq(m1 * m2, -1, "q18")
    m2b = implicit_slope(2 * x**2 + y**2 - k)
    assert sp.simplify(m1 * m2b + 1) != 0
    # q19: polar: tan(psi) = r dtheta/dr = r / r'(theta); orthogonal iff r1'r2' + r1 r2 = 0 at same point? use tan psi1 * tan psi2 = -1
    th = sp.symbols("theta")
    r1 = a * (1 + sp.cos(th))
    r2 = b * (1 - sp.cos(th))
    tp1 = r1 / sp.diff(r1, th)
    tp2 = r2 / sp.diff(r2, th)
    eq(sp.simplify(tp1 * tp2), -1, "q19")
    r2b = b * (1 + sp.sin(th))
    assert sp.simplify(tp1 * r2b / sp.diff(r2b, th) + 1) != 0
    # q20: rule check with r = a cos(theta) -> r = b sin(theta)
    eq(sp.simplify((a * sp.cos(th) / sp.diff(a * sp.cos(th), th)) * (b * sp.sin(th) / sp.diff(b * sp.sin(th), th))), -1, "q20")
    # q21: statement 2 symbolic; statement 3 via sample
    n = sp.symbols("n")
    P_, Q_ = sp.Function("P")(x), sp.Function("Q")(x)
    yy = Y(x)
    vv = yy ** (1 - n)
    dvv = sp.diff(vv, x).subs(yy.diff(x), Q_ * yy**n - P_ * yy)
    eq(sp.simplify(dvv + (1 - n) * P_ * vv - (1 - n) * Q_), 0, "q21 s2")
    # s1: xy^2 nonlinear: second derivative wrt y nonzero
    assert sp.diff(x * y**2, y, 2) != 0
    # q22 s2 counterexample: x^2+4y=0 not of form y = cx + c^2
    # no constant c makes -x^2/4 - (cx + c^2) vanish identically (x^2 coefficient is -1/4)
    eq(sp.Poly(-x**2 / 4 - c * x - c**2, x).coeff_monomial(x**2), sp.Rational(-1, 4), "q22 s2")
    # q23
    pp = sp.Symbol("pp")
    E = y - 2 * x * pp - y * pp**2
    eq(sp.expand(E.subs(pp, -1 / pp) * pp**2), sp.expand(-E), "q23 s1")  # same equation up to sign
    # (also check y^2 = 4a(x+a) satisfies y = 2xp + yp^2)
    ya = sp.sqrt(4 * a * (X + a))
    eq(sp.simplify(ya - 2 * X * sp.diff(ya, X) - ya * sp.diff(ya, X) ** 2), 0, "q23 s1 ode")
    m1 = implicit_slope(x**2 + y**2 - 2 * c * x).subs(c, (x**2 + y**2) / (2 * x))
    m2 = implicit_slope(x**2 + y**2 - 2 * k * y).subs(k, (x**2 + y**2) / (2 * y))
    eq(m1 * m2, -1, "q23 s2")
    m1 = implicit_slope(y - c * sp.exp(x)).subs(c, y * sp.exp(-x))
    m_bad = implicit_slope(y - k * sp.exp(-x)).subs(k, y * sp.exp(x))
    assert sp.simplify(m1 * m_bad + 1) != 0
    m_good = implicit_slope(y**2 - k + 2 * x)
    eq(m1 * m_good, -1, "q23 s3")
    # q24
    xs_ = sp.symbols("x", positive=True)
    eq(sp.exp(sp.integrate(1 / xs_, xs_)), xs_, "q24 A")
    eq(sp.exp(sp.integrate(-1 / xs_, xs_)), 1 / xs_, "q24 B")
    eq(sp.simplify(sp.exp(sp.integrate(sp.cot(xs), xs)) - sp.sin(xs)), 0, "q24 C")
    eq(sp.exp(sp.integrate(2 * xs, xs)), sp.exp(xs**2), "q24 D")
    # q25
    pairs = [(y - c * x, x**2 + y**2 - k, c, y / x, k),
             (x * y - c, x**2 - y**2 - k, c, x * y, k),
             (y**2 - c * x, 2 * x**2 + y**2 - k, c, y**2 / x, k)]
    for i, (f1, f2, cc, cval, kk) in enumerate(pairs):
        eq(implicit_slope(f1).subs(cc, cval) * implicit_slope(f2), -1, f"q25 {i}")
    eq(sp.simplify((a * sp.cos(th) / sp.diff(a * sp.cos(th), th)) * (b * sp.sin(th) / sp.diff(b * sp.sin(th), th))), -1, "q25 D")
    # q26
    ode_ok(2 * sp.sqrt(X), lambda f, fp: f - fp * X - 1 / fp, X, "q26")
    ode_ok(c * X + 1 / c, lambda f, fp: f - fp * X - 1 / fp, X, "q26 general")
    # q27: Bernoulli n = 2 with v = 1/y gives linear
    s27 = sp.dsolve(sp.Eq(Y(X).diff(X) + Y(X) / X, Y(X) ** 2))
    assert sp.checkodesol(sp.Eq(Y(X).diff(X) + Y(X) / X, Y(X) ** 2), s27)[0]
    # q28: p-discriminant of p^2 - 5p + 6 is constant 1
    eq(sp.discriminant(p**2 - 5 * p + 6, p), 1, "q28")
    ode_ok(-x**2 / 4, lambda f, fp: f - fp * x - fp**2, x, "q28 A")
    # q29: covered by q23 s1
    # q30: uniqueness illustrated: dsolve of a linear IVP gives one solution
    s30 = sp.dsolve(sp.Eq(Y(x).diff(x) + 2 * Y(x), sp.exp(-x)), ics={Y(0): 3})
    eq(s30.rhs, sp.exp(-x) + 2 * sp.exp(-2 * x), "q30")


T.write(check)
