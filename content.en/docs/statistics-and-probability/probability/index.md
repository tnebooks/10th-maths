---
title: 'Probability'
weight: 4
extensions:
- katex
---


# Probability 

![Alt text](image.png)
Few centuries ago, gambling and gaming were considered to be fashionable and became widely popular among many men. As the games became more complicated, players were interested in knowing the chances of winning or losing a game from a given situation. In 1654, Chevalier de Mere, a French nobleman with a taste of gambling, wrote a letter to one of the prominent mathematician of the time, Blaise Pascal, seeking his advice about how much dividend he would get for a gambling game played by paying money. Pascal worked this problem mathematically but thought of sharing this problem and see how his good friend and mathematician Pierre de Fermat could solve. Their subsequent correspondences on the issue represented the birth of Probability Theory as a new branch of mathematics.

**Random Experiment** 

A random experiment is an experiment in which

1. The set of all possible outcomes are known 
2. Exact outcome is not known.

**Example :** 1\. Tossing a coin. 2\. Rolling a die. 3\. Selecting a card from a pack of 52 cards.

**Sample space** 
The set of all possible outcomes in a random experiment is called a sample space. It is generally denoted by _S_. 

**Example :** When we roll a die, the possible outcomes are the face numbers 1,2,3,4,5,6 of the die. Therefore the sample space is _S_ = {1,2,3,4,5,6}

**Sample point** Each element of a sample space is called a sample point. 

![Alt text](image-1.png)

## Tree diagram 

Tree diagram allow us to see visually all possible outcomes of an random experiment. Each branch in a tree diagram represent a possible outcome.

**Illustration**

![Alt text](image-2.png)
1. When we throw a die, then from the tree diagram (Fig.8.3), the sample space can be written as _S_ \= {1,2,3,4,5,6}

![Alt text](image-3.png)
2. When we toss two coins, then from the tree diagram (Fig.8.4), 
the sample space can be written as S={_HH,HT,TH,TT_}

**Progress Check**

1\. An experiment in which a particular outcome cannot be predicted is called \_\_\_\_\_\_\_. 

2\. The set of all possible outcomes is called \_\_\_\_\_\_\_.

**Example 8.17** Express the sample space for rolling two dice using tree diagram. 

**_Solution_** When we roll two dice, since each die contain 6 faces marked with 1,2,3,4,5,6 the tree diagram will look like

![Alt text](image-4.png)

Hence, the sample space can be written as

S= {(1,1),(1,2),(1,3),(1,4),(1,5),(1,6)

(2,1),(2,2),(2,3),(2,4),(2,5),(2,6)

(3,1),(3,2),(3,3),(3,4),(3,5),(3,6)

(4,1),(4,2),(4,3),(4,4),(4,5),(4,6)

(5,1),(5,2),(5,3),(5,4),(5,5),(5,6)

(6,1),(6,2),(6,3),(6,4),(6,5),(6,6)}

**Event :** In a random experiment, each possible outcome is called an event. Thus, an event will be a subset of the sample space.

![Alt text](image-5.png)

**Example :** Getting two heads when we toss two coins is an event.

**Trial :** Performing an experiment once is called a trial.

**Example :** When we toss a coin thrice, then each toss of a coin is a trial.



| Events | Explanation | Example |
| :---: | :---: | :---: |
| Equally likely events | Two or more events are said to be equally likely if each one of them has an equal chance of occurring. | Head and tail are equally likely events in tossing a coin. |
| Certain events | In an experiment, the event which surely occur is called certain event. | When we roll a die, the event of getting any natural number from one to six is a certain event. |
| Impossible events | In an experiment if an event has no scope to occur then it is called an impossible event. | When we toss two coins, the event of getting three heads is an impossible event. |
| Mutually exclusive events | Two or more events are said to be mutually exclusive if they don’t have common sample points. i.e., events A, B are said to be mutually exclusive if {{< katex >}}A ∩ B = \phi{{< /katex >}} . | When we roll a die the events of getting odd numbers and even numbers are mutually exclusive events. |
| Exhaustive events | The collection of events whose union is the whole sample space are called exhaustive events. | When we toss a coin twice, the collection of events of getting two heads, exactly one head, no head are exhaustive events. |
| Complementary events | The complement of an event A is the event representing collection of sample points not in A. It is denoted {{< katex >}}A^{'}{{< /katex >}} or {{< katex >}}A^{c}{{< /katex >}} or {{< katex >}}\bar{A}{{< /katex >}} The event A and its complement {{< katex >}}A^{'}{{< /katex >}} are mutually exclusive and exhaustive. | When we roll a die, the event ‘rolling a 5 or 6’ and the event of rolling a 1, 2, 3 or 4 are complementary events. |


