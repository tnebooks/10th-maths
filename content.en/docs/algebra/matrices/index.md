---
title: 'Matrices'
weight: 8
---
## 3.9 Matrices

### Introduction

Let us consider the following information. Vanitha has 12 story books, 20 notebooks and 4 pencils. Radha has 27 story books, 17 notebooks and 6 pencils. Gokul has 7 story books, 11 notebooks and 4 pencils. Geetha has 10 story books, 12 notebooks and 5 pencils.

| Details | Story Books | Note Books | Pencils |
|:---|:---|:---|:---|
| Vanitha | 12 | 20 | 4 |
| Radha | 27 | 17 | 6 |
| Gokul | 7 | 11 | 4 |
| Geetha | 10 | 12 | 5 |

Now, we arrange this information in the tabular form as follows.

| First row | (12 | 20 | 4) |
|:---|:---|:---|:---|
| Second row | 27 | 17 | 6 |
| Third row | 7 | 11 | 4 |
| Fourth row | 10 | 12 | 5 |

Here, the items possessed by four people are aligned or positioned in a rectangular array containing four horizontal and three vertical arrangements. The horizontal arrangements are called "**rows**" and the vertical arrangements are called "**columns**". The whole rectangular arrangement is called a "**Matrix**". Generally, if we arrange things in a rectangular array, we call it as "Matrix".

Applications of matrices are found in several scientific fields. In Physics, matrices are applied in the calculations of battery power outputs, resistor conversion of electrical energy into other forms of energy. In computer based applications, matrices play a vital role in the projection of three dimensional image into a two dimensional screen, creating a realistic seeming motions. In graphic software, Matrix Algebra is used to process linear transformations to render images. One of the most important usage of matrices are encryption of message codes. The encryption and decryption process are carried out using matrix multiplication and inverse operations. The concept of matrices is used in transmission of codes when the messages are lengthy. In Geology, matrices are used for taking seismic surveys. In Robotics, matrices are used to identify the robot movements.

### Definition

A **matrix** is a rectangular array of elements. The horizontal arrangements are called rows and vertical arrangements are called columns.

For example, 
```
[ 4  8  0 ]
[ 1  9 -2 ]
```
is a matrix.

Usually capital letters such as A, B, C, X, Y, ... etc., are used to represent the matrices and small letters such as a, b, c, l, m, n, a₁₂, a₁₃, ... to indicate the entries or elements of the matrices.

### 3.9.1 Order of a Matrix

If a matrix A has m number of rows and n number of columns, then the **order** of the matrix A is (Number of rows) × (Number of columns) that is, m × n. We read m × n as m cross n or m by n. It may be noted that m × n is not a product of m and n.

General form of a matrix A with m rows and n columns (order m × n) can be written as:

```
A = [ a₁₁  a₁₂  a₁₃  ...  a₁ⱼ  ...  a₁ₙ ]
    [ a₂₁  a₂₂  a₂₃  ...  a₂ⱼ  ...  a₂ₙ ]
    [  :    :    :   ...   :   ...   :  ]
    [ aᵢ₁  aᵢ₂  aᵢ₃  ...  aᵢⱼ  ...  aᵢₙ ]
    [  :    :    :   ...   :   ...   :  ]
    [ aₘ₁  aₘ₂  aₘ₃  ...  aₘⱼ  ...  aₘₙ ]
```

where a₁₁, a₁₂, a₁₃ denote entries of the matrix. a₁₁ is the element in first row, first column, a₁₂ is the element in the first row, second column, and so on.

In general, aᵢⱼ is the element in the i-th row and j-th column and is referred as (i,j)-th element. With this notation, we can express the matrix A as A = (aᵢⱼ)ₘₓₙ where i = 1,2,...,m and j = 1,2,...,n.

The total number of entries in the matrix A = (aᵢⱼ)ₘₓₙ is mn.

**Note:** When giving the order of a matrix, you should always mention the number of rows first, followed by the number of columns.

### 3.9.2 Types of Matrices

In this section, we shall define certain types of matrices.

#### 1. Row Matrix

A matrix is said to be a row matrix if it has only one row and any number of columns. A row matrix is also called as a row vector.

For example, A = [8 9 4]₁ₓ₃, B = [3  -2  1/3]₁ₓ₃ are row matrices.

In general A = [a₁₁ a₁₂ a₁₃ ... a₁ₙ] is a row matrix of order 1 × n.

#### 2. Column Matrix

A matrix is said to be a column matrix if it has only one column and any number of rows. It is also called as a column vector.

For example,
```
    [ x     ]         [ 5 ]         [  8  ]
A = [ sin x ],   B = [ 7 ],    C = [ -3  ]
    [ cos x ]         [   ]         [ 23  ]
                      [   ]         [ 17  ]
```
are column matrices of order 3×1, 2×1 and 4×1 respectively.

In general,
```
    [ a₁₁ ]
A = [ a₂₁ ]
    [ a₃₁ ]
    [  :  ]
    [ aₘ₁ ]
```
is a column matrix of order m × 1.

#### 3. Square Matrix

A matrix in which the number of rows is equal to the number of columns is called a **square matrix**. Thus a matrix A = (aᵢⱼ)ₘₓₙ will be a square matrix if m = n.

