import csv
import spacy
from stop_words import get_stop_words
from nltk.stem.snowball import RomanianStemmer, EnglishStemmer
from utils import replace_diacritics, replace_nonletters

def build_stopwords(lang='ro'):
    stop_words = get_stop_words(lang)
    pipeline = 'ro_core_news_md'
    if lang == 'en':
        pipeline='en_core_web_md'
    nlp = spacy.load(pipeline)
    stemmer = RomanianStemmer()
    if lang == 'en':
        stemmer = EnglishStemmer()
    stopwords_cnt = {}
    with open(f'legislatie/legislatie_completa_{lang}.tsv') as tsvfile:
        tsv_reader = csv.reader(tsvfile, delimiter='\t')
        for line in tsv_reader:
            clean_text = replace_diacritics(replace_nonletters(line[2]))
            doc = nlp(replace_diacritics(clean_text))
            current_words = set()
            for token in doc:
                if token.text[0].isalpha() and (not token.text in stop_words):
                    stemmed_word = stemmer.stem(token.text)
                    current_words.add(stemmed_word)
            for word in current_words:
                if word in stopwords_cnt.keys():
                    stopwords_cnt[word] = stopwords_cnt[word] + 1
                else:
                    stopwords_cnt[word] = 1
    sorted_stopwords = [(cnt, word) for (word, cnt) in stopwords_cnt.items()]
    with open(f'legal_stopwords_{lang}', 'w') as file:
        for (cnt, word) in sorted_stopwords:
            if cnt >= 500:
                file.write(f"{word} ")
