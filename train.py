from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import AdaBoostClassifier
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
import numpy as np
import joblib
import pandas as pd

loan_df= pd.read_csv("loan_data_set.csv")

# Drop Loan_ID (not useful for prediction)
loan_df = loan_df.drop(columns=['Loan_ID'])

# Separate features and target
X = loan_df.drop(columns=['Loan_Status'])
y = loan_df['Loan_Status']

# Encode target variable
y = LabelEncoder().fit_transform(y)

# Identify categorical and numerical columns
categorical_cols = X.select_dtypes(include=['object']).columns.tolist()
numerical_cols = X.select_dtypes(include=[np.number]).columns.tolist()

# Preprocessing pipelines
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', LabelEncoder())  # We'll apply custom encoding in Streamlit due to fit requirements
])

numerical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

# Apply transformations
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_cols),
        # Categorical processing will be done manually in Streamlit for real-time input
    ])

# Fit preprocessing pipeline on numerical features only for model
X_num = preprocessor.fit_transform(X)

# Train AdaBoost model
X_train, X_test, y_train, y_test = train_test_split(X_num, y, test_size=0.2, random_state=42)
model = AdaBoostClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model and preprocessor
joblib.dump(model, 'adaboost_model1.pkl')
joblib.dump(preprocessor, 'preprocessor1.pkl')

# Output files to user for use in Streamlit app
model_path = "adaboost_model1.pkl"
preprocessor_path = "preprocessor1.pkl"