For example,
```
[ 1  3 ]           [ -1  0  2 ]
[ 4  5 ]     and   [  3  6  8 ]
                   [  2  3  5 ]
```
are square matrices of orders 2×2 and 3×3.

**Definition:** In a square matrix, the elements of the form a₁₁, a₂₂, a₃₃, ... (i.e.) aᵢᵢ are called **leading diagonal elements**.

#### 4. Diagonal Matrix

A square matrix, all of whose elements, except those in the leading diagonal are zero is called a **diagonal matrix** (i.e.) A square matrix A = (aᵢⱼ) is said to be diagonal matrix if aᵢⱼ = 0 for i ≠ j.

Note that some elements of the leading diagonal may be zero but not all.

#### 5. Scalar Matrix

A diagonal matrix in which all the leading diagonal elements are equal is called a **scalar matrix**.

For example,
```
[ 4  0 ]         [ k  0  0 ]         [ 5  0  0 ]
[ 0  4 ],   [ 0  k  0 ],   [ 0  5  0 ]
                 [ 0  0  k ]         [ 0  0  5 ]
```

In general, A = (aᵢⱼ)ₘₓₘ is said to be a scalar matrix if:
- aᵢⱼ = 0 when i ≠ j
- aᵢⱼ = k when i = j, where k is constant

#### 6. Identity (or) Unit Matrix

A square matrix in which elements in the leading diagonal are all "1" and rest are all zero is called an **identity matrix** or **unit matrix**.

Thus, the square matrix A = (aᵢⱼ) is an identity matrix if:
- aᵢⱼ = 1 if i = j
- aᵢⱼ = 0 if i ≠ j

A unit matrix of order n is written as Iₙ.

For example:
```
        [ 1  0 ]             [ 1  0  0 ]
I₂ =    [ 0  1 ],      I₃ =  [ 0  1  0 ]
                             [ 0  0  1 ]
```

#### 7. Zero matrix (or) null matrix

A matrix is said to be a **zero matrix** or **null matrix** if all its elements are zero.

For example, [0], 
```
[ 0  0 ]
[ 0  0 ]
```
, 
```
[ 0  0  0 ]
[ 0  0  0 ]
[ 0  0  0 ]
```
are all zero matrices of order 1×1, 2×2 and 3×3 but of different orders. We denote zero matrix of order n×n by Oₙ.

#### 8. Transpose of a matrix

The matrix which is obtained by interchanging the elements in rows and columns of the given matrix A is called **transpose** of A and is denoted by Aᵀ.

- If A = 
```
[ 5  3  1 ]
[ 2  8  9 ]
[ 4  7  5 ]
```
then Aᵀ = 
```
[ 5  2  4 ]
[ 3  8  7 ]
[ 1  9  5 ]
```

- If B = 
```
[ 1  5 ]
[ 8  9 ]
[ 4  3 ]
```
then Bᵀ = 
```
[ 1  8  4 ]
[ 5  9  3 ]
```

If order of A is m × n then order of Aᵀ is n × m.

We note that (Aᵀ)ᵀ = A.

#### 9. Triangular Matrix

A square matrix in which all the entries above the leading diagonal are zero is called a **lower triangular matrix**.

If all the entries below the leading diagonal are zero, then it is called an **upper triangular matrix**.

**Definition:** A square matrix A = (aᵢⱼ)ₙₓₙ is called upper triangular matrix if aᵢⱼ = 0 for i > j and is called lower triangular matrix if aᵢⱼ = 0, i < j.

#### Equal Matrices

Two matrices A and B are said to be **equal** if and only if they have the same order and each element of matrix A is equal to the corresponding element of matrix B. That is, aᵢⱼ = bᵢⱼ for all i, j.

#### The negative of a matrix

The negative of a matrix Aₘₓₙ denoted by -Aₘₓₙ is the matrix formed by replacing each element in the matrix Aₘₓₙ with its additive inverse.

Additive inverse of an element k is -k. That is, every element of –A is the negative of the corresponding element of A.

### Example 3.56

Consider the following information regarding the number of men and women workers in three factories I, II and III.

| Factory | Men | Women |
|:---|:---|:---|
| I | 23 | 18 |
| II | 47 | 36 |
| III | 15 | 16 |

Represent the above information in the form of a matrix. What does the entry in the second row and first column represent?

**Solution:**

The information is represented in the form of a 3×2 matrix as follows:
```
    [ 23  18 ]
A = [ 47  36 ]
    [ 15  16 ]
```

The entry in the second row and first column represent that there are 47 men workers in factory II.

### Example 3.57

If a matrix has 16 elements, what are the possible orders it can have?

**Solution:**

We know that a matrix of order m × n has mn elements. Thus to find all possible orders of a matrix with 16 elements, we will find all ordered pairs of natural numbers whose product is 16.

Such ordered pairs are (1,16), (16,1), (4,4), (8,2), (2,8)

Hence, possible orders are 1×16, 16×1, 4×4, 8×2, 2×8.

### Example 3.58

Construct a 3×3 matrix whose elements are aᵢⱼ = i²j²

**Solution:**

The general 3×3 matrix is:
```
    [ a₁₁  a₁₂  a₁₃ ]
A = [ a₂₁  a₂₂  a₂₃ ]
    [ a₃₁  a₃₂  a₃₃ ]
```

