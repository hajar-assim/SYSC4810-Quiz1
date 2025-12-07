# Quiz Question Format Instructions

This document describes the exact format for creating quiz questions for the SYSC 4810 Quiz System.

## File Structure

Each chapter should be in its own file named `chapterX_questions.py` containing a single function:

```python
def get_chapter_X_questions():
    """Returns Chapter X questions"""
    return {
        # Sections go here
    }
```

## Section Format

Questions are organized into sections. Each section is a dictionary with:
- **Key**: Section identifier (e.g., `"section1"`, `"section2"`)
- **Value**: Dictionary containing:
  - `"title"`: String - Display title for the section
  - `"questions"`: List - Array of question dictionaries

Example:
```python
"section1": {
    "title": "Section 1: Multiple Choice (2 points each)",
    "questions": [
        # Question objects here
    ]
}
```

## Question Types

### 1. Multiple Choice Questions

**Format:**
```python
{
    "num": 1,                    # Question number (integer)
    "question": "Question text?", # The actual question (string)
    "options": {                 # Answer choices (dictionary)
        "A": "First option",
        "B": "Second option",
        "C": "Third option",
        "D": "Fourth option"
    },
    "answer": "B",               # Correct answer letter (string)
    "points": 2,                 # Points awarded (integer)
    "explanation": "Why B is correct..." # Feedback text (string)
}
```

**Required Fields:**
- `num` - Question number
- `question` - Question text
- `options` - Dictionary with "A", "B", "C", "D" keys
- `answer` - Letter of correct answer ("A", "B", "C", or "D")
- `points` - Point value
- `explanation` - Educational feedback

**Use Cases:**
- Standard multiple choice questions
- Scenario-based questions with multiple choice answers
- Questions worth 2-3 points

---

### 2. True/False Questions

**Format:**
```python
{
    "num": 21,
    "question": "Statement to evaluate.",
    "answer": "T",               # "T" for True or "F" for False
    "points": 1,                 # Typically 1 point
    "explanation": "TRUE - Explanation of why..."
}
```

**Required Fields:**
- `num` - Question number
- `question` - Statement to evaluate
- `answer` - "T" or "F" (string)
- `points` - Point value (typically 1)
- `explanation` - Should start with "TRUE -" or "FALSE -"

**Important:**
- NO `options` field for True/False questions
- Answer must be exactly "T" or "F" (uppercase)
- Explanation should clearly state TRUE/FALSE first

---

### 3. Short Answer Questions (Single Answer)

**Format:**
```python
{
    "num": 50,
    "question": "Fill in the blank or short answer question?",
    "answer": ["acceptable answer 1", "acceptable answer 2", "answer 3"],
    "points": 2,
    "type": "text",              # Indicates short answer format
    "explanation": "Detailed explanation..."
}
```

**Required Fields:**
- `num` - Question number
- `question` - Question text
- `answer` - **List of acceptable answers** (all lowercase)
- `points` - Point value
- `type` - Must be `"text"`
- `explanation` - Explanation of the answer

**Important:**
- `answer` is a **list**, not a string
- All acceptable variations should be included
- Answers are matched using case-insensitive substring matching
- User gets full points if their answer contains ANY acceptable answer

**Example:**
```python
"answer": ["initialization vector", "init vector", "iv"]
# User typing "The IV is used..." would match "iv"
```

---

### 4. Short Answer Questions (Multiple Required Answers)

**Format:**
```python
{
    "num": 46,
    "question": "Name TWO examples (separate with comma):",
    "answer": ["option 1", "option 2", "option 3", "option 4"],
    "points": 2,
    "type": "multi_text",        # Requires multiple matches
    "explanation": "Valid answers include: option 1, option 2, option 3, option 4"
}
```

**Required Fields:**
- `num` - Question number
- `question` - Question text (should indicate how many answers needed)
- `answer` - **List of acceptable answers** (all lowercase)
- `points` - Point value
- `type` - Must be `"multi_text"`
- `explanation` - Explanation listing all valid answers

**Scoring:**
- User must match **at least 2** acceptable answers to get full points
- If only 1 match found: User gets **half points**
- If 0 matches: User gets **0 points**

**Example:**
```python
{
    "question": "Name TWO attack types that are classified as ACTIVE attacks:",
    "answer": ["denial of service", "replay", "masquerade", "modification"],
    "type": "multi_text",
    "points": 2
}
# User must mention at least 2 of these to get 2 points
```

---

## Complete Examples

### Example Section with Multiple Question Types

