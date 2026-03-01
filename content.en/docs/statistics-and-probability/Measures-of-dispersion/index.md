---
title: 'Measures of Dispersion'
weight: 2
extensions:
- katex
---
# 8.2 Measures of Dispersion

The following data provide the runs scored by two batsmen in the last 10 matches.

Batsman A: 25, 20, 45, 93, 8, 14, 32, 87, 72, 4

Batsman B: 33, 50, 47, 38, 45, 40, 36, 48, 37, 26

Mean of Batsman A = (25 + 20 + 45 + 93 + 8 + 14 + 32 + 87 + 72 + 4) / 10 = 40

Mean of Batsman B = (33 + 50 + 47 + 38 + 45 + 40 + 36 + 48 + 37 + 26) / 10 = 40

The mean of both datas are same (40), but they differ significantly.

![Fig. 8.1(a) - Batsman A](image5.png)

![Fig. 8.1(b) - Batsman B](image11.png)

From the above diagrams, we see that runs of batsman B are grouped around the mean. But the runs of batsman A are scattered from 0 to 100, though they both have same mean.

Thus, some additional statistical information may be required to determine how the values are spread in data. For this, we shall discuss Measures of Dispersion.

**Dispersion** is a measure which gives an idea about the scatteredness of the values.

**Measures of Variation (or) Dispersion** of a data provide an idea of how observations spread out (or) scattered throughout the data.

---

### Different Measures of Dispersion are

1. Range
2. Mean deviation
3. Quartile deviation
4. Standard deviation
5. Variance
6. Coefficient of Variation

---

## 8.2.1 Range

The difference between the largest value and the smallest value is called Range.

Range R = L − S

Coefficient of range = (L − S) / (L + S)

where L - Largest value; S - Smallest value

> **Progress Check**
>
> The range of first 10 prime numbers is \_\_\_\_\_\_\_

---

### Example 8.1

Find the range and coefficient of range of the following data: 25, 67, 48, 53, 18, 39, 44.

**Solution**

Largest value L = 67; Smallest value S = 18

Range R = L − S = 67 − 18 = 49

Coefficient of range = (L − S) / (L + S)

Coefficient of range = (67 − 18) / (67 + 18) = 49/85 = **0.576**

---

### Example 8.2

Find the range of the following distribution.

| Age (in years) | 16-18 | 18-20 | 20-22 | 22-24 | 24-26 | 26-28 |
|---|---|---|---|---|---|---|
| Number of students | 0 | 4 | 6 | 8 | 2 | 2 |

**Solution**

Here Largest value L = 28

Smallest value S = 16

Range R = L − S

R = 28 − 16 = **12 Years**

> **Note**
>
> If the frequency of initial class is zero, then the next class will be considered for the calculation of range.

---

### Example 8.3

The range of a set of data is 13.67 and the largest value is 70.08. Find the smallest value.

**Solution**

Range R = 13.67

Largest value L = 70.08

Range R = L − S

13.67 = 70.08 − S

S = 70.08 − 13.67 = **56.41**

Therefore, the smallest value is 56.41.

> **Note**
>
> The range of a set of data does not give the clear idea about the dispersion of the data from measures of Central Tendency. For this, we need a measure which depend upon the deviation from the measures of Central Tendency.

---

## 8.2.2 Deviations from the mean

For a given data with n observations x₁, x₂, ... xₙ, the deviations from the mean x̄ are x₁ − x̄, x₂ − x̄, …, xₙ − x̄.

---

## 8.2.3 Squares of deviations from the mean

The squares of deviations from the mean x̄ of the observations x₁, x₂, …, xₙ are

(x₁ − x̄)², (x₂ − x̄)², ..., (xₙ − x̄)² or Σ(xᵢ − x̄)², i = 1 to n

> **Note**
>
> We note that (xᵢ − x̄) ≥ 0 for all observations xᵢ, i = 1, 2, 3, …, n. If the deviations from the mean (xᵢ − x̄) are small, then the squares of the deviations will be very small.

---

## 8.2.4 Variance

The mean of the squares of the deviations from the mean is called **Variance**. It is denoted by σ² (read as sigma square).

Variance = Mean of squares of deviations