a₁₁ = 1²·1² = 1, a₁₂ = 1²·2² = 4, a₁₃ = 1²·3² = 9
a₂₁ = 2²·1² = 4, a₂₂ = 2²·2² = 16, a₂₃ = 2²·3² = 36
a₃₁ = 3²·1² = 9, a₃₂ = 3²·2² = 36, a₃₃ = 3²·3² = 81

Hence,
```
    [ 1   4   9  ]
A = [ 4  16  36  ]
    [ 9  36  81  ]
```

### Example 3.59

Find the value of a, b, c, d from the equation:
```
[ a-b    2a+c  ]   [ 1  5 ]
[ 2a-b  3c+d  ] = [ 0  2 ]
```

**Solution:**

Equating corresponding elements:
- a - b = 1 ... (1)
- 2a + c = 5 ... (2)
- 2a - b = 0 ... (3)
- 3c + d = 2 ... (4)

From (3): b = 2a
From (1): a - 2a = 1 → -a = 1 → a = -1
Therefore b = -2

From (2): 2(-1) + c = 5 → c = 7
From (4): 3(7) + d = 2 → d = -19

Therefore, a = -1, b = -2, c = 7, d = -19

## Exercise 3.17

1. In the matrix 
```
    [ 8  9  4  3 ]
A = [ 1  7    3  ]
    [ 2  5  1  4 ]
    [ 3  0  6  8 ]
    [ 1  1  1    ]
```
write (i) The number of elements (ii) The order of the matrix (iii) Write the elements a₂₂, a₂₃, a₂₄, a₃₄, a₄₃, a₄₄.

2. If a matrix has 18 elements, what are the possible orders it can have? What if it has 6 elements?

3. Construct a 3×3 matrix whose elements are given by
   - (i) aᵢⱼ = i - 2j
   - (ii) aᵢⱼ = (i+j)³/3

4. If A = 
```
[ 5  4  3 ]
[ 1  7  9 ]
[ 3  8  2 ]
```
then find the transpose of A.

5. If A = 
```
[ 7  -3 ]
[ 5   2 ]
[ 3   5 ]
```
then find the transpose of -A.

6. If A = 
```
[ 5  2  2 ]
[ 1  7  0 ]
[ 7    5  ]
[ 2  8  3 ]
[ 1  1    ]
```
find the values of a then verify (Aᵀ)ᵀ = A

7. Find the values of x, y and z from the following equations
   - (i) 
   ```
   [ x+y+z ]   [ 9 ]
   [ x+z   ] = [ 5 ]
   [ y+z   ]   [ 7 ]
   ```
   - (ii) 
   ```
   [ x+y ]   [ 2  5 ]
   [ x+z ] = [ 6  2 ]
   [ y+z ]   [ 5  8 ]
   ```
   - (iii) 
   ```
   [ x+y+z ]   [  9  ]
   [ x+z   ] = [  5  ]
   [ y+z   ]   [  7  ]
   ```

### 3.9.3 Operations on Matrices

In this section, we shall discuss the addition and subtraction of matrices, multiplication of a matrix by a scalar and multiplication of matrices.

#### Addition and subtraction of matrices

Two matrices can be added or subtracted if they have the same order. To add or subtract two matrices, simply add or subtract the corresponding elements.

For example:
```
[ a  b  c ]   [ g  h  i ]   [ a+g  b+h  c+i ]
[ d  e  f ] + [ j  k  l ] = [ d+j  e+k  f+l ]
```

```
[ a  b ]   [ e  f ]   [ a-e  b-f ]
[ c  d ] - [ g  h ] = [ c-g  d-h ]
```

If A = (aᵢⱼ), B = (bᵢⱼ), i = 1,2,...,m and j = 1,2,...,n then C = A + B is such that C = (cᵢⱼ) where cᵢⱼ = aᵢⱼ + bᵢⱼ for all i = 1,2,...,m and j = 1,2,...,n

### Example 3.60

If 
```
      [ 1  2  3 ]         [ 1  7  0 ]
A =   [ 4  5  6 ],    B = [ 1  3  1 ]
      [ 7  8  9 ]         [ 2  4  0 ]
```
find A + B.

**Solution:**
```
      [ 1+1  2+7  3+0 ]   [ 2  9  3 ]
A+B = [ 4+1  5+3  6+1 ] = [ 5  8  7 ]
      [ 7+2  8+4  9+0 ]   [ 9 12  9 ]
```

### Example 3.61

Two examinations were conducted for three groups of students namely group 1, group 2, group 3 and their data on average of marks for the subjects Tamil, English, Science and Mathematics are given below in the form of matrices A and B. Find the total marks of both the examinations for all the three groups.

**Solution:**
The total marks in both the examinations for all the three groups is the sum of the given matrices.

### Example 3.62

If 
```
      [ 1  3 -2 ]         [ 1  8 ]
A =   [ 5 -4  6 ],    B = [ 3  4 ]
      [-3  2  9 ]         [ 9  6 ]
```
find A + B.

**Solution:**

It is not possible to add A and B because they have different orders.

#### Multiplication of Matrix by a Scalar

We can multiply the elements of the given matrix A by a non-zero number k to obtain a new matrix kA whose elements are multiplied by k. The matrix kA is called scalar multiplication of A.

Thus if A = (aᵢⱼ)ₘₓₙ then, kA = (kaᵢⱼ)ₘₓₙ for all i = 1,2,...,m and for all j = 1,2,...,n.

### Example 3.63

