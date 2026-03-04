---
title: 'Special Series'
weight: 10
---
## 2.11 Special Series

There are some series whose sum can be expressed by explicit formulae. Such series are called **special series**.

Here we study some common special series like:
- (i) Sum of first '{{< katex >}}n{{< /katex >}}' natural numbers
- (ii) Sum of first '{{< katex >}}n{{< /katex >}}' odd natural numbers.
- (iii) Sum of squares of first '{{< katex >}}n{{< /katex >}}' natural numbers.
- (iv) Sum of cubes of first '{{< katex >}}n{{< /katex >}}' natural numbers.

We can derive the formula for sum of any powers of first {{< katex >}}n{{< /katex >}}
 natural numbers using the expression {{< katex >}}(x+1)^{k+1} - x^{k+1}{{< /katex >}}.
  That is to find {{< katex >}}1^k + 2^k + 3^k + \ldots + n^k{{< /katex >}}
   we can use the expression {{< katex >}}(x+1)^{k+1} - x^{k+1}{{< /katex >}}.

### 2.11.1 Sum of first {{< katex >}}n{{< /katex >}} natural numbers

To find {{< katex >}}1 + 2 + 3 + \cdots + n{{< /katex >}},
 let us consider the identity {{< katex >}}(x+1)^2 - x^2 = 2x + 1{{< /katex >}}

Where {{< katex >}}x = 1, 2, 3, \ldots, n-1, n{{< /katex >}}

{{< katex >}}\begin{aligned}
x = 1, &\quad 2^2 - 1^2 = 2(1) + 1 \\
x = 2, &\quad 3^2 - 2^2 = 2(2) + 1 \\
x = 3, &\quad 4^2 - 3^2 = 2(3) + 1 \\
&\vdots \\
x = n-1, &\quad n^2 - (n-1)^2 = 2(n-1) + 1 \\
x = n, &\quad (n+1)^2 - n^2 = 2(n) + 1
\end{aligned}{{< /katex >}}

Adding all these equations and cancelling the terms on the Left Hand side, we get:
{{< katex >}}\begin{aligned}
(n+1)^2 - 1^2 &= 2(1 + 2 + 3 + \cdots + n) + n \\
n^2 + 2n &= 2(1 + 2 + 3 + \cdots + n) + n \\
2(1 + 2 + 3 + \cdots + n) &= n^2 + n = n(n+1) \\
1 + 2 + 3 + \cdots + n &= \frac{n(n+1)}{2}
\end{aligned}{{< /katex >}}

### 2.11.2 Sum of first {{< katex >}}n{{< /katex >}} odd natural numbers

{{< katex >}}1 + 3 + 5 + \cdots + (2n-1){{< /katex >}}

It is an A.P. with {{< katex >}}a = 1, d = 2{{< /katex >}}
 and {{< katex >}}l = 2n-1{{< /katex >}}

{{< katex >}}\begin{aligned}
S_n &= \frac{n}{2}[a + l] \\
&= \frac{n}{2}[1 + 2n - 1] \\
S_n &= \frac{n}{2} \times 2n = n^2
\end{aligned}{{< /katex >}}

### 2.11.3 Sum of squares of first {{< katex >}}n{{< /katex >}} natural numbers

To find {{< katex >}}1^2 + 2^2 + 3^2 + \cdots + n^2{{< /katex >}},
 let us consider the identity {{< katex >}}(x+1)^3 - x^3 = 3x^2 + 3x + 1{{< /katex >}}

Where {{< katex >}}x = 1, 2, 3, \ldots, n-1, n{{< /katex >}}

{{< katex >}}\begin{aligned}
x = 1, &\quad 2^3 - 1^3 = 3(1)^2 + 3(1) + 1 \\
x = 2, &\quad 3^3 - 2^3 = 3(2)^2 + 3(2) + 1 \\
x = 3, &\quad 4^3 - 3^3 = 3(3)^2 + 3(3) + 1 \\
&\vdots
\end{aligned}{{< /katex >}}

Adding all these equations and cancelling the terms on the Left Hand side, we get:
{{< katex >}}(n+1)^3 - 1^3 = 3(1^2 + 2^2 + 3^2 + \cdots + n^2) + 3(1 + 2 + 3 + \cdots + n) + n{{< /katex >}}

{{< katex >}}\begin{aligned}
n^3 + 3n^2 + 3n &= 3(1^2 + 2^2 + 3^2 + \cdots + n^2) + 3\frac{n(n+1)}{2} + n \\
1^2 + 2^2 + 3^2 + \cdots + n^2 &= \frac{n(n+1)(2n+1)}{6}
\end{aligned}{{< /katex >}}

