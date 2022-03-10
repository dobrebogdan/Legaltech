import csv
from build_stopwords import build_stopwords
from googletrans import Translator

translator = Translator()


def translate_ro_to_en(romanian_text):
    english_text = translator.translate(romanian_text)
    return english_text.text


def build_en_resources():
    with open('legislatie/legislatie_completa_ro.tsv', "r") as input_tsv_file:
        with open('legislatie/legislatie_completa_en.tsv', "w") as output_tsv_file:
            tsv_reader = csv.reader(input_tsv_file, delimiter='\t')
            tsv_writer = csv.writer(output_tsv_file, delimiter='\t')
            for line in tsv_reader:
                line[2] = translate_ro_to_en(line[2])
                tsv_writer.writerow(line)
    build_stopwords(lang='en')


build_en_resources()
