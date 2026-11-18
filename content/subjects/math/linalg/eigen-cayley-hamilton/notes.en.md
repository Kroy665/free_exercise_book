# Eigenvalues and Cayley–Hamilton

## The characteristic polynomial {#characteristic-polynomial}

Let $A$ be an $n \times n$ matrix over a field $F$ ($\R$ or $\C$). A scalar $\lambda$ is an **eigenvalue** of $A$ if $Ax = \lambda x$ for some **non-zero** vector $x$. Such an $x$ exists exactly when $A - \lambda I$ is singular, that is, when

$$\det(\lambda I - A) = 0.$$

- $\chi_A(\lambda) = \det(\lambda I - A)$ is the **characteristic polynomial**. It is monic of degree $n$.
- $\chi_A(\lambda) = 0$ is the **characteristic equation**; its roots are the eigenvalues.

:::caution
Many Indian texts write $|A - \lambda I| = 0$ instead. Since $\det(A - \lambda I) = (-1)^n\det(\lambda I - A)$, the two polynomials differ only by the sign $(-1)^n$. The equation and the eigenvalues are the same. In these notes the characteristic polynomial is the monic one, $\det(\lambda I - A)$.
:::

**Coefficients for small orders.** For $n = 2$:

$$\chi_A(\lambda) = \lambda^2 - (\operatorname{tr} A)\,\lambda + \det A.$$

For $n = 3$:

$$\chi_A(\lambda) = \lambda^3 - (\operatorname{tr} A)\,\lambda^2 + S_2\,\lambda - \det A,$$

where $S_2$ is the **sum of the three principal minors of order 2** (the minors of $a_{11}, a_{22}, a_{33}$). In general, the coefficient of $\lambda^{n-k}$ is $(-1)^k$ times the sum of all principal minors of order $k$. In particular, the constant term is $(-1)^n\det A$.

**Worked example.** For

$$A = \begin{pmatrix} 2 & 1 & 1\\ 1 & 2 & 1\\ 1 & 1 & 2 \end{pmatrix}:\qquad \operatorname{tr} A = 6,\quad S_2 = 3 + 3 + 3 = 9,\quad \det A = 4.$$

So $\chi_A(\lambda) = \lambda^3 - 6\lambda^2 + 9\lambda - 4 = (\lambda - 1)^2(\lambda - 4)$, and the eigenvalues are $1, 1, 4$.

**Consequences.**
- Over $\C$, $A$ has exactly $n$ eigenvalues counted with multiplicity (fundamental theorem of algebra).
- For a **real** matrix, non-real eigenvalues come in conjugate pairs. So a real matrix of **odd** order has at least one real eigenvalue.
- **Similar matrices** ($B = P^{-1}AP$) have the same characteristic polynomial, since $\det(\lambda I - P^{-1}AP) = \det\big(P^{-1}(\lambda I - A)P\big)$. Hence they have the same eigenvalues, trace and determinant.
- $AB$ and $BA$ have the same characteristic polynomial (for square $A, B$ of the same order).

:::exam-tip
For a $2 \times 2$ matrix, write the equation straight away as $\lambda^2 - (\text{trace})\lambda + \det = 0$. For $3 \times 3$, read off trace, sum of principal minors and determinant. There is no need to expand $\det(A - \lambda I)$.
:::

## Eigenvectors, eigenspaces and multiplicity {#eigenvectors}

For an eigenvalue $\lambda$, the eigenvectors are the **non-zero** solutions of $(A - \lambda I)x = 0$. Together with $0$ they form the **eigenspace**

$$E_\lambda = \ker(A - \lambda I), \qquad \dim E_\lambda = n - \operatorname{rank}(A - \lambda I).$$

Any non-zero multiple of an eigenvector is again an eigenvector, so answers are unique only up to scaling.

