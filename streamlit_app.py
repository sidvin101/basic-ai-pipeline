import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report

st.set_page_config(page_title="Logistic Regression App", layout="wide")
st.title("Logistic Regression App")

#File upload
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("File uploaded successfully!")

    # Diplays the features and target variable selection
    st.subheader("Select Features and Target Variable")
    columns = df.columns.tolist()
    selected_features = st.multiselect("Select Features", columns, default=columns[:-1])
    target = st.selectbox("Select Target Variable", columns)

    # Display hyperparameters
    st.subheader("Hyperparameters")
    C = st.number_input("Regularization Strength (C)", min_value=0.01, max_value=10.0, value=1.0, step=0.01)
    max_iter = st.number_input("Maximum Iterations", min_value=50, max_value=500, value=100, step=10)
    solver = st.selectbox("Solver", ["lbfgs", "liblinear", "sag", "saga"])

    #trains the model
    if st.button("Train Model"):
        try:
            X = df[selected_features]
            y = df[target]

            # Split the data
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # Standardize the features
            scaler = StandardScaler()
            X_train = scaler.fit_transform(X_train)
            X_test = scaler.transform(X_test)

            # Train the model
            model = LogisticRegression(C=C, max_iter=max_iter, solver=solver)
            model.fit(X_train, y_train)

            # Make predictions
            y_pred = model.predict(X_test)

            # Display results
            accuracy = accuracy_score(y_test, y_pred)
            report = classification_report(y_test, y_pred)

            st.subheader("Model Performance")
            st.write(f"Accuracy: {accuracy:.2f}")
            st.text(report)

        except Exception as e:
            st.error(f"An error occurred: {e}")
else:
    st.info("Please upload a CSV file to get started.")
