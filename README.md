![image](https://github.com/abdullahbh/ML-Voice-Assistant/assets/75631205/4399e03b-3b52-4409-98f1-73dd630542ba)


# RUHA - Roman Urdu Audio Analysis

## Introduction
In this project, I have developed a comprehensive audio analysis application named RUHA, which focuses on processing and classifying Roman Urdu audio commands using various machine learning models. The project extends upon my previous experience with the KNN classifier applied on the same dataset, advancing into more complex and varied classifiers to enhance prediction accuracy and broaden the analysis spectrum.

## Objective
The main goal of this project was to implement and compare five different classifiers on a Roman Urdu dataset to analyze audio commands effectively. Additionally, I aimed to develop a user-friendly web application using Flask to allow interactive user engagement and display the results of audio command analysis.

## Methods and Technologies
### Data Description
The dataset consists of Roman Urdu audio commands, providing a unique challenge in natural language processing specific to the Roman Urdu dialect.

### Machine Learning Models
I utilized the `sklearn` library to implement the following five classifiers:
- **Logistic Regression**
- **Decision Tree**
- **Support Vector Machine (SVM)**
- **Random Forest**
- **Neural Network**

Each model was trained on the dataset, and their performance was evaluated based on various metrics such as accuracy, precision, recall, F1-score, and confusion matrices.

### Web Application Development
The Flask framework was chosen due to its simplicity and efficiency in creating web applications. It allowed me to construct a straightforward yet effective interface for users to interact with the models by submitting audio commands and viewing the analysis results.

### Deployment
The application was deployed using Heroku, a cloud platform service, which enabled easy access to the app via the internet.

## Results
Each classifier was evaluated, and their performance metrics were carefully recorded. The results were as follows:
- **Accuracy**: Measures how often the classifier makes the correct prediction. It’s the ratio of the number of correct predictions to the total number of predictions.
- **Precision**: Indicates the proportion of positive identifications that were actually correct.
- **Recall**: Shows the proportion of actual positives that were identified correctly.
- **F1-Score**: A weighted average of precision and recall.

These metrics were displayed in the web application, providing users with insights into each model's performance.

## Challenges Encountered
One of the significant challenges was the processing of audio data, which required the extraction of features suitable for machine learning models. Another challenge was ensuring that the Flask application could handle live audio data efficiently and display results in real-time.

## Conclusion
The project successfully met the objectives by implementing multiple classifiers on a Roman Urdu dataset and developing a Flask web application for interactive user engagement. This experience has enhanced my understanding of machine learning applications in audio analysis and web development using Flask.

## Future Work
Improvements can be made in the area of real-time data processing and expanding the dataset to include more diverse Roman Urdu commands. Further, exploring deeper neural networks could potentially improve classification accuracy.

