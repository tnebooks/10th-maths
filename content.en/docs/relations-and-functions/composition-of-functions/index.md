---
title: 'Composition of Functions'
weight: 8
---

<<<<<<< HEAD
## 1.9 Composition of Functions

When a car driver depresses the accelerator pedal, it controls the flow of fuel which in turn influences the speed of the car. Likewise, the **composition of two functions** is a kind of 'chain reaction', where the functions act upon one 
after another.


![](image-42.png)


We can explain this further with the concept that a function is a 'process'. If f and g are two functions then the composition g(f(x)) is formed in two steps:
1. Feed an input (say x) to f;
2. Feed the output f(x) to g to get g(f(x)) and call it g∘f(x).

---

### Illustration

Consider the set A of all students, who appeared in class X of Board Examination. Each student appearing in the Board Examination is assigned a roll number. In order to have confidentiality, the Board arranges to deface the roll number of each student and assigns a code number to each roll number.


![](image-43.png)


Let A be the set of all students appearing for the board exam. B ⊆ ℕ be the set all roll numbers and C ⊆ ℕ be the set of all code numbers. This gives rise to two functions:
- f: A → B given by b = f(a) = the roll number assigned to student a
- g: B → C given by c = g(b) = the code number assigned to roll number b

where a ∈ A, b ∈ B and c ∈ C.

We can write c = g(b) = g(f(a)).

Thus, by the combination of these two functions, each student is eventually attached a code number. This idea leads to the following definition.

---

### Definition

Let f: A → B and g: B → C be two functions. Then the **composition of f and g** denoted by **g∘f** is defined as the function:

**g∘f(x) = g(f(x))** for all x ∈ A.

---

![](image-44.png)


### Example 1.19

Find f∘g and g∘f when f(x) = 2x + 1 and g(x) = x² - 2

**Solution**

f(x) = 2x + 1, g(x) = x² – 2

**f∘g(x)** = f(g(x)) = f(x² - 2) = 2(x² - 2) + 1 = **2x² - 3**

**g∘f(x)** = g(f(x)) = g(2x + 1) = (2x + 1)² - 2 = 4x² + 4x + 1 - 2 = **4x² + 4x - 1**

Thus f∘g(x) = 2x² - 3, g∘f(x) = 4x² + 4x - 1.

From the above, we see that **f∘g ≠ g∘f**.

---

### Thinking Corner

If f(x) = x^m and g(x) = x^n, does f∘g = g∘f?

---

### Note

Generally, **f∘g ≠ g∘f** for any two functions f and g. So, **composition of functions is not commutative**.

---

### Example 1.20

Represent the function f(x) = √(2x² - 5x + 3) as a composition of two functions.

**Solution**

Let f₂(x) = 2x² - 5x + 3 and f₁(x) = √x

Then f(x) = √(2x² - 5x + 3) = √f₂(x) = f₁[f₂(x)] = **f₁∘f₂(x)**

---

### Example 1.21

If f(x) = 3x - 2, g(x) = 2x + k and if f∘g = g∘f, then find the value of k.

**Solution**

f(x) = 3x - 2, g(x) = 2x + k

**f∘g(x)** = f(g(x)) = f(2x + k) = 3(2x + k) - 2 = **6x + 3k - 2**

**g∘f(x)** = g(f(x)) = g(3x - 2) = 2(3x - 2) + k = **6x - 4 + k**

Given that f∘g = g∘f

∴ 6x + 3k - 2 = 6x - 4 + k
3k - k = -4 + 2
2k = -2
**k = -1**

---

### Example 1.22

Find k if f∘f(k) = 5 where f(k) = 2k - 1.

**Solution**

f∘f(k) = f(f(k)) = f(2k - 1) = 2(2k - 1) - 1 = 4k - 2 - 1 = **4k - 3**

But f∘f(k) = 5
∴ 4k - 3 = 5
4k = 8
**k = 2**

---

### Note

The Composition g∘f(x) exists **only when range of f is a subset of domain of g**.

---

## 1.9.1 Composition of three functions

Let A, B, C, D be four sets and let f: A → B, g: B → C and h: C → D be three functions. Using composite functions f∘g and g∘h, we get two new functions like (f∘g)∘h and f∘(g∘h).


![](image-46.png)


We observed that the composition of functions is not commutative. The natural question is about the associativity of the operation.

---

### Note

**Composition of three functions is always associative.** That is:

**f∘(g∘h) = (f∘g)∘h**

---

### Example 1.23

If f(x) = 2x + 3, g(x) = 1 - 2x and h(x) = 3x. Prove that f∘(g∘h) = (f∘g)∘h

**Solution**

f(x) = 2x + 3, g(x) = 1 - 2x, h(x) = 3x

Now, **(f∘g)(x)** = f(g(x)) = f(1 - 2x) = 2(1 - 2x) + 3 = 2 - 4x + 3 = **5 - 4x**

Then, **(f∘g)∘h(x)** = (f∘g)(h(x)) = (f∘g)(3x) = 5 - 4(3x) = **5 - 12x** ... (1)

**(g∘h)(x)** = g(h(x)) = g(3x) = 1 - 2(3x) = **1 - 6x**

⇒ **f∘(g∘h)(x)** = f(1 - 6x) = 2(1 - 6x) + 3 = 2 - 12x + 3 = **5 - 12x** ... (2)

From (1) and (2), we get **(f∘g)∘h = f∘(g∘h)**

---

### Example 1.24

Find x if f∘f∘f(x) = f∘g∘g(x), given f(x) = 3x + 1 and g(x) = x + 3.

**Solution**

**f∘f∘f(x)** = f[f{f(x)}] = f[f(3x + 1)] = f[3(3x + 1) + 1] = f(9x + 4)
= 3(9x + 4) + 1 = 27x + 12 + 1 = **27x + 13**

Wait, let me re-read... The original says g∘f∘f(x) = f∘g∘g(x)

Let me redo:

**g∘f∘f(x)** = g[f{f(x)}] 
= g[f(3x + 1)] 
= g[3(3x + 1) + 1] 
= g(9x + 4) 
= (9x + 4) + 3 = **9x + 7**

**f∘g∘g(x)** = f[g{g(x)}]
= f[g(x + 3)]
= f[(x + 3) + 3]
= f(x + 6)
= 3(x + 6) + 1 = 3x + 18 + 1 = **3x + 19**

These two quantities being equal:
9x + 7 = 3x + 19
6x = 12
**x = 2**

---

### Progress Check

State your answer for the following questions by selecting the correct option.

1. Composition of functions is commutative
   - (a) Always true
   - (b) Never true
   - (c) Sometimes true

2. Composition of functions is associative
   - (a) Always true
   - (b) Never true
   - (c) Sometimes true

---

### Activity 4

Given that h(x) = f∘g(x), fill in the table for h(x)

| x | f(x) |
|---|------|
| 1 | 2 |
| 2 | 3 |
| 3 | 1 |
| 4 | 4 |

| x | g(x) |
|---|------|
| 1 | 2 |
| 2 | 4 |
| 3 | 3 |
| 4 | 1 |

| x | h(x) |
|---|------|
| 1 | 3 |
| 2 | ? |
| 3 | ? |
| 4 | ? |

**How to find h(1)?**

h(x) = f∘g(x)
h(1) = f(g(1)) = f(2) = **3** ∴ h(1) = 3

---
=======
TBD
>>>>>>> 15f6ef76085591e823daf71800df63727236033b