### 2.11.4 Sum of cubes of first {{< katex >}}n{{< /katex >}} natural numbers

To find {{< katex >}}1^3 + 2^3 + 3^3 + \cdots + n^3{{< /katex >}}, let us consider the identity:
{{< katex >}}(x+1)^4 - x^4 = 4x^3 + 6x^2 + 4x + 1{{< /katex >}}

Where {{< katex >}}x = 1, 2, 3, \ldots, n-1, n{{< /katex >}}

Adding all these equations and cancelling the terms on the Left Hand side, we get:
{{< katex >}}(n+1)^4 - 1^4 = 4(1^3 + 2^3 + 3^3 + \cdots + n^3) + 6(1^2 + 2^2 + \cdots + n^2) + 4(1 + 2 + \cdots + n) + n{{< /katex >}}

After simplification:
{{< katex >}}\boxed{1^3 + 2^3 + 3^3 + \cdots + n^3 = \left[\frac{n(n+1)}{2}\right]^2}{{< /katex >}}

> **Ideal Friendship - KNOW**
> Consider the numbers 220 and 284.
> 
> Sum of the divisors of 220 (excluding 220) {{< katex >}}= 1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110 = 284{{< /katex >}}
> 
> Sum of the divisors of 284 (excluding 284) {{< katex >}}= 1 + 2 + 4 + 71 + 142 = 220{{< /katex >}}.
> 
> Thus, sum of divisors of one number excluding itself is the other. Such pair of numbers is called **Amicable Numbers** or **Friendly Numbers**.
> 
> 220 and 284 are least pair of Amicable Numbers. They were discovered by Pythagoras. We now know more than 12 million amicable pair of Numbers.

### Summary of Summation Formulae

{{< katex >}}\begin{aligned}
\sum_{k=1}^{n} k &= 1 + 2 + 3 + \cdots + n = \frac{n(n+1)}{2} \\
\sum_{k=1}^{n} (2k-1) &= 1 + 3 + 5 + \cdots + (2n-1) = n^2 \\
\sum_{k=1}^{n} k^2 &= 1^2 + 2^2 + 3^2 + \cdots + n^2 = \frac{n(n+1)(2n+1)}{6} \\
\sum_{k=1}^{n} k^3 &= 1^3 + 2^3 + 3^3 + \cdots + n^3 = \left[\frac{n(n+1)}{2}\right]^2
\end{aligned}{{< /katex >}}

**Example 2.54** Find the value of:
- (i) {{< katex >}}1 + 2 + 3 + \ldots + 50{{< /katex >}}
- (ii) {{< katex >}}16 + 17 + 18 + \cdots + 75{{< /katex >}}

**Solution:**

**(i)** {{< katex >}}1 + 2 + 3 + \cdots + 50{{< /katex >}}

Using {{< katex >}}\sum_{k=1}^{n} k = \frac{n(n+1)}{2}{{< /katex >}}:
{{< katex >}}= \frac{50 \times 51}{2} = 1275{{< /katex >}}

**(ii)** {{< katex >}}16 + 17 + 18 + \cdots + 75{{< /katex >}}
{{< katex >}}= (1 + 2 + 3 + \cdots + 75) - (1 + 2 + 3 + \cdots + 15){{< /katex >}}
{{< katex >}}= \frac{75 \times 76}{2} - \frac{15 \times 16}{2} = 2850 - 120 = 2730{{< /katex >}}

**Progress Check**
1. The sum of cubes of first {{< katex >}}n{{< /katex >}}
 natural numbers is __________ of the first {{< katex >}}n{{< /katex >}} natural numbers.
2. The average of first 100 natural numbers is __________.

**Example 2.55** Find the sum of:
- (i) {{< katex >}}1 + 3 + 5 + \cdots{{< /katex >}} to 40 terms
- (ii) {{< katex >}}2 + 4 + 6 + \cdots + 80{{< /katex >}}
- (iii) {{< katex >}}1 + 3 + 5 + \cdots + 55{{< /katex >}}

**Solution:**

**(i)** {{< katex >}}1 + 3 + 5 + \cdots{{< /katex >}}
 40 terms {{< katex >}}= 40^2 = 1600{{< /katex >}}

**(ii)** {{< katex >}}2 + 4 + 6 + \cdots + 80 = 2(1 + 2 + 3 + \cdots + 40) = 2 \times \frac{40 \times 41}{2} = 1640{{< /katex >}}

