import streamlit as st
import pandas as pd
import numpy as np
import nltk
import nltk.data
nltk.download('punkt')
import re
from nltk.corpus import stopwords
import networkx as nx
from nltk.tokenize import sent_tokenize
 
def read_article(file_name, txt):
    # file = open(file_name, "r")
    # sentences = file.readlines()
    # st.write(sentences)
    # # st.write([txt])
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    sentences = tokenizer.tokenize(txt)

    word_embeddings = {}
    f = open('glove.6B.100d.txt', encoding='utf-8')
    for line in f:
        values = line.split()
        word = values[0]
        coefs = np.asarray(values[1:], dtype='float32')
        word_embeddings[word] = coefs
    f.close()

    clean_sentences = pd.Series(sentences).str.replace("[^a-zA-Z]", " ")
    clean_sentences = [s.lower() for s in clean_sentences]
    stop_words = stopwords.words('english')
    def remove_stopwords(sen):
        sen_new = " ".join([i for i in sen if i not in stop_words])
        return sen_new
    clean_sentences = [remove_stopwords(r.split()) for r in clean_sentences]

    sentence_vectors = []
    for i in clean_sentences:
        if len(i) != 0:
            v = sum([word_embeddings.get(w, np.zeros((100,))) for w in i.split()])/(len(i.split())+0.01)
        else:
            v = np.zeros((100,))
        sentence_vectors.append(v)

    return [sentences, sentence_vectors]


def build_similarity_matrix(sentences, sentence_vectors):
    # Create an empty similarity matrix
    similarity_matrix = np.zeros((len(sentences), len(sentences)))

    from sklearn.metrics.pairwise import cosine_similarity
    for index1 in range(len(sentences)):
        for index2 in range(len(sentences)):
            if index1 != index2:
                similarity_matrix[index1][index2] = cosine_similarity(sentence_vectors[index1].reshape(1,100), sentence_vectors[index2].reshape(1,100))[0,0]
    
    return similarity_matrix

@st.cache(suppress_st_warning=True)
def generate_summary(file_name, txt, top_n=5):

    # Step 1 - Read text anc split it
    sentences, sentence_vectors = read_article(file_name, txt)

    # Step 2 - Generate Similary Martix across sentences
    sentence_similarity_martix = build_similarity_matrix(sentences, sentence_vectors)

    # Step 3 - Rank sentences in similarity martix
    sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_martix)
    scores = nx.pagerank(sentence_similarity_graph)

    # Step 4 - Sort the rank and pick top sentences
    ranked_sentence = sorted(((scores[i],s) for i,s in enumerate(sentences)), reverse=True)    
    print("Indexes of top ranked_sentence order are ", ranked_sentence) 

    return ranked_sentence
    
try:
    text_min_length = 250
    st.image("logo.png")
    st.header('Weighted Text Summarizer (WTS)')
    txt = st.text_area('Paste text here:', height=500)
    article_length = len(txt.strip())
    st.write('Length of input is: {}'.format(article_length))  
    
    if article_length > text_min_length:
        summary_sentence = generate_summary('msft.txt', txt, 2)
        summary_sentence_length = len(summary_sentence)
        st.write("")
        sentence_qty = st.slider('Sentence length of summary',  1, summary_sentence_length, 1)
        st.write("")
        st.write("Summary: \n")
        for i in range(sentence_qty):
            st.write("{}\n".format(summary_sentence[i][1]))
    elif article_length < text_min_length and article_length is not 0:
        st.warning("Text length must be at least {} characters long.".format(text_min_length))
except:
    st.error("Beep bop! Something went wrong.")



