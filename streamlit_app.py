#Input the relevant libraries
import numpy as np
import pandas as pd
import streamlit as st
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Define the Streamlit app
def app():
    
    st.title('Logistic Regression')
    st.subheader('by Louie F. Cervantes M.Eng., WVSU College of ICT')
    st.write('The titanic dataset contains information about multiple \
    people like their ages, sexes, sibling counts, number of parent \
    or children companions on aboard, embarkment points and \
    whether or not they survived the disaster. Based on these \
    features, you have to predict if an arbitrary passenger on \
    Titanic would survive the sinking. The question of interest \
    for this natural dataset is how survival relates to the \
    other attributes. There is obviously no practical need to \
    predict survival, so the real interest is in interpretation, \
    but success at prediction would appear to be closely related \
    to the discovery of interesting features of the relationship. \
    To simplify the processing, the datarows with missing values \
    so this dataset is not the original dataset available at the \
    machine learning websites.')

    if st.button('Start'):
        df = pd.read_csv('titanic.csv', header=0)
        # st.dataframe(df, use_container_width=True)  
        df = labeltonumeric(df, 'Sex')
        df = labeltonumeric(df, 'Embarked')
        
        # display the dataset
        st.dataframe(df, use_container_width=True)  

        #load the data and the labels
        X = df.values[:,0:-1]
        y = df.values[:,-1].astype(int)            
        
        # Split the dataset into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, \
            test_size=0.2, random_state=42)

        # Create the logistic regression 
        clf = LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
                        intercept_scaling=1, max_iter=100, multi_class='multinomial',
                        n_jobs=1, penalty='l2', random_state=42, solver='lbfgs',
                        tol=0.0001, verbose=0, warm_start=False)

        clf.fit(X_train,y_train)

        # Test the classifier on the testing set
        accuracy = clf.score(X_test, y_test)
        st.write('accuracy = ' + str(accuracy))
        st.text(classification_report(y_test, clf.predict(X_test)))
        
# Convert string data to numerical data
def labeltonumeric(df, column):
    from sklearn.preprocessing import LabelEncoder
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])
    return df



#run the app
if __name__ == "__main__":
    app()
