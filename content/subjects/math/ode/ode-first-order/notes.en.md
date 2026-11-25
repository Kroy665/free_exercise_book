# First-Order Equations

## Order, degree and solutions {#order-degree}

An **ordinary differential equation (ODE)** relates an unknown function $y(x)$, the variable $x$ and finitely many derivatives $y', y'', \dots$.

- **Order:** the order of the highest derivative present.
- **Degree:** the power of the highest-order derivative, **after** the equation has been made a polynomial in all the derivatives (clear radicals and fractions in $y', y'', \dots$). If it cannot be made polynomial in the derivatives (e.g. $\sin y'$, $e^{y''}$, $\ln y'$ appear), the degree is **not defined**.
- **Linear:** $y$ and its derivatives occur only to the first power, not multiplied together, with coefficients depending on $x$ only. Example: $y'' + x^2y = \sin x$ is linear; $yy'' = 1$, $y'' + \sin y = 0$ and $(y')^2 = y$ are not.

| Equation | Order | Degree |
|:---|:---:|:---:|
| $\left(1 + y'^2\right)^{3/2} = y''$ | 2 | 2 (square both sides) |
| $\left(y'''\right)^{2/3} = y'$ | 3 | 2 (cube: $y'''^2 = y'^3$) |
| $y = xy' + \dfrac{a}{y'}$ | 1 | 2 (multiply by $y'$) |
| $y'' + \sin y' = 0$ | 2 | not defined |
| $y' = e^{x + y}$ | 1 | 1 (only $y$ is inside $\exp$) |

**Solutions.** A **general solution** of an $n$th-order equation contains $n$ independent (essential) arbitrary constants. A **particular solution** fixes the constants, usually by initial conditions. A **singular solution** satisfies the equation but is not obtained from the general solution for any value of the constant (treated with Clairaut's equation in `math.ode.ode-linear-clairaut`).

**Geometric meaning.** $y' = f(x,y)$ assigns a slope to each point of the plane (a **direction field**). A solution is a curve tangent to the field at every point; the general solution is a one-parameter family of such curves.

:::caution
Degree is read only **after** removing radicals. $\left(1 + y'^2\right)^{3/2} = y''$ has degree 2, not $1$ or $\tfrac32$. Degree is always a positive integer, never a fraction.
:::

## Formation by eliminating constants {#formation}

A family with $n$ **essential** arbitrary constants gives an ODE of **order $n$**:

1. Differentiate the relation $n$ times.
2. Eliminate the $n$ constants between the $n + 1$ equations.

Constants are essential only if they cannot be merged. $y = (A + B)e^{x + C} = Ke^x$ has just one essential constant, so its equation is $y' = y$, of order 1.

**Examples.**

- $y = Ae^{2x} + Be^{-2x}$: $y'' = 4Ae^{2x} + 4Be^{-2x} = 4y$, so $y'' - 4y = 0$.
- $y = A\cos x + B\sin x$: $y'' + y = 0$.
- All non-vertical lines $y = mx + c$: $y'' = 0$ (order 2, not $y' = 0$).
- Circles through the origin with centres on the $x$-axis, $x^2 + y^2 = 2ax$. Differentiate: $x + yy' = a$. Eliminate $a$:
  $$x^2 + y^2 = 2x(x + yy') \;\Rightarrow\; 2xy\,y' = y^2 - x^2.$$
- All circles of a fixed radius $r$, $(x - h)^2 + (y - k)^2 = r^2$ (two constants):
  $$\left(1 + y'^2\right)^3 = r^2\,y''^2 \qquad \text{(order 2, degree 2).}$$
- All circles in the plane (three constants): order 3.

| Family | Essential constants | Order of ODE |
|:---|:---:|:---:|
| lines through the origin | 1 | 1 |
| all lines | 2 | 2 |
| circles of fixed radius | 2 | 2 |
| all circles | 3 | 3 |
| parabolas $y = ax^2 + bx + c$ | 3 | 3 |

:::exam-tip
To check a candidate ODE quickly, substitute one member of the family. For $2xyy' = y^2 - x^2$, take the circle $x^2 + y^2 = 2x$ at $(1, 1)$: there $y' = 0$, and indeed $y^2 - x^2 = 0$.
:::

## Existence and uniqueness {#existence}

:::keyfacts
- **Peano (existence).** If $f$ is continuous on a rectangle $R$ around $(x_0, y_0)$, then $y' = f(x,y)$, $y(x_0) = y_0$ has **at least one** solution near $x_0$.
- **Picard (existence and uniqueness).** Let $f$ be continuous on $R = \{\lvert x - x_0\rvert \le a,\ \lvert y - y_0\rvert \le b\}$, with $\lvert f\rvert \le K$ there, and let $f$ satisfy a **Lipschitz condition in $y$** on $R$: $\lvert f(x, y_1) - f(x, y_2)\rvert \le L\lvert y_1 - y_2\rvert$. Then the IVP has a **unique** solution on $\lvert x - x_0\rvert \le h$, where $h = \min(a, b/K)$.
- A convenient sufficient condition for the Lipschitz condition: $\partial f/\partial y$ is continuous (hence bounded) on $R$.
:::

The theorem is **local**: it promises a solution only on a small interval, even when $f$ is very smooth. For $y' = y^2$, $y(0) = 1$:
$$\frac{dy}{y^2} = dx \;\Rightarrow\; -\frac1y = x - 1 \;\Rightarrow\; y = \frac{1}{1 - x},$$
which blows up at $x = 1$. The maximal interval containing $0$ is $(-\infty, 1)$.

**Failure of uniqueness.** For $y' = 3y^{2/3}$, $y(0) = 0$, the function $f$ is continuous but $\partial f/\partial y = 2y^{-1/3}$ is unbounded near $y = 0$, and $f$ is not Lipschitz there. Both $y = 0$ and $y = x^3$ are solutions, and so is every function that stays $0$ up to some $c \ge 0$ and equals $(x - c)^3$ after it.

```plot
title: Many solutions of $y' = 3y^{2/3}$ through the origin
x: -1.5, 2.5
y: -1.5, 3
f: x^3 | $y = x^3$
f: 0 | $y = 0$
f: max(0, x - 1)^3 | $y = 0$, then $(x - 1)^3$
point: 0, 0 | $(0, 0)$
```

:::caution
Continuity of $f$ alone gives existence, **not** uniqueness. Lipschitz (or continuous $f_y$) is sufficient for uniqueness, not necessary.
:::

## Variables separable {#separable}

The equation $\dfrac{dy}{dx} = g(x)\,h(y)$ separates as
$$\int\frac{dy}{h(y)} = \int g(x)\,dx + C \qquad (h(y) \ne 0).$$
If $h(y_0) = 0$, then the constant $y = y_0$ is also a solution; dividing by $h(y)$ may lose it.

**Example 1.** $\dfrac{dy}{dx} = \dfrac{1 + y^2}{1 + x^2}$ gives $\tan^{-1}y = \tan^{-1}x + C$, i.e. $\dfrac{y - x}{1 + xy} = k$.

**Example 2.** $\dfrac{dy}{dx} = e^{x + y}$, $y(0) = 0$: $e^{-y}dy = e^x dx$, so $-e^{-y} = e^x + C$. At $(0, 0)$, $C = -2$:
$$e^{-y} = 2 - e^x, \qquad y = -\ln(2 - e^x) \quad (x < \ln 2).$$

**Example 3.** $e^x\tan y\,dx + (1 - e^x)\sec^2 y\,dy = 0$. Divide by $(1 - e^x)\tan y$:
$$\frac{e^x}{1 - e^x}dx + \frac{\sec^2 y}{\tan y}dy = 0 \;\Rightarrow\; \tan y = C(1 - e^x).$$

**Reducible to separable: $y' = f(ax + by + c)$.** Put $v = ax + by + c$. Then $v' = a + b f(v)$, which is separable.

For $y' = (x + y + 1)^2$, let $v = x + y + 1$: $v' = 1 + v^2$, so
$$\tan^{-1}(x + y + 1) = x + C, \quad\text{i.e.}\quad y = \tan(x + C) - x - 1.$$

:::caution
Write the constant where the integration produces it. $\tan^{-1}v = x + C$ gives $v = \tan(x + C)$, **not** $v = \tan x + C$.
:::

## Homogeneous equations {#homogeneous}

$f(x, y)$ is **homogeneous of degree $n$** if $f(tx, ty) = t^n f(x, y)$. The equation $M\,dx + N\,dy = 0$ is **homogeneous** if $M$ and $N$ are homogeneous of the **same** degree; equivalently, $\frac{dy}{dx} = F\!\left(\frac{y}{x}\right)$.

**Method.** Put $y = vx$, $\frac{dy}{dx} = v + x\frac{dv}{dx}$. Then
$$x\frac{dv}{dx} = F(v) - v \;\Rightarrow\; \int\frac{dv}{F(v) - v} = \ln\lvert x\rvert + C.$$

**Example 1.** $(x^2 + y^2)\,dx - 2xy\,dy = 0$. Here $F(v) = \frac{1 + v^2}{2v}$, so $F(v) - v = \frac{1 - v^2}{2v}$:
$$\int\frac{2v\,dv}{1 - v^2} = \ln\lvert x\rvert + c \;\Rightarrow\; x(1 - v^2) = C \;\Rightarrow\; x^2 - y^2 = Cx.$$

**Example 2.** $\frac{dy}{dx} = \frac{y}{x} + \tan\frac{y}{x}$: $x v' = \tan v$, so $\int\cot v\,dv = \ln\lvert x\rvert + c$, giving $\sin\frac{y}{x} = Cx$.

### Reducible to homogeneous

For
$$\frac{dy}{dx} = \frac{a_1x + b_1y + c_1}{a_2x + b_2y + c_2}:$$

| Case | Substitution | Result |
|:---|:---|:---|
| $a_1b_2 - a_2b_1 \ne 0$ (lines meet at $(h, k)$) | $x = X + h,\ y = Y + k$ | homogeneous in $X, Y$ |
| $a_1b_2 - a_2b_1 = 0$ (parallel lines) | $z = a_1x + b_1y$ | separable in $x, z$ |

**Example 3.** $\frac{dy}{dx} = \frac{x + 2y - 3}{2x + y - 3}$. The lines $x + 2y = 3$ and $2x + y = 3$ meet at $(1, 1)$. Put $x = X + 1$, $y = Y + 1$: $\frac{dY}{dX} = \frac{X + 2Y}{2X + Y}$.

**Example 4.** $\frac{dy}{dx} = \frac{x + y + 1}{2x + 2y + 3}$. The lines are parallel; put $z = x + y$:
$$\frac{dz}{dx} = 1 + \frac{z + 1}{2z + 3} = \frac{3z + 4}{2z + 3}, \qquad \int\left(\frac23 + \frac{1/3}{3z + 4}\right)dz = x + c.$$
So $6z + \ln\lvert 3z + 4\rvert = 9x + C$, i.e. $6y - 3x + \ln\lvert 3x + 3y + 4\rvert = C$.

:::exam-tip
Test homogeneity in one line: replace $x, y$ by $tx, ty$. Constant terms (like the $+1$ in $x + y + 1$) destroy it; then look for a shift of origin.
:::

## Exact equations {#exact}

$M\,dx + N\,dy = 0$ is **exact** if $M\,dx + N\,dy = du$ for some $u(x, y)$; its solution is then $u(x, y) = C$.

:::keyfacts
- **Test.** Let $M, N, \partial M/\partial y, \partial N/\partial x$ be continuous on a rectangle (more generally, a simply connected region). Then the equation is exact **if and only if** $\dfrac{\partial M}{\partial y} = \dfrac{\partial N}{\partial x}$.
- **Solution.** $\displaystyle\int M\,dx\ (\text{treating } y \text{ as constant}) + \int(\text{terms of } N \text{ not containing } x)\,dy = C.$
:::

**Example 1.** $(2xy + e^x)\,dx + (x^2 + \cos y)\,dy = 0$. Here $M_y = 2x = N_x$. Then $\int M\,dx = x^2y + e^x$; the term of $N$ free of $x$ is $\cos y$, giving $\sin y$:
$$x^2y + e^x + \sin y = C.$$
Do **not** integrate the $x^2$ of $N$ again; it is already in $x^2y$.

**Example 2.** $(ye^{xy} + 2x)\,dx + (xe^{xy} - 2y)\,dy = 0$, $y(0) = 1$. It is exact, with $u = e^{xy} + x^2 - y^2$. At $(0, 1)$, $u = 1 + 0 - 1 = 0$, so the solution is $e^{xy} + x^2 - y^2 = 0$.

**Standard exact differentials** (useful for solving by inspection):

| Expression | Exact differential of |
|:---|:---|
| $x\,dy + y\,dx$ | $xy$ |
| $\dfrac{x\,dy - y\,dx}{x^2}$ | $\dfrac{y}{x}$ |
| $\dfrac{y\,dx - x\,dy}{y^2}$ | $\dfrac{x}{y}$ |
| $\dfrac{x\,dy - y\,dx}{xy}$ | $\ln\left\lvert\dfrac{y}{x}\right\rvert$ |
| $\dfrac{x\,dy - y\,dx}{x^2 + y^2}$ | $\tan^{-1}\dfrac{y}{x}$ |
| $\dfrac{x\,dx + y\,dy}{x^2 + y^2}$ | $\tfrac12\ln(x^2 + y^2)$ |

:::caution
Keep the order: $\partial M/\partial y$ against $\partial N/\partial x$. $y\,dx - x\,dy = 0$ is **not** exact ($M_y = 1$, $N_x = -1$), but $y\,dx + x\,dy = 0$ is. Homogeneous does not imply exact.
:::

## Integrating factors {#integrating-factors}

$\mu(x, y) \ne 0$ is an **integrating factor (IF)** of $M\,dx + N\,dy = 0$ if $\mu M\,dx + \mu N\,dy = 0$ is exact. IFs are never unique: if $\mu$ is an IF and the solution is $u = C$, then $\mu\,g(u)$ is also an IF for any differentiable $g$. For example, $\frac{1}{x^2}$, $\frac{1}{y^2}$, $\frac{1}{xy}$ and $\frac{1}{x^2 + y^2}$ are all IFs of $y\,dx - x\,dy = 0$, but $\frac{1}{xy^2}$ is not.

**Standard rules.**

| Condition | Integrating factor |
|:---|:---|
| homogeneous, $Mx + Ny \ne 0$ | $\dfrac{1}{Mx + Ny}$ |
| $M = y f_1(xy)$, $N = x f_2(xy)$, $Mx - Ny \ne 0$ | $\dfrac{1}{Mx - Ny}$ |
| $\dfrac{M_y - N_x}{N} = f(x)$ alone | $e^{\int f(x)\,dx}$ |
| $\dfrac{N_x - M_y}{M} = g(y)$ alone | $e^{\int g(y)\,dy}$ |
| $x^a y^b(my\,dx + nx\,dy) + x^c y^d(py\,dx + qx\,dy) = 0$ | $x^h y^k$, with $\frac{a + h + 1}{m} = \frac{b + k + 1}{n}$, $\frac{c + h + 1}{p} = \frac{d + k + 1}{q}$ |

Note the **signs** in the last two rows: $M_y - N_x$ over $N$, but $N_x - M_y$ over $M$.

**Example 1 (rule in $x$).** $(x^2 + y^2 + x)\,dx + xy\,dy = 0$: $\frac{M_y - N_x}{N} = \frac{2y - y}{xy} = \frac1x$, so the IF is $e^{\ln x} = x$. Then
$$(x^3 + xy^2 + x^2)\,dx + x^2y\,dy = 0 \;\Rightarrow\; \frac{x^4}{4} + \frac{x^2y^2}{2} + \frac{x^3}{3} = c,$$
i.e. $3x^4 + 4x^3 + 6x^2y^2 = C$.

**Example 2 (rule in $y$).** $(y^4 + 2y)\,dx + (xy^3 + 2y^4 - 4x)\,dy = 0$: $\frac{N_x - M_y}{M} = \frac{(y^3 - 4) - (4y^3 + 2)}{y(y^3 + 2)} = -\frac3y$, so the IF is $y^{-3}$.

**Example 3 (homogeneous).** $(x^2y - 2xy^2)\,dx - (x^3 - 3x^2y)\,dy = 0$: $Mx + Ny = x^2y^2$, so the IF is $\frac{1}{x^2y^2}$.

**Example 4 ($y f_1(xy)$ form).** $y(xy + 2x^2y^2)\,dx + x(xy - x^2y^2)\,dy = 0$: $Mx - Ny = 3x^3y^3$, so $\frac{1}{x^3y^3}$ is an IF.

**By inspection.** $x\,dy - y\,dx = (x^2 + y^2)\,dx$: divide by $x^2 + y^2$ to get $d\left(\tan^{-1}\frac{y}{x}\right) = dx$, so $\tan^{-1}\frac{y}{x} = x + C$.

Linear equations $y' + Py = Q$ (IF $e^{\int P\,dx}$) and Bernoulli equations are in `math.ode.ode-linear-clairaut`.

## Quick checks and traps {#exam-tips}

- **Degree:** remove radicals first; degree is undefined when a derivative sits inside $\sin$, $\exp$ or $\ln$.
- **Order of a family's ODE** = number of **essential** constants. $y = Ae^{x + B}$ has one.
- **Check a general solution** by differentiating: for $u(x, y) = C$, the slope is $-u_x/u_y$; compare with $f(x, y)$.
- **Exact test:** $M_y = N_x$, not $M_x = N_y$.
- **IF rules:** $\frac{M_y - N_x}{N} \to$ function of $x$; $\frac{N_x - M_y}{M} \to$ function of $y$. Swapping the sign gives the reciprocal of the right IF.
- **Homogeneous IF** $\frac{1}{Mx + Ny}$ fails when $Mx + Ny \equiv 0$; then $y = kx$ already solves the equation.
- **Reducible to homogeneous:** if $a_1b_2 = a_2b_1$, no shift works; use $z = a_1x + b_1y$.
- **Separable:** do not lose constant solutions $y = y_0$ with $h(y_0) = 0$.
- **Picard is local:** $y' = y^2$, $y(0) = 1$ has $y = \frac{1}{1 - x}$, defined only on $(-\infty, 1)$.
- **Uniqueness needs more than continuity:** $y' = 3y^{2/3}$, $y(0) = 0$ has both $y = 0$ and $y = x^3$.
