
## **Model & Training Approach**  
### **Data Preprocessing & Splitting**  
- **Feature Extraction**: Initial exploratory analysis identified key discriminative features in the signal response.  
- **Data Format Selection**: The signals were transformed into a format suitable for CNN-based classification.  
- **Dataset Split**:  
  - **Training Set** – 80% of the data  
  - **Validation Set** – 10% of the data  
  - **Test Set** – 10% of the data  

### **Model Architecture**  
A **Convolutional Neural Network (CNN)** was chosen due to its ability to learn spatial patterns in signal data. The model consists of:  
- **Convolutional layers** to extract local features.  
- **Batch Normalization** to stabilize and accelerate training.  
- **Dropout Layers** to prevent overfitting.  
- **Pooling layers** to reduce dimensionality.  
- **Fully connected layers** for classification.  
- **Sigmoid output** for probability-based classification.  

### **Training Strategy**  
- **Loss Function**:  Binary Cross-entropy loss.  
- **Optimizer**: Adam optimizer with an adaptive learning rate.  
- **Metrics**: Accuracy, precision, recall.  

## **Results**  
- **Training & Validation Loss**: The loss consistently decreased, indicating good generalization.  
- **Test Accuracy**: The model achieved **~99% accuracy**.  
- **Po Contamination**: Controlled under the **5% threshold**, ensuring high purity of Li6 detection.  
- **Final Prediction on Phys Dataset**: Approximately **1,450 Li6 samples** were correctly identified.  

## **Uncertainty Estimation & Post-Processing**  
To further evaluate the model’s reliability:  
- **Monte Carlo Dropout** was used for uncertainty estimation.  
- **Uncertainty Distribution**: Most samples had uncertainty values between **0 and 0.01**, indicating high confidence in predictions.  
- **Probability Thresholding** was applied to optimize the trade-off between Li6 retention and Po contamination.  

## **Conclusion**  
This project successfully demonstrated the use of **CNNs for scintillation signal classification**, achieving high accuracy while maintaining **low contamination levels**. Future work can involve testing different architectures or incorporating additional uncertainty estimation techniques.  
