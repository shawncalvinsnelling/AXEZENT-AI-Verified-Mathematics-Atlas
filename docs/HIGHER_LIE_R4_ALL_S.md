# Higher Lie hook multiplicities for the rectangular family (4^s)

**Status:** `PROVED_FROM_PUBLISHED_PRODUCT_FORMULA / INTERNAL_REPLICATION`  
**Novelty status:** `NOT_ESTABLISHED`  
**Global Conjecture 8.1:** `OPEN`  
**Global Conjecture 8.2:** `OPEN`

## Theorem

Let
[
M_{(4^s)}(x)=sum_{k=0}^{4s-1}m_{k,(4^s)}x^k
]
be the hook-multiplicity generating polynomial of the higher Lie character indexed by the rectangular partition ((4^s)).

For every integer (sge 1),
[
oxed{M_{(4^s)}(x)=s,x^{2s-1}(1+x).}
]

Equivalently,
[
m_{k,(4^s)}=
egin{cases}
s,&k=2s-1	ext{ or }k=2s,\\
0,&	ext{otherwise}.
end{cases}
]

Hence the complete hook-multiplicity sequence for ((4^s)) is log-concave and unimodal for every (sge1).

## Source identities

The derivation uses the notation and identities in:

Ron M. Adin, Pál Hegedüs, Yuval Roichman,
"Higher Lie characters and cyclic descent extension on conjugacy classes",
Algebraic Combinatorics 6 (2023), 1557--1591,
DOI 10.5802/alco.323.

The paper defines
[
E_r(x,y)=1+(1+x)M_r(x,y)
]
and proves
[
E_r(x,y)=prod_{j=0}^{r}
left(1-(-x)^j yight)^{(-1)^{j+1}f_j(r)}.
]

For a single 4-cycle the paper gives
[
M_{(4)}(x)=x+x^2.
]
Since (F_4(x)=(1+x)M_{(4)}(x)),
[
F_4(x)=x+2x^2+x^3,
]
so
[
(f_0(4),f_1(4),f_2(4),f_3(4),f_4(4))=(0,1,2,1,0).
]

## Exact derivation

Substitution in the product formula gives
[
E_4(x,y)=
rac{(1+xy)(1+x^3y)}{(1-x^2y)^2}.
]

Use
[
(1-x^2y)^{-2}
=sum_{tge0}(t+1)x^{2t}y^t
]
and
[
(1+xy)(1+x^3y)=1+(x+x^3)y+x^4y^2.
]

For (sge1), the coefficient of (y^s) is
[
egin{aligned}
[y^s]E_4(x,y)
&=(s+1)x^{2s}
+s(x+x^3)x^{2s-2}
+(s-1)x^4x^{2s-4}\\
&=s x^{2s-1}+2s x^{2s}+s x^{2s+1}\\
&=s x^{2s-1}(1+x)^2.
end{aligned}
]
(The final term has coefficient (s-1=0) when (s=1), so the same formula applies.)

But from (E_4(x,y)=1+(1+x)M_4(x,y)),
[
[y^s]E_4(x,y)=(1+x)M_{(4^s)}(x).
]
Therefore
[
M_{(4^s)}(x)=s x^{2s-1}(1+x).
]

The coefficient sequence has two adjacent nonzero entries, both equal to (s); therefore it is unimodal and log-concave.

## Truth boundary

This proves the (r=4), all-(s) rectangular family as a direct exact consequence of the published generating-function identities.

It does **not** prove Conjecture 8.1 for every partition, and it does **not** prove Conjecture 8.2 for every even (r
e6).

The 2023 article states that its rectangular conjectures were computationally verified for (rle40, sle5). This artifact extends the (r=4) family symbolically to all (s), but no publication-priority or novelty claim is made here until a dedicated literature review establishes that boundary.
