import csv
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


def add_articles_from_file(filename):
    with open(filename) as tsvfile:
        tsv_reader = csv.reader(tsvfile, delimiter='\t')
        for line in tsv_reader:
            articles.append(article.Article(line[2], utils.text_to_coords(line[2]), f"{line[1]}_{line[0]}"))


add_articles_from_file('Legaltech/legislatie/legislatie_completa.tsv')
