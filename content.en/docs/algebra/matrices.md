---
title: 'Matrices'
weight: 9
---

### 3.9 Matrices

#### Introduction

Let us consider the following information. Vanitha has 12 story books, 20 notebooks and 4 pencils. Radha has 27 story books, 17 notebooks and 6 pencils. Gokul has 7 story books, 11 notebooks and 4 pencils. Geetha has 10 story books, 12 notebooks and 5 pencils.

| Details | Story Books | Note Books | Pencils |
|---|---|---|---|
| Vanitha | 12 | 20 | 4 |
| Radha | 27 | 17 | 6 |
| Gokul | 7 | 11 | 4 |
| Geetha | 10 | 12 | 5 |

Now, we arrange this information in the tabular form as follows.

| First row | 12 | 20 | 4 |
|---|---|---|---|
| Second row | 27 | 17 | 6 |
| Third row | 7 | 11 | 4 |
| Fourth row | 10 | 12 | 5 |

First Second Third Column Column Column

Here, the items possessed by four people are aligned or positioned in a rectangular array containing four horizontal and three vertical arrangements. The horizontal arrangements are called "rows" and the vertical arrangements are called "columns". The whole rectangular arrangement is called a "Matrix". Generally, if we arrange things in a rectangular array, we call it as "Matrix".

Applications of matrices are found in several scientific fields. In Physics, matrices are applied in the calculations of battery power outputs, resistor conversion of electrical energy into other forms of energy. In computer based applications, matrices play a vital role in the projection of three dimensional image into a two dimensional screen, creating a realistic seeming motions. In graphic software, Matrix Algebra is used to process linear transformations to render images. One of the most important usage of matrices are encryption of message codes. The encryption and decryption process are carried out using matrix multiplication and inverse operations. The concept of matrices is used in transmission of codes when the messages are lengthy. In Geology, matrices are used for taking seismic surveys. In Robotics, matrices are used to identify the robot movements.

#### Definition

A matrix is a rectangular array of elements. The horizontal arrangements are called rows and vertical arrangements are called columns.

For example,

\[
\begin{bmatrix}
4 & 8 & 0 \\
1 & 9 & -2
\end{bmatrix}
\]

is a matrix.

Usually capital letters such as \( A, B, C, X, Y, \dots \) etc., are used to represent the matrices and small letters such as \( a, b, c, l, m, n, a_{12}, a_{13}, \dots \) to indicate the entries or elements of the matrices.

The following are some examples of matrices

\[
\begin{bmatrix}
1 & 0 \\
-1 & 2
\end{bmatrix},
\quad
\begin{bmatrix}
\sqrt{2} & 0 & 3
\end{bmatrix},
\quad
\begin{bmatrix}
1 \\
4 \\
-7
\end{bmatrix}
\]

#### 3.9.1 Order of a Matrix

If a matrix \( A \) has \( m \) number of rows and \( n \) number of columns, then the order of the matrix \( A \) is (Number of rows) \( \times \) (Number of columns) that is, \( m \times n \). We read \( m \times n \) as \( m \) cross \( n \) or \( m \) by \( n \). It may be noted that \( m \times n \) is not a product of \( m \) and \( n \).

General form of a matrix \( A \) with \( m \) rows and \( n \) columns (order \( m \times n \)) can be written in the form

\[
A =
\begin{bmatrix}
a_{11} & a_{12} & \dots & a_{1n} \\
a_{21} & a_{22} & \dots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \dots & a_{mn}
\end{bmatrix}
\]

where, \( a_{11}, a_{12}, \dots \) denote entries of the matrix. \( a_{11} \) is the element in first row, first column, \( a_{12} \) is the element in the first row, second column, and so on.

#### Progress Check

1. Find the element in the second row and third column of the matrix

\[
\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{bmatrix}
\]

2. Find the order of the matrix

\[
\begin{bmatrix}
1 & 3 & 5 \\
2 & 4 & 6
\end{bmatrix}
\]

3. Determine the entries denoted by \( a_{11}, a_{22}, a_{33}, a_{44} \) from the matrix

\[
\begin{bmatrix}
1 & 2 & 3 & 4 \\
5 & 6 & 7 & 8 \\
9 & 10 & 11 & 12 \\
13 & 14 & 15 & 16
\end{bmatrix}
\]

In general, \( a_{ij} \) is the element in the \( i^{\text{th}} \) row and \( j^{\text{th}} \) column and is referred as \( (i, j)^{\text{th}} \) element. With this notation, we can express the matrix \( A \) as

\[
A = (a_{ij})_{m \times n}
\]

where \( i = 1, 2, \dots, m \) and \( j = 1, 2, \dots, n \). The total number of entries in the matrix \( A = (a_{ij})_{m \times n} \) is \( mn \).

#### Note

When giving the order of a matrix, you should always mention the number of rows first, followed by the number of columns.

For example,

| S.No. | Matrices | Elements of the matrix | Order of the matrix |
|---|---|---|---|
| 1. | \( \begin{bmatrix} \sin\theta & -\cos\theta \\ \cos\theta & \sin\theta \end{bmatrix} \) | \( a_{11} = \sin\theta, a_{12} = -\cos\theta, \) \( a_{21} = \cos\theta, a_{22} = \sin\theta \) | \( 2 \times 2 \) |
| 2. | \( \begin{bmatrix} 1 & 3 \\ \sqrt{2} & 5 \\ \frac{1}{2} & -4 \end{bmatrix} \) | \( a_{11} = 1, a_{12} = 3, \) \( a_{21} = \sqrt{2}, a_{22} = 5, \) \( a_{31} = \frac{1}{2}, a_{32} = -4 \) | \( 3 \times 2 \) |

#### Activity 4

(i) Take calendar sheets of a particular month in a particular year.

(ii) Construct matrices from the dates of the calendar sheet.

(iii) Write down the number of possible matrices of orders \( 2 \times 2, 3 \times 2, 2 \times 3, 3 \times 3, 4 \times 3, \) etc.

(iv) Find the maximum possible order of a matrix that you can create from the given calendar sheet.

(v) Mention the use of matrices to organize information from daily life situations.

#### 3.9.2 Types of Matrices

In this section, we shall define certain types of matrices.

##### 1. Row Matrix

A matrix is said to be a row matrix if it has only one row and any number of columns. A row matrix is also called as a row vector.

For example,

\[
A = \begin{bmatrix} 8 & 9 & 4 & 3 \end{bmatrix}
\]

\[
B = \begin{bmatrix} -\sqrt{3} & 1 & \sqrt{3} \end{bmatrix}
\]

are row matrices of order \( 1 \times 4 \) and \( 1 \times 3 \) respectively.

In general,

\[
A = \begin{bmatrix} a_{11} & a_{12} & a_{13} & \dots & a_{1n} \end{bmatrix}
\]

is a row matrix of order \( 1 \times n \).

##### 2. Column Matrix

A matrix is said to be a column matrix if it has only one column and any number of rows. It is also called as a column vector.

