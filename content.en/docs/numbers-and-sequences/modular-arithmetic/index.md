---
title: 'Modular Arithmetic'
weight: 4
---
## 2.5 Modular Arithmetic

In a clock, we use the numbers 1 to 12 to represent the time period of 24 hours. How is it possible to represent the 24 hours of a day in a 12 number format? We use 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 and after 12, we use 1 instead of 13 and 2 instead of 14 and so on. That is after 12 we again start from 1, 2, 3, ... In this system the numbers wrap around 1 to 12. This type of wrapping around after hitting some value is called **Modular Arithmetic**.

![Clock Fig. 2.5](clock.jpg)

In Mathematics, modular arithmetic is a system of arithmetic for integers where numbers wrap around a certain value. Unlike normal arithmetic, Modular Arithmetic process cyclically. The ideas of Modular arithmetic was developed by great German mathematician Carl Friedrich Gauss, who is hailed as the "Prince of mathematicians".

### Examples

1. The day and night change repeatedly.
2. The days of a week occur cyclically from Sunday to Saturday.
3. The life cycle of a plant.
4. The seasons of a year change cyclically. (Summer, Autumn, Winter, Spring)
5. The railway and aeroplane timings also work cyclically. The railway time starts at 00:00 and continue. After reaching 23:59, the next minute will become 00:00 instead of 24:00.

![Life Cycle of Plant Fig. 2.6](plant_lifecycle.jpg)

### 2.5.1 Congruence Modulo

Two integers {{< katex >}}a{{< /katex >}} 
and {{< katex >}}b{{< /katex >}}
 are congruence modulo {{< katex >}}n{{< /katex >}} 
 if they differ by an integer multiple of {{< katex >}}n{{< /katex >}}. 
 That {{< katex >}}a - b = kn{{< /katex >}} 
 for some integer {{< katex >}}k{{< /katex >}}. This can also be written as:
{{< katex >}}a \equiv b \pmod{n}{{< /katex >}}

Here the number {{< katex >}}n{{< /katex >}}
 is called **modulus**. In other words, {{< katex >}}a \equiv b \pmod{n}{{< /katex >}} 
 means {{< katex >}}a - b{{< /katex >}} 
 is divisible by {{< katex >}}n{{< /katex >}}.

For example, {{< katex >}}61 \equiv 5 \pmod{7}{{< /katex >}} 
because {{< katex >}}61 - 5 = 56{{< /katex >}} is divisible by 7.

> **Note**
> When a positive integer is divided by {{< katex >}}n{{< /katex >}}, 
then the possible remainders are {{< katex >}}0, 1, 2, \ldots, n-1{{< /katex >}}.
> Thus, when we work with modulo {{< katex >}}n{{< /katex >}},
 we replace all the numbers by their remainders upon division by {{< katex >}}n{{< /katex >}},
  given by {{< katex >}}0, 1, 2, 3, \ldots, n-1{{< /katex >}}.

Two illustrations are provided to understand modulo concept more clearly.

**Illustration 1**

To find {{< katex >}}8 \pmod{4}{{< /katex >}}

With a modulus of 4 (since the possible remainders are 0, 1, 2, 3) we make a diagram like a clock with numbers 0, 1, 2, 3. We start at 0 and go through 8 numbers in a clockwise sequence 1, 2, 3, 0, 1, 2, 3, 0. After doing so cyclically, we end at 0.

Therefore, {{< katex >}}8 \equiv 0 \pmod{4}{{< /katex >}}

**Illustration 2**

To find {{< katex >}}-5 \pmod{3}{{< /katex >}}

With a modulus of 3 (since the possible remainders are 0, 1, 2) we make a diagram like a clock with numbers 0, 1, 2.

We start at 0 and go through 5 numbers in anti-clockwise sequence 2, 1, 0, 2, 1. After doing so cyclically, we end at 1.

Therefore, {{< katex >}}-5 \equiv 1 \pmod{3}{{< /katex >}}

### 2.5.2 Connecting Euclid's Division lemma and Modular Arithmetic

Let {{< katex >}}m{{< /katex >}}
 and {{< katex >}}n{{< /katex >}}
  be integers, where {{< katex >}}m{{< /katex >}}
   is positive. Then by Euclid's division lemma, we can write {{< katex >}}n = mq + r{{< /katex >}} 
   where {{< katex >}}0 \leq r < m{{< /katex >}} 
   and {{< katex >}}q{{< /katex >}} is an integer. Instead of writing 
   {{< katex >}}n = mq + r{{< /katex >}} we can use the congruence notation in the following way.

