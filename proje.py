
import numpy as np
import pickle
import streamlit as st
import sklearn



model = pickle.load(open('proje2.pkl', 'rb'))

def predict(data):
    prediction = model.predict(data)
    if prediction == 0:
        return "No"
    else:
        return "Yes"


def main():
    
    # Giving a title
    st.title('Bank Marketing Prediction App')

    # Defining options for categorical variables
    job_options = {
        0: 'admin.',
        1: 'blue-collar',
        2: 'entrepreneur',
        3: 'housemaid',
        4: 'management',
        5: 'retired',
        6: 'self-employed',
        7: 'services',
        8: 'student',
        9: 'technician',
        10: 'unemployed',
        11: 'unknown'
    }
    marital_options = {
        0: 'single',
        1: 'married',
        2: 'divorced',
        3: 'unknown'
    }
    education_options = {
        0: 'illiterate',
        1: 'basic.4y',
        2: 'basic.6y',
        3: 'basic.9y',
        4: 'high.school',
        5: 'professional.course',
        6: 'university.degree',
        7: 'unknown'
    }
    default_options = {
        0: 'No',
        1: 'Yes',
        2: 'unknown'
    }
    housing_options = {
        0: 'No',
        1: 'Yes',
        2: 'unknown'
    }
    loan_options = {
        0: 'No',
        1: 'Yes',
        2: 'unknown'
    }
    contact_options = {
        0: 'cellular',
        1: 'telephone'
    }
    poutcome_options = {
        0: 'failure',
        1: 'success',
        2: 'nonexistent'
    }

    # Getting input from the user
    age = st.number_input('Age', step=1)
    job = st.selectbox('Job', list(job_options.keys()), format_func=lambda x: job_options[x])
    marital = st.selectbox('Marital', list(marital_options.keys()), format_func=lambda x: marital_options[x])
    education = st.selectbox('Education', list(education_options.keys()), format_func=lambda x: education_options[x])
    default = st.selectbox('Default', list(default_options.keys()), format_func=lambda x: default_options[x])
    housing = st.selectbox('Housing', list(housing_options.keys()), format_func=lambda x: housing_options[x])
    loan = st.selectbox('Loan', list(loan_options.keys()), format_func=lambda x: loan_options[x])
    contact = st.selectbox('Contact', list(contact_options.keys()), format_func=lambda x: contact_options[x])
    duration = st.number_input('Duration', step=1)
    campaign = st.number_input('Campaign', step=1)
    pdays = st.number_input('Pdays', step=1)
    previous = st.number_input('Previous', step=1)
    poutcome = st.selectbox('Poutcome', list(poutcome_options.keys()), format_func=lambda x: poutcome_options[x])
    conspriceidx = st.number_input('Cons.price.idx')
    consconfidx = st.number_input('Cons.conf.idx')
    euribor3m = st.number_input('Euribor3m')
    nremployed = st.number_input('Nr.employed')
    
    
    
    if st.button("Predict"):
        input_data = np.array([age,job,marital,education,default,housing,loan,contact,duration,campaign,pdays,previous,poutcome,conspriceidx,consconfidx,euribor3m,nremployed])  # Replace ... with input values for other features
        input_data_reshaped = input_data.reshape(1, -1)
        result = predict(input_data_reshaped)
        st.success(f"The predicted outcome is {result}.")
   
        
    
    

if __name__ == '__main__':
    main()