If 
```
      [ 7  8  6 ]         [ 4  11 -3 ]
A =   [ 1  3  9 ],    B = [ -1  2  4 ]
      [-4  3 -1 ]         [  7  5  0 ]
```
then Find 2A + B.

**Solution:**
Since A and B have same order 3×3, 2A + B is defined.

### Example 3.64

If 
```
      [   5     4    -2   ]         [  -7     4    -3   ]
A =   [  1/2   3/4   √2   ],    B = [  1/4   7/2    3   ]
      [   1     9     4   ]         [  1/5   -6     9   ]
```
find 4A - 3B.

**Solution:**
Since A, B are of the same order 3×3, subtraction of 4A and 3B is defined.

#### Properties of Matrix Addition and Scalar Multiplication

Let A, B, C be m×n matrices and p and q be two non-zero scalars (numbers). Then we have the following properties.

- (i) A + B = B + A [Commutative property of matrix addition]
- (ii) A + (B + C) = (A + B) + C [Associative property of matrix addition]
- (iii) (pq)A = p(qA) [Associative property of scalar multiplication]
- (iv) IA = A [Scalar Identity property where I is the unit matrix]
- (v) p(A + B) = pA + pB [Distributive property of scalar and two matrices]
- (vi) (p+q)A = pA + qA [Distributive property of two scalars with a matrix]

#### Additive Identity

The null matrix or zero matrix is the identity for matrix addition.

Let A be any matrix. Then, A + O = O + A = A where O is the null matrix or zero matrix of same order as that of A.

#### Additive Inverse

If A be any given matrix then –A is the additive inverse of A. In fact we have A + (-A) = (-A) + A = O

### Example 3.65

Find the value of a, b, c, d from the following matrix equation.
```
[ d   8 ]   [ 3   a ]   [ 2  2a ]   [ 0  1 ]
[3b   a ] + [ -2 -4 ] = [  b 4c ] + [ -5 0 ]
```

**Solution:**

First, we add the two matrices on both left, right hand sides to get:
```
[ d+3   8+a ]   [ 2    2a+1 ]
[3b-2   a-4 ] = [ b-5   4c  ]
```

Equating corresponding elements:
- d + 3 = 2 → d = -1
- 8 + a = 2a + 1 → a = 7
- 3b - 2 = b - 5 → 2b = -3 → b = -3/2
- a - 4 = 4c → 7 - 4 = 4c → c = 3/4

Therefore, a = 7, b = -3/2, c = 3/4, d = -1.

### Example 3.66

If 
```
      [ 1  8  3 ]         [  8 -6 -4 ]         [ 5  3  0 ]
A =   [ 3  5  0 ],    B = [  2 11 -3 ],    C = [-1 -7  2 ]
      [ 8  7  6 ]         [  0  1  5 ]         [ 1  4  3 ]
```
compute the following: (i) 3A + 2B - C (ii) 1/2 A - 3B

**Solution:**

(i) 3A + 2B - C = ...

(ii) 1/2 A - 3B = ...

## Exercise 3.18

1. If 
```
      [ 1  9 ]         [ 5  7 ]
A =   [ 3  4 ],    B = [ 3  3 ]
      [ 8 -3 ]         [ 1  0 ]
```
then verify that (i) A + B = B + A (ii) A + (-A) = (-A) + A = O

2. If 
```
      [ 4  3  1 ]         [ 2  3  4 ]         [ 8  3  4 ]
A =   [ 2  3 -8 ],    B = [ 1  9  2 ],    C = [ 1 -2  3 ]
      [ 1  0 -4 ]         [-7  1 -1 ]         [ 2  4 -1 ]
```
then verify that A + (B + C) = (A + B) + C

3. Find X and Y if 
```
      [ 7  0 ]         [ 3  0 ]
X+Y = [ 3  5 ] and X-Y = [ 0  4 ]
```

4. If 
```
      [ 0  4  9 ]         [ 7  3  8 ]
A =   [ 8  3  7 ],    B = [ 1  4  9 ]
```
find the value of (i) B - 5A (ii) 3A - 9B

5. Find the values of x, y, z if 
```
[ x    x-3  z   ]   [  3   3   7 ]
[ x+y  x+y+z ] = [ 10  16    ]
```

6. Find x and y if 
```
      [ x    4 ]       [ y   2 ]   [ 4  6 ]
x ×   [ 3   -2 ] + y × [ -3  3 ] = [ 7    ]
```

7. Find the non-zero values of x satisfying the matrix equation
```
[ x   2x ]   [ 2   8 ]     [ 2    8    ]
[ 3    2 ] + [ 5  4x ] = x [ 2x  4x²   ]
                      [ 4   10    6   ]
```

8. Solve for x, y:
```
    [ x  ]     [  2   ]   [ 5 ]
x × [ y  ] +   [ -2x  ] = [ 8 ]
    [ 2  ]     [  y   ]   [   ]
```

#### Multiplication of Matrices

To multiply two matrices, the number of columns in the first matrix must be equal to the number of rows in the second matrix.

(Order of left hand matrix) × (order of right hand matrix) → (order of product matrix)
(3 × 3)(3 × 2) → (3 × 2)

Matrices are multiplied by multiplying the elements in a row of the first matrix by the elements in a column of the second matrix, and adding the results.

