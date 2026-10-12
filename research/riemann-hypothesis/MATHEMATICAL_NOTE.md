# Exact finite prime-error certificates and a conditional route to RH

**Shawn Calvin Snelling · AXEZENT · 12 October 2026 · Public review edition 0.1.0**

Mathematical exposition and verification software prepared with ChatGPT assistance. This is a reviewable research note, not a complete RH proof. Theorems A and B are conditional implications, C is an elementary method obstruction, and D has a finite domain. No historical-priority claim, outside specialist approval, or formal-kernel verification is asserted.

## 1. Definitions and the target

All logarithms are natural. For x >= 1 let

$$
\Lambda(n)=\begin{cases}\log p,&n=p^k,\ p\text{ prime},\ k\ge1,\\0,&\text{otherwise},\end{cases}
\qquad
\psi(x)=\sum_{n\le x}\Lambda(n),\quad E(x)=\psi(x)-x,
$$

and define $G(u)=e^{-u/2}E(e^u)$ for u >= 0. RH asserts that every nontrivial zero of the meromorphic continuation of zeta has real part 1/2 [S2].

Runtime, polynomial degree, and growth of E are distinct. An O(n) computation may have an output of size n or an output of zero. A fixed-degree polynomial identity can be certified at sufficiently many distinct exact points only after its degree bound has been justified. Neither observation establishes an all-scale bound for the actual prime error.

## 2. Theorem A: a polynomial normalized envelope implies RH

**Claim RH-IMPL-001.** Suppose finite constants A > 0, u0 >= 0 and a fixed integer d >= 0 satisfy

$$
|G(u)|\le A(1+u)^d\quad\text{for every real }u\ge u_0.
$$

Then RH follows.

**Proof.** In Re(s) > 1 the logarithmic-derivative Dirichlet series [S1] and partial summation give