**(iii)** {{< katex >}}1 + 3 + 5 + \cdots + 55{{< /katex >}}

Here the number of terms is not given. Now we have to find the number of terms using the formula:
{{< katex >}}n = \frac{(l-a)}{d} + 1 = \frac{(55-1)}{2} + 1 = 28{{< /katex >}}

Therefore, {{< katex >}}1 + 3 + 5 + \cdots + 55 = (28)^2 = 784{{< /katex >}}

**Example 2.56** Find the sum of:
- (i) {{< katex >}}1^2 + 2^2 + \cdots + 19^2{{< /katex >}}
- (ii) {{< katex >}}5^2 + 10^2 + 15^2 + \cdots + 105^2{{< /katex >}}
- (iii) {{< katex >}}15^2 + 16^2 + 17^2 + \cdots + 28^2{{< /katex >}}

**Solution:**

**(i)** {{< katex >}}1^2 + 2^2 + \cdots + 19^2{{< /katex >}}
{{< katex >}}= \frac{19 \times 20 \times 39}{6} = 2470{{< /katex >}}

**(ii)** {{< katex >}}5^2 + 10^2 + 15^2 + \cdots + 105^2{{< /katex >}}
{{< katex >}}= 5^2(1^2 + 2^2 + 3^2 + \cdots + 21^2){{< /katex >}}
{{< katex >}}= 25 \times \frac{21 \times 22 \times 43}{6} = 82775{{< /katex >}}

**(iii)** {{< katex >}}15^2 + 16^2 + 17^2 + \cdots + 28^2{{< /katex >}}
{{< katex >}}\begin{aligned}
&= (1^2 + 2^2 + 3^2 + \cdots + 28^2) - (1^2 + 2^2 + 3^2 + \cdots + 14^2) \\
&= \frac{28 \times 29 \times 57}{6} - \frac{14 \times 15 \times 29}{6} = 7714 - 1015 = 6699
\end{aligned}{{< /katex >}}

**Example 2.57** Find the sum of:
- (i) {{< katex >}}1^3 + 2^3 + 3^3 + \cdots + 16^3{{< /katex >}}
- (ii) {{< katex >}}9^3 + 10^3 + \cdots + 21^3{{< /katex >}}

**Solution:**

**(i)** {{< katex >}}1^3 + 2^3 + 3^3 + \cdots + 16^3 = \left[\frac{16 \times 17}{2}\right]^2 = (136)^2 = 18496{{< /katex >}}

**(ii)** {{< katex >}}9^3 + 10^3 + \cdots + 21^3{{< /katex >}}
{{< katex >}}\begin{aligned}
&= (1^3 + 2^3 + \cdots + 21^3) - (1^3 + 2^3 + \cdots + 8^3) \\
&= \left[\frac{21 \times 22}{2}\right]^2 - \left[\frac{8 \times 9}{2}\right]^2 \\
&= (231)^2 - (36)^2 = 53361 - 1296 = 52065
\end{aligned}{{< /katex >}}

**Example 2.58** If {{< katex >}}1 + 2 + 3 + \cdots + n = 666{{< /katex >}}
 then find {{< katex >}}n{{< /katex >}}.

**Solution:** Since, {{< katex >}}1 + 2 + 3 + \ldots + n = \frac{n(n+1)}{2}{{< /katex >}}, we have:
{{< katex >}}\frac{n(n+1)}{2} = 666{{< /katex >}}
{{< katex >}}n^2 + n - 1332 = 0 \implies (n+37)(n-36) = 0{{< /katex >}}

So, {{< katex >}}n = -37{{< /katex >}}
 or {{< katex >}}n = 36{{< /katex >}}

But {{< katex >}}n \neq -37{{< /katex >}}
 ({{< katex >}}n{{< /katex >}}
  is a natural number); Hence {{< katex >}}n = 36{{< /katex >}}.

**Progress Check**

Say True or False. Justify them.
1. The sum of first {{< katex >}}n{{< /katex >}} odd natural numbers is always an odd number.
2. The sum of consecutive even numbers is always an even number.
3. The difference between the sum of squares of first {{< katex >}}n{{< /katex >}}
 natural numbers and the sum of first {{< katex >}}n{{< /katex >}} natural numbers is always divisible by 2.
4. The sum of cubes of the first {{< katex >}}n{{< /katex >}} natural numbers is always a square number.

---

## Exercise 2.9