```python
def get_chapter_5_questions():
    """Returns Chapter 5 questions"""
    return {
        "section1": {
            "title": "Section 1: Multiple Choice (2 points each)",
            "questions": [
                {
                    "num": 1,
                    "question": "What is the primary purpose of encryption?",
                    "options": {
                        "A": "To compress data",
                        "B": "To ensure confidentiality",
                        "C": "To verify identity",
                        "D": "To speed up transmission"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "Encryption's primary purpose is to ensure confidentiality by making data unreadable to unauthorized parties."
                },
                {
                    "num": 2,
                    "question": "In asymmetric encryption, the public key can decrypt messages encrypted with the private key.",
                    "options": {
                        "A": "True - for digital signatures",
                        "B": "False - only private can decrypt public",
                        "C": "True - for all encryption",
                        "D": "False - keys are unrelated"
                    },
                    "answer": "A",
                    "points": 2,
                    "explanation": "TRUE for digital signatures: sign with private key, verify with public key. For confidentiality: encrypt with public, decrypt with private."
                }
            ]
        },

        "section2": {
            "title": "Section 2: True/False (1 point each)",
            "questions": [
                {
                    "num": 3,
                    "question": "SSL and TLS are the same protocol.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - TLS is the successor to SSL. While similar, TLS has improved security features and is the current standard."
                },
                {
                    "num": 4,
                    "question": "HTTPS uses TLS to secure HTTP communications.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - HTTPS = HTTP + TLS/SSL. It provides encrypted communication over the web."
                }
            ]
        },

        "section3": {
            "title": "Section 3: Short Answer (2 points each)",
            "questions": [
                {
                    "num": 5,
                    "question": "What does PKI stand for?",
                    "answer": ["public key infrastructure", "pki"],
                    "points": 2,
                    "type": "text",
                    "explanation": "PKI = Public Key Infrastructure, the framework for managing public key encryption."
                },
                {
                    "num": 6,
                    "question": "Name TWO components required for a digital signature (separate with comma):",
                    "answer": ["private key", "hash function", "public key", "signing algorithm"],
                    "points": 2,
                    "type": "multi_text",
                    "explanation": "Digital signatures require: a hash function, private key (for signing), public key (for verification), and a signing algorithm."
                }
            ]
        }
    }
```

---

## Field Reference

### All Question Types

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `num` | int | Yes | Question number (sequential within chapter) |
| `question` | str | Yes | The question text |
| `answer` | str or list | Yes | Correct answer (format varies by type) |
| `points` | int | Yes | Point value (1-3 typically) |
| `explanation` | str | Yes | Educational feedback explaining the answer |

### Multiple Choice Only

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `options` | dict | Yes | Dictionary with keys "A", "B", "C", "D" |

### Short Answer Only

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | str | Yes | Either `"text"` or `"multi_text"` |

---

## Best Practices

### Question Numbering
- Number questions sequentially starting from 1 within each chapter
- Questions are automatically renumbered when chapters are combined
- Use consistent numbering within each section

### Answer Lists for Short Answer
- Include all reasonable variations and abbreviations
- Use lowercase for all entries
- Think about partial answers users might give
- Example: `["symmetric", "secret key", "symmetric key"]`

### Explanations
- Always provide clear, educational explanations
- For True/False, start with "TRUE -" or "FALSE -"
- Reference relevant concepts or lecture material
- Keep explanations concise but informative

### Points Distribution
- Multiple Choice: 2-3 points
- True/False: 1 point
- Short Answer (text): 2 points
- Short Answer (multi_text): 2 points
- Scenario/Complex: 3 points

### Section Organization
- Group similar question types together
- Use descriptive section titles
- Include point values in section titles
- Typical structure:
  - Section 1: Multiple Choice
  - Section 2: True/False
  - Section 3: Scenario-Based (optional)
  - Section 4: Short Answer

---

## Common Mistakes to Avoid

1. **Wrong answer format for T/F**: Use "T" or "F", not True/False or 1/0
2. **Forgetting `type` field**: Short answer questions MUST have `"type": "text"` or `"type": "multi_text"`
3. **Answer as string instead of list**: For short answer, use `["answer"]` not `"answer"`
4. **Missing options for multiple choice**: All multiple choice must have "A", "B", "C", "D"
5. **Including options for T/F**: True/False questions should NOT have an `options` field
6. **Uppercase in answer lists**: All entries in answer lists should be lowercase
7. **Missing explanation**: Every question must have an explanation

---

## Testing Your Questions

After creating your chapter file:

1. **Import test**:
   ```bash
   python3 -c "from chapterX_questions import get_chapter_X_questions; print('Success!')"
   ```

2. **Structure test**:
   ```python
   from chapterX_questions import get_chapter_X_questions
   q = get_chapter_X_questions()
   print(f"Sections: {len(q)}")
   print(f"First section questions: {len(q['section1']['questions'])}")
   ```

3. **Verify all questions have required fields**

---

## Quick Reference Template

```python
# Multiple Choice
{
    "num": 1,
    "question": "Question?",
    "options": {"A": "...", "B": "...", "C": "...", "D": "..."},
    "answer": "B",
    "points": 2,
    "explanation": "..."
}

# True/False
{
    "num": 21,
    "question": "Statement.",
    "answer": "T",  # or "F"
    "points": 1,
    "explanation": "TRUE - ..."
}

# Short Answer (single)
{
    "num": 41,
    "question": "Question?",
    "answer": ["answer1", "answer2"],
    "points": 2,
    "type": "text",
    "explanation": "..."
}

# Short Answer (multiple required)
{
    "num": 46,
    "question": "Name TWO...",
    "answer": ["opt1", "opt2", "opt3"],
    "points": 2,
    "type": "multi_text",
    "explanation": "..."
}
```
