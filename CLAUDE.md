# Claude Project Instructions: 10th Maths MCQ Generation

This repository contains Class 10 Mathematics textbooks in English (`content.en/`) and Tamil (`content.ta/`).
A specialized skill is established to extract, solve, and format multiple-choice questions into standardized quiz files.

---

## Skill: Chapter MCQ Generator

Whenever asked to process or generate MCQs for a chapter:
Available chapters:
1. `relations-and-functions`
2. `numbers-and-sequences`
3. `algebra` (completed in [questions/maths/algebra/](file:///questions/maths/algebra/))
4. `geometry`
5. `coordinate-geometry`
6. `trigonometry`
7. `mensuration`
8. `statistics-and-probability`

### 1. File Locations
- **Source English**: `content.en/docs/<chapter>/_index.md` (under `Multiple choice questions` heading)
- **Source Tamil**: `content.ta/docs/<chapter>/_index.md` (under `தெரிவு வினாக்கள்` heading)
- **Output Directory**: `questions/maths/<chapter>/`
  - English: `questions/maths/<chapter>/<number>.md`
  - Tamil: `questions/maths/<chapter>/<number>_ta.md`

### 2. Quick Helper Tool
To preview or verify the raw MCQ text for any chapter in both languages, run:
```bash
python3 scripts/extract_raw_mcqs.py <chapter-name>
# e.g., python3 scripts/extract_raw_mcqs.py relations-and-functions
```

### 3. Output Schema
Each question file MUST follow this exact structure:

```markdown
---
choices:
  - <distractor 1>
  - <distractor 2>
  - <distractor 3>
answers:
  - <correct answer>
---

## <Question statement without leading numbers>

---

#### <Factual, step-by-step mathematical reasoning and proof>
```

### 4. Mandatory Rules
- **Choices**: Place exactly the 3 incorrect options (distractors) under `choices:`.
- **Answers**: Place the single correct option under `answers:`.
- **Strip labels**: Remove option identifiers like `(A)`, `(B)`, `(C)`, `(D)` and `(அ)`, `(ஆ)`, `(இ)`, `(ஈ)`. Only retain the actual choice expression.
- **Header**: Use `## ` followed by the clean question text (strip `1. `, `2. `, etc.).
- **Divider**: Exactly one `---` horizontal divider line below the `## ` header.
- **Truth-Based Explanations**: Use `#### `. Must provide rigorous, factual mathematical derivations and justifications (no bluffing or shortcuts). English files explain in English; Tamil files explain in Tamil.
- **CRITICAL - Post-Extraction Cleanup**: Once all MCQs for a chapter are parsed, solved, and saved under `questions/maths/<chapter>/`, **REMOVE the entire MCQ exercise section** from both `content.en/docs/<chapter>/_index.md` and `content.ta/docs/<chapter>/_index.md`. The document should cleanly flow from the preceding exercise directly to the next section (e.g. Unit Exercise or Points to Remember).

---

## Detailed Skill Documentation & Examples
Full instructions and working examples are documented in:
- [.agents/skills/chapter-mcq-parser/SKILL.md](file:///.agents/skills/chapter-mcq-parser/SKILL.md)
- Reference completed chapter: [questions/maths/algebra/](file:///questions/maths/algebra/)
