import csv
from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer
from build_stopwords import build_stopwords


model = M2M100ForConditionalGeneration.from_pretrained('facebook/m2m100_418M')
tokenizer = M2M100Tokenizer.from_pretrained('facebook/m2m100_418M')

tokenizer.src_lang = "ro"

def translate_ro_to_en(romanian_text):
    encoded_romanian_text = tokenizer(romanian_text, return_tensors="pt")
    generated_english_tokens = model.generate(**encoded_romanian_text, forced_bos_token_id=tokenizer.get_lang_id("en"))
    romanian_text = tokenizer.batch_decode(generated_english_tokens, skip_special_tokens=True)
    return romanian_text


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
