# basic-ai-pipeline

This AI Pipeline allows for the user to upload a file, select the columns for features and labels, and runs it accordingly. 

AI Pipeline:
- Preprocesses Data
- Scales Data
- Runs a Logistic Regression Model
- Displays the Classification Report
- Has Retry Mechanisms in case of an error

How to Run this code locally
- Clone this repo
- Install requirements.txt
- run app.py

Alternatively, if you would like to run the application without having to take the steps to run locally, please use this Streamlit link: https://basic-ai-pipeline.streamlit.app/ 
* Note that this doesn't include some features as with the Flask application

Architecture
```
basic-ai-pipeline
|- /templates
|  - index.html //The UI for file uploading
|  - select_columns.html // The UI for column and hyperparameter selection
|  - results // The UI to display the Logistic Regression results
|- /uploads // A temporary folder to store the file uploads
|- app.py // The main Flask app
|- streamlit_app.py // The main Streamlit app
|- requirements.txt // The list of requirementrs

```

# Flow
- File Upload with Validation
- Handles Sessions with Flask
- Web UI for Feature Selection and Parameter tuning
- Preprocessing and Splitting
- Model Training
- Evaluation Metrics
- Retry Mechanism

# Big O
- File Upload: O(1)
- Reading the csv file: O(n), where n is the number of rows
- Feature Scaling: O(n), where n is the number of rows while d is the number of feeatures
- Data Splitting: O(n)
- Logistic Regression: O(n*d*k), where k is the number of iterations and d is the number of selected features
- Classification Report: O(n*d)
