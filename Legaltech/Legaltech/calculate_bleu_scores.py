import csv
from nltk.translate.bleu_score import sentence_bleu


def process(curr_str):
    curr_str = curr_str.lower()
    for i in range(0, len(curr_str)):
        if (not curr_str[i] == " ") and (not curr_str[i].isalpha()):
            curr_str = curr_str.replace(curr_str[i], " ")
    return curr_str


with open('legislatie/translated_articles.tsv') as tsvfile:
    tsv_reader = csv.reader(tsvfile, delimiter='\t')
    for line in tsv_reader:
        candidate = process(line[0])
        reference = process(line[1])
        score = sentence_bleu([reference], candidate)
        print(score)