**Note**

**Elementary event:** If an event _E_ consists of only one outcome then it is called an elementary event.

**Do You Know**

In 1713, Bernoulli was the first to recognise the wide-range applicability of probability in fields outside gambling.

## Probability of an Event

In a random experiment, let S be the sample space and {{< katex >}}E \subseteq S{{< /katex >}} . Then if _E_ is an event, the probability of occurrence of _E_ is defined as

{{< katex >}}
P(E) =\frac{\text { Number of outcomes favourable to occurence of E }}{\text { Number of all possible outcomes }} =\frac{n(E)}{n(S)}
{{< /katex >}}

This way of defining the probability is applicable only to finite sample spaces. So in this chapter, we will be dealing problems only with finite sample spaces.

**Note**

{{< katex >}}P(E)=\frac{n(E)}{n(E)}{{< /katex >}}

{{< katex >}}P(E)=\frac{n(S)}{n(S)}=1{{< /katex >}}. The The probability of sure event is 1.

{{< katex >}}P(\phi)=\frac{n(\phi)}{n(S)}=\frac{0}{n(s)}=0{{< /katex >}}. The probability of impossible event is 0.

Since _E_ is a subset of _S_ and {{< katex >}}\phi{{< /katex >}} is a subset of any set,

{{< katex display >}}\phi \subseteq E \subseteq S{{< /katex >}}

{{< katex display>}}P(\phi) \leq P(E) \leq P(S){{< /katex >}}

{{< katex display>}}0 \leq P(E) \leq 1{{< /katex >}}

Therefore, the probability value always lies from 0 to 1.

{{< katex >}}>{{< /katex >}} The complement event of {{< katex >}}E{{< /katex >}} is {{< katex >}}\bar{E}{{< /katex >}} .

Let {{< katex >}}P(E)=\frac{m}{n}{{< /katex >}} (where _m_ is the number of favourable outcomes of _E_ and _n_ is the total number of possible outcomes).

{{< katex display >}}
P(\bar{E}) =\frac{\text { Number of outcomes unfavourable to occurence of E }}{\text { Number of all possible outcomes }}
{{< /katex >}}

{{< katex display >}}
P(\bar{E}) =\frac{n-m}{n} =1-\frac{m}{n}
{{< /katex >}}

{{< katex display >}}P(\bar{E})=1-P(E){{< /katex >}}

{{< katex display >}}P(E)+P(\bar{E})=1{{< /katex >}}
![Alt text](image-6.png)

**Progress Check**

Which of the following values cannot be a probability of an event?

1. –0.0001 
2. 0.5 
3. 1.001 
4. 1
5. 20% 
6. 0.253 
7. {{< katex >}} P(E) =\frac{1-\sqrt5}{2} {{< /katex >}} 
8. {{< katex >}} P(E) =\frac{\sqrt3 +1}{4} {{< /katex >}}



**Example 8.18** A bag contains 5 blue balls and 4 green balls. A ball is drawn at random from the bag. Find the probability that the ball drawn is 1. blue 2. not blue. 

**_Solution_** Total number of possible outcomes {{< katex >}}n(S)=5+4=9{{< /katex >}}

1. Let _A_ be the event of getting a blue ball. Number of favourable outcomes for the event A. Therefore, {{< katex >}}n(A) = 5{{< /katex >}}
Probability that the ball drawn is blue. Therefore, {{< katex >}} P(A) =\frac{n(A)}{n(S)} =\frac{5}{9}
{{< /katex >}}

2. {{< katex >}}\bar{A}{{< /katex >}} will be the event of not getting a blue ball. So {{< katex >}} P(\bar{A}) =1-P(A)=1-\frac{5}{9}=\frac{4}{9} {{< /katex >}}