For example,

\[
A = \begin{bmatrix} 1 \\ -3 \\ 5 \end{bmatrix}, \quad
B = \begin{bmatrix} 8 \\ 9 \\ 4 \\ 3 \end{bmatrix}
\]

are column matrices of order \( 3 \times 1 \) and \( 4 \times 1 \) respectively.

In general,

\[
A = \begin{bmatrix} a_{11} \\ a_{21} \\ a_{31} \\ \vdots \\ a_{m1} \end{bmatrix}
\]

is a column matrix of order \( m \times 1 \).

##### 3. Square Matrix

A matrix in which the number of rows is equal to the number of columns is called a square matrix. Thus a matrix \( A = (a_{ij})_{m \times n} \) will be a square matrix if \( m = n \).

For example,

\[
\begin{bmatrix} 1 & 3 \\ 4 & 5 \end{bmatrix}_{2 \times 2},
\quad
\begin{bmatrix} -1 & 0 & 2 \\ 3 & 6 & 8 \\ 2 & 3 & 5 \end{bmatrix}_{3 \times 3}
\]

are square matrices.

In general,

\[
\begin{bmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{bmatrix}_{2 \times 2},
\quad
\begin{bmatrix} b_{11} & b_{12} & b_{13} \\ b_{21} & b_{22} & b_{23} \\ b_{31} & b_{32} & b_{33} \end{bmatrix}
\]

are square matrices of orders \( 2 \times 2 \) and \( 3 \times 3 \) respectively.

\( A = (a_{ij})_{m \times m} \) is a square matrix of order \( m \).

**Definition:** In a square matrix, the elements of the form \( a_{11}, a_{22}, a_{33}, \dots \) (i.e.) \( a_{ii} \) are called leading diagonal elements. For example in the matrix

\[
\begin{bmatrix} 1 & 3 \\ 4 & 5 \end{bmatrix}
\]

1 and 5 are leading diagonal elements.

##### 4. Diagonal Matrix

A square matrix, all of whose elements, except those in the leading diagonal are zero is called a diagonal matrix.

A square matrix \( A = (a_{ij}) \) is said to be diagonal matrix if \( a_{ij} = 0 \) for \( i \neq j \). Note that some elements of the leading diagonal may be zero but not all.

For example,

\[
\begin{bmatrix} 8 & 0 & 0 \\ 0 & -3 & 0 \\ 0 & 0 & 11 \end{bmatrix},
\quad
\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{bmatrix}
\]

are diagonal matrices.

##### 5. Scalar Matrix

A diagonal matrix in which all the leading diagonal elements are equal is called a scalar matrix.

For example,

\[
\begin{bmatrix} 5 & 0 & 0 \\ 0 & 5 & 0 \\ 0 & 0 & 5 \end{bmatrix},
\quad
\begin{bmatrix} -3 & 0 \\ 0 & -3 \end{bmatrix}
\]

are scalar matrices.

##### 6. Identity (or) Unit Matrix

A square matrix in which elements in the leading diagonal are all "1" and rest are all zero is called an identity matrix or unit matrix.

Thus, the square matrix \( A = (a_{ij}) \) is an identity matrix if

\[
a_{ij} =
\begin{cases}
1 & \text{if } i = j \\
0 & \text{if } i \neq j
\end{cases}
\]

A unit matrix of order \( n \) is written as \( I_n \).

\[
I_1 = \begin{bmatrix} 1 \end{bmatrix},
\quad
I_2 = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix},
\quad
I_3 = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}
\]

##### 7. Zero matrix (or) null matrix

A matrix is said to be a zero matrix or null matrix if all its elements are zero.

For example,

\[
(0),
\quad
\begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix},
\quad
\begin{bmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix}
\]

are all zero matrices of order \( 1 \times 1, 2 \times 2 \) and \( 3 \times 3 \) but of different orders. We denote zero matrix of order \( n \times n \) by \( O_n \).

\[
\begin{bmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix}
\]

is a zero matrix of the order \( 2 \times 3 \).

##### 8. Transpose of a matrix

The matrix which is obtained by interchanging the elements in rows and columns of the given matrix \( A \) is called transpose of \( A \) and is denoted by \( A^T \).

For example,

\[
A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix}, \quad
A^T = \begin{bmatrix} 1 & 3 & 5 \\ 2 & 4 & 6 \end{bmatrix}
\]

\[
B = \begin{bmatrix} 1 & 3 & 5 \end{bmatrix}, \quad
B^T = \begin{bmatrix} 1 \\ 3 \\ 5 \end{bmatrix}
\]

If order of \( A \) is \( m \times n \) then order of \( A^T \) is \( n \times m \). We note that \( (A^T)^T = A \).

##### 9. Triangular Matrix

A square matrix in which all the entries above the leading diagonal are zero is called a lower triangular matrix.

If all the entries below the leading diagonal are zero, then it is called an upper triangular matrix.

**Definition:** A square matrix \( A = (a_{ij})_{n \times n} \) is called upper triangular matrix if \( a_{ij} = 0 \) for \( i > j \) and is called lower triangular matrix if \( a_{ij} = 0 \) for \( i < j \).

For example,

\[
A = \begin{bmatrix} 1 & 7 & -3 \\ 0 & 2 & 4 \\ 0 & 0 & 7 \end{bmatrix}
\]

is an upper triangular matrix and

\[
B = \begin{bmatrix} 8 & 0 & 0 \\ 4 & 5 & 0 \\ -11 & 3 & 1 \end{bmatrix}
\]

is a lower triangular matrix.

##### Equal Matrices

Two matrices \( A \) and \( B \) are said to be equal if and only if they have the same order and each element of matrix \( A \) is equal to the corresponding element of matrix \( B \). That is, \( a_{ij} = b_{ij} \) for all \( i, j \).

For example, if

\[
A = \begin{bmatrix} 5 & 1 \\ 0 & 3 \end{bmatrix}
\]

and

\[
B = \begin{bmatrix} 5 & 1 \\ 0 & 3 \end{bmatrix}
\]

note that \( A \) and \( B \) have same order and \( a_{ij} = b_{ij} \) for every \( i, j \). Hence, \( A \) and \( B \) are equal matrices.

#### Progress Check

1. The number of column(s) in a column matrix are ______.

2. The number of row(s) in a row matrix are ______.

3. The non-diagonal elements in any unit matrix are ______.

4. Does there exist a square matrix with 32 elements?

##### The negative of a matrix

The negative of a matrix \( A_{m \times n} \) denoted by \( -A_{m \times n} \) is the matrix formed by replacing each element in the matrix \( A_{m \times n} \) with its additive inverse.

Additive inverse of an element \( k \) is \( -k \). That is, every element of \( -A \) is the negative of the corresponding element of \( A \).

\[
A = \begin{bmatrix} 1 & -2 \\ 3 & 4 \end{bmatrix}, \quad
-A = \begin{bmatrix} -1 & 2 \\ -3 & -4 \end{bmatrix}
\]

