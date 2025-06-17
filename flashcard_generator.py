def generate_flashcards(text):
    """
    Generate simple question-answer flashcards from input text.
    Each sentence becomes one flashcard.
    """
    flashcards = []
    sentences = text.strip().split('.')

    for i, sentence in enumerate(sentences):
        clean_sentence = sentence.strip()
        if clean_sentence:
            question = f"What is meant by: '{clean_sentence}'?"
            answer = clean_sentence
            flashcards.append({'question': question, 'answer': answer})

    return flashcards

