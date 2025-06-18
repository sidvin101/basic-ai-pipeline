import os
from flask import Flask, render_template, request, redirect, url_for, session
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
from werkzeug.utils import secure_filename
from sklearn.datasets import load_iris

#Creates a flask application
app = Flask(__name__)

#Upload folder configuration
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
app.config['UPLOAD_FOLDER'] = 'uploads'

#Creates a secret key for the session
app.secret_key = 'secret'  

#Only allows CSV's for the time being
ALLOWED_EXTENSIONS = {'csv'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get("file")
        #Uploads the file if it exists and is valid
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(filepath)
            df = pd.read_csv(filepath)

            session['filepath'] = filepath
            session['columns'] = df.columns.tolist()
            return redirect(url_for("select_columns"))
        # Exception if the file is not exist or invalid
        return render_template("index.html", error="Please upload a valid CSV file.")
    return render_template("index.html")

@app.route("/select", methods=["GET", "POST"])
def select_columns():
    columns = session.get('columns')
    if request.method == "POST":
        # Get the list of features from the csv and list them
        selected_features = request.form.getlist("features")
        target = request.form.get("target")

        # Allow the user to modify the params
        C = float(request.form.get("C", 1.0))
        max_iter = int(request.form.get("max_iter", 100))
        solver = request.form.get("solver", "lbfgs")

        try:
            #PIPELINE 
            df = pd.read_csv(session['filepath'])
            X = df[selected_features]
            y = df[target]

            # Preprocessing
            scaler = StandardScaler()
            X_scaled = scaler.fit_transform(X)

            #Data Splitting
            X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

            #Logistic Regression
            model = LogisticRegression(C=C, max_iter=max_iter, solver=solver)
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)

            #Displays the report
            accuracy = accuracy_score(y_test, y_pred)
            report = classification_report(y_test, y_pred)

            return render_template("results.html", accuracy=accuracy, report=report)
        except Exception as e:
            return render_template("select_columns.html", columns=columns, error=str(e))
    
    return render_template("select_columns.html", columns=columns)


if __name__ == "__main__":
    app.run(debug=True)
