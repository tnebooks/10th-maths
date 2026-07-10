---
title: 'Relations'
weight: 4
---

### 1.4 Relations

Many day-to-day occurrences involve two objects that are connected with each other by some rule of correspondence. We say that the two objects are related under the specified rule. How shall we represent it? Here are some examples,

| Relationship | Expressing using the symbol R | Representation as ordered pair |
|---|---|---|
| New Delhi is the capital of India | New Delhi R India | (New Delhi, India) |
| Line AB is perpendicular to line XY | line AB R line XY | (line AB, line XY) |
| -1 is greater than -5 | -1 R -5 | (-1, -5) |
| ℓ is a line of symmetry for ΔPQR | ℓ R ΔPQR | (ℓ, ΔPQR) |

How are New Delhi and India related? We may expect the response, "New Delhi is the capital of India". But there are several ways in which 'New Delhi' and 'India' are related. Here are some possible answers.

- New Delhi is the capital of India.
- New Delhi is in the northern part of India.
- New Delhi is one of the largest cities of India etc.

So, when we wish to specify a particular relation, providing only one ordered pair may not be enough. We need to specify a set of ordered pairs which satisfy a particular rule of correspondence.

#### Illustration 2

Let us consider the set \( A = \{1,2,3,4\} \) and \( B = \{a,b,c,d\} \).

A relation \( R \) from \( A \) to \( B \) is given by the rule \(\{(x,y) \mid x \in A, y \in B, x \text{ is a factor of } y\}\). Some of the ordered pairs are

\[
R = \{(1,a),(1,b),(1,c),(1,d),(2,b),(2,d),(3,c),(4,d)\}
\]

<center>Fig. 1.3</center>

Observe that the relation \( R \) is a subset of \( A \times B \).

#### Illustration 3

In a school, there are 4 teachers who teach different subjects. The teacher-student relationship can be represented as shown in Fig. 1.4.

<center>Fig. 1.4</center>

#### Note

A relation may be represented algebraically either by the roster method or by the set builder method. An arrow diagram is a visual representation of a relation.

#### Definition

Let \( A \) and \( B \) be any two non-empty sets. A 'relation' \( R \) from \( A \) to \( B \) is a subset of \( A \times B \) satisfying some specified conditions. If \( x \in A \) is related to \( y \in B \) through \( R \), then we write it as \( xRy \). \( xRy \) if and only if \( (x,y) \in R \).

The **domain** of the relation \( R = \{x \in A \mid xRy, \text{ for some } y \in B\} \)

The **co-domain** of the relation \( R \) is \( B \)

The **range** of the relation \( R = \{y \in B \mid xRy, \text{ for some } x \in A\} \)

From these definitions, we note that domain of \( R \subseteq A \), co-domain of \( R = B \) and range of \( R \subseteq B \).

#### Illustration 4

Let us define a relation between heights of corresponding students. (Fig.1.7)

\[
R = \{(\text{heights, students})\}
\]

\[
R = \{(4.5,S_1), (4.5,S_1), (4.7,S_9), (4.9,S_{10}), (5,S_1), (5,S_1), (5,S_8), (5.1,S_1), (5.2,S_2), (5.2,S_1)\}
\]

<center>Fig. 1.7</center>

#### Illustration 5

Let \( A = \{1,2,3,4,5\} \) and \( B = \{\text{Mathi}, \text{Aru}, \text{John}\} \)

A relation R between the above sets \( A \) and \( B \) can be represented by an arrow diagram (Fig. 1.8).

Then, domain of \( R = \{1,2,3,4\} \)

range of \( R = \{\text{Mathi}, \text{Aru}, \text{John}\} = \text{co-domain of R} \).

Note that domain of R is a proper subset of \( A \).

<center>Fig.1.8</center>

#### Illustration 6

Let \( A = \{1,3,5,7\} \) and \( B = \{4,8\} \). If \( R \) is a relation defined by "is less than" from \( A \) to \( B \), then 1R4 ( \( \because 1 \) is less than 4). Similarly, it is observed that 1R8, 3R4, 3R8, 5R8, 7R8

Equivalently \( R = \{(1,4),(1,8),(3,4),(3,8),(5,8),(7,8)\} \)

#### Note

In the above illustration \( A \times B = \{(1,4),(1,8),(3,4),(3,8),(5,4),(5,8),(7,4),(7,8)\} \)

\( R = \{(1,4),(1,8),(3,4),(3,8),(5,8),(7,8)\} \)

We see that \( R \) is a subset of \( A \times B \)

#### Illustration 7

