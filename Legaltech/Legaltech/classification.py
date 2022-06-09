import numpy as np
import csv
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from Legaltech.utils import text_to_coords, text_to_tokens
from Legaltech.suggestions import get_top_suggestions_from_text

nickname_to_number = {
    'ro_cp': 0,
    'ro_cc': 1
}

number_to_name = {
    0: 'Domeniul penal',
    1: 'Domeniul civil'
}

ro_model = None
en_model = None
ro_train_data = None
ro_train_labels = None

for lang in ['ro', 'en']:
    train_data = []
    train_labels = []
    with open(f'Legaltech/legislatie/legislatie_completa_{lang}.tsv') as tsvfile:
        tsv_reader = csv.reader(tsvfile, delimiter='\t')
        for line in tsv_reader:
            coords = text_to_coords(line[2], lang=lang)
            train_data.append(coords)
            train_labels.append(nickname_to_number[line[1]])
    clf = make_pipeline(StandardScaler(), SVC(gamma='auto'))
    clf.fit(train_data, train_labels)
    if lang == 'ro':
        ro_model = clf
        ro_train_data = train_data
        ro_train_labels = train_labels
    else:
        en_model = clf
        en_train_data = train_data
        en_train_labels = train_labels


def get_model_classification(text, lang='ro'):
    model = ro_model
    if lang == 'en':
        model = en_model

    y_pred = model.predict(np.array([text_to_coords(text, lang=lang)]))
    return number_to_name[y_pred[0]]


def get_spatial_classification(text, lang='ro'):
  laws = get_top_suggestions_from_text(text, lang=lang)
  return number_to_name[nickname_to_number[laws[0].type]]


def get_text_classification(text, lang='ro'):
    if len(text_to_tokens(text, lang=lang)) <= 3:
        return get_spatial_classification(text, lang=lang)
    else:
        return get_model_classification(text, lang=lang)
