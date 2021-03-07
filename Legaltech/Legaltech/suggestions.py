import gensim
import math
import article
import utils


def dist_between_coords(coords1, coords2):
    dist = 0.0
    for i in range(0, len(coords1)):
        dist += (coords1[i] - coords2[i]) * (coords1[i] - coords2[i])
    dist = math.sqrt(dist)
    return dist


def get_top_suggestions_from_text(current_text, articles, limit=10):
    distances = []
    [distances.append((dist_between_coords(utils.text_to_coords(current_text), article.coords), article)) for article in articles]
    sorted_distances = sorted(distances)
    sorted_articles = []
    for distance in sorted_distances:
        sorted_articles.append(distance[1])
    if limit:
        sorted_articles = sorted_articles[0: limit]
    return sorted_articles


def get_top_suggestions_from_article(current_article, articles, limit=10):
    distances = []
    [distances.append((dist_between_coords(current_article.coords, article.coords), article)) for article in articles]
    sorted_distances = sorted(distances)
    sorted_articles = []
    for distance in sorted_distances:
        if distance[1].id != current_article.id:
            sorted_articles.append(distance[1])
    if limit:
        sorted_articles = sorted_articles[0: limit]
    return sorted_articles


train_tokens = []
with open('legislatie/codul_civil') as f:
    content = f.read()
    lines = content.split("\nArticolul ")
    formated_lines = []
    [formated_lines.append(f"Articolul {line}") for line in lines]
    x = 0
    for line in formated_lines:
        #print(x)
        #print(line)
        x += 1
        train_tokens.append(utils.text_to_tokens(line))


#print(train_tokens)


# Word2Vec is used to turn words into numerical vectors, which are then averaged to obtain a vector for a tweet
# Multiple tests were done and the parameters which behaved the best were selected
model = gensim.models.Word2Vec.load('word2vec.model')

print("Model loaded")
articles = []
id = 0
for line in formated_lines:
    articles.append(article.Article(line, utils.text_to_coords(model, line), id))
    id += 1

searched_article = articles[998]
suggestions = get_top_suggestions_from_article(searched_article, articles)
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print(searched_article.text)
for suggestion in suggestions:
    print("------------------------------------")
    print(suggestion.text)
