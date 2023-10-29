# Prediction of Iris Species Using K-Nearest Neighbors Algorithm

## Project Overview
In this project, aim to accurately predict the species of iris flowers based on the physical attributes of their flowers. I utilize the K-Nearest Neighbors (KNN) algorithm, a versatile machine learning technique, to predict based on the 'distance' between feature values.

## Dataset
Using the renowned "Iris" dataset, frequently cited in pattern recognition literature. The dataset comprises 150 records across five attributes:
- Petal length
- Petal width
- Sepal length
- Sepal width
- Species

The dataset includes three species of iris (Iris setosa, Iris virginica, and Iris versicolor). With 50 instances per species, it offers a balanced dataset for prediction.

## Tools and Technology
- **Programming Language:** Python (chosen for its comprehensive support and libraries tailored for machine learning and data manipulation.)
- **Libraries:** 
  - scikit-learn (for machine learning algorithms including KNN)
  - Pandas (for data manipulation)
  - Matplotlib/Seaborn (for data visualization)

## Methodology

### 1. Data Exploration and Visualization
- Load the dataset and understand its structure.
- Obtain statistical summaries of the features.
- Employ visual aids like scatter plots, histograms, and perhaps pair plots to interpret the relationships in the dataset.

### 2. Data Preprocessing
- Inspect for missing values.
- Normalize data ensuring the KNN algorithm, which is dependent on distance measures, can accurately predict.

### 3. Model Development
- Implement the K-Nearest Neighbors algorithm.
- Divide the dataset into training and test subsets. A common ratio is 70% training data to 30% test data.

### 4. Parameter Tuning
- Utilize cross-validation to determine the optimal number of neighbors (k) in the KNN algorithm.

### 5. Model Evaluation
- Evaluate using metrics suited for classification tasks: accuracy, precision, recall, and the F1 score.
- Implement a confusion matrix to provide a visual representation of the algorithm's performance across different classes.

### 6. Reporting
- Document the procedure and the results.
- Delve into the findings, emphasizing the optimal number of neighbors identified and the resulting accuracy.
- Propose recommendations and areas for future research, like exploring other algorithms or considering supplementary features.

## Conclusion
![image](https://github.com/mosigaaa/Prediction-Iris-species-dataset-on-KNN-prediction/assets/132208415/a8efa552-259c-40eb-96be-5011521d2619)

Based on the plot, the optimal values for 'K' in this dataset appear to be around 6, 13, and 18, where the prediction accuracy peaks. Among these, \( K approxmately 6 \) seems to provide the highest accuracy, making it the most optimal value for 'K'. However, it's important to note that selecting the smallest 'K' value with the highest accuracy can be preferable as it often yields a simpler, more interpretable, and faster model. Therefore, for this dataset and based on the provided graph, \( K = 6 \) is recommended as the optimal choice for achieving the best accuracy using the K-Nearest Neighbors algorithm.

This project exemplifies the entirety of the machine learning workflow, from data comprehension to model execution. It is an ideal foundational venture for individuals aiming to explore data science and machine learning. The K-Nearest Neighbors algorithm, with its straightforwardness, serves as an ideal tool for grasping the fundamental concepts of machine learning classification tasks.

Engaging in this project provides a hands-on understanding of the workings of the K-Nearest Neighbors algorithm and its applicability in real-world situations. Moreover, this project lays the groundwork for more intricate applications and a plethora of other machine learning algorithms and techniques.
