---
title: 'Functions'
weight: 4
---


# Functions

Among several relations that exist between two non-empty sets, some special relations are important for further exploration. Such relations are called“Functions”. 
![alt text](image1-11.png)

**Illustration 8**

A company has 5 employees in different categories. If we consider their salary distribution for a month as shown by arrow diagram in Fig.1.11, we see that there is only one salary associated for every employee of the company.

Here are various real life situations illustrating some special relations:

* Consider the set A of all of your classmates; corresponding to each student, there is only one age.
* You go to a shop to buy a book. If you take out a book, there is only one price corresponding to it; it does not have two prices corresponding to it. (of course, many books may have the same price).
* You are aware of Boyle’s law. Corresponding to a given value of pressure P, there is only one value of volume V.
* In Economics, the quantity demanded can be expressed as {{<katex display>}}Q = 360−4P{{</katex>}} , where P is the price of the commodity. We see that for each value of P, there is only one value of Q. Thus the quantity demanded Q depend on the price P of the commodity.

We often come across certain relations, in which, for each element of a set A, there is only one corresponding element of a set B. Such relations are called functions. We usually use the symbol f to denote a functional relation.       
![alt text](image12a.png)
> Definition
> A relation f between two non-empty sets X and Y is called a
function from X to Y if, for each x ∈  X there exists only one {{<katex display>}}y ∈ Y{{</katex>}}
such that {{<katex display>}}(x,y) ∈  f{{</katex>}}
That is, {{<katex display>}}f ={(x,y)| for all x ∈  X, y ∈ Y }.{{</katex>}}

A function f from X to Y is written as f : X -> Y . 

 ![alt text](image1-12b.png)
Comparing the definitions of relation and function, we see that
every function is a relation. Thus, functions are subsets of relations
and relations are subsets of cartesian product. (Fig.1.12(a))

A function f can be thought as a mechanism (or device) (Fig.1.12(b)), which gives a unique output f(x) to every input x.

> Definition
>A function is also called as a mapping or transformation.


> Note
> If f : X ->Y is a function then 
> * The set X is called the domain of the function f and the set Y is called its co-domain.
> * If {{<katex display>}}f (a) = b,{{</katex>}} then b is called ‘image’ of a under f and a is called a ‘pre-image’ of b.  
>* The set of all images of the elements of X under f is called the ‘range’ of f.
> * {{<katex display>}}f : X ®Y{{</katex>}} is a function only if
(i) every element in the domain of f has an image.
(ii) the image is unique.
>* If A and B are finite sets such that {{<katex display>}}n(A) = p , n(B) = q{{</katex>}} then the total number of functions that exist from A to B is {{<katex display>}}q^p.{{</katex>}}
> * In this chapter we always consider f to be a real valued function.

![Alt text](image-7.png)

 Illustration 9 - Testing for functions

Representation by Arrow diagram 

![Alt text](image-11.png)

Functions play very important role in the understanding of higher ideas in mathematics. They are basic tools to convert from one form to another form. In this sense, functions are widely applied in Engineering Sciences.

> Note
> The range of a function is a subset of its co-domain.

**Example 1.6** Let {{<katex display>}}X = {1,2, 3, 4}{{</katex>}} and {{<katex display>}}Y = {2, 4,6, 8,10} {{</katex>}}and {{<katex display>}}R = {(1,2),(2,4),(3,6),(4,8)}.{{</katex>}}
Show that R is a function and find its domain, co-domain and range?

Solution: Pictorial representation of R is given in Fig.1.14. From the diagram, we see that for each {{<katex display>}}x ∈ X{{</katex>}} , there exists only one {{<katex display>}}y ∈ Y{{</katex>}} . Thus all elements in X have only one image in Y. Therefore R is a function. Domain {{<katex display>}}X = {1,2,3,4}{{</katex>}}; Co-domain {{<katex display>}}Y = {2,4,6,8,10};{{</katex>}} Range of {{<katex display>}}f = {2,4,6,8}.{{</katex>}}

**Example 1.7**  A relation {{<katex display>}}f :X →Y {{</katex>}}is defined by {{<katex display>}}f (x) =x2 −2{{</katex>}} where, {{<katex display>}}X = {−2,−1, 0, 3} {{</katex>}}and {{<katex display>}}Y = R.{{</katex>}}
(i) List the elements of f (ii) Is f a function?
Solution{{<katex display>}} f (x) = x^2 – 2{{</katex>}} where {{<katex display>}}X = {−2,−1, 0, 3}{{</katex>}}
(i) {{<katex display>}}f (-2) = (−2)2 – 2 = 2 ; f (-1) = (−1)2 – 2 = −1{{</katex>}}
{{<katex display>}}f (0) = (0)2 – 2 = −2 ; f (3) =(3)^2 – 2 =7{{</katex>}}
{{<katex display>}}∴ f = {(−2,2),(−1,−1),(0,−2),(3,7)}{{</katex>}}
(ii) We note that each element in the domain of f has a unique image.
Therefore, f is a function.

> Thinking Corner
> Is the relation representing the association between planets and their respective moons
a function?

Example 1.8 If {{< katex display >}}X = {–5,1,3,4}{{< /katex >}} and {{< katex display >}}Y = {a,b,c},{{< /katex >}} then which of the following relations are
functions from {{< katex display >}}X to Y ?{{< /katex >}}

(i) {{< katex display >}}R_{1}={(-5, a),(1, a),(3, b)}{{< /katex >}}  (ii) {{< katex display >}}R_{2}={(-5, b),(1, b),(3, a),(4, c)}{{< /katex >}}

