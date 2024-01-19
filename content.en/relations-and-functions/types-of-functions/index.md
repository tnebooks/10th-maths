---
title: 'Types of Functions'
weight: 6
---


# Types of Functions

In this section, we will discuss the following types of functions with suitable examples.

(i) one - one
(ii) many - one
(iii) onto
(iv) into

## One-one Function

Let us assume that we have a cell phone with proper working condition. If you make a usual call to your friend then you can make only one call at a time (Fig.1.21).

If we treat making calls as a function, then it will be one - one. 
  ![Alt text](image-21.png)

A function {{<katex display>}}f: A -> B{{</katex>}} is called one - one function if distinct elements of A have distinct images in B.

A one-one function is also called an injection.

Equivalently,

If for all {{<katex display>}}a_{1}, a_{2} in A, f(a_{1})=f(a_{2}){{</katex>}} implies  {{<katex display>}}a_{1}=a_{2},{{</katex>}} then f is called one - one function. 

**Illustration 10**

{{< katex display >}}
A=\{1,2,3,4\} \text { and } B=\{a, b, c, d, e\}
{{< /katex >}}

(i) Let {{< katex display >}}f={(1, a),(2, b),(3, d),(4, c)}{{< /katex >}}

In Fig. 1.22, for different elements in $A$, there are different images in $B$.
![Alt text](image-22.png)

Hence f is a one - one function.

(ii) Let {{< katex display >}}g={(1, b),(2, b),(3, c),(4, e)}{{< /katex >}}

g is a function from A to B such that {{< katex display >}}g(1)=g(2)=b,{{< /katex >}} but 1 eq 2. Thus two distinct elements 1 and 2 in the first set A have same image b the second set in B (Fig.1.23). Hence, g is not a one-one function.
![Alt text](image-23.png)

##  Many - one function

In a theatre complex three films {{< katex display >}}F_{1}, F_{2}, F_{3}{{< /katex >}} are shown. Seven persons {{< katex display >}}(P_{1} to P_{7}){{< /katex >}} arrive at the theatre and buy tickets as shown (Fig.1.24).

If the selection of films is considered as a relation, then this is a function which is many-one, since more than one person may choose to watch the same film.
![Alt text](image-24.png)
> A function {{< katex display >}}f: A-> B{{< /katex >}} is called many-one function if two or more elements of A have same image in B.

In other words, a function f: A -> B is called many-one if f it is not one-one.

**Illustration 11**
Let {{< katex display >}}A={1,2,3,4}{{< /katex >}} and{{< katex display >}} B={a, b, c}{{< /katex >}}, {{< katex display >}}f={(1, a),(2, a),(3, b),(4, c)}{{< /katex >}}
Then f is a function from A to B in which different elements 1 and 2 of A have the same image a in B. Hence f is a many - one function.

## Onto function

In a mobile phone assume that there are 3 persons in the contact. If every person in the contact receives a call, then the function representing making calls will be onto. (Fig.1.25)

> A function {{< katex display >}}f: A -> B{{< /katex >}} is said to be onto function if the range of f is equal to the co-domain of f.

![Alt text](image-25.png)

In other words, every element in the co-domain B has a pre-image in the domain A.

An onto function is also called a surjection.

> Note: 
> If f: A -> B is an onto function then, the range of f=B.

 **Illustration 12**
Let {{< katex display >}}A={x, y, z}, B={l, m, n};{{< /katex >}}
Range of {{< katex display >}}f={l, m, n}=B{{< /katex >}} (Fig.1.26)

Hence f is an onto function.
![Alt text](image-26.png)
## Into function
In a home appliance showroom, the products television, air conditioner, washing machine and water heater were provided with 20% discount as new year sale offer. If the selection of the above products by the three customers {{< katex display >}}C_{1}, C_{2}, C_{3} {{< /katex >}}is considered as a function then the following diagram (Fig.1.27) will represent an into function.
![Alt text](image-27.png)
During winter season customers usually do not prefer buying air conditioner. Here air conditioner is not chosen by any customer. This is an example of into function.

