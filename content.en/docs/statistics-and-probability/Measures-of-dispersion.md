---
title: "Measures of Dispersion"
weight: 2
---

### 8.2 Measures of Dispersion

The following data provide the runs scored by two batsmen in the last 10 matches.

Batsman A: 25, 20, 45, 93, 8, 14, 32, 87, 72, 4

Batsman B: 33, 50, 47, 38, 45, 40, 36, 48, 37, 26

Mean of Batsman A \(= \frac{25 + 20 + 45 + 93 + 8 + 14 + 32 + 87 + 72 + 4}{10} = 40\)

Mean of Batsman B \(= \frac{33 + 50 + 47 + 38 + 45 + 40 + 36 + 48 + 37 + 26}{10} = 40\)

The mean of both datas are same (40), but they differ significantly.

![](image-2.png)
<center>Fig. 8.1(a)</center>

![](image-3.png)
<center>Fig. 8.1(b)</center>

From the above diagrams, we see that runs of batsman \(B\) are grouped around the mean. But the runs of batsman \(A\) are scattered from 0 to 100, though they both have same mean.

Thus, some additional statistical information may be required to determine how the values are spread in data. For this, we shall discuss Measures of Dispersion.

Dispersion is a measure which gives an idea about the scatteredness of the values.

Measures of Variation (or) Dispersion of a data provide an idea of how observations spread out (or) scattered throughout the data.

---

## Different Measures of Dispersion are

1. Range
2. Mean deviation
3. Quartile deviation
4. Standard deviation
5. Variance
6. Coefficient of Variation

---

##### Progress Check


The range of first 10 prime numbers is __________

 ---

#### 8.2.1 Range

The difference between the largest value and the smallest value is called Range.

\[
\text{Range } R = L - S
\]

\[
\text{Coefficient of range} = \frac{L - S}{L + S}
\]

where \(L\) - Largest value; \(S\) - Smallest value.

---

**Example 8.1** Find the range and coefficient of range of the following data: 25, 67, 48, 53, 18, 39, 44.

**Solution** Largest value \(L = 67\); Smallest value \(S = 18\).

Range \(R = L - S = 67 - 18 = 49\)

Coefficient of range \(= \frac{L - S}{L + S} = \frac{67 - 18}{67 + 18} = \frac{49}{85} = 0.576\)

---

**Example 8.2** Find the range of the following distribution.

![](image-4.png)

**Solution** Here Largest value \(L = 28\).

Smallest value \(S = 16\).

Range \(R = L - S = 28 - 16 = 12\) Years.

---

**Example 8.3** The range of a set of data is 13.67 and the largest value is 70.08. Find the smallest value.

**Solution** Range \(R = 13.67\); Largest value \(L = 70.08\).

Range \(R = L - S\)

\[
13.67 = 70.08 - S \Rightarrow S = 70.08 - 13.67 = 56.41
\]

Therefore, the smallest value is 56.41.

---

**Note**


If the frequency of initial class is zero, then the next class will be considered for the calculation of range.


**Note**

The range of a set of data does not give the clear idea about the dispersion of the data from measures of Central Tendency. For this, we need a measure which depend upon the deviation from the measures of Central Tendency.

---

#### 8.2.2 Deviations from the mean

For a given data with \(n\) observations \(x_1, x_2, \ldots, x_n\), the deviations from the mean \(\bar{x}\) are \(x_1 - \bar{x}, x_2 - \bar{x}, \ldots, x_n - \bar{x}\).

#### 8.2.3 Squares of deviations from the mean

The squares of deviations from the mean \(\bar{x}\) of the observations \(x_1, x_2, \ldots, x_n\) are \((x_1 - \bar{x})^2, (x_2 - \bar{x})^2, \ldots, (x_n - \bar{x})^2\) or $$\sum_{i=1}^{n} (x_i - \bar{x})^2$$

**Note**

We note that $(x_i - \bar{x})^2 \ge 0$  for all observations $x_i$, $i = 1,2,3,\dots,n$. If the deviations from the mean $(x_i - \bar{x})$ are small, then the squares of the deviations will be very small.

##### Thinking Corner

Thinking Corner
Can variance be negative?

#### 8.2.4 Variance

The mean of the squares of the deviations from the mean is called Variance. It is denoted by \(\sigma^2\) (read as sigma square).