= [(x₁ − x̄)² + (x₂ − x̄)² + ... + (xₙ − x̄)²] / n

Variance σ² = Σ(xᵢ − x̄)² / n, i = 1 to n

> **Thinking Corner**
>
> Can variance be negative?

---

## 8.2.5 Standard Deviation

The positive square root of Variance is called **Standard deviation**. That is, standard deviation is the positive square root of the mean of the squares of deviations of the given values from their mean. It is denoted by σ.

Standard deviation gives a clear idea about how far the values are spreading or deviating from the mean.

Standard deviation σ = √[Σ(xᵢ − x̄)² / n], i = 1 to n

> **Do You Know?**
>
> Karl Pearson was the first person to use the word standard deviation. German mathematician Gauss used the word Mean error.

> **Note**
>
> The standard deviation and mean have same units in which the data are given.

---

### Calculation of Standard Deviation for ungrouped data

**(i) Direct Method**

Standard deviation σ = √[(Σxᵢ²/n) − (Σxᵢ/n)²]

> **Note**
>
> - While computing standard deviation, arranging data in ascending order is not mandatory.
> - If the data values are given directly then to find standard deviation we can use the formula σ = √[(Σxᵢ²/n) − (Σxᵢ/n)²]
> - If the data values are not given directly but the squares of the deviations from the mean of each observation is given then to find standard deviation we can use the formula σ = √[Σ(xᵢ − x̄)² / n].

---

### Example 8.4

The number of televisions sold in each day of a week are 13, 8, 4, 9, 7, 12, 10. Find its standard deviation.

**Solution**

| xᵢ | xᵢ² |
|---|---|
| 13 | 169 |
| 8 | 64 |
| 4 | 16 |
| 9 | 81 |
| 7 | 49 |
| 12 | 144 |
| 10 | 100 |
| Σxᵢ = 63 | Σxᵢ² = 623 |

Standard deviation σ = √[(Σxᵢ²/n) − (Σxᵢ/n)²]

= √[(623/7) − (63/7)²]

= √[89 − 81] = √8

Hence, **σ ≈ 2.83**

> **Thinking Corner**
>
> Can the standard deviation be more than the variance?

> **Progress Check**
>
> If the variance is 0.49 then the standard deviation is \_\_\_\_\_.

---

**(ii) Mean method**

Another convenient way of finding standard deviation is to use the following formula.

Standard deviation (by mean method) σ = √[Σ(xᵢ − x̄)² / n]

If dᵢ = xᵢ − x̄ are the deviations, then σ = √(Σdᵢ² / n)

---

### Example 8.5

The amount of rainfall in a particular season for 6 days are given as 17.8 cm, 19.2 cm, 16.3 cm, 12.5 cm, 12.8 cm and 11.4 cm. Find its standard deviation.

**Solution**

Arranging the numbers in ascending order we get, 11.4, 12.5, 12.8, 16.3, 17.8, 19.2. Number of observations n = 6

Mean = (11.4 + 12.5 + 12.8 + 16.3 + 17.8 + 19.2) / 6 = 90/6 = 15

| xᵢ | dᵢ = xᵢ − x̄ = x − 15 | dᵢ² |
|---|---|---|
| 11.4 | −3.6 | 12.96 |
| 12.5 | −2.5 | 6.25 |
| 12.8 | −2.2 | 4.84 |
| 16.3 | 1.3 | 1.69 |
| 17.8 | 2.8 | 7.84 |
| 19.2 | 4.2 | 17.64 |
|  | | Σdᵢ² = 51.22 |

Standard deviation σ = √(Σdᵢ² / n) = √(51.22 / 6) = √8.53

Hence, **σ ≈ 2.9**

---

**(iii) Assumed Mean method**

When the mean value is not an integer (since calculations are very tedious in decimal form) then it is better to use the assumed mean method to find the standard deviation.

Let x₁, x₂, x₃, ..., xₙ be the given data values and let x̄ be their mean.

Let dᵢ be the deviation of xᵢ from the assumed mean A, which is usually the middle value or near the middle value of the given data.

dᵢ = xᵢ − A gives, xᵢ = dᵢ + A ...(1)

Σdᵢ = Σ(xᵢ − A) = Σxᵢ − (A + A + A + ... to n times)