1. Find the sum of the following series:
   - (i) {{< katex >}}1 + 2 + 3 + \cdots + 60{{< /katex >}}
   - (ii) {{< katex >}}3 + 6 + 9 + \cdots + 96{{< /katex >}}
   - (iii) {{< katex >}}51 + 52 + 53 + \cdots + 92{{< /katex >}}
   - (iv) {{< katex >}}1 + 4 + 9 + 16 + \cdots + 225{{< /katex >}}
   - (v) {{< katex >}}6^2 + 7^2 + 8^2 + \cdots + 21^2{{< /katex >}}
   - (vi) {{< katex >}}10^3 + 11^3 + 12^3 + \cdots + 20^3{{< /katex >}}
   - (vii) {{< katex >}}1 + 3 + 5 + 7 + \cdots + 71{{< /katex >}}

2. If {{< katex >}}1 + 2 + 3 + \cdots + k = 325{{< /katex >}},
 then find {{< katex >}}1^3 + 2^3 + 3^3 + \cdots + k^3{{< /katex >}}.

3. If {{< katex >}}1^3 + 2^3 + 3^3 + \cdots + k^3 = 44100{{< /katex >}}
 then find {{< katex >}}1 + 2 + 3 + \cdots + k{{< /katex >}}.

4. How many terms of the series {{< katex >}}1^3 + 2^3 + 3^3 + \cdots{{< /katex >}} should be taken to get the sum 14400?

5. The sum of the cubes of the first {{< katex >}}n{{< /katex >}}
 natural numbers is 2025, then find the value of {{< katex >}}n{{< /katex >}}.

6. Rekha has 15 square colour papers of sizes 10 cm, 11 cm, 12 cm, ..., 24 cm. How much area can be decorated with these colour papers?

7. Find the sum of the series {{< katex >}}(2^3 - 1^3) + (4^3 - 3^3) + (6^3 - 5^3) + \cdots{{< /katex >}}:
   - (i) {{< katex >}}n{{< /katex >}} terms
   - (ii) 8 terms

---

## Exercise 2.10 - Multiple Choice Questions

1. Euclid's division lemma states that for positive integers {{< katex >}}a{{< /katex >}}
 and {{< katex >}}b{{< /katex >}},
  there exist unique integers {{< katex >}}q{{< /katex >}}
   and {{< katex >}}r{{< /katex >}}
    such that {{< katex >}}a = bq + r{{< /katex >}},
     where {{< katex >}}r{{< /katex >}} must satisfy:
   - (A) {{< katex >}}1 < r < b{{< /katex >}}
   - (B) {{< katex >}}0 < r < b{{< /katex >}}
   - (C) {{< katex >}}0 \leq r < b{{< /katex >}}
   - (D) {{< katex >}}0 < r \leq b{{< /katex >}}

2. Using Euclid's division lemma, if the cube of any positive integer is divided by 9 then the possible remainders are:
   - (A) {{< katex >}}0, 1, 8{{< /katex >}}
   - (B) {{< katex >}}1, 4, 8{{< /katex >}}
   - (C) {{< katex >}}0, 1, 3{{< /katex >}}
   - (D) {{< katex >}}1, 3, 5{{< /katex >}}

3. If the HCF of 65 and 117 is expressible in the form of {{< katex >}}65m - 117{{< /katex >}},
 then the value of {{< katex >}}m{{< /katex >}} is:
   - (A) 4
   - (B) 2
   - (C) 1
   - (D) 3

4. The sum of the exponents of the prime factors in the prime factorization of 1729 is:
   - (A) 1
   - (B) 2
   - (C) 3
   - (D) 4

5. The least number that is divisible by all the numbers from 1 to 10 (both inclusive) is:
   - (A) 2025
   - (B) 5220
   - (C) 5025
   - (D) 2520

6. {{< katex >}}7^{4k} \equiv{{< /katex >}} _____ (mod 100)
   - (A) 1
   - (B) 2
   - (C) 3
   - (D) 4

7. Given {{< katex >}}F_1 = 1, F_2 = 3{{< /katex >}}
 and {{< katex >}}F_n = F_{n-1} + F_{n-2}{{< /katex >}}
  then {{< katex >}}F_5{{< /katex >}} is:
   - (A) 3
   - (B) 5
   - (C) 8
   - (D) 11

8. The first term of an arithmetic progression is unity and the common difference is 4. Which of the following will be a term of this A.P.:
   - (A) 4551
   - (B) 10091
   - (C) 7881
   - (D) 13531

