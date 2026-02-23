---
title: 'Algebra of Events'
weight: 5
extensions:
- katex
---

# Algebra of Events 

In a random experiment, let S be the sample space. Let {{< katex >}}A \subseteq S{{< /katex >}} and {{< katex >}}B \subseteq S{{< /katex >}} be the events in _S._ We say that

![Alt text](image.png)

**Note**

{{< katex >}}A \cap \bar{A} = \phi{{< /katex >}}

{{< katex >}}A \cup \bar{A} = S{{< /katex >}}

If _A, B_ are mutually exclusive events, then {{< katex >}}P(A \cup B) = P(A) + P(B){{< /katex >}}

_P_ (Union of mutually exclusive events)= {{< katex >}}\Sigma{{< /katex >}}( Probability of events)

**Thorem 1** 

If _A_ and _B_ are two events associated with a random experiment, then prove that

![Alt text](image-1.png)

1. {{< katex >}}P(A \cap \bar{B}) = P{{< /katex >}}(only _A_){{< katex >}}=P(A)-P(A \cap B){{< /katex >}}

2. {{< katex >}}P(\bar{A} \cap B) = P{{< /katex >}}(only _B_){{< katex >}}=P(B)-P(A \cap B){{< /katex >}}

**Proof** 

1. By Distributive property of sets,
    1. {{< katex >}}(A \cap B) \cup (A \cap \bar{B}) = A \cap (B \cup \bar{B}) = A \cap S = A{{< /katex >}}
    2. {{< katex >}}(A \cap B) \cap (A \cap \bar{B}) = A \cap (B \cap \bar{B}) = A \cap \phi = \phi{{< /katex >}}

Therefore, the events {{< katex >}}A \cap B{{< /katex >}} and {{< katex >}}A \cap \bar{B}{{< /katex >}} are mutually exclusive whose union is _A_. 

Therefore, {{< katex display >}}P(A) = P[(A \cap B) \cup (A \cap \bar{B})]{{< /katex >}}

{{< katex display >}}P(A) = P(A \cap B) + P(A \cap \bar{B}){{< /katex >}}

Therefore, {{< katex display >}}P(A \cap \bar{B}) = P(A) - P(A \cap B){{< /katex >}}

That is, {{< katex >}}P(A \cap \bar{B}) = P{{< /katex >}}(only _A_){{< katex >}}=P(A)-P(A \cap B){{< /katex >}}

![Alt text](image-2.png)

2. By Distributive property of sets, 
    1. {{< katex >}}(A \cap B) \cup (\bar{A} \cap B) = (A \cup \bar{A}) \cap B = S \cap B = B{{< /katex >}}
    2. {{< katex >}}(A \cap B) \cap (\bar{A} \cap B) = (A \cap \bar{A}) \cap B = \phi \cap B = \phi{{< /katex >}}

Therefore, the events {{< katex >}}A \cap B{{< /katex >}} and {{< katex >}}\bar{A} \cap B{{< /katex >}} are mutually exclusive whose union is _B_.

{{< katex display >}}P(B) = P[(A \cap B) \cup (\bar{A} \cap B)]{{< /katex >}}

{{< katex display >}}P(B) = P(A \cap B) + P(\bar{A} \cap B){{< /katex >}}

Therefore, {{< katex display >}}P(\bar{A} \cap B) = P(B) - P(A \cap B){{< /katex >}}

That is, {{< katex >}}P(\bar{A} \cap B) = P{{< /katex >}}(only _B_){{< katex >}}=P(B)-P(A \cap B){{< /katex >}}

**Progress Check**

1. _P_(only _A_)= \_\_\_\_\_\_\_\_. 

2. {{< katex >}}P(\bar{A} \cap B){1}{{< /katex >}} = \_\_\_\_\_\_\_\_.

3. {{< katex >}}A \cap B{{< /katex >}} and {{< katex >}}A \cap \bar{B}{{< /katex >}} are \_\_\_\_\_\_\_ events.

4. {{< katex >}}P(\bar{A} \cap \bar{B}){{< /katex >}} = \_\_\_\_\_\_\_\_.

5. If _A_ and _B_ are mutually exclusive events then {{< katex dispaly >}}P(A \cap B){{< /katex >}} = \_\_\_\_\_\_\_.

6. If {{< katex >}}P(A \cap B)=0.3, P(\bar{A} \cap B)=0.45{{< /katex >}} then {{< katex >}}P(B){{< /katex >}} =\_\_\_\_\_\_\_.