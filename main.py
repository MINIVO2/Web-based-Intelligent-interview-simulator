import os
import google.generativeai as genai

from skills import extracted_skills

# Retrieve the API key from environment variables
api_key = os.getenv("GOOGLE_API_KEY")

if api_key is None:
    raise ValueError("API key not found in environment variables")

genai.configure(api_key=api_key)

# Example skills list
skills_list = extracted_skills  # Add more skills as needed

# Function to extract skills using keyword matching
def extract_skills(cv_text):
    detected_skills = [skill for skill in skills_list if skill.lower() in cv_text.lower()]
    return detected_skills

# Model 1: Question Generation
def generate_question_for_skill(skill):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(f"Generate an interview question related to the skill: {skill}", stream=False)
    return response.text

# Model 2: Analyze Responses and Generate Follow-Up Questions
def analyze_response_and_generate_follow_up(response):
    model = genai.GenerativeModel("gemini-1.5-flash")
    analysis_response = model.generate_content(f"Analyze this response: {response}", stream=False)
    follow_up_question_response = model.generate_content(f"Generate a follow-up question based on this analysis: {analysis_response}", stream=False)
    return follow_up_question_response.text

# Model 3: Scoring and Judging
def score_candidate(responses):
    model = genai.GenerativeModel("gemini-1.5-flash")
    scoring_response = model.generate_content(f"Evaluate and score the following responses: {responses}", stream=False)
    return scoring_response.text

# Function to conduct the interview process
def conduct_interview(cv_text):
    skills = extract_skills(cv_text)
    interview_responses = []
    total_questions = 10
    question_count = 0
    score = 0

    if not skills:
        print("No skills detected. Cannot generate tailored interview questions.")
        return
    
    # Continue asking questions until we reach the total question limit (10)
    while question_count < total_questions:
        for skill in skills:
            if question_count >= total_questions:
                break
            
            # Generate and ask a question related to the skill
            question = generate_question_for_skill(skill)
            print(f"Question {question_count+1}: {question}")
            
            # Simulate receiving a response (replace this with actual input handling in practice)
            response = input("Candidate's Response (Type 'skip' if unknown): ")
            
            if response.lower() == "skip":
                print("Moving to the next question...")
            else:
                interview_responses.append(response)
                # Increment score for each valid response
                score += 1

            question_count += 1
            
    # Score the candidate based on the number of questions answered correctly
    print(f"Final Candidate Score: {score}/10")
    return score

# Example Usage
cv_text = "Sample CV text with skills such as Python, Machine Learning, and Data Analysis"
final_score = conduct_interview(cv_text)
