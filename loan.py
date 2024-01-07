import streamlit as st
import random

# Define a list of financial psychometric analysis questions and their possible answers
questions = [
    {
        'question': 'How do you handle unexpected financial emergencies?',
        'answers': {
            'Save in advance': 10,
            'Borrow from friends/family': 5,
            'Take a loan': 15,
            'Use credit cards': 8
        }
    },
    {
        'question': 'What is your current employment status?',
        'answers': {
            'Full-time employed': 15,
            'Part-time employed': 8,
            'Unemployed': 5,
            'Self-employed': 12
        }
    },
    {
        'question': 'How would you rate your credit score?',
        'answers': {
            'Excellent': 15,
            'Good': 12,
            'Fair': 8,
            'Poor': 5
        }
    },
    {
        'question': 'What is your monthly income range?',
        'answers': {
            'Less than ₹20,000': 5,
            '₹20,000 - ₹50,000': 10,
            '₹50,000 - ₹1,00,000': 15,
            'More than ₹1,00,000': 12
        }
    },
    {
        'question': 'How often do you check your bank statements?',
        'answers': {
            'Daily': 10,
            'Weekly': 15,
            'Monthly': 8,
            'Rarely': 5
        }
    }
]

# Function to calculate the user's score based on responses and their weightage
def calculate_score(user_responses):
    total_score = 0
    for i, response in enumerate(user_responses):
        question_data = questions[i]
        total_score += question_data['answers'][response]
    return total_score

# Streamlit app
def main():
    st.title('Loan Approval Psychometric Analysis')

    # Display questions and collect user responses
    user_responses = []
    for i, question_data in enumerate(questions):
        st.subheader(f"Question {i + 1}: {question_data['question']}")
        selected_answer = st.selectbox('Select your answer:', list(question_data['answers'].keys()))
        user_responses.append(selected_answer)

    # Submit button
    if st.button('Submit'):
        # Calculate and display user's score
        user_score = calculate_score(user_responses)
        st.subheader('Psychometric Analysis Result:')
        st.write(f'Your score is: {user_score}')

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
