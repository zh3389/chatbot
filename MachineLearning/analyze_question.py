import joblib
import numpy as np
from pyhanlp import *


class AnalysisQuestion():
    def abstract_question(self, question):
        """
        使用hanlp进行分词，将关键词进行词性抽象
        :param question:
        :RETURN:
        """
        self.abstractMap = {}
        print("=" * 30 + "HanLP分词" + "=" * 30)
        # 中文分词
        segment = HanLP.newSegment().enableCustomDictionary(True)
        list_word = segment.seg(question)
        print(list_word)
        print("-" * 70)
        abstractQuery = ''
        nr_count = 0
        for item in list_word:
            word = item.word
            pos = str(item)
            if 'nm' in pos:  # 电影名
                abstractQuery += "nm "
                self.abstractMap['nm'] = word
            elif 'nr' in pos and nr_count == 0:
                abstractQuery += 'nnt '
                self.abstractMap['nnt'] = word
                nr_count += 1
            elif 'nr' in pos and nr_count == 1:  # nr再一次出现，改成nnr
                abstractQuery += "nnr "
                self.abstractMap['nnr'] = word
                nr_count += 1
            elif 'x' in pos:
                abstractQuery += "x "
                self.abstractMap['x'] = word
            else:
                abstractQuery += word + " "
        return abstractQuery

    def query_classify(self, sentence):
        """
        获取模板索引
        :param sentence:
        :RETURN:
        """
        vocab = {}
        with open('vocab/vocabulary.txt', 'r', encoding='UTF-8')as fread:
            for line in fread:
                arr = line.rstrip().split(':')
                vocab[arr[1]] = arr[0]
        tmp = np.zeros(len(vocab))
        list_sentence = sentence.split(' ')
        for word in list_sentence:
            if word in vocab:
                tmp[int(vocab[word])] = 1
        clf = joblib.load('model/clf.model')
        index = clf.predict(np.expand_dims(tmp, 0))[0]
        dict_template = {}
        with open('vocab/question_classification.txt', 'r', encoding='utf-8')as fread:
            for line in fread:
                arr_tmp = line.rstrip().split(':')
                dict_template[arr_tmp[0]] = arr_tmp[1]
        return int(index), dict_template[index]

    def query_extention(self, temp):
        """
        模板中的实体值
        :param sentence:
        :RETURN:
        """
        params = []
        for abs_key in self.abstractMap:
            if abs_key in temp:
                params.append(self.abstractMap[abs_key])
        return params

    def analysis(self, question):
        # 打印原始句子
        print('原始句子：{}'.format(question))
        # 关键词进行词性抽象
        abstr = self.abstract_question(question)
        print('句子抽象化结果：{}'.format(abstr))
        # 句子抽象获取对应模板
        index, strpatt = self.query_classify(abstr)
        print('句子对应的索引{}\t模板：{}'.format(index, strpatt))
        # 模板还原成句子
        finalpatt = self.query_extention(strpatt)
        return index, finalpatt


if __name__ == "__main__":
    aq = AnalysisQuestion()
    question = input('请输入你想查询的信息：')  # 英雄这部电影讲的什么？
    index, params = aq.analysis(question)
    print(index, params)