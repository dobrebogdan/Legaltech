import spacy
from stop_words import get_stop_words

stop_words = get_stop_words('ro')

nlp = spacy.load("ro_core_news_sm")

# method that turns a text into a list of lemmatized words (tokens).
def text_to_tokens(curr_str):
    # removal of punctuation and other characters from the text
    for i in range(0, len(curr_str)):
        if (not curr_str[i] == " ") and (not curr_str[i].isalpha()):
            curr_str = curr_str.replace(curr_str[i], " ")


    # turining the text to lowercase
    curr_str = curr_str.lower()

    # Returns an object of type Doc, which is a sequence of Token objects
    tokens = nlp(curr_str)
    # A list of valid tokens
    good_tokens = []
    for token in tokens:
        # Gets the lemmatized token from the Token object
        lemma = token.lemma_
        # Checks token validity
        if lemma == "" or lemma in stop_words:
            continue
        # Adds token to list
        good_tokens.append(lemma)
    return good_tokens


def text_to_coords(model, curr_str):
    # get the lemmatized tokens from text
    tokens = text_to_tokens(curr_str)
    # the sum vector of all vectors of words that are found in the model's vocabulary
    sum = []
    cnt = 0.0
    for i in range(0, len(tokens)):
        if sum == []:
            # if the sum vector is empty, try to initialize it with the vector of the current word
            # if it exists in the model's vocabulary
            try:
                sum = model.wv[tokens[i]].copy()
                cnt += 1.0
            except:
                pass
        else:
            # try to add the vector for the current word to the sum of vectors if the world
            # exists in the model's vocabulary
            try:
                sum += model.wv[tokens[i]]
                cnt += 1.0
            except:
                pass

    # divide to the number of words that exist in the model's vocabulary to get the average
    sum = sum / cnt
    return sum
