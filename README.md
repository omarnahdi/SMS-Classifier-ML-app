# SMS Classifier ML App

## Overview

The **SMS Classifier ML App** is a machine learning application that classifies SMS messages as either **spam** or **ham** (not spam) using natural language processing (NLP) techniques. Built with **Streamlit**, this app provides a user-friendly interface for users to input SMS messages and receive instant predictions.

watch live [![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://omar-nahdi-sms-classifier.streamlit.app/)

## Features

- **User Input**: Users can enter SMS messages through a simple text area.
- **Real-time Classification**: The app uses a trained machine learning model to classify messages as spam or ham.
- **Feedback**: Displays whether the input message is detected as spam or not.
- **Model Training**: Built on a machine learning model trained with various SMS datasets.

## Technologies Used

- **Streamlit**: A Python library for creating web applications.
- **Natural Language Processing (NLP)**: For processing and understanding text data.
- **Machine Learning**: To classify messages based on training data.
- **Pandas**: For data manipulation and analysis.
- **Scikit-Learn**: For building and evaluating machine learning models.

## Installation

### Prerequisites

Make sure you have Python 3.x installed on your machine. You will also need to install the following packages:

- Streamlit
- NLTK (Natural Language Toolkit)
- Scikit-Learn
- Pandas

### Steps to Install

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/sms-classifier-app.git
   cd sms-classifier-app
   ```
2. Install the required packages:
  ```python
  pip install -r requirements.txt
  ```
3. Download NLTK data (if not already installed):
  ```python
  import nltk
  nltk.download('punkt')
  nltk.download('stopwords')
  ```
4. Run the Streamlit app:
```python
streamlit run main.py
```
5. Open your web browser and navigate to ```http://localhost:8501``` to access the app.

## Contact
For any inquiries or feedback, please contact me:

- Email: omarnahdi2021@gmail.com
- LinkedIn: [LinkedIn](https://www.linkedin.com/in/omarnahdi/)

