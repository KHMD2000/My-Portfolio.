# **Temperature Prediction Using RNN**  

## **Project Overview**  
This project aims to predict the **room air temperature** for the next day based on historical temperature values using a **Recurrent Neural Network (RNN)**. The dataset consists of time-series temperature recordings from an **IoT device**, and the model is trained to capture patterns in these values.  

### **Objective**  
- Develop a **time-series forecasting model** to predict temperature for the next day.  
- Use a **Recurrent Neural Network (RNN)** to capture sequential dependencies.  
- Evaluate performance using **Mean Absolute Error (MAE)**.  

## **Data**  

### **Provenance & Sources**  
The dataset is generated using an **IoT device**, capturing **room air temperature** at different timestamps.  

### **Dataset Description**  
This dataset represents a **Univariate Time Series**, meaning it consists of a single variable (**temperature**) recorded at different time instances.  

The dataset contains two key features:  
1. **Hourly_Temp** – The mean **supply air temperature** in degrees Celsius per hour.  
2. **Datetime** – The timestamp indicating the date and hour of data recording.  

### **Time-Series Characteristics**  
- Each observation depends on previous values, making it essential to use sequential models like **RNNs**.  
- The dataset is a **special case of time series analysis**, where predictions rely only on **past temperature values** (no external features).  

## **Model & Training Approach**  
### **Data Preprocessing & Splitting**  
- **Feature Selection**: Used **Hourly_Temp** as the single feature for univariate time-series forecasting.  
- **Sequence Generation**: Created **input-output sequences** where each input represents a past sequence of temperature values, and the output is the **next day’s temperature**.  
- **Dataset Split**:  
  - **Training Set** – 80% of the data  
  - **Validation Set** – 10% of the data  
  - **Test Set** – 10% of the data  

### **Model Architecture**  
A **Recurrent Neural Network (RNN)** was implemented with the following layers:  
- **RNN Layer**: Captures temporal dependencies in the sequence data.  
- **Fully Connected Linear Layer**: Produces a single output for the predicted temperature.  

### **Training Strategy**  
- **Loss Function**: **Mean Absolute Error (MAE)** to measure prediction accuracy.  
- **Optimizer**: **Adam** optimizer for better convergence.  


## **Results**  
- **Training Loss**: **1.69** (meaning the model’s predictions are off by approximately **1.69°C** on average).  
- **Test Loss**: **0.74**, showing better generalization on unseen data.  

## **Conclusion**  
This project successfully implemented an **RNN-based time-series forecasting model** for temperature prediction. The results indicate reasonable accuracy, with the following possible improvements:  
- Experimenting with **LSTMs or GRUs** for better long-term memory.  
- Using **additional weather-related features** for improved performance.  
- Extending the forecast horizon beyond just one day.  


