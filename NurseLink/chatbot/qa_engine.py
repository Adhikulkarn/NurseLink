import google.generativeai as genai
from .pdf_engine import find_relevant_chunks

model = genai.GenerativeModel("gemini-flash-latest")

def get_pdf_answer(question, chunks):
    context = find_relevant_chunks(question, chunks)

    prompt = f"""
You are the official NurseLink assistant.

Answer the user's question ONLY using the context below. 
If the answer is not present, say:
"I could not find this information in the NurseLink manual."

---

CONTEXT:
{context}

---

QUESTION:
{question}

Respond clearly and concisely.
"""

    response = model.generate_content(prompt)
    return response.text