\[
\text{Variance} = \text{Mean of squares of deviations}
\]

\[
= \frac{(x_1 - \bar{x})^2 + (x_2 - \bar{x})^2 + \ldots + (x_n - \bar{x})^2}{n}
\]

\[
\text{Variance } \sigma^2 = \frac{\sum_{i=1}^n (x_i - \bar{x})^2}{n}
\]

#### 8.2.5 Standard Deviation

The positive square root of Variance is called Standard deviation. That is, standard deviation is the positive square root of the mean of the squares of deviations of the given values from their mean. It is denoted by \(\sigma\).

Standard deviation gives a clear idea about how far the values are spreading or deviating from the mean.

![](image-5.png)
![](image-6.png)

---

**Do You Know?**
Karl Pearson was the first person to use the word standard deviation. German mathematician Gauss used the word Mean error.

---

**Note**

The standard deviation and mean have same units in which the data are given.

---


### Calculation of Standard Deviation for ungrouped data

#### (i) Direct Method


$$\text{Standard deviation } \sigma = \sqrt{\frac{\sum (x_i - \bar{x})^2}{n}}$$

$$= \sqrt{\frac{\sum (x_i^2 - 2x_i\bar{x} + \bar{x}^2)}{n}}$$

$$= \sqrt{\frac{\sum x_i^2}{n} - 2\bar{x}\frac{\sum x_i}{n} + \frac{\bar{x}^2}{n} \times (1 + 1 + \dots to\ n\text{ times})}$$

$$= \sqrt{\frac{\sum x_i^2}{n} - 2\bar{x} \times \bar{x} + \frac{\bar{x}^2}{n} \times n} = \sqrt{\frac{\sum x_i^2}{n} - 2\bar{x}^2 + \bar{x}^2} = \sqrt{\frac{\sum x_i^2}{n} - \bar{x}^2}$$

$$\text{Standard deviation, } \sigma = \sqrt{\frac{\sum x_i^2}{n} - \left(\frac{\sum x_i}{n}\right)^2}$$

---

**Note**

* While computing standard deviation, arranging data in ascending order is not mandatory.
* If the data values are given directly then to find standard deviation we can use the formula $\sigma = \sqrt{\frac{\sum x_i^2}{n} - \left(\frac{\sum x_i}{n}\right)^2}$.


* If the data values are not given directly but the squares of the deviations from the mean of each observation is given then to find standard deviation we can use the formula $\sigma = \sqrt{\frac{\sum (x_i - \bar{x})^2}{n}}$.


---

**Example 8.4** The number of televisions sold in each day of a week are $13, 8, 4, 9, 7, 12, 10$. Find its standard deviation.

**Solution**

| $x_i$ | $x_i^2$ |
| --- | --- |
| $13$ | $169$ |
| $8$ | $64$ |
| $4$ | $16$ |
| $9$ | $81$ |
| $7$ | $49$ |
| $12$ | $144$ |
| $10$ | $100$ |
| $\sum x_i = 63$ | $\sum x_i^2 = 623$ |

$$\begin{aligned}
\text{Standard deviation } \sigma &= \sqrt{\frac{\sum x_i^2}{n} - \left(\frac{\sum x_i}{n}\right)^2} \\
&= \sqrt{\frac{623}{7} - \left(\frac{63}{7}\right)^2} \\
&= \sqrt{89 - 81} = \sqrt{8} \\
\text{Hence, } \sigma &\simeq 2.83
\end{aligned}$$

---

#####  Thinking Corner

Can the standard deviation be more than the variance?

---

##### Progress Check

If the variance is $0.49$ then the standard deviation is _______.

---

**(ii) Mean method**
Another convenient way of finding standard deviation is to use the following formula.

$$\text{Standard deviation (by mean method) } \sigma = \sqrt{\frac{\sum(x_i - \bar{x})^2}{n}}$$

$$\text{If } d_i = x_i - \bar{x} \text{ are the deviations, then } \sigma = \sqrt{\frac{\sum d_i^2}{n}}$$


---

**Example 8.5** The amount of rainfall in a particular season for 6 days are given as $17.8\text{ cm}, 19.2\text{ cm}, 16.3\text{ cm}, 12.5\text{ cm}, 12.8\text{ cm}$ and $11.4\text{ cm}$. Find its standard deviation.

