---
title: 'நிகழ்ச்சிகளின் இயற்கணிதம்'
weight: 5
---

## 8.5 நிகழ்ச்சிகளின் செயல்பாடுகள் (Algebra of Events)

ஒரு சமவாய்ப்பு சோதனையில் \( S \) ஆனது கூறுவெளி என்க. \( A \subseteq S \) மற்றும் \( B \subseteq S \) ஆகியவை, கூறுவெளி \( S \)-ன் நிகழ்ச்சிகள் என்க. மேலும்,

(i) \( A \) மற்றும் \( B \) ஆகிய இரண்டு நிகழ்ச்சிகளும் சேர்ந்து நடைபெற்றால் அந்த நிகழ்ச்சியானது \( (A \cap B) \) என்ற நிகழ்ச்சியாகும்.

(ii) \( A \) அல்லது \( B \)-யில் ஏதாவது ஒன்று நடைபெற்றால் அந்த நிகழ்ச்சியானது \( (A \cup B) \) என்ற நிகழ்ச்சியாகும்.

(iii) \( \bar{A} \) என்ற நிகழ்ச்சியானது, \( A \) என்ற நிகழ்ச்சி நடைபெறாத பொழுது நடைபெறும் நிகழ்ச்சியாகும்.

<center>படம் 8.6(i)</center>

<center>படம் 8.6(ii)</center>

<center>படம் 8.6(iii)</center>

**குறிப்பு:**

\( \bullet \quad A \cap \bar{A} = \emptyset \)

\( \bullet \quad A \cup \bar{A} = S \)

\( \bullet \quad A, B \) ஆகியன ஒன்றையொன்று விலக்கும் நிகழ்ச்சிகள் எனில் \( P(A \cup B) = P(A) + P(B) \)

\( \bullet \quad P(\text{ஒன்றையொன்று விலக்கும் நிகழ்ச்சிகளின் சேர்ப்பு}) = \sum (\text{நிகழ்ச்சிகளின் நிகழ்தகவு}) \)

**தேற்றம் 1**

\( A \) மற்றும் \( B \) ஆகியவை ஒரு சமவாய்ப்பு சோதனையின் இரண்டு நிகழ்ச்சிகள் எனில்

(i) \( P(A \cap \bar{B}) = P(A \text{ மட்டும்}) = P(A) - P(A \cap B) \)

(ii) \( P(\bar{A} \cap B) = P(B \text{ மட்டும்}) = P(B) - P(A \cap B) \) என நிறுவுக.

**நிரூபணம்**

(i) கணங்களின் பங்கீட்டுப் பணியின் படி,

1. \( (A \cap B) \cup (A \cap \bar{B}) = A \cap (B \cup \bar{B}) = A \cap S = A \)

2. \( (A \cap B) \cap (A \cap \bar{B}) = A \cap (B \cap \bar{B}) = A \cap \emptyset = \emptyset \)

எனவே, \( A \cap B \) மற்றும் \( A \cap \bar{B} \) ஆகியவை ஒன்றையொன்று விலக்கும் நிகழ்ச்சிகள் மற்றும் அவைகளின் சேர்ப்பு \( A \) ஆகும்.

ஆகையால், \( P(A) = P[(A \cap B) \cup (A \cap \bar{B})] \)

\( P(A) = P(A \cap B) + P(A \cap \bar{B}) \)

\( P(A \cap \bar{B}) = P(A) - P(A \cap B) \)

அதாவது, \( P(A \cap \bar{B}) = P(A \text{ மட்டும்}) = P(A) - P(A \cap B) \)

<center>படம் 8.7</center>

(ii) கணங்களின் பங்கீட்டுப் பணியின் படி,

1. \( (A \cap B) \cup (\bar{A} \cap B) = (A \cup \bar{A}) \cap B = S \cap B = B \)

2. \( (A \cap B) \cap (\bar{A} \cap B) = (A \cap \bar{A}) \cap B = \emptyset \cap B = \emptyset \)

<center>படம் 8.8</center>

எனவே, \( A \cap B \) மற்றும் \( \bar{A} \cap B \) ஆகியவை ஒன்றையொன்று விலக்கும் நிகழ்ச்சிகள் மற்றும் அவைகளின் சேர்ப்பு \( B \) ஆகும்.

ஆகையால், \( P(B) = P[(A \cap B) \cup (\bar{A} \cap B)] \)

\( P(B) = P(A \cap B) + P(\bar{A} \cap B) \)

\( P(\bar{A} \cap B) = P(B) - P(A \cap B) \)

அதாவது, \( P(\bar{A} \cap B) = P(B \text{ மட்டும்}) = P(B) - P(A \cap B) \)

**முன்னேற்றச் சோதனை**

1. \( P(A \text{ மட்டும்}) = \) __________.

2. \( P(\bar{A} \cap \bar{B}) = \) __________.

3. \( A \cap B \) மற்றும் \( A \cap \bar{B} \) ஆகியவை __________ நிகழ்ச்சிகள்.

4. \( P(A \cap \bar{B}) = \) __________.

5. \( A \) மற்றும் \( B \) ஆகியவை ஒன்றையொன்று விலக்கும் நிகழ்ச்சிகள் எனில், \( P(A \cap B) = \) ______.

6. \( P(\bar{A} \cap B) = 0.3, P(A \cap B) = 0.45 \) எனில், \( P(B) = \) ______.

---

**Note:** Section 8.6 (Addition Theorem of Probability) will be covered in the next response.