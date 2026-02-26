---
title: 'Types of Functions'
weight: 6
---


## 1.7 Types of Functions

In this section, we will discuss the following types of functions with suitable examples:
- (i) one – one
- (ii) many – one
- (iii) onto
- (iv) into

---

## 1.7.1 One – one function

Let us assume that we have a cell phone with proper working condition. If you make a usual call to your friend then you can make only one call at a time.


![](image-21.png)


If we treat making calls as a function, then it will be **one-one**.

A function f: A → B is called **one – one function** if **distinct elements of A have distinct images in B**.

A one-one function is also called an **injection**.

Equivalently, if for all a₁, a₂ ∈ A, f(a₁) = f(a₂) implies a₁ = a₂, then f is called **one – one function**.

---

### Illustration 10

A = {1, 2, 3, 4} and B = {a, b, c, d, e}

**(i)** Let f = {(1,a), (2,b), (3,d), (4,c)}

![](image-22.png)


In Fig. 1.22, for different elements in A, there are different images in B.

Hence f is a **one – one function**.

**(ii)** Let g = {(1,b), (2,b), (3,c), (4,e)}


![](image-23.png)


g is a function from A to B such that g(1) = g(2) = b, but 1 ≠ 2. Thus two distinct elements 1 and 2 in the first set A have same image b in the second set in B. Hence, **g is not a one – one function**.

---

## 1.7.2 Many – one function

In a theatre complex three films F₁, F₂, F₃ are shown. Seven persons (P₁ to P₇) arrive at the theatre and buy tickets.

If the selection of films is considered as a relation, then this is a function which is **many–one**, since more than one person may choose to watch the same film.


![](image-24.png)


A function f: A → B is called **many-one function** if **two or more elements of A have same image in B**.

In other words, a function f: A → B is called many-one if it is **not one – one**.

---

### Illustration 11

Let A = {1, 2, 3, 4} and B = {a, b, c}, f = {(1,a), (2,a), (3,b), (4,c)}

Then f is a function from A to B in which different elements 1 and 2 of A have the same image a in B. Hence f is a **many – one function**.

---

## 1.7.3 Onto function

In a mobile phone assume that there are 3 persons in the contact. If every person in the contact receives a call, then the function representing making calls will be **onto**.


![](image-25.png)


A function f: A → B is said to be **onto function** if **the range of f is equal to the co-domain of f**.

In other words, **every element in the co-domain B has a pre-image in the domain A**.

An onto function is also called a **surjection**.

---

### Note

If f: A → B is an onto function then, the range of f = B

---

### Illustration 12

Let A = {x, y, z}, B = {l, m, n}; Range of f = {l, m, n} = B


![](image-26.png)

Hence f is an **onto function**.

---

## 1.7.4 Into function

In a home appliance showroom, the products television, air conditioner, washing machine and water heater were provided with 20% discount as new year sale offer. If the selection of the above products by the three customers C₁, C₂, C₃ is considered as a function then the following diagram will represent an **into function**.


![](image-27.png)


During winter season customers usually do not prefer buying air conditioner. Here air conditioner is not chosen by any customer. This is an example of **into function**.

A function f: A → B is called an **into function** if **there exists at least one element in B which is not the image of any element of A**.

That is the **range of f is a proper subset of the co-domain of f**.

In other words, a function f: A → B is called 'into' if it is **not 'onto'**.

---

### Illustration 13

Let A = {1, 2, 3} and B = {w, x, y, z}, f = {(1,w), (2,z), (3,x)}

Here, range of f = {w, x, z} ⊂ B

![](image-28.png)


∴ f is a **into function**.

Note that y ∈ B is not an image of any element in A.

---

## 1.7.5 Bijection

Consider the circle where each letter of the English alphabet is changed from inner portion to a letter in the outer portion. Thus A → D, B → E, C → F, ... Z → C. We call this circle as **'cipher circle'**. In this way if we try to change the word 'HELLO' then it will become 'KHOOR'. Now using the same circle if we substitute for each outer letter the corresponding inner letter we will get back the word 'HELLO'. This process of converting from one form to another form and receiving back the required information is called **bijection**. This process is widely used in the study of secret codes called **cryptography**.


![](image-29.png)


If a function f: A → B is **both one – one and onto**, then f is called a **bijection** from A to B.

---

### Illustration 14

**One to one and onto function (Bijection)**

![](image-30.png)

Distinct elements of A have distinct images in B and every element in B has a pre-image in A.

---

### Illustration 15
![](image-31.png)

---

### Note

A one – one and onto function is also called a **one – one correspondence**.

---

### Thinking Corner

**Can there be a one to many function?**

