# find-similar-sentence

This Python tool is designed to find the most semantically similar sentence to a given input sentence (in French) within a PDF document (in English), including the page number where this sentence can be found.

## Features

- Translate input in French to English
- Extracts text from PDF documents.
- Utilizes NLP to analyze and compare sentence semantics.
- Finds and returns the most similar sentence to a given input, along with its page number in the PDF.

### Installation

This project requires Python 3.8+ (I used Python 3.11.8) and pip for installation. Follow these steps to install the necessary dependencies:

1. Clone the repository
`git clone https://github.com/umutulay/FindSimilarSentenceInFrench-English.git`
2. Install Python packages
`pip install -r requirements.txt`
3. You'll also need to download a spaCy language model. For English, you can use:
`python -m spacy download en_core_web_md`

### Dependencies
- spaCy
- PyMuPDF (Fitz)
- Transformers
- PyTorch
- sentencepiece
- sacremoses

## Usage

- To use the code, replace 'PATH' with the path to your PDF file.
- Run the script from the command line. You will be prompted to enter a sentence

## Authors
* Umut Tulay - [umutulay](https://github.com/umutulay)
