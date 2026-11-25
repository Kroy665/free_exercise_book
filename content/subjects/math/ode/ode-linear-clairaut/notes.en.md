# Linear, Bernoulli and Clairaut Equations

Throughout, $p = \dfrac{dy}{dx}$. Separable, homogeneous and exact equations are in *First-Order Equations*; higher-order linear equations are in *Higher-Order Linear Equations*.

## Linear equations and the integrating factor {#linear-equations}

A first-order equation is **linear in $y$** if it can be written

$$\frac{dy}{dx} + P(x)\,y = Q(x).$$

$y$ and $y'$ appear only to the first power, and are not multiplied together or inside other functions.

:::keyfacts
- **Integrating factor (IF):** $\mu(x) = e^{\int P\,dx}$. Multiplying by $\mu$ turns the left side into $\dfrac{d}{dx}(\mu y)$.
- **Solution:** $$y\cdot \mu = \int Q\,\mu\,dx + C.$$
- **Existence and uniqueness:** if $P$ and $Q$ are continuous on an interval $I$, then for every $x_0 \in I$ and every $y_0$ there is exactly one solution on all of $I$ with $y(x_0) = y_0$. So the formula above gives **every** solution, and a linear equation has **no singular solution**.
:::

**Write the equation in standard form first.** The coefficient of $y'$ must be $1$. For $x y' - 2y = x^3$ ($x > 0$), divide by $x$: $P = -\dfrac2x$, so

$$\mu = e^{-2\ln x} = \frac{1}{x^2}, \qquad \frac{y}{x^2} = \int x^2\cdot\frac{1}{x^2}\,dx = x + C, \qquad y = x^3 + Cx^2.$$

Common integrating factors:

| $P(x)$ | IF $e^{\int P\,dx}$ |
|:---|:---|
| $\dfrac{k}{x}$ | $x^k$ (on $x > 0$) |
| $\tan x$ | $\sec x$ |
| $\cot x$ | $\sin x$ |
| $2x$ | $e^{x^2}$ |
| constant $a$ | $e^{ax}$ |

**Example.** $y' + y\tan x = \sec x$ on $(-\pi/2, \pi/2)$: IF $= \sec x$, and
$$y\sec x = \int \sec^2 x\,dx = \tan x + C \implies y = \sin x + C\cos x.$$

**Linear in $x$.** Sometimes the equation is linear when $x$ is taken as the dependent variable:

$$\frac{dx}{dy} + P(y)\,x = Q(y), \qquad x\,e^{\int P\,dy} = \int Q\,e^{\int P\,dy}\,dy + C.$$

For $y\,dx = (x + y^2)\,dy$: $\dfrac{dx}{dy} - \dfrac{x}{y} = y$, IF $= \dfrac1y$, so $\dfrac{x}{y} = y + C$, i.e. $x = y^2 + Cy$.

:::caution
The IF is $e^{\int P\,dx}$, **not** $e^{\int Q\,dx}$, and the sign of $P$ is taken from the standard form $y' + Py = Q$. For $y' - \frac{y}{x} = x$, $P = -\frac1x$ and the IF is $\frac1x$, not $x$.
:::

:::exam-tip
Check a candidate solution by substitution: it is quicker than solving. For $y' + 2y = e^{-x}$, try $y = e^{-x}$: $-e^{-x} + 2e^{-x} = e^{-x}$. So $y = e^{-x} + Ce^{-2x}$.
:::

## Bernoulli and other reducible equations {#bernoulli}

**Bernoulli's equation:**

$$\frac{dy}{dx} + P(x)\,y = Q(x)\,y^n, \qquad n \ne 0, 1.$$

(For $n = 0$ it is already linear; for $n = 1$ it is linear and separable.) Divide by $y^n$ and put $v = y^{1-n}$, so $v' = (1-n)y^{-n}y'$:

$$\frac{dv}{dx} + (1-n)P\,v = (1-n)\,Q.$$

This is linear in $v$.

| Equation | $n$ | Substitution |
|:---|:---:|:---|
| $y' + Py = Qy^2$ | 2 | $v = 1/y$ |
| $y' + Py = Qy^3$ | 3 | $v = 1/y^2$ |
| $y' + Py = Q\sqrt y$ | $\tfrac12$ | $v = \sqrt y$ |

