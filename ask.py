from .search import search_top_k

def answer_question(query: str) -> str:
    ...

def build_answer(snippets: list) -> str: # defines function to build answer from snippets
    """
    Combine multiple note snippets into a simple answer.
    Right now, this is a rule-based summarizer (no LLM).
    """
    if not snippets: #checks if snippets list is empty
        return "I couldn't find related information in your notes." #returns default message if no snippets found

    combined = " ".join([entry["text"] for entry in snippets]) #collect raw text from the top results

    combined = combined.strip() #very simple cleanup

    if len(combined) > 500: #truncate if too long
        combined = combined[:500] + "..." #indicate truncation

    return combined #return the combined answer