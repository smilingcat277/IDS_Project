import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()


def transform_msg(Messages):
    Messages = Messages.lower()
    Messages = nltk.word_tokenize(Messages)

    x = []
    for i in Messages:
        if i.isalnum(): # It's alphabetically numeric.
            x.append(i)

    Messages  = x[:]  # bro you really dumb XDDDDD
    x.clear() # x = []

    for i in Messages:
        if i not in stopwords.words('english') and i not in string.punctuation:
            x.append(i)

    Messages  = x[:]
    x.clear() # x = []

    for i in Messages:
        x.append(ps.stem(i))   # Mujhe smjh nhi aya brother

    return " ".join(x)
        

tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

st.title("SMS Spam Classifier")

input_sms = st.text_area("Enter a message")

if st.button('Predict'):

    # 1. preprocess
    transformed_sms = transform_msg(input_sms)
    # 2. vectorize
    vector_input = tfidf.transform([transformed_sms])
    # 3. predict
    result = model.predict(vector_input)[0]
    # 4. Display, Bhai yahan par hum kuch zyada blunt language
    #    Nhi use kar rahe apne comments meh??? Yeh button hi toh
    #    hai.
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")