**Worked example.** $A = \begin{pmatrix} 4 & 1\\ 2 & 3\end{pmatrix}$ has $\chi_A = \lambda^2 - 7\lambda + 10$, so $\lambda = 5, 2$.
- $\lambda = 5$: $A - 5I = \begin{pmatrix} -1 & 1\\ 2 & -2\end{pmatrix}$ gives $x = y$, eigenvector $(1, 1)^T$.
- $\lambda = 2$: $A - 2I = \begin{pmatrix} 2 & 1\\ 2 & 1\end{pmatrix}$ gives $y = -2x$, eigenvector $(1, -2)^T$.

**Theorem.** Eigenvectors belonging to **distinct** eigenvalues are linearly independent.

*Proof idea.* Take a shortest dependence $c_1x_1 + \cdots + c_kx_k = 0$. Apply $A - \lambda_k I$: this kills $x_k$ and leaves a shorter dependence with coefficients $c_i(\lambda_i - \lambda_k) \ne 0$, a contradiction. Consequently, an $n \times n$ matrix with $n$ distinct eigenvalues has $n$ independent eigenvectors.

**Multiplicity.** For an eigenvalue $\lambda_0$:
- the **algebraic multiplicity** $a(\lambda_0)$ is its multiplicity as a root of $\chi_A$;
- the **geometric multiplicity** $g(\lambda_0) = \dim E_{\lambda_0} = n - \operatorname{rank}(A - \lambda_0 I)$.

Always

$$1 \le g(\lambda_0) \le a(\lambda_0).$$

| Matrix | Eigenvalue | $a$ | $g$ |
|:---|:---:|:---:|:---:|
| $I_2$ | $1$ | 2 | 2 |
| $\begin{pmatrix} 1 & 1\\ 0 & 1\end{pmatrix}$ | $1$ | 2 | 1 |
| $\begin{pmatrix} 2 & 1 & 1\\ 1 & 2 & 1\\ 1 & 1 & 2\end{pmatrix}$ | $1$ | 2 | 2 |

In the last matrix, $A - I$ has all rows equal to $(1, 1, 1)$, so its rank is 1 and $g(1) = 3 - 1 = 2$. The eigenspace is the plane $x + y + z = 0$, spanned by $(1, -1, 0)^T$ and $(1, 0, -1)^T$. For $\lambda = 4$ the eigenvector is $(1, 1, 1)^T$.

:::caution
$0$ **can** be an eigenvalue (exactly when $A$ is singular), but the zero **vector** is never an eigenvector. A matrix with a repeated eigenvalue may or may not have a full set of eigenvectors: always compute the rank of $A - \lambda I$.
:::

## Eigenvalues of related matrices {#properties}

If $Ax = \lambda x$ with $x \ne 0$, apply the operation to both sides:

| Matrix | Eigenvalue | Same eigenvector $x$? |
|:---|:---|:---:|
| $A^T$ | $\lambda$ | not in general |
| $kA$ | $k\lambda$ | yes |
| $A + cI$ | $\lambda + c$ | yes |
| $A^m$ ($m \ge 1$) | $\lambda^m$ | yes |
| $A^{-1}$ ($A$ non-singular) | $1/\lambda$ | yes |
| $\operatorname{adj} A$ ($A$ non-singular) | $\det A/\lambda$ | yes |
| $p(A)$, $p$ a polynomial | $p(\lambda)$ | yes |
| $P^{-1}AP$ | $\lambda$ | eigenvector $P^{-1}x$ |

- $A^T$ has the same eigenvalues because $\det(\lambda I - A^T) = \det(\lambda I - A)^T = \det(\lambda I - A)$.
- **Spectral mapping:** if the eigenvalues of $A$ (over $\C$, with multiplicity) are $\lambda_1, \dots, \lambda_n$, then those of $p(A)$ are exactly $p(\lambda_1), \dots, p(\lambda_n)$.

**Trace and determinant.** Comparing coefficients in $\chi_A(\lambda) = \prod(\lambda - \lambda_i)$:

$$\lambda_1 + \lambda_2 + \cdots + \lambda_n = \operatorname{tr} A, \qquad \lambda_1\lambda_2\cdots\lambda_n = \det A.$$

So $A$ is singular $\iff$ $0$ is an eigenvalue. Also $\operatorname{tr}(A^k) = \sum \lambda_i^k$.

**Triangular matrices.** If $A$ is upper or lower triangular (or diagonal), then $\lambda I - A$ is triangular, so $\chi_A(\lambda) = \prod(\lambda - a_{ii})$: **the eigenvalues are the diagonal entries.**

**Worked example.** A $3 \times 3$ matrix $A$ has eigenvalues $1, -1, 2$. Then:
- $\det A = -2$ and $\operatorname{tr} A = 2$;
- $A^2 - 2A$ has eigenvalues $\lambda^2 - 2\lambda$: $-1, 3, 0$, so it is singular;
- $\operatorname{adj} A$ has eigenvalues $-2/1, -2/(-1), -2/2 = -2, 2, -1$;
- $\det(A + 3I) = (1 + 3)(-1 + 3)(2 + 3) = 40$.

:::caution
The eigenvalues of $A + B$ or $AB$ are **not** sums or products of eigenvalues of $A$ and $B$ in general. The rules in the table use one matrix only. They also do not say that $A^T$ has the same eigenvectors: for $\begin{pmatrix}1 & 1\\ 0 & 2\end{pmatrix}$, $(1, 0)^T$ is an eigenvector of $A$ but not of $A^T$.
:::

## Special matrices {#special-matrices}

| Matrix type | Defining property | Eigenvalues |
|:---|:---|:---|
| real symmetric / Hermitian | $A^T = A$ / $A^* = A$ | all real |
| real skew-symmetric / skew-Hermitian | $A^T = -A$ / $A^* = -A$ | $0$ or purely imaginary |
| real orthogonal / unitary | $A^TA = I$ / $A^*A = I$ | $\lvert\lambda\rvert = 1$ |
| idempotent | $A^2 = A$ | $0$ or $1$ |
| involutory | $A^2 = I$ | $1$ or $-1$ |
| nilpotent | $A^k = 0$ for some $k$ | only $0$ |

**Real symmetric matrices.**
1. *All eigenvalues are real.* Let $Ax = \lambda x$, $x \in \C^n$, $x \ne 0$. Then $\bar x^T A x = \lambda\,\bar x^T x$. The left side equals its own conjugate (because $A$ is real symmetric), and $\bar x^T x = \sum \lvert x_i\rvert^2 > 0$. So $\lambda$ is real.
2. *Eigenvectors for distinct eigenvalues are orthogonal.* If $Ax = \lambda x$, $Ay = \mu y$, then $\lambda\, x^Ty = (Ax)^Ty = x^TAy = \mu\, x^Ty$. With $\lambda \ne \mu$ this forces $x^Ty = 0$.
3. *(Spectral theorem)* A real symmetric matrix is **orthogonally diagonalisable**: $Q^TAQ = D$ with $Q$ orthogonal. So it is always diagonalisable, even with repeated eigenvalues.

**Orthogonal matrices.** If $A^TA = I$ and $Ax = \lambda x$, then $\lVert Ax\rVert = \lVert x\rVert$, so $\lvert\lambda\rvert\,\lVert x\rVert = \lVert x\rVert$ and $\lvert\lambda\rvert = 1$. A real orthogonal matrix can only have **real** eigenvalues $\pm 1$; any other eigenvalues are conjugate pairs $e^{\pm i\theta}$. The rotation $\begin{pmatrix}\cos\theta & -\sin\theta\\ \sin\theta & \cos\theta\end{pmatrix}$ has eigenvalues $e^{\pm i\theta}$.