**Solution** Arranging the numbers in ascending order we get, $11.4, 12.5, 12.8, 16.3, 17.8, 19.2$. Number of observations $n = 6$

$$\text{Mean} = \frac{11.4 + 12.5 + 12.8 + 16.3 + 17.8 + 19.2}{6} = \frac{90}{6} = 15$$

| $x_i$ | $d_i = x_i - \bar{x} = x - 15$ | $d_i^2$ |
| --- | --- | --- |
| $11.4$ | $-3.6$ | $12.96$ |
| $12.5$ | $-2.5$ | $6.25$ |
| $12.8$ | $-2.2$ | $4.84$ |
| $16.3$ | $1.3$ | $1.69$ |
| $17.8$ | $2.8$ | $7.84$ |
| $19.2$ | $4.2$ | $17.64$ |
|  |  | $\sum d_i^2 = 51.22$ |

$$\begin{aligned}
\text{Standard deviation } \sigma &= \sqrt{\frac{\sum d_i^2}{n}} \\
&= \sqrt{\frac{51.22}{6}} = \sqrt{8.53} \\
\text{Hence, } \sigma &\simeq 2.9
\end{aligned}$$

---

#### (iii) Assumed Mean method

When the mean value is not an integer (since calculations are very tedious in decimal form) then it is better to use the assumed mean method to find the standard deviation.

Let \(x_1, x_2, x_3, \ldots, x_n\) be the given data values and let \(\bar{x}\) be their mean.

Let \(d_i\) be the deviation of \(x_i\) from the assumed mean \(A\), which is usually the middle value or near the middle value of the given data.

\[
d_i = x_i - A \Rightarrow x_i = d_i + A \qquad \dots (1)
\]

\[
\sum d_i = \sum (x_i - A) = \sum x_i - (A +A +A+ ..... to  n  times)
\]

\[
\frac{\sum d_i}{n} = \frac{\sum x_i}{n} - A \Rightarrow \bar{d} = \bar{x} - A \text{ (or) } \bar{x} = \bar{d} + A \qquad \dots (2)
\]

Standard deviation

\[
\sigma = \sqrt{\frac{\sum (x_i - \bar{x})^2}{n}} = \sqrt{\frac{\sum (d_i - \bar{d})^2}{n}}
\]

\[
= \sqrt{\frac{\sum d_i^2}{n} - \left(\frac{\sum d_i}{n}\right)^2}
\]

Standard deviation
$$\sigma = \sqrt{\frac{\sum (x_i - \bar{x})^2}{n}} = \sqrt{\frac{\sum (d_i + A - \bar{d} - A)^2}{n}} \quad \text{(using (1) and (2))}$$

$$= \sqrt{\frac{\sum (d_i - \bar{d})^2}{n}} = \sqrt{\frac{\sum (d_i^2 - 2d_i \times \bar{d} + \bar{d}^2)}{n}}$$

$$= \sqrt{\frac{\sum d_i^2}{n} - 2\bar{d}\frac{\sum d_i}{n} + \frac{\bar{d}^2}{n}(1 + 1 + 1 + \dots \text{ to } n \text{ times})}$$

$$= \sqrt{\frac{\sum d_i^2}{n} - 2\bar{d} \times \bar{d} + \frac{\bar{d}^2}{n} \times n} \quad \text{(since } \bar{d} \text{ is a constant)}$$

$$= \sqrt{\frac{\sum d_i^2}{n} - \bar{d}^2}$$

$$\sigma = \sqrt{\frac{\sum d_i^2}{n} - \left(\frac{\sum d_i}{n}\right)^2}$$
---

##### Thinking Corner

For any collection of $n$ values, can you find the value of
$$\text{(i) } \sum(x_i - \bar{x})$$
$$\text{(ii) } \left(\sum x_i\right) - \bar{x}$$

---

**Example 8.6** The marks scored by 10 students in a class test are $25, 29, 30, 33, 35, 37, 38, 40, 44, 48$. Find the standard deviation.

**Solution** The mean of marks is $35.9$ which is not an integer. Hence we take assumed mean, $A = 35$, $n = 10$.


![](image-7.png)


Standard deviation

$$\sigma = \sqrt{\frac{\sum d_i^2}{n} - \left(\frac{\sum d_i}{n}\right)^2}$$

$$= \sqrt{\frac{453}{10} - \left(\frac{9}{10}\right)^2}$$

