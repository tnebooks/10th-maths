---
title: 'Sum to n terms of a Geometric Progression'
weight: 10
---

### 2.10 Sum to \( n \) terms of a Geometric progression

A series whose terms are in Geometric progression is called Geometric series.

Let

\[
a, ar, ar^2, \dots, ar^{n-1}, \dots
\]

be the Geometric Progression.

The sum of first \( n \) terms of the Geometric progression is

\[
S_n = a + ar + ar^2 + \dots + ar^{n-2} + ar^{n-1} \tag{1}
\]

Multiplying both sides by \( r \), we get

\[
rS_n = ar + ar^2 + ar^3 + \dots + ar^{n-1} + ar^n \tag{2}
\]

\[
(2) - (1) \Rightarrow rS_n - S_n = ar^n - a
\]

\[
S_n(r - 1) = a(r^n - 1)
\]

Thus, the sum to \( n \) terms is

\[
S_n = \frac{a(r^n - 1)}{r - 1}, \quad r \neq 1
\]

#### Note

The above formula for sum of first \( n \) terms of a G.P. is not applicable when \( r = 1 \).

If \( r = 1 \), then

\[
S_n = a + a + a + \dots + a = na
\]

#### Progress Check

1. A series whose terms are in Geometric progression is called ______.

2. When \( r = 1 \), the formula for finding sum to \( n \) terms of a G.P. is ______.

3. When \( r \neq 1 \), the formula for finding sum to \( n \) terms of a G.P. is ______.

#### 2.10.1 Sum to infinite terms of a G.P.

The sum of infinite terms of a G.P. is given by

\[
S_{\infty} = a + ar + ar^2 + ar^3 + \dots = \frac{a}{1 - r}, \quad -1 < r < 1
\]

#### Example 2.46

Find the sum of 8 terms of the G.P. \( 1, -3, 9, -27, \dots \)

#### Solution

Here, the first term \( a = 1 \), common ratio

\[
r = \frac{-3}{1} = -3 < 1
\]

Here, \( n = 8 \).

Sum to \( n \) terms of a G.P. is

\[
S_n = \frac{a(r^n - 1)}{r - 1} \quad \text{if } r \neq 1
\]

\[
S_8 = \frac{1((-3)^8 - 1)}{(-3) - 1}
\]

\[
= \frac{6561 - 1}{-4} = -1640
\]

#### Example 2.47

Find the first term of a G.P. in which \( S_6 = 4095 \) and \( r = 4 \).

#### Solution

Common ratio \( = 4 > 1 \), Sum of first 6 terms \( S_6 = 4095 \)

\[
S_6 = \frac{a(r^n - 1)}{r - 1} = 4095
\]

\[
\therefore r = 4, \quad \frac{a(4^6 - 1)}{4 - 1} = 4095
\]

\[
a \times \frac{4095}{3} = 4095
\]

\[
\text{First term } a = 3
\]

#### Example 2.48

How many terms of the series \( 1 + 4 + 16 + \dots \) make the sum 1365?

#### Solution

Let \( n \) be the number of terms to be added to get the sum 1365

\[
a = 1, \quad r = \frac{4}{1} = 4 > 1
\]

\[
S_n = 1365 \Rightarrow \frac{a(r^n - 1)}{r - 1} = 1365
\]

\[
\frac{1(4^n - 1)}{4 - 1} = 1365
\]

\[
4^n - 1 = 4095
\]

\[
4^n = 4096
\]

\[
4^n = 4^6
\]

\[
n = 6
\]

#### Example 2.49

Find the sum \( 3 + 1 + \frac{1}{3} + \dots \infty \)

#### Solution

Here \( a = 3 \),

\[
r = \frac{t_2}{t_1} = \frac{1}{3}
\]

Sum of infinite terms

\[
S_{\infty} = \frac{a}{1 - r} = \frac{3}{1 - \frac{1}{3}} = \frac{9}{2}
\]

#### Example 2.50

Find the rational form of the number \( 0.6666\dots \)

#### Solution

We can express the number \( 0.6666\dots \) as follows

\[
0.6666\dots = 0.6 + 0.06 + 0.006 + 0.0006 + \dots
\]

We now see that numbers 0.6, 0.06, 0.006, ... form a G.P. whose first term \( a = 0.6 \) and common ratio

\[
r = \frac{0.06}{0.6} = 0.1
\]

Also \( -1 < r = 0.1 < 1 \)

Using the infinite G.P. formula, we have

\[
0.6666\dots = 0.6 + 0.06 + 0.006 + 0.0006 + \dots = \frac{0.6}{1 - 0.1} = \frac{0.6}{0.9} = \frac{2}{3}
\]

Thus the rational number equivalent of \( 0.6666\dots \) is \( \frac{2}{3} \)

#### Example 2.51

<center>Fig.2.15</center>

