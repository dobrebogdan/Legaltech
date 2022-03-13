import gensim
import utils
import csv


for lang in ['ro', 'en']:
    train_tokens = []

    def add_tokens_from_file(filename):
        with open(filename) as tsvfile:
            tsv_reader = csv.reader(tsvfile, delimiter='\t')
            for line in tsv_reader:
                train_tokens.append(utils.text_to_tokens(line[2]))


    add_tokens_from_file(f'legislatie/legislatie_completa_{lang}.tsv')

    # Word2Vec is used to turn words into numerical vectors, which are then averaged to obtain a vector for a tweet
    # Multiple tests were done and the parameters which behaved the best were selected
    model = gensim.models.Word2Vec(min_count=2,
                                   window=6,
                                   sample=5e-5,
                                   alpha=0.1,
                                   min_alpha=0.01,
                                   workers=4)

    # Building the model's vocabulary and training the model
    model.build_vocab(train_tokens, progress_per=100)
    model.train(train_tokens, total_examples=model.corpus_count, epochs=100)

    # Keeping only the current vectors to save memory
    model.save(f'word2vec.model.{lang}')