#### Example 3.57

Consider the following information regarding the number of men and women workers in three factories I, II and III.

| Factory | Men | Women |
|---|---|---|
| I | 23 | 18 |
| II | 47 | 36 |
| III | 15 | 16 |

Represent the above information in the form of a matrix. What does the entry in the second row and first column represent?

#### Solution

The information is represented in the form of a \( 3 \times 2 \) matrix as follows

\[
A = \begin{bmatrix} 23 & 18 \\ 47 & 36 \\ 15 & 16 \end{bmatrix}
\]

The entry in the second row and first column represent that there are 47 men workers in factory II.

#### Example 3.58

If a matrix has 16 elements, what are the possible orders it can have?

#### Solution

We know that a matrix of order \( m \times n \), has \( mn \) elements. Thus to find all possible orders of a matrix with 16 elements, we will find all ordered pairs of natural numbers whose product is 16.

Such ordered pairs are (1, 16), (16, 1), (4, 4), (8, 2), (2, 8)

Hence, possible orders are \( 1 \times 16, 16 \times 1, 4 \times 4, 2 \times 8, 8 \times 2 \).

#### Activity 5

| No. | Elements | Possible orders | Number of possible orders |
|---|---|---|---|
| 1. | 4 | | |
| 2. | 9 | \( 1 \times 9, 9 \times 1, 3 \times 3 \) | |
| 3. | 20 | | |
| 4. | 84 | | |
| 5. | | | |
| 6. | 100 | | |
| 7. | 10 | \( 1 \times 10, 10 \times 1, 2 \times 5, 5 \times 2 \) | |

Do you find any relationship between number of elements (second column) and number of possible orders (fourth column)? If so, what is it?

#### Example 3.59

Construct a \( 3 \times 3 \) matrix whose elements are \( a_{ij} = i^2 j^2 \).

#### Solution

The general \( 3 \times 3 \) matrix is given by

