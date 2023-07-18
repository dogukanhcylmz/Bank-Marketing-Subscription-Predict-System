# Bank-Marketing-Subscription-Predict-System - Classification

In this project, me and my team mates' aim is to create a machine learning model to forecast whether or not a bank customer will subscribe for a term deposit and we deployed our project on the streamlit platform. While doing that we used “bank-additional.csv” files, which can be found at this site https://archive.ics.uci.edu/ml/datasets/Bank+Marketing. This dataset has 4119 rows and 21 columns.


## Problem 
Predict if the client will subscribe a term deposit.
## System Environment

**The project was developed using:**
 - Python
 - Jupyter Notebook
 - Streamlit
 - numpy
 - Pandas
 - Scikit-learn
 - Matplotlib

## Approach
- The goal is to predict whether or not a bank customer will subcribe for a term deposit  based on various features given in  a dataset of bank-additional.csv
- Performing a classification analysis on this data set.
- In order to accomplish this project, we perform;
   - data cleaning and preprocessing, 
   - future scaling and normalization,
   - feature selection and engineering steps,
   - model selection and training
   - hyperparameter tuning using pipeline and grid search
 
- We train 4 different models, and the best- performing model is Gradient Boosting . We obtain it with using appropriate metrics.  After that,  we tune the hyperparameters of the selected model to improve its performance. We create a pipeline for whole process. 
- Four different models are used:RandomForestClassifier ,GradientBoostingClassifier ,SGDCClassifier, Naive Bayes.
- And the best performing model is Gradient Boosting  with 0.94 accuracy.


## Streamlit Cloud Address
Check out: https://beyzaelaslan-bank-additional-prediction-proje-ar5a2s.streamlit.ap
