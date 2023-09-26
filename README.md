# Credit-Card-Fraud
This project utilizes logistic regression and machine learning to identify credit card fraud. It learns from transaction data to distinguish between genuine and fraudulent transactions. In real-time, it assesses new transactions using learned patterns, aiding in fraud prevention.
# Credit Card Fraud Detection

[![Project Status](https://img.shields.io/badge/status-completed-brightgreen)](https://colab.research.google.com/drive/1dYiQgfYHk53UMyt0WROINGpnGmuLu0dR?usp=sharing)

This project implements machine learning techniques to detect credit card fraud. By analyzing transaction data, the system learns patterns and characteristics of legitimate and fraudulent transactions. When a new transaction occurs, the model assesses its likelihood of being fraudulent based on these patterns, thereby helping prevent fraudulent activities in real-time.

## Table of Contents
- [Overview](#overview)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Contributing](#contributing)

## Overview

Credit card fraud is a significant concern in today's digital world. This project aims to develop a robust fraud detection system using machine learning. The model is trained on a dataset containing historical credit card transaction data, allowing it to identify suspicious patterns and detect potential fraudulent transactions.

## Dataset

The dataset used for this project contains transaction records, including features like time, transaction amount, and various anonymized features (V1, V2, ..., V28). The target variable is "Class," where 0 represents legitimate transactions, and 1 represents fraudulent transactions.

## Installation

1. Clone this repository:
   
   git clone https://github.com/SrSurajithPranav/credit-card-fraud-detection.git
   

2. Install the required dependencies:
   
   pip install -r requirements.txt
   

## Usage

1. Place your credit card transaction dataset in the project directory.
2. Run the Jupyter Notebook or Python script to train and test the fraud detection model.
3. Evaluate the model's performance and make predictions on new transactions.

## Results

- Training Accuracy: 99.92%
- Testing Accuracy: 99.91%

The model demonstrates high accuracy in identifying fraudulent transactions while minimizing false positives.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please create a pull request.