**Example.** $y' + y = x y^2$. Put $v = \dfrac1y$, so $v' = -\dfrac{y'}{y^2}$. Dividing by $-y^2$:
$$v' - v = -x, \qquad \text{IF } e^{-x}, \qquad v e^{-x} = \int -x e^{-x}\,dx = (x + 1)e^{-x} + C.$$
So $\dfrac1y = x + 1 + Ce^{x}$. Also $y = 0$ is a solution (lost on dividing by $y^2$).

**General reduction.** If the equation has the form

$$f'(y)\,\frac{dy}{dx} + P(x)\,f(y) = Q(x),$$

put $v = f(y)$: it becomes $v' + Pv = Q$. Bernoulli is the case $f(y) = y^{1-n}$.

**Example.** $\sec^2 y\,y' + 2x\tan y = x^3$. With $v = \tan y$: $v' + 2xv = x^3$, IF $e^{x^2}$,
$$v e^{x^2} = \int x^3 e^{x^2}\,dx = \tfrac12(x^2 - 1)e^{x^2} + C \implies \tan y = \tfrac12(x^2 - 1) + Ce^{-x^2}.$$

(Substitute $t = x^2$ in the integral: $\tfrac12\int t e^t\,dt = \tfrac12(t - 1)e^t$.)

:::caution
After $v = y^{1-n}$, **both** $P$ and $Q$ are multiplied by $(1 - n)$. Forgetting the factor on one side is the commonest slip. For $n = 2$ the factor is $-1$, which flips signs.
:::

:::exam-tip
Recognise the substitution from the exponent alone: for $y' + \frac{y}{x} = xy^3$, $v = y^{1-3} = y^{-2}$.
:::

## First-order equations of higher degree {#higher-degree}

An equation $F(x, y, p) = 0$ of degree $n > 1$ in $p$ is solved in one of three ways.

**1. Solvable for $p$.** Factorise into $(p - f_1)(p - f_2)\cdots(p - f_n) = 0$, solve each first-degree factor as $\phi_k(x, y, c) = 0$, and write the general solution as the product

$$\phi_1(x, y, c)\,\phi_2(x, y, c)\cdots\phi_n(x, y, c) = 0,$$

with **one** constant $c$ (the equation is still first order).

Example: $p^2 - (x + y)p + xy = 0$ factorises as $(p - x)(p - y) = 0$. So $p = x$ gives $2y = x^2 + c$, and $p = y$ gives $y = ce^x$. The general solution is $(2y - x^2 - c)(y - ce^x) = 0$.

**2. Solvable for $y$:** $y = f(x, p)$. Differentiate with respect to $x$:
$$p = \frac{\partial f}{\partial x} + \frac{\partial f}{\partial p}\,\frac{dp}{dx}.$$
This is a first-order equation in $x$ and $p$. Solve it as $\psi(x, p, c) = 0$, then eliminate $p$ (or keep $x, y$ in terms of the parameter $p$).

The important case is **Lagrange's (d'Alembert's) equation** $y = x\,\phi(p) + \psi(p)$. Differentiating gives an equation that is **linear in $x$ as a function of $p$**.

Example: $y = 2px + p^2$. Differentiating:
$$p = 2p + (2x + 2p)\frac{dp}{dx} \implies \frac{dx}{dp} + \frac{2}{p}\,x = -2.$$
IF $= p^2$, so $xp^2 = -\tfrac23 p^3 + c$. The solution in parametric form is
$$x = \frac{c}{p^2} - \frac{2p}{3}, \qquad y = 2px + p^2.$$

**3. Solvable for $x$:** $x = f(y, p)$. Differentiate with respect to $y$ and use $\dfrac{dx}{dy} = \dfrac1p$:
$$\frac1p = \frac{\partial f}{\partial y} + \frac{\partial f}{\partial p}\,\frac{dp}{dy}.$$
Solve for $p$ in terms of $y$, then eliminate $p$. Example: $x = y + p^2$ gives $\frac1p = 1 + 2p\frac{dp}{dy}$, which is separable in $p$ and $y$.

:::caution
A first-order equation has **one** arbitrary constant, whatever its degree. Writing $(2y - x^2 - c_1)(y - c_2e^x) = 0$ with two constants is wrong in form.
:::

## Clairaut's equation {#clairaut}

**Clairaut's equation** is

$$y = px + f(p).$$

Differentiate with respect to $x$:
$$p = p + x\frac{dp}{dx} + f'(p)\frac{dp}{dx} \implies \big(x + f'(p)\big)\frac{dp}{dx} = 0.$$

:::keyfacts
- $\dfrac{dp}{dx} = 0$ gives $p = c$ and the **general solution** $y = cx + f(c)$: a one-parameter family of **straight lines**. Just replace $p$ by $c$.
- $x + f'(p) = 0$, with $y = px + f(p)$, gives the **singular solution** in parametric form. Eliminating $p$ gives the **envelope** of the family of lines.
:::

