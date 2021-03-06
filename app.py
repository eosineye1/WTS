import streamlit as st
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize


@st.cache(suppress_st_warning=True)
def generate_summary(text):
    stopWords = [ "i","me","my","myself","we","our","ours","ourselves","you","your","yours","yourself","yourselves","he","him","his","himself","she","her","hers","herself","it","its","itself","they","them","their","theirs","themselves","what","which","who","whom","this","that","these","those","am","is","are","was","were","be","been","being","have","has","had","having","do","does","did","doing","a","an","the","and","but","if","or","because","as","until","while","of","at","by","for","with","about","against","between","into","through","during","before","after","above","below","to","from","up","down","in","out","on","off","over","under","again","further","then","once","here","there","when","where","why","how","all","any","both","each","few","more","most","other","some","such","no","nor","not","only","own","same","so","than","too","very","can","will","just","don't","should","now"]
    words = word_tokenize(text)

    # Creating a frequency table to keep the score of each word

    freqTable = dict()
    for word in words:
        word = word.lower()
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1

    # Creating a dictionary to keep the score of each sentence
    sentences = sent_tokenize(text)
    sentenceValue = dict()

    for sentence in sentences:
        for word, freq in freqTable.items():
            if word in sentence.lower():
                if sentence in sentenceValue:
                    sentenceValue[sentence] += freq
                else:
                    sentenceValue[sentence] = freq

    sumValues = 0

    for sentence in sentenceValue:
        sumValues += sentenceValue[sentence]

    # Average value of a sentence from the original text
    average = int(sumValues / len(sentenceValue))

    # Storing sentences into our summary
    summary = ''
    for sentence in sentences:
        if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
            summary += " " + sentence

    return summary


try:
    text_min_length = 250
    st.image("logo.png")
    st.header('Weighted Text Summarizer (WTS)')
    txt = st.text_area('Paste text here:', height=500)
    article_length = len(txt.strip())
    st.write('Length of input is: {}'.format(article_length))
    if article_length > text_min_length:
        summary_sentence = generate_summary(txt)
        summary_sentence_length = len(summary_sentence)
        st.write("")
        st.write("Summary:\n\n{}\n".format(summary_sentence))
    elif article_length < text_min_length and article_length != 0:
        st.warning(
            "Text length must be at least {} characters long.".format(text_min_length))
except:
    st.error("Beep bop! Something went wrong.")
