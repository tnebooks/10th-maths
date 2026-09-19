---
title: 'relations-and-functions'
weight: 1
---

# Chapter 1

## RELATIONS AND FUNCTIONS

"Mathematicians do not study objects, but relations between objects...Content to them is irrelevant: they are interested in form only" - Henri Poincare

Gottfried Wilhelm Leibniz (also known as von Leibniz) was a prominent German mathematician, philosopher, physicist and inventor. He wrote extensively on 26 topics covering wide range of subjects among which were Geology, Medicine, Biology, Epidemiology, Paleontology, Psychology, Engineering, Philology, Sociology, Ethics, History, Politics, Law and Music Theory.

In a manuscript Leibniz used the word "function" to mean any quantity varying from point to point of a curve. Leibniz provided the foundations of Formal Logic and Boolean Algebra, which are fundamental for modern day computers. For all his remarkable discoveries and contributions in various fields, Leibniz is hailed as "The Father of Applied Sciences".

<center>Gottfried Wilhelm Leibniz (1646-1716)</center>

---

## Learning Outcomes

To define and determine cartesian product of sets. To define a relation as a subset of cartesian product of sets. To understand function as a special relation. To represent a function through an arrow diagram, a set of ordered pairs, a table, a rule or a graph. To classify functions as one-one, many-one, onto, into and bijection. To study combination of functions through composition operation. To understand the graphs of linear, quadratic, cubic and reciprocal functions.

---

---

<!-- Chapter 1 textbook content reconstructed from the supplied PDF. Image assets are placeholders for now. -->

## 1.1 Introduction

The notion of sets provides the stimulus for learning higher concepts in mathematics. A set is a collection of well-defined objects. This means that a set is merely a collection of something which we may recognize. In this chapter, we try to extend the concept of sets in two forms called Relations and Functions. For doing this, we need to first know about cartesian products that can be defined between two non-empty sets.

It is quite interesting to note that most of the day-to-day situations can be represented mathematically either through a relation or a function. For example, the distance travelled by a vehicle in given time can be represented as a function. The price of a commodity can be expressed as a function in terms of its demand. The area of polygons and volume

Relations and Functions of common objects like circle, right circular cone, right circular cylinder, sphere can be expressed as a function with one or more variables.

In class IX, we had studied the concept of sets. We have also seen how to form new sets from the given sets by taking union, intersection and complementation.

Now we are about to study a new set called 'cartesian product' for the given sets A and B .

## 1.2 Ordered Pair

Observe the seating plan in an auditorium (Fig.1.1).

> **[IMAGE PLACEHOLDER — Fig. 1.1: Seating plan in an auditorium]**
 To help orderly occupation of seats, tokens with numbers such as (1,5), (7,16), (3,4), (10,12) etc. are issued. The person who gets (4,10) will go to row 4 and occupy the 10 th seat. Thus the first number denotes the row and the second number, the seat. Which seat will the visitor with token (5,9) occupy? Can he go to 9 th row and take the 5 th seat? Do (9,5) and (5,9) refer to the same location? No,

Fig. 1.1

certainly! What can you say about the tokens (2,3), (6,3) and (10,3)?

This is one example where a pair of numbers, written in a particular order, precisely indicates a location. Such a number pair is called an ordered pair of numbers. This notion is skillfully used to mathematize the concept of a 'Relation' .

## 1.3 Cartesian Product

## Illustration 1

Let us consider the following two sets.

A is the set of 3 vegetables and B is the set of 4 fruits. That is,

A = {carrot, brinjal, ladies finger} and B = {apple, orange, grapes, strawberry} What are the possible ways of choosing a vegetable with a fruit? (Fig.1.2)

| Vegetables (A) | Fruits (B) |
|---------------------|------------------|
| Carrot (c) | Apple (a) |
| Brinjal (b) | Orange (o) |
| Ladies finger (l) | Grapes (g) |
| | Strawberry (s) |

> **[IMAGE PLACEHOLDER — Fig. 1.2: Cartesian product of vegetables and fruits]**

We can select them in 12 distinct pairs as given below.

(c , a), (c , o), (c , g), (c , s), (b , a), (b , o), (b , g), (b , s), (l , a), (l , o), (l , g), (l , s)

This collection represents the cartesian product of the set of vegetables and set of fruits.

## Definition

If A and B are two non-empty sets, then the set of all ordered pairs (a , b) such that a \in A, b \in B is called the Cartesian Product of A and B, and is denoted by A \times B . Thus, A \times B = ∈ ∈ \{(a,b) \mid a \in A, b \in B\} (read as A cross B). Also note that A \times \emptyset = \emptyset

## Note

- A × B is the set of all possible ordered pairs between the elements of A and B such that the first coordinate is an element of A and the second coordinate is an element of B .
- B × A is the set of all possible ordered pairs between the elements of A and B such that the first coordinate is an element of B and the second coordinate is an element of A .
- In general (a , b) \neq (b , a), in particular, if a = b , then (a , b) = (b , a).
- The 'cartesian product' is also referred as 'cross product' .

## Illustration 2

Let A = {1, 2, 3} and B = {a, b}. Write A \times B and B \times A ?

A \times B = {1,2,3}×{a , b} = {(,),(,),(,),(,),(,),(,)} 1 1 2 2 3 3 a b a b a b (as shown in Fig.1.3)

> **[IMAGE PLACEHOLDER — Fig. 1.3: Arrow diagram of Cartesian Product]**

B \times A = {a , b} × {1,2,3} = {(a ,1), (a ,2), (a ,3),(b ,1), (b ,2), (b ,3)} (as shown in Fig.1.3)

Fig. 1.3

## Recall of standard infinite sets

Natural Numbers \mathbb{N} = … {} , , , 1 2 3 4 ; Whole Numbers W = {0,1,2,3, ...};

= p q p q q | , , ∈ \neq ⎧ ⎨ ⎪ ⎪ ⎪ ⎫ ⎬ ⎪ ⎪ ⎪ \mathbb{Z} 0

Integers \mathbb{Z} ={..., -2,-1,0,1,2, ...} ; Rational Numbers \mathbb{Q} ⎩ ⎪ ⎭ ⎪ ;

Real Numbers \mathbb{R} = \mathbb{Q} \mathbb{Q} ∪ ′ , where ¢ \mathbb{Q} is the set of all irrational numbers.

## Illustration 3

For example, let A be the set of numbers in the interval [3, 5] and B be the set of numbers in the interval [2,3]. Then the Cartesian product A \times B corresponds to the rectangular region shown in the Fig. 1.4. It consists of all points (x , y) within the region.

> **[IMAGE PLACEHOLDER — Fig. 1.4: Geometrical representation of Cartesian product in the coordinate plane]**

## Progress Check

1. For any two non-empty sets A and B, A \times B is called as \_\_\_\_\_.
2. If n A B () × = 20 and n A () = 5 then n B () is \_\_\_\_\_.
3. If A = - {, 1 1} and B = - {,} 1 1 then geometrically describe the set of points of A \times B .
4. If A, B are the line segments given by the intervals (-4, 3) and (-2, 3) respectively, represent the cartesian product of A and B.

Fig. 1.4

## Thinking Corner

When will A \times B be equal to B \times A ?

## Note

- In general A B B \times A \neq × , but n A B n B A () () × = ×
- A \times B = \emptyset if and only if A = \emptyset or B = \emptyset
- If n A p () = and n B q () = then n A B pq () × =

## Note

The set of all points in the cartesian plane can be viewed as the set of all ordered pairs (x , y) where x , y are real numbers. In fact, \mathbb{R} \times \mathbb{R} is the set of all points which we call as the cartesian plane.

## Activity 1

Let A x x x = ∈ \le {,} | \mathbb{N} 4 , B y y y = ∈ < {|} , \mathbb{N} 3

Represent A \times B and B \times A in a graph sheet. Can you see the difference between A \times B and B \times A ?

Example 1.1 If A = {1,3,5} and B = {2,3} then (i) find A \times B and B \times A .

(ii) Is A B B \times A = × ? If not why? (iii) Show that n(A \\times B) = n(B \\times A) = n(A)× n(B)

Solution Given that A = {1,3,5} and B = {2,3}

(i) A × B = {1,3,5} × {2,3} = {(1,2), (1,3), (3,2), (3,3), (5,2), (5,3)} ...(1) B \times A = {2,3} × {1,3,5} = {(2,1), (2,3), (2,5), (3,1), (3,3), (3,5)} ...(2)

- (ii) From (1) and (2) we conclude that A B B \times A \neq × as (,) (,) 1 2 2 1 \neq and (,) (,) 1 3 3 1 \neq , etc.

(iii) n(A)=3; n(B) = 2.

From (1) and (2) we observe that, n(A \\times B) = n(B \\times A) = 6;

we see that, n(A) × n(B) = 3 × 2 = 6 and n(B) × n(A) = 2 × 3 = 6

Hence, n(A \\times B) = n(B \\times A) = n(A) × n(B) = 6.

Thus, n(A \\times B) = n(B \\times A) = n(A) × n (B

).

Example 1.2 If A × B = {(3,2), (3,4), (5,2), (5,4)} then find A and B .

Solution A × B = {(3,2), (3,4), (5,2), (5,4)}

We have A = {set of all first coordinates of elements of A \times B}. ∴ A = {3,5}

B = {set of all second coordinates of elements of A \times B}. ∴ B = {2,4}

Thus A = {3,5} and B = {2,4}.

Example 1.3 Let A x x = ∈ < < {} | \mathbb{N} 1 4 , B x = ∈ {W |} 0 2 \le < x and C x x = ∈ < {} | \mathbb{N} 3 Then verify that

.

(i) () () () A B C A B A C # , # , # = (ii) () () () A B C A B A C # + # + # =

