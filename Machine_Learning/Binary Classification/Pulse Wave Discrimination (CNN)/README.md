# **Pulse Crime Discrimination Using CNN**  

## **Project Overview**  
This project focuses on classifying scintillation signals from a scintillator material to distinguish between two types of signals:  
- **Li6 signals**: The target signals we want to recognize.  
- **Po signals**: The background contamination that needs to be filtered out.  
Additionally, a **third dataset** (Phys) contains real-world signals consisting of both Li6 and Po responses.  

The goal is to build a **Convolutional Neural Network (CNN)** to classify these signals with an accuracy **above 80%**, ensuring that **Po contamination does not exceed 5%** while maximizing the retention of Li6 signals.  

## **Data**  

### **Provenance & Sources**  
The dataset consists of scintillation response signals collected from experimental measurements. The signals represent energy depositions in a scintillator material and are categorized as:  
1. **Li6.npz** – The desired signal.  
2. **Po.npz** – The background contamination to be filtered out.  
3. **Phys.npz** – A mixed dataset containing both Li6 and Po signals.  

The dataset was preprocessed to extract key features that help in distinguishing the two types of signals.  

### **Collection Methodology**  
The signals were collected from a detector using real-time pulse measurements. These measurements were then digitized and stored as numerical arrays. Exploratory data analysis was conducted to:  
- Identify key differences between **Li6** and **Po** signals.  
- Select the most relevant input format for model training.  
- Choose an appropriate dataset split for training, validation, and testing.  

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