\[
A = \begin{bmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{bmatrix}
\]

\( a_{ij} = i^2 j^2 \)

\[
a_{11} = 1^2 \times 1^2 = 1
\]

\[
a_{12} = 1^2 \times 2^2 = 4
\]

\[
a_{13} = 1^2 \times 3^2 = 9
\]

\[
a_{21} = 2^2 \times 1^2 = 4
\]

\[
a_{22} = 2^2 \times 2^2 = 16
\]

\[
a_{23} = 2^2 \times 3^2 = 36
\]

\[
a_{31} = 3^2 \times 1^2 = 9
\]

\[
a_{32} = 3^2 \times 2^2 = 36
\]

\[
a_{33} = 3^2 \times 3^2 = 81
\]

Hence, the required matrix is

\[
A = \begin{bmatrix}
1 & 4 & 9 \\
4 & 16 & 36 \\
9 & 36 & 81
\end{bmatrix}
\]

#### Example 3.60

Find the value of \( a, b, c, d \) from the equation

\[
\begin{bmatrix} a - b & 2a + c \\ 2a - b & 3c + d \end{bmatrix}
=
\begin{bmatrix} 1 & 5 \\ 0 & 2 \end{bmatrix}
\]

#### Solution

The given matrices are equal. Thus all corresponding elements are equal.

\[
a - b = 1 \tag{1}
\]

\[
2a + c = 5 \tag{2}
\]

\[
2a - b = 0 \tag{3}
\]

\[
3c + d = 2 \tag{4}
\]

From (1) and (3):

Subtracting (1) from (3),

\[
(2a - b) - (a - b) = 0 - 1
\]

\[
a = -1
\]

Substituting \( a = -1 \) in (1):

\[
-1 - b = 1 \Rightarrow b = -2
\]

Substituting \( a = -1 \) in (2):

\[
2(-1) + c = 5 \Rightarrow c = 7
\]

Substituting \( c = 7 \) in (4):

\[
3(7) + d = 2 \Rightarrow d = -19
\]

Therefore,

\[
a = -1, \quad b = -2, \quad c = 7, \quad d = -19
\]

### Exercise 3.16

1. Construct a matrix of order \( 3 \times 3 \) whose elements are given by

(i) \( a_{ij} = i + j \)

(ii) \( a_{ij} = i - j \)

(iii) \( a_{ij} = i \times j \)

2. Find the values of \( x, y, z \) if

\[
\begin{bmatrix} x & y \\ z & 2 \end{bmatrix}
=
\begin{bmatrix} 1 & 3 \\ 4 & 2 \end{bmatrix}
\]

3. Find the values of \( a, b, c, d \) if

\[
\begin{bmatrix} a + b & c + d \\ a - b & c - d \end{bmatrix}
=
\begin{bmatrix} 5 & 6 \\ 3 & 2 \end{bmatrix}
\]

4. Find the values of \( x, y, z, w \) if

\[
\begin{bmatrix} x + y & x - z \\ y + z & w \end{bmatrix}
=
\begin{bmatrix} 5 & 1 \\ 3 & 4 \end{bmatrix}
\]

5. Find the values of \( a, b, c, d \) if

\[
\begin{bmatrix} a - b & 2a + c \\ 2a - b & 3c + d \end{bmatrix}
=
\begin{bmatrix} -1 & 5 \\ 0 & 13 \end{bmatrix}
\]

#### 3.9.3 Operations on Matrices

In this section, we shall discuss the addition and subtraction of matrices, multiplication of a matrix by a scalar and multiplication of matrices.

##### Addition and subtraction of matrices

Two matrices can be added or subtracted if they have the same order. To add or subtract two matrices, simply add or subtract the corresponding elements.

If \( A = (a_{ij}) \), \( B = (b_{ij}) \), \( i = 1, 2, \dots, m \), \( j = 1, 2, \dots, n \) then \( C = A + B \) is such that \( C = (c_{ij}) \) where

\[
c_{ij} = a_{ij} + b_{ij}
\]

for all \( i = 1, 2, \dots, m \) and \( j = 1, 2, \dots, n \).

#### Example 3.61

If

\[
A = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{bmatrix},
\quad
B = \begin{bmatrix} 1 & 7 & 0 \\ 1 & 3 & 1 \\ 2 & 4 & 0 \end{bmatrix}
\]

find \( A + B \).

#### Solution

\[
A + B =
\begin{bmatrix}
1+1 & 2+7 & 3+0 \\
4+1 & 5+3 & 6+1 \\
7+2 & 8+4 & 9+0
\end{bmatrix}
=
\begin{bmatrix}
2 & 9 & 3 \\
5 & 8 & 7 \\
9 & 12 & 9
\end{bmatrix}
\]

#### Example 3.62

Two examinations were conducted for three groups of students namely group 1, group 2, group 3 and their data on average of marks for the subjects Tamil, English, Science and Mathematics are given below in the form of matrices \( A \) and \( B \). Find the total marks of both the examinations for all the three groups.

\[
A = \begin{bmatrix}
50 & 60 & 70 & 80 \\
55 & 65 & 75 & 85 \\
60 & 70 & 80 & 90
\end{bmatrix},
\quad
B = \begin{bmatrix}
40 & 50 & 60 & 70 \\
45 & 55 & 65 & 75 \\
50 & 60 & 70 & 80
\end{bmatrix}
\]

#### Solution

The total marks in both the examinations for all the three groups is the sum of the given matrices.

\[
A + B =
\begin{bmatrix}
50+40 & 60+50 & 70+60 & 80+70 \\
55+45 & 65+55 & 75+65 & 85+75 \\
60+50 & 70+60 & 80+70 & 90+80
\end{bmatrix}
=
\begin{bmatrix}
90 & 110 & 130 & 150 \\
100 & 120 & 140 & 160 \\
110 & 130 & 150 & 170
\end{bmatrix}
\]

#### Example 3.63

If

\[
A = \begin{bmatrix} 3 & -2 \\ 5 & 4 \\ -3 & 2 \end{bmatrix},
\quad
B = \begin{bmatrix} 1 & 8 \\ 3 & 4 \\ 9 & 6 \end{bmatrix}
\]

find \( A + B \).

#### Solution

It is not possible to add \( A \) and \( B \) because they have different orders. \( A \) is of order \( 3 \times 2 \) and \( B \) is of order \( 3 \times 2 \). Wait, they have the same order \( 3 \times 2 \). So addition is possible.

\[
A + B =
\begin{bmatrix}
3+1 & -2+8 \\
5+3 & 4+4 \\
-3+9 & 2+6
\end{bmatrix}
=
\begin{bmatrix}
4 & 6 \\
8 & 8 \\
6 & 8
\end{bmatrix}
\]

##### Multiplication of Matrix by a Scalar

We can multiply the elements of the given matrix \( A \) by a non-zero number \( k \) to obtain a new matrix \( kA \) whose elements are multiplied by \( k \). The matrix \( kA \) is called scalar multiplication of \( A \).

Thus if \( A = (a_{ij})_{m \times n} \) then,

\[
kA = (ka_{ij})_{m \times n}
\]

for all \( i = 1, 2, \dots, m \) and \( j = 1, 2, \dots, n \).

#### Example 3.64

If

\[
A = \begin{bmatrix} 7 & 8 & 6 \\ 1 & 3 & 9 \\ -4 & 3 & -1 \end{bmatrix},
\quad
B = \begin{bmatrix} 4 & 11 & -3 \\ -1 & 2 & 4 \\ 7 & 5 & 0 \end{bmatrix}
\]

then find \( 2A + B \).

#### Solution

Since \( A \) and \( B \) have same order \( 3 \times 3 \), \( 2A + B \) is defined.

\[
2A =
\begin{bmatrix}
14 & 16 & 12 \\
2 & 6 & 18 \\
-8 & 6 & -2
\end{bmatrix}
\]

\[
2A + B =
\begin{bmatrix}
14+4 & 16+11 & 12-3 \\
2-1 & 6+2 & 18+4 \\
-8+7 & 6+5 & -2+0
\end{bmatrix}
=
\begin{bmatrix}
18 & 27 & 9 \\
1 & 8 & 22 \\
-1 & 11 & -2
\end{bmatrix}
\]

#### Example 3.65

If

\[
A = \begin{bmatrix}
5 & 4 & -2 \\
\frac{1}{2} & \frac{3}{4} & \sqrt{2} \\
1 & 9 & 4
\end{bmatrix},
\quad
B = \begin{bmatrix}
-7 & 4 & -3 \\
\frac{1}{2} & \frac{7}{2} & 3 \\
5 & -6 & 9
\end{bmatrix}
\]

find \( 4A - 3B \).

#### Solution

Since \( A, B \) are of the same order \( 3 \times 3 \), subtraction of \( 4A \) and \( 3B \) is defined.

\[
4A =
\begin{bmatrix}
20 & 16 & -8 \\
2 & 3 & 4\sqrt{2} \\
4 & 36 & 16
\end{bmatrix}
\]

\[
3B =
\begin{bmatrix}
-21 & 12 & -9 \\
\frac{3}{2} & \frac{21}{2} & 9 \\
15 & -18 & 27
\end{bmatrix}
\]

\[
4A - 3B =
\begin{bmatrix}
20-(-21) & 16-12 & -8-(-9) \\
2-\frac{3}{2} & 3-\frac{21}{2} & 4\sqrt{2}-9 \\
4-15 & 36-(-18) & 16-27
\end{bmatrix}
=
\begin{bmatrix}
41 & 4 & 1 \\
\frac{1}{2} & -\frac{15}{2} & 4\sqrt{2}-9 \\
-11 & 54 & -11
\end{bmatrix}
\]

##### Properties of Matrix Addition and Scalar Multiplication

Let \( A, B, C \) be \( m \times n \) matrices and \( p \) and \( q \) be two non-zero scalars (numbers). Then we have the following properties.

(i) \( A + B = B + A \) [Commutative property of matrix addition]

(ii) \( A + (B + C) = (A + B) + C \) [Associative property of matrix addition]

(iii) \( (pq)A = p(qA) \) [Associative property of scalar multiplication]

(iv) \( IA = A \) [Scalar Identity property where \( I \) is the unit matrix]

(v) \( p(A + B) = pA + pB \) [Distributive property of scalar and two matrices]

(vi) \( (p + q)A = pA + qA \) [Distributive property of two scalars with a matrix]

##### Additive Identity

The null matrix or zero matrix is the identity for matrix addition.

Let \( A \) be any matrix.

Then,

\[
A + O = O + A = A
\]

where \( O \) is the null matrix or zero matrix of same order as that of \( A \).

##### Additive Inverse

If \( A \) be any given matrix then \( -A \) is the additive inverse of \( A \).

In fact we have

\[
A + (-A) = (-A) + A = O
\]

#### Example 3.66

Find the value of \( a, b, c, d \) from the following matrix equation.

\[
\begin{bmatrix} a + 3 & 4 \\ 2 & b - 1 \end{bmatrix}
+
\begin{bmatrix} 4 & 1 \\ c & d + 3 \end{bmatrix}
=
\begin{bmatrix} 14 & 5 \\ 6 & 9 \end{bmatrix}
\]

#### Solution

First, we add the two matrices on left hand side to get

\[
\begin{bmatrix} a + 3 + 4 & 4 + 1 \\ 2 + c & b - 1 + d + 3 \end{bmatrix}
=
\begin{bmatrix} 14 & 5 \\ 6 & 9 \end{bmatrix}
\]

\[
\begin{bmatrix} a + 7 & 5 \\ c + 2 & b + d + 2 \end{bmatrix}
=
\begin{bmatrix} 14 & 5 \\ 6 & 9 \end{bmatrix}
\]

Equating the corresponding elements of the two matrices, we have

\[
a + 7 = 14 \Rightarrow a = 7
\]

\[
c + 2 = 6 \Rightarrow c = 4
\]

\[
b + d + 2 = 9 \Rightarrow b + d = 7 \tag{1}
\]

From the element \( a_{12} = 5 \), we have \( 5 = 5 \), which is true.

We need one more equation to find \( b \) and \( d \). Let us check the given problem again.

Actually the given equation is

\[
\begin{bmatrix} a - 4 & 4 \\ 2 & b - 1 \end{bmatrix}
+
\begin{bmatrix} 4 & 1 \\ c & d + 3 \end{bmatrix}
=
\begin{bmatrix} 14 & 5 \\ 6 & 9 \end{bmatrix}
\]

Then,

\[
\begin{bmatrix} a - 4 + 4 & 4 + 1 \\ 2 + c & b - 1 + d + 3 \end{bmatrix}
=
\begin{bmatrix} 14 & 5 \\ 6 & 9 \end{bmatrix}
\]

\[
\begin{bmatrix} a & 5 \\ c + 2 & b + d + 2 \end{bmatrix}
=
\begin{bmatrix} 14 & 5 \\ 6 & 9 \end{bmatrix}
\]

\[
a = 14
\]

\[
c + 2 = 6 \Rightarrow c = 4
\]

\[
b + d + 2 = 9 \Rightarrow b + d = 7
\]

Therefore, \( a = 14, c = 4, b + d = 7 \).

#### Example 3.67

If

\[
A = \begin{bmatrix} 8 & 3 \\ 3 & 5 \\ 8 & 7 \end{bmatrix},
\quad
B = \begin{bmatrix} 8 & -6 \\ 2 & 11 \\ 0 & 1 \end{bmatrix},
\quad
C = \begin{bmatrix} -4 & 5 \\ -1 & -7 \\ 1 & 4 \end{bmatrix}
\]

compute the following:

(i) \( 3A + 2B - C \)

(ii) \( \frac{1}{2}A - 3B \)

#### Solution

(i)
\[
3A + 2B - C =
3\begin{bmatrix} 8 & 3 \\ 3 & 5 \\ 8 & 7 \end{bmatrix}
+
2\begin{bmatrix} 8 & -6 \\ 2 & 11 \\ 0 & 1 \end{bmatrix}
-
\begin{bmatrix} -4 & 5 \\ -1 & -7 \\ 1 & 4 \end{bmatrix}
\]

\[
=
\begin{bmatrix} 24 & 9 \\ 9 & 15 \\ 24 & 21 \end{bmatrix}
+
\begin{bmatrix} 16 & -12 \\ 4 & 22 \\ 0 & 2 \end{bmatrix}
-
\begin{bmatrix} -4 & 5 \\ -1 & -7 \\ 1 & 4 \end{bmatrix}
\]

\[
=
\begin{bmatrix} 24+16-(-4) & 9-12-5 \\ 9+4-(-1) & 15+22-(-7) \\ 24+0-1 & 21+2-4 \end{bmatrix}
=
\begin{bmatrix} 44 & -8 \\ 14 & 44 \\ 23 & 19 \end{bmatrix}
\]

(ii)
\[
\frac{1}{2}A - 3B = \frac{1}{2}(A - 6B)
\]

\[
= \frac{1}{2}\left( \begin{bmatrix} 8 & 3 \\ 3 & 5 \\ 8 & 7 \end{bmatrix}
-
6\begin{bmatrix} 8 & -6 \\ 2 & 11 \\ 0 & 1 \end{bmatrix} \right)
\]

\[
= \frac{1}{2}\left( \begin{bmatrix} 8 & 3 \\ 3 & 5 \\ 8 & 7 \end{bmatrix}
-
\begin{bmatrix} 48 & -36 \\ 12 & 66 \\ 0 & 6 \end{bmatrix} \right)
\]

\[
= \frac{1}{2}\begin{bmatrix} -40 & 39 \\ -9 & -61 \\ 8 & 1 \end{bmatrix}
=
\begin{bmatrix} -20 & \frac{39}{2} \\ -\frac{9}{2} & -\frac{61}{2} \\ 4 & \frac{1}{2} \end{bmatrix}
\]

### Exercise 3.17

1. If

\[
A = \begin{bmatrix} 3 & 4 \\ 8 & -3 \end{bmatrix},
\quad
B = \begin{bmatrix} 3 & 3 \\ 1 & 0 \end{bmatrix}
\]

then verify that

(i) \( A + B = B + A \)

(ii) \( A + (-A) = (-A) + A = O \)

2. If

\[
A = \begin{bmatrix} 4 & 3 & 1 \\ 2 & 3 & 4 \\ 8 & 3 & 4 \end{bmatrix},
\quad
B = \begin{bmatrix} 8 & 3 & 4 \\ 1 & -2 & 3 \\ 2 & 4 & -1 \end{bmatrix},
\quad
C = \begin{bmatrix} 1 & -7 & 3 \\ 2 & 4 & -1 \\ 1 & 2 & 4 \end{bmatrix}
\]

then verify that

\[
A + (B + C) = (A + B) + C
\]

3. Find \( X \) and \( Y \) if

\[
X + Y = \begin{bmatrix} 7 & 0 \\ 3 & 5 \end{bmatrix}
\quad \text{and} \quad
X - Y = \begin{bmatrix} 3 & 0 \\ 0 & 4 \end{bmatrix}
\]

4. If

\[
A = \begin{bmatrix} 0 & 4 & 9 \\ 8 & 3 & 7 \end{bmatrix},
\quad
B = \begin{bmatrix} 7 & 3 & 8 \\ 1 & 4 & 9 \end{bmatrix}
\]

find the value of

(i) \( B - 5A \)

(ii) \( 3A - 9B \)

5. Find the values of \( x, y, z \) if

(i)
\[
\begin{bmatrix} x - 3 & 3x - z \\ x + y + 7 & x + y + z \end{bmatrix}
=
\begin{bmatrix} 1 & 0 \\ 1 & 6 \end{bmatrix}
\]

(ii)
\[
\begin{bmatrix} x - y - z & 3 \end{bmatrix}
+
\begin{bmatrix} y & 4 \end{bmatrix}
=
\begin{bmatrix} 4 & 8 \end{bmatrix}
\]

6. Find \( x \) and \( y \) if

\[
x\begin{bmatrix} 4 \\ -3 \end{bmatrix}
+
y\begin{bmatrix} -2 \\ 3 \end{bmatrix}
=
\begin{bmatrix} 4 \\ 6 \end{bmatrix}
\]

7. Find the non-zero values of \( x \) satisfying the matrix equation

\[
x\begin{bmatrix} 2x & 2 \\ 3 & x \end{bmatrix}
+
2\begin{bmatrix} 8 & 5x \\ 4 & 4x \end{bmatrix}
=
2\begin{bmatrix} x^2 + 8 & 24 \\ 10 & 6x \end{bmatrix}
\]

8. Solve for \( x, y \):

\[
\begin{bmatrix} x^2 \\ y^2 \end{bmatrix}
+
2\begin{bmatrix} -2x \\ -y \end{bmatrix}
=
\begin{bmatrix} 5 \\ 8 \end{bmatrix}
\]

##### Multiplication of Matrices

To multiply two matrices, the number of columns in the first matrix must be equal to the number of rows in the second matrix. Consider the multiplications of \( 3 \times 3 \) and \( 3 \times 2 \) matrices.

(Order of left hand matrix) \( \times \) (order of right hand matrix) \( \rightarrow \) (order of product matrix).

\[
(3 \times 3)(3 \times 2) \rightarrow (3 \times 2)
\]

Matrices are multiplied by multiplying the elements in a row of the first matrix by the elements in a column of the second matrix, and adding the results.

For example, product of matrices

\[
\begin{bmatrix} a & b \\ c & d \\ e & f \end{bmatrix}
\times
\begin{bmatrix} g & h & i \\ k & l & m \end{bmatrix}
=
\begin{bmatrix}
ag + bk & ah + bl & ai + bm \\
cg + dk & ch + dl & ci + dm \\
eg + fk & eh + fl & ei + fm
\end{bmatrix}
\]

The product \( AB \) can be found if the number of columns of matrix \( A \) is equal to the number of rows of matrix \( B \). If the order of matrix \( A \) is \( m \times n \) and \( B \) is \( n \times p \) then the order of \( AB \) is \( m \times p \).

##### Properties of Multiplication of Matrix

**(a) Matrix multiplication is not commutative in general**

If \( A \) is of order \( m \times n \) and \( B \) of the order \( n \times p \) then \( AB \) is defined but \( BA \) is not defined. Even if \( AB \) and \( BA \) are both defined, it is not necessary that they are equal. In general

\[
AB \neq BA
\]

**(b) Matrix multiplication is distributive over matrix addition**

(i) If \( A, B, C \) are \( m \times n, n \times p \) and \( n \times p \) matrices respectively then

\[
A(B + C) = AB + AC
\]

(Right Distributive Property)

(ii) If \( A, B, C \) are \( m \times n, m \times n \) and \( n \times p \) matrices respectively then

\[
(A + B)C = AC + BC
\]

(Left Distributive Property)

**(c) Matrix multiplication is always associative**

If \( A, B, C \) are \( m \times n, n \times p \) and \( p \times q \) matrices respectively then

\[
(AB)C = A(BC)
\]

**(d) Multiplication of a matrix by a unit matrix**

If \( A \) is a square matrix of order \( n \times n \) and \( I \) is the unit matrix of same order then

\[
AI = IA = A
\]

#### Note

If \( x \) and \( y \) are two real numbers such that \( xy = 0 \) then either \( x = 0 \) or \( y = 0 \). But this condition may not be true with respect to two matrices.

\( AB = 0 \) does not necessarily imply that \( A = 0 \) or \( B = 0 \) or both \( A, B = 0 \).

#### Illustration

\[
A = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix},
\quad
B = \begin{bmatrix} 0 & 0 \\ 1 & 0 \end{bmatrix}
\]