9. If 6 times of {{< katex >}}6^{\text{th}}{{< /katex >}}
 term of an A.P. is equal to 7 times the {{< katex >}}7^{\text{th}}{{< /katex >}}
  term, then the {{< katex >}}13^{\text{th}}{{< /katex >}} term of the A.P. is:
   - (A) 0
   - (B) 6
   - (C) 7
   - (D) 13

10. An A.P. consists of 31 terms. If its {{< katex >}}16^{\text{th}}{{< /katex >}}
 term is {{< katex >}}m{{< /katex >}}, then the sum of all the terms of this A.P. is:
    - (A) {{< katex >}}16m{{< /katex >}}
    - (B) {{< katex >}}62m{{< /katex >}}
    - (C) {{< katex >}}31m{{< /katex >}}
    - (D) {{< katex >}}m{{< /katex >}}

11. In an A.P., the first term is 1 and the common difference is 4. How many terms of the A.P. must be taken for their sum to be equal to 120?
    - (A) 6
    - (B) 7
    - (C) 8
    - (D) 9

12. If {{< katex >}}A = 2^{65}{{< /katex >}}
 and {{< katex >}}B = 2^{64} + 2^{63} + 2^{62} + \cdots + 2^0{{< /katex >}} which of the following is true?
    - (A) {{< katex >}}B{{< /katex >}}
     is {{< katex >}}2^{64}{{< /katex >}}
      more than {{< katex >}}A{{< /katex >}}
    - (B) {{< katex >}}A{{< /katex >}}
     and {{< katex >}}B{{< /katex >}} are equal
    - (C) {{< katex >}}B{{< /katex >}}
     is larger than {{< katex >}}A{{< /katex >}} by 1
    - (D) {{< katex >}}A{{< /katex >}}
     is larger than {{< katex >}}B{{< /katex >}} by 1

13. The next term of the sequence {{< katex >}}\frac{3}{16}, \frac{1}{8}, \frac{1}{12}, \frac{1}{18}, \ldots{{< /katex >}} is:
    - (A) {{< katex >}}\frac{1}{24}{{< /katex >}}
    - (B) {{< katex >}}\frac{1}{27}{{< /katex >}}
    - (C) {{< katex >}}\frac{2}{3}{{< /katex >}}
    - (D) {{< katex >}}\frac{1}{81}{{< /katex >}}

14. If the sequence {{< katex >}}t_1, t_2, t_3, \ldots{{< /katex >}}
 are in A.P. then the sequence {{< katex >}}t_6, t_{12}, t_{18}, \ldots{{< /katex >}} is:
    - (A) a Geometric Progression
    - (B) an Arithmetic Progression
    - (C) neither an Arithmetic Progression nor a Geometric Progression
    - (D) a constant sequence

15. The value of {{< katex >}}(1^3 + 2^3 + 3^3 + \cdots + 15^3) - (1 + 2 + 3 + \cdots + 15){{< /katex >}} is:
    - (A) 14400
    - (B) 14200
    - (C) 14280
    - (D) 14520

---

## Unit Exercise - 2

1. Prove that {{< katex >}}n^2 - n{{< /katex >}}
 is divisible by 2 for every positive integer {{< katex >}}n{{< /katex >}}.

2. A milk man has 175 litres of cow's milk and 105 litres of buffalow's milk. He wishes to sell the milk by filling the two types of milk in cans of equal capacity. Calculate the following:
   - (i) Capacity of a can
   - (ii) Number of cans of cow's milk
   - (iii) Number of cans of buffalow's milk.

3. When the positive integers {{< katex >}}a, b{{< /katex >}}
 and {{< katex >}}c{{< /katex >}} 
 are divided by 13 the respective remainders are 9, 7 and 10. Find the remainder when {{< katex >}}a + 2b + 3c{{< /katex >}} is divided by 13.

4. Show that {{< katex >}}10^n{{< /katex >}}
 is of the form {{< katex >}}4q + 3{{< /katex >}}
  for any integer {{< katex >}}q{{< /katex >}}.

5. If {{< katex >}}(m+1)^{\text{th}}{{< /katex >}}
 term of an A.P. is twice the {{< katex >}}(n+1)^{\text{th}}{{< /katex >}}
  term, then prove that {{< katex >}}(3m+1)^{\text{th}}{{< /katex >}}
   term is twice the {{< katex >}}(m+n+1)^{\text{th}}{{< /katex >}} term.

