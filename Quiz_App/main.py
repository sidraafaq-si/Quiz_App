import streamlit as st
import random

st.title("Quiz Application")

questions = [
    {
        "question": "What is the capital of Pakistan?",
        "options": ["Islamabad", "Karachi", "Lahore", "Peshawar"],
        "answer": "Islamabad"
    },
    {
        "question": "Who is the founder of Pakistan?",
        "options": [
            "Allama Iqbal",
            "Muhammad Ali Jinnah",
            "Liaquat Ali Khan",
            "Benazir Bhutto"
        ],
        "answer": "Muhammad Ali Jinnah"
    },
    {
        "question": "Which is the national language of Pakistan?",
        "options": ["English", "Urdu", "Pashto", "Sindhi"],
        "answer": "Urdu"
    },
    {
        "question": "What is the currency of Pakistan?",
        "options": ["Rupee", "Dollar", "Euro", "Pound"],
        "answer": "Rupee"
    },
    {
        "question": "Which city is known as the city of Lights in Pakistan?",
        "options": ["Karachi", "Lahore", "Islamabad", "Peshawar"],
        "answer": "Karachi"
    },
]

if "current_question_index" not in st.session_state:
    st.session_state.current_question_index = 0
    st.session_state.score = 0
    st.session_state.selected_answers = [None] * len(questions)

index = st.session_state.current_question_index
question = questions[index]

st.subheader(f"Question {index + 1}: {question['question']}")

selected_option = st.radio("Choose your answer:", question["options"], key=f"q{index}", index=None)

if st.button("Next"):
    if selected_option:
        st.session_state.selected_answers[index] = selected_option
        if selected_option == question["answer"]:
            st.session_state.score += 1

        if st.session_state.current_question_index < len(questions) - 1:
            st.session_state.current_question_index += 1
        else:
            st.session_state.quiz_completed = True
    else:
        st.warning("Please select an answer before proceeding.")

if st.session_state.get("quiz_completed", False):
    st.subheader("Quiz Completed!")
    st.write(f"Your final score is: **{st.session_state.score} / {len(questions)}**")
    
    st.write("### Correct Answers:")
    for i, q in enumerate(questions):
        st.write(f"**Q{i+1}: {q['question']}**")
        st.write(f"✅ Correct Answer: {q['answer']}")
        user_answer = st.session_state.selected_answers[i]
        if user_answer == q["answer"]:
            st.write(f"🎯 Your Answer: {user_answer}")
        else:
            st.write(f"❌ Your Answer: {user_answer if user_answer else 'Not Answered'}")
    
    if st.button("Restart Quiz"):
        st.session_state.current_question_index = 0
        st.session_state.score = 0
        st.session_state.selected_answers = [None] * len(questions)
        st.session_state.quiz_completed = False
        st.rerun()
