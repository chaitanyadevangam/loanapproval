import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

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

# Function to train and evaluate a loan approval prediction model (replace with your actual model and dataset)
def train_and_evaluate_model():
    # Load your dataset (replace 'your_dataset.csv' with your actual dataset)
    df = pd.read_csv('loan_approval_dataset.csv')

    # Drop columns not needed for training
    features = ['no_of_dependents', 'income_annum', 'loan_amount', 'loan_term', 'cibil_score',
                'residential_assets_value', 'commercial_assets_value', 'luxury_assets_value', 'bank_asset_value']
    target = 'loan_status'
    df = df[features + [target]]

    # Convert categorical features to numerical using one-hot encoding
    df = pd.get_dummies(df, columns=['education', 'self_employed'])

    # Extract features and target variable
    X = df.drop(target, axis=1)
    y = df[target]

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a RandomForestClassifier (replace with your actual model)
    classifier = RandomForestClassifier()
    classifier.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = classifier.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)

    return accuracy

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

        # Train and evaluate the loan approval prediction model
        model_accuracy = train_and_evaluate_model()
        st.subheader('Loan Approval Prediction Model Accuracy:')
        st.write(f'The model accuracy is: {model_accuracy:.2%}')

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
