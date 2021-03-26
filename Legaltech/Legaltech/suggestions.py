import math

import gensim

import Legaltech.article as article
import Legaltech.utils as utils

articles = []

def dist_between_coords(coords1, coords2):
    dist = 0.0
    for i in range(0, len(coords1)):
        dist += (coords1[i] - coords2[i]) * (coords1[i] - coords2[i])
    dist = math.sqrt(dist)
    return dist


def get_top_suggestions_from_text(current_text, limit=10):
    distances = []
    [distances.append((dist_between_coords(utils.text_to_coords(current_text), article.coords), article)) for article in articles]
    sorted_distances = sorted(distances)
    sorted_articles = []
    for distance in sorted_distances:
        sorted_articles.append(distance[1])
    if limit:
        sorted_articles = sorted_articles[0: limit]
    return sorted_articles


def get_top_suggestions_from_article(current_article, limit=10):
    distances = []
    [distances.append((dist_between_coords(current_article.coords, article.coords), article.id, article)) for article in articles]
    sorted_distances = sorted(distances)
    sorted_articles = []
    for distance in sorted_distances:
        if distance[1] != current_article.id:
            sorted_articles.append(distance[2])
    if limit:
        sorted_articles = sorted_articles[0: limit]
    return sorted_articles


# Word2Vec is used to turn words into numerical vectors, which are then averaged to obtain a vector for a tweet
# Multiple tests were done and the parameters which behaved the best were selected
model = gensim.models.Word2Vec.load('word2vec.model')

print("Model loaded")

def add_articles_from_file(filename, filecode):
    with open(filename) as f:
        content = f.read()
        lines = content.split("    Articolul ")
        formated_lines = []
        [formated_lines.append(f"Articolul {line}") for line in lines]
        id = 0
        for line in formated_lines:
            articles.append(article.Article(line, utils.text_to_coords(model, line), f"{filecode}_{id}"))
            id += 1


for (filename, filecode) in [('legislatie/md/codul_penal', 'md_cp')]:# ('legislatie/md/codul_civil', 'md_cc')]:
    add_articles_from_file(filename, filecode)


searched_article = articles[108]
suggestions = get_top_suggestions_from_article(searched_article)
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print(searched_article.text)
for suggestion in suggestions:
    print("------------------------------------")
    print(suggestion.text)