6. Find the {{< katex >}}12^{\text{th}}{{< /katex >}}
 term from the last term of the A.P. {{< katex >}}-2, -4, -6, \ldots, -100{{< /katex >}}.

7. Two A.P.'s have the same common difference. The first term of one A.P. is 2 and that of the other is 7. Show that the difference between their {{< katex >}}10^{\text{th}}{{< /katex >}}
 terms is the same as the difference between their {{< katex >}}21^{\text{st}}{{< /katex >}} terms, which is the same as the difference between any two corresponding terms.

8. A man saved ₹16500 in ten years. In each year after the first he saved ₹100 more than he did in the preceding year. How much did he save in the first year?

9. Find the G.P. in which the {{< katex >}}2^{\text{nd}}{{< /katex >}}
 term is {{< katex >}}\sqrt{6}{{< /katex >}}
  and the {{< katex >}}6^{\text{th}}{{< /katex >}}
   term is {{< katex >}}9\sqrt{6}{{< /katex >}}.

10. The value of a motor cycle depreciates at the rate of 15% per year. What will be the value of the motor cycle 3 year hence, which is now purchased for ₹45,000?

---

## Points to Remember

- **Euclid's Division Lemma**
  
  If {{< katex >}}a{{< /katex >}}
   and {{< katex >}}b{{< /katex >}}
    are two positive integers then there exist unique integers {{< katex >}}q{{< /katex >}}
     and {{< katex >}}r{{< /katex >}}
      such that {{< katex >}}a = bq + r{{< /katex >}},
       {{< katex >}}0 \leq r < |b|{{< /katex >}}

- **Fundamental Theorem of Arithmetic**
  
  Every composite number can be expressed as a product of primes and this factorization is unique except for the order in which the prime factors occur.

- **Arithmetic Progression**
  - (i) Arithmetic Progression is {{< katex >}}a, a+d, a+2d, a+3d, \ldots{{< /katex >}}.
   {{< katex >}}n^{\text{th}}{{< /katex >}}
    term is given by {{< katex >}}t_n = a + (n-1)d{{< /katex >}}
  - (ii) Sum to first {{< katex >}}n{{< /katex >}}
   terms of an A.P. is {{< katex >}}S_n = \frac{n}{2}[2a + (n-1)d]{{< /katex >}}
  - (iii) If the last term {{< katex >}}l{{< /katex >}}
   ({{< katex >}}n^{\text{th}}{{< /katex >}}
    term) is given, then {{< katex >}}S_n = \frac{n}{2}[a + l]{{< /katex >}}

- **Geometric Progression**
  - (i) Geometric Progression is {{< katex >}}a, ar, ar^2, ar^3, \ldots, ar^{n-1}, \ldots{{< /katex >}}.
   {{< katex >}}n^{\text{th}}{{< /katex >}} 
   term is given by {{< katex >}}t_n = ar^{n-1}{{< /katex >}}
  - (ii) Sum to first {{< katex >}}n{{< /katex >}}
   terms of a G.P. is {{< katex >}}S_n = \frac{a(r^n - 1)}{r-1}{{< /katex >}}
    if {{< katex >}}r \neq 1{{< /katex >}}
  - (iii) Suppose {{< katex >}}r = 1{{< /katex >}}
   then {{< katex >}}S_n = na{{< /katex >}}
  - (iv) Sum to infinite terms of a G.P. {{< katex >}}a + ar + ar^2 + \cdots{{< /katex >}} 
  is {{< katex >}}S_\infty = \frac{a}{1-r}{{< /katex >}},
   where {{< katex >}}-1 < r < 1{{< /katex >}}

- **Special Series**
  - (i) The sum of first {{< katex >}}n{{< /katex >}}
   natural numbers: {{< katex >}}1 + 2 + 3 + \cdots + n = \frac{n(n+1)}{2}{{< /katex >}}
  - (ii) The sum of squares of first {{< katex >}}n{{< /katex >}}
   natural numbers: {{< katex >}}1^2 + 2^2 + 3^2 + \cdots + n^2 = \frac{n(n+1)(2n+1)}{6}{{< /katex >}}
  - (iii) The sum of cubes of first {{< katex >}}n{{< /katex >}}
   natural numbers: {{< katex >}}1^3 + 2^3 + 3^3 + \cdots + n^3 = \left[\frac{n(n+1)}{2}\right]^2{{< /katex >}}
  - (iv) The sum of first {{< katex >}}n{{< /katex >}} 
  odd natural numbers: {{< katex >}}1 + 3 + 5 + \cdots + (2n-1) = n^2{{< /katex >}}