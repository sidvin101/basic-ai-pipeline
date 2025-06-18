# basic-ai-pipeline

This AI Pipeline allows for the user to upload a file, select the columns for features and labels, and runs it accordingly. 

AI Pipeline:
- Preprocesses Data
- Scales Data
- Runs a Logistic Regression Model
- Displays the Classification Report

If the deployment does not work, please download this repo, and run app.py locally.

# Complexity
- File Upload with Validation
- Handles Sessions with Flask
- Web UI for Feature Selection and Parameter tuning
- Preprocessing and Splitting
- Model Training
- Evaluation Metrics

# Big O
- File Upload: O(1)
- Reading the csv file: O(n), where n is the number of rows
- Feature Scaling: O(n), where n is the number of rows while d is the number of feeatures
- Data Splitting: O(n)
- Logistic Regression: O(n*d*k), where k is the number of iterations and d is the number of selected features
- Classification Report: O(n*d)
