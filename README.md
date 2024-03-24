# PDF Sentence Comparer

PDF Sentence Comparer is a Python tool designed to find the most semantically similar sentence to a given input sentence within a PDF document, including the page number where this sentence can be found. It leverages the powerful natural language processing capabilities of spaCy and the PDF text extraction features of PyMuPDF (Fitz).

## Features

- Extracts text from PDF documents.
- Utilizes NLP to analyze and compare sentence semantics.
- Finds and returns the most similar sentence to a given input, along with its page number in the PDF.

### Installation

This project requires Python 3.8+ and pip for installation. Follow these steps to install the necessary dependencies:

1. Clone the repository
`git clone https://github.com/eksen1907/FindSimilarSentenceInFrench-English.git`
2. Install Python packages
`pip install -r requirements.txt`

### Dependencies
- spaCy
- PyMuPDF (Fitz)
- You'll also need to download a spaCy language model. For English, you can use:
`python -m spacy download en_core_web_md`

## Usage

- To use the code, replace 'PATH' with the path to your PDF file.
- Run the script from the command line. You will be prompted to enter a sentence

## Authors
* Umut Tulay - [eksen1907](https://github.com/eksen1907) with ChatGPT
