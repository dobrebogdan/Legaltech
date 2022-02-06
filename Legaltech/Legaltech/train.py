import gensim
import utils

filenames = ['legislatie/ro/codul_administrativ', 'legislatie/ro/codul_civil', 'legislatie/ro/codul_fiscal',
                 'legislatie/ro/codul_muncii', 'legislatie/ro/codul_penal']

train_tokens = []


def add_tokens_from_file(filename):
    with open(filename) as f:
        content = f.read()
        lines = content.split("$Articolul ")
        formated_lines = []
        [formated_lines.append(f"Articolul {line}") for line in lines[1:]]
        for line in formated_lines:
            print("$$$$")
            print(line)
            train_tokens.append(utils.text_to_tokens(line))


for filename in filenames:
    add_tokens_from_file(filename)

# Word2Vec is used to turn words into numerical vectors, which are then averaged to obtain a vector for a tweet
# Multiple tests were done and the parameters which behaved the best were selected
model = gensim.models.Word2Vec(min_count=5,
                     window=10,
                     sample=5e-5,
                     alpha=0.1,
                     min_alpha=0.01,
                     workers=4)

# Building the model's vocabulary and training the model
model.build_vocab(train_tokens, progress_per=10000)
model.train(train_tokens, total_examples=model.corpus_count, epochs=100)

# Keeping only the current vectors to save memory
model.save("word2vec.model")