\[
AB = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}
\begin{bmatrix} 0 & 0 \\ 1 & 0 \end{bmatrix}
=
\begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}
\]

Thus \( A \neq 0 \), \( B \neq 0 \) but \( AB \neq 0 \).

#### Example 3.68

If

\[
A = \begin{bmatrix} 1 & 2 & 0 \\ 3 & 1 & 5 \end{bmatrix},
\quad
B = \begin{bmatrix} 8 & 3 & 1 \\ 2 & 4 & 1 \\ 5 & 3 & 1 \end{bmatrix}
\]

find \( AB \).

#### Solution

We observe that \( A \) is a \( 2 \times 3 \) matrix and \( B \) is a \( 3 \times 3 \) matrix, hence \( AB \) is defined and it will be of the order \( 2 \times 3 \).

\[
AB =
\begin{bmatrix}
1(8)+2(2)+0(5) & 1(3)+2(4)+0(3) & 1(1)+2(1)+0(1) \\
3(8)+1(2)+5(5) & 3(3)+1(4)+5(3) & 3(1)+1(1)+5(1)
\end{bmatrix}
\]

\[
=
\begin{bmatrix}
8+4+0 & 3+8+0 & 1+2+0 \\
24+2+25 & 9+4+15 & 3+1+5
\end{bmatrix}
=
\begin{bmatrix}
12 & 11 & 3 \\
51 & 28 & 9
\end{bmatrix}
\]