We say that {{< katex >}}n{{< /katex >}}
 is congruent to {{< katex >}}r{{< /katex >}}
  modulo {{< katex >}}m{{< /katex >}}, 
 if {{< katex >}}n = mq + r{{< /katex >}} 
 for some integer {{< katex >}}q{{< /katex >}}.

{{< katex >}}\begin{aligned}
n &= mq + r \\
n - r &= mq \\
n - r &\equiv 0 \pmod{m} \\
n &\equiv r \pmod{m}
\end{aligned}{{< /katex >}}

Thus the equation {{< katex >}}n = mq + r{{< /katex >}} 
through Euclid's Division lemma can also be written as {{< katex >}}n \equiv r \pmod{m}{{< /katex >}}.

> **Note**
> Two integers {{< katex >}}a{{< /katex >}} 
and {{< katex >}}b{{< /katex >}} 
are congruent modulo {{< katex >}}m{{< /katex >}},
 written as {{< katex >}}a \equiv b \pmod{m}{{< /katex >}},
  if they leave the same remainder when divided by {{< katex >}}m{{< /katex >}}.

**Progress Check**
1. Two integers {{< katex >}}a{{< /katex >}}
 and {{< katex >}}b{{< /katex >}} 
 are congruent modulo {{< katex >}}n{{< /katex >}} if ___________.
2. The set of all positive integers which leave remainder 5 when divided by 7 are ___________.

### 2.5.3 Modulo operations

> **Thinking Corner**
> How many integers exist which leave a remainder of 2 when divided by 3?

Similar to basic arithmetic operations like addition, subtraction and multiplication performed on numbers we can think of performing same operations in modulo arithmetic. The following theorem provides the information of doing this.

### Theorem 5

{{< katex >}}a, b, c{{< /katex >}}
 and {{< katex >}}d{{< /katex >}} 
 are integers and {{< katex >}}m{{< /katex >}} 
 is a positive integer such that if {{< katex >}}a \equiv b \pmod{m}{{< /katex >}} 
 and {{< katex >}}c \equiv d \pmod{m}{{< /katex >}} then:
- (i) {{< katex >}}(a + c) \equiv (b + d) \pmod{m}{{< /katex >}}
- (ii) {{< katex >}}(a - c) \equiv (b - d) \pmod{m}{{< /katex >}}
- (iii) {{< katex >}}(a \times c) \equiv (b \times d) \pmod{m}{{< /katex >}}

**Illustration 3**

If {{< katex >}}17 \equiv 4 \pmod{13}{{< /katex >}} 
and {{< katex >}}42 \equiv 3 \pmod{13}{{< /katex >}} then from theorem 5,
- (i) {{< katex >}}17 + 42 \equiv 4 + 3 \pmod{13} \implies 59 \equiv 7 \pmod{13}{{< /katex >}}
- (ii) {{< katex >}}17 - 42 \equiv 4 - 3 \pmod{13} \implies -25 \equiv 1 \pmod{13}{{< /katex >}}
- (iii) {{< katex >}}17 \times 42 \equiv 4 \times 3 \pmod{13} \implies 714 \equiv 12 \pmod{13}{{< /katex >}}

### Theorem 6

If {{< katex >}}a \equiv b \pmod{m}{{< /katex >}} then:
- (i) {{< katex >}}ac \equiv bc \pmod{m}{{< /katex >}}
- (ii) {{< katex >}}a \pm c \equiv b \pm c \pmod{m}{{< /katex >}}
 for any integer {{< katex >}}c{{< /katex >}}

**Progress Check**
1. The positive values of {{< katex >}}k{{< /katex >}}
 such that {{< katex >}}(k - 3) \equiv 5 \pmod{11}{{< /katex >}} are _________.
2. If {{< katex >}}59 \equiv 3 \pmod{7}{{< /katex >}}
, {{< katex >}}464 \equiv 4 \pmod{7}{{< /katex >}} 
then {{< katex >}}105 \equiv{{< /katex >}} 
_______ {{< katex >}}\pmod{7}{{< /katex >}}
, {{< katex >}}13 \equiv{{< /katex >}}
 _______ {{< katex >}}\pmod{7}{{< /katex >}},
  {{< katex >}}413 \equiv{{< /katex >}}
   _______ {{< katex >}}\pmod{7}{{< /katex >}},
    {{< katex >}}368 \equiv{{< /katex >}}
     _______ {{< katex >}}\pmod{7}{{< /katex >}}.