**Example 8.19** Two dice are rolled. Find the probability that the sum of outcomes is 
1. equal to 4  
2. greater than 10  
3. less than 13

**_Solution_** When we roll two dice, the sample space is given by

 _S_ = { (1,1),(1,2),(1,3),(1,4),(1,5),(1,6)

(2,1),(2,2),(2,3),(2,4),(2,5),(2,6)

(3,1),(3,2),(3,3),(3,4),(3,5),(3,6)

(4,1),(4,2),(4,3),(4,4),(4,5),(4,6)

(5,1),(5,2),(5,3),(5,4),(5,5),(5,6)

(6,1),(6,2),(6,3),(6,4),(6,5),(6,6) }; {{< katex >}}n(S)=36{{< /katex >}}

1. Let _A_ be the event of getting the sum of outcome values equal to 4. 

Then _A_ = {(1,3),(2,2),(3,1)}; {{< katex >}}n(A)=3{{< /katex >}}.

Probability of getting the sum of outcomes equal to 4 is {{< katex >}} P(A) =\frac{n(A)}{n(S)}=\frac{3}{36}=\frac{1}{12} {{< /katex >}}

2. Let B be the event of getting the sum of outcome values greater than 10. 

Then B = {(5,6),(6,5),(6,6)}; {{< katex >}}n(B)=3{{< /katex >}}

Probability of getting the sum of outcomes greater than 10 is {{< katex >}}P(B) =\frac{n(B)}{n(S)}=\frac{3}{36}=\frac{1}{12}{{< /katex >}}

3. Let C be the event of getting the sum of outcomes less than 13. Here all the outcomes have the sum value less than 13. 

Hence {{< katex >}}C=S{{< /katex >}}.

Therefore, {{< katex >}}n(C)=n(S)=36{{< /katex >}}

Probability of getting the total value less than 13 is {{< katex >}}P(C) = \frac{n(C)}{n(S)}=\frac{36}{36}=1{{< /katex >}}.

**Example 8.20** Two coins are tossed together. What is the probability of getting different faces on the coins? 

**_Solution_** When two coins are tossed together, the sample space is 

_S_ = {_HH,HT,TH,TT_}; {{< katex >}}n(S)=4{{< /katex >}} 

Let _A_ be the event of getting different faces on the coins. 

_A_ = {_HT, TH_};  {{< katex >}}n(A)=2{{< /katex >}} 

Probability of getting different faces on the coins is 

{{< katex >}}P(A) = \frac{n(A)}{n(S)}=\frac{2}{4}==\frac{1}{2}{{< /katex >}}.

**Example 8.21** From a well shuffled pack of 52 cards, one card is drawn at random. Find the probability of getting 1. red card 2. heart card 3. red king 4. face card 5. number card

![Alt text](image-7.png)

**_Solution_** {{< katex >}}n(S)=52{{< /katex >}}

1. Let _A_ be the event of getting a red card.

{{< katex >}}n(A)=26{{< /katex >}}

Probability of getting a red card is

{{< katex >}}P(A) = \frac{26}{52}=\frac{1}{1}=1{{< /katex >}}.

2. Let _B_ be the event of getting a heart card.

{{< katex >}}n(B)=13{{< /katex >}}

Probability of getting a heart card is

{{< katex >}}P(B) =\frac{n(B)}{n(S)}=\frac{13}{52}=\frac{1}{4}{{< /katex >}}

3. Let _C_ be the event of getting a red king card. A red king card can be either a diamond king or a heart king.

{{< katex >}}n(C)=2{{< /katex >}}

Probability of getting a red king card is

{{< katex >}}P(C) =\frac{n(C)}{n(S)}=\frac{2}{52}=\frac{1}{26}{{< /katex >}}

4. Let _D_ be the event of getting a face card. The face cards are Jack (_J_), Queen (_Q_), and King (_K_).

{{< katex >}}n(D)=4{{< /katex >}}X{{< katex >}}3=12{{< /katex >}}

Probability of getting a face card is

{{< katex >}}P(D) =\frac{n(D)}{n(S)}=\frac{12}{52}=\frac{3}{13}{{< /katex >}}

5. Let _E_ be the event of getting a number card. The number cards are 2, 3, 4, 5, 6, 7, 8, 9 and 10.

