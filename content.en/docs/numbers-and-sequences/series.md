---
title: 'Series'
weight: 8
---

### 2.8 Series

The sum of the terms of a sequence is called series. Let \( a_1, a_2, a_3, \dots, a_n, \dots \) be the sequence of real numbers. Then the real number

\[
a_1 + a_2 + a_3 + \dots
\]

is defined as the series of real numbers.

If a series has finite number of terms then it is called a Finite series. If a series has infinite number of terms then it is called an Infinite series. Let us focus our attention only on studying finite series.

#### 2.8.1 Sum to \( n \) terms of an A.P.

A series whose terms are in Arithmetic progression is called Arithmetic series.

Let

\[
a, a + d, a + 2d, a + 3d, \dots
\]

be the Arithmetic Progression.

The sum of first \( n \) terms of a Arithmetic Progression denoted by \( S_n \) is given by,

\[
S_n = a + (a + d) + (a + 2d) + \dots + (a + (n - 1)d) \tag{1}
\]

Rewriting the above in reverse order

\[
S_n = (a + (n - 1)d) + (a + (n - 2)d) + \dots + (a + d) + a \tag{2}
\]

Adding (1) and (2) we get,

\[
2S_n = [a + a + (n - 1)d] + [a + d + a + (n - 2)d] + \dots + [a + (n - 2)d + (a + d)] + [a + (n - 1)d + a]
\]

\[
= [2a + (n - 1)d] + [2a + (n - 1)d] + \dots + [2a + (n - 1)d] \quad (n \text{ terms})
\]

\[
2S_n = n \times [2a + (n - 1)d]
\]

\[
\Rightarrow S_n = \frac{n}{2}[2a + (n - 1)d]
\]

#### Note

If the first term \( a \), and the last term \( l \) (\( n^{\text{th}} \) term) are given then

\[
S_n = \frac{n}{2}[2a + (n - 1)d] = \frac{n}{2}[a + a + (n - 1)d]
\]

\[
(\because l = a + (n - 1)d)
\]

\[
S_n = \frac{n}{2}[a + l]
\]

#### Progress Check

1. The sum of terms of a sequence is called ______.

2. If a series have finite number of terms then it is called ______.

3. A series whose terms are in ______ is called Arithmetic series.

4. If the first and last terms of an A.P. are given, then the formula to find the sum is ______.

#### Example 2.31

Find the sum of first 15 terms of the A.P. \( 8, 7\frac{1}{4}, 6\frac{1}{2}, 5\frac{3}{4}, \dots \)

#### Solution

Here the first term \( a = 8 \), common difference

\[
d = 7\frac{1}{4} - 8 = -\frac{3}{4}
\]

Sum of first \( n \) terms of an A.P.

\[
S_n = \frac{n}{2}[2a + (n - 1)d]
\]

\[
S_{15} = \frac{15}{2}\left[2 \times 8 + (15 - 1)\left(-\frac{3}{4}\right)\right]
\]

\[
S_{15} = \frac{15}{2}\left[16 - \frac{21}{2}\right] = \frac{165}{4}
\]

#### Example 2.32

Find the sum of \( 0.40 + 0.43 + 0.46 + \dots + 1 \).

#### Solution

Here the value of \( n \) is not given. But the last term is given. From this, we can find the value of \( n \).

Given, \( a = 0.40 \) and \( l = 1 \), we find \( d = 0.43 - 0.40 = 0.03 \).

\[
l = a + (n - 1)d
\]

\[
1 = 0.40 + (n - 1)(0.03)
\]

\[
0.60 = (n - 1)(0.03)
\]

\[
n - 1 = 20
\]

\[
n = 21
\]

Sum of first \( n \) terms of an A.P.

\[
S_n = \frac{n}{2}[a + l]
\]

\[
S_{21} = \frac{21}{2}[0.40 + 1] = 14.7
\]

So, the sum of 21 terms of the given series is 14.7.

#### Example 2.33

How many terms of the series \( 1 + 5 + 9 + \dots \) must be taken so that their sum is 190?

#### Solution

Here we have to find the value of \( n \), such that \( S_n = 190 \).

First term \( a = 1 \), common difference \( d = 5 - 1 = 4 \).

Sum of first \( n \) terms of an A.P.

\[
S_n = \frac{n}{2}[2a + (n - 1)d] = 190
\]

\[
\frac{n}{2}[2 \times 1 + (n - 1) \times 4] = 190
\]

\[
n[4n - 2] = 380
\]

\[
2n^2 - n - 190 = 0
\]

\[
(n - 10)(2n + 19) = 0
\]

