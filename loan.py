import streamlit as st
import random

# Define a list of financial psychometric analysis questions and their possible answers
questions = [
    {
        'question': 'How do you handle unexpected financial emergencies?',
        'answers': ['Save in advance', 'Borrow from friends/family', 'Take a loan', 'Use credit cards']
    },
    {
        'question': 'What is your current employment status?',
        'answers': ['Full-time employed', 'Part-time employed', 'Unemployed', 'Self-employed']
    },
    {
        'question': 'How would you rate your credit score?',
        'answers': ['Excellent', 'Good', 'Fair', 'Poor']
    },
    {
        'question': 'What is your monthly income range?',
        'answers': ['Less than ₹20,000', '₹20,000 - ₹50,000', '₹50,000 - ₹1,00,000', 'More than ₹1,00,000']
    },
    {
        'question': 'How often do you check your bank statements?',
        'answers': ['Daily', 'Weekly', 'Monthly', 'Rarely']
    }
]

# Function to calculate the correctness percentage based on user responses
def calculate_percentage(user_responses):
    correct_answers = [2, 0, 1, 2, 1]  # Adjust the correct answers based on your criteria
    num_correct = sum(user_responses[i] == correct_answers[i] for i in range(len(correct_answers)))
    percentage = (num_correct / len(correct_answers)) * 100
    return round(percentage, 2)

# Streamlit app
def main():
    st.title('Loan Approval Psychometric Analysis')

    # Display questions and collect user responses
    user_responses = []
    for i, question_data in enumerate(questions):
        st.subheader(f"Question {i + 1}: {question_data['question']}")
        selected_answer = st.selectbox('Select your answer:', question_data['answers'])
        user_responses.append(question_data['answers'].index(selected_answer))

    # Calculate and display correctness percentage
    correctness_percentage = calculate_percentage(user_responses)
    st.subheader('Psychometric Analysis Result:')
    st.write(f'Your correctness percentage is: {correctness_percentage}%')

    # CSS styling for the app
    st.markdown(
        """
        <style>
            body {
                background-color: #ecf0f1;
            }
            .stApp {
                max-width: 800px;
                margin: 0 auto;
            }
            .stHeader {
                color: #3498db;
                font-size: 3em;
                text-align: center;
                margin-bottom: 20px;
            }
            .stSubheader {
                color: #3498db;
                font-size: 1.8em;
                margin-bottom: 10px;
            }
            .stSelectbox {
                width: 100%;
                padding: 15px;
                font-size: 1.2em;
                margin-bottom: 25px;
                border: 2px solid #3498db;
                border-radius: 5px;
                box-sizing: border-box;
            }
            .stMarkdown {
                color: #3498db;
                font-size: 1.5em;
                text-align: center;
                margin-top: 30px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()