---
![](image-32.png)

---

To determine whether the given function is one – one or not the following test may help us.

---

## 1.7.6 Horizontal Line Test

Previously we have seen the vertical line test. Now let us see the horizontal line test.

**"A function represented in a graph is one – one, if every horizontal line intersects the curve at only one point".**

---

### Example 1.12

Using horizontal line test (Fig. 1.35(a), 1.35(b), 1.35(c)), determine which represent one-one function?

![](image-33.png)
![](image-34.png)
![](image-35.png)

**Solution**

The curves in **Fig. 1.35(a)** and **Fig. 1.35(c)** represent a **one – one function** as the horizontal lines meet the curves in only one point P.

The curve in **Fig. 1.35(b)** does **not** represent a **one – one function**, since the horizontal line intersects the curve at two points P and Q.

---

### Example 1.13

Let A = {1, 2, 3}, B = {4, 5, 6, 7} and f = {(1,4), (2,5), (3,6)} be a function from A to B. Show that f is one – one but not onto function.

![](image-36.png)

**Solution**

A = {1, 2, 3}, B = {4, 5, 6, 7}; f = {(1,4), (2,5), (3,6)}

Then f is a function from A to B and for different elements in A, there are different images in B. Hence f is **one – one function**.

Note that the element 7 in the co-domain does not have any pre-image in the domain. Hence f is **not onto**.

∴ **f is one – one but not an onto function.**

---

### Example 1.14

If A = {-2, -1, 0, 1, 2} and f: A → B is an onto function defined by f(x) = x² + x + 1 then find B.

**Solution**

Given A = {-2, -1, 0, 1, 2} and f(x) = x² + x + 1.

- f(-2) = (-2)² + (-2) + 1 = 4 - 2 + 1 = **3**
- f(-1) = (-1)² + (-1) + 1 = 1 - 1 + 1 = **1**
- f(0) = 0² + 0 + 1 = **1**
- f(1) = 1² + 1 + 1 = **3**
- f(2) = 2² + 2 + 1 = 4 + 2 + 1 = **7**

∴ **B = {1, 3, 7}**

---

### Example 1.15

Let f be a function f: ℕ → ℕ be defined by f(x) = 3x + 2, x ∈ ℕ

(i) Find the images of 1, 2, 3
(ii) Find the pre-images of 29, 53
(iii) Identify the type of function

**Solution**

The function f: ℕ → ℕ is defined by f(x) = 3x + 2

**(i)** 
- If x = 1, f(1) = 3(1) + 2 = **5**
- If x = 2, f(2) = 3(2) + 2 = **8**
- If x = 3, f(3) = 3(3) + 2 = **11**

The images of 1, 2, 3 are **5, 8, 11** respectively.

**(ii)** If x is the pre-image of 29, then f(x) = 29.

3x + 2 = 29
3x = 27
**x = 9**

Similarly, if x is the pre-image of 53, then f(x) = 53.

3x + 2 = 53
3x = 51
**x = 17**

Thus the pre-images of 29 and 53 are **9** and **17** respectively.

**(iii)** Since different elements of ℕ have different images in the co-domain, the function f is **one – one function**.

The co-domain of f is ℕ. But the range of f = {5, 8, 11, 14, 17, ...} is a proper subset of ℕ.

∴ f is **not an onto function**. That is, f is an **into function**.

Thus **f is one – one and into function**.

---

### Example 1.16

Forensic scientists can determine the height (in cm) of a person based on the length of the thigh bone. They usually do so using the function h(b) = 2.47b + 54.10 where b is the length of the thigh bone.

(i) Verify the function h is one – one or not.
(ii) Also find the height of a person if the length of his thigh bone is 50 cm.
(iii) Find the length of the thigh bone if the height of a person is 147.96 cm.

**Solution**

**(i)** To check if h is one – one, we assume that h(b₁) = h(b₂).

Then we get:
2.47b₁ + 54.10 = 2.47b₂ + 54.10
2.47b₁ = 2.47b₂
**b₁ = b₂**

Thus, h(b₁) = h(b₂) ⇒ b₁ = b₂. So, the function h is **one – one**.

**(ii)** If the length of the thigh bone b = 50, then the height is:
h(50) = (2.47 × 50) + 54.10 = 123.5 + 54.10 = **177.6 cm**

**(iii)** If the height of a person is 147.96 cm, then h(b) = 147.96 and so the length of the thigh bone is given by:

2.47b + 54.10 = 147.96
2.47b = 147.96 - 54.10 = 93.86
b = 93.86/2.47 = **38**

Therefore, the length of the thigh bone is **38 cm**.

---

### Activity 3
![](image-37.png)


---