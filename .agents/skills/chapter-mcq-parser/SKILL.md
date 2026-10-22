---
name: chapter-mcq-parser
description: >-
  Extracts Multiple Choice Questions (MCQ) from Class 10 Maths textbook chapters
  (content.en/docs/<chapter>/_index.md and content.ta/docs/<chapter>/_index.md),
  verifies the mathematically correct answer, writes standardized question files
  under questions/maths/<chapter>/ (<num>.md for English and <num>_ta.md for Tamil),
  and removes the MCQ section from the source _index.md files.
---

# Chapter MCQ Generator & Parser Skill

Use this skill to extract, solve, generate structured question markdown files for any chapter in the 10th Maths textbook repository, and remove the extracted section from the source files.

## Repository Layout & Chapter List

Source textbook files:
- **English**: `content.en/docs/<chapter>/_index.md`
- **Tamil**: `content.ta/docs/<chapter>/_index.md`

Target output folder:
- `questions/maths/<chapter>/`
  - English files: `<num>.md` (e.g., `1.md`, `2.md`, ...)
  - Tamil files: `<num>_ta.md` (e.g., `1_ta.md`, `2_ta.md`, ...)

Available Chapters:
1. `relations-and-functions`
2. `numbers-and-sequences`
3. `algebra` (already completed in `questions/maths/algebra/`)
4. `geometry`
5. `coordinate-geometry`
6. `trigonometry`
7. `mensuration`
8. `statistics-and-probability`

---

## Quick Helper Tool

To inspect and extract the raw MCQ section for any chapter in both languages:
```bash
python3 scripts/extract_raw_mcqs.py <chapter-name>
# Example:
python3 scripts/extract_raw_mcqs.py relations-and-functions
```

---

## Where to Find Questions in Source Files

In each chapter's `_index.md`:
- **English**: Look for the heading `Multiple choice questions` (can be formatted as `##### Multiple choice questions` or `**Multiple choice questions**`).
- **Tamil**: Look for the heading containing `தெரிவு வினாக்கள்` (e.g., `##### பலவுள் தெரிவு வினாக்கள்`, `**பலவுள் தெரிவு வினாக்கள்**`, or `பயனுள் தெரிவு வினாக்கள்`).

---

## Exact Question File Specification

Each question must be saved in its own file matching this exact schema:

```markdown
---
choices:
  - <distractor 1>
  - <distractor 2>
  - <distractor 3>
answers:
  - <correct answer>
---

## <Question text without leading question number>

---

#### <Truth-based mathematical reasoning and step-by-step proof>
```

### Formatting Rules

1. **Frontmatter**:
   - `choices:` contains **only the 3 incorrect options (distractors)**.
   - `answers:` contains **the 1 correct answer**.
   - Strip option letters: Remove `(A)`, `(B)`, `(C)`, `(D)` and `(அ)`, `(ஆ)`, `(இ)`, `(ஈ)`. Only include the option text/expression itself.
   - Preserve LaTeX math markers (`$...$` or `$$...$$`) and formatting.
2. **Question Statement**:
   - Level 2 heading: `## `
   - Strip leading question numbers (e.g., change `1. A system...` to `A system...`).
3. **Divider**:
   - Exactly one horizontal rule `---` (3 hyphens) below the question header.
4. **Explanation**:
   - Level 4 heading: `#### `
   - **Reasoning based on truth (No bluffing)**:
     - Provide full mathematical steps (solve equations, evaluate discriminant, cite theorem/definitions, show matrix multiplication).
     - State explicitly why the correct option holds and why distractors fail.
     - English file has explanation in English.
     - Tamil file has explanation in Tamil.

---

## Concrete Examples

### Example 1: Theoretical / Conceptual Question

#### English: `questions/maths/algebra/1.md`
```markdown
---
choices:
  - intersect only at a point
  - intersect in a line
  - coincides with each other
answers:
  - do not intersect
---

## A system of three linear equations in three variables is inconsistent if their planes

---

#### A system of linear equations is inconsistent if it has no solution. In three dimensions, each linear equation represents a plane. For the system to have no solution, there is no common point or line shared by all three planes; therefore, their planes do not intersect.
```

