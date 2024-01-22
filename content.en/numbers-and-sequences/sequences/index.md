---
title: 'Sequences'
weight: 5
---


# Sequences

Consider the following pictures.

![sequences](sequences.png)

There is some pattern or arrangement in these pictures. In the first picture, the first row contains one apple, the second row contains two apples and in the third row there are three apples etc... The number of apples in each of the rows are 1, 2, 3, ...

In the second picture each step have 0 . 5 feet height. The total height of the steps from the base are 0 . 5 feet, 1 feet, 1 . 5 feet,... In the third picture one square, 3 squares, 5 squares,These numbers belong to category called **"sequences"**

**Definition**

A **real valued sequence** is a function defined on the set of natural numbers and taking real values.

Each element in the sequence is called a term of the sequence. The element in the first position is called the first term of the sequence. The element in the second position is called second term of the sequence and so on.

If the {{<katex>}}n^{th}{{</katex>}} term is denoted by {{<katex>}}a^{n}{{</katex>}} , then {{<katex>}}a^{1}{{</katex>}} is the first term, {{<katex>}}a^{2}{{</katex>}} is the second term, and so on.
A sequence can be written as {{<katex>}}a^{1}{{</katex>}}, {{<katex>}}a^{2}{{</katex>}}, {{<katex>}}a^{3}{{</katex>}} ,..., {{<katex>}}a^{n}{{</katex>}} ,...

**Illustration**

1. 1, 3, 5, 7 ,... is a sequence with general term {{<katex>}}a_{n}{{</katex>}} = 2n − 1 . When we put n = 1, 2, 3 ,..., we get {{<katex>}}a_{1}{{</katex>}} =1, {{<katex>}}a_{2}{{</katex>}} = 3, {{<katex>}}a_{3}{{</katex>}} = 5 , {{<katex>}}a_{n}{{</katex>}}= 7 ,...
2. 1/2,1/3,1/4,1/5,....is a sequence with general term 1/(n+1). When we put n = 1, 2, 3,.... we get {{<katex>}}a_{1}{{</katex>}}=1/2, {{<katex>}}a_{2}{{</katex>}}=1/3, {{<katex>}}a_{3}{{</katex>}}=1/4, {{<katex>}}a_{4}{{</katex>}}=1/5,......

If the number of elements in a sequence is finite then it is called a Finite sequence.

If the number of elements in a sequence is infinite then it is called an Infinite sequence.

**Sequence as a Function**

![](6.png)

A sequence can be considered as a function defined on the set of natural numbers **N** . In particular, a sequence is a function

f:**N->R**, where **R** is the set of all real numbers.

If the sequence is of the form a1, a2, a3,... then we can associate the function to the sequence {{<katex>}}a_{1}{{</katex>}}, {{<katex>}}a_{2}{{</katex>}}, {{<katex>}}a_{3}{{</katex>}},... by f ( k ) = {{<katex>}}a_{k}{{</katex>}}, k =1 ,2 ,3 ,...

![Progress check](sequence2.png)

**Example 2.19**  Find the next three terms of the sequences

(i) {{<katex>}}\frac{1}{2}, \frac{1}{6}, \frac{1}{10}, \frac{1}{14}, \ldots{{</katex>}}
(ii) {{<katex>}}5,2,-1,-4, \ldots{{</katex>}}
(iii) {{<katex>}}1,0.1,0.01, \ldots{{</katex>}}

***Solution***

(i) 
![Sol](1.png)

In the above sequence the numerators are same and the denominator is increased by 4 .

So the next three terms are {{<katex>}}a_{5}=\frac{1}{14+4}=\frac{1}{18}{{</katex>}}

{{<katex>}}
\begin{gathered}
a_{6}=\frac{1}{18+4}=\frac{1}{22}\\
a_{7}=\frac{1}{22+4}=\frac{1}{26}
\end{gathered}
{{</katex>}}

(ii).
![Sol](2.png)

Here each term is decreased by 3. So the next three terms are -7, -10, -13.

(iii).
![Sol](3.png)

Here each term is divided by 10. Hence, the next three terms are

{{<katex>}}
\begin{aligned}
& a_{4}=\frac{0.01}{10}=0.001 \\
& a_{5}=\frac{0.001}{10}=0.0001 \\
& a_{6}=\frac{0.0001}{10}=0.00001
\end{aligned}
{{</katex>}}

**Example 2.20** Find the general term for the following sequences
(i) {{<katex>}}3,6,9, \ldots{{</katex>}}
(ii) {{<katex>}}\frac{1}{2}, \frac{2}{3}, \frac{3}{4}, \ldots{{</katex>}}
(iii) {{<katex>}}5,-25,125, \ldots{{</katex>}}

***Solution*** 
(i) {{<katex>}}3,6,9, \ldots{{</katex>}}

Here the terms are multiples of 3 . So the general term is {{<katex>}}a_{n}=3 n{{</katex>}},

(ii) {{<katex>}}\frac{1}{2}, \frac{2}{3}, \frac{3}{4}, \ldots{{</katex>}}

{{<katex>}}a_{1}=\frac{1}{2} ; a_{2}=\frac{2}{3} ; a_{3}=\frac{3}{4}{{</katex>}}

We see that the numerator of {{<katex>}}n^{\text {th }}{{</katex>}} term is n, and the denominator is one more than the numerator. Hence, {{<katex>}}a_{n}=\frac{n}{n+1}, n \in \mathbb{N}{{</katex>}}

(iii) {{<katex>}}5,-25,125, \ldots{{</katex>}}