Σdᵢ = Σxᵢ − A × n

Σdᵢ/n = Σxᵢ/n − A

d̄ = x̄ − A (or) x̄ = d̄ + A ...(2)

Standard deviation σ = √[Σdᵢ²/n − (Σdᵢ/n)²]

> **Thinking Corner**
>
> For any collection of n values, can you find the value of
> (i) Σ(xᵢ − x̄)  (ii) (Σxᵢ) − x̄

---

### Example 8.6

The marks scored by 10 students in a class test are 25, 29, 30, 33, 35, 37, 38, 40, 44, 48. Find the standard deviation.

**Solution**

The mean of marks is 35.9 which is not an integer. Hence we take assumed mean, A = 35, n = 10.

| xᵢ | dᵢ = xᵢ − A = xᵢ − 35 | dᵢ² |
|---|---|---|
| 25 | −10 | 100 |
| 29 | −6 | 36 |
| 30 | −5 | 25 |
| 33 | −2 | 4 |
| 35 | 0 | 0 |
| 37 | 2 | 4 |
| 38 | 3 | 9 |
| 40 | 5 | 25 |
| 44 | 9 | 81 |
| 48 | 13 | 169 |
| Σdᵢ = 9 | | Σdᵢ² = 453 |

Standard deviation σ = √[Σdᵢ²/n − (Σdᵢ/n)²]

= √[(453/10) − (9/10)²]

= √[45.3 − 0.81]

= √44.49

**σ ≈ 6.67**

---

**(iv) Step deviation method**

Let x₁, x₂, x₃, ..., xₙ be the given data. Let A be the assumed mean. Let c be the common divisor of xᵢ − A.

Let dᵢ = (xᵢ − A) / c

Then xᵢ = dᵢc + A ...(1)

Σxᵢ = Σ(dᵢc + A) = cΣdᵢ + A × n

Σxᵢ/n = c(Σdᵢ/n) + A

x̄ = cd̄ + A ...(2)

xᵢ − x̄ = cdᵢ + A − cd̄ − A = c(dᵢ − d̄) (using (1) and (2))

σ = c × √[Σdᵢ²/n − (Σdᵢ/n)²]

> **Note**
>
> We can use any of the above methods for finding the standard deviation.

> **Activity 1**
>
> Find the standard deviation of the marks obtained by you in all five subjects in the quarterly examination and in the midterm test separately. What do you observe from your results.

---

### Example 8.7

The amount that the children have spent for purchasing some eatables in one day trip of a school are 5, 10, 15, 20, 25, 30, 35, 40. Using step deviation method, find the standard deviation of the amount they have spent.

**Solution**

We note that all the observations are divisible by 5. Hence we can use the step deviation method. Let the Assumed mean A = 20, n = 8.

| xᵢ | dᵢ = xᵢ − A = xᵢ − 20 | dᵢ = (xᵢ − A)/c, c = 5 | dᵢ² |
|---|---|---|---|
| 5 | −15 | −3 | 9 |
| 10 | −10 | −2 | 4 |
| 15 | −5 | −1 | 1 |
| 20 | 0 | 0 | 0 |
| 25 | 5 | 1 | 1 |
| 30 | 10 | 2 | 4 |
| 35 | 15 | 3 | 9 |
| 40 | 20 | 4 | 16 |
| | Σdᵢ = 4 | | Σdᵢ² = 44 |

Standard deviation σ = c × √[Σdᵢ²/n − (Σdᵢ/n)²]

= √[(44/8) − (4/8)²] × 5

= √[11/2 − 1/4] × 5

= √[5.5 − 0.25] × 5 = 2.29 × 5

**σ ≈ 11.45**

---

### Example 8.8

Find the standard deviation of the following data 7, 4, 8, 10, 11. Add 3 to all the values then find the standard deviation for the new values.

**Solution**

Arranging the values in ascending order we get, 4, 7, 8, 10, 11 and n = 5

| xᵢ | xᵢ² |
|---|---|
| 4 | 16 |
| 7 | 49 |
| 8 | 64 |
| 10 | 100 |
| 11 | 121 |
| Σxᵢ = 40 | Σxᵢ² = 350 |

Standard deviation σ = √[(Σxᵢ²/n) − (Σxᵢ/n)²]

