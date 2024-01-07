import streamlit as st

# Define a list of financial psychometric analysis questions and their possible answers
questions = [
    {
        'question': 'How do you handle unexpected financial emergencies?',
        'answers': {
            'Save in advance': 20,
            'Borrow from friends/family': 10,
            'Take a loan': 30,
            'Use credit cards': 15
        }
    },
    {
        'question': 'What is your current employment status?',
        'answers': {
            'Full-time employed': 30,
            'Part-time employed': 15,
            'Unemployed': 10,
            'Self-employed': 25
        }
    },
    {
        'question': 'How would you rate your credit score?',
        'answers': {
            'Excellent': 30,
            'Good': 25,
            'Fair': 15,
            'Poor': 10
        }
    },
    {
        'question': 'What is your monthly income range?',
        'answers': {
            'Less than ₹20,000': 10,
            '₹20,000 - ₹50,000': 20,
            '₹50,000 - ₹1,00,000': 30,
            'More than ₹1,00,000': 25
        }
    },
    {
        'question': 'How often do you check your bank statements?',
        'answers': {
            'Daily': 20,
            'Weekly': 30,
            'Monthly': 15,
            'Rarely': 10
        }
    }
]

# Function to calculate the user's normalized score based on responses and their weightage
def calculate_normalized_score(user_responses, credit_utilization_ratio):
    total_score = 0
    max_possible_score = 0

    for i, response in enumerate(user_responses):
        question_data = questions[i]
        total_score += question_data['answers'][response]
        max_possible_score += max(question_data['answers'].values())

    # Normalize the score to be in the range [0, 100]
    normalized_score = (total_score / max_possible_score) * 100

    # Adjust the score based on the credit utilization ratio
    normalized_score += (credit_utilization_ratio - 20) * 0.5  # Adjust the weight and factor as needed

    return round(normalized_score, 2)

# Streamlit app
def main():
    st.title('Loan Approval Psychometric Analysis')

    # Display questions and collect user responses
    user_responses = []
    for i, question_data in enumerate(questions):
        st.subheader(f"Question {i + 1}: {question_data['question']}")
        selected_answer = st.selectbox('Select your answer:', list(question_data['answers'].keys()))
        user_responses.append(selected_answer)

    # Get user's input for credit utilization
    credit_utilization_ratio = st.number_input('Enter your credit utilization ratio based on previous loans:', min_value=0.0, max_value=100.0, step=1.0)

    # Submit button
    if st.button('Submit'):
        # Calculate and display user's normalized score
        normalized_score = calculate_normalized_score(user_responses, credit_utilization_ratio)
        st.subheader('Psychometric Analysis Result:')
        st.write(f'Your normalized score is: {normalized_score}')

        # Check if the user's score is above 65%
        if normalized_score > 65:
            # Display video from your PC
            st.video('path/to/your/video.mp4')

    # CSS styling for the app
    st.markdown(
        """
        <style>
            body {
                background-color: #ecf0f1;
                margin: 0;
            }
            .stApp {
                max-width: 100%;
                margin: 0;
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
            .stNumberInput {
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
