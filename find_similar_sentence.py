import fitz  # PyMuPDF for PDF processing
import spacy
import re

def find_most_similar_sentence(input_sentence):
    """
    Finds and returns the most semantically similar sentence and its page number in a PDF.
    """
    # Load the medium English model from spaCy for NLP tasks
    nlp = spacy.load("en_core_web_md")
    
    # Path to the PDF document (to be replaced with the actual path)
    pdf_path = 'PATH'
    # Open the PDF document using PyMuPDF
    doc = fitz.open(pdf_path)

    # Lists to store sentences extracted from the PDF and their corresponding page numbers
    all_sentences = []
    sentence_pages = []

    # Iterate through each page in the PDF document
    for page_num in range(len(doc)):
        # Load the current page
        page = doc.load_page(page_num)
        # Extract text from the current page
        text = page.get_text()
        # Preprocess the text to replace non-terminal newlines with spaces
        text = re.sub(r'(?<![\.\?\!])\n', ' ', text)
        # Use spaCy to tokenize the preprocessed text into sentences
        spacy_doc = nlp(text)
        for sent in spacy_doc.sents:
            # Add the sentence and its page number to the lists
            all_sentences.append(sent.text.strip())
            sentence_pages.append(page_num)

    # Create a spaCy document for the input sentence to compare against the PDF sentences
    input_doc = nlp(input_sentence)

    # Initialize variables to track the most similar sentence found
    max_similarity = 0
    most_similar_sentence = None
    most_similar_page = None

    # Iterate over the sentences extracted from the PDF to find the most similar one
    for sentence, page_num in zip(all_sentences, sentence_pages):
        # Create a spaCy document for the current sentence
        sentence_doc = nlp(sentence)
        # Calculate the semantic similarity between the input sentence and the current sentence
        similarity = input_doc.similarity(sentence_doc)
        # Update tracking variables if the current sentence is more similar than the previous most similar
        if similarity > max_similarity:
            max_similarity = similarity
            most_similar_sentence = sentence
            most_similar_page = page_num

    # Return the most similar sentence found and its one-indexed page number
    return most_similar_sentence, most_similar_page + 1