#### Example 3.69

If

\[
A = \begin{bmatrix} 2 & 1 \\ 1 & 3 \end{bmatrix},
\quad
B = \begin{bmatrix} 2 & 0 \\ 1 & 3 \end{bmatrix}
\]

find \( AB \) and \( BA \). Verify \( AB = BA \)?

#### Solution

We observe that \( A \) is a \( 2 \times 2 \) matrix and \( B \) is a \( 2 \times 2 \) matrix, hence \( AB \) is defined and it will be of the order \( 2 \times 2 \).

\[
AB =
\begin{bmatrix}
2(2)+1(1) & 2(0)+1(3) \\
1(2)+3(1) & 1(0)+3(3)
\end{bmatrix}
=
\begin{bmatrix}
4+1 & 0+3 \\
2+3 & 0+9
\end{bmatrix}
=
\begin{bmatrix}
5 & 3 \\
5 & 9
\end{bmatrix}
\]

\[
BA =
\begin{bmatrix}
2(2)+0(1) & 2(1)+0(3) \\
1(2)+3(1) & 1(1)+3(3)
\end{bmatrix}
=
\begin{bmatrix}
4+0 & 2+0 \\
2+3 & 1+9
\end{bmatrix}
=
\begin{bmatrix}
4 & 2 \\
5 & 10
\end{bmatrix}
\]

Therefore, \( AB \neq BA \).

#### Example 3.70

If

\[
A = \begin{bmatrix} \frac{2}{2} & -2 \\ 2 & \frac{2}{2} \end{bmatrix},
\quad
B = \begin{bmatrix} \frac{2}{2} & -2 \\ 2 & \frac{2}{2} \end{bmatrix}
\]

Show that \( A \) and \( B \) satisfy commutative property with respect to matrix multiplication.

#### Solution

We have to show that \( AB = BA \).

LHS = \( AB \)

\[
AB =
\begin{bmatrix} 1 & -2 \\ 2 & 1 \end{bmatrix}
\begin{bmatrix} 1 & -2 \\ 2 & 1 \end{bmatrix}
=
\begin{bmatrix}
1(1)+(-2)(2) & 1(-2)+(-2)(1) \\
2(1)+1(2) & 2(-2)+1(1)
\end{bmatrix}
=
\begin{bmatrix}
1-4 & -2-2 \\
2+2 & -4+1
\end{bmatrix}
=
\begin{bmatrix}
-3 & -4 \\
4 & -3
\end{bmatrix}
\]

