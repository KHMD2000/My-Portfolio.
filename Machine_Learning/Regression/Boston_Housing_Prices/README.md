
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
- **Stopping Criteria**: The model training was stopped when validation loss plateaued to prevent overfitting.  

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

