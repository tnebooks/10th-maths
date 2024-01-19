---
title: 'Special Cases of Functions'
weight: 7
---


# Special Cases of Functions

There are some special cases of a function which will be very useful. We discuss some of them below

(i) Constant function
(ii) Identity function
(iii) Real - valued function

(i) Constant function
A function {{< katex display >}}f: A \rightarrow B{{< /katex >}} is called a constant function if the range of {{< katex display >}}f{{< /katex >}} contains only one element. That is, {{< katex display >}}f(x)=c{{< /katex >}}, for all {{< katex display >}}x \in A{{< /katex >}} and for some fixed {{< katex display >}}c \in B{{< /katex >}}.

**Illustration 16**

From Fig.1.37, {{< katex display >}}A=\{a, b, c, d\}, B=\{1,2,3\}{{< /katex >}} and {{< katex display >}}f=\{(a, 3),(b, 3),(c, 3),(d, 3)\} . \because f(x)=3 \forall x \in A{{< /katex >}}Range of {{< katex display >}}f=\{3\} f{{< /katex >}} is a constant function.
![Alt text](image-38.png)

(ii) Identity function

Let A be a non-empty set. Then the function f: A -> A defined by f(x)=x for all  {{< katex display >}}x \in A{{< /katex >}} is called an identity function on A and is denoted by {{< katex display >}} I_{\mathrm{A}}{{< /katex >}}
![Alt text](image-39.png) 

**Illustration 17**

If   {{< katex display >}}A=\{a, b, c\}{{< /katex >}} then  {{< katex display >}}f=I_{A}=\{(a, a),(b, b),(c, c)\}{{< /katex >}} is an identity function on A.

(iii) Real valued function

> **Thinking Corner**
>Is an identity function one to one function?
>A function  {{< katex display >}}f: A \rightarrow B{{< /katex >}} is called a real valued function if the range of f is a subset of the set of all real numbers  {{< katex display >}}\mathbb{R}{{< /katex >}}. That is,  {{< katex display >}}f(a) \subseteq \mathbb{R}, \forall a \in A{{< /katex >}}.

>Progress Check
>State True or False.
>1. All one - one functions are onto functions.
>2. There will be no one - one function from A to B when n(A)=4, n(B)=3.
>3. All onto functions are one - one functions.
>4. There will be no onto function from A to B when n(A)=4, n(B)=5.
>5. If f is a bijection from A to B, then n(A)=n(B).
>6. If n(A)=n(B), then f is a bijection from A to B.
>7. All constant functions are bijections.

**Example 1.17** Let f be a function from R to R defined by {{< katex display >}}f(x)=3 x-5.{{< /katex >}} Find the values of a and b given that {{< katex display >}}(a, 4){{< /katex >}} and {{< katex display >}}(1, b){{< /katex >}} belong to f.

Solution {{< katex display >}}f(x)=3 x-5{{< /katex >}} can be written as {{< katex display >}}f=\{(x, 3 x-5) \mid x \in R\}{{< /katex >}}

{{< katex display >}}(a, 4){{< /katex >}} means the image of a is 4 . i.e., {{< katex display >}}f(a)=4{{< /katex >}}


{{< katex display >}}
3 \mathrm{a}-5=4 \Rightarrow a=3
{{< /katex >}}

(1, b) means the image of 1 is b. i.e., f(1)=b

{{< katex display >}}
3(1)-5=b \Rightarrow b=-2
{{< /katex >}}