RHS = \( BA \)

\[
BA =
\begin{bmatrix} 1 & -2 \\ 2 & 1 \end{bmatrix}
\begin{bmatrix} 1 & -2 \\ 2 & 1 \end{bmatrix}
=
\begin{bmatrix}
1(1)+(-2)(2) & 1(-2)+(-2)(1) \\
2(1)+1(2) & 2(-2)+1(1)
\end{bmatrix}
=
\begin{bmatrix}
-3 & -4 \\
4 & -3
\end{bmatrix}
\]

Hence, LHS = RHS (i.e.) \( AB = BA \).

#### Example 3.71

Solve

\[
\begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}
\begin{bmatrix} x \\ y \end{bmatrix}
=
\begin{bmatrix} 4 \\ 5 \end{bmatrix}
\]

#### Solution

By matrix multiplication,

\[
\begin{bmatrix} 2x + y \\ x + 2y \end{bmatrix}
=
\begin{bmatrix} 4 \\ 5 \end{bmatrix}
\]

Rewriting,

\[
2x + y = 4 \tag{1}
\]

\[
x + 2y = 5 \tag{2}
\]

(1) \( \times 2 \):

\[
4x + 2y = 8
\]

Subtracting (2) from this,

\[
(4x + 2y) - (x + 2y) = 8 - 5
\]

\[
3x = 3 \Rightarrow x = 1
\]

Substituting \( x = 1 \) in (1),

\[
2(1) + y = 4 \Rightarrow y = 2
\]

Therefore,

\[
x = 1, \quad y = 2
\]

#### Example 3.72

If

\[
A = \begin{bmatrix} 1 & -1 & 2 \end{bmatrix},
\quad
B = \begin{bmatrix} 1 & -1 \\ 2 & 1 \\ 1 & 3 \end{bmatrix},
\quad
C = \begin{bmatrix} 1 & -2 \\ 2 & 1 \end{bmatrix}
\]

show that \( (AB)C = A(BC) \).

#### Solution

LHS = \( (AB)C \)

\[
AB =
\begin{bmatrix} 1 & -1 & 2 \end{bmatrix}
\begin{bmatrix} 1 & -1 \\ 2 & 1 \\ 1 & 3 \end{bmatrix}
=
\begin{bmatrix}
1(1)+(-1)(2)+2(1) & 1(-1)+(-1)(1)+2(3)
\end{bmatrix}
=
\begin{bmatrix}
1-2+2 & -1-1+6
\end{bmatrix}
=
\begin{bmatrix} 1 & 4 \end{bmatrix}
\]

\[
(AB)C =
\begin{bmatrix} 1 & 4 \end{bmatrix}
\begin{bmatrix} 1 & -2 \\ 2 & 1 \end{bmatrix}
=
\begin{bmatrix}
1(1)+4(2) & 1(-2)+4(1)
\end{bmatrix}
=
\begin{bmatrix}
1+8 & -2+4
\end{bmatrix}
=
\begin{bmatrix} 9 & 2 \end{bmatrix} \tag{1}
\]

RHS = \( A(BC) \)

\[
BC =
\begin{bmatrix} 1 & -1 \\ 2 & 1 \\ 1 & 3 \end{bmatrix}
\begin{bmatrix} 1 & -2 \\ 2 & 1 \end{bmatrix}
=
\begin{bmatrix}
1(1)+(-1)(2) & 1(-2)+(-1)(1) \\
2(1)+1(2) & 2(-2)+1(1) \\
1(1)+3(2) & 1(-2)+3(1)
\end{bmatrix}
=
\begin{bmatrix}
1-2 & -2-1 \\
2+2 & -4+1 \\
1+6 & -2+3
\end{bmatrix}
=
\begin{bmatrix}
-1 & -3 \\
4 & -3 \\
7 & 1
\end{bmatrix}
\]

\[
A(BC) =
\begin{bmatrix} 1 & -1 & 2 \end{bmatrix}
\begin{bmatrix}
-1 & -3 \\
4 & -3 \\
7 & 1
\end{bmatrix}
=
\begin{bmatrix}
1(-1)+(-1)(4)+2(7) & 1(-3)+(-1)(-3)+2(1)
\end{bmatrix}
=
\begin{bmatrix}
-1-4+14 & -3+3+2
\end{bmatrix}
=
\begin{bmatrix} 9 & 2 \end{bmatrix} \tag{2}
\]

From (1) and (2), \( (AB)C = A(BC) \).

#### Example 3.73

If

\[
A = \begin{bmatrix} -1 & 1 \\ 1 & 3 \end{bmatrix},
\quad
B = \begin{bmatrix} -1 & 2 \\ 4 & 2 \end{bmatrix},
\quad
C = \begin{bmatrix} -7 & 6 \\ 3 & 2 \end{bmatrix}
\]

verify that \( A(B + C) = AB + AC \).

#### Solution

LHS = \( A(B + C) \)

\[
B + C =
\begin{bmatrix} -1 & 2 \\ 4 & 2 \end{bmatrix}
+
\begin{bmatrix} -7 & 6 \\ 3 & 2 \end{bmatrix}
=
\begin{bmatrix}
-1-7 & 2+6 \\
4+3 & 2+2
\end{bmatrix}
=
\begin{bmatrix}
-8 & 8 \\
7 & 4
\end{bmatrix}
\]

\[
A(B + C) =
\begin{bmatrix} -1 & 1 \\ 1 & 3 \end{bmatrix}
\begin{bmatrix} -8 & 8 \\ 7 & 4 \end{bmatrix}
=
\begin{bmatrix}
-1(-8)+1(7) & -1(8)+1(4) \\
1(-8)+3(7) & 1(8)+3(4)
\end{bmatrix}
=
\begin{bmatrix}
8+7 & -8+4 \\
-8+21 & 8+12
\end{bmatrix}
=
\begin{bmatrix}
15 & -4 \\
13 & 20
\end{bmatrix} \tag{1}
\]

RHS = \( AB + AC \)

\[
AB =
\begin{bmatrix} -1 & 1 \\ 1 & 3 \end{bmatrix}
\begin{bmatrix} -1 & 2 \\ 4 & 2 \end{bmatrix}
=
\begin{bmatrix}
-1(-1)+1(4) & -1(2)+1(2) \\
1(-1)+3(4) & 1(2)+3(2)
\end{bmatrix}
=
\begin{bmatrix}
1+4 & -2+2 \\
-1+12 & 2+6
\end{bmatrix}
=
\begin{bmatrix}
5 & 0 \\
11 & 8
\end{bmatrix}
\]

\[
AC =
\begin{bmatrix} -1 & 1 \\ 1 & 3 \end{bmatrix}
\begin{bmatrix} -7 & 6 \\ 3 & 2 \end{bmatrix}
=
\begin{bmatrix}
-1(-7)+1(3) & -1(6)+1(2) \\
1(-7)+3(3) & 1(6)+3(2)
\end{bmatrix}
=
\begin{bmatrix}
7+3 & -6+2 \\
-7+9 & 6+6
\end{bmatrix}
=
\begin{bmatrix}
10 & -4 \\
2 & 12
\end{bmatrix}
\]