$$= \sqrt{45.3 - 0.81}$$

$$= \sqrt{44.49}$$

$$\sigma \simeq 6.67$$

#### (iv) Step deviation method

Let \(x_1, x_2, x_3, \ldots, x_n\) be the given data. Let \(A\) be the assumed mean.

Let \(c\) be the common divisor of \(x_i - A\).

Let \(d_i = \frac{x_i - A}{c}\).

Then \(x_i = d_i c + A\) ...(1)

\[
\sum x_i = \sum (d_i c + A) = c \sum d_i + A \times n
\]

\[
\frac{\sum x_i}{n} = c \frac{\sum d_i}{n} + A \Rightarrow \bar{x} = c \bar{d} + A \qquad \dots (2)
\]

\[
x_i - \bar{x} = c(d_i - \bar{d}) \quad \text{(using (1) and (2))}
\]

\[
\sigma = \sqrt{\frac{\sum (x_i - \bar{x})^2}{n}} = \sqrt{\frac{\sum c^2 (d_i - \bar{d})^2}{n}} = c \times \sqrt{\frac{\sum d_i^2}{n} - \left(\frac{\sum d_i}{n}\right)^2}
\]

---

**Note**

We can use any of the above methods for finding the standard deviation

**Activity 1**

Find the standard deviation of the marks obtained by you in all five subjects in the quarterly examination and in the midterm test separately. What do you observe from your results.

---

**Example 8.7** The amount that the children have spent for purchasing some eatables in one day trip of a school are 5, 10, 15, 20, 25, 30, 35, 40. Using step deviation method, find the standard deviation of the amount they have spent.

**Solution** We note that all the observations are divisible by 5. Hence we can use the step deviation method. Let the Assumed mean \(A = 20\), \(n = 8\).

![](image-8.png)

Standard deviation

\[
\sigma = \sqrt{\frac{\sum d_i^2}{n} - \left(\frac{\sum d_i}{n}\right)^2} \times c
\]

\[
= \sqrt{\frac{44}{8} - \left(\frac{4}{8}\right)^2} \times 5 = \sqrt{\frac{11}{2} - \frac{1}{4}} \times 5
\]

\[
= \sqrt{5.5 - 0.25} \times 5 = 2.29 \times 5 \approx 11.45
\]

---

**Example 8.8** Find the standard deviation of the following data 7, 4, 8, 10, 11. Add 3 to all the values then find the standard deviation for the new values.

**Solution** Arranging the values in ascending order we get, 4, 7, 8, 10, 11 and \(n = 5\).

![](image-9.png)

Standard deviation

\[
\sigma = \sqrt{\frac{\sum x_i^2}{n} - \left(\frac{\sum x_i}{n}\right)^2}
\]

\[
= \sqrt{\frac{350}{5} - \left(\frac{40}{5}\right)^2} = \sqrt{70 - 64} = \sqrt{6} \approx 2.45
\]

When we add 3 to all the values, we get the new values as 7, 10, 11, 13, 14.

![](image-10.png)

Standard deviation

\[
\sigma = \sqrt{\frac{635}{5} - \left(\frac{55}{5}\right)^2} = \sqrt{127 - 121} = \sqrt{6} \approx 2.45
\]

We see that the standard deviation will not change when we add some fixed constant \(k\) to all the values.

---

**Example 8.9** Find the standard deviation of the data 2, 3, 5, 7, 8. Multiply each data by 4. Find the standard deviation of the new values.

**Solution** Given, \(n = 5\).

![](image-11.png)

Standard deviation

\[
\sigma = \sqrt{\frac{151}{5} - \left(\frac{25}{5}\right)^2} = \sqrt{30.2 - 25} = \sqrt{5.2} \approx 2.28
\]

When we multiply each data by 4, we get the new values as 8, 12, 20, 28, 32.

![](image-12.png)

Standard deviation

\[
\sigma = \sqrt{\frac{2416}{5} - \left(\frac{100}{5}\right)^2} = \sqrt{483.2 - 400} = \sqrt{83.2}
\]

\[
= \sqrt{16 \times 5.2} = 4\sqrt{5.2} \approx 9.12
\]

We see that when we multiply each data by some fixed constant \(k\) the standard deviation also get multiplied by \(k\).

---

**Example 8.10** Find the mean and variance of the first \(n\) natural numbers.