The sides of a given square is \( 10\text{ cm} \). The mid points of its sides are joined to form a new square. Again, the mid points of the sides of this new square are joined to form another square. This process is continued indefinitely. Find the sum of the areas and the sum of the perimeters of the squares formed through this process.

#### Example 2.52

Find the sum to \( n \) terms of the series \( 5 + 55 + 555 + \dots \)

#### Solution

The series is neither Arithmetic nor Geometric series. So it can be split into two series and then find the sum.

\[
5 + 55 + 555 + \dots + n \text{ terms} = 5[1 + 11 + 111 + \dots + n \text{ terms}]
\]

\[
= \frac{5}{9}[9 + 99 + 999 + \dots + n \text{ terms}]
\]

\[
= \frac{5}{9}[(10 - 1) + (100 - 1) + (1000 - 1) + \dots + n \text{ terms}]
\]

\[
= \frac{5}{9}[(10 + 100 + 1000 + \dots + n \text{ terms}) - n]
\]

\[
= \frac{5}{9}\left[\frac{10(10^n - 1)}{(10 - 1)} - n\right]
\]

\[
= \frac{50(10^n - 1)}{81} - \frac{5n}{9}
\]

#### Progress Check

1. Is the series \( 3 + 33 + 333 + \dots \) a Geometric series?

2. The value of \( r \), such that \( 1 + r + r^2 + r^3 \dots = \frac{3}{4} \) is ______.

#### Example 2.53

Find the least positive integer \( n \) such that

\[
1 + 6 + 6^2 + \dots + 6^n > 5000
\]

#### Solution

We have to find the least number of terms for which the sum must be greater than 5000.

That is, to find the least value of \( n \) such that \( S_n > 5000 \)

\[
S_n = \frac{a(r^n - 1)}{r - 1} = \frac{1(6^n - 1)}{6 - 1} = \frac{6^n - 1}{5}
\]

\[
S_n > 5000 \Rightarrow \frac{6^n - 1}{5} > 5000
\]

\[
6^n - 1 > 25000 \Rightarrow 6^n > 25001
\]

\[
\therefore 6^5 = 7776 \text{ and } 6^6 = 46656
\]

The least positive value of \( n \) is 6 such that \( 1 + 6 + 6^2 + \dots + 6^n > 5000 \).

#### Example 2.54

A person saved money every year, half as much as he could in the previous year. If he had totally saved \( ₹7875 \) in 6 years then how much did he save in the first year?

#### Solution

Total amount saved in 6 years is \( S_n = 7875 \)

Since he saved half as much money as every year he saved in the previous year,

\[
\text{We have } r = \frac{1}{2} < 1
\]

\[
\frac{a(1 - r^n)}{1 - r} = 7875
\]

\[
\frac{a\left(1 - \left(\frac{1}{2}\right)^6\right)}{1 - \frac{1}{2}} = 7875
\]

\[
\frac{a\left(1 - \frac{1}{64}\right)}{\frac{1}{2}} = 7875
\]

\[
a \times \frac{63}{64} \times 2 = 7875
\]

\[
a \times \frac{63}{32} = 7875
\]

\[
a = \frac{7875 \times 32}{63}
\]

\[
a = 4000
\]

The amount saved in the first year is \( ₹4000 \).

### Exercise 2.7

1. Find the sum of first \( n \) terms of the G.P.

(i) \( 5, -3, \frac{9}{5}, -\frac{27}{25}, \dots \)

(ii) 256, 64, 16, \dots

2. Find the sum of first six terms of the G.P. 5, 15, 45, \dots

3. Find the first term of the G.P. whose common ratio 5 and whose sum to first 6 terms is 46872.

4. Find the sum to infinity of

(i) \( 9 + 3 + 1 + \dots \)

(ii) \( 21 + 14 + \frac{28}{3} + \dots \)

5. If the first term of an infinite G.P. is 8 and its sum to infinity is \( \frac{32}{3} \) then find the common ratio.

6. Find the sum to \( n \) terms of the series

(i) \( 0.4 + 0.44 + 0.444 + \dots \) to \( n \) terms

(ii) \( 3 + 33 + 333 + \dots \) to \( n \) terms

7. Find the sum of the Geometric series \( 3 + 6 + 12 + \dots + 1536 \).

8. Kumar writes a letter to four of his friends. He asks each one of them to copy the letter and mail to four different persons with the instruction that they continue the process similarly. Assuming that the process is unaltered and it costs \( ₹2 \) to mail one letter, find the amount spent on postage when \( 8^{\text{th}} \) set of letters is mailed.

9. Find the rational form of the number \( 0.\overline{123} \).

10. If

\[
S_n = \frac{x}{y} + \frac{x(x + y)}{y^2} + \frac{x(x + y)^2}{y^3} + \dots \text{ to } n \text{ terms}
\]

then prove that

\[
(x - y)S_n = \frac{x^2(x^n - 1)}{y^{n-1}(x - y)} - \frac{y(y^n - 1)}{y - 1}
\]