= √[(350/5) − (40/5)²]

**σ = √6 ≈ 2.45**

When we add 3 to all the values, we get the new values as 7, 10, 11, 13, 14.

| xᵢ | xᵢ² |
|---|---|
| 7 | 49 |
| 10 | 100 |
| 11 | 121 |
| 13 | 169 |
| 14 | 196 |
| Σxᵢ = 55 | Σxᵢ² = 635 |

Standard deviation σ = √[(Σxᵢ²/n) − (Σxᵢ/n)²]

= √[(635/5) − (55/5)²]

**σ = √6 ≈ 2.45**

**We see that the standard deviation will not change when we add some fixed constant k to all the values.**

---

### Example 8.9

Find the standard deviation of the data 2, 3, 5, 7, 8. Multiply each data by 4. Find the standard deviation of the new values.

**Solution**

Given, n = 5

| xᵢ | xᵢ² |
|---|---|
| 2 | 4 |
| 3 | 9 |
| 5 | 25 |
| 7 | 49 |
| 8 | 64 |
| Σxᵢ = 25 | Σxᵢ² = 151 |

Standard deviation σ = √[(Σxᵢ²/n) − (Σxᵢ/n)²]

= √[(151/5) − (25/5)²] = √[30.2 − 25] = √5.2 **≈ 2.28**

When we multiply each data by 4, we get the new values as 8, 12, 20, 28, 32.

| xᵢ | xᵢ² |
|---|---|
| 8 | 64 |
| 12 | 144 |
| 20 | 400 |
| 28 | 784 |
| 32 | 1024 |
| Σxᵢ = 100 | Σxᵢ² = 2416 |

Standard deviation σ = √[(Σxᵢ²/n) − (Σxᵢ/n)²]

= √[(2416/5) − (100/5)²] = √[483.2 − 400] = √83.2

σ = √(16 × 5.2) = 4√5.2 **≈ 9.12**

**We see that when we multiply each data by some fixed constant k the standard deviation also get multiplied by k.**

---

### Example 8.10

Find the mean and variance of the first n natural numbers.

**Solution**

Mean x̄ = Sum of all the observations / Number of observations

= Σxᵢ/n = (1 + 2 + 3 + ... + n) / n = n(n+1) / (2 × n)

**Mean x̄ = (n + 1) / 2**

Variance σ² = (Σxᵢ²/n) − (Σxᵢ/n)²

[Σxᵢ² = 1² + 2² + 3² + ... + n²]

[(Σxᵢ)² = (1 + 2 + 3 + ... + n)²]

= [n(n+1)(2n+1) / (6 × n)] − [n(n+1) / (2 × n)]²

= (2n² + 3n + 1)/6 − (n² + 2n + 1)/4

**Variance σ² = (n² − 1) / 12**

---

### Calculation of Standard deviation for grouped data

**(i) Mean method**

Standard deviation σ = √[Σfᵢ(xᵢ − x̄)² / N]

dᵢ = xᵢ − x̄

σ = √(Σfᵢdᵢ² / N), where N = Σfᵢ, i = 1 to n

(fᵢ are frequency values of the corresponding data points xᵢ)

---

### Example 8.11

48 students were asked to write the total number of hours per week they spent on watching television. With this information find the standard deviation of hours spent for watching television.

| x | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|
| f | 3 | 6 | 9 | 13 | 8 | 5 | 4 |

**Solution**

| xᵢ | fᵢ | xᵢfᵢ | dᵢ = xᵢ − x̄ | dᵢ² | fᵢdᵢ² |
|---|---|---|---|---|---|
| 6 | 3 | 18 | −3 | 9 | 27 |
| 7 | 6 | 42 | −2 | 4 | 24 |
| 8 | 9 | 72 | −1 | 1 | 9 |
| 9 | 13 | 117 | 0 | 0 | 0 |
| 10 | 8 | 80 | 1 | 1 | 8 |
| 11 | 5 | 55 | 2 | 4 | 20 |
| 12 | 4 | 48 | 3 | 9 | 36 |
| N = 48 | | Σxᵢfᵢ = 432 | Σdᵢ = 0 | | Σfᵢdᵢ² = 124 |

