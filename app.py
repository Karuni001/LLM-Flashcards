import streamlit as st
from flashcard_generator import generate_flashcards

# Title
st.set_page_config(page_title="🧠 Flashcard Generator", layout="centered")
st.title("🧠 Flashcard Generator")

# Input options
uploaded_file = st.file_uploader("📄 Upload a .txt file", type=["txt"])
user_input = st.text_area("📝 Or type/paste your text here")

# Read text
text = ""
if uploaded_file:
    text = uploaded_file.read().decode("utf-8")
elif user_input:
    text = user_input

# Generate flashcards
if text:
    flashcards = generate_flashcards(text)

    if 'index' not in st.session_state:
        st.session_state.index = 0
        st.session_state.show_answer = False

    if flashcards:
        card = flashcards[st.session_state.index]

        st.markdown(f"### ❓ Question:\n{card['question']}")

        if st.session_state.show_answer:
            st.success(f"💡 Answer: {card['answer']}")

        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("Show Answer"):
                st.session_state.show_answer = True
        with col2:
            if st.button("Next"):
                st.session_state.index = (st.session_state.index + 1) % len(flashcards)
                st.session_state.show_answer = False
    else:
        st.warning("⚠️ Couldn't generate any flashcards.")
else:
    st.info("👆 Upload a file or enter text above to begin.")
