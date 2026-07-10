---
title: 'Cartesian Product'
weight: 3
---


### 1.3 Cartesian Product

#### Illustration 1

Let us consider the following two sets.

\( A \) is the set of 3 vegetables and \( B \) is the set of 4 fruits. That is,

\( A = \) {carrot, brinjal, ladies finger} and \( B = \) {apple, orange, grapes, strawberry}

What are the possible ways of choosing a vegetable with a fruit? (Fig.1.2)

| Vegetables (A) | Fruits (B) |
|---|---|
| Carrot (c) | Apple (a) |
| Brinjal (b) | Orange (o) |
| Ladies finger (l) | Grapes (g) |
|  | Strawberry (s) |

<center>Fig. 1.2</center>

We can select them in 12 distinct pairs as given below.

\[
(c,a),(c,o),(c,g),(c,s),(b,a),(b,o),(b,g),(b,s),(l,a),(l,o),(l,g),(l,s)
\]

This collection represents the cartesian product of the set of vegetables and set of fruits.

#### Definition

If A and B are two non-empty sets, then the set of all ordered pairs \( (a,b) \) such that \( a \in A \), \( b \in B \) is called the Cartesian Product of A and B, and is denoted by \( A \times B \). Thus,

\[
A \times B = \{(a,b) \mid a \in A, b \in B\}
\]

(read as A cross B). Also note that \( A \times \phi = \phi \).

### Activity 1

Let \( A = \{x \mid x \in \mathbb{N}, x \leq 4\} \) and \( B = \{y \mid y \in \mathbb{N}, y < 3\} \).

Represent \( A \times B \) and \( B \times A \) in a graph sheet. Can you see the difference between \( A \times B \) and \( B \times A \)?

### Example 1.1

If \( A = \{1,3,5\} \) and \( B = \{2,3\} \) then

(i) find \( A \times B \) and \( B \times A \)

(ii) Is \( A \times B = B \times A \)? If not why?

(iii) Show that \( n(A \times B) = n(B \times A) = n(A) \times n(B) \)

#### Solution

Given that \( A = \{1,3,5\} \) and \( B = \{2,3\} \)

\[
A \times B = \{1,3,5\} \times \{2,3\} = \{(1,2),(1,3),(3,2),(3,3),(5,2),(5,3)\} \tag{1}
\]

\[
B \times A = \{2,3\} \times \{1,3,5\} = \{(2,1),(2,3),(2,5),(3,1),(3,3),(3,5)\} \tag{2}
\]

(ii) From (1) and (2) we conclude that \( A \times B \neq B \times A \) as \( (1,2) \neq (2,1) \) and \( (1,3) \neq (3,1) \), etc.

(iii) \( n(A) = 3 \); \( n(B) = 2 \)

From (1) and (2) we observe that, \( n(A \times B) = n(B \times A) = 6 \)

we see that, \( n(A) \times n(B) = 3 \times 2 = 6 \) and \( n(B) \times n(A) = 2 \times 3 = 6 \)

Hence, \( n(A \times B) = n(B \times A) = n(A) \times n(B) = 6 \)

Thus, \( n(A \times B) = n(B \times A) = n(A) \times n(B) \)

### Example 1.2

If \( A \times B = \{(3,2),(3,4),(5,2),(5,4)\} \) then find \( A \) and \( B \)

#### Solution

\( A \times B = \{(3,2),(3,4),(5,2),(5,4)\} \)

We have \( A = \{ \) set of all first coordinates of elements of \( A \times B \} \)

\[
\therefore A = \{3,5\}
\]

\( B = \{ \) set of all second coordinates of elements of \( A \times B \} \)

\[
\therefore B = \{2,4\}
\]

Thus \( A = \{3,5\} \) and \( B = \{2,4\} \)

### Example 1.3

Let \( A = \{x \in \mathbb{N} \mid 1 < x < 4\} \), \( B = \{x \in \mathbb{W} \mid 0 \leq x < 2\} \) and \( C = \{x \in \mathbb{N} \mid x < 3\} \). Then verify that

\[
A \times (B \cup C) = (A \times B) \cup (A \times C)
\]

\[
A \times (B \cap C) = (A \times B) \cap (A \times C)
\]

#### Solution

\( A = \{x \in \mathbb{N} \mid 1 < x < 4\} = \{2,3\} \)

\( B = \{x \in \mathbb{W} \mid 0 \leq x < 2\} = \{0,1\} \)

\( C = \{x \in \mathbb{N} \mid x < 3\} = \{1,2\} \)

\[
A \times (B \cup C) = (A \times B) \cup (A \times C)
\]

\[
B \cup C = \{0,1\} \cup \{1,2\} = \{0,1,2\}
\]

\[
A \times (B \cup C) = \{2,3\} \times \{0,1,2\} = \{(2,0),(2,1),(2,2),(3,0),(3,1),(3,2)\}
\]

\[
A \times B = \{2,3\} \times \{0,1\} = \{(2,0),(2,1),(3,0),(3,1)\}
\]

\[
A \times C = \{2,3\} \times \{1,2\} = \{(2,1),(2,2),(3,1),(3,2)\}
\]

\[
(A \times B) \cup (A \times C) = \{(2,0),(2,1),(3,0),(3,1),(2,2),(3,2)\}
\]

Thus, \( A \times (B \cup C) = (A \times B) \cup (A \times C) \)

Similarly, \( A \times (B \cap C) = (A \times B) \cap (A \times C) \) can be verified.

### Exercise 1.1

1. Find \( A \times B \), \( A \times A \) and \( B \times A \)

(i) \( A = \{2, -2, 3\} \) and \( B = \{1, -4\} \)

(ii) \( A = B = \{p, q\} \)

(iii) \( A = \{m, n\} \); \( B = \phi \)

2. Let \( A = \{1,2,3\} \) and \( B = \{x \mid x \text{ is a prime number less than 10}\} \). Find \( A \times B \) and \( B \times A \)

3. If \( B \times A = \{(-2,3),(-2,4),(0,3),(0,4),(3,3),(3,4)\} \) find \( A \) and \( B \)

4. If \( A = \{5,6\} \), \( B = \{4,5,6\} \), \( C = \{5,6,7\} \). Show that \( A \times A = (B \times B) \cap (C \times C) \)

5. Given \( A = \{1,2,3\} \), \( B = \{2,3,5\} \), \( C = \{3,4\} \) and \( D = \{1,3,5\} \), check if
\[
(A \cap C) \times (B \cap D) = (A \times B) \cap (C \times D)
\]
is true?

6. Let \( A = \{x \in W \mid x < 2\} \), \( B = \{x \in N \mid 1 < x \leq 4\} \) and \( C = \{3,5\} \). Verify that

(i) \( A \times (B \cup C) = (A \times B) \cup (A \times C) \)

(ii) \( A \times (B \cap C) = (A \times B) \cap (A \times C) \)

(iii) \( (A \cup B) \times C = (A \times C) \cup (B \times C) \)

7. Let \( A = \) The set of all natural numbers less than 8,
\( B = \) The set of all prime numbers less than 8,
\( C = \) The set of even prime number.
Verify that

(i) \( (A \cap B) \times C = (A \times C) \cap (B \times C) \)

(ii) \( A \times (B - C) = (A \times B) - (A \times C) \)
---


