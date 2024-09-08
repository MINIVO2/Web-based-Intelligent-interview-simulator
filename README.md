# Recruitment and Assessment Software

## Overview

This project is a recruitment and assessment software that evaluates candidates based on their CV and real-time responses. The system extracts skills from the candidate's CV using BERT, generates interview questions using Google Gemini API (Gemini 1.5 Flash), analyzes the candidate’s responses, and scores them based on their performance.

## Features

- **Skill Extraction:** Automatically extract skills from the candidate’s CV using BERT model.
- **Tailored Question Generation:** Generate interview questions tailored to the candidate's extracted skills using the Google Gemini API.
- **Response Analysis:** Analyze the candidate’s answers in real-time and generate follow-up questions.
- **Scoring System:** Score candidates based on their responses and generate an overall performance evaluation.

## Project Structure

```bash
.
├── skills.py               # Skill extraction logic using BERT
├── script.py               # Main script for the interview and evaluation process
├── requirements.txt        # Dependencies required for the project
├── README.md               # Project documentation
└── ...
```

## Setup Instructions

### Prerequisites

- Python 3.7+
- Google API Key for Gemini API
- TensorFlow and required libraries

### Installation

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/repository-name.git
cd repository-name
```

2. **Set up a virtual environment (optional but recommended):**

```bash
python -m venv venv
source venv/bin/activate   # On Windows, use: venv\Scripts\activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Set your Google API key:**

Make sure to add your API key to your environment variables.

```bash
export GOOGLE_API_KEY="your-api-key"   # On Windows, use: set GOOGLE_API_KEY="your-api-key"
```

### Running the Software

Run the `script.py` to start the interview process. The system will extract skills from the candidate’s CV and generate questions accordingly.

```bash
python script.py
```

## How It Works

1. **Skill Extraction:**
   - The candidate’s CV is analyzed using a BERT model to extract key skills like `Python`, `Machine Learning`, etc.
   
2. **Interview Questions:**
   - Based on the extracted skills, the Google Gemini API generates tailored questions.
   
3. **Response Handling:**
   - The candidate answers the questions one by one. The system analyzes each response and, based on the analysis, may ask follow-up questions.
   
4. **Scoring:**
   - After 10 questions, the system provides a score out of 10 based on the quality of the candidate's responses.

## Example Output

```bash
Question 1: Describe your approach to using Python for data analysis.
Candidate's Response: "I would use pandas and NumPy for preprocessing, and scikit-learn for modeling."
...
Final Candidate Score: 8/10
```

## Dependencies

- Python 3.7+
- TensorFlow
- Huggingface Transformers
- Google Generative AI (Gemini API)

