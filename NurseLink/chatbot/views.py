from django.shortcuts import render
from .pdf_engine import extract_pdf_text, chunk_text
from .qa_engine import get_pdf_answer

PDF_PATH = "media/pdf/nurselink_manual.pdf"

loaded = False
chunks = None

def chatbot_home(request):
    global loaded, chunks

    # load PDF once
    if not loaded:
        text = extract_pdf_text(PDF_PATH)
        chunks = chunk_text(text)
        loaded = True

    answer = ""

    if request.method == "POST":
        question = request.POST.get("question")
        answer = get_pdf_answer(question, chunks)

    return render(request, "chatbot/chat.html", {"answer": answer})
