# **Iris Flower Classification using K-Means Clustering**  

## **Project Overview**  
This project applies **K-Means Clustering**, an **unsupervised machine learning algorithm**, to classify different species of the **Iris flower dataset**. Despite being an **unsupervised approach**, we evaluated the clustering results by identifying the **majority species in each cluster**, allowing us to compute an accuracy score.  

### **Objective**  
- Use **K-Means Clustering** to group the Iris dataset into three clusters.  
- Compare the predicted clusters with the actual species labels.  
- Compute an **accuracy score** based on the majority species assigned to each cluster.  

## **Data**  

### **Provenance & Sources**  
The **Iris flower dataset** is a well-known **multivariate dataset** introduced by **Ronald Fisher** in his 1936 paper *"The Use of Multiple Measurements in Taxonomic Problems."* It was originally collected by **Edgar Anderson** to quantify the **morphologic variation** of three related Iris species.  

This dataset is **publicly available** at the **UCI Machine Learning Repository**.  

### **Dataset Description**  
The dataset consists of **150 samples** divided equally into three species:  
1. **Iris Setosa**  
2. **Iris Virginica**  
3. **Iris Versicolor**  

Each sample has **four numerical features**:  
- **Sepal Length** (cm)  
- **Sepal Width** (cm)  
- **Petal Length** (cm)  
- **Petal Width** (cm)  

Additionally, the dataset includes a **target label** specifying the species.  


## **Model & Training Approach**  
### **Data Preprocessing & Splitting**  
- **Feature Selection**: Used all **four numerical features** (Sepal & Petal Length/Width).  
- **Scaling**: Standardized the features to improve K-Means performance.  
- **Dataset Split**:  
  - **Training Set** – 70% of the data  
  - **Test Set** – 30% of the data  
  *(Note: While K-Means is unsupervised, splitting the dataset helps evaluate clustering performance.)*  

### **Clustering Algorithm: K-Means**  
- **Number of Clusters (K)**: 3 (corresponding to the three Iris species).  
- **Initialization**: K-Means++ for optimal centroid selection.  
- **Iteration**: The model assigns each sample to the nearest centroid and updates cluster centers until convergence.  

### **Evaluation Strategy**  
- Since K-Means does not use true labels, we assigned a **majority species** to each cluster.  
- We compared the predicted species labels with the actual dataset labels.  
- Computed **accuracy** based on the percentage of correctly assigned samples.  

## **Results**  
- **Final Accuracy**: Approximately **89%**, indicating that K-Means successfully identified meaningful clusters.  
- **Cluster Analysis**:  
  - **Iris Setosa** was the easiest to differentiate.  
  - **Iris Virginica and Iris Versicolor** had some overlap due to similar feature distributions.  

## **Conclusion**  
This project demonstrates how **unsupervised learning** can still be evaluated using labeled data. The results indicate that **K-Means Clustering** is an effective method for classifying species in the **Iris dataset** with high accuracy.  

### **Potential Improvements**  
- Experimenting with **PCA** for dimensionality reduction before clustering.  
- Using **Gaussian Mixture Models (GMM)** to capture soft probabilities instead of hard clustering.  
- Applying **Hierarchical Clustering** for comparison.  