The product AB can be found if the number of columns of matrix A is equal to the number of rows of matrix B. If the order of matrix A is m × n and B is n × p then the order of AB is m × p.

#### Properties of Multiplication of Matrix

**(a) Matrix multiplication is not commutative in general**

If A is of order m × n and B of the order n × p then AB is defined but BA is not defined. Even if AB and BA are both defined, it is not necessary that they are equal. In general AB ≠ BA.

**(b) Matrix multiplication is distributive over matrix addition**
- (i) A(B + C) = AB + AC (Right Distributive Property)
- (ii) (A + B)C = AC + BC (Left Distributive Property)

**(c) Matrix multiplication is always associative**

If A, B, C are m × n, n × p and p × q matrices respectively then (AB)C = A(BC)

**(d) Multiplication of a matrix by a unit matrix**

If A is a square matrix of order n × n and I is the unit matrix of same order then AI = IA = A.

**Note:** If x and y are two real numbers such that xy = 0 then either x = 0 or y = 0. But this condition may not be true with respect to two matrices.

AB = 0 does not necessarily imply that A = 0 or B = 0 or both A, B = 0.

### Example 3.67

If 
```
      [ 1  2  0 ]         [ 8  3  1 ]
A =   [ 3  1  5 ],    B = [ 2  4  1 ]
                      [ 5  3  1 ]
```
find AB.

**Solution:**

We observe that A is a 2×3 matrix and B is a 3×3 matrix, hence AB is defined and it will be of the order 2×3.

AB = 
```
[ 1×8+2×2+0×5  1×3+2×4+0×3  1×1+2×1+0×1 ]   [ 12  11  3 ]
[ 3×8+1×2+5×5  3×3+1×4+5×3  3×1+1×1+5×1 ] = [ 51  28  9 ]
```

### Example 3.68

If 
```
      [ 2  1 ]         [ 2  0 ]
A =   [ 1  3 ],    B = [ 1  3 ]
```
find AB and BA. Verify AB = BA?

**Solution:**

AB = 
```
[ 2  1 ]   [ 2  0 ]   [ 4+1  0+3 ]   [ 5  3 ]
[ 1  3 ] × [ 1  3 ] = [ 2+3  0+9 ] = [ 5  9 ]
```

BA = 
```
[ 2  0 ]   [ 2  1 ]   [ 4+0  2+0 ]   [ 4  2 ]
[ 1  3 ] × [ 1  3 ] = [ 2+3  1+9 ] = [ 5 10 ]
```

Therefore, AB ≠ BA.

### Example 3.69

If 
```
      [  2    -2√2 ]         [  2    2√2 ]
A =   [ √2      2  ],    B = [ -√2     2 ]
```
Show that A and B satisfy commutative property with respect to matrix multiplication.

**Solution:**

We have to show that AB = BA

LHS = AB = 
```
[  2    -2√2 ]   [  2    2√2 ]   [ 4+4    4√2-4√2 ]   [ 8  0 ]
[ √2      2  ] × [ -√2     2 ] = [ 2√2-2√2  4+4   ] = [ 0  8 ]
```

RHS = BA = 
```
[  2    2√2 ]   [  2    -2√2 ]   [ 4+4    -4√2+4√2 ]   [ 8  0 ]
[ -√2     2 ] × [ √2      2  ] = [ -2√2+2√2   4+4   ] = [ 0  8 ]
```

Hence, LHS = RHS (i.e.) AB = BA

### Example 3.70

Solve:
```
[ 2  1 ]   [ x ]   [ 4 ]
[ 1  2 ] × [ y ] = [ 5 ]
```

**Solution:**

By matrix multiplication:
- 2x + y = 4 ... (1)
- x + 2y = 5 ... (2)

From (1) - 2×(2): -3y = -6 → y = 2
Substituting y = 2 in (1): 2x + 2 = 4 → x = 1

Therefore, x = 1, y = 2.

### Example 3.71

If A = [1 -1 2], 
```
      [ 1  -1 ]
B =   [ 2   1 ]
      [ 1   1 ]
```
and C = 
```
[ 1  2 ]
[ 2 -1 ]
```
show that (AB)C = A(BC).

**Solution:**

LHS = (AB)C = ...

RHS = A(BC) = ...

From (1) and (2), (AB)C = A(BC).

### Example 3.72

If 
```
      [ 1  1 ]         [ 1  2 ]         [ -7  6 ]
A =   [ -1 3 ],    B = [ -4 2 ],    C = [  3  2 ]
```
verify that A(B + C) = AB + AC.

**Solution:**

LHS = A(B + C) = ...

RHS = AB + AC = ...

From (1) and (2), A(B+C) = AB + AC. Hence proved.

### Example 3.73

If 
```
      [ 1  2  1 ]         [ 2 -1 ]
A =   [ 2 -1  1 ],    B = [ -1 4 ]
                      [  0  2 ]
```
show that (AB)ᵀ = BᵀAᵀ

**Solution:**

LHS = (AB)ᵀ = ...

RHS = BᵀAᵀ = ...

From (1) and (2), (AB)ᵀ = BᵀAᵀ. Hence proved.

## Exercise 3.19

1. Find the order of the product matrix AB if

| | (i) | (ii) | (iii) | (iv) | (v) |
|:---|:---|:---|:---|:---|:---|
| Orders of A | 3×3 | 4×3 | 4×2 | 4×5 | 1×1 |
| Orders of B | 3×3 | 3×2 | 2×2 | 5×1 | 1×3 |