(iii) {{< katex display >}}R_{3}={(-5, a),(1, a),(3, b),(4, c),(1, b)}{{< /katex >}}

 Solution : 


(i) {{< katex display >}}quad R_{1}={(-5, a),(1, a),(3, b)}{{< /katex >}}

We may represent the relation {{< katex display >}}R_{1}{{< /katex >}} in an arrow diagram (Fig.1.15(a)).
![Alt text](image-12.png)
![Alt text](image-13.png)
![Alt text](image-14.png)

{{< katex display >}}R_{1}{{< /katex >}} is not a function as 4 in X does not have an image in Y.

(ii) {{< katex display >}}R_{2}={(-5, b),(1, b),(3, a),(4, c)}{{< /katex >}}

Arrow diagram of {{< katex display >}}R_{2}{{< /katex >}} is shown in Fig.1.15(b).

{{< katex display >}}R_{2}{{< /katex >}} is a function as each element of X has an unique image in Y.

(iii) {{< katex display >}}R_{3}={(-5, a),(1, a),(3, b),(4, c),(1, b)}{{< /katex >}}

Representing {{< katex display >}}R_{3}{{< /katex >}} in an arrow diagram (Fig.1.15(c)).

{{< katex display >}}R_{3}{{< /katex >}} is not a function as 1 in X has two images {{< katex display >}}a in Y {{< /katex >}}and {{< katex display >}}b in Y.{{< /katex >}}

Note that the image of an element should always be unique.

Example 1.9 Given {{< katex display >}}f(x)=2 x-x^{2},{{< /katex >}}

{{< katex display >}}
\text { find (i) } f(1) \text { (ii) } f(x+1) \text { (iii) } f(x)+f(1)
{{< /katex >}}

Solution (i) {{< katex display >}}x=1,{{< /katex >}} we get

{{< katex display >}}
f(1)=2(1)-(1)^{2}=2-1=1
{{< /katex >}}

(ii) {{< katex display >}}x=x+1,{{< /katex >}} we get

{{< katex display >}}
f(x+1)=2(x+1)-(x+1)^{2}=2 x+2-\left(x^{2}+2 x+1\right)=-x^{2}+1
{{< /katex >}}

(iii) {{< katex display >}}f(x)+f(1)=\left(2 x-x^{2}\right)+1=-x^{2}+2 x+1{{< /katex >}}

[Note that {{< katex display >}}f(x)+f(1) \neq f(x+1).{{< /katex >}} In general {{< katex display >}}f(a+b) {{< /katex >}}is not equal to{{< katex display >}} f(a)+f(b) ]{{< /katex >}}

Exercise 1.3

1. Let {{< katex display >}}f={(x, y)  x, y  N and y=2 x} {{< /katex >}}be a relation on N. Find the domain, co-domain and range. Is this relation a function?
2. Let {{< katex display >}}X={3,4,6,8}.{{< /katex >}} Determine whether the relation {{< katex display >}}R=\left\{(x, f(x)) \mid x \in X, f(x)=x^{2}+1\right\} {{< /katex >}}is a function from X to N ?
3. Given the function{{< katex display >}}f: x \rightarrow x^{2}-5 x+6{{< /katex >}}, evaluate
(i) {{< katex display >}}f(-1){{< /katex >}}
(ii) {{< katex display >}}f(2 a){{< /katex >}}
(iii) {{< katex display >}}f(2){{< /katex >}}
(iv) {{< katex display >}}f(x-1){{< /katex >}}
4. A graph representing the function {{< katex display >}}f(x){{< /katex >}} is given in Fig.1.16 it is clear that {{< katex display >}}f(9)=2.{{< /katex >}}

(i) Find the following values of the function
(a) {{< katex display >}}f(0){{< /katex >}}
(b) {{< katex display >}}f(7){{< /katex >}}
(c) {{< katex display >}}f(2){{< /katex >}}
(d) {{< katex display >}}f(10){{< /katex >}}

(ii) For what value of {{< katex display >}}x  is f(x)=1 ?{{< /katex >}}

(iii) Describe the following (i) Domain (ii) Range.

![Alt text](image-15.png)
![Alt text](image-16.png)

7. An open box is to be made from a square piece of material,  {{< katex display >}}24 \mathrm{~cm}{{< /katex >}} on a side, by cutting equal squares from the corners and turning up the sides as shown (Fig.1.17). Express the volume V of the box as a function of x.
8. A function f is defined by {{< katex display >}}f(x)=3-2 x.{{< /katex >}} Find x such that {{< katex display >}}f\left(x^{2}\right)=(f(x))^{2}{{< /katex >}}
9. A plane is flying at a speed of {{< katex display >}}500 \mathrm{~km}{{< /katex >}} per hour. Express the distance ' d ' travelled by the plane as function of time t in hours.
10. The data in the adjacent table depicts the length of a person forehand and their corresponding height. Based on this data, a student finds a

| Length ‘x’ of forehand (in cm) | Height ‘y’ (in inches) |
|----------|----------|
| 35| 56 |
|45 | 65 |
| 50 | 69.5 | 
|55 | 74 |

(i) Check if this relation is a function.

(ii) Find a and b.
14) {{< katex display >}}10^{\text {th }}{{< /katex >}} Standard Mathematics
(iii) Find the height of a person whose forehand length is {{< katex display >}}40 \mathrm{~cm}.{{< /katex >}}
(iv) Find the length of forehand of a person if the height is 53.3 inches.


























