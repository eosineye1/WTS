FROM python:3.7
EXPOSE 8501
RUN pip3 install streamlit
RUN pip3 install pandas
RUN pip3 install numpy
RUN pip3 install nltk
RUN pip3 install re
RUN pip3 install networkx
COPY . .
CMD streamlit run main.py