In a particular area of a town, let us consider ten families \( A, B, C, D, E, F, G, H, I \) and \( J \) with two children. Among these, families \( B, F, I \) have two girls; \( D, G, J \) have one boy and one girl; the remaining have two boys. Let us define a relation \( R \) by \( xRy \), where \( x \) denote the number of boys and \( y \) denote the family with \( x \) number of boys. Represent this situation as a relation through ordered pairs and arrow diagram.

Since the domain of the relation \( R \) is concerned about the number of boys, and we are considering families with two children, the domain of \( R \) will consist of three elements given by \( \{0,1,2\} \), where 0, 1, 2 represent the number of boys say no, one, two boys respectively. We note that families with two girls are the ones with no boys. Hence the relation \( R \) is given by

\[
R = \{(0,B),(0,F),(0,I),(1,D),(1,G),(1,J),(2,A),(2,C),(2,E),(2,H)\}
\]

This relation is shown in an arrow diagram (Fig.1.9).

<center>Fig. 1.9</center>

#### Example 1.4

Let \( A = \{3,4,7,8\} \) and \( B = \{1,7,10\} \). Which of the following sets are relations from \( A \) to \( B \):

(i) \( R_1 = \{(3,7),(4,7),(7,10),(8,1)\} \)

(ii) \( R_2 = \{(3,1),(4,12)\} \)

(iii) \( R_3 = \{(3,7),(4,10),(7,7),(7,8),(8,11),(8,7),(8,10)\} \)

#### Solution

\( A \times B = \{(3,1),(3,7),(3,10),(4,1),(4,7),(4,10),(7,1),(7,7),(7,10),(8,1),(8,7),(8,10)\} \)

(i) We note that, \( R_1 \subseteq A \times B \). Thus, \( R_1 \) is a relation from \( A \) to \( B \).

(ii) Here, \( (4,12) \in R_2 \), but \( (4,12) \notin A \times B \). So, \( R_2 \) is not a relation from \( A \) to \( B \).

(iii) Here, \( (7,8) \in R_3 \), but \( (7,8) \notin A \times B \). So, \( R_3 \) is not a relation from \( A \) to \( B \).

#### Example 1.5

The arrow diagram shows (Fig.1.10) a relationship between the sets \( P \) and \( Q \). Write the relation in

(i) Set builder form

(ii) Roster form

(iii) What is the domain and range of R.

#### Solution

(i) Set builder form of \( R = \{(x,y) \mid y = x - 2, x \in P, y \in Q\} \)

(ii) Roster form \( R = \{(5,3),(6,4),(7,5)\} \)

(iii) Domain of \( R = \{5,6,7\} \) and range of \( R = \{3,4,5\} \)

<center>Fig.1.10</center>

#### 'Null relation'

Let us consider the following example. Suppose \( A = \{-3, -2, -1\} \) and \( B = \{1,2,3,4\} \). A relation from \( A \) to \( B \) is defined as \( a - b = 8 \) i.e., there is no pair \( (a,b) \) such that \( a - b = 8 \). Thus R contain no element and so \( R = \phi \).

A relation which contains no element is called a 'Null relation'.

### Exercise 1.2

1. Let \( A = \{1,2,3,7\} \) and \( B = \{3,0,-1,7\} \), which of the following are relation from \( A \) to \( B \)?

(i) \( R_1 = \{(2,1),(7,1)\} \)

(ii) \( R_2 = \{(-1,1)\} \)

(iii) \( R_3 = \{(2,-1),(7,7),(1,3)\} \)

(iv) \( R_4 = \{(7,-1),(0,3),(3,3),(0,7)\} \)

2. Let \( A = \{1,2,3,4,\dots,45\} \) and \( R \) be the relation defined as "square is of a number" on \( A \). Write \( R \) as a subset of \( A \times A \). Also, find the domain and range of \( R \).

3. A Relation R is given by the set \( \{(x,y) \mid y = x + 3, x \in \{0,1,2,3,4,5\}\} \). Determine its domain and range.

4. Represent each of the given relations by (a) an arrow diagram, (b) a graph and (c) a set in roster form, wherever possible.

(i) \( \{(x,y) \mid x = 2y, x \in \{2,3,4,5\}, y \in \{1,2,3,4\}\} \)

(ii) \( \{(x,y) \mid y = x + 3, x, y \text{ are natural numbers } < 10\} \)

5. A company has four categories of employees given by Assistants (A), Clerks (C), Managers (M) and an Executive Officer (E). The company provide 10,000, 25,000, 50,000 and 1,00,000 as salaries to the people who work in the categories respectively. If A1, A2, A3, A4 were Assistants; C1, C2, C3, C4 were Clerks; M1, M2, M3 were Managers and E1, E2 were Executive Officers and the relation R is defined by "is the salary of". Represent the relation through

(a) an arrow diagram

(b) a set of ordered pairs

(c) a graph