**Solution**

Mean \(\bar{x} = \frac{\text{Sum of all the observations}}{\text{Number of observations}}\)

\[
\bar{x} = \frac{\sum x_i}{n} = \frac{1 + 2 + 3 + \ldots + n}{n} = \frac{n(n+1)}{2 \times n}
\]

\[
\bar{x} = \frac{n+1}{2}
\]

Variance \(\sigma^2 = \frac{\sum x_i^2}{n} - \left(\frac{\sum x_i}{n}\right)^2\)

\[
\sum x_i^2 = 1^2 + 2^2 + 3^2 + \ldots + n^2 = \frac{n(n+1)(2n+1)}{6}
\]

\[
\sigma^2 = \frac{n(n+1)(2n+1)}{6n} - \left[\frac{n(n+1)}{2n}\right]^2
\]

\[
= \frac{(n+1)(2n+1)}{6} - \left(\frac{n+1}{2}\right)^2
\]

\[
= \frac{2n^2 + 3n + 1}{6} - \frac{n^2 + 2n + 1}{4}
\]

\[
= \frac{4n^2 + 6n + 2 - 3n^2 - 6n - 3}{12} = \frac{n^2 - 1}{12}
\]

---

### Calculation of Standard deviation for grouped data

#### (i) Mean method

Standard deviation \(\sigma = \sqrt{\frac{\sum f_i (x_i - \bar{x})^2}{N}}\)

Let \(d_i = x_i - \bar{x}\), then

\[
\sigma = \sqrt{\frac{\sum f_i d_i^2}{N}}, \text{ where } N = \sum_{i=1}^n f_i
\]

(\(f_i\) are frequency values of the corresponding data points \(x_i\))

---

**Example 8.11** 48 students were asked to write the total number of hours per week they spent on watching television. With this information find the standard deviation of hours spent for watching television.

![](image-13.png)

# Solution

![](image-14.png)

Mean \(\bar{x} = \frac{\sum f_i x_i}{N} = \frac{432}{48} = 9\) (\(\because N = \sum f_i\))

Standard deviation \(\sigma = \sqrt{\frac{\sum f_i d_i^2}{N}} = \sqrt{\frac{124}{48}} = \sqrt{2.58} \approx 1.6\)

---

#### (ii) Assumed Mean method

Let \(x_1, x_2, x_3, \ldots, x_n\) be the given data with frequencies \(f_1, f_2, f_3, \ldots, f_n\) respectively. Let \(\bar{x}\) be their mean and \(A\) be the assumed mean.

\[
d_i = x_i - A
\]

Standard deviation,

\[
\sigma = \sqrt{\frac{\sum f_i d_i^2}{N} - \left(\frac{\sum f_i d_i}{N}\right)^2}
\]

---

**Example 8.12** The marks scored by the students in a slip test are given below. Find the standard deviation of their marks.

![](image-15.png)

**Solution** Let the assumed mean, \(A = 8\).

![](image-16.png)

Standard deviation

\[
\sigma = \sqrt{\frac{\sum f_i d_i^2}{N} - \left(\frac{\sum f_i d_i}{N}\right)^2}
\]

\[
= \sqrt{\frac{240}{29} - \left(\frac{4}{29}\right)^2} = \sqrt{\frac{240 \times 29 - 16}{29 \times 29}}
\]

\[
\sigma = \sqrt{\frac{6944}{29 \times 29}} \approx 2.87
\]

---

### Calculation of Standard deviation for continuous frequency distribution

#### (i) Mean method

Standard deviation \(\sigma = \sqrt{\frac{\sum f_i (x_i - \bar{x})^2}{N}}\)

where, \(x_i =\) Middle value of the \(i\)th class.

\(f_i =\) Frequency of the \(i\)th class.

---

#### (ii) Shortcut method (or) Step deviation method

To make the calculation simple, we provide the following formula. Let \(A\) be the assumed mean, \(x_i\) be the middle value of the \(i\)th class and \(c\) is the width of the class interval.

\[
d_i = \frac{x_i - A}{c}
\]

\[
\sigma = c \times \sqrt{\frac{\sum f_i d_i^2}{N} - \left(\frac{\sum f_i d_i}{N}\right)^2}
\]

---

**Example 8.13** Marks of the students in a particular subject of a class are given below. Find its standard deviation.