2. If A is of order p × q and B is of order q × r what is the order of AB and BA?

3. A has 'c' rows and 'a+3' columns. B has 'b²' rows and '17-b' columns, and if both products AB and BA exist, find a, b?

4. If 
```
      [ 2  5 ]         [ 1 -3 ]
A =   [ 4  3 ],    B = [ 2  5 ]
```
find AB, BA and verify AB ≠ BA

5. Given that 
```
      [ 1  3 ]         [ 1 -1  2 ]         [ 1  3  2 ]
A =   [ 5 -1 ],    B = [ 3  5  2 ],    C = [ -4 1  3 ]
```
verify that A(B + C) = AB + AC

6. Show that the matrices 
```
      [ 1  2 ]         [ 1 -2 ]
A =   [ 3  1 ],    B = [ -3 1 ]
```
satisfy commutative property AB = BA

7. Let 
```
      [ 1  2 ]         [ 4  0 ]         [ 2  0 ]
A =   [ 1  3 ],    B = [ 1  5 ],    C = [ 1  2 ]
```
Show that (i) A(BC) = (AB)C (ii) (A+B)C = AC + BC (iii) (A-B)ᵀ = Aᵀ - Bᵀ

8. If 
```
      [ cos θ   0    ]         [ sin θ   0    ]
A =   [  0    cos θ  ],    B = [  0    sin θ  ]
```
then show that A² + B² = I.

9. If 
```
      [ cos θ   sin θ ]
A =   [ -sin θ  cos θ ]
```
prove that AAᵀ = I.

10. Verify that A² = I when 
```
      [ 5  -4 ]
A =   [ 6  -5 ]
```

11. If 
```
      [ a  b ]
A =   [ c  d ]
```
and I = 
```
[ 1  0 ]
[ 0  1 ]
```
show that A² - (a+d)A = (bc - ad)I₂

12. If 
```
      [ 5  2  9 ]         [ 1  7 ]
A =   [ 1  2  8 ],    B = [ 1  2 ]
                      [ 5 -1 ]
```
verify that (AB)ᵀ = BᵀAᵀ

13. If 
```
      [ 3  1 ]
A =   [ -1 2 ]
```
show that A² - 5A + 7I₂ = 0

## Multiple choice questions

### Exercise 3.20

1. A system of three linear equations in three variables is inconsistent if their planes
   - (A) intersect only at a point
   - (B) intersect in a line
   - (C) coincides with each other
   - (D) do not intersect

2. The solution of the system x + y - 3z = -6, -7y + 7z = 7, z = 9 is
   - (A) x = y = z = 1, 2, 3
   - (B) x = -1, y = 2, z = 3
   - (C) x = -1, y = -2, z = 3
   - (D) x = y = z = -1, 2, 3

3. If (x-6) is the HCF of x² - 2x - 24 and x² - kx - 6 then the value of k is
   - (A) 3
   - (B) 5
   - (C) 6
   - (D) 8

4. (3y-3)/y ÷ (7y-7)/(3y²) =
   - (A) 9y/7
   - (B) 9y³/(21y-21)
   - (C) (21y²-42y+21)/(3y³)
   - (D) 7(y²-2y+1)/y²

5. y²/(y²+1) is not equal to
   - (A) (y⁴+1)/(y²+1)
   - (B) y²/(y²+1)
   - (C) (y²-1)/(y²+1) + 2/(y²+1)
   - (D) (y²+1)/(y²+1) - 1/(y²+1)

6. (x²-25)/(x³+8x²-6x+5) gives
   - (A) (x-5)(x+5)/[(x-1)(x²-7x+40)]
   - ...

7. The square root of 256x⁶y⁶z¹⁰ - 256x⁶y⁶z⁶ is equal to
   - (A) 16x³z⁵/y³
   - (B) 16y³/(x³z⁵)
   - (C) 16y³/(xz⁵)
   - (D) 16x³z⁵/y³

8. Which of the following should be added to make x⁴ - 64 + a perfect square
   - (A) 4x²
   - (B) 16x²
   - (C) 8x²
   - (D) -8x²

9. The solution of 2(x-1)² = (x+1) is equal to
   - (A) -1
   - (B) 2
   - (C) -1, 2
   - (D) None of these

10. The values of a and b if 4x⁴ - 24x³ + 76x² + ax + b is a perfect square are
    - (A) 100, 120
    - (B) 10, 12
    - (C) -120, 100
    - (D) 12, 10

11. If the roots of the equation q²x² + p²x + r² = 0 are the squares of the roots of the equation qx² + px + r = 0, then q, p, r are in _______
    - (A) A.P
    - (B) G.P
    - (C) Both A.P and G.P
    - (D) none of these

12. Graph of a linear equation is a _______
    - (A) straight line
    - (B) circle
    - (C) parabola
    - (D) hyperbola

13. The number of points of intersection of the quadratic polynomial x² + x + 4 with the X axis is
    - (A) 0
    - (B) 1
    - (C) 0 or 1
    - (D) 2

14. For the given matrix 
```
      [ 1  3  5  7 ]
A =   [ 2  4  6  8 ]
      [ 9 11 13 15 ]
```
the order of the matrix Aᵀ is
    - (A) 2×3
    - (B) 3×2
    - (C) 3×4
    - (D) 4×3

