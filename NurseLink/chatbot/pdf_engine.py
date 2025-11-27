import PyPDF2

# 1) Extract text
def extract_pdf_text(pdf_path):
    text = ""
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            content = page.extract_text()
            if content:
                text += content + "\n"
    return text

# 2) Chunking
def chunk_text(text, size=600):
    words = text.split()
    chunks = []
    current = []

    for w in words:
        current.append(w)
        if len(current) >= size:
            chunks.append(" ".join(current))
            current = []

    if current:
        chunks.append(" ".join(current))

    return chunks

# 3) Simple keyword-based retrieval
def find_relevant_chunks(query, chunks, k=3):
    query_words = query.lower().split()

    # score chunks based on keyword overlap
    scored = []
    for chunk in chunks:
        text = chunk.lower()
        score = sum(1 for q in query_words if q in text)
        scored.append((score, chunk))

    scored.sort(reverse=True)
    best = [c for s, c in scored[:k] if s > 0]

    # fallback: return first chunk if no match
    if not best:
        best = chunks[:1]

    return "\n\n".join(best)