Mean x̄ = Σxᵢfᵢ / N = 432/48 = 9 (∵ N = Σfᵢ)

Standard deviation σ = √(Σfᵢdᵢ² / N) = √(124/48) = √2.58

**σ ≈ 1.6**

---

**(ii) Assumed Mean method**

Let x₁, x₂, x₃, ..., xₙ be the given data with frequencies f₁, f₂, f₃, ..., fₙ respectively. Let x̄ be their mean and A be the assumed mean.

dᵢ = xᵢ − A

Standard deviation, σ = √[(Σfᵢdᵢ²/N) − (Σfᵢdᵢ/N)²]

---

### Example 8.12

The marks scored by the students in a slip test are given below. Find the standard deviation of their marks.

| x | 4 | 6 | 8 | 10 | 12 |
|---|---|---|---|---|---|
| f | 7 | 3 | 5 | 9 | 5 |

**Solution**

Let the assumed mean, A = 8

| xᵢ | fᵢ | dᵢ = xᵢ − A | fᵢdᵢ | fᵢdᵢ² |
|---|---|---|---|---|
| 4 | 7 | −4 | −28 | 112 |
| 6 | 3 | −2 | −6 | 12 |
| 8 | 5 | 0 | 0 | 0 |
| 10 | 9 | 2 | 18 | 36 |
| 12 | 5 | 4 | 20 | 80 |
| N = 29 | | | Σfᵢdᵢ = 4 | Σfᵢdᵢ² = 240 |

Standard deviation σ = √[(Σfᵢdᵢ²/N) − (Σfᵢdᵢ/N)²]

= √[(240/29) − (4/29)²]

= √[(240 × 29 − 16) / (29 × 29)]

= √(6944 / (29 × 29))

**σ ≈ 2.87**

---

### Calculation of Standard deviation for continuous frequency distribution

**(i) Mean method**

Standard deviation σ = √[Σfᵢ(xᵢ − x̄)² / N]

where xᵢ = Middle value of the i th class.

fᵢ = Frequency of the i th class.

(N = Σfᵢ)

**(ii) Shortcut method (or) Step deviation method**

To make the calculation simple, we provide the following formula. Let A be the assumed mean, xᵢ be the middle value of the i th class and c is the width of the class interval.

dᵢ = (xᵢ − A) / c

σ = c × √[(Σfᵢdᵢ²/N) − (Σfᵢdᵢ/N)²]

---

### Example 8.13

Marks of the students in a particular subject of a class are given below. Find its standard deviation.

| Marks | 0-10 | 10-20 | 20-30 | 30-40 | 40-50 | 50-60 | 60-70 |
|---|---|---|---|---|---|---|---|
| Number of students | 8 | 12 | 17 | 14 | 9 | 7 | 4 |

**Solution**

Let the assumed mean, A = 35, c = 10

| Marks | Mid value (xᵢ) | fᵢ | dᵢ = xᵢ − A | dᵢ = (xᵢ − A)/c | fᵢdᵢ | fᵢdᵢ² |
|---|---|---|---|---|---|---|
| 0-10 | 5 | 8 | −30 | −3 | −24 | 72 |
| 10-20 | 15 | 12 | −20 | −2 | −24 | 48 |
| 20-30 | 25 | 17 | −10 | −1 | −17 | 17 |
| 30-40 | 35 | 14 | 0 | 0 | 0 | 0 |
| 40-50 | 45 | 9 | 10 | 1 | 9 | 9 |
| 50-60 | 55 | 7 | 20 | 2 | 14 | 28 |
| 60-70 | 65 | 4 | 30 | 3 | 12 | 36 |
| | | N = 71 | | | Σfᵢdᵢ = −30 | Σfᵢdᵢ² = 210 |

Standard deviation σ = c × √[(Σfᵢdᵢ²/N) − (Σfᵢdᵢ/N)²]

σ = 10 × √[(210/71) − (−30/71)²]

= 10 × √[210/71 − 900/5041]

= 10 × √2.779

**σ ≈ 16.67**

> **Thinking Corner**
>
> 1. The standard deviation of a data is 2.8, if 5 is added to all the data values then the new standard deviation is \_\_\_.
> 2. If S is the standard deviation of values p, q, r then standard deviation of p−3, q−3, r−3 is \_\_\_.