15. If A is a 2×3 matrix and B is a 3×4 matrix, how many columns does AB have
    - (A) 3
    - (B) 4
    - (C) 2
    - (D) 5

16. If number of columns and rows are not equal in a matrix then it is said to be a
    - (A) diagonal matrix
    - (B) rectangular matrix
    - (C) square matrix
    - (D) identity matrix

17. Transpose of a column matrix is
    - (A) unit matrix
    - (B) diagonal matrix
    - (C) column matrix
    - (D) row matrix

18. Find the matrix X if 
```
      [ 1  3 ]       [ 5  7 ]
2 ×   [ 5  7 ] X =   [ 9  5 ]
```
    - (A) 
    ```
    [ -2 -2 ]
    [  2 -1 ]
    ```
    - (B) 
    ```
    [ 2  2 ]
    [ 2 -1 ]
    ```
    - (C) 
    ```
    [ 1  2 ]
    [ 2  2 ]
    ```
    - (D) 
    ```
    [ 2  1 ]
    [ 2  2 ]
    ```

19. Which of the following can be calculated from the given matrices
```
      [ 1  2 ]              [ 1  2  3 ]
A =   [ 3  4 ],        B =  [ 4  5  6 ]
      [ 5  6 ]              [ 7  8  9 ]
```
(i) A² (ii) B² (iii) AB (iv) BA

    - (A) (i) and (ii) only
    - (B) (ii) and (iii) only
    - (C) (ii) and (iv) only
    - (D) all of these

20. If 
```
      [ 1  0 ]              [ 0  1 ]
AB =  [ 2 -1 ],       C =   [ -2 5 ]
      [ 0  2 ]              [      ]
```
Which of the following statements are correct?
(i) AB + C = 
```
[ 5  5 ]
[ 5  5 ]
```
(ii) BC = 
```
[  0   1 ]
[  2  -3 ]
[ -4  10 ]
```
(iii) BA + C = 
```
[ 2  5 ]
[ 3  0 ]
```
(iv) (AB)C = 
```
[ -8  20 ]
[ -8  13 ]
```

    - (A) (i) and (ii) only
    - (B) (ii) and (iii) only
    - (C) (iii) and (iv) only
    - (D) all of these

## Unit Exercise - 3

1. Solve: 1/3(x+y-5) = y-z = 2x-11 = 9-(x+2z)

2. One hundred and fifty students are admitted to a school. They are distributed over three sections A, B and C. If 6 students are shifted from section A to section C, the sections will have equal number of students. If 4 times of students of section C exceeds the number of students of section A by the number of students in section B, find the number of students in the three sections.

3. In a three-digit number, when the tens and the hundreds digit are interchanged the new number is 54 more than three times the original number. If 198 is added to the number, the digits are reversed. The tens digit exceeds the hundreds digit by twice as that of the tens digit exceeds the unit digit. Find the original number.

4. Find the least common multiple of xy(k²x² + 2k²y²) and xy(k²x² - 2k²y²)

5. Find the GCD of the following by division algorithm:
   x⁴ + 2x³ + 3x² + 2x + 1, x³ + 3x² + 3x + 1, x² + 2x + 1

6. Reduce the given Rational expressions to its lowest form
   - (i) (a³ - a)/(a⁴ + a²)
   - (ii) (10x² - 25x + 10)/(4x² - 10x² - 2x)

7. Simplify: 
```
[ 1/(p²-q²) + 1/(q²-r²) + 1/(r²-p²) ] × [ (p+q)(q+r)(r+p) ] / [ (p-q)(q-r)(r-p) ]
```

8. Arul, Madan and Ram working together can clean a store in 6 hours. Working alone, Madan takes twice as long to clean the store as Arul does. Ram needs three times as long as Arul does. How long would it take each if they are working alone?

9. Find the square root of 289x⁸ - 612x⁶ + 970x⁴ - 684x² + 361.

10. Solve y² + y + 1 = 25/3

11. A boat takes 1.6 hours longer to go 36 kms up a river than down the river. If the speed of the water current is 4 km per hr, what is the speed of the boat in still water?

12. Is it possible to design a rectangular park of perimeter 320 m and area 4800 m²? If so find its length and breadth.

13. At t minutes past 2 pm, the time needed to 3 pm is 3 minutes less than t²/4. Find t.

14. The number of seats in a row is equal to the total number of rows in a hall. The total number of seats in the hall will increase by 375 if the number of rows is doubled and the number of seats in each row is reduced by 5. Find the number of rows in the hall at the beginning.

15. If a and b are the roots of the polynomial f(x) = x² - x + 2, find the polynomial whose roots are (i) a+2, b+2 (ii) (a-1)/(a+1), (b-1)/(b+1)

16. If –4 is a root of the equation x² + px - 24 = 0 and if the equation x² + px + q = 0 has equal roots, find the values of p and q.

17. Two farmers Thilagan and Kausigan cultivates three varieties of grains namely rice, wheat and ragi. If the sale (in ₹) of three varieties of grains by both the farmers in the month of April is given by the matrix.

```
[ 500  1000  1500 ]  Thilagan
[ 2500 1500   500 ]  Kausigan
  Rice  Wheat  Ragi
```

and the May month sale (in ₹) is exactly twice as that of the April month sale for each variety.