Solution A x x = ∈ < < = {} {, |} \mathbb{N} 1 4 2 3 , B x = ∈ {W |} 0 2 \le < x = {,} 0 1 , C x x = ∈ < {} | \mathbb{N} 3 ={1,2} (i) A B C × ∪ () = () () A B A C # , # B C \cup = ∪ = {,} {,} {, ,} 0 1 1 2 0 1 2 A B C × ∪ () = {,} {, ,} 2 3 0 1 2 # = {(,), (,), (,), (,), (,), (,)} 2 0 2 1 2 2 3 0 3 1 3 2 = ...(1) A \times B = {,} {,} 2 3 0 1 # = {(2,0),(2,1),(3,0),(3,1)} A C \times = {,} {,} {(,), (,), (,), (,)} 2 3 1 2 2 1 2 2 3 1 3 2 # =

() () A B A C × ∪ × {(,), (,), (,), (,)} {(,), (,), (,), (,)} 2 0 2 1 3 0 3 1 2 1 2 2 3 1 3 2 , = {(,), (,), (,), (,), (,), (,)} 2 0 2 1 2 2 3 0 3 1 3 2 = ...(2)

From (1) and (2), A B C A B A C × ∪ = × ∪ × () () () is verified.

(ii) A B C × ∩ () = × ∩ × () () A B A C B C \cap = ∩ = {,} {,} {} 0 1 1 2 1 A B C × ∩ () = × = {,} {} {(,),(,)} 2 3 1 2 1 3 1 = × = {,} {} {(,),(,)} 2 3 1 2 1 3 1 ... (3) A \times B = × = {,} {,} {(,),(,),(,),(,)} 2 3 0 1 2 0 2 1 3 0 3 1 A C \times = × {,} {,} 2 3 1 2 = {(,),(,),(,),(,)} 2 1 2 2 3 1 3 2 () () A B A C × ∩ × = ∩ {(,),(,),(,),(,)} {(,),(,),(,),(,)} 2 0 2 1 3 0 3 1 2 1 2 2 3 1 3 2 = {(,),(,)} 2 1 3 1 ... (4)

From (3) and (4), A B C A B A C × ∩ = × ∩ × () () () is verified.

The above two verified properties are called distributive property of cartesian product over union and intersection respectively. In fact, for any three sets A , B , C we have (i) A B C × ∪ () = × ∪ × () () A B A C (ii) A B C C × ∩ = × ∩ × () (A B) (A) .

## 1.3.1 Cartesian Product of three Sets

If (A), (B), (C) are three non-empty sets then the cartesian product of three sets is the set of all possible ordered triplets given by

$$
A \times B \times C = \{(a,b,c) \mid a \in A, b \in B, c \in C\}.
$$

### Illustration for Geometrical understanding of Cartesian product of two and three sets

Let
[
A={0,1},\quad B={0,1},\quad C={0,1}.
]

$$
A \times B=\{(0,0),(0,1),(1,0),(1,1)\}.
$$

Representing (A \times B) in the (XY)-plane gives the picture shown in Fig. 1.5.

> **[IMAGE PLACEHOLDER — Fig. 1.5: Cartesian coordinates of two sets]**

$$
(A \times B) \times C
=\{(0,0),(0,1),(1,0),(1,1)\}\times\{0,1\}
$$

$$
=\{(0,0,0),(0,0,1),(0,1,0),(0,1,1),
(1,0,0),(1,0,1),(1,1,0),(1,1,1)\}.
$$

Representing (A \times B \times C) in the (XYZ)-space gives the picture shown in Fig. 1.6.

> **[IMAGE PLACEHOLDER — Fig. 1.6: Geometrical representation of Cartesian product of three sets as a 3D box]**

Thus, (A \times B) represents vertices of a square in two dimensions and (A \times B \times C) represents vertices of a cube in three dimensions.

In general, the Cartesian product of two non-empty sets provides a shape in two dimensions and similarly the Cartesian product of three non-empty sets provides an object in three dimensions.

## Exercise 1.1

1. Find A \times B , A \times A and B \times A

(i) A = - {, ,} 2 2 3 and B = - {,} 1 4 (ii) A B p q = = {,} (iii) A m n = {,} ; B = \emptyset

2. Let A = {1,2,3} and B = {x x | is a prime number less than 10}. Find A \times B and B \times A .
3. If B \times A = - {(,),(,),(,),(,),(,),(,)} 2 3 2 4 0 3 0 4 3 3 3 4 find A and B .
4. If A = {} , 5 6 , B = {,} , 4 5 6 , C = {} , , 5 6 7 , Show that A A B B C C × = × ∩ × () () .
5. Given A={1,2,3}, B = {2,3,5}, C = {3,4} and D = {1,3,5}, check if () () () () A C B D A B C D ∩ × ∩ = × ∩ × is true?
6. Let A x = ∈ {W |} x < 2 , B x = ∈ {\mathbb{N} N | 1 4 < \le x} and C = {, 3 5} . Verify that (i) A B C × ∪ () = × ∪ × () () A B A C (ii) A B C A B A C × ∩ = × ∩ × () () () (iii) () () () A B C A C B C ∪ × = × ∪ ×
7. Let A = The set of all natural numbers less than 8, B = The set of all prime numbers less than 8, C = The set of even prime number. Verify that

(i) () () () A B C A C B C ∩ × = × ∩ × (ii) A B C A B A C × - = × - × () () ()

## 1.4 Relations

Many day-to-day occurrences involve two objects that are connected with each other by some rule of correspondence. We say that the two objects are related under the specified rule. How shall we represent it? Here are some examples,

| Relationship | Expressing using the symbol R | Representation as ordered pair |
|-------------------------------------|---------------------------------|----------------------------------|
| New Delhi is the capital of India | New Delhi R India | (New Delhi, India) |

> **[IMAGE PLACEHOLDER — Fig. 1.7: Relation between countries and their capitals]**

| Line AB is perpendicular to line XY | line AB R line XY | (line AB , line XY) |
| -1 is greater than -5 | -1 R -5 | (-1, -5) |
| ℓ is a line of symmetry for D PQR | ℓ R D PQR | (ℓ, D PQR) |

How are New Delhi and India related? We may expect the response, 'New Delhi is the capital of India' . But there are several ways in which 'New Delhi' and 'India' are related. Here are some possible answers.

- � New Delhi is the capital of India.
- � New Delhi is in the northern part of India.
- �
- New Delhi is one of the largest cities of India etc.,

So, when we wish to specify a particular relation, providing only one ordered pair

(New Delhi, India) it may not be practically helpful. If we ask the relation in the following set of ordered pairs,

{(New Delhi, India), (Washington, USA), (Beijing, China), (London, U.K.), (Kathmandu, Nepal)} then specifying the relation is easy.

## Progress Check

Let A = {1, 2, 3, 4} and B = {a, b, c}.

| 1. | Which of the following are relations from A to B? | 2. Which of the following are relations from B to A ? |
|------|-----------------------------------------------------|---------------------------------------------------------|
| | (i) {(1, b), (1, c), (3, a), (4, b)} | (i) {(c, a), (c, b), (c, 1)} |
| | (ii) {(1, a), (b, 4), (c, 3)} | (ii) {(c, 1), (c, 2), (c, 3), (c, 4)} |
| | (iii) {(1, a), (a, 1), (2, b), (b, 2)} | (iii) {(a, 4), (b, 3), (c, 2)} |

## Illustration 4

| Students in a class | S 1 | S 2 | S 3 | S 4 | S 5 | S 6 | S 7 | S 8 | S 9 | S 10 |
|-----------------------|-------|-------|-------|-------|-------|-------|-------|-------|-------|--------|
| Heights (in feet) | 4.5 | 5.2 | 5 | 4.5 | 5 | 5.1 | 5.2 | 5 | 4.7 | 4.9 |

Let us define a relation between heights of corresponding students. (Fig.1.7)

> **[IMAGE PLACEHOLDER — Fig. 1.8: Relation between students and their heights]**

R = {(heights, students)} R = () () () () () () (. , , . , , . , , . , , , , , , 4 5 4 5 4 7 4 9 5 5 1 4 9 10 3 5 S S S S S S 5 8 ,), S {() () () . , , . , , . , 5 1 5 2 5 2 6 2 7 S S S}

## Definition

Let A and B be any two non-empty sets. A 'relation' R from A to B is a subset of A \times B satisfying some specified conditions. If x A \in is related to y B \in through R , then we write it as x R y . x R y if and only if (,) x y \in R .

The domain of the relation R = {| ,} x A x y y B \in \in R for some

The co-domain of the relation R is B

The range of the relation R = {| ,} y B x y x A \in \in R for some

From these definitions, we note that domain of R \subseteq A , co-domain of R = B and range of R \subseteq B .

## Illustration 5

Let A = {1,2,3,4,5} and B = {Mathi, Arul, John}

A relation R between the above sets A and B can be represented by an arrow diagram (Fig. 1.8).

Then, domain of R = {1,2,3,4}

range of R = {Mathi, Arul, John} = co-domain of R .

Note that domain of R is a proper subset of A .

## Activity 2

Let A and B be the set of lines in xy -plane such that A consists of lines parallel to X -axis. For x A \in , y B \in , let R be a relation from A to B defined by x y R if x is perpendicular to y . Find the elements of B using a graph sheet.

## Illustration 6

Let A = {1,3,5,7} and B = {4,8}. If R is a relation defined by 'is less than' from A to B , then 1R4 (1 is less than 4). Similarly, it is observed that 1R8, 3R4, 3R8, 5R8, 7R8

Equivalently R= {(1,4), (1,8), (3,4), (3,8), (5,8), (7,8)}

 In the above illustration A × B = {(1,4), (1,8), (3,4), (3,8), (5,4), (5,8), (7,4),(7,8)} R = {(1,4), (1,8), (3,4), (3,8), (5,8), (7,8)} We see that R is a subset of A \times B .

## Illustration 7

In a particular area of a town, let us consider ten families A , B , C , D , E , F , G , H , I and J with two children. Among these, families B , F , I have two girls; D , G , J have one boy and one girl; the remaining have two boys. Let us define a relation R by x R y , where x denote the number of boys and y denote the family with x number of boys. Represent this situation as a relation through ordered pairs and arrow diagram.

Since the domain of the relation R is concerned about the number of boys, and we are considering families with two