**Example 1.18**
 If the function {{< katex display >}}f: \mathbb{R} \rightarrow \mathbb{R}{{< /katex >}} is defined by {{< katex display >}}f(x)=\left\{\begin{array}{cc}2 x+7 ; & x<-2 \\ x^{2}-2 ; & -2 \leq x<3 \\ 3 x-2 ; & x \geq 3\end{array}\right.{{< /katex >}}
(i) {{< katex display >}}f(4){{< /katex >}}
(ii) {{< katex display >}}f(-2){{< /katex >}}
(iii) {{< katex display >}}f(4)+2 f(1){{< /katex >}}
(iv) {{< katex display >}}\frac{f(1)-3 f(4)}{f(-3)}{{< /katex >}}

**Solution**

The function f is defined by three values in intervals I, II, III as shown by the side
![Alt text](image-40.png) 
For a given value of x=a, find out the interval at which the point a is located, there after find f(a) using the particular value defined in that interval.

(i) First, we see that, {{< katex display >}}x=4{{< /katex >}} lie in the third interval.

{{< katex display >}}\therefore f(x)=3 x-2 ; f(4)=3(4)-2=10{{< /katex >}}

(ii) {{< katex display >}}x=-2{{< /katex >}} lies in the second interval.

{{< katex display >}} \therefore f(x)=x^{2}-2 ; f(-2)=(-2)^{2}-2=2{{< /katex >}}

(iii) From (i), {{< katex display >}}f(4)=10{{< /katex >}}.

To find f(1), first we see that x=1 lies in the second interval.

{{< katex display >}}
\begin{aligned}
\therefore f(x)=x^{2}-2 & \Rightarrow f(1)=1^{2}-2=-1 \\
f(4)+2 f(1) & =10+2(-1)=8
\end{aligned}
{{< /katex >}}

(iv) We know that{{< katex display >}}f(1)=-1{{< /katex >}} and {{< katex display >}}f(4)=10.{{< /katex >}}

For finding {{< katex display >}}f(-3),{{< /katex >}} we see that{{< katex display >}} x=-3,{{< /katex >}} lies in the first interval.

therefore {{< katex display >}}f(x)=2 x+7;{{< /katex >}} thus, {{< katex display >}}f(-3)=2(-3)+7=1{{< /katex >}}
{{< katex display >}}
Hence,  \quad \frac{f(1)-3 f(4)}{f(-3)}=\frac{-1-3(10)}{1}=-31
{{< /katex >}}
**Exercise 1.4**

1. Determine whether the graph given below represent functions. Give reason for your answers concerning each graph.

 ![Alt text](image-41.png)
2. Let f: A -> B be a function defined by {{< katex display >}}f(x)=\frac{x}{2}-1{{< /katex >}}, where {{< katex display >}}A={2,4,6,10,12}, B={0,1,2,4,5,9}.{{< /katex >}} Represent f by
(i) set of ordered pairs
(ii) a table
(iii) an arrow diagram
(iv) a graph
3. Represent the function {{< katex display >}}f={(1,2),(2,2),(3,2),(4,3),(5,4)}{{< /katex >}} through
(i) an arrow diagram
(ii) a table form
(iii) a graph
4. Show that the function {{< katex display >}}f: \mathbb{N} \rightarrow \mathbb{N}{{< /katex >}} defined by {{< katex display >}}f(x)=2x-1{{< /katex >}} is one-one but not onto.
5. Show that the function {{< katex display >}}f: \mathbb{N} \rightarrow \mathbb{N}{{< /katex >}} defined by {{< katex display >}}f(m)=m^{2}+m+3{{< /katex >}} is one-one function.
6. Let {{< katex display >}}A=\{1,2,3,4\}{{< /katex >}} and {{< katex display >}}B=\mathbb{N}{{< /katex >}}. Let {{< katex display >}}f: A \rightarrow B{{< /katex >}} be defined by {{< katex display >}}f(x)=x^{3}{{< /katex >}} then,
(i) find the range of f
(ii) identify the type of function
7. In each of the following cases state whether the function is bijective or not. Justify your answer.
(i) {{< katex display >}}f: \mathbb{R} \rightarrow \mathbb{R}{{< /katex >}} defined by {{< katex display >}}f(x)=2 x+1{{< /katex >}}
(ii) {{< katex display >}}f: \mathbb{R} \rightarrow \mathbb{R}{{< /katex >}} defined by {{< katex display >}}f(x)=3-4 x^{2}{{< /katex >}}
8. Let A={-1,1} and B={0,2}. If the function {{< katex display >}}f: A \rightarrow B{{< /katex >}} defined by {{< katex display >}}f(x)=a x+b{{< /katex >}} is an onto function? Find a and b.
9. If the function f is defined by {{< katex display >}} f(x)=\left\{\begin{array}{ll}x+2 ; & x>1 \\ 2 ; & -1 \leq x \leq 1 \\ x-1 ; & -3<x<-1\end{array}\right.{{< /katex >}} find the values of
(i) {{< katex display >}}f(3){{< /katex >}}
(ii) {{< katex display >}}f(0){{< /katex >}}
(iii) {{< katex display >}}f(-1 \cdot 5){{< /katex >}}
(iv) {{< katex display >}}f(2)+f(-2){{< /katex >}}
10. A function {{< katex display >}}f:[-5,9] \rightarrow \mathbb{R}{{< /katex >}} is defined as follows:
{{< katex display >}}
f(x)=\left\{\begin{array}{lr}6 x+1 ; & -5 \leq x<2 \\ 5 x^{2}-1 ; & 2 \leq x<6 \\ 3 x-4 ; & 6 \leq x \leq 9\end{array}\right.
{{< /katex >}}
Find
(i) {{< katex display >}}f(-3)+f(2){{< /katex >}}
(ii) {{< katex display >}}f(7)-f(1){{< /katex >}}
(iii) {{< katex display >}}2 f(4)+f(8){{< /katex >}}
(iv) {{< katex display >}}\frac{2 f(-2)-f(6)}{f(4)+f(-2)}{{< /katex >}}

11. The distance S an object travels under the influence of gravity in time t seconds is given by {{< katex display >}}S(t)=\frac{1}{2} g t^{2}+a t+b{{< /katex >}} where, ( g is the acceleration due to gravity), a, b are constants. Verify wheather the function S(t) is one-one or not.
12. The function ' t ' which maps temperature in Celsius (C) into temperature in Fahrenheit (F) is defined by {{< katex display >}}t(C)=F{{< /katex >}} where {{< katex display >}}F=\frac{9}{5} C+32{{< /katex >}}. Find,
(i) {{< katex display >}}t(0){{< /katex >}}
(ii) {{< katex display >}}t(28){{< /katex >}}
(iii) {{< katex display >}}t(-10){{< /katex >}}

(iv) the value of C when {{< katex display >}}t(C)=212{{< /katex >}}

(v) the temperature when the Celsius value is equal to the Farenheit value. 

