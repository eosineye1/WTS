# WTS [![version][version-badge]][CHANGELOG]
---
[![Run on Ainize](https://ainize.ai/images/run_on_ainize_button.svg)](https://ainize.web.app/redirect?git_repo=https://github.com/eosineye1/WTS)

Github: [WTS](https://github.com/eosineye1/WTS)

Model: [Weighted Text Summarizr](https://ainize.ai/eosineye1/WTS?branch=main)

## Aim

The goal of WTS is to be a model that produces a compact and coherent summary while preserving key information content and overall meaning.

## Problem

Having to read a large body of text to get a conscise and conherent summary.

## Solution

Asummarization model that take a large body of text and creates a summary.

Two different approaches are used for Text Summarization - extractive Summarization and abstractive Summarization. WTS utilizes extractive summarization. In extractive summarization, we are identifying important phrases or sentences from the original text and extract only these phrases from the text. These extracted sentences would be the summary.


## Terminal Commands

1. Install Python from [Python Official Page](https://www.python.org/).
2. Open Terminal
3. Go to your file project
4. Run in terminal: ```pip install streamlit``` 
5. Run in terminal: ```pip3 install streamlit```
6. Run in terminal: ```pip3 install nltk```
7. Run in terminal: ```python3 -m nltk.downloader punkt``
8. Run in terminal: ```streamlit run app.py```
9. Navigate to [localhost:8501](http://localhost:8501/)

endpoint : [On Ainize](https://main-wts-eosineye1.endpoint.ainize.ai/)

### Sample datasets

You can find sample articles in file ```article.txt```.

### What's included

Within the download you'll find the following directories and files:

```
WTS
├── Dockerfile
├── app.py
├── logo.png
├── msft.txt
├── Swagger.yaml
└── README.md
```

## Useful Links

Streamlit: <https://www.streamlit.io/>

Linkedin: <https://www.linkedin.com/in/eniolaosineye/>

Portfolio: <http://osineye.com>

[CHANGELOG]: ./CHANGELOG.md
[version-badge]: https://img.shields.io/badge/version-1.0.0-blue.svg

