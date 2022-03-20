import numpy as np
import csv
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from Legaltech.utils import text_to_coords

name_to_number = {
    'ro_cp': 0,
    'ro_cc': 1
}

number_to_name = {
    0: 'Domeniul penal',
    1: 'Domeniul civil'
}

ro_model = None
en_model = None

for lang in ['ro', 'en']:
    train_data = []
    train_labels = []
    with open(f'Legaltech/legislatie/legislatie_completa_{lang}.tsv') as tsvfile:
        tsv_reader = csv.reader(tsvfile, delimiter='\t')
        for line in tsv_reader:
            coords = text_to_coords(line[2], lang=lang)
            train_data.append(coords)
            train_labels.append(name_to_number[line[1]])
    clf = make_pipeline(StandardScaler(), SVC(gamma='auto'))
    clf.fit(train_data, train_labels)
    if lang == 'ro':
        ro_model = clf
    else:
        en_model = clf


def get_text_classification(text, lang='ro'):
    model = ro_model
    if lang == 'en':
        model = en_model
    print(text_to_coords(text, lang=lang))
    y_pred = model.predict(np.array([text_to_coords(text, lang=lang)]))
    return number_to_name[y_pred[0]]