A function {{< katex display >}}f: A -> B{{< /katex >}} is called an into function if there exists atleast one element in B which is not the image of any element of A.

That is the range of f is a proper subset of the co-domain of f.

In other words, a function f: A -> B is called 'into' if it is not 'onto'.

**Illustration 13**
Let {{< katex display >}}A={1,2,3,4}{{< /katex >}} and{{< katex display >}} B={w, x, y, z},{{< /katex >}} {{< katex display >}}f={(1, w),(2, z),(3, x)}{{< /katex >}}

Here, range of {{< katex display >}}f={w, x, z}{{< /katex >}}  subset B(Fig.1.28)

therefore f is a into function.

Note that y in B is not an image of any element in A.
![Alt text](image-28.png)

## Bijection

Consider the circle where each letter of the English alphabet is changed from inner portion to a letter in the outer portion. Thus A -> D, B -> E, C -> F, Z -> C. We call this circle as 'cipher circle'. (Fig.1.29) In this way if we try to change the word 'HELLO' then it will become 'KHOOR'. Now using the same circle if we substitute for each outer letter the corresponding inner letter we will get back the word 'HELLO'. 
![Alt text](image-29.png)
This process of converting Fig. 1.29 from one form to an other form and receiving back the required information is called bijection. This process is widely used in the study of secret codes called cryptography.

> If a function f: A -> B is both one-one and onto, then f is called a bijection from A to B.

Illustration 14

| one to one and onto function (Bijection) |  
| :--- | 
|   Distinct elements of A have distinct images<br> in B and every element in B has a pre-image <br> in A.  
 ![Alt text](image-30.png)| 

Illustration 15

![Alt text](image-31.png)
>Note
>A one - one and onto function is also called a one-one correspondence.

> Thinking Corner
> Can there be a one to many function?

![Alt text](image-32.png)
To determine whether the given function is one-one or not the following test may help us.

## Horizontal Line Test

Previously we have seen the vertical line test. Now let us see the horizontal line test. "A function represented in a graph is one-one, if every horizontal line intersects the curve in at most one point".

Example 1.12 Using horizontal line test (Fig. 1.35 (a), 1.35 (b), 1.35 (c)), determine which of the following functions are one - one.
![Alt text](image-33.png)![Alt text](image-34.png) ![Alt text](image-35.png)

Solution The curves in Fig.1.35 (a) and Fig.1.35 (c) represent a one-one function as the horizontal lines meet the curves in only one point P.

The curve in Fig. 1.35 (b) does not represent a one-one function, since, the horizontal line intersects the curve at two points P and Q.

Example 1.13 Let {{< katex display >}}A={1,2,3},{{< /katex >}} {{< katex display >}}B={4,5,6,7} {{< /katex >}}and {{< katex display >}}f={(1,4),(2,5),(3,6)}{{< /katex >}} be a function from A to B. Show that f is one - one but not onto function.

Solution {{< katex display >}}A={1,2,3},{{< /katex >}} {{< katex display >}}B={4,5,6,7} {{< /katex >}}; {{< katex display >}}f={(1,4),(2,5),(3,6)}{{< /katex >}}

Then f is a function from A to B and for different elements in A, there are different images in B. Hence f is one-one function. Note that the element 7 in the co-domain does not have any pre-image in the domain. Hence f is not onto (Fig.1.36). 
![Alt text](image-36.png)

therefore f is one-one but not an onto function.

Example 1.14 If {{< katex display >}}A={-2,-1,0,1,2} {{< /katex >}}and {{< katex display >}}f: A -> B{{< /katex >}} is an onto function defined by {{< katex display >}}f(x)=x^{2}+x+1{{< /katex >}} then find B.

Solution Given {{< katex display >}} A={-2,-1,0,1,2}{{< /katex >}} and {{< katex display >}}f(x)=x^{2}+x+1.{{< /katex >}}