#### Tamil: `questions/maths/algebra/1_ta.md`
```markdown
---
choices:
  - ஒரே ஒரு புள்ளியில் வெட்டுகின்றன
  - ஒரே ஒரு கோட்டில் வெட்டுகின்றன
  - ஒன்றின் மீது ஒன்று பொருந்தும்
answers:
  - ஒன்றையொன்று வெட்டாது
---

## மூன்று மாறிகளில் அமைந்த மூன்று நேரியல் சமன்பாடுகளின் தொகுப்பிற்குத் தீர்வுகள் இல்லையெனில், அத்தொகுப்பில் உள்ள தளங்கள்

---

#### மூன்று மாறிகளில் அமைந்த ஒரு நேரியல் சமன்பாட்டுத் தொகுப்பிற்கு தீர்வு இல்லை எனில் அது ஒருங்கமைவற்றது ஆகும். வடிவியல் ரீதியாக, ஒவ்வொரு சமன்பாடும் முப்பரிமாணத்தில் ஒரு தளத்தைக் குறிக்கும். அத்தொகுப்பிற்குத் தீர்வு இல்லை எனில், மூன்று தளங்களுக்கும் பொதுவான புள்ளி ஏதும் இல்லை; எனவே, அத்தொகுப்பில் உள்ள தளங்கள் ஒன்றையொன்று வெட்டாது.
```

---

### Example 2: Mathematical Computation & Solving

#### English: `questions/maths/algebra/2.md`
```markdown
---
choices:
  - $x=-1,y=2,z=3$
  - $x=-1,y=-2,z=3$
  - $x=1,y=-2,z=3$
answers:
  - $x=1,y=2,z=3$
---

## The solution of the system $x+y-3z=-6$, $-7y+7z=7$, $3z=9$ is

---

#### From $3z = 9$, we get $z = 3$. Substituting $z = 3$ into $-7y + 7(3) = 7$ gives $-7y + 21 = 7 \implies -7y = -14 \implies y = 2$. Substituting $y = 2$ and $z = 3$ into $x + y - 3z = -6$ gives $x + 2 - 3(3) = -6 \implies x - 7 = -6 \implies x = 1$. Thus, the solution is $x = 1, y = 2, z = 3$.
```

---

## Step-by-Step Procedure for Any Remaining Chapter

When requested to process a chapter (e.g. `relations-and-functions`):

1. **Locate MCQs in Source Files**:
   - Run `python3 scripts/extract_raw_mcqs.py <chapter>` or open `content.en/docs/<chapter>/_index.md` and `content.ta/docs/<chapter>/_index.md`.
2. **Read and Align Questions**:
   - Number of questions in English and Tamil must match 1:1.
   - For each question index `i` (from 1 to N):
     - Identify question text.
     - Identify the 4 options: (A), (B), (C), (D) in English and (அ), (ஆ), (இ), (ஈ) in Tamil.
3. **Solve Mathematically**:
   - Compute the exact solution algebraically / analytically.
   - Match the result to the correct option.
   - Place the other 3 options into `choices:`.
   - Place the correct option into `answers:`.
   - Draft a comprehensive, truth-based explanation (`#### ...`).
4. **Write Files**:
   - Ensure directory `questions/maths/<chapter>/` exists.
   - Write English file `questions/maths/<chapter>/<i>.md`.
   - Write Tamil file `questions/maths/<chapter>/<i>_ta.md`.
5. **Verify**:
   - Verify all options are clean without leftover labels `(A)` or `(அ)`.
   - Ensure YAML frontmatter is valid.
   - Ensure formulas and LaTeX syntax render cleanly.
6. **Remove MCQ Section from Source Files**:
   - Once all questions are created and verified in `questions/maths/<chapter>/`, delete the entire MCQ exercise section from:
     - `content.en/docs/<chapter>/_index.md`
     - `content.ta/docs/<chapter>/_index.md`
   - Ensure smooth transition from the previous exercise to the following section (e.g. `## Unit Exercise` or `## Points to Remember`).