**Skew-symmetric.** The same argument as for symmetric matrices gives $\bar\lambda = -\lambda$. Example: $\begin{pmatrix}0 & -2\\ 2 & 0\end{pmatrix}$ has $\chi = \lambda^2 + 4$, so $\lambda = \pm 2i$. A real skew-symmetric matrix of **odd** order is singular, so $0$ is always an eigenvalue.

**Worked example.** A real symmetric $2 \times 2$ matrix has eigenvalues $3$ and $-1$, with $(1, 2)^T$ an eigenvector for $3$. The eigenvector for $-1$ must be orthogonal to it, so it is a multiple of $(2, -1)^T$. Reconstruct $A = 3\,\frac{uu^T}{5} - \frac{vv^T}{5}$ with $u = (1, 2)^T$, $v = (2, -1)^T$ if needed.

:::caution
"Real eigenvalues" needs the matrix to be real symmetric (or Hermitian). A complex symmetric matrix can have non-real eigenvalues, and a real non-symmetric matrix such as the rotation above can too.
:::

## The Cayley–Hamilton theorem {#cayley-hamilton}

:::keyfacts
- **Theorem.** Every square matrix satisfies its own characteristic equation: if $\chi_A(\lambda) = \lambda^n + c_{n-1}\lambda^{n-1} + \cdots + c_1\lambda + c_0$, then
  $$A^n + c_{n-1}A^{n-1} + \cdots + c_1A + c_0I = O.$$
- It holds for matrices over any field (indeed over any commutative ring).
:::

*Proof idea.* $(\lambda I - A)\operatorname{adj}(\lambda I - A) = \chi_A(\lambda)I$. Write $\operatorname{adj}(\lambda I - A) = B_{n-1}\lambda^{n-1} + \cdots + B_0$ with constant matrices $B_k$, compare coefficients of powers of $\lambda$, then multiply the $k$th equation by $A^k$ and add. The sum telescopes to $\chi_A(A) = O$.

:::caution
"Put $\lambda = A$ in $\det(\lambda I - A)$ to get $\det(A - A) = 0$" is **not** a proof: it produces the scalar $0$, not the zero matrix.
:::

**Illustration.** $A = \begin{pmatrix} 2 & 1\\ 1 & 3\end{pmatrix}$: $\operatorname{tr} A = 5$, $\det A = 5$, $\chi_A = \lambda^2 - 5\lambda + 5$.

$$A^2 = \begin{pmatrix} 5 & 5\\ 5 & 10\end{pmatrix},\qquad A^2 - 5A + 5I = \begin{pmatrix} 5 - 10 + 5 & 5 - 5\\ 5 - 5 & 10 - 15 + 5\end{pmatrix} = O.$$

**Inverse.** If $c_0 = (-1)^n\det A \ne 0$, then $A\,(A^{n-1} + c_{n-1}A^{n-2} + \cdots + c_1 I) = -c_0 I$, so

$$A^{-1} = -\frac{1}{c_0}\left(A^{n-1} + c_{n-1}A^{n-2} + \cdots + c_1I\right).$$

For the example: $A(A - 5I) = -5I$, so $A^{-1} = \dfrac{5I - A}{5} = \dfrac15\begin{pmatrix} 3 & -1\\ -1 & 2\end{pmatrix}$.

For a $3 \times 3$ matrix with $\chi_A = \lambda^3 - 6\lambda^2 + 11\lambda - 6$: $A^{-1} = \dfrac{A^2 - 6A + 11I}{6}$.

**High powers.** Two methods.
1. *Reduce step by step.* From $A^2 = 5A - 5I$: $A^3 = 5A^2 - 5A = 20A - 25I$, and so on.
2. *Remainder method.* Divide: $\lambda^m = q(\lambda)\chi_A(\lambda) + r(\lambda)$ with $\deg r < n$. Then $A^m = r(A)$. The coefficients of $r$ come from $\lambda_i^m = r(\lambda_i)$ at each eigenvalue (use the derivative as well at a repeated eigenvalue).

