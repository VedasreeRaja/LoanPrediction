import streamlit as st

def main():
    bg = """<div style='background-color:black; padding:13px'>
              <h1 style='color:white'>Streamlit Loan Elgibility Prediction App</h1>
       </div>"""
    st.markdown(bg, unsafe_allow_html=True)

    left, right = st.columns((2,2))
    gender = left.selectbox('Gender', ('Male', 'Female'))
    married = right.selectbox('Married', ('Yes', 'No'))
    dependent = left.selectbox('Dependents', ('None', 'One', 'Two', 'Three'))
    education = right.selectbox('Education', ('Graduate', 'Not Graduate'))
    self_employed = left.selectbox('Self-Employed', ('Yes', 'No'))
    applicant_income = right.number_input('Applicant Income')
    coApplicantIncome = left.number_input('Coapplicant Income')
    loanAmount = right.number_input('Loan Amount')
    loan_amount_term = left.number_input('Loan Tenor (in months)')
    creditHistory = right.number_input('Credit History', 0.0, 1.0)
    propertyArea = st.selectbox('Property Area', ('Semiurban', 'Urban', 'Rural'))
    button = st.button('Predict')


    # if button is clicked
    if button:
        # make prediction
        result = predict(gender, married, dependent, education, self_employed, applicant_income,
                        coApplicantIncome, loanAmount, loan_amount_term, creditHistory, propertyArea)
        st.success(f'You are {result} for the loan')