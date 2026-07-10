---
title: 'Modular Arithmetic'
weight: 5
---

### 2.5 Modular Arithmetic

In a clock, we use the numbers 1 to 12 to represent the time period of 24 hours. How is it possible to represent the 24 hours of a day in a 12 number format? We use 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 and after 12, we use 1 instead of 13 and 2 instead of 14 and so on. That is after 12 we again start from 1, 2, 3, ... In this system the numbers wrap around 1 to 12. This type of wrapping around after hitting some value is called Modular Arithmetic.

<center>Fig.2.5</center>

In Mathematics, modular arithmetic is a system of arithmetic for integers where numbers wrap around a certain value. Unlike normal arithmetic, Modular Arithmetic process cyclically. The ideas of Modular arithmetic was developed by great German mathematician Carl Friedrich Gauss, who is hailed as the "Prince of mathematicians".

#### Examples

1. The day and night change repeatedly.

2. The days of a week occur cyclically from Sunday to Saturday.

3. The life cycle of a plant.

4. The seasons of a year change cyclically. (Summer, Autumn, Winter, Spring)

5. The railway and aeroplane timings also work cyclically. The railway time starts at 00:00 and continue. After reaching 23:59, the next minute will become 00:00 instead of 24:00.

<center>Fig.2.6</center>

#### 2.5.1 Congruence Modulo

Two integers \( a \) and \( b \) are congruence modulo \( n \) if they differ by an integer multiple of \( n \). That is \( a - b = kn \) for some integer \( k \). This can also be written as

\[
a \equiv b \pmod{n}
\]

Here the number \( n \) is called modulus. In other words, \( a \equiv b \pmod{n} \) means \( a - b \) is divisible by \( n \).

For example, \( 61 \equiv 5 \pmod{7} \) because \( 61 - 5 = 56 \) is divisible by 7.

When a positive integer is divided by \( n \), then the possible remainders are 0, 1, 2, ..., \( n - 1 \).

Thus, when we work with modulo \( n \), we replace all the numbers by their remainders upon division by \( n \), given by 0, 1, 2, 3, ..., \( n - 1 \).

Two illustrations are provided to understand modulo concept more clearly.

#### Illustration 1

To find \( 8 \pmod{4} \)

With a modulus of 4 (since the possible remainders are 0, 1, 2, 3) we make a diagram like a clock with numbers 0, 1, 2, 3. We start at 0 and go through 8 numbers in a clockwise sequence 1, 2, 3, 0, 1, 2, 3, 0. After doing so cyclically, we end at 0.

Therefore, \( 8 \equiv 0 \pmod{4} \)

#### Illustration 2

To find \( -5 \pmod{3} \)

With a modulus of 3 (since the possible remainders are 0, 1, 2) we make a diagram like a clock with numbers 0, 1, 2.

We start at 0 and go through 5 numbers in anti-clockwise sequence 2, 1, 0, 2, 1. After doing so cyclically, we end at 1.

Therefore, \( -5 \equiv 1 \pmod{3} \)

<center>Fig.2.7</center>

<center>Fig.2.8</center>

#### 2.5.2 Connecting Euclid's Division lemma and Modular Arithmetic

Let \( m \) and \( n \) be integers, where \( m \) is positive. Then by Euclid's division lemma, we can write

\[
n = mq + r
\]

where \( 0 \leq r < m \) and \( q \) is an integer. Instead of writing \( n = mq + r \) we can use the congruence notation in the following way.

We say that \( n \) is congruent to \( r \) modulo \( m \), if \( n = mq + r \) for some integer \( q \).

#### Progress Check

1. Two integers \( a \) and \( b \) are congruent modulo \( n \) if ______.

2. The set of all positive integers which leave remainder 5 when divided by 7 are ______.

Thus the equation \( n = mq + r \) through Euclid's Division lemma can also be written as

\[
n \equiv r \pmod{m}
\]

#### 2.5.3 Modulo operations

Similar to basic arithmetic operations like addition, subtraction and multiplication performed on numbers we can think of performing same operations in modulo arithmetic. The following theorem provides the information of doing this.

#### Theorem 5

\( a, b, c \) and \( d \) are integers and \( m \) is a positive integer such that if

\[
a \equiv b \pmod{m}
\]

and

\[
c \equiv d \pmod{m}
\]

then

\[
(i) (a + c) \equiv (b + d) \pmod{m}
\]

\[
(ii) (a - c) \equiv (b - d) \pmod{m}
\]

\[
(iii) (a \times c) \equiv (b \times d) \pmod{m}
\]

#### Illustration 3

If \( 17 \equiv 4 \pmod{13} \) and \( 42 \equiv 3 \pmod{13} \) then from theorem 5,

\[
17 + 42 \equiv 4 + 3 \pmod{13}
\]

\[
59 \equiv 7 \pmod{13}
\]

\[
17 - 42 \equiv 4 - 3 \pmod{13}
\]

\[
-25 \equiv 1 \pmod{13}
\]

\[
17 \times 42 \equiv 4 \times 3 \pmod{13}
\]

\[
714 \equiv 12 \pmod{13}
\]

#### Theorem 6

If \( a \equiv b \pmod{m} \) then

(i) \( ac \equiv bc \pmod{m} \)

(ii) \( a \pm c \equiv b \pm c \pmod{m} \) for any integer \( c \)

#### Progress Check

1. The positive values of \( k \) such that \( (k - 3) \equiv 5 \pmod{11} \) are ______.

2. If \( 59 \equiv 3 \pmod{7} \), \( 46 \equiv 4 \pmod{7} \) then

\( 105 \equiv \) ______ \( \pmod{7} \),

\( 13 \equiv \) ______ \( \pmod{7} \),

\( 413 \equiv \) ______ \( \pmod{7} \),

\( 368 \equiv \) ______ \( \pmod{7} \).

3. The remainder when \( 7 \times 13 \times 19 \times 23 \times 29 \times 31 \) is divided by 6 is ______.

### Exercise 2.2

1. Find the least positive value of \( x \) such that

\[
(i) 71 \equiv x \pmod{8}
\]

\[
(ii) 78 + x \equiv 3 \pmod{5}
\]

\[
(iii) 89 \equiv (x + 3) \pmod{4}
\]

\[
(iv) 96 \equiv \frac{x}{7} \pmod{5}
\]

\[
(v) 5x \equiv 4 \pmod{6}
\]

2. If \( x \) is congruent to 13 modulo 17 then \( 7x - 3 \) is congruent to which number modulo 17?

3. Solve \( 5x \equiv 4 \pmod{6} \)

4. Solve \( 3x - 2 \equiv 0 \pmod{11} \)

5. What is the time 100 hours after 7 a.m.?

6. What is the time 15 hours before 11 p.m.?

7. Today is Tuesday. My uncle will come after 45 days. In which day my uncle will be coming?

8. Prove that \( 2^n + 6 \times 9^n \) is always divisible by 7 for any positive integer \( n \).

9. Find the remainder when \( 2^{81} \) is divided by 17.

10. The duration of flight travel from Chennai to London through British Airlines is approximately 11 hours. The airplane begins its journey on Sunday at 23:30 hours. If the time at Chennai is four and half hours ahead to that of London's time, then find the time at London, when will the flight lands at London Airport.