children, the domain of R will consist of three elements given by {0,1,2}, where 0, 1, 2 represent the number of boys say no, one, two boys respectively. We note that families with two girls are the ones with no boys. Hence the relation R is given by

R = {(,),(,),(,),(,),(,),(,),(,),(,),(,),(0 0 0 1 1 1 2 2 2 B F I D G J A C E 2,)} H

This relation is shown in an arrow diagram (Fig.1.9).

Example 1.4 Let A = {3,4,7,8} and B = {1,7,10}. Which of the following sets are relations from A to B ?

- (i) R 1 ={(3,7), (4,7), (7,10), (8,1)} (ii) R 2 = {(3,1), (4,12)}
- (iii) R 3 = {(3,7), (4,10), (7,7), (7,8), (8,11), (8,7), (8,10)}

Solution A \times B = {(3,1), (3,7), (3,10), (4,1), (4,7), (4,10), (7,1), (7,7), (7,10), (8,1), (8,7), (8,10)}

- (i) We note that, R 1 ⊆ × A B . Thus, R 1 is a relation from A to B .
- (ii) Here, (, 4 12) 2 \in R , but (, 4 12) ∉ × A B . So, R 2 is not a relation from A to B .
- (iii) Here, (, 7 8) 3 \in R , but (, 7 8) ∉ × A B . So, R 3 is not a relation from A to B .

## Note

- A relation may be represented algebraically either by the roster method or by the set builder method.
- An arrow diagram is a visual representation of a relation.

Example 1.5 The arrow diagram shows (Fig.1.10) a relationship between the sets P and

> **[IMAGE PLACEHOLDER — Fig. 1.10: Arrow diagram for relationship between sets P and Q]**
 Q . Write the relation in (i) Set builder form (ii) Roster form (iii) What is the domain and range of R.

## Solution

- (i) Set builder form of R = = - ∈ ∈ {} (,) | , , x y y x x P y Q 2
- (ii) Roster form R = {(,),(,),(,)} 5 3 6 4 7 5
- (iii) Domain of R	= {5,6,7} and range of R = {} 3 4 5 , ,

Fig. 1.10

If n A p () = , n B q () = , then the total number of relations that exist from A to B is 2 pq .

## ' Null relation '

Let us consider the following example. Suppose A = {-3,-2,-1} and B = {1,2,3,4}. A relation from A to B is defined as a b - = 8 i.e., there is no pair(a , b) such that a b - = 8 . Thus R contain no element and so R = \emptyset .

A relation which contains no element is called a 'Null relation' .

## Exercise 1.2

1. Let A = {1,2,3,7} and B = {3,0,-1,7}, which of the following are relation from A to B ?
2. (i) R 1 = {(2,1), (7,1)}
3. (ii) R 2 = {(-1,1)}
4. (iii) R 3 = {(2,-1), (7,7), (1,3)}
5. (iv) R 4 = {(7,-1), (0,3), (3,3), (0,7)}
2. Let A ={1,2,3,4,...,45} and R be the relation defined as 'square is of a number' on A . Write R as a subset of A \times A . Also, find the domain and range of R.
3. A Relation R is given by the set (,) / , {, , , , ,} x y y x x = + ∈ {} 3 0 1 2 3 4 5 . Determine its domain and range.
4. Represent each of the given relations by (a) an arrow diagram, (b) a graph and (c) a set in roster form, wherever possible.
9. (i) {(x , y)| x = 2 y , x ∈ {2,3,4,5}, y ∈ {1,2,3,4}}
10. (ii) {(x , y)| y = x +3, x , y are natural numbers < 10}
5. A company has four categories of employees given by Assistants (A), Clerks (C), Managers (M) and an Executive Officer (E). The company provide ₹10,000, ₹25,000, ₹50,000 and ₹1,00,000 as salaries to the people who work in the categories

A , C , M and E respectively. If A 1 , A 2 , A 3 , A 4 and A 5 were Assistants; C 1 , C 2 , C 3 , C 4 were Clerks; M 1 , M 2 , M 3 were managers and E 1 , E 2 were Executive officers and if the relation R is defined by x R y , where x is the salary given to person y , express the relation R through an ordered pair and an arrow diagram.

## 1.5 Functions

Among several relations that exist between two non-empty sets, some special relations are important for further exploration. Such relations are called 'Functions' .

## Illustration 8

A company has 5 employees in different categories. If we consider their salary distribution for a month as shown by arrow diagram in Fig.1.11, we see that there is only one salary associated for every employee of the company.

Here are various real life situations illustrating some special relations:

1. Consider the set A of all of your classmates; corresponding to each student, there is only one age.
2. You go to a shop to buy a book. If you take out a book, there is only one price corresponding to it; it does not have two prices corresponding to it. (of course, many books may have the same price).
3. You are aware of Boyle's law. Corresponding to a given value of pressure P , there is only one value of volume V .
4. In Economics, the quantity demanded can be expressed as Q P = - 360 4 , where P is the price of the commodity. We see that for each value of P , there is only one value of Q . Thus the quantity demanded Q depend on the price P of the commodity.

We often come across certain relations, in which, for each element of a set A , there is only one corresponding element of a set B . Such relations are called functions. We usually use the symbol \emptyset to denote a functional relation.

## Definition

A relation \emptyset between two non-empty sets X and Y is called a function from X to Y if, for each x X \in there exists only one y Y \in such that (,) x y \emptyset \in .

That is, \emptyset ={(x , y)| for all x ∈ X , y ∈ Y}.

A function \emptyset from X to Y is written as \emptyset X Y : \\to .

Comparing the definitions of relation and function, we see that every function is a relation. Thus, functions are subsets of relations and relations are subsets of cartesian product. (Fig.1.12(a))

If \emptyset X Y : \\to is a function then

- The set X is called the domain of the function \emptyset and the set Y is called its co-domain.
- If \emptyset (a) = b , then b is called 'image' of a under \emptyset and a is called a 'pre-image' of b .
- The set of all images of the elements of X under \emptyset is called the 'range' of \emptyset .
- \emptyset X Y : \\to is a function only if
- (i) every element in the domain of \emptyset has an image.
- (ii) the image is unique.
- If A and B are finite sets such that n A p () = , n B q () = then the total number of functions that exist from A to B is q p .
- In this chapter we always consider \emptyset to be a real valued function.
- Describing domain of a function
- (i) Let \emptyset x x () = + 1 1 . If x = -1 then \emptyset (-1) is not defined. Hence \emptyset is defined for all real numbers except at x =- 1. So, domain of \emptyset is \mathbb{R} - {1} .
- (ii) Let \emptyset x x x () = - + 1 5 6 2 ; If x = 2 3 , then \emptyset (2) and \emptyset (3) are not defined. Hence \emptyset is

defined for all real numbers except at x = 2 and 3. So, domain of \emptyset = - \mathbb{R} {, 2 3}.

## Progress Check

1. Relations are subsets of \_\_\_\_. Functions are subsets of \_\_\_\_.
2. True or False: All the elements of a relation should have images.
3. True or False: All the elements of a function should have images.
4. True or False: If R : A B \\to is a relation then the domain of R = A .
5. If \emptyset : \mathbb{N} \mathbb{N} \\to is defined as \emptyset x x () = 2 the image of 1 and 2 are \_\_\_\_ and \_\_\_\_.
6. What is the difference between relation and function?
7. Let A and B be two non-empty finite sets. Then which one among the following two collection is large?
8. (i) The number of relations between A and B .
9. (ii) The number of functions between A and B .

A function is also called as a mapping or transformation.

## Illustration 9 - Testing for functions

## Representation by Arrow diagram

This represents a function. Each input corresponds to a single output.

Fig. 1.13(a)

This represents a function. Each input corresponds to a single output.

Fig. 1.13(b)

This is not a function. One of the input b is associated with two outputs.

Fig. 1.13(c)

Functions play very important role in the understanding of higher ideas in mathematics. They are basic tools to convert from one form to another form. In this sense, functions are widely applied in Engineering Sciences.

## Note

The range of a function is a subset of its co-domain.

Example 1.6 Let X = {} 1 2 3 4 , , , and Y = {} 2 4 6 8 10 , , , , and R = {(1,2),(2,4),(3,6),(4,8)} . Show that R is a function and find its domain, co-domain and range? Solution Pictorial representation of R is given in Fig.1.14. From the diagram, we see that for each x X \in , there exists only one y Y \in . Thus all elements in X have only one image in Y . Therefore R is a function. Domain X = {1,2,3,4}; Co-domain Y = {2,4,6,8,10}; Range of \emptyset = {2,4,6,8}. 1 2 3 4 Fig. 1.14 2 4 6 8 10 X R Y

Example 1.7 A relation \emptyset : X → Y is defined by \emptyset x x () = - 2 2 where, X = - {, , ,} 2 1 0 3 and Y = R. (i) List the elements of \emptyset (ii) Is \emptyset a function?

Solution

f

x

x

(

)

-

=

2

2

where

X

= -

-

{

,

,

,

}

2

1 0 3

(i) \emptyset () - 2 = - = () - 2 2 2 2 ; \emptyset () - 1 = - =- () - 1 2 1 2 \emptyset (0) = =- () - 0 2 2 2 ; \emptyset (3) = = () - 3 2 7 2 ∴ \emptyset = - - {(,),(,) , ,} ,(),() 2 2 1 1 0 2 3 7

- (ii) We note that each element in the domain of \emptyset has a unique image. Therefore, \emptyset is a function.

## Thinking Corner

Is the relation representing the association between planets and their respective moons a function?

Example 1.8 If X = {-5,1,3,4} and Y = {a , b , c}, then which of the following relations are functions from X to Y

> **[IMAGE PLACEHOLDER — Fig. 1.15: Arrow diagrams for relations R1, R2, and R3]**
 ?

(i) R 1 = {(-5, a), (1, a), (3, b)} (ii) R 2 = {(-5, b), (1, b), (3, a),(4, c)}

(iii) R 3 = {(-5, a), (1, a), (3, b),(4, c),(1, b)}

## Solution

