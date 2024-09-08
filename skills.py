# Install the required library
import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    text = ""
    pdf_document = fitz.open(pdf_path)
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text += page.get_text()
    return text

pdf_path = "Your cv"
cv_text = extract_text_from_pdf(pdf_path)


from transformers import BertTokenizer, BertModel
import torch

# Load pre-trained BERT model and tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')



# Tokenize the text
inputs = tokenizer(cv_text, return_tensors="pt", truncation=True, padding=True)

# Get BERT model outputs
with torch.no_grad():
    outputs = model(**inputs)

# Extract token embeddings (last hidden states)
token_embeddings = outputs.last_hidden_state

# Convert token IDs to tokens
tokens = tokenizer.convert_ids_to_tokens(inputs['input_ids'][0])

# Print tokens and their embeddings (for demonstration)
# for token, embedding in zip(tokens, token_embeddings[0]):
#     print(f"Token: {token}, Embedding: {embedding.numpy()}")
known_skills = ["python", "machine learning", "data analysis", "java", "sql", "deep learning", "tensorflow", "keras"]

# Extract skills mentioned in the CV
# Create a set of unique tokens from the known skills list
known_skill_set = set([skill.lower() for skill in known_skills])

# Find tokens that match the known skills
extracted_skills = [token for token in tokens if token.lower() in known_skill_set]

print("Extracted Skills:", extracted_skills)