**Worked example.** $A = \begin{pmatrix} 1 & 1\\ -2 & 4\end{pmatrix}$ has eigenvalues $2, 3$. Write $A^m = aA + bI$. Then $2^m = 2a + b$ and $3^m = 3a + b$, so

$$a = 3^m - 2^m,\qquad b = 3\cdot 2^m - 2\cdot 3^m.$$

If $\chi_A = (\lambda - 1)^2$, then $\lambda^m = a\lambda + b$ and its derivative $m\lambda^{m-1} = a$ at $\lambda = 1$ give $a = m$, $b = 1 - m$: $A^m = mA - (m - 1)I$.

## Diagonalisation {#diagonalisation}

$A$ ($n \times n$) is **diagonalisable** if $P^{-1}AP = D$ is diagonal for some invertible $P$.

:::keyfacts
- $A$ is diagonalisable $\iff$ $A$ has $n$ **linearly independent eigenvectors**. Then the columns of $P$ are these eigenvectors, and $D = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$ lists the eigenvalues **in the same order**.
- Equivalently, $\chi_A$ splits into linear factors over the field and $g(\lambda) = a(\lambda)$ for every eigenvalue.
- **Sufficient:** $n$ distinct eigenvalues. **Not necessary:** $I$ is diagonal with a single repeated eigenvalue.
- Real symmetric matrices are always diagonalisable (by an orthogonal $P$).
:::

The condition comes from $AP = PD$: column $j$ of this equation reads $Ap_j = \lambda_j p_j$.

**Powers.** If $A = PDP^{-1}$, then $A^m = PD^mP^{-1}$, and $D^m = \operatorname{diag}(\lambda_1^m, \dots, \lambda_n^m)$. More generally $p(A) = P\,p(D)\,P^{-1}$.

**Worked example.** $A = \begin{pmatrix} 5 & 4\\ 1 & 2\end{pmatrix}$: $\chi_A = \lambda^2 - 7\lambda + 6$, eigenvalues $6, 1$.
- $\lambda = 6$: $A - 6I = \begin{pmatrix} -1 & 4\\ 1 & -4\end{pmatrix}$, eigenvector $(4, 1)^T$.
- $\lambda = 1$: $A - I = \begin{pmatrix} 4 & 4\\ 1 & 1\end{pmatrix}$, eigenvector $(1, -1)^T$.

$$P = \begin{pmatrix} 4 & 1\\ 1 & -1\end{pmatrix},\quad P^{-1} = \frac15\begin{pmatrix} 1 & 1\\ 1 & -4\end{pmatrix},\quad P^{-1}AP = \begin{pmatrix} 6 & 0\\ 0 & 1\end{pmatrix}.$$

$$A^m = \frac15\begin{pmatrix} 4\cdot 6^m + 1 & 4\cdot 6^m - 4\\ 6^m - 1 & 6^m + 4\end{pmatrix}.$$

Check at $m = 1$: this gives $\begin{pmatrix} 5 & 4\\ 1 & 2\end{pmatrix}$.

**A non-diagonalisable matrix.** $\begin{pmatrix} 1 & 1\\ 0 & 1\end{pmatrix}$ has $a(1) = 2$ but $\operatorname{rank}(A - I) = 1$, so $g(1) = 1$. Only one independent eigenvector exists. More generally, a non-zero nilpotent matrix is never diagonalisable: $D$ would have to be $O$.

**Diagonalisability test (summary):**
1. Find the eigenvalues and their algebraic multiplicities.
2. For each repeated eigenvalue, compute $g = n - \operatorname{rank}(A - \lambda I)$.
3. Diagonalisable $\iff$ $g = a$ for each one.

:::exam-tip
For a triangular matrix with a repeated diagonal entry $\lambda$, look at $A - \lambda I$. If an off-diagonal entry sitting "between" two equal diagonal entries is non-zero, the rank goes up and $g < a$. Example: $\begin{pmatrix} 2 & 0 & 0\\ a & 2 & 0\\ b & c & 3\end{pmatrix}$ is diagonalisable exactly when $a = 0$.
:::

