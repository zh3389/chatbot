from sklearn.naive_bayes import GaussianNB
import argparse
import os
import re
import jieba
import numpy as np
import joblib


def load_data(train_path):
    list_files = os.listdir(train_path)
    X = []
    Y = []
    vocab = {}
    with open('vocabulary.txt', 'r', encoding='UTF-8')as fread:
        for line in fread:
            arr = line.rstrip().split(':')
            vocab[arr[1]] = arr[0]
    print(vocab)
    for filename in list_files:
        path_file = os.path.join(train_path, filename)
        result = re.match('【[0-9]*】', filename).span()
        start = result[0]
        end = result[1]
        with open(path_file, 'r', encoding='utf-8')as fread:
            for line in fread:
                tmp = np.zeros(len(vocab))
                Y.append(filename[start + 1:end - 1])  # label
                list_sentence = jieba.lcut(line.rstrip())
                for word in list_sentence:
                    if word in vocab:
                        tmp[int(vocab[word])] = 1
                X.append(tmp)
    return X, Y


def train(train_path):
    X, Y = load_data(train_path)
    clf = GaussianNB().fit(X, Y)
    joblib.dump(clf, 'clf.model')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dir', default='')
    args = parser.parse_args()
    try:
        train(args.dir)
    except Exception as ex:
        print(ex)