{{< katex >}}n(D)=4{{< /katex >}}X{{< katex >}}9=36{{< /katex >}}

Probability of getting a number card is

{{< katex >}}P(E) =\frac{n(E)}{n(S)}=\frac{36}{52}=\frac{9}{13}{{< /katex >}}


**Example 8.22** What is the probability that a leap year selected at random will contain 53 saturdays.

**_Solution_** A leap year has 366 days. So it has 52 full weeks and 2 days. 52 Saturdays must be in 52 full weeks. The possible chances for the remaining two days will be the sample space.

_S_ = {Sun-Mon, Mon-Tue, Tue-Wed, Wed-Thu, Thu-Fri, Fri-Sat, Sat-Sun}

{{< katex >}}n(S)=7{{< /katex >}}

Let _A_ be the event of getting 53rd Saturday. Then _A_ = {Fri-Sat, Sat-Sun}; {{< katex >}}n(A)=2{{< /katex >}}

Probability of getting 53 Saturdays in a leap year is {{< katex >}}P(A) =\frac{n(A)}{n(S)}=\frac{2}{7}{{< /katex >}}

**Thinking Corner**

 What will be the probability that a non- leap year will have 53 Saturdays?

**Example 8.23** A die is rolled and a coin is tossed simultaneously. Find the probability that the die shows an odd number and the coin shows a head. 

![Alt text](image-8.png)

**_Solution_** Sample space _S_ = {1H,1T,2H,2T,3H,3T,4H,4T,5H,5T,6H,6T};

{{< katex >}}n(S)=12{{< /katex >}}

Let _A_ be the event of getting an odd number and a head. A = {1H, 3H, 5H}; {{< katex >}}n(A)=3{{< /katex >}}

{{< katex >}}P(A) =\frac{n(A)}{n(S)}=\frac{3}{12}=\frac{1}{4}{{< /katex >}}

| Activity 3 | Activity 4 |
| :---: | :---: |
| There are three routes {{< katex >}}R_{1}{{< /katex >}} , {{< katex >}}R_{2}{{< /katex >}} and {{< katex >}}R_{3}{{< /katex >}} from Madhu’s home to her place of work. There are four parking lots {{< katex >}}P_{1}{{< /katex >}} , {{< katex >}}P_{2}{{< /katex >}} , {{< katex >}}P_{3}{{< /katex >}} , {{< katex >}}P_{4}{{< /katex >}} and three entrances {{< katex >}}B_{1}{{< /katex >}} , {{< katex >}}B_{2}{{< /katex >}} , {{< katex >}}B_{3}{{< /katex >}} into the office building. There are two elevators {{< katex >}}E_{1}{{< /katex >}} and {{< katex >}}E_{2}{{< /katex >}} to her floor. Using the tree diagram explain how many ways can she reach her office? | Collect the details and find the probabilities of 1. selecting a boy from your class. 2. selecting a girl from your class. 3. selecting a student from tenth standard in your school. 4. selecting a boy from tenth standard in your school. 5. selecting a girl from tenth standard in your school. |

**Example 8.24** A bag contains 6 green balls, some black and red balls. Number of black balls is as twice as the number of red balls. Probability of getting a green ball is thrice the probability of getting a red ball. Find 1. number of black balls 2. total number of balls. 

**_Solution_** Number of green balls is {{< katex >}}n(G)=6{{< /katex >}}

Let number of red balls is {{< katex >}}n(R)=x{{< /katex >}}

Therefore, number of black balls is {{< katex >}}n(B)=2x{{< /katex >}}

Total number of balls {{< katex >}}n(S)=6+x+2x=6+3x{{< /katex >}}

It is given that, {{< katex >}}P(R)=3{{< /katex >}}X{{< katex >}}P(R){{< /katex >}}

{{< katex >}}\frac{6}{6+3x}=3{{< /katex >}}X{{< katex >}}\frac{x}{6+3x}{{< /katex >}}

{{< katex >}}3x=6{{< /katex >}} gives, {{< katex >}}x=2{{< /katex >}}

1. Number of black balls = 2 x 2 = 4

2. Total number of balls = 6 + (3 X 2) = 12

**Example 8.25** A game of chance consists of spinning an arrow which is equally likely to come to rest pointing to one of the numbers 1, 2, 3, …12. What is the probability that it will point to 1. 7 2. a prime number 3. a composite number? 

