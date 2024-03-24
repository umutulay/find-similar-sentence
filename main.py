from find_similar_sentence import find_most_similar_sentence
from french_to_english import french_to_english

if __name__ == "__main__":
    input_sentence = input("Enter the French sentence to compare: ")
    translated_version = french_to_english(input_sentence)
    print (translated_version)

    if translated_version is not None:
        most_similar_sentence, page_number = find_most_similar_sentence(translated_version)
        print(f"Most similar sentence: \"{most_similar_sentence}\" found on page {page_number}")
    else:
        print("Translation was unsuccessful or returned an empty response.")
