from joblib import load
import streamlit as st
import nltk
from nltk.corpus import stopwords
import string
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
nltk.download('punkt_tab')
nltk.download('punkt')
nltk.download('stopwords')

transformer = load('transformer.joblib')
model = load('Spam_model.joblib')
#
def transformed_text(text):
  text = str(text)
  text = text.lower()
  text = nltk.word_tokenize(text)
  grp = []
  for i in text:
    if i.isalnum():
      grp.append(i)

    text = grp[:]
    grp.clear()
    for i in text:
      if i not in stopwords.words('english') and string.punctuation:
        grp.append(i)
    text = grp[:]
    grp.clear()
    for i in text:
      grp.append(ps.stem(i))
  return " ".join(grp)

st.header('Spam Detection ML Model')

st.write('Introducing ****SpamShield****, a robust AI-driven spam detection model developed by ****Omar Nahdi****. This model leverages advanced natural language processing (NLP) '
         'and machine learning algorithms to accurately identify and filter out spam across various communication channels. '
         'Designed for high precision and minimal false positives, SpamShield aims to create a cleaner, '
         'safer environment for online communities and platforms.')

msg = st.text_area("Enter the message here").strip()

if st.button('Predict'):
    if not msg:
        st.write("Type a message")
    else:
        transformed_msg = transformed_text(msg)  # Pass msg directly as a string
        if not transformed_msg:  # Check if transformed message is empty
            st.write("No meaningful content found. Type a message.")
        else:
            # Transform for the model
            model_input = transformer.transform([transformed_msg])  # Wrap in a list for the model
            pred = model.predict(model_input)
            if pred == 1:
                st.warning('️⚠️️Spam Detected⚠️')
            elif pred == 0:
                st.success('✅Not Spam Message')
            else:
                st.error("An error occurred")
