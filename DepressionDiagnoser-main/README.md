# Depression Diagnosis Expert System

A medical AI expert system that provides a basic assessment of depression severity based on user input. The system uses a weighted scoring model applied to common symptoms of depression, guided by a 10-question self-report.

## Features
- GUI-based questionnaire using Tkinter
- Knowledge base of key depressive symptoms
- Severity scoring system with weights for each symptom
- Dynamic navigation (next/previous question)
- Instant feedback based on total score

## How It Works
1. User responds to 10 questions about their mood, habits, and thoughts over the past two weeks.
2. Each answer is given a severity score (e.g., "Most of the time" = 4).
3. Scores are multiplied by symptom weights and totaled.
4. Based on the total score, the system gives a basic indication of potential depression severity.

## Requirements
- Python 3.x
- Tkinter (pre-installed with most Python distributions)

## How to Run
```bash
python "main (1).py"
