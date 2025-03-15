# Diabetes Binary Classification

## Project Overview:
The **Diabetes Prediction** dataset is a collection of medical and demographic data from patients, along with their diabetes status (positive or negative). The dataset contains several features that capture the patient's health and lifestyle, including:

- **Age**: The age of the patient.
- **Gender**: The gender of the patient.
- **Body Mass Index (BMI)**: The patient's BMI, which is an indicator of body fat.
- **Hypertension**: Whether the patient has high blood pressure.
- **Heart Disease**: Whether the patient has a history of heart disease.
- **Smoking History**: Whether the patient has a history of smoking.
- **HbA1c Level**: The level of hemoglobin A1c, a marker for long-term blood glucose control.
- **Blood Glucose Level**: The patient's blood glucose levels, which are important indicators of diabetes.

This dataset can be used to build **machine learning models** that predict diabetes in patients based on their medical history and demographic information. The goal is to create a predictive model that can help healthcare professionals identify individuals who may be at risk of developing diabetes, enabling earlier intervention and personalized treatment plans.

Additionally, this dataset offers valuable insights for researchers interested in exploring the relationships between various medical and demographic factors and the likelihood of developing diabetes. By analyzing the dataset, researchers can gain a deeper understanding of the risk factors associated with diabetes and improve the accuracy of predictive models used in clinical settings.

This project uses **Artificial Neural Networks (ANNs)** to train a binary classification model for diabetes prediction based on the provided features.

## Data

The **Diabetes Prediction** dataset is sourced from **Electronic Health Records (EHRs)**, which contain comprehensive patient health information, including medical history, diagnosis, and treatment details. The data was collected from multiple healthcare providers and aggregated into a single dataset. It includes demographic and clinical features like age, gender, BMI, hypertension, heart disease, smoking history, HbA1c level, and blood glucose level.

The data was cleaned and preprocessed to ensure accuracy and consistency. EHRs provide a longitudinal view of patients' health, making the dataset valuable for identifying patterns and trends, and developing machine learning models relevant to real-world healthcare settings.

## Project Structure

The project is organized into the following directories and files:

- **images/**: This folder contains plots generated during the model training process:
  - Loss and accuracy plots for the training of the Artificial Neural Network (ANN) model.
  - Bar plots visualizing the feature relevance estimation for predicting diabetes.

- **code/**: This folder contains the Python script and Jupyter notebook for the project:
  - **`diabetes_prediction.ipynb`**: A Jupyter notebook that trains the ANN model, preprocesses the data, and includes detailed commentary on each step of the process. It explains the model-building process, data cleaning, and evaluation of the model.

- **data/**: This folder contains the diabetes dataset used in the project. It includes the features related to patient health and demographic information.

Each part of the project is organized to support the workflow of data preprocessing, model training, and evaluation, along with visualizations that help in understanding the model's performance and feature importance.