The terms of the sequence have + and - sign alternatively and also they are in powers of 5 .

So the general term {{<katex>}}a_{n}=(-1)^{n+1} 5^{n}, n \in \mathbb{N}{{</katex>}}

**Example 2.21** The general term of a sequence is defined as
![Sol](4.png)

<!-- {{<katex>}}
a_{n}=\left\{\begin{array}{l}
n(n+3) ; n \in \mathbb{N} \text { is odd } \\
n^{2}+1 \quad ; n \in \mathbb{N} \text { is even }
\end{array}}\right.
{{</katex>}} -->

Find the eleventh and eighteenth terms.

***Solution*** To find {{<katex>}}a_{11}{{</katex>}}, since 11 is odd, we put n=11 in {{<katex>}}a_{n}=n(n+3){{</katex>}}

Thus, the eleventh term {{<katex>}}\quad a_{11}=11(11+3)=154{{</katex>}}.

To find {{<katex>}}a_{18}{{</katex>}}, since 18 is even, we put {{<katex>}}\quad n=18{{</katex>}} in {{<katex>}}a_{n}=n^{2}+1{{</katex>}}

Thus, the eighteenth term {{<katex>}}\quad a_{18}=18^{2}+1=325{{</katex>}}

**Example 2.22** Find the first five terms of the following sequence.

{{<katex>}}
a_{1}=1, a_{2}=1, a_{n}=\frac{a_{n-1}}{a_{n-2}+3} ; n \geq 3, n \in \mathbb{N}
{{</katex>}}

***Solution*** The first two terms of this sequence are given by {{<katex>}}a_{1}=1, a_{2}=1{{</katex>}}. The third term {{<katex>}}a_{3}{{</katex>}} depends on the first and second terms.


{{<katex>}}
a_{3}=\frac{a_{3-1}}{a_{3-2}+3}=\frac{a_{2}}{a_{1}+3}=\frac{1}{1+3}=\frac{1}{4}
{{</katex>}}

Similarly the fourth term {{<katex>}}a_{4}{{</katex>}} depends upon {{<katex>}}a_{2}{{</katex>}} and {{<katex>}}a_{3}{{</katex>}}.

{{<katex>}}
a_{4}=\frac{a_{4-1}}{a_{4-2}+3}=\frac{a_{3}}{a_{2}+3}=\frac{\frac{1}{4}}{1+3}=\frac{\frac{1}{4}}{4}=\frac{1}{4} \times \frac{1}{4}=\frac{1}{16}
{{</katex>}}

In the same way, the fifth term {{<katex>}}a_{5}{{</katex>}} can be calculated as

{{<katex>}}
a_{5}=\frac{a_{5-1}}{a_{5-2}+3}=\frac{a_{4}}{a_{3}+3}=\frac{\frac{1}{16}}{\frac{1}{4}+3}=\frac{1}{16} \times \frac{4}{13}=\frac{1}{52}
{{</katex>}}

Therefore, the first five terms of the sequence are {{<katex>}}1,1, \frac{1}{4}, \frac{1}{16}{{</katex>}} and {{<katex>}}\frac{1}{52}{{</katex>}}

![Ex](5.png)

1. Find the next three terms of the following sequence.
(i) {{<katex>}}8,24,72, \ldots{{</katex>}}
(ii) {{<katex>}}5,1,-3, \ldots{{</katex>}}
(iii) {{<katex>}}\frac{1}{4}, \frac{2}{9}, \frac{3}{16}, \ldots{{</katex>}}
1. Find the first four terms of the sequences whose {{<katex>}}n^{\text {th }}{{</katex>}} terms are given by
(i) {{<katex>}}a_{n}=n^{3}-2{{</katex>}}
(ii) {{<katex>}}a_{n}=(-1)^{n+1} n(n+1){{</katex>}}
(iii) {{<katex>}}a_{n}=2 n^{2}-6{{</katex>}}
1. Find the {{<katex>}}n^{\text {th }}{{</katex>}} term of the following sequences
(i) {{<katex>}}2,5,10,17, \ldots{{</katex>}}
(ii) {{<katex>}}0, \frac{1}{2}, \frac{2}{3}, \ldots{{</katex>}}
(iii) {{<katex>}}3,8,13,18, \ldots{{</katex>}}
1. Find the indicated terms of the sequences whose {{<katex>}}n^{\text {th }}{{</katex>}} terms are given by
(i) {{<katex>}}a_{n}=\frac{5 n}{n+2} ; a_{6}{{</katex>}} and {{<katex>}}a_{13}{{</katex>}}
(ii) {{<katex>}}a_{n}=-\left(n^{2}-4\right) ; a_{4}{{</katex>}} and {{<katex>}}a_{11}{{</katex>}}
1. Find {{<katex>}}a_{8}{{</katex>}} and {{<katex>}}a_{15}{{</katex>}} whose {{<katex>}}n^{\text {th }}{{</katex>}} term is {{<katex>}}a_{n}= \begin{cases}\frac{n^{2}-1}{n+3} & ; n \text { is even, } n \in \mathbb{N} \\ \frac{n^{2}}{2 n+1} & ; n \text { is odd, } n \in \mathbb{N}\end{cases}{{</katex>}}
2. If {{<katex>}}a_{1}=1, a_{2}=1{{</katex>}} and {{<katex>}}a_{n}=2 a_{n-1}+a_{n-2,} n \geq 3, n \in \mathbb{N}{{</katex>}}, then find the first six terms of the sequence.






