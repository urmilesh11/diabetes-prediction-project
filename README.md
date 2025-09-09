🩺 Diabetes Prediction System using SVM:

A machine learning project that predicts whether a person is diabetic based on medical attributes using the PIMA Indian Diabetes dataset and a Support Vector Machine (SVM) classifier.

📊 Dataset Overview:

This project uses the PIMA Diabetes Dataset, which contains diagnostic measurements of female patients of Pima Indian heritage. The dataset includes:
- 768 samples
- 8 medical features:
- Pregnancies
- Glucose
- BloodPressure
- SkinThickness
- Insulin
- BMI
- DiabetesPedigreeFunction
- Age
- Outcome: 0 (Non-diabetic), 1 (Diabetic)

⚙️ Technologies Used
- Python 🐍
- NumPy
- Pandas
- Scikit-learn
- Jupyter/Colab Notebook

🧠 ML Workflow
- Data Loading & Exploration:
 
   Read CSV using pandas.
  
   Analyze distribution and statistics.
  
   Visualize outcome classes.
  
- Preprocessing:
  
    Feature scaling using StandardScaler.
  
    Train-test split with stratification.
  
- Model Training:
  
   Support Vector Machine (SVM) with linear kernel.
  
   Fit on training data.
  
- Evaluation:
  
   Accuracy on training set: ~78.6%
  
   Accuracy on test set: ~77.3%
  
- Prediction System:
  
    Accepts user input.
  
    Standardizes features.
  
    Predicts diabetic status.


