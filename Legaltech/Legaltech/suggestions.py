import csv
import Legaltech.article as article
import Legaltech.utils as utils
from scipy import spatial


articles = []


def dist_between_coords(coords1, coords2):
    return spatial.distance.cosine(coords1, coords2)
"""
    dist = 0.0
    for i in range(0, len(coords1)):
        dist += (coords1[i] - coords2[i]) * (coords1[i] - coords2[i])
    dist = math.sqrt(dist)
    return dist
"""


def get_top_suggestions_from_text(current_text, lang='ro', limit=20):
    distances = []
    [distances.append((dist_between_coords(utils.text_to_coords(current_text, lang=lang), article.coords), article)) for article in articles]
    sorted_distances = sorted(distances)
    sorted_articles = []
    for distance in sorted_distances:
        sorted_articles.append(distance[1])
    if limit:
        sorted_articles = sorted_articles[0: limit]
    return sorted_articles


def add_articles_from_file(filename, lang='ro'):
    with open(filename) as tsvfile:
        tsv_reader = csv.reader(tsvfile, delimiter='\t')
        for line in tsv_reader:
            articles.append(article.Article(line[2], utils.text_to_coords(line[2], lang=lang), f"{line[0]}", line[1]))


def load_articles_for_language(lang='ro'):
    articles.clear()
    add_articles_from_file(f'Legaltech/legislatie/legislatie_completa_{lang}.tsv', lang=lang)
