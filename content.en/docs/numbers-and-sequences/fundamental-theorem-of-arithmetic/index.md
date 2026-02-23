---
title: 'Fundamental Theorem of Arithmetic'
weight: 3
---

# Fundamental Theorem of Arithmetic
Let us consider the following conversation between a Teacher and students.
<!-- <div style="border: 1px solid red; padding: 10px;">  -->

**Teacher**: Factorise the number 240.

Malar: 24 × 10

Raghu : 8 × 30

Iniya: 12 × 20

Kumar : 15 × 16

Malar: Whose answer is correct Sir?

**Teacher** : All the answers are correct.

Raghu : How sir?

**Teacher** : Split each of the factors into product of prime numbers.

Malar: 2 × 2 × 2 × 3 × 2 × 5

Raghu : 2 × 2 × 2 × 2 × 3 × 5

Iniya: 2 × 2 × 3 × 2 × 2 × 5

Kumar : 3 × 5 × 2 × 2 × 2 × 2

**Teacher** : Good! Now, count the number of 2 ’s, 3 ’s and 5 ’s.

Malar: I got four 2 ’s, one 3 and one 5.

Raghu : I got four 2 ’s, one 3 and one 5.

Iniya: I also got the same numbers too.

Kumar : Me too sir.

Malar: All of us got four 2 ’s, one 3 and one 5 . This is very surprising to us.

**Teacher** : Yes, It should be. Once any number is factorized up to a product of prime numbers, everyone should get the same collection of prime numbers.

This concept leads us to the following important theorem.

**Theorem 4 (Fundamental Theorem of Arithmetic) (without proof )**

![](fundamental.png)

"Every positive integer (except the number 1) can be represented in exactly one way apart from rearrangement as a product of one or more primes."

The fundamental theorem asserts that every composite number can be decomposed as a product of prime numbers and that the decomposition is unique. In the sense that there is one and only way to express the decomposition as product of primes.

In general, we conclude that given a composite number $\mathrm{N}$, we decompose it uniquely in the form {{<katex>}}N=p_{1}^{q_{1}} \times p_{2}^{q_{2}} \times p_{3}^{q_{3}} \times \cdots \times p_{n}^{q_{n}}{{</katex>}} where {{<katex>}}p_{1}, p_{2}, p_{3}, \ldots, p_{n}{{</katex>}} are primes and {{<katex>}}q_{1}, q_{2}, q_{3}, \ldots, q_{n}{{</katex>}} are natural numbers.

First, we try to factorize {{<katex>}}\mathrm{N}{{</katex>}} into its factors. If all the factors are themselves primes then we can stop. Otherwise, we try to further split the factors which are not prime. Continue the process till we get only prime numbers.

**Illustration**

For example, if we try to factorize 32760 we get

{{<katex>}}
\begin{aligned}
32760 & =2 \times 2 \times 2 \times 3 \times 3 \times 5 \times 7 \times 13 \\
& =2^{3} \times 3^{2} \times 5^{1} \times 7^{1} \times 13^{1}
\end{aligned}
{{</katex>}}

Thus, in whatever way we try to factorize 32760 , we should finally get three 2's, two 3's, one 5, one 7 and one 13

The fact that "Every composite number can be written uniquely as the product of power of primes" is called Fundamental Theorem of Arithmetic.

## Significance of the Fundamental Theorem of Arithmetic

The fundamental theorem about natural numbers except 1, that we have stated above has several applications, both in Mathematics and in other fields. The theorem is vastly important in Mathematics, since it highlights the fact that prime numbers are the 'Building Blocks' for all the positive integers. Thus, prime numbers can be compared to atoms making up a molecule.

![](2.png)

**Example 2.7** In the given factorisation, find the numbers m and n.

***Solution*** Value of the first box from bottom {{<katex>}}=5 \times 2=10{{</katex>}}

{{<katex>}}
\text { Value of } n=5 \times 10=50
{{</katex>}}

Value of the second box from bottom {{<katex>}}=3 \times 50=150{{</katex>}}

{{<katex>}}
\text { Value of } m=2 \times 150=300
{{</katex>}}

Thus, the required numbers are m=300, n=50

**Example 2.8** Can the number {{<katex>}}6^{n}, n{{</katex>}} being a natural number end with the digit 5 ? Give reason for your answer.

***Solution*** Since {{<katex>}}6^{n}=(2 \times 3)^{n}=2^{n} \times 3^{n}{{</katex>}},

2 is a factor of {{<katex>}}6^{n}{{</katex>}}. So, {{<katex>}}6^{n}{{</katex>}} is always even.

But any number whose last digit is 5 is always odd.

Hence, {{<katex>}}6^{n}{{</katex>}} cannot end with the digit 5.

**Example 2.9** Is {{<katex>}}7 \times 5 \times 3 \times 2+3{{</katex>}} a composite number? Justify your answer.

***Solution*** Yes, the given number is a composite number, because

{{<katex>}}
7 \times 5 \times 3 \times 2+3=3 \times(7 \times 5 \times 2+1)=3 \times 71
{{</katex>}}

Since the given number can be factorized in terms of two primes, it is a composite number.

**Example 2.10** 'a' and 'b' are two positive integers such that {{<katex>}}a^{b} \times b^{a}=800{{</katex>}}. Find 'a' and 'b'.

***Solution*** The number 800 can be factorized as

{{<katex>}}
800=2 \times 2 \times 2 \times 2 \times 2 \times 5 \times 5=2^{5} \times 5^{2}
{{</katex>}}

Hence, {{<katex>}}a^{b} \times b^{a}=2^{5} \times 5^{2}{{</katex>}}

This implies that a=2 and b=5 (or) a=5 and b=2

![](ten.png)

**Exercise 2.2**


1. For what values of natural number {{<katex>}}n, 4^{n}{{</katex>}} can end with the digit 6 ?
2. If m, n are natural numbers, for what values of m, does {{<katex>}}2^{n} \times 5^{m}{{</katex>}} ends in 5 ?
3. Find the HCF of 252525 and 363636.
4. If {{<katex>}}13824=2^{a} \times 3^{b}{{</katex>}} then find a and b.
5. If {{<katex>}}p_{1}^{x_{1}} \times p_{2}^{x_{2}} \times p_{3}^{x_{3}} \times p_{4}^{x_{4}}=113400{{</katex>}} where {{<katex>}}p_{1}, p_{2}, p_{3}, p_{4}{{</katex>}} are primes in ascending order and {{<katex>}}x_{1}, x_{2}, x_{3}, x_{4}{{</katex>}} are integers, find the value of {{<katex>}}p_{1}, p_{2}, p_{3}, p_{4}{{</katex>}} and {{<katex>}}x_{1}, x_{2}, x_{3}, x_{4}{{</katex>}}.
6. Find the LCM and HCF of 408 and 170 by applying the fundamental theorem of arithmetic.
7. Find the greatest number consisting of 6 digits which is exactly divisible by 24,15,36 ?
8. What is the smallest number that when divided by three numbers such as 35,56 and 91 leaves remainder 7 in each case?
9. Find the least number that is divisible by the first ten natural numbers.


3\times