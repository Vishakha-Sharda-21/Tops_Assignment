"""
Session 2 - Task 2: Simulated RAG workflow for IPL stats (no API needed)

RAG = Retrieval + Augmented + Generation
1. RETRIEVE : read ipl_stats.txt and find lines that match the user's question (string matching)
2. AUGMENT  : combine the question + retrieved lines into one prompt
3. GENERATE : print a combined answer (simulated; a real RAG would send the prompt to an LLM)

Run: python task2_rag_ipl.py
"""
import re

STOPWORDS = {"the", "a", "an", "is", "are", "of", "in", "who", "what", "which", "how", "many",
             "did", "has", "have", "for", "to", "and", "ipl", "was", "by", "me", "tell", "about",
             "much", "does", "do", "with", "on", "at", "their", "his", "her"}


def load_lines(path="ipl_stats.txt"):
    with open(path, encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def keywords(text):
    words = re.findall(r"[a-z0-9]+", text.lower())
    return [w for w in words if w not in STOPWORDS and len(w) > 1]


def retrieve(question, lines, top_k=3):
    """Score each line by number of matching keywords; return the best lines."""
    kws = keywords(question)
    scored = []
    for line in lines:
        low = line.lower()
        score = sum(1 for k in kws if k[:5] in low)   # prefix match = simple stemming
        if score > 0:
            scored.append((score, line))
    scored.sort(key=lambda x: x[0], reverse=True)
    if not scored:
        return []
    best = scored[0][0]          # keep only the best-matching lines
    return [line for sc, line in scored if sc >= max(best - 0, 1)][:top_k]


def build_prompt(question, context):
    ctx = "\n".join(f"- {c}" for c in context) or "- (no relevant data found)"
    return f"Answer the question using only this data.\n\nData:\n{ctx}\n\nQuestion: {question}"


def answer(question, context):
    if not context:
        return "Sorry, I could not find this in the IPL stats file."
    return "Based on the stats file: " + " ".join(context)


if __name__ == "__main__":
    lines = load_lines()
    print("IPL Stats RAG Bot (type 'exit' to quit)")
    while True:
        q = input("\nAsk a question about IPL: ").strip()
        if q.lower() in ("exit", "quit", ""):
            break
        found = retrieve(q, lines)
        print("\n[1] Retrieved lines:")
        for l in found:
            print("   *", l)
        print("\n[2] Combined prompt (question + retrieved data):")
        print(build_prompt(q, found))
        print("\n[3] Final answer:")
        print(answer(q, found))
