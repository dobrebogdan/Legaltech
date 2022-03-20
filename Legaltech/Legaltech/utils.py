import gensim
import spacy
from stop_words import get_stop_words
from nltk.stem.snowball import RomanianStemmer, EnglishStemmer

romanian_stemmer = RomanianStemmer()
english_stemmer = EnglishStemmer()


def replace_nonletters(curr_str):
    for i in range(0, len(curr_str)):
        if (not curr_str[i] == " ") and (not curr_str[i].isalpha()):
            curr_str = curr_str.replace(curr_str[i], " ")
    return curr_str


def replace_diacritics(curr_str):
    diacritics_pairs = [ ("Ă", "A"),  ("ă",  "a"), ("Â", "A"), ("â",  "a"), ("Î", "I"), ("î",  "i"), ("Ș", "S"),
                         ("ș", "s"), ("ş", "s"), ("Ț", "T"), ("ț", "t")]
    for curr_pair in diacritics_pairs:
        curr_str = curr_str.replace(curr_pair[0], curr_pair[1])
    return curr_str


def get_extended_stopwords(lang='ro'):
    stemmer = romanian_stemmer
    if lang == 'en':
        stemmer = english_stemmer
    stop_words = get_stop_words(lang)
    stop_words = [stemmer.stem(stop_word) for stop_word in stop_words]
    legal_stopwords = []
    # depending on how this function was ran, the relative path may be different
    try:
        with open(f'Legaltech/legal_stopwords_{lang}', 'r') as legal_stopwords_file:
            legal_stopwords.extend(legal_stopwords_file.read().split())
    except:
        with open(f'legal_stopwords_{lang}', 'r') as legal_stopwords_file:
            legal_stopwords.extend(legal_stopwords_file.read().split())

    stop_words.extend(legal_stopwords)
    return stop_words


# method that turns a text into a list of stemmed words (tokens).
def text_to_tokens(curr_str, lang='ro'):
    stemmer = romanian_stemmer
    if lang == 'en':
        stemmer = english_stemmer
    stop_words = get_extended_stopwords(lang)
    # removal of punctuation and other characters from the text
    curr_str = replace_nonletters(curr_str)
    # replacement of diacritics with their corresponding regular symbols
    curr_str = replace_diacritics(curr_str)
    # turning the text to lowercase
    curr_str = curr_str.lower()

    # Returns an object of type Doc, which is a sequence of Token objects
    tokens = curr_str.split()
    # A list of valid tokens
    good_tokens = []
    for token in tokens:
        # Gets the stemmed token from the Token object
        stem = stemmer.stem(token)
        # Checks token validity
        if stem == "" or stem in stop_words:
            continue
        if not stem[0].isalpha():
            continue
        # Adds token to list
        good_tokens.append(stem)
    return good_tokens


romanian_model = None
english_model = None
try:
    romanian_model = gensim.models.Word2Vec.load(f'Legaltech/word2vec.model.ro')
    english_model = gensim.models.Word2Vec.load(f'Legaltech/word2vec.model.en')
except:
    try:
        romanian_model = gensim.models.Word2Vec.load(f'word2vec.model.ro')
        english_model = gensim.models.Word2Vec.load(f'word2vec.model.en')
    except:
        pass

def text_to_coords(curr_str, lang='ro'):
    model = romanian_model
    if lang == 'en':
        model = english_model
    # get the stemmed tokens from text
    tokens = text_to_tokens(curr_str, lang=lang)
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

    # No relevant references
    if len(sum) == 0:
        return [0.0001] * 100

    # divide to the number of words that exist in the model's vocabulary to get the average
    sum = sum / cnt
    return sum
