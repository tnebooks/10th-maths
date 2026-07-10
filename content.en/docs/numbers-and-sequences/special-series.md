---
title: 'Special Series'
weight: 11
---

### 2.11 Special Series

There are some series whose sum can be expressed by explicit formulae. Such series are called special series.

Here we study some common special series like

(i) Sum of first \( n \) natural numbers

(ii) Sum of first \( n \) odd natural numbers

(iii) Sum of squares of first \( n \) natural numbers

(iv) Sum of cubes of first \( n \) natural numbers

We can derive the formula for sum of any powers of first \( n \) natural numbers using the expression \( (x + 1)^{k+1} - x^{k+1} \). That is to find

\[
1^k + 2^k + 3^k + \dots + n^k
\]

we can use the expression \( (x + 1)^{k+1} - x^{k+1} \).

#### 2.11.1 Sum of first \( n \) natural numbers

To find \( 1 + 2 + 3 + \dots + n \), let us consider the identity

\[
(x + 1)^2 - x^2 = 2x + 1
\]

Where \( x = 1, 2, 3, \dots, n - 1, n \)

\[
x = 1, \quad 2^2 - 1^2 = 2(1) + 1
\]

\[
x = 2, \quad 3^2 - 2^2 = 2(2) + 1
\]

\[
x = 3, \quad 4^2 - 3^2 = 2(3) + 1
\]

\[
\vdots \quad \vdots \quad \vdots
\]

\[
x = n - 1, \quad n^2 - (n - 1)^2 = 2(n - 1) + 1
\]

\[
x = n, \quad (n + 1)^2 - n^2 = 2n + 1
\]

Adding all these equations and cancelling the terms on the Left Hand side, we get,

\[
(n + 1)^2 - 1^2 = 2(1 + 2 + 3 + \dots + n) + n
\]

\[
n^2 + 2n = 2(1 + 2 + 3 + \dots + n) + n
\]

\[
2(1 + 2 + 3 + \dots + n) = n^2 + n = n(n + 1)
\]

\[
1 + 2 + 3 + \dots + n = \frac{n(n + 1)}{2}
\]

#### 2.11.2 Sum of first \( n \) odd natural numbers

\[
1 + 3 + 5 + \dots + (2n - 1)
\]

It is an A.P. with \( a = 1 \), \( d = 2 \) and \( l = 2n - 1 \)

\[
S_n = \frac{n}{2}[a + l]
\]

\[
= \frac{n}{2}[1 + 2n - 1]
\]

\[
S_n = \frac{n}{2} \times 2n = n^2
\]

#### 2.11.3 Sum of squares of first \( n \) natural numbers

To find \( 1^2 + 2^2 + 3^2 + \dots + n^2 \), let us consider the identity

\[
(x + 1)^3 - x^3 = 3x^2 + 3x + 1
\]

Where \( x = 1, 2, 3, \dots, n - 1, n \)

\[
x = 1, \quad 2^3 - 1^3 = 3(1)^2 + 3(1) + 1
\]

\[
x = 2, \quad 3^3 - 2^3 = 3(2)^2 + 3(2) + 1
\]

\[
x = 3, \quad 4^3 - 3^3 = 3(3)^2 + 3(3) + 1
\]

\[
\vdots \quad \vdots \quad \vdots
\]

\[
x = n - 1, \quad n^3 - (n - 1)^3 = 3(n - 1)^2 + 3(n - 1) + 1
\]

\[
x = n, \quad (n + 1)^3 - n^3 = 3n^2 + 3n + 1
\]

Adding all these equations and cancelling the terms on the Left Hand side, we get,

\[
(n + 1)^3 - 1^3 = 3(1^2 + 2^2 + 3^2 + \dots + n^2) + 3(1 + 2 + 3 + \dots + n) + n
\]

\[
n^3 + 3n^2 + 3n = 3\sum_{k=1}^n k^2 + 3\left(\frac{n(n + 1)}{2}\right) + n
\]

\[
3\sum_{k=1}^n k^2 = n^3 + 3n^2 + 3n - \frac{3n(n + 1)}{2} - n
\]

\[
= n^3 + 3n^2 + 2n - \frac{3n^2 + 3n}{2}
\]

\[
= \frac{2n^3 + 6n^2 + 4n - 3n^2 - 3n}{2}
\]

\[
= \frac{2n^3 + 3n^2 + n}{2}
\]

\[
= \frac{n(2n^2 + 3n + 1)}{2} = \frac{n(n + 1)(2n + 1)}{2}
\]

Thus,

\[
\sum_{k=1}^n k^2 = \frac{n(n + 1)(2n + 1)}{6}
\]

#### 2.11.4 Sum of cubes of first \( n \) natural numbers

To find \( 1^3 + 2^3 + 3^3 + \dots + n^3 \), let us consider the identity

\[
(x + 1)^4 - x^4 = 4x^3 + 6x^2 + 4x + 1
\]

Proceeding as above, we get

\[
1^3 + 2^3 + 3^3 + \dots + n^3 = \left[\frac{n(n + 1)}{2}\right]^2
\]

#### Note

1. The sum of first \( n \) natural numbers are also called Triangular Numbers because they form triangle shapes.

2. The sum of squares of first \( n \) natural numbers are also called Square Pyramidal Numbers because they form pyramid shapes with square base.

<center>Fig. 2.16</center>

#### Thinking Corner

1. How many squares are there in a standard chess board?

2. How many rectangles are there in a standard chess board?

Here is a summary of list of some useful summation formulae which we discussed. These formulae are used in solving summation problems with finite terms.