But, \( n = 10 \) as \( n = -\frac{19}{2} \) is impossible. Therefore, \( n = 10 \).

#### Progress Check

State True or False. Justify it.

1. The \( n^{\text{th}} \) term of any A.P. is of the form \( pn + q \) where \( p \) and \( q \) are some constants.

2. The sum to \( n^{\text{th}} \) term of any A.P. is of the form \( pn^2 + qn + r \) where \( p, q, r \) are some constants.

#### Example 2.34

The \( 13^{\text{th}} \) term of an A.P. is 3 and the sum of first 13 terms is 234. Find the common difference and the sum of first 21 terms.

#### Solution

Given, the \( 13^{\text{th}} \) term \( = 3 \)

\[
t_{13} = a + 12d = 3 \tag{1}
\]

Sum of first 13 terms \( = 234 \)

\[
S_{13} = \frac{13}{2}[2a + 12d] = 234
\]

\[
13(2a + 12d) = 468
\]

\[
2a + 12d = 36 \tag{2}
\]

Solving (1) and (2) we get,

From (1): \( a + 12d = 3 \)

From (2): \( 2a + 12d = 36 \)

Subtracting: \( a = 33 \)

Substituting \( a = 33 \) in (1):

\[
33 + 12d = 3 \Rightarrow 12d = -30 \Rightarrow d = -\frac{5}{2}
\]

Therefore, common difference is \( -\frac{5}{2} \).

Sum of first 21 terms

\[
S_{21} = \frac{21}{2}\left[2 \times 33 + (21 - 1) \times \left(-\frac{5}{2}\right)\right]
\]

\[
= \frac{21}{2}[66 - 50] = 168
\]

#### Example 2.35

In an A.P. the sum of first \( n \) terms is \( \frac{5n^2}{2} + \frac{3n}{2} \). Find the \( 17^{\text{th}} \) term.

#### Solution

The \( 17^{\text{th}} \) term can be obtained by subtracting the sum of first 16 terms from the sum of first 17 terms

\[
S_{17} = \frac{5 \times (17)^2}{2} + \frac{3 \times 17}{2} = \frac{1445}{2} + \frac{51}{2} = 748
\]

\[
S_{16} = \frac{5 \times (16)^2}{2} + \frac{3 \times 16}{2} = \frac{1280}{2} + \frac{48}{2} = 664
\]

\[
t_{17} = S_{17} - S_{16} = 748 - 664 = 84
\]

#### Example 2.36

Find the sum of all natural numbers between 300 and 600 which are divisible by 7.

#### Solution

The natural numbers between 300 and 600 which are divisible by 7 are

\[
301, 308, 315, \dots, 595
\]

The sum of all natural numbers between 300 and 600 is

\[
301 + 308 + 315 + \dots + 595
\]

The terms of the above series are in A.P.

First term \( a = 301 \); common difference \( d = 7 \); Last term \( l = 595 \).

\[
n = \left(\frac{l - a}{d}\right) + 1 = \left(\frac{595 - 301}{7}\right) + 1 = 43
\]

\[
\therefore S_n = \frac{n}{2}[a + l]
\]

\[
S_{43} = \frac{43}{2}[301 + 595] = 19264
\]

#### Example 2.37

A mosaic is designed in the shape of an equilateral triangle, 12 ft on each side. Each tile in the mosaic is in the shape of an equilateral triangle of 12 inch side. The tiles are alternate in colour as shown in the figure. Find the number of tiles of each colour and total number of tiles in the mosaic.

#### Solution

Since the mosaic is in the shape of an equilateral triangle of 12 feet, and the tile is in the shape of an equilateral triangle of 12 inch (1 feet), there will be 12 rows in the mosaic.

<center>Fig.2.12</center>

From the figure, it is clear that number of white tiles in each row are 1, 2, 3, 4, ..., 12 which clearly forms an Arithmetic Progression.

Similarly the number of blue tiles in each row are 0, 1, 2, 3, ..., 11 which is also an Arithmetic Progression.

Number of white tiles

\[
= 1 + 2 + 3 + \dots + 12 = \frac{12}{2}[2 \times 1 + (12 - 1) \times 1] = 78
\]

Number of blue tiles

\[
= 0 + 1 + 2 + 3 + \dots + 11 = \frac{12}{2}[2 \times 0 + (12 - 1) \times 1] = 66
\]

The total number of tiles in the mosaic

\[
= 78 + 66 = 144
\]

#### Example 2.38

The houses of a street are numbered from 1 to 49. Senthil's house is numbered such that the sum of numbers of the houses prior to Senthil's house is equal to the sum of numbers of the houses following Senthil's house. Find Senthil's house number?