| Equation | General solution | Singular solution |
|:---|:---|:---|
| $y = px + p^2$ | $y = cx + c^2$ | $x^2 + 4y = 0$ |
| $y = px + \dfrac{a}{p}$ | $y = cx + \dfrac{a}{c}$ | $y^2 = 4ax$ |
| $y = px + \sqrt{a^2p^2 + b^2}$ | $y = cx + \sqrt{a^2c^2 + b^2}$ | $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$ |
| $y = px - e^{p}$ | $y = cx - e^{c}$ | $y = x\ln x - x$ |
| $y = px + a\sqrt{1 + p^2}$ | $y = cx + a\sqrt{1 + c^2}$ | $x^2 + y^2 = a^2$ |

Worked: for $y = px + \dfrac ap$, $x - \dfrac{a}{p^2} = 0$ gives $p^2 = \dfrac ax$, and then $y = 2\sqrt{ax}$, so $y^2 = 4ax$. Geometrically, $y = cx + \frac ac$ is the tangent of slope $c$ to the parabola $y^2 = 4ax$.

```plot
title: The lines $y = cx + 1/c$ (Clairaut, $f(p) = 1/p$) and their envelope $y^2 = 4x$
x: -1, 6
y: -6, 6
f: 2sqrt(x) | envelope $y^2 = 4x$
f: -2sqrt(x)
f: 0.5x + 2 | $c = 1/2$
f: x + 1 | $c = 1$
f: 2x + 0.5 | $c = 2$
f: -x - 1 | $c = -1$
```

**Reducible to Clairaut form.** A substitution can turn an equation into Clairaut form. With $X = x^2$, $Y = y^2$, we have $P = \dfrac{dY}{dX} = \dfrac{yp}{x}$. For example, $x^2(y - px) = yp^2$ becomes $Y = PX + P^2$. So the general solution is $y^2 = cx^2 + c^2$. Another standard substitution is $X = e^x$, $Y = e^y$. In each case the aim is an equation of the form $Y = PX + f(P)$.

:::exam-tip
To get the singular solution of $y = px + f(p)$ quickly: solve $x = -f'(p)$ for $p$, substitute into $y = px + f(p)$. For $y = px + p^2$: $p = -\frac x2$, so $y = -\frac{x^2}{2} + \frac{x^2}{4} = -\frac{x^2}{4}$.
:::

## Singular solutions and discriminants {#singular-solutions}

A **singular solution** of $F(x, y, p) = 0$ satisfies the equation but is **not** obtained from the general solution $\phi(x, y, c) = 0$ by any choice of $c$. Geometrically, it is usually the **envelope** of the family of solution curves. At each of its points it touches some member of the family, and so it has the same $x, y, p$.

**Two discriminants.**

- **$c$-discriminant:** eliminate $c$ from $\phi = 0$ and $\dfrac{\partial\phi}{\partial c} = 0$.
- **$p$-discriminant:** eliminate $p$ from $F = 0$ and $\dfrac{\partial F}{\partial p} = 0$. If $F$ is quadratic in $p$, $Ap^2 + Bp + C = 0$, this is just $B^2 - 4AC = 0$.

Besides the envelope $E$, these loci can contain:

| Locus | What it is | In $p$-disc. | In $c$-disc. | Solution? |
|:---|:---|:---:|:---:|:---:|
| Envelope $E$ | touches every curve of the family | $E$ | $E$ | **yes** |
| Tac-locus $T$ | where two non-consecutive curves touch | $T^2$ | no | no (in general) |
| Node locus $N$ | locus of nodes (double points) | no | $N^2$ | no |
| Cusp locus $C$ | locus of cusps | $C$ | $C^3$ | no (in general) |

So, schematically, the **$p$-discriminant is $E\,T^2\,C = 0$** and the **$c$-discriminant is $E\,N^2\,C^3 = 0$**. The envelope appears **once in both**. Always confirm a candidate by substituting it into the differential equation.

**Example.** $p^2 + y^2 = 1$. Solving for $p$: $\dfrac{dy}{\sqrt{1 - y^2}} = \pm dx$, so $y = \sin(x + c)$.

- $p$-discriminant: $\partial F/\partial p = 2p = 0$, so $y^2 = 1$.
- $c$-discriminant: from $y = \sin(x + c)$ and $\cos(x + c) = 0$, also $y = \pm1$.
- Check: $y = \pm1$ gives $p = 0$ and $0 + 1 = 1$, so it satisfies the equation. No $c$ gives $\sin(x + c) \equiv 1$, so $y = \pm1$ is singular. The lines $y = \pm 1$ touch every sine curve at its crests.

**Example (no singular solution).** $p^2 - 5p + 6 = 0$ has $B^2 - 4AC = 25 - 24 = 1 \ne 0$, so there is no $p$-discriminant locus at all. Its solutions are the two families of lines $y = 2x + c$ and $y = 3x + c$.

:::caution
A singular solution is **not** a particular solution: particular solutions come from fixing $c$, while singular solutions cannot. Also, not every point of a discriminant locus is a solution. Node, tac and cusp loci must be rejected by substitution.
:::