- (i) R 1 = {(-5, a), (1, a), (3, b)} We may represent the relation R 1 in an arrow diagram (Fig.1.15(a)).

R 1 is not a function as 4 \in X does not have an image in Y .

(ii) R 2 = {(-5, b), (1, b), (3, a),(4, c)} Arrow diagram of R 2 is shown in Fig.1.15(b).

R 2 is a function as each element of X has an unique image in Y .

- (iii) R 3 = {(-5, a), (1, a), (3, b),(4, c),(1, b)}

Representing R 3 in an arrow diagram (Fig.1.15(c)).

R 3 is not a function as 1 \in X has two images a Y \in and b Y \in .

Note that the image of an element should always be unique.

Example 1.9 Given \emptyset x x x () - = 2 2 ,

find (i) \emptyset (1) (ii) \emptyset (x +1) (iii) \emptyset (x) + \emptyset (1)

Solution (i) x = 1, we get

f (1) = = = 2 1 1 2 1 1 2 () - () -

- (ii) x = x +1, we get

f (x +1) = + + 2 1 1 2 () - () x x = + + + - () 2 2 2 1 2 x x x =- + x 2 1

(iii) \emptyset (x) + \emptyset (1) = + =- + + () - 2 1 2 1 2 2 x x x x

[Note that \emptyset \emptyset \emptyset x x () () () + \neq + 1 1 . In general \emptyset a b () + is not equal to \emptyset (a)+ \emptyset (b)]

1. Let \emptyset x y x y N y x = ∈ = {(,) | ,} and 2 be a relation on \mathbb{N}. Find the domain, co-domain and range. Is this relation a function?
2. Let X = {3, 4, 6, 8}. Determine whether the relation R x \emptyset x x X \emptyset x x = ∈ = + {(, ()) | , ()} 2 1 is a function from X to N ?

Fig. 1.15(c)

3. Given the function \emptyset x x x : → - + 2 5 6 , evaluate
2. (i) \emptyset () - 1 (ii)
3. \emptyset a () 2
4. (iii) \emptyset (2) (iv) \emptyset x - () 1
4. A graph representing the function \emptyset (x) is given in Fig.1.16 it is clear that \emptyset (9) = 2.

> **[IMAGE PLACEHOLDER — Fig. 1.16: Graph representing the function f(x)]**

6. (i) Find the following values of the function
7. (a) \emptyset (0) (b) \emptyset (7) (c) \emptyset (2) (d) \emptyset (10)
8. (ii) For what value of x is \emptyset (x) = 1?
9. (iii) Describe the following (i) Domain (ii) Range.
10. (iv) What is the image of 6 under \emptyset ?
5. Let \emptyset (x) = 2 x +5. If x \neq 0 then find \emptyset x \emptyset x () () + - 2 2 .
6. A function \emptyset is defined by \emptyset x x () - = 2 3
13. (i) find \emptyset \emptyset () () 0 1 2 + .
14. (ii) find x such that \emptyset (x) = 0.
15. (iii) find x such that \emptyset x x () = .
16. (iv) find x such that \emptyset x \emptyset x () () = - 1 .

10

7. An open box is to be made from a square piece of material, 24 cm on a side, by cutting equal squares from the corners and turning up the sides as shown (Fig.1.17). Express the volume V of the box as a function of x .
8. A function \emptyset is defined by \emptyset x x () = - 3 2 . Find x such that \emptyset x \emptyset x () (()) 2 2 = .
9. A plane is flying at a speed of 500 km per hour. Express the distance ' d ' travelled by the plane as function of time t in hours.
10. The data in the adjacent table depicts the length of a person forehand and their corresponding height. Based on this data, a student finds a relationship between the height (y) and the forehand length(x) as y ax b = + , where a , b are constants.
5. (i) Check if this relation is a function.
6. (ii) Find a and b .

| Length ' x ' of forehand (in cm) | Height ' y ' (in inches) |
|------------------------------------|----------------------------|
| 35 | 56 |
| 45 | 65 |
| 50 | 69.5 |
| 55 | 74 |

- (iii) Find the height of a person whose forehand length is 40 cm.
- (iv) Find the length of forehand of a person if the height is 53.3 inches.

## 1.6 Representation of Functions

A function may be represented by

- (a) a set of ordered pairs (b) a table form
- (c) an arrow diagram
- (d) a graphical form
- Let \emptyset A B : \\to be a function

## (a) Set of ordered pairs

The set \emptyset x y y \emptyset x x A = = ∈ {, | (),} () of all ordered pairs represent a function.

## (b) Table form

The values of x and the values of their respective images under \emptyset can be given in the form of a table.

## (c) Arrow diagram

An arrow diagram indicates the elements of the domain of \emptyset and their respective images by means of arrows.

## (d) Graph

The ordered pairs in the collection \emptyset x y y \emptyset x x A = = ∈ {() |} , (), are plotted as points in the XY - plane. The graph of \emptyset is the totality of all such points.

Every function can be represented by a curve in a graph. But not every curve drawn in a graph will represent a function.

The following test will help us in determining whether a given curve is a function or not.

## 1.6.1 Vertical line test

A curve drawn in a graph represents a function, if every vertical line intersects the curve at only one point.