## The minimal polynomial {#minimal-polynomial}

The **minimal polynomial** $m_A(\lambda)$ is the monic polynomial of least degree with $m_A(A) = O$. It exists because $\chi_A(A) = O$ (Cayley–Hamilton), and it is unique.

**Properties.**
- If $p(A) = O$, then $m_A \mid p$. In particular, $m_A \mid \chi_A$, so $\deg m_A \le n$.
- $m_A$ and $\chi_A$ have the **same roots** (ignoring multiplicity): every eigenvalue is a root of $m_A$, because $m_A(A)x = m_A(\lambda)x = 0$ for an eigenvector $x$.
- Similar matrices have the same minimal polynomial.
- $A$ is diagonalisable over $F$ $\iff$ $m_A$ is a product of **distinct** linear factors over $F$.

**Finding it (orders $\le 3$).** Factor $\chi_A$, list the monic divisors that contain every eigenvalue, and test them in increasing degree.

| $A$ | $\chi_A$ | $m_A$ |
|:---|:---|:---|
| $2I_3$ | $(\lambda - 2)^3$ | $\lambda - 2$ |
| $\operatorname{diag}(3, 3, 5)$ | $(\lambda - 3)^2(\lambda - 5)$ | $(\lambda - 3)(\lambda - 5)$ |
| $\begin{pmatrix} 2 & 1 & 0\\ 0 & 2 & 0\\ 0 & 0 & 2\end{pmatrix}$ | $(\lambda - 2)^3$ | $(\lambda - 2)^2$ |
| $\begin{pmatrix} 1 & 1\\ 0 & 1\end{pmatrix}$ | $(\lambda - 1)^2$ | $(\lambda - 1)^2$ |

For the third matrix, $A - 2I \ne O$ but $(A - 2I)^2 = O$, so $m_A = (\lambda - 2)^2$. It has a repeated factor, so $A$ is not diagonalisable.

:::exam-tip
Use the minimal polynomial as a fast diagonalisability test. If $A^2 = A$, then $m_A$ divides $\lambda(\lambda - 1)$, which has distinct factors, so every idempotent matrix is diagonalisable. The same argument works for $A^2 = I$, which gives $m_A \mid (\lambda - 1)(\lambda + 1)$.
:::

## Quick checks and traps {#exam-tips}

- **Trace and determinant first.** For a $2 \times 2$ answer, the two eigenvalues must add to the trace and multiply to the determinant. This eliminates most options in seconds.
- **Triangular means read the diagonal.** Do not expand a determinant for a triangular matrix.
- **Check an eigenvector by multiplying.** $Ax$ must be a scalar multiple of $x$; any non-zero multiple of a correct answer is also correct.
- **Sign convention.** $|A - \lambda I|$ and $|\lambda I - A|$ give the same equation; options written as "$= 0$" match either way.
- **Inverse by Cayley–Hamilton.** From $\lambda^2 - t\lambda + d = 0$: $A^{-1} = \dfrac{tI - A}{d}$. Check the sign by multiplying back: $A(tI - A) = tA - A^2 = dI$.
- **Adjoint.** The eigenvalues of $\operatorname{adj} A$ are $\det A/\lambda_i$, not $1/\lambda_i$.
- **Repeated eigenvalue does not mean non-diagonalisable.** Compute $g = n - \operatorname{rank}(A - \lambda I)$; $I_n$ and real symmetric matrices are always diagonalisable.
- **Minimal versus characteristic.** $m_A \mid \chi_A$, they have the same roots, and $m_A$ has distinct linear factors exactly when $A$ is diagonalisable.
- **Orthogonal and skew-symmetric.** Real orthogonal: $\lvert\lambda\rvert = 1$, so real eigenvalues can only be $\pm1$. Real skew-symmetric: eigenvalues are $0$ or purely imaginary, in conjugate pairs.