$$
-\frac{\zeta'(s)}{\zeta(s)}
=\frac{s}{s-1}+s\int_1^\infty E(x)x^{-s-1}\,dx
=\frac{s}{s-1}+s\int_0^\infty G(u)e^{-(s-1/2)u}\,du.
$$

The initial finite segment causes no convergence problem because E is locally bounded. On each compact subset of Re(s) > 1/2 there is epsilon > 0 such that the remaining integrand is dominated by a constant multiple of $(1+u)^d e^{-\epsilon u}$. This is integrable, as are the bounds after any fixed number of differentiations in s. The integral therefore defines a holomorphic function on that half-plane.

The right-hand side is meromorphic there, with its only possible pole at s = 1. By uniqueness of meromorphic continuation it equals the logarithmic derivative there. A zeta zero of multiplicity m creates a nonremovable logarithmic-derivative pole; it cannot occur at s = 1, which is the zeta pole. Thus no zero lies to the right of 1/2. Symmetry of nontrivial zeros about the critical line [S2] excludes the left half as well. QED.

The implication is proved, not its hypothesis. A cubic polynomial envelope would suffice, as would a quadratic one. This refers to normalized error amplitude, not program running time. RH-OPEN-001 remains unproved.

## 3. Theorem B: exact dyadic transfer

**Claim RH-IMPL-002.** Set

$$D(x)=\psi(2x)-\psi(x)-x=E(2x)-E(x).$$

Suppose fixed K >= 0 and X0 >= 2 satisfy

$$|D(x)|\le K\sqrt{x}(\log x)^2\quad\text{for every real }x\ge X_0.$$

Choose a finite C0 >= 0 with $|E(u)|\le C_0\sqrt{u}(\log u)^2$ on $[X_0,2X_0)$. Such a finite constant exists on this bounded interval. Then

$$
|E(x)|\le\bigl[C_0+(1+\sqrt2)K\bigr]\sqrt{x}(\log x)^2\quad(x\ge X_0),
$$

and Theorem A implies RH.

**Proof.** Write x = 2^m u with $X_0\le u<2X_0$ and m a nonnegative integer. Telescoping gives

$$E(x)=E(u)+\sum_{j=0}^{m-1}D(2^ju).$$

Use $\log(2^j u)\le\log x$, $\sqrt{2^ju}=\sqrt{x}2^{-(m-j)/2}$, and

$$\sum_{h=1}^{\infty}2^{-h/2}=1+\sqrt2.$$

The initial term is bounded by $C_0\sqrt{x}(\log x)^2$ because this envelope is increasing for x >= 2. This proves the bound and implication. QED.

The uniform estimate for D is itself an RH-strength requirement. It has not been proved in this project. Proving it only at integer powers of two would not justify the stated all-real hypothesis.

## 4. Theorem C: an elementary obstruction to discarding signs

**Claim RH-OBSTRUCTION-001.** For every positive integer m,

$$
\sum_{m<n\le2m}|\Lambda(n)-1|
\ge\left\lfloor\frac{2m}{6}\right\rfloor-\left\lfloor\frac m6\right\rfloor
\ge\frac m6-1.
$$

**Proof.** Each multiple of six has both prime factors two and three, so it is not a prime power. Its von Mangoldt value is zero and its absolute summand equals one. Counting these multiples and using the elementary floor bounds gives the result. QED.

For integer m, $D(m)=\sum_{m<n\le2m}(\Lambda(n)-1)$. The displayed absolute sum is not O(sqrt(m) log(m)^2), because its lower bound is linear. Consequently that termwise triangle-inequality estimate cannot supply Theorem B. This does not refute RH or every certificate approach; it explains why the proposed route must retain or recover cancellation. This observation is elementary; no originality claim is made.

## 5. Theorem D: a finite-domain, all-real certificate

**Claim RH-FINITE-001.** Without assuming RH, the supplied computation and the interval argument below establish

$$
|\psi(x)-x|\le\frac1{16}\sqrt{x}(\log x)^2
\quad\text{for every real }256\le x\le1{,}048{,}576.
$$

The computational dependencies are `certify_finite_envelope.py`, `test_certificate.py`, and `receipts/finite_envelope_receipt.json`. A reviewer must audit both the argument and the executable implementation.

### 5.1 Exhaustive arithmetic events

An Eratosthenes sieve lists primes p through the finite cutoff. For each p the program lists p, p^2, ... up to the cutoff. Unique factorization ensures distinct prime bases cannot produce the same event; the program also checks uniqueness. Sorted events are exactly the jumps of psi.

All events at or below the left endpoint contribute to its initial value. Between consecutive events, psi is constant. At a later prime-power event the preceding interval is checked before the new log(p) increment is added. The final endpoint is checked after its own increment, if present. Thus left and right jump conventions are retained.

### 5.2 Cell coverage

Suppose psi on a half-open cell [a,b) is enclosed in [L,U]. Then

$$
|\psi(x)-x|\le\max\{|L-a|,|U-a|,|L-b|,|U-b|\}\quad(a\le x<b).
$$

This follows by maximizing absolute value over the rectangle $[L,U]\times[a,b]$. The envelope $\sqrt{x}(\log x)^2/16$ is increasing for x >= 1. It suffices to compare the error upper bound with a rigorous lower bound on the envelope at a. A separate zero-length endpoint check includes x = 1,048,576.

### 5.3 Logarithm enclosures

Write the positive integer n as $n=2^k r$ with $1\le r<2$, and let $z=(r-1)/(r+1)$. With T = 40 terms,

$$
\log r=2\sum_{j=0}^{T-1}\frac{z^{2j+1}}{2j+1}+R_T,
\qquad
0\le R_T\le\frac{2z^{2T+1}}{(2T+1)(1-z^2)}
\le\frac{9}{4(2T+1)3^{2T+1}}.
$$

The bound follows by replacing every remaining odd denominator with 2T+1 and summing the geometric tail. The same formula encloses log(2) using z = 1/3. Work on the rational grid with denominator Q = 2^96: floor for lower bounds, ceiling for upper bounds. Products have nonnegative operands; each outward interval operation preserves containment by induction. Add k times the log(2) interval to the interval for log(r).

For integer a, `isqrt(a*Q*Q)/Q` is a lower bound for sqrt(a). Multiplying the nonnegative lower bounds, dividing by 16, and rounding down gives a lower bound for the envelope. No floating-point value decides acceptance. The receipt's decimal ratio is display-only.

### 5.4 Recorded finite computation

The supplied receipt lists 82,025 primes, 82,267 prime-power events, and 82,197 constant-psi cells from 256 to the cutoff, plus the final endpoint. Every interval comparison passed. The ordered exact-cell SHA-256 is

```text
ee5b85b29884d7071c0471f05b38b4f468e7beb36d3ae9efde14fdf0eb09f744
```

Normal and optimized-Python replay match the frozen receipt. Seventeen tests include a separately formed rational-series logarithm enclosure, sieve versus trial division, prime powers versus factorization, a deliberately false envelope, and a polynomial-degree counterexample. These are implementation checks; not 17 independent mathematical discoveries. Hash agreement is an integrity check, not a substitute for the argument.

This proves the stated finite-domain claim by the computation plus cell coverage. It says nothing about x beyond the cutoff. The range is a demonstration, not a claimed worldwide computational record.

## 6. The exact remaining obligation

**RH-OPEN-001:** establish an unconditional, uniform bound for the actual prime error sufficient for Theorem A or B, with constants independent of the growing scale, or supply another complete RH argument. Theorems A-C, Theorem D, program speed, and a count of successful tests do not supply that bound.

No implication from the separate AHR higher-Lie work to RH is used. No wave minimum is equated with a zeta zero. No extrapolation of a finite interval is called a universal proof.

## Primary sources

[S1] NIST Digital Library of Mathematical Functions, §27.4, equation 27.4.12: the von Mangoldt Dirichlet series equals -zeta'/zeta for Re(s) > 1. https://dlmf.nist.gov/27.4.E12

[S2] NIST DLMF §25.10(i): nontrivial zeros, critical strip, and functional-equation symmetry. https://dlmf.nist.gov/25.10

[S3] Clay Mathematics Institute, Riemann Hypothesis and official problem description. https://www.claymath.org/millennium/riemann-hypothesis/

[S4] Clay Mathematics Institute, Rules for the Millennium Prize Problems. https://www.claymath.org/millennium-problems/rules/

The sources provide standard definitions and background, not independent validation of this note or its software. The conditional arguments are written out here; the computation is supplied for reproduction and criticism.
