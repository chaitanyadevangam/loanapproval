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
    },
    {
        'question': 'How do you manage unexpected changes in your income?',
        'answers': {
            'Savings and emergency fund': 30,
            'Adjusting budget and expenses': 25,
            'Seeking additional income sources': 20,
            'No specific plan': 10
        }
    },
    {
        'question': 'What is your approach to handling existing debts?',
        'answers': {
            'Aggressively paying off debts': 30,
            'Making regular payments': 25,
            'Consolidating debts': 20,
            'Struggling to meet payments': 10
        }
    },
    {
        'question': 'How do you stay informed about financial matters?',
        'answers': {
            'Regularly reading financial news': 30,
            'Consulting with financial advisors': 25,
            'Attending financial workshops/seminars': 20,
            'Limited awareness of financial matters': 10
        }
    },
    {
        'question': 'What is your attitude towards long-term financial planning?',
        'answers': {
            'Actively plan for the future': 30,
            'Consider future but not actively planning': 25,
            'Live in the present, minimal future planning': 15,
            'No specific attitude towards long-term planning': 10
        }
    },
    {
        'question': 'How often do you review and update your financial goals?',
        'answers': {
            'Regularly reassess and adjust goals': 30,
            'Occasionally update goals': 25,
            'Rarely revisit financial goals': 15,
            'No specific routine for goal review': 10
        }
    },
    {
        'question': 'How would you describe your approach to budgeting?',
        'answers': {
            'Detailed budgeting and tracking expenses': 30,
            'Rough estimation of monthly spending': 20,
            'Occasional budgeting, mostly impulsive spending': 15,
            'No specific budgeting': 10
        }
    },
    {
        'question': 'In case of a financial windfall (unexpected large sum of money), what would you do?',
        'answers': {
            'Invest a significant portion': 30,
            'Save for future goals': 25,
            'Pay off debts or loans': 20,
            'Splurge on luxury items': 10
        }
    },
    {
        'question': 'How proactive are you in seeking financial advice?',
        'answers': {
            'Regularly consult with financial advisors': 30,
            'Seek advice occasionally': 25,
            'Rarely seek financial advice': 15,
            'Rely on personal decisions': 10
        }
    },
    {
        'question': 'What percentage of your income do you allocate for savings?',
        'answers': {
            'More than 20%': 30,
            '10% - 20%': 25,
            '5% - 10%': 15,
            'Less than 5%': 10
        }
    },
    {
        'question': 'How do you handle financial setbacks, such as unexpected expenses or job loss?',
        'answers': {
            'Dip into emergency savings': 30,
            'Cut down on discretionary spending': 25,
            'Seek additional sources of income': 20,
            'Struggle to cope with the setback': 10
        }
    },
    {
        'question': 'What is your attitude towards long-term financial planning?',
        'answers': {
            'Actively plan for the future': 30,
            'Consider future but not actively planning': 25,
            'Live in the present, minimal future planning': 15,
            'No specific attitude towards long-term planning': 10
        }
    },
    {
        'question': 'How often do you review and update your financial goals?',
        'answers': {
            'Regularly reassess and adjust goals': 30,
            'Occasionally update goals': 25,
            'Rarely revisit financial goals': 15,
            'No specific routine for goal review': 10
        }
    }
]

# Function to calculate the user's normalized score based on responses and their weightage
def calculate_normalized_score(user_responses):
    total_score = 0
    max_possible_score = 0

    for i, response in enumerate(user_responses):
        question_data = questions[i]
        total_score += question_data['answers'][response]
        max_possible_score += max(question_data['answers'].values())

    # Normalize the score to be in the range [0, 100]
    normalized_score = (total_score / max_possible_score) * 100

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

    # Submit button
    if st.button('Submit'):
        # Calculate and display user's normalized score
        normalized_score = calculate_normalized_score(user_responses)
        st.subheader('Psychometric Analysis Result:')
        st.write(f'Your normalized score is: {normalized_score}')

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