\[
\sum_{k=1}^n k = 1 + 2 + 3 + \dots + n = \frac{n(n + 1)}{2}
\]

\[
\sum_{k=1}^n (2k - 1) = 1 + 3 + 5 + \dots + (2n - 1) = n^2
\]

\[
\sum_{k=1}^n k^2 = 1^2 + 2^2 + 3^2 + \dots + n^2 = \frac{n(n + 1)(2n + 1)}{6}
\]

\[
\sum_{k=1}^n k^3 = 1^3 + 2^3 + 3^3 + \dots + n^3 = \left[\frac{n(n + 1)}{2}\right]^2
\]

#### Example 2.55

Find the sum of

(i) \( 1 + 2 + 3 + \dots + 50 \)

(ii) \( 1^2 + 2^2 + 3^2 + \dots + 50^2 \)

(iii) \( 1^3 + 2^3 + 3^3 + \dots + 50^3 \)

#### Solution

(i) \( 1 + 2 + 3 + \dots + 50 = \frac{50 \times 51}{2} = 1275 \)

(ii) \( 1^2 + 2^2 + 3^2 + \dots + 50^2 = \frac{50 \times 51 \times 101}{6} = 42925 \)

(iii) \( 1^3 + 2^3 + 3^3 + \dots + 50^3 = \left[\frac{50 \times 51}{2}\right]^2 = (1275)^2 = 1625625 \)

#### Example 2.56

Find the sum of

(i) \( 3 + 6 + 9 + \dots + 300 \)

(ii) \( 2^2 + 4^2 + 6^2 + \dots + 100^2 \)

#### Solution

(i) \( 3 + 6 + 9 + \dots + 300 \)

\[
= 3(1 + 2 + 3 + \dots + 100)
\]

\[
= 3 \times \frac{100 \times 101}{2} = 15150
\]

(ii) \( 2^2 + 4^2 + 6^2 + \dots + 100^2 \)

\[
= (2 \times 1)^2 + (2 \times 2)^2 + (2 \times 3)^2 + \dots + (2 \times 50)^2
\]

\[
= 4(1^2 + 2^2 + 3^2 + \dots + 50^2)
\]

\[
= 4 \times \frac{50 \times 51 \times 101}{6} = 171700
\]

#### Example 2.57

Find the sum of

(i) \( 1^3 + 2^3 + 3^3 + \dots + 16^3 \)

(ii) \( 9^3 + 10^3 + \dots + 21^3 \)

#### Solution

(i) \( 1^3 + 2^3 + 3^3 + \dots + 16^3 \)

\[
= \left[\frac{16 \times (16 + 1)}{2}\right]^2 = (136)^2 = 18496
\]

(ii) \( 9^3 + 10^3 + \dots + 21^3 \)

\[
= (1^3 + 2^3 + 3^3 + \dots + 21^3) - (1^3 + 2^3 + 3^3 + \dots + 8^3)
\]

\[
= \left[\frac{21 \times (21 + 1)}{2}\right]^2 - \left[\frac{8 \times (8 + 1)}{2}\right]^2
\]

\[
= (231)^2 - (36)^2 = 53361 - 1296 = 52065
\]

#### Example 2.58

If \( 1 + 2 + 3 + \dots + n = 666 \) then find \( n \).

#### Solution

Since,

\[
1 + 2 + 3 + \dots + n = \frac{n(n + 1)}{2}
\]

we have

\[
\frac{n(n + 1)}{2} = 666
\]

\[
n^2 + n - 1332 = 0
\]

\[
(n + 37)(n - 36) = 0
\]

So, \( n = -37 \) or \( n = 36 \)

But \( n \neq -37 \) ( \( \because n \) is a natural number); Hence \( n = 36 \).

#### Progress Check

Say True or False. Justify them.

1. The sum of first \( n \) odd natural numbers is always an odd number.

2. The sum of consecutive even numbers is always an even number.

3. The difference between the sum of squares of first \( n \) natural numbers and the sum of first \( n \) natural numbers is always divisible by 2.

4. The sum of cubes of the first \( n \) natural numbers is always a square number.

### Exercise 2.8

1. Find the sum of the following series

(i) \( 1 + 2 + 3 + \dots + 60 \)

(ii) \( 3 + 6 + 9 + \dots + 96 \)

(iii) \( 51 + 52 + 53 + \dots + 92 \)

(iv) \( 1 + 4 + 9 + 16 + \dots + 225 \)

(v) \( 6^2 + 7^2 + 8^2 + \dots + 21^2 \)

(vi) \( 10^3 + 11^3 + 12^3 + \dots + 20^3 \)

(vii) \( 1 + 3 + 5 + \dots + 71 \)

2. If \( 1 + 2 + 3 + \dots + k = 325 \), then find

\[
1^3 + 2^3 + 3^3 + \dots + k^3
\]

3. If \( 1^3 + 2^3 + 3^3 + \dots + k^3 = 44100 \) then find

\[
1 + 2 + 3 + \dots + k
\]

4. How many terms of the series \( 1^3 + 2^3 + 3^3 + \dots \) should be taken to get the sum 14400?

5. The sum of the cubes of the first \( n \) natural numbers is 2025, then find the value of \( n \).

6. Rekha has 15 square colour papers of sizes \( 10\text{ cm}, 11\text{ cm}, 12\text{ cm}, \dots, 24\text{ cm} \). How much area can be decorated with these colour papers?

7. Find the sum of the series

\[
(2^3 - 1^3) + (4^3 - 3^3) + (6^3 - 5^3) + \dots
\]

to

(i) \( n \) terms

(ii) 8 terms