\[
AB + AC =
\begin{bmatrix}
5+10 & 0-4 \\
11+2 & 8+12
\end{bmatrix}
=
\begin{bmatrix}
15 & -4 \\
13 & 20
\end{bmatrix} \tag{2}
\]

From (1) and (2), \( A(B + C) = AB + AC \). Hence proved.

#### Example 3.74

If

\[
A = \begin{bmatrix} 1 & 2 & 1 \\ 2 & -1 & 1 \\ 0 & 2 & 2 \end{bmatrix},
\quad
B = \begin{bmatrix} 2 & -1 \\ -1 & 4 \\ 0 & 2 \end{bmatrix}
\]

show that \( (AB)^T = B^T A^T \).

#### Solution

LHS = \( (AB)^T \)

\[
AB =
\begin{bmatrix}
1(2)+2(-1)+1(0) & 1(-1)+2(4)+1(2) \\
2(2)+(-1)(-1)+1(0) & 2(-1)+(-1)(4)+1(2) \\
0(2)+2(-1)+2(0) & 0(-1)+2(4)+2(2)
\end{bmatrix}
=
\begin{bmatrix}
2-2+0 & -1+8+2 \\
4+1+0 & -2-4+2 \\
0-2+0 & 0+8+4
\end{bmatrix}
=
\begin{bmatrix}
0 & 9 \\
5 & -4 \\
-2 & 12
\end{bmatrix}
\]

\[
(AB)^T =
\begin{bmatrix}
0 & 5 & -2 \\
9 & -4 & 12
\end{bmatrix} \tag{1}
\]

RHS = \( B^T A^T \)

\[
B^T =
\begin{bmatrix}
2 & -1 & 0 \\
-1 & 4 & 2
\end{bmatrix},
\quad
A^T =
\begin{bmatrix}
1 & 2 & 0 \\
2 & -1 & 2 \\
1 & 1 & 2
\end{bmatrix}
\]

\[
B^T A^T =
\begin{bmatrix}
2 & -1 & 0 \\
-1 & 4 & 2
\end{bmatrix}
\begin{bmatrix}
1 & 2 & 0 \\
2 & -1 & 2 \\
1 & 1 & 2
\end{bmatrix}
=
\begin{bmatrix}
2(1)+(-1)(2)+0(1) & 2(2)+(-1)(-1)+0(1) & 2(0)+(-1)(2)+0(2) \\
-1(1)+4(2)+2(1) & -1(2)+4(-1)+2(1) & -1(0)+4(2)+2(2)
\end{bmatrix}
=
\begin{bmatrix}
2-2+0 & 4+1+0 & 0-2+0 \\
-1+8+2 & -2-4+2 & 0+8+4
\end{bmatrix}
=
\begin{bmatrix}
0 & 5 & -2 \\
9 & -4 & 12
\end{bmatrix} \tag{2}
\]

From (1) and (2), \( (AB)^T = B^T A^T \). Hence proved.

### Exercise 3.18

1. Find the order of the product matrix \( AB \) if

| (i) | (ii) | (iii) | (iv) | (v) |
|---|---|---|---|---|
| Orders of A | \( 3 \times 3 \) | \( 4 \times 3 \) | \( 4 \times 2 \) | \( 4 \times 5 \) | \( 1 \times 1 \) |
| Orders of B | \( 3 \times 3 \) | \( 3 \times 2 \) | \( 2 \times 2 \) | \( 5 \times 1 \) | \( 1 \times 3 \) |

2. If \( A \) is of order \( p \times q \) and \( B \) is of order \( q \times r \) what is the order of \( AB \) and \( BA \)?

3. \( A \) has ' \( a \) ' rows and ' \( a + 3 \) ' columns. \( B \) has ' \( b \) ' rows and ' \( 17 - b \) ' columns, and if both products \( AB \) and \( BA \) exist, find \( a, b \).

4. If

\[
A = \begin{bmatrix} 2 & 5 \\ 4 & 3 \end{bmatrix},
\quad
B = \begin{bmatrix} 1 & -3 \\ 2 & 5 \end{bmatrix}
\]

find \( AB, BA \) and verify \( AB = BA \)?

5. Given that

\[
A = \begin{bmatrix} 1 & 3 \\ 5 & -1 \end{bmatrix},
\quad
B = \begin{bmatrix} 1 & -1 & 2 \\ 3 & 5 & 2 \end{bmatrix},
\quad
C = \begin{bmatrix} 1 & 3 & 2 \\ -4 & 1 & 3 \end{bmatrix}
\]

verify that \( A(B + C) = AB + AC \).

6. Show that the matrices

\[
A = \begin{bmatrix} 1 & 2 \\ 3 & 1 \end{bmatrix},
\quad
B = \begin{bmatrix} 1 & -2 \\ -3 & 1 \end{bmatrix}
\]

satisfy commutative property \( AB = BA \).

7. If

\[
A = \begin{bmatrix} 1 & 2 \\ 1 & 3 \end{bmatrix},
\quad
B = \begin{bmatrix} 4 & 0 \\ 1 & 5 \end{bmatrix},
\quad
C = \begin{bmatrix} 2 & 0 \\ 1 & 2 \end{bmatrix}
\]

verify that

(i) \( (A - B)C = AC - BC \)

(ii) \( (A - B)^T = A^T - B^T \)

8. If

\[
A = \begin{bmatrix} \cos\theta & 0 \\ 0 & \cos\theta \end{bmatrix},
\quad
B = \begin{bmatrix} \sin\theta & 0 \\ 0 & \sin\theta \end{bmatrix}
\]

then show that \( A + B = \begin{bmatrix} \cos\theta + \sin\theta & 0 \\ 0 & \cos\theta + \sin\theta \end{bmatrix} \)

9. If

\[
A = \begin{bmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{bmatrix}
\]

then verify that \( A^T A = I \).

10. Verify that \( A^2 = I \) when

\[
A = \begin{bmatrix} 5 & -4 \\ 6 & -5 \end{bmatrix}
\]

11. If

\[
A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}
\quad \text{and} \quad
I = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}
\]

show that

\[
A^2 - (a + d)A = (bc - ad)I_2
\]

12. If

\[
A = \begin{bmatrix} 5 & 2 & 9 \\ 1 & 2 & 8 \end{bmatrix},
\quad
B = \begin{bmatrix} 1 & 7 \\ 1 & 2 \\ 2 & 1 \end{bmatrix}
\]

verify that \( (AB)^T = B^T A^T \).

13. If

\[
A = \begin{bmatrix} 3 & 1 \\ -1 & 2 \end{bmatrix}
\]

show that \( A^2 - 5A + 7I_2 = 0 \).