(i) What is the average sales of the months April and May.
(ii) If the sales continues to increase in the same way in the successive months, what will be sales in the month of August?

18. If 
```
[ cos θ   sin θ ]   [ sin θ  -cos θ ]     [ 1  0 ]
[ sin θ  -cos θ ] + [ cos θ   sin θ ] = I₂, find ...
```

19. Given 
```
      [ p  0 ]         [ 2   0 ]
A =   [ 0  2 ],    B = [ 0  10 ],    C = [ 2  -2 ]
                                      [ 2   2 ]
```
and if BA = C², find p and q.

20. If A = [3 0], B = [4 5], C = [3 6], find the matrix D, such that CD - AB = 0
          [4 5]      [6 3]      [8 5]             [3 6]
                   [1 1]

## Points to Remember

- A system of linear equations in three variables will be according to one of the following cases:
  - (i) Unique solution
  - (ii) Infinitely many solutions
  - (iii) No solution

- The least common multiple of two or more algebraic expressions is the expression of lowest degree (or power) such that the expressions exactly divides it.

- A polynomial of degree two in variable x is called a quadratic polynomial in x. Every quadratic polynomial can have atmost two zeroes. Also the zeroes of a quadratic polynomial intersects the x-axis.

- The roots of the quadratic equation ax² + bx + c = 0, (a ≠ 0) are given by [-b ± √(b²-4ac)]/(2a).

- For a quadratic equation ax² + bx + c = 0, a ≠ 0:
  - Sum of the roots: α + β = -b/a = -(Coefficient of x)/(Coefficient of x²)
  - Product of the roots: αβ = c/a = (Constant term)/(Coefficient of x²)

- If the roots of a quadratic equation are α and β, then the equation is given by x² - (α+β)x + αβ = 0.

- The value of the discriminant (Δ = b² - 4ac) decides the nature of roots as follows:
  - (i) When Δ > 0, the roots are real and unequal.
  - (ii) When Δ = 0, the roots are real and equal.
  - (iii) When Δ < 0, there are no real roots.

- Solving quadratic equation graphically.

- A matrix is a rectangular array of elements arranged in rows and columns.

- **Order of a matrix:** If a matrix A has m number of rows and n number of columns, then the order of the matrix A is (Number of rows) × (Number of columns) that is, m × n. We read m × n as m cross n or m by n. It may be noted that m × n is not a product of m and n.

- **Types of matrices:**
  - (i) A matrix is said to be a row matrix if it has only one row and any number of columns. A row matrix is also called as a row vector.
  - (ii) A matrix is said to be a column matrix if it has only one column and any number of rows. It is also called as a column vector.
  - (iii) A matrix in which the number of rows is equal to the number of columns is called a square matrix.
  - (iv) A matrix is said to be a zero matrix or null matrix if all its elements are zero.
  - (v) If A is a matrix, the matrix obtained by interchanging the rows and columns of A is called its transpose and is denoted by Aᵀ.
  - (vi) A square matrix, all of whose elements, except those in the leading diagonal are zero is called a diagonal matrix.
  - (vii) A diagonal matrix in which all the leading diagonal elements are same is called a scalar matrix.
  - (viii) A square matrix in which elements in the leading diagonal are all "1" and rest are all zero is called an identity matrix (or) unit matrix.
  - (ix) A square matrix in which all the entries above the leading diagonal are zero is called a lower triangular matrix. If all the entries below the leading diagonal are zero, then it is called an upper triangular matrix.
  - (x) Two matrices A and B are said to be equal if and only if they have the same order and each element of matrix A is equal to the corresponding element of matrix B. That is, aᵢⱼ = bᵢⱼ for all i, j.

- The negative of a matrix Aₘₓₙ denoted by -Aₘₓₙ is the matrix formed by replacing each element in the matrix Aₘₓₙ with its additive inverse.

- **Addition and subtraction of matrices:** Two matrices can be added or subtracted if they have the same order. To add or subtract two matrices, simply add or subtract the corresponding elements.

- **Multiplication of matrix by a scalar:** We can multiply the elements of the given matrix A by a non-zero number k to obtain a new matrix kA whose elements are multiplied by k. The matrix kA is called scalar multiplication of A. Thus if A = (aᵢⱼ)ₘₓₙ then, kA = (kaᵢⱼ)ₘₓₙ for all i = 1,2,...,m and for all j = 1,2,...,n.

## ICT CORNER

### ICT 3.1

Step 1: Open the Browser type the URL Link given below (or) Scan the QR Code. Chapter named "Algebra" will open. Select the work sheet "Simultaneous equations"

Step 2: In the given worksheet you can see three linear equations and you can change the equations by typing new values for a, b and c for each equation. You can move the 3-D graph to observe. Observe the nature of solutions by changing the equations.

### ICT 3.2

Step 1: Open the Browser type the URL Link given below (or) Scan the QR Code. GeoGebra work book named "ALGEBRA" will open. Click on the worksheet named "Nature of Quadratic Equation".

Step 2: In the given worksheet you can change the co-efficient by moving the sliders given. Click on "New position" and move the sliders to fix the boundary for throwing the shell. Then click on "Get Ball" and click "fire" to hit the target. Here you can learn what happen to the curve when each co-efficient is changed.

https://www.geogebra.org/m/jfr2zzgy#chapter/356193 or Scan the QR Code.
```