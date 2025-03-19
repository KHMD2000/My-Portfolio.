# **Boston Housing Price Prediction Using ANN**  

## **Project Overview**  
This project aims to predict the price of houses in Boston using an **Artificial Neural Network (ANN)** regression model. The model takes in key features related to housing conditions and economic factors to estimate the cost of a house.  

### **Objective**  
- Build a regression model using an ANN to predict house prices.  
- Evaluate model performance based on **Mean Squared Error (MSE)**.  


## **Data**  

### **Provenance & Sources**  
The dataset is sourced from the **UCI Machine Learning Repository** and originates from the **Boston Housing Dataset**, collected in **1978**. It consists of **506 samples**, each representing aggregated housing information from different suburbs in **Boston, Massachusetts**.  

### **Dataset Description**  
The dataset contains **14 features**, but for this project, we focus on the following key predictors:  
- **RM**: Average number of rooms per dwelling.  
- **LSTAT**: Percentage of lower-status population.  
- **PTRATIO**: Pupil-teacher ratio by town.  

The target variable is the **median house price** in **$1,000s**.  

## **Model & Training Approach**  
### **Data Preprocessing & Splitting**  
- **Feature Selection**: Focused on the most impactful features (**RM, LSTAT, PTRATIO**).  
- **Normalization**: Scaled the selected features to improve model performance.  
- **Dataset Split**:  
  - **Training Set** – 80% of the data  
  - **Validation Set** – 10% of the data  
  - **Test Set** – 10% of the data  

### **Model Architecture**  
A **Fully Connected Artificial Neural Network (ANN)** was used, consisting of:  
- **Input Layer**: 3 neurons (one for each selected feature).  
- **Hidden Layers**: Multiple dense layers with **ReLU activation**.  
- **Output Layer**: A single neuron for regression (linear activation).  

### **Training Strategy**  
- **Loss Function**: **Mean Squared Error (MSE)** for regression.  
- **Optimizer**: **Adam** optimizer for adaptive learning.  
 

## **Results**  
- **Training & Validation Loss**: The loss consistently decreased, showing good generalization.  
- **Prediction Performance**:  
  - The model predicts house prices with an **average estimation error of ±$45,000**.  
  - Predictions closely align with actual prices but still have some variance.  

## **Conclusion**  
This project successfully implemented an **ANN-based regression model** for house price prediction. Despite achieving reasonable accuracy, further improvements could be made by:  
- Incorporating additional features.  
- Experimenting with different architectures.  
- Using ensemble methods to refine predictions.  