![](image-17.png)

**Solution** Let the assumed mean, \(A = 35\), \(c = 10\).

![](image-18.png)

Standard deviation

\[
\sigma = c \times \sqrt{\frac{\sum f_i d_i^2}{N} - \left(\frac{\sum f_i d_i}{N}\right)^2}
\]

\[
= 10 \times \sqrt{\frac{210}{71} - \left(-\frac{30}{71}\right)^2} = 10 \times \sqrt{\frac{210}{71} - \frac{900}{5041}}
\]

\[
= 10 \times \sqrt{2.779} \approx 16.67
\]

---

##### Thinking Corner

1. The standard deviation of a data is 2.8, if 5 is added to all the data values then the new standard deviation is ______.

2. If \(S\) is the standard deviation of values \(p, q, r\) then standard deviation of \(p - 3, q - 3, r - 3\) is ______.

---

**Example 8.14** The mean and standard deviation of 15 observations are found to be 10 and 5 respectively. On rechecking it was found that one of the observation with value 8 was incorrect. Calculate the correct mean and standard deviation if the correct observation value was 23.

**Solution** \(n = 15\), \(\bar{x} = 10\), \(\sigma = 5\).

\[
\bar{x} = \frac{\sum x}{n} \Rightarrow \sum x = 15 \times 10 = 150
\]

Wrong observation value \(= 8\), Correct observation value \(= 23\).

Correct total \(= 150 - 8 + 23 = 165\).

Correct mean \(= \frac{165}{15} = 11\).

Standard deviation \(\sigma = \sqrt{\frac{\sum x^2}{n} - \left(\frac{\sum x}{n}\right)^2}\)

Incorrect value of \(\sigma = 5 = \sqrt{\frac{\sum x^2}{15} - (10)^2}\)

\[
25 = \frac{\sum x^2}{15} - 100 \Rightarrow \frac{\sum x^2}{15} = 125
\]

Incorrect value of \(\sum x^2 = 1875\).

Correct value of \(\sum x^2 = 1875 - 8^2 + 23^2 = 1875 - 64 + 529 = 2340\).

Correct standard deviation

\[
\sigma = \sqrt{\frac{2340}{15} - (11)^2} = \sqrt{156 - 121} = \sqrt{35} \approx 5.9
\]

---

## Exercise 8.1

1. Find the range and coefficient of range of the following data.

(i) 63, 89, 98, 125, 79, 108, 117, 68

(ii) 43.5, 13.6, 18.9, 38.4, 61.4, 29.8

2. If the range and the smallest value of a set of data are 36.8 and 13.4 respectively, then find the largest value.

3. Calculate the range of the following data.

![](image-19.png)

4. A teacher asked the students to complete 60 pages of a record note book. Eight students have completed only 32, 35, 37, 30, 33, 36, 35 and 37 pages. Find the standard deviation of the pages completed by them.

5. Find the variance and standard deviation of the wages of 9 workers given below: 310, 290, 320, 280, 300, 290, 320, 310, 280.

6. A wall clock strikes the bell once at 1 o'clock, 2 times at 2 o'clock, 3 times at 3 o'clock and so on. How many times will it strike in a particular day. Find the standard deviation of the number of strikes the bell make a day.

7. Find the standard deviation of first 21 natural numbers.

8. If the standard deviation of a data is 4.5 and if each value of the data is decreased by 5, then find the new standard deviation.

9. If the standard deviation of a data is 3.6 and each value of the data is divided by 3, then find the new variance and new standard deviation.

10. The rainfall recorded in various places of five districts in a week are given below. Find its standard deviation.

![](image-20.png)

11. In a study about viral fever, the number of people affected in a town were noted as Find its standard deviation.

![](image-21.png)

12. The measurements of the diameters (in cms) of the plates prepared in a factory are given below. Find its standard deviation.

![](image-22.png)

13. The time taken by 50 students to complete a 100 meter race are given below. Find its standard deviation.

![](image-23.png)

14. For a group of 100 candidates the mean and standard deviation of their marks were found to be 60 and 15 respectively. Later on it was found that the scores 45 and 72 were wrongly entered as 40 and 27. Find the correct mean and standard deviation.

15. The mean and variance of seven observations are 8 and 16 respectively. If five of these are 2, 4, 10, 12 and 14, then find the remaining two observations.

---