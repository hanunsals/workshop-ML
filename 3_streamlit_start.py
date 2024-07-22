from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
 
# Load dataset
iris = load_iris()
X, y = iris.data, iris.target
 
# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
 
# Train a Random Forest Classifier
model = RandomForestClassifier()
model.fit(X_train, y_train)
 
import streamlit as st
import numpy as np
 
 
# Define the layout of the app
st.title("Iris Flower Prediction App")
 
# Create input fields for user input
st.sidebar.header("Input Features")
sepal_length = st.sidebar.slider("Sepal Length", 4.0, 8.0, 5.0)
sepal_width = st.sidebar.slider("Sepal Width", 2.0, 4.5, 3.0)
petal_length = st.sidebar.slider("Petal Length", 1.0, 7.0, 3.5)
petal_width = st.sidebar.slider("Petal Width", 0.1, 2.5, 1.0)
 
# Make a prediction
features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
prediction = model.predict(features)
prediction_proba = model.predict_proba(features)
 
# Display the prediction
st.subheader("Prediction")
iris_species = ['Setosa', 'Versicolor', 'Virginica']
st.write(f"The predicted species is: {iris_species[prediction[0]]}")
 
# Display the prediction probabilities
st.subheader("Prediction Probabilities")
st.write(f"Setosa: {prediction_proba[0][0]:.2f}")
st.write(f"Versicolor: {prediction_proba[0][1]:.2f}")
st.write(f"Virginica: {prediction_proba[0][2]:.2f}")