3. The remainder when {{< katex >}}7 \times 13 \times 19 \times 23 \times 29 \times 31{{< /katex >}} is divided by 6 is ________.

**Example 2.11** Find the remainders when 70004 and 778 is divided by 7.

**Solution:** Since 70000 is divisible by 7:
{{< katex >}}\begin{aligned}
70000 &\equiv 0 \pmod{7} \\
70000 + 4 &\equiv 0 + 4 \pmod{7} \\
70004 &\equiv 4 \pmod{7}
\end{aligned}{{< /katex >}}

Therefore, the remainder when 70004 is divided by 7 is 4.

777 is divisible by 7:
{{< katex >}}\begin{aligned}
777 &\equiv 0 \pmod{7} \\
777 + 1 &\equiv 0 + 1 \pmod{7} \\
778 &\equiv 1 \pmod{7}
\end{aligned}{{< /katex >}}

Therefore, the remainder when 778 is divided by 7 is 1.

**Example 2.12** Determine the value of {{< katex >}}d{{< /katex >}} 
such that {{< katex >}}15 \equiv 3 \pmod{d}{{< /katex >}}.

**Solution:** {{< katex >}}15 \equiv 3 \pmod{d}{{< /katex >}}
 means {{< katex >}}15 - 3 = kd{{< /katex >}},
  for some integer {{< katex >}}k{{< /katex >}}.
{{< katex >}}12 = kd{{< /katex >}}

The divisors of 12 are 1, 2, 3, 4, 6, 12. But {{< katex >}}d{{< /katex >}}
 should be larger than 3 and so the possible values for {{< katex >}}d{{< /katex >}} 
 are {{< katex >}}4, 6, 12{{< /katex >}}.

**Example 2.13** Find the least positive value of {{< katex >}}x{{< /katex >}} such that:
- (i) {{< katex >}}67 + x \equiv 1 \pmod{4}{{< /katex >}}
- (ii) {{< katex >}}98 \equiv (x + 4) \pmod{5}{{< /katex >}}

**Solution:**

**(i)**
{{< katex >}}\begin{aligned}
67 + x &\equiv 1 \pmod{4} \\
67 - 1 + x &= 4n, \text{ for some integer } n \\
66 + x &= 4n
\end{aligned}{{< /katex >}}

{{< katex >}}66 + x{{< /katex >}} is a multiple of 4.

Therefore, the least positive value of {{< katex >}}x{{< /katex >}} must be 2, since 68 is the nearest multiple of 4 more than 66.

**(ii)**
{{< katex >}}\begin{aligned}
98 &\equiv (x + 4) \pmod{5} \\
98 - (x + 4) &= 5n, \text{ for some integer } n \\
94 - x &= 5n
\end{aligned}{{< /katex >}}

{{< katex >}}94 - x{{< /katex >}} is a multiple of 5.

Therefore, the least positive value of {{< katex >}}x{{< /katex >}} 
must be 4, since {{< katex >}}94 - 4 = 90{{< /katex >}} is the nearest multiple of 5 less than 94.

> **Note**
> While solving congruent equations, we get infinitely many solutions compared to finite number of solutions in solving a polynomial equation in Algebra.

**Example 2.14** Solve {{< katex >}}8x \equiv 1 \pmod{11}{{< /katex >}}

**Solution:** {{< katex >}}8x \equiv 1 \pmod{11}$ can be written as $8x - 1 = 11k$, for some integer $k{{< /katex >}}.

{{< katex >}}x = \frac{11k + 1}{8}{{< /katex >}}

When we put {{< katex >}}k = 5, 13, 21, 29, \ldots$ then $11k + 1{{< /katex >}} is divisible by 8.

{{< katex >}}\begin{aligned}
x &= \frac{11 \times 5 + 1}{8} = 7 \\
x &= \frac{11 \times 13 + 1}{8} = 18
\end{aligned}{{< /katex >}}

{{< katex >}}\therefore{{< /katex >}} 
The solutions are {{< katex >}}7, 18, 29, 40, \ldots{{< /katex >}}

**Example 2.15** Compute {{< katex >}}x{{< /katex >}},
 such that {{< katex >}}10^4 \equiv x \pmod{19}{{< /katex >}}