---

### Example 8.14

The mean and standard deviation of 15 observations are found to be 10 and 5 respectively. On rechecking it was found that one of the observation with value 8 was incorrect. Calculate the correct mean and standard deviation if the correct observation value was 23?

**Solution**

n = 15, x̄ = 10, σ = 5

x̄ = Σx/n; Σx = 15 × 10 = 150

Wrong observation value = 8, Correct observation value = 23.

Correct total = 150 − 8 + 23 = 165

Correct mean x̄ = 165/15 = **11**

Standard deviation σ = √[(Σx²/n) − (Σx/n)²]

Incorrect value of σ = 5 = √[(Σx²/15) − (10)²]

25 = Σx²/15 − 100 ⟹ Σx²/15 = 125

Incorrect value of Σx² = 1875

Correct value of Σx² = 1875 − 8² + 23² = 2340

Correct standard deviation σ = √[(2340/15) − (11)²]

σ = √[156 − 121] = √35

**σ ≈ 5.9**

---

## Exercise 8.1

1. Find the range and coefficient of range of the following data.
   - (i) 63, 89, 98, 125, 79, 108, 117, 68
   - (ii) 43.5, 13.6, 18.9, 38.4, 61.4, 29.8

2. If the range and the smallest value of a set of data are 36.8 and 13.4 respectively, then find the largest value.

3. Calculate the range of the following data.

   | Income | 400-450 | 450-500 | 500-550 | 550-600 | 600-650 |
   |---|---|---|---|---|---|
   | Number of workers | 8 | 12 | 30 | 21 | 6 |

4. A teacher asked the students to complete 60 pages of a record note book. Eight students have completed only 32, 35, 37, 30, 33, 36, 35 and 37 pages. Find the standard deviation of the pages completed by them.

5. Find the variance and standard deviation of the wages of 9 workers given below: ₹310, ₹290, ₹320, ₹280, ₹300, ₹290, ₹320, ₹310, ₹280.

6. A wall clock strikes the bell once at 1 o' clock, 2 times at 2 o' clock, 3 times at 3 o' clock and so on. How many times will it strike in a particular day. Find the standard deviation of the number of strikes the bell make a day.

7. Find the standard deviation of first 21 natural numbers.

8. If the standard deviation of a data is 4.5 and if each value of the data is decreased by 5, then find the new standard deviation.

9. If the standard deviation of a data is 3.6 and each value of the data is divided by 3, then find the new variance and new standard deviation.

10. The rainfall recorded in various places of five districts in a week are given below. Find its standard deviation.

    | Rainfall (in mm) | 45 | 50 | 55 | 60 | 65 | 70 |
    |---|---|---|---|---|---|---|
    | Number of places | 5 | 13 | 4 | 9 | 5 | 4 |

11. In a study about viral fever, the number of people affected in a town were noted as. Find its standard deviation.

    | Age in years | 0-10 | 10-20 | 20-30 | 30-40 | 40-50 | 50-60 | 60-70 |
    |---|---|---|---|---|---|---|---|
    | Number of people affected | 3 | 5 | 16 | 18 | 12 | 7 | 4 |

12. The measurements of the diameters (in cms) of the plates prepared in a factory are given below. Find its standard deviation.

    | Diameter (cm) | 21-24 | 25-28 | 29-32 | 33-36 | 37-40 | 41-44 |
    |---|---|---|---|---|---|---|
    | Number of plates | 15 | 18 | 20 | 16 | 8 | 7 |

13. The time taken by 50 students to complete a 100 meter race are given below. Find its standard deviation.

    | Time taken (sec) | 8.5-9.5 | 9.5-10.5 | 10.5-11.5 | 11.5-12.5 | 12.5-13.5 |
    |---|---|---|---|---|---|
    | Number of students | 6 | 8 | 17 | 10 | 9 |

14. For a group of 100 candidates the mean and standard deviation of their marks were found to be 60 and 15 respectively. Later on it was found that the scores 45 and 72 were wrongly entered as 40 and 27. Find the correct mean and standard deviation.

15. The mean and variance of seven observations are 8 and 16 respectively. If five of these are 2, 4, 10, 12 and 14, then find the remaining two observations.