Example 1.10 Using vertical line test, determine which of the following curves (Fig.1.18(a),

> **[IMAGE PLACEHOLDER — Fig. 1.18: Vertical line test curves (a, b, c, d)]**

Solution The curves in Fig.1.18 (a) and Fig.1.18 (c) do not represent a function as the vertical lines meet the curves in two points P and Q .

The curves in Fig.1.18 (b) and Fig.1.18 (d) represent a function as the vertical lines meet the curve in at most one point.

Any equation represented in a graph is usually called a curve.

Example 1.11 Let A = {, , , 1 2 3 4} and B = {} , , , , 2 5 8 11 14 be two sets. Let \emptyset A B : \\to be a function given by \emptyset x x () = - 3 1 . Represent this function

> **[IMAGE PLACEHOLDER — Fig. 1.19: Representations of function: arrow diagram, table, and graph]**

- (i) by arrow diagram (ii) in a table form
- (iii) as a set of ordered pairs (iv) in a graphical form

## Solution

A = {, , , 1 2 3 4} B = {} , , , , 2 5 8 11 14 \emptyset x x () = - 3

f () 1 = = = 3 1 1 3 1 2 () - ; \emptyset (2) = = = 3 2 1 6 1 () - -

; ; 1 5

f (3) = = = 3 3 1 9 1 8 () - ; \emptyset (4) = = = 4 3 1 12 1 11 () - -

## (i) Arrow diagram

Let us represent the function \emptyset A B : \\to by an arrow diagram (Fig.1.19).

## (ii) Table form

Fig. 1.19

The given function \emptyset can be represented in a tabular form as given below

| x 1 | 2 | 3 4 |
|-----------|-----|-------|
| \emptyset (x) 2 | 5 | 8 11 |

## (iii) Set of ordered pairs

The function \emptyset can be represented as a set of ordered pairs as

f = {(1,2),(2,5),(3,8),(4,11)}

## (iv) Graphical form

In the adjacent XY -plane the points (1,2), (2,5), (3,8), (4,11) are plotted (Fig.1.20).

Fig. 1.20

## 1.7 Types of Functions

In this section, we will discuss the following types of functions with suitable examples.

- (i) one - one

(ii) many - one (iii) onto (iv) into

## 1.7.1 One - one function

Let us assume that we have a cell phone with proper working condition. If you make a usual call to your friend then you can make only one call at a time (Fig.1.21).

If we treat making calls as a function, then it will be one - one.

A function \emptyset A B : \\to is called one - one function if distinct elements of A have distinct images in B .

A one-one function is also called an injection .

Equivalently,

If for all a a A 1 2 , \in , \emptyset a \emptyset a () () 1 2 = implies a a 1 2 = , then \emptyset is called one - one function.

## Illustration 10

A = {1,2,3,4} and B = {a , b , c , d , e}

- (i) Let \emptyset = {(1, a), (2, b), (3, d), (4, c)}

In Fig. 1.22, for different elements in A , there are different images in B .

Hence \emptyset is a one - one function.

- (ii) Let g = {(1, b), (2, b), (3, c), (4, e)} g is a function from A to B such that g g b () () 1 2 = = , but 1 2 \neq . Thus two distinct elements 1 and 2 in the first set A have same image b the second set in B (Fig.1.23). Hence, g is not a one-one function.

## 1.7.2 Many - one function

In a theatre complex three films F 1 , F 2 , F 3 are shown. Seven persons (P 1 to P 7) arrive at the theatre and buy tickets as shown (Fig.1.24).

If the selection of films is considered as a relation, then this is a function which is many-one, since more than one person may choose to watch the same film.

A function \emptyset A B : \\to is called many-one function if two or more elements of A have same image in B .

In other words, a function \emptyset A B : \\to is called many-one if \emptyset it is not one-one.

## Illustration 11

Let A = {1,2,3,4} and B = {a , b , c}, \emptyset = {(1, a), (2, a), (3, b), (4, c)}

Then \emptyset is a function from A to B in which different elements 1 and 2 of A have the same image a in B . Hence \emptyset is a many - one function.

## 1.7.3 Onto function

In a mobile phone assume that there are 3 persons in the contact. If every person in the contact receives a call, then the function representing making calls will be onto. (Fig.1.25)

A function \emptyset A B : \\to is said to be onto function if the range of \emptyset is equal to the co-domain of \emptyset .

In other words, every element in the co-domain B has a pre-image in the domain A .

An onto function is also called a surjection .

> **[IMAGE PLACEHOLDER — Fig. 1.25: Onto function mapping]**

If \emptyset A B : \\to is an onto function then, the range of \emptyset B = .

## Illustration 12

Let A x y z B l m n = = {, ,}, {, ,} ;

Range of \emptyset = = {, ,} l m n B (Fig.1.26)

Hence \emptyset is an onto function.

## 1.7.4 Into function

In a home appliance showroom, the products television, air conditioner, washing machine and water heater were provided with 20% discount as new year sale offer. If the selection of the above products by the three customers C 1 , C 2 , C 3 is considered as a function then the following diagram (Fig.1.27) will represent an into function.

During winter season customers usually do not prefer buying air conditioner. Here air conditioner is not chosen by any customer. This is an example of into function.

That is the range of \emptyset is a proper subset of the co-domain of \emptyset .

In other words, a function \emptyset A B : \\to is called 'into' if it is not 'onto' .

## Illustration 13

Let A = {1,2,3,} and B w x y z = {} , , , , \emptyset w z x = {()} , ,(,) 1 2 ,(3,)

Here, range of \emptyset w x z B = ⊂ {} , , (Fig.1.28)

∴ \emptyset is a into function.

Note that y B \in is not an image of any element in A .

## 1.7.5 Bijection

Consider the circle where each letter of the English alphabet is changed from inner portion to a letter in the outer portion. Thus A D \\to , B E \\to , C F \\to , … Z C \\to . We call this circle as 'cipher circle' . (Fig.1.29) In this way if we try to change the word 'HELLO' then it will become 'KHOOR'. Now using the same circle if we substitute for each outer letter the corresponding inner letter we will get back the word 'HELLO' . This process of converting

Fig. 1.28

from one form to an other form and receiving back the required information is called bijection . This process is widely used in the study of secret codes called cryptography .

If a function \emptyset A B : \\to is both one-one and onto, then \emptyset is called a bijection from A to B .

## Illustration 14

| one to one and onto function (Bijection) | one to one and onto function (Bijection) |
|--------------------------------------------|------------------------------------------------------------------------------------------------|
| Fig. 1.30 1 2 3 w x z A B \emptyset | Distinct elements of A have distinct images in B and every element in B has a pre-image in A . |

## Illustration 15

## One to One

## Many to One

Fig. 1.31

Distinct elements of A have distinct images in B .

Fig. 1.32

Two or more elements of A have same image in B .

## Onto

## Note

A one - one and onto function is also called a one - one correspondence.

## Thinking Corner

Can there be a one to many function?

## Into

## Range of \emptyset = co-domain

(Every element in B has a pre-image in A)

Range of \emptyset is a proper subset of co-domain (There exists at least one element in B which is not the image of any element of A)

To determine whether the given function is one-one or not the following test may help us.

## 1.7.6 Horizontal Line Test

Previously we have seen the vertical line test. Now let us see the horizontal line test. 'A function represented in a graph is one-one, if every horizontal line intersects the curve at only one point' .

Example 1.12 Using horizontal line test (Fig.1.35 (a), 1.35 (b), 1.35 (c)), determine which

> **[IMAGE PLACEHOLDER — Fig. 1.35: Horizontal line test curves (a, b, c)]**
 of the following functions are one - one.

Solution The curves in Fig.1.35 (a) and Fig.1.35 (c) represent a one-one function as the horizontal lines meet the curves in only one point P .

The curve in Fig. 1.35 (b) does not represent a one-one function, since, the horizontal line intersects the curve at two points P and Q .

Solution A = {} , , 1 2 3 , B = {} , , , 4 5 6 7 ; \emptyset = {(,)} ,(,),(,) 1 4 2 5 3 6

Then \emptyset is a function from A to B and for different elements in A , there are different images in B . Hence \emptyset is one-one function. Note that the element 7 in the co-domain does not have any pre-image in the domain. Hence \emptyset is not onto (Fig.1.36).

∴ \emptyset is one-one but not an onto function.

Example 1.14 If A = - {} , , , , 2 1 0 1 2 and \emptyset A B : \\to is an onto function defined by \emptyset x x x () = + + 2 1 then find B .

Solution Given A = - {} , , , , 2 1 0 1 2 and \emptyset x x x () = + + 2 1

f () - 2 = - + - + () () 2 2 1 2 \emptyset () - 1 = - + - + () () 1 1 1 2 =1 \emptyset (0) = + + 0 0 1 2 =1; \emptyset (1) = + + = 1 1 1 3 2 \emptyset (2) = + + 2 2 1 2 = 7 ∴ B = {} , , 1 3 7

. =3; .

Example 1.15 Let \emptyset be a function \emptyset : \mathbb{N} \mathbb{N} \\to be defined by \emptyset x x x () , = + ∈ 3 2 \mathbb{N}

- (i) Find the images of 1, 2, 3 (ii) Find the pre-images of 29, 53
- (ii) Identify the type of function

Solution The function \emptyset : \mathbb{N} \mathbb{N} \\to is defined by \emptyset x x () = + 3 2

(i) If x = 1, \emptyset () () 1 3 1 2 = + = 5 If x = 2, \emptyset () () 2 3 2 2 = + = 8 If x = 3 , \emptyset () () 3 3 3 2 = + = 11

The images of 1, 2, 3 are 5, 8, 11 respectively.

- (ii) If x is the pre-image of 29, then \emptyset x () = 29 . Hence 3 2 29 x + =

3 27 9 x x = ⇒ = .

x \emptyset x () = 53 3 2 53 x + =

Similarly, if is the pre-image of 53, then . Hence 3 51 17 x x = ⇒ = .

Thus the pre-images of 29 and 53 are 9 and 17 respectively.

- (iii) Since different elements of \mathbb{N} have different images in the co-domain, the function \emptyset is one - one function.

The co-domain of \emptyset is \mathbb{N} .

But the range of \emptyset = {5, 8, 11, 14, 17, ...} is a proper subset of \mathbb{N} .

- ∴ \emptyset is not an onto function. That is, \emptyset is an into function.

Thus \emptyset is one - one and into function.

Example 1.16 Forensic scientists can determine the height (in cm) of a person based on the length of the thigh bone. They usually do so using the function h b b () = ⋅ + ⋅ 2 47 54 10 where b is the length of the thigh bone.

- (i) Verify the function h is one - one or not.
- (ii) Also find the height of a person if the length of his thigh bone is 50 cm.
- (iii) Find the length of the thigh bone if the height of a person is 147 96 × cm.

Solution (i)	To check if h is one - one, we assume that h b h b () () 1 2 = .

2

Then we get, 2 47 54 10 1 ⋅ + ⋅ b = ⋅ + ⋅ 2 47 54 10 2 b 2 47 1 × b = ⋅ ⇒ = 2 47 2 1 b b b = ⋅ ⇒ = 2 47 2 1 2 b b b

Thus, h b h b b b () () 1 2 1 2 = ⇒ = . So, the function h is one - one.

- (ii) If the length of the thigh bone b = 50, then the height is h () () 50 2 47 50 54 10 177 6 = ⋅ × + ⋅ = ⋅ cm.
- (iii) If the height of a person is 147 96 × cm, then h b () = ⋅ 147 96 and so the length of the thigh bone is given by

2 47 54 10 147 96 ⋅ + ⋅ = ⋅ b \implies 2 47 147 96 54 10 93 86 ⋅ = ⋅ - ⋅ = ⋅ b b = ⋅ ⋅ = 93 86 2 47 38

Therefore, the length of the thigh bone is 38 cm.

## Activity 3

Check whether the following curves represent a function. In the case of a function, check whether it is one-one? (Hint: Use the vertical and the horizontal line tests)

## 1.8 Special Cases of Functions

There are some special cases of a function which will be very useful. We discuss some of them below

- (i) Constant function
- (ii) Identity function
- (iii) Real - valued function

> **[IMAGE PLACEHOLDER — Fig. 1.36: Graphs of Constant, Identity, and Real-valued functions]**

## (i) Constant function

A function \emptyset A B : \\to is called a constant function if the range of \emptyset contains only one element. That is, \emptyset x c () = , for all x A \in and for some fixed c B \in . A \emptyset B

## Illustration 16

From Fig.1.37, A a b c d = {} , , , , B = {, , 1 2 3} and \emptyset a b c d = {() () () ()} , , , , , , , 3 3 3 3 . \emptyset x () = 3 ∀ x A \in , Range of \emptyset = {} 3 , \emptyset is a constant function.

## (ii) Identity function

Let A be a non-empty set. Then the function \emptyset A A : \\to defined by \emptyset x x () = \emptysetor all x A \in is called an identity function on A and is denoted by I A .

## Illustration 17

If A a b c = {} , , then \emptyset I a a b b c c A = = {(,),(,),(,)} is an identity function on A .

## (iii) Real valued function

A function \emptyset A B : \\to is called a real valued function if the range of \emptyset is a subset of the set of all real numbers \mathbb{R} . That is, \emptyset a a A () , ⊆ ∀ ∈ \mathbb{R} .

## Progress Check

## State True or False.

1. All one - one functions are onto functions.
2. There will be no one - one function from A to B when n A () = 4 , n B () = 3 .
3. All onto functions are one - one functions.
4. There will be no onto function from A to B when n A () = 4 , n B () = 5 .
5. If \emptyset is a bijection from A to B , then n n A B () () = .
6. If n n A B () () = , then \emptyset is a bijection from A to B .
7. All constant functions are bijections.

Example 1.17 Let \emptyset be a function from \mathbb{R} to \mathbb{R} defined by \emptyset x x () = - 3 5 . Find the values of a and b given that (a , 4) and (1, b) belong to \emptyset .

Solution \emptyset x x () - = 3 5 can be written as \emptyset x x x R = ∈ {} () , - | 3 5

(a , 4) means the image of a is 4. i.e., \emptyset a () = 4 3a - 5 = 4 ⇒ = a 3 (1, b) means the image of 1 is b . i.e., \emptyset b () 1 = 3(1) - 5 = b ⇒ b = -2

## Thinking Corner

Is an identity function one to one function?

Example 1.18

If the function

f

then find the values of

f x x x x x x x () ; ; ; = + <- - \ge ⎧ ⎨ ⎪ ⎪ ⎪ ⎪ ⎩ ⎪ ⎪ ⎪ ⎪ - \le < 2 7 2 3 2 3 2 2 3 2 ,

(i) \emptyset (4) (ii) \emptyset () - 2 (iii) \emptyset \emptyset () () 4 2 1 + (iv) \emptyset \emptyset \emptyset () () () 1 3 4 3 - -

## Solution

The function \emptyset is defined by three values in intervals I, II, III as shown by the side

Fig. 1.39 -6 -5 -4 -3 -2 -1 0 1 2 3 4 5 6 \emptyset (x) = 2 x +7 I X ′ II III X \emptyset (x) = x 2 -2 \emptyset (x) = 3 x -2 [ [))

For a given value of x a = , find out the interval at which the point a is located, there after find \emptyset a () using the particular value defined in that interval.

- (i) First, we see that, x = 4 lie in the third interval.

∴ \emptyset x x () = - 3 2 ; \emptyset () () - 4 3 4 2 10 = =

- (ii) x =- 2 lies in the second interval.

∴ \emptyset x x () - = 2 2 ; \emptyset () () - = - = 2 2 2 2 2

- (iii) From (i), \emptyset (4) 10 = .

To find \emptyset (), 1 first we see that x = 1 lies in the second interval.

∴ \emptyset x x () - = 2 2 ⇒ = =- \emptyset () - 1 1 2 2

f \emptyset () () 4 2 1 + = + - = 10 2 1 ()

1 8

- (iv) We know that \emptyset () 1 1 = - and \emptyset (4) 10 = .

For finding \emptyset () - 3 , we see that x =- 3 , lies in the first interval.

∴ \emptyset x x () = + 2 7 ; thus, \emptyset () () - = - + = 3 2 3 7 1

Hence, \emptyset \emptyset \emptyset () () () 1 3 4 3 - = - 1 3 10 1 () =- 31

## Exercise 1.4

1. Determine whether the graph given below represent functions. Give reason for your answers concerning each graph.

> **[IMAGE PLACEHOLDER — Fig. 1.39: Vertical line test graphs for Exercise 1.4]**

Y

f

R

R

:

®

:

\mathbb{R}

\mathbb{R}

is defined by

2. Let \emptyset A B : \\to be a function defined by \emptyset x x () , = - 2 1 where A = {} , , , , 2 4 6 10 12 , B = {} , , , , , 0 1 2 4 5 9 . Represent \emptyset by
2. (i) set of ordered pairs (ii) a table (iii) an arrow diagram (iv) a graph
3. Represent the function \emptyset = {, , , , ,} ()()()()() 1 2 2 2 3 2 4 3 5 4 , , , , through
4. (i) an arrow diagram (ii) a table form (iii) a graph
4. Show that the function \emptyset : \mathbb{N} \mathbb{N} \\to defined by \emptyset x x () - = 2 1 is one-one but not onto.
5. Show that the function \emptyset : \mathbb{N} \mathbb{N} \\to defined by \emptyset m m m () = + + 2 3 is one-one function.
6. Let A = {} , , , 1 2 3 4 and B = \mathbb{N} . Let \emptyset A B : \\to be defined by \emptyset x x () = 3 then, (i) find the range of \emptyset (ii) identify the type of function
7. In each of the following cases state whether the function is bijective or not. Justify your answer.
9. (i) \emptyset : \mathbb{R} \mathbb{R} \\to defined by \emptyset x x () = + 2 1 (ii) \emptyset : \mathbb{R} \mathbb{R} \\to defined by \emptyset x x () - = 3 4 2
8. Let A = - {,} 1 1 and B = {} , 0 2 . If the function \emptyset A B : \\to defined by \emptyset x ax b () = + is an onto function? Find a and b .
9. If the function \emptyset is defined by \emptyset x x x x x x () ; ; - ; = + > - \le \le - < <- ⎧ ⎨ ⎪ ⎪ ⎪ ⎪ ⎩ ⎪ ⎪ ⎪ ⎪ 2 1 2 1 1 1 3 1 find the values of
12. (i) \emptyset (3) (ii) \emptyset (0) (iii) \emptyset () - ⋅ 1 5 (iv) \emptyset \emptyset () () 2 2 + -
10. A function \emptyset : [ , ] - → 5 9 \mathbb{R} is defined as follows:

f x x x x x x x () ; ; - ; = + - \le < - \le < \le \le ⎧ ⎨ ⎪ ⎪ ⎪ ⎪ ⎩ ⎪ ⎪ ⎪ ⎪ 6 1 5 2 5 1 2 6 3 4 6 9 2

Find (i) \emptyset \emptyset () () - + 3 2 (ii) \emptyset \emptyset () () 7 1 - (iii) 2 4 8 \emptyset \emptyset () () + (iv) 2 2 6 4 2 \emptyset \emptyset \emptyset \emptyset () () () () - + -

11. The distance S an object travels under the influence of gravity in time t seconds is given by S t gt at b () = + + 1 2 2 where, (g is the acceleration due to gravity), a > 0, b are constants. Verify wheather the function S t () is one-one or not.
12. The function ' t ' which maps temperature in Celsius (C) into temperature in Fahrenheit (F) is defined by t C F () = where F C = + 9 5 32 . Find,
3. (i) t (0) (ii) t (28) (iii)
4. t () - 10
5. (iv) the value of C when t C () = 212
6. (v) the temperature when the Celsius value is equal to the Farenheit value.

## 1.9 Composition of Functions

When a car driver depresses the accelerator pedal, it controls the flow of fuel which in turn influences the speed of the car. Likewise, the composition of two functions is a

> **[IMAGE PLACEHOLDER — Fig. 1.41: Composition of functions arrow diagram (f o g)]**
 kind of 'chain reaction' , where the functions act upon one after another (Fig.1.40).

We can explain this further with the concept that a function is a 'process' . If \emptyset and g are two functions then the composition g \emptyset x (()) (Fig.1.41) is formed in two steps.

- (i) Feed an input (say x) to \emptyset ;
- (ii) Feed the output \emptyset (x) to g to get g \emptyset x (()) and call it gf (x).

## Illustration

Consider the set A of all students, who appeared in class X of Board Examination. Each student appearing in the Board Examination is assigned a roll number. In order to have confidentiality, the Board arranges to deface the roll number of each student and assigns a code number to each roll number.

Let A be the set of all students appearing for the board exam. B \subseteq \mathbb{N} be the set all roll numbers and C \subseteq \mathbb{N} be the set of all code numbers (Fig.1.41). This gives rise to two functions \emptyset A B : \\to and g B C : \\to given by b \emptyset a = () be the roll number assigned to student a , c g b = () be the code number assigned to roll number b , where a \in A, b \in B and c C \in . Fig. 1.41

We can write c g b g \emptyset a = = () (()) .

Thus, by the combination of these two functions, each student is eventually attached a code number. This idea leads to the following definition. A B C

## Definition

Let \emptyset A B : \\to and g B C : \\to be two functions (Fig.1.42). Then the composition of \emptyset and g denoted by g \emptyset \\circ is defined as the function g \emptyset x g \emptyset x \\circ () (()) = ∀ x A \in .

Example 1.19 Find \emptyset g \\circ and g \emptyset \\circ when \emptyset x x () = + 2 1 and g x x () = - 2 2

f g x () = \emptyset g x (()) = - \emptyset x () 2 2 = - + 2 2 1 2 () x = - 2 3 2 x g \emptyset x () = g \emptyset x (()) = + g x () 2 1 = + - () 2 1 2 2 x = + - 4 4 1 2 x x

Solution \emptyset x x () = + 2 1 , g (x) = x 2 - 2 \\circ 

Thus \emptyset g x \\circ = - 2 3 2 , g \emptyset x x \\circ = + - 4 4 1 2 . From the above, we see that \emptyset g g \emptyset \\circ  \neq .

Example 1.20 Represent the function \emptyset x x x () = - + 2 5 3 2 as a composition of two functions.

Solution

f x x x 2 2 5 3 2 () = - + and \emptyset x x 1 () =

f x () = - + 2 5 3 2 x x = \emptyset x 2 () = ⎡ ⎣ ⎢ ⎤ ⎦ ⎥ \emptyset \emptyset x 1 2 () = \emptyset \emptyset x 1 2 ()

Example 1.21 If \emptyset x x () = - 3 2 , g x x k () = + 2 and if \emptyset g g \emptyset \\circ  = , then find the value of k . Solution \emptyset x x () = - 3 2 , g x x k () = + 2

f g x \\circ () = \emptyset g x (()) = + \emptyset x k () 2 = + - 3 2 2 () x k = + - 6 3 2 x k

f g x \\circ () = + - 6 3 2 x k .

g \emptyset x () = - g x () 3 2 = - + 2 3 2 () x k

 g \emptyset x \\circ () = - + 6 4 x k .

Given that \emptyset g \\circ = g \emptyset \\circ ∴ 6 3 2 x k + - = - + 6 4 x k 6 6 3 x x k k - + - =- + 4 2 ⇒ =- k 1

Example 1.22 Find k if \emptyset \emptyset k \\circ () = 5 where \emptyset k k () = - 2 1 .

Solution \emptyset \emptyset k \\circ () = \emptyset \emptyset k (()) = - 2 2 1 1 () k = - 4 3 k . \emptyset \emptyset k \\circ () = - 4 3 k But, \emptyset \emptyset k \\circ () = 5 ∴ 4 3 k - = 5 ⇒ = k 2 .

## 1.9.1 Composition of three functions

Let A , B , C , D be four sets and let \emptyset A B : \\to , g B C : \\to and h C D : \\to be three functions (Fig.1.43). Using composite functions \emptyset g \\circ and g h \\circ , we get two new functions like () \emptyset g h \\circ  and \emptyset g h \\circ  () .

We observed that the composition of functions is not commutative. The natural question is about the associativity of the operation.

Composition of three functions is always associative. That is, \emptyset g h \emptyset g h \\circ  \\circ  () () =

The Composition g \emptyset x \\circ () exists only when range of \emptyset is a subset of domain of g.

Example 1.23 If \emptyset x x () = + 2 3 , g x x () = - 1 2 and h x x () = 3 . Prove that \emptyset g h \emptyset g h \\circ  \\circ  () () =

Solution \emptyset x x () = + 2 3 , g x x () = - 1 2 , h x x () = 3 Now, ()() \emptyset g x \\circ = \emptyset g x (()) = - \emptyset x () 1 2 = - + 2 1 2 3 () x = - 5 4 x Then, () () \emptyset g h x \\circ  = ()(()) \emptyset g h x \\circ = ()() \emptyset g x \\circ 3 = - 5 4 3 () x = - 5 12 x ....(1) ()() g h x \\circ = g h x (()) = g x () 3 = - 1 2 3 () x = - 1 6 x ⇒ \emptyset g h x \\circ  ()() = - \emptyset x () 1 6 = - + 2 1 6 3 () x = - 5 12 x ....(2) From (1) and (2), we get () () \emptyset g h \emptyset g h \\circ  \\circ  =

Example 1.24 Find x if gff (x) = \emptysetgg (x), given \emptyset x x () = + 3 1 and g x x () = + 3 .

Solution

gff (x)	= g [ \emptyset {\emptyset (x)}] (This means ' g of \emptyset of \emptyset of x ') = g [ \emptyset (3 x +1)] = g [ 3(3 x +1)+1] = g (9 x + 4) g (9 x + 4)	= [ (9 x + 4) + 3] = 9 x + 7 fgg (x)	= \emptyset [ g {g (x)}] (This means ' \emptyset of g of g of x ') = \emptyset [ g (x + 3)] = \emptyset [ (x + 3) + 3] = \emptyset (x + 6) \emptyset (x + 6)	= [ 3(x + 6) + 1 ] = 3 x + 19

These two quantities being equal, we get 9 x + 7 = 3 x + 19. Solving this equation we obtain x = 2.

## Progress Check

State your answer for the following questions by selecting the correct option.

1. Composition of functions is commutative
2. (a) Always true
3. (b) Never true
4. (c) Sometimes true
2. Composition of functions is associative
6. (a) Always true
7. (b) Never true
8. (c) Sometimes true

## Activity 4

Given that h x \emptyset g x () () = \\circ , fill in the table for h x ()

| x | f(x) |
|-----|--------|
| 1 | 2 |
| 2 | 3 |
| 3 | 1 |
| 4 | 4 |

| x | g(x) |
|-----|--------|
| 1 | 2 |
| 2 | 4 |
| 3 | 3 |
| 4 | 1 |

| x | h(x) |
|-----|--------|
| 1 | 3 |
| 2 | - |
| 3 | - |
| 4 | - |

h x () = \emptyset g x \\circ () h () 1 = \emptyset g \\circ () 1 = \emptyset (2) = 3 ∴ h () 1 = 3

## 1.10 Identifying the Graphs of Linear, Quadratic, Cubic and Reciprocal Functions

Graphs provide visualization of curves and functions. Hence, graphs help a lot in understanding the concepts in a much efficient way.

In this section, we will be discussing about the identification of some of the functions through their graphs. In particular, we discuss graphs of Linear, Quadratic, Cubic and Reciprocal functions.

## 1.10.1	Linear Function

A function \emptyset : \mathbb{R} \mathbb{R} \\to defined by \emptyset x mx c () = + , m \neq 0 is called a linear function. Geometrically this represents a straight line in the graph.

> **[IMAGE PLACEHOLDER — Fig. 1.42: Linear function graph]**

Some Specific Linear Functions and their graphs are given below.

| No. | Function | Domain and Definition |
|-------|---------------------------|-----------------------------------|
| 1 | The identity function | \emptyset : \mathbb{R} \mathbb{R} \\to defined by \emptyset x x () = |
| 2 | Additive inverse function | \emptyset : \mathbb{R} \mathbb{R} \\to defined by \emptyset x x () =- |

## Note

- Modulus function is not a linear function but it is composed of two linear functions x and - x .
- Linear functions are always one-one functions and has applications in Cryptography as well as in several branches of Science and Technology.

## 1.10.2 Modulus or Absolute valued Function

A function (f:\mathbb{R}\to[0,\infty)) defined by

$$
f(x)=|x|
$$

is called the modulus or absolute valued function.

It can be written as

$$
f(x)=
\begin{cases}
x, & x\ge 0,\\
-x, & x<0.
\end{cases}
$$

> **[IMAGE PLACEHOLDER — Fig. 1.46: Graph of the modulus or absolute valued function]**

## Note

- Modulus function is not a linear function but it is composed of two linear functions (x) and (-x).
- Linear functions are always one-one functions and have applications in Cryptography as well as in several branches of Science and Technology.

## 1.10.3 Quadratic Function

A function \emptyset : \mathbb{R} \mathbb{R} \\to defined by \emptyset x ax bx c () , = + + 2 () a \neq 0 is called a quadratic function.

Some specific quadratic functions and their graphs

> **[IMAGE PLACEHOLDER — Fig. 1.43: Graphs of Quadratic, Cubic, and Reciprocal functions]**

| Function, Domain, Range and Definition | Graph |
|--------------------------------------------------------------------|----------------------------|
| \emptyset : \mathbb{R} \mathbb{R} \\to defined by \emptyset x x x () , . = ∈ 2 \mathbb{R} \emptyset x () [ ,) ∈ ∞ 0 | X Y ′ O X ′ Y Fig. 1.47(a) |
| \emptyset : \mathbb{R} \mathbb{R} \\to defined by \emptyset x x x () , . =- ∈ 2 \mathbb{R} \emptyset x () (, ] ∈ -∞ 0 | X Y ′ O Y X ′ Fig. 1.47(b) |

## 1.10.4 Cubic Function

A function \emptyset : ®

f x ax bx cx d a () ,() = + + + \neq 3 2 0

The graph of \emptyset x x () = 3

\mathbb{R} \mathbb{R} defined by is called a cubic function. is shown in Fig.1.48.

## 1.10.5 Reciprocal Function

A function \emptyset : \mathbb{R} \mathbb{R} - {} → 0 defined by \emptyset x x () = 1

is called a reciprocal function (Fig.1.49).

## 1.10.6 Constant Function

A function \emptyset : \mathbb{R} \mathbb{R} \\to defined by \emptyset x c () , = ∀ x \in \mathbb{R} is called a constant function (Fig.1.50).

## Progress Check

1. Is a constant function a linear function?
2. Is quadratic function a one - one function?
3. Is cubic function a one - one function?
4. Is the reciprocal function a bijection?
5. If \emptyset A B : \\to is a constant function, then the range of \emptyset will have \_\_\_\_ elements.
1. Using the functions \emptyset and g given below, find \emptyset g \\circ and g \emptyset \\circ . Check whether \emptyset g g \emptyset \\circ  = .
7. (i) \emptyset x x () , = - 6 g x x () = 2

(iii) \emptyset x x () , = + 6 3 g x x () = - 3

- (v) \emptyset x x g x x () , () = - = + 4 1 1 2
2. Find the value of k , such that \emptyset g g \emptyset \\circ  =
- (i) \emptyset x x g x x k () , () = + = - 3 2 6

(ii) \emptyset x x () , = 2 g x x () = - 2 1 2

- (iv) \emptyset x x () , = + 3 g x x () = - 4

(ii) \emptyset x x k g x x () , () = - = + 2 4 5

3. If \emptyset x x () , = - 2 1 g x x () = + 1 2 , show that \emptyset g g \emptyset x \\circ  = =
4. If \emptyset x x () , = - 2 1 g x x () = - 2 find a , if g \emptyset a \\circ () = 1 .
5. Let A B C , , \subseteq \mathbb{N} and a function \emptyset A B : \\to be defined by \emptyset x x () = + 2 1 and g B C : \\to be defined by g x x () = 2 . Find the range of \emptyset g \\circ and g \emptyset \\circ .
6. Let \emptyset x x () = - 2 1 . Find (i) \emptyset \emptyset \\circ (ii) \emptyset \emptyset \emptyset \\circ 
7. If \emptyset : \mathbb{R} \mathbb{R} \\to and g : \mathbb{R} \mathbb{R} \\to are defined by \emptyset x x () = 5 and g x x () = 4 then check if \emptyset , g are one-one and \emptyset g \\circ is one-one?

Fig. 1.50

8. Consider the functions \emptyset x (), g x (), h x () as given below. Show that () () \emptyset g h \emptyset g h \\circ  \\circ  = in each case.
2. (i) \emptyset x x () , = - 1 g x x () = + 3 1 and h x x () = 2
3. (ii) \emptyset x x () , = 2 g x x () = 2 and h x x () = + 4
4. (iii) \emptyset x x () , = - 4 g x x () = 2 and h x x () = - 3 5
9. Let \emptyset = - - {() () ()} , , , , , 1 3 0 1 2 9 be a linear function from \mathbb{Z} into \mathbb{Z} . Find \emptyset (x).
10. In electrical circuit theory, a circuit C (t) is called a linear circuit if it satisfies the superposition principle given by C at bt aC t bC t () () () 1 2 1 2 + = + , where a b , are constants. Show that the circuit C t t () = 3 is linear.

1.

## Exercise 1.5

1. Using the functions (f) and (g) given below, find (f\circ g) and (g\circ f). Check whether (f\circ g=g\circ f).

   1. (f(x)=x-6,quad g(x)=x^2)
   2. (f(x)=\dfrac{2}{x},quad g(x)=2x^2-1)
   3. (f(x)=\dfrac{x+6}{3},quad g(x)=3-x)
   4. (f(x)=3+x,quad g(x)=x-4)
   5. (f(x)=4x^2-1,quad g(x)=1+x^2)

2. Find the value of (k), such that (f\circ g=g\circ f).

   1. (f(x)=3x+2,quad g(x)=6x-k)
   2. (f(x)=2x-k,quad g(x)=4x+5)

3. If (f(x)=2x-1,quad g(x)=\dfrac{x+1}{2}), show that
   [
   f\circ g=g\circ f=x.
   ]

4. If (f(x)=x^2-1,quad g(x)=x-2), find (a), if
   [
   (g\circ f)(a)=1.
   ]

5. Let (A,B,C\subseteq\mathbb{N}) and a function (f:A\to B) be defined by (f(x)=2x+1) and (g:B\to C) be defined by (g(x)=x^2). Find the range of (f\circ g) and (g\circ f).

6. Let (f(x)=x^2-1). Find
   1. (f\circ f)
   2. (f\circ f\circ f)

7. If (f:\mathbb{R}\to\mathbb{R}) and (g:\mathbb{R}\to\mathbb{R}) are defined by (f(x)=x^5) and (g(x)=x^4), then check if (f,g) are one-one and (f\circ g) is one-one.

8. Consider the functions (f(x),g(x),h(x)) as given below. Show that
   [
   (f\circ g)\circ h=f\circ(g\circ h)
   ]
   in each case.

   1. (f(x)=x-1,quad g(x)=3x+1,quad h(x)=x^2)
   2. (f(x)=x^2,quad g(x)=2x,quad h(x)=x+4)
   3. (f(x)=x-4,quad g(x)=x^2,quad h(x)=3x-5)

9. Let
   [
   f=\{(-1,3),(0,-1),(2,-9)\}
   ]
   be a linear function from (mathbb{Z}) into (mathbb{Z}). Find (f(x)).

10. In electrical circuit theory, a circuit (C(t)) is called a linear circuit if it satisfies the superposition principle
    [
    C(at_1+bt_2)=aC(t_1)+bC(t_2),
    ]
    where (a,b) are constants. Show that the circuit (C(t)=3t) is linear.

## Exercise 1.6

### Multiple choice questions

1. If (n(A\times B)=6) and (A=\{1,3\}), then (n(B)) is

   - (A) 1
   - (B) 2
   - (C) 3
   - (D) 6

2. (A=\{a,b,p\}, B=\{2,3\}, C=\{p,q,r,s\}), then (n[(A\cup C)\times B]) is

   - (A) 8
   - (B) 20
   - (C) 12
   - (D) 16

3. If (A=\{1,2\}, B=\{1,2,3,4\}, C=\{5,6\}) and (D=\{5,6,7,8\}), then state which of the following statement is true.

   - (A) ((A\times C)\subset(B\times D))
   - (B) ((B\times D)\subset(A\times C))
   - (C) ((A\times B)\subset(A\times D))
   - (D) ((D\times A)\subset(B\times A))

4. If there are 1024 relations from a set (A=\{1,2,3,4,5\}) to a set (B), then the number of elements in (B) is

   - (A) 3
   - (B) 2
   - (C) 4
   - (D) 8

5. The range of the relation
   [
   R=\{(x,x^2)\mid x\text{ is a prime number less than }13\}
   ]
   is

   - (A) \(\{2,3,5,7\}\)
   - (B) \(\{2,3,5,7,11\}\)
   - (C) \(\{4,9,25,49,121\}\)
   - (D) \(\{1,4,9,25,49,121\}\)

6. If the ordered pairs ((a+2,4)) and ((5,2a+b)) are equal, then ((a,b)) is

   - (A) ((2,-2))
   - (B) ((5,1))
   - (C) ((2,3))
   - (D) ((3,-2))

7. Let (n(A)=m) and (n(B)=n). Then the total number of non-empty relations that can be defined from (A) to (B) is

   - (A) (mn)
   - (B) (nm)
   - (C) (2^{mn}-1)
   - (D) (2^{mn})

8. If ({(a,8),(6,b)}) represents an identity function, then the value of (a) and (b) are respectively

   - (A) ((8,6))
   - (B) ((8,8))
   - (C) ((6,8))
   - (D) ((6,6))

9. Let (A=\{1,2,3,4\}) and (B=\{4,8,9,10\}). A function (f:A\to B) given by
   [
   f=\{(1,4),(2,8),(3,9),(4,10)\}
   ]
   is a

   - (A) Many-one function
   - (B) Identity function
   - (C) One-to-one function
   - (D) Into function

10. If (f(x)=2x^2) and (g(x)=\dfrac{1}{3x}), then (f\circ g) is

   - (A) (\dfrac{3}{2x^2})
   - (B) (\dfrac{2}{3x^2})
   - (C) (\dfrac{2}{9x^2})
   - (D) (\dfrac{1}{6x^2})

11. If (f:A\to B) is a bijective function and (n(B)=7), then (n(A)) is equal to

   - (A) 7
   - (B) 49
   - (C) 1
   - (D) 14

12. Let (f) and (g) be two functions given by
   [
   f=\{(0,1),(2,0),(3,-4),(4,2),(5,7)\}
   ]
   [
   g=\{(0,2),(1,0),(2,4),(-4,2),(7,0)\}.
   ]
   Then the range of (f\circ g) is

   - (A) \(\{0,2,3,4,5\}\)
   - (B) \(\{-4,1,0,2,7\}\)
   - (C) \(\{1,2,3,4,5\}\)
   - (D) \(\{0,1,2\}\)

13. Let
   [
   f(x)=\sqrt{1+x^2}
   ]
   then

   - (A) (f(xy)=f(x)f(y))
   - (B) (f(xy)\ge f(x)f(y))
   - (C) (f(xy)\le f(x)f(y))
   - (D) None of these

14. If
   [
   g=\{(1,1),(2,3),(3,5),(4,7)\}
   ]
   is a function given by (g(x)=\alpha x+\beta), then the values of (alpha) and (eta) are

   - (A) ((-1,2))
   - (B) ((2,-1))
   - (C) ((-1,-2))
   - (D) ((1,2))

15. (f(x)=(x+1)^3-(x-1)^3) represents a function which is

   - (A) linear
   - (B) cubic
   - (C) reciprocal
   - (D) quadratic

## Unit Exercise - 1

1. If the ordered pairs ((x^2-3x, y^2+4y)) and ((-2,5)) are equal, then find (x) and (y).

2. The Cartesian product (A\times A) has 9 elements among which ((-1,0)) and ((0,1)) are found. Find the set (A) and the remaining elements of (A\times A).

3. Given that
   [
   f(x)=
   \begin{cases}
   \sqrt{x-1}, & x\ge1,\\
   4, & x<1,
   \end{cases}
   ]
   find
   1. (f(0))
   2. (f(3))
   3. (f(a+1)) in terms of (a). (Given that (a\ge0))

4. Let
   [
   A=\{9,10,11,12,13,14,15,16,17\}
   ]
   and let (f:A\to\mathbb{N}) be defined by (f(n)) = the highest prime factor of (n\in A). Write (f) as a set of ordered pairs and find the range of (f).

5. Find the domain of the function
   [
   f(x)=1+\sqrt{1+\sqrt{1-x^2}}.
   ]

6. If (f(x)=x^2, g(x)=3x) and (h(x)=x-2), prove that
   [
   (f\circ g)\circ h=f\circ(g\circ h).
   ]

7. Let (A=\{1,2\}), (B=\{1,2,3,4\}), (C=\{5,6\}) and (D=\{5,6,7,8\}). Verify whether (A\times C) is a subset of (B\times D).

8. If
   [
   f(x)=\frac{x-1}{x+1},\quad x\ne-1,
   ]
   show that
   [
   f(f(x))=-\frac{1}{x},
   ]
   provided (x\ne0).

9. The functions (f) and (g) are defined by
   [
   f(x)=6x+8,\qquad g(x)=\frac{x-2}{3}.
   ]

   1. Calculate the value of
      [
      g\left(g\left(\frac12\right)\right).
      ]
   2. Write an expression for (g f(x)) in its simplest form.

10. Write the domain of the following real functions:

   1. [
      f(x)=\frac{2x+1}{x-9}
      ]
   2. [
      p(x)=\frac{-5}{4x^2+1}
      ]
   3. [
      g(x)=\sqrt{x-2}
      ]
   4. [
      h(x)=x+6
      ]

## Points to Remember

- z The Cartesian Product of A with B is defined as A B a b × = {(,) | for all a \in A, b \in B}
- z A relation R from A to B is always a subset of A \times B . That is R ⊆ × A B
- z A relation R from X to Y is a function if for every x X \in there exists only one y Y \in .
- z A function can be represented by
- (i) an arrow diagram
- (ii) a tabular form
- (iii) a set of ordered pairs
- (iv) a graphical form
- z Some types of functions
- (i) One-one function
- (ii) Onto function
- (iii) Many-one function
- (iv) Into function
- z Identity function \emptyset x x () =
- z Reciprocal function \emptyset x x () = 1

- z Constant function \emptyset x c () =
- z Linear function \emptyset x ax b () = + , a \neq 0
- z Quadratic function \emptyset x ax bx c () = + + 2 , a \neq 0
- z Cubic function \emptyset x ax bx cx d () = + + + 3 2 , a \neq 0
- z For three non-empty sets A , B and C , if \emptyset A B : \\to and g B C : \\to are two functions, then the composition of \emptyset and g is a function g \emptyset A C \\circ : \\to will be defined as g \emptyset x g \emptyset x \\circ () (()) = \emptysetor all x A \in .
- z If \emptyset and g are any two functions, then in general, \emptyset g g \emptyset \\circ  \neq
- z If \emptyset , g and h are any three functions, then \emptyset g h \emptyset g h \\circ  \\circ  () () =

## ICT CORNER

## ICT 1.1

Step 1: Open the Browser type the URL Link given below (or) Scan the QR Code. GeoGebra work book named 'Relations and Functions-X' will open. In the left side of the work book there are many activity related to Relations and Functions chapter. Select the work sheet 'Functions Identification'

Step 2: In the given worksheet click on the check boxes corresponding to each function on left hand side. You can see the graph of respective function on Right hand side. Analyse each graph and then click 'New Functions' and continue till you understand.

## Step 1

## Step 2

## Expected results

## ICT 1.2

Step 1: Open the Browser type the URL Link given below (or) Scan the QR Code. GeoGebra work book named 'Relations and Functions-X' will open. In the left side of the work book there are many activity related to Relations and Functions chapter. Select the work sheet 'Composition of Functions'

Step 2: In the given worksheet click on the check boxes corresponding to each function on left hand side. You can see the graph of respective function on Right hand side. Analyse each graph and then click 'New Functions' and continue till you understand.

You can repeat the same steps for other activities

https://www.geogebra.org/m/jfr2zzgy#chapter/356191 or Scan the QR Code.