**Solution:**
{{< katex >}}\begin{aligned}
10^2 &= 100 \equiv 5 \pmod{19} \\
10^4 &= (10^2)^2 \equiv 5^2 \pmod{19} \\
10^4 &\equiv 25 \pmod{19} \\
10^4 &\equiv 6 \pmod{19} \quad (\because 25 \equiv 6 \pmod{19}) \\
\therefore x &= 6
\end{aligned}{{< /katex >}}

**Example 2.16** Find the number of integer solutions of {{< katex >}}3x \equiv 1 \pmod{15}{{< /katex >}}.

**Solution:** {{< katex >}}3x \equiv 1 \pmod{15}{{< /katex >}} can be written as:
{{< katex >}}3x - 15k = 1 \text{ for some integer } k{{< /katex >}}
{{< katex >}}3(x - 5k) = 1{{< /katex >}}
{{< katex >}}x - 5k = \frac{1}{3}{{< /katex >}}

Since {{< katex >}}5k{{< /katex >}}
 is an integer, {{< katex >}}5k + \frac{1}{3}{{< /katex >}} cannot be an integer.

So there is no integer solution.

**Example 2.17** A man starts his journey from Chennai to Delhi by train. He starts at 22.30 hours on Wednesday. If it takes 32 hours of travelling time and assuming that the train is not late, when will he reach Delhi?

**Solution:** Starting time 22.30, Travelling time 32 hours. Here we use modulo 24.

The reaching time is:
{{< katex >}}22.30 + 32 \pmod{24} \equiv 54.30 \pmod{24} \equiv 6.30 \pmod{24}{{< /katex >}}

({{< katex >}}32 = (1 \times 24) + 8{{< /katex >}},
 Thursday {{< katex >}}\to{{< /katex >}} Friday)

Thus, he will reach Delhi on Friday at 6.30 hours.

**Example 2.18** Kala and Vani are friends. Kala says, "Today is my birthday" and she asks Vani, "When will you celebrate your birthday?" Vani replies, "Today is Monday and I celebrated my birthday 75 days ago". Find the day when Vani celebrated her birthday.

**Solution:** Let us associate the numbers 0, 1, 2, 3, 4, 5, 6 to represent the weekdays from Sunday to Saturday respectively.

Vani says today is Monday. So the number for Monday is 1. Since Vani's birthday was 75 days ago, we have to subtract 75 from 1 and take the modulo 7, since a week contains 7 days.

{{< katex >}}1 - 75 \pmod{7} \equiv -74 \pmod{7} \equiv -4 \pmod{7} \equiv 7 - 4 \pmod{7} \equiv 3 \pmod{7}{{< /katex >}}

({{< katex >}}-74 = -11 \times 7 + 3{{< /katex >}}, 
{{< katex >}}-77{{< /katex >}} is divisible by 7)

The day for the number 3 is Wednesday.

Therefore, Vani's birthday must be on Wednesday.

---

## Exercise 2.3

1. Find the least positive value of {{< katex >}}x{{< /katex >}} such that:
   - (i) {{< katex >}}71 \equiv x \pmod{8}{{< /katex >}}
   - (ii) {{< katex >}}78 + x \equiv 3 \pmod{5}{{< /katex >}}
   - (iii) {{< katex >}}89 \equiv (x + 3) \pmod{4}{{< /katex >}}
   - (iv) {{< katex >}}96 \equiv \frac{x}{7} \pmod{5}{{< /katex >}}
   - (v) {{< katex >}}5x \equiv 4 \pmod{6}{{< /katex >}}

2. If {{< katex >}}x{{< /katex >}}
 is congruent to 13 modulo 17 then {{< katex >}}7x - 3{{< /katex >}} is congruent to which number modulo 17?

3. Solve {{< katex >}}5x \equiv 4 \pmod{6}{{< /katex >}}

4. Solve {{< katex >}}3x - 2 \equiv 0 \pmod{11}{{< /katex >}}

5. What is the time 100 hours after 7 a.m.?

6. What is the time 15 hours before 11 p.m.?

7. Today is Tuesday. My uncle will come after 45 days. In which day my uncle will be coming?

8. Prove that {{< katex >}}2^n + 6 \times 9^n{{< /katex >}} 
is always divisible by 7 for any positive integer {{< katex >}}n{{< /katex >}}.

9. Find the remainder when {{< katex >}}2^{81}{{< /katex >}} is divided by 17.

10. The duration of flight travel from Chennai to London through British Airlines is approximately 11 hours. The airplane begins its journey on Sunday at 23:30 hours. If the time at Chennai is four and half hours ahead to that of London's time, then find the time at London, when will the flight lands at London Airport.

---