#### Solution

Let Senthil's house number be \( x \).

It is given that

\[
1 + 2 + 3 + \dots + (x - 1) = (x + 1) + (x + 2) + \dots + 49
\]

\[
1 + 2 + 3 + \dots + (x - 1) = [1 + 2 + 3 + \dots + 49] - [1 + 2 + 3 + \dots + x]
\]

\[
\frac{(x - 1)(x - 1 + 1)}{2} = \frac{49 \times 50}{2} - \frac{x(x + 1)}{2}
\]

\[
\frac{x(x - 1)}{2} = \frac{2450}{2} - \frac{x(x + 1)}{2}
\]

\[
\frac{x^2 - x}{2} = 1225 - \frac{x^2 + x}{2}
\]

\[
x^2 - x = 2450 - x^2 - x
\]

\[
2x^2 = 2450
\]

\[
x^2 = 1225 \Rightarrow x = 35
\]

Therefore, Senthil's house number is 35.

#### Example 2.39

The sum of first \( n \), \( 2n \) and \( 3n \) terms of an A.P. are \( S_1, S_2 \) and \( S_3 \) respectively. Prove that

\[
S_3 = 3(S_2 - S_1)
\]

#### Solution

If \( S_1, S_2 \) and \( S_3 \) are sum of first \( n \), \( 2n \) and \( 3n \) terms of an A.P. respectively then

\[
S_1 = \frac{n}{2}[2a + (n - 1)d]
\]

\[
S_2 = \frac{2n}{2}[2a + (2n - 1)d]
\]

\[
S_3 = \frac{3n}{2}[2a + (3n - 1)d]
\]

Consider,

\[
S_2 - S_1 = \frac{2n}{2}[2a + (2n - 1)d] - \frac{n}{2}[2a + (n - 1)d]
\]

\[
= n[2a + (2n - 1)d] - \frac{n}{2}[2a + (n - 1)d]
\]

\[
= \frac{n}{2}[4a + (4n - 2)d - 2a - (n - 1)d]
\]

\[
= \frac{n}{2}[2a + (3n - 1)d]
\]

Now,

\[
3(S_2 - S_1) = \frac{3n}{2}[2a + (3n - 1)d] = S_3
\]

#### Thinking Corner

1. What is the sum of first \( n \) odd natural numbers?

2. What is the sum of first \( n \) even natural numbers?

### Exercise 2.5

1. Find the sum of the following

(i) 3, 7, 11, ... up to 40 terms.

(ii) 102, 97, 92, ... up to 27 terms.

(iii) \( 6 + 13 + 20 + \dots + 97 \)

2. How many consecutive odd integers beginning with 5 will sum to 480?

3. Find the sum of first 28 terms of an A.P. whose \( n^{\text{th}} \) term is \( 4n - 3 \).

4. The sum of first \( n \) terms of a certain series is given as \( 2n^2 - 3n \). Show that the series is an A.P.

5. The \( 104^{\text{th}} \) term and \( 4^{\text{th}} \) term of an A.P. are 125 and 0. Find the sum of first 35 terms.

6. Find the sum of all odd positive integers less than 450.

7. Find the sum of all natural numbers between 602 and 902 which are not divisible by 4.

8. Raghu wish to buy a laptop. He can buy it by paying \( ₹40,000 \) cash or by giving it in 10 installments as \( ₹4800 \) in the first month, \( ₹4750 \) in the second month, \( ₹4700 \) in the third month and so on. If he pays the money in this fashion, find

(i) total amount paid in 10 installments.

(ii) how much extra amount that he has to pay than the cost?

9. A man repays a loan of \( ₹65,000 \) by paying \( ₹400 \) in the first month and then increasing the payment by \( ₹300 \) every month. How long will it take for him to clear the loan?

10. A brick staircase has a total of 30 steps. The bottom step requires 100 bricks. Each successive step requires two bricks less than the previous step.

(i) How many bricks are required for the top most step?

(ii) How many bricks are required to build the stair case?

11. If \( S_1, S_2, S_3, \dots, S_m \) are the sums of \( n \) terms of \( m \) A.P's whose first terms are 1, 2, 3, ..., \( m \) and whose common differences are 1, 3, 5, ..., \( (2m - 1) \) respectively, then show that

\[
S_1 + S_2 + S_3 + \dots + S_m = \frac{1}{2} mn(mn + 1)
\]

12. Find the sum

\[
\frac{a - b}{a + b} + \frac{3a - 2b}{a + b} + \frac{5a - 3b}{a + b} + \dots \text{ to } 12 \text{ terms}
\]