![Alt text](image-9.png)

**_Solution_** Sample space _S_ = {1,2,3,4,5,6,7,8,9,10,11,12}; {{< katex >}}n(S)=12{{< /katex >}}

1. Let _A_ be the event of resting in 7. {{< katex >}}n(A)=1{{< /katex >}}

{{< katex >}}P(A) =\frac{n(A)}{n(S)}=\frac{1}{12}{{< /katex >}}

2. Let _B_ be the event that the arrow will come to rest in a prime number. _B_ = {2,3,5,7,11}; {{< katex >}}n(B)=5{{< /katex >}}

{{< katex >}}P(B) =\frac{n(B)}{n(S)}=\frac{5}{12}{{< /katex >}}

(iii) Let _C_ be the event that arrow will come to rest in a composite number. _C_ = {4,6,8,9,10,12}; {{< katex >}}n(C)=6{{< /katex >}}

{{< katex >}}P(C) =\frac{n(C)}{n(S)}=\frac{6}{12}=\frac{1}{2}{{< /katex >}}

**Thinking Corner**

 What is the complement event of an impossible event?

**Exercise 8.3**

1\. Write the sample space for tossing three coins using tree diagram. 

2\. Write the sample space for selecting two balls at a time from a bag containing 6 balls numbered 1 to 6 (using tree diagram).

3\. If _A_ is an event of a random experiment such that _P_(_A_) : _P A_( )=17:15 and _n_(_S_)=640
then find 
1. {{< katex >}}P(\bar{A}){{< /katex >}} 
2. {{< katex >}}n(A){{< /katex >}}. 

4\. A coin is tossed thrice. What is the probability of getting two consecutive tails? 

5\. At a fete, cards bearing numbers 1 to 1000, one number on one card are put in a box.
Each player selects one card at random and that card is not replaced. If the selected card has a perfect square number greater than 500, the player wins a prize. What is the probability that 
1. the first player wins a prize 
2. the second player wins a prize, if the first has won?

6\. A bag contains 12 blue balls and _x_ red balls. If one ball is drawn at random 
1. what is the probability that it will be a red ball? 
2. If 8 more red balls are put in the bag, and if the probability of drawing a red ball will be twice that of the probability in 1, then find x.

7\. Two unbiased dice are rolled once. Find the probability of getting 
1. a doublet (equal numbers on both dice) 
2. the product as a prime number 
3. the sum as a prime number 
4. the sum as 1


8\. Three fair coins are tossed together. Find the probability of getting 
1. all heads 
2. atleast one tail 
3. atmost one head 
4. atmost two tails

9\. A bag contains 5 red balls, 6 white balls, 7 green balls, 8 black balls. One ball is drawn at random from the bag. Find the probability that the ball drawn is
1. white 
2. black or red 
3. not white 
4. neither white nor black 

10\. In a box there are 20 non-defective and some defective bulbs. If the probability that
a bulb selected at random from the box found to be defective is {{< katex >}}\frac{3}{8}{{< /katex >}}
then, find the number of defective bulbs.

11\. The king and queen of diamonds, queen and jack of hearts, jack and king of spades are removed from a deck of 52 playing cards and then well shuffled. Now one card is drawn at random from the remaining cards. Determine the probability that the card is 
1. a clavor 
2. a queen of red card 
3. a king of black card

12\. Some boys are playing a game, in which the stone thrown by them landing in a circular region (given in the figure) is considered as win and landing other than the circular region is considered as loss. What is the probability to win the game? (π = 3.14)
![Alt text](image-10.png)

13\. Two customers Priya and Amuthan are visiting a particular shop in the same week (Monday to Saturday). Each is equally likely to visit the shop on any one day as on another day. What is the probability that both will visit the shop on
1. the same day 
2. different days 
3. consecutive days? 

14\. In a game, the entry fee is ₹150. The game consists of tossing a coin 3 times. Dhana bought
a ticket for entry . If one or two heads show, she gets her entry fee back. If she throws 3 heads, she receives double the entry fees. Otherwise she will lose. Find the probability that she 
1. gets double entry fee 
2. just gets her entry fee 
3. loses the entry fee.