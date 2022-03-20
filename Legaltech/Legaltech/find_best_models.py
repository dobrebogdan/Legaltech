import csv
import numpy as np
from utils import text_to_coords
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score
import xgboost as xgb
import tensorflow as tf

train_data = []
train_labels = []

lang='ro'

name_to_number = {
    'ro_cp': 0,
    'ro_cc': 1
}

number_to_name = {
    0: 'ro_cp',
    1: 'ro_cc'
}

with open(f'legislatie/legislatie_completa_{lang}.tsv') as tsvfile:
    tsv_reader = csv.reader(tsvfile, delimiter='\t')
    for line in tsv_reader:
        coords = text_to_coords(line[2], lang=lang)
        train_data.append(coords)
        train_labels.append(name_to_number[line[1]])

train_data = np.array(train_data)
train_labels = np.array(train_labels)

X_train, X_test, y_train, y_test = train_test_split(train_data, train_labels, test_size=0.2, random_state=5)


def print_res(y_test, y_pred, model_name=""):
    print(f"""
Model: {model_name}
Accuracy score: {accuracy_score(y_pred, y_test)}
Precision score: {precision_score(y_pred, y_test)}
Recall score: {recall_score(y_pred, y_test)}
F1 score: {f1_score(y_pred, y_test)}

""")


def grid_search_svm():
    for C in [0.1, 1, 10]:
        for gamma in [0.01, 0.1, 1]:
            clf = make_pipeline(StandardScaler(), SVC(C=C, gamma=gamma))
            clf.fit(X_train, y_train)
            y_pred = clf.predict(X_test)
            print_res(y_pred, y_test, model_name='SVM')


def svm_classifier():
    clf = make_pipeline(StandardScaler(), SVC(gamma='auto'))
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print_res(y_pred, y_test, model_name='SVM')


def random_forest_classifier():
    model = RandomForestClassifier(max_depth=3, random_state=3)
    model.fit(X_train, y_train)
    RandomForestClassifier()
    y_pred = model.predict(X_test)
    print_res(y_pred, y_test, model_name='Random forest')


def xgboost_classifier():
    model = xgb.XGBClassifier()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print_res(y_pred, y_test, model_name='XGBoost')


def rnn_classifier():
    model = tf.keras.Sequential([
        tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64)),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(1)
    ])
    model.compile(loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
                  optimizer=tf.keras.optimizers.Adam(1e-4),
                  metrics=['accuracy'])
    model.fit(np.expand_dims(X_train, axis=2), y_train, epochs=20)
    y_pred_raw = model.predict(np.expand_dims(X_test, axis=2))
    y_pred = []
    for sample in y_pred_raw:
        if sample[0] < 0:
            y_pred.append(0.0)
        else:
            y_pred.append(1.0)
    y_pred = np.array(y_pred)
    print_res(y_test, y_pred)



# svm_classifier()
# random_forest_classifier()
# xgboost_classifier()
# rnn_classifier()
grid_search_svm()