## Orthogonal trajectories {#orthogonal-trajectories}

Curves that cut every member of a given family at right angles are its **orthogonal trajectories**.

**Cartesian method.**
1. Form the differential equation $F(x, y, p) = 0$ of the family by eliminating the parameter.
2. Replace $p$ by $-\dfrac1p$ (i.e. $\dfrac{dy}{dx}$ by $-\dfrac{dx}{dy}$).
3. Solve the new equation.

**Polar method.** The angle $\psi$ between the radius vector and the tangent satisfies $\tan\psi = r\dfrac{d\theta}{dr}$. Form the polar equation $F\!\left(r, \theta, \dfrac{dr}{d\theta}\right) = 0$, then replace $\dfrac{dr}{d\theta}$ by $-r^2\dfrac{d\theta}{dr}$. Equivalently, replace $r\dfrac{d\theta}{dr}$ by $-\dfrac1r\dfrac{dr}{d\theta}$.

**Example (Cartesian).** $y = cx^2$: $p = 2cx = \dfrac{2y}{x}$. The trajectories satisfy $-\dfrac{1}{p} = \dfrac{2y}{x}$, so $2y\,dy = -x\,dx$, i.e.
$$x^2 + 2y^2 = k \quad\text{(ellipses)}.$$

**Example (polar).** For the cardioids $r = a(1 + \cos\theta)$: $\dfrac1r\dfrac{dr}{d\theta} = \dfrac{-\sin\theta}{1 + \cos\theta} = -\tan\dfrac\theta2$. Replacing $\dfrac1r\dfrac{dr}{d\theta}$ by $-r\dfrac{d\theta}{dr}$:
$$r\frac{d\theta}{dr} = \tan\frac\theta2 \implies \frac{dr}{r} = \cot\frac\theta2\,d\theta \implies r = b\sin^2\frac\theta2,$$
i.e. $r = b(1 - \cos\theta)$, the cardioids facing the other way.

| Family | Orthogonal trajectories |
|:---|:---|
| $y = cx$ | $x^2 + y^2 = k$ |
| $xy = c$ | $x^2 - y^2 = k$ |
| $y = cx^2$ | $x^2 + 2y^2 = k$ |
| $y^2 = cx$ | $2x^2 + y^2 = k$ |
| $y = ce^x$ | $y^2 = k - 2x$ |
| $x^2 + y^2 = 2cx$ | $x^2 + y^2 = 2ky$ |
| $r = a\cos\theta$ | $r = b\sin\theta$ |
| $r = a(1 + \cos\theta)$ | $r = b(1 - \cos\theta)$ |
| $r^n = a^n\cos n\theta$ | $r^n = b^n\sin n\theta$ |

A family is **self-orthogonal** if its trajectories are the family itself. The standard example is the confocal parabolas $y^2 = 4a(x + a)$. Their equation is $y = 2xp + yp^2$, and this is unchanged when $p$ is replaced by $-1/p$.

```plot
title: Parabolas $y = cx^2$ and their orthogonal trajectories $x^2 + 2y^2 = k$
x: -3, 3
y: -2.5, 2.5
equal: true
f: x^2 | $y = cx^2$
f: -x^2
f: 0.3x^2
f: -0.3x^2
implicit: x^2 + 2y^2 = 1 | $x^2 + 2y^2 = k$
implicit: x^2 + 2y^2 = 4
implicit: x^2 + 2y^2 = 8
```

:::caution
Eliminate the parameter **before** replacing $p$. If $c$ is still present, the "trajectories" will depend on the curve chosen and the answer is wrong.
:::

## Quick checks and traps {#exam-tips}

- **IF sign:** in $y' + Py = Q$, the IF is $e^{+\int P}$. $P = -\frac{2}{x}$ gives $\frac{1}{x^2}$, not $x^2$.
- **Check by substitution:** any proposed solution of a linear equation can be checked in seconds; the arbitrary-constant part must solve $y' + Py = 0$.
- **Bernoulli:** $v = y^{1-n}$; then both $P$ and $Q$ are multiplied by $(1 - n)$.
- **Clairaut:** general solution = replace $p$ by $c$. Singular solution = eliminate $p$ from $y = px + f(p)$ and $x + f'(p) = 0$.
- **Discriminants:** $p$-disc. $= E\,T^2C$, $c$-disc. $= E\,N^2C^3$. The envelope appears in both, once. Only loci that satisfy the equation are singular solutions.
- **Linear equations have no singular solution**, because of uniqueness.
- **Orthogonal trajectories:** Cartesian $p \to -1/p$; polar $\dfrac{dr}{d\theta} \to -r^2\dfrac{d\theta}{dr}$. Self-orthogonal: $y^2 = 4a(x + a)$.
- **Degree vs constants:** a first-order equation of any degree has a general solution with exactly one constant.