{{< katex display >}}
\begin{aligned}
f(-2) & =(-2)^{2}+(-2)+1=3 ; \\
f(-1) & =(-1)^{2}+(-1)+1=1 \\
f(0) & =0^{2}+0+1=1 ; \\
f(1) & =1^{2}+1+1=3 \\
f(2) & =2^{2}+2+1=7 \\
\therefore B & =\{1,3,7\} .
\end{aligned}
{{< /katex >}}

**Example 1.15** Let f be a function {{< katex display >}}f: b{N} -> b{N}{{< /katex >}} be defined by {{< katex display >}}f(x)=3 x+2, x in b{N}{{< /katex >}}

(i) Find the images of 1, 2,3

(ii) Find the pre-images of 29, 53

(ii) Identify the type of function

**Solution** The function {{< katex display >}}f: b{N} -> b{N}{{< /katex >}} is defined by {{< katex display >}}f(x)=3 x+2{{< /katex >}}

(i) If x=1, {{< katex display >}} f(1)=3(1)+2=5{{< /katex >}}

If x=2, {{< katex display >}}f(2)=3(2)+2=8{{< /katex >}}

If x=3, {{< katex display >}}f(3)=3(3)+2=11{{< /katex >}}

The images of 1, 2, 3 are 5, 8, 11 respectively.

(ii) If x is the pre-image of 29 , then f(x)=29. Hence {{< katex display >}}3x+2=29{{< /katex >}}

{{< katex display >}}3x=27 -> x=9.{{< /katex >}}

Similarly, if x is the pre-image of 53 , then {{< katex display >}}f(x)=53.{{< /katex >}} Hence 3x+2=53

3x=51 -> x=17.

Thus the pre-images of 29 and 53 are 9 and 17 respectively.

(iii) Since different elements of b{N} have different images in the co-domain, the function f is one - one function.

The co-domain of f is b{N}.

But the range of {{< katex display >}}f={5,8,11,14,17, ldots} {{< /katex >}}is a proper subset of N.

therefore f is not an onto function. That is, f is an into function.

Thus f is one - one and into function.

Example 1.16 Forensic scientists can determine the height (in cm) of a person based on the length of the thigh bone. They usually do so using the function {{< katex display >}}h(b)=2.47 b+54.10{{< /katex >}} where b is the length of the thigh bone.

(i) Verify the function h is one - one or not.

(ii) Also find the height of a person if the length of his thigh bone is 50 cm.

(iii) Find the length of the thigh bone if the height of a person is 147.96cm.

Solution (i) To check if h is one - one, we assume that {{< katex display >}}h(b_{1})=h(b_{2}).{{< /katex >}}

Then we get, {{< katex display >}}2.47 b_{1}+54.10=2.47 b_{2}+54.10{{< /katex >}}

{{< katex display >}}
\begin{aligned}
2 \cdot 47 b_{1} & =2 \cdot 47 b_{2} \\
\Rightarrow b_{1} & =b_{2}
\end{aligned}
{{< /katex >}}

Thus, {{< katex display >}}ht(b_{1})=h(b_{2}) -> b_{1}=b_{2}.{{< /katex >}} So, the function h is one - one.

(ii) If the length of the thigh bone b=50, then the height is {{< katex display >}}h(50)=(2.47x50)+54.10=177.6cm.{{< /katex >}}

(iii) If the height of a person is 147.9cm, then {{< katex display >}}h(b)=147.96{{< /katex >}} and so the length of the thigh bone is given by

{{< katex display >}}
\begin{aligned}
2 \cdot 47 b+54 \cdot 10 & =147 \cdot 96 \\
\Rightarrow 2 \cdot 47 b & =147 \cdot 96-54 \cdot 10=93 \cdot 86 \\
b & =\frac{93 \cdot 86}{2 \cdot 47}=38
\end{aligned}
{{< /katex >}}

Therefore, the length of the thigh bone is 38cm .

![Alt text](image-37.png)

