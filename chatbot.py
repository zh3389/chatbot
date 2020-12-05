from MachineLearning.analyze_question import AnalysisQuestion
from KnowledgeGraph.get_answer import Get_answer

if __name__ == "__main__":
    aq = AnalysisQuestion()
    ga = Get_answer()
    while True:
        question = input('请输入你想查询的信息：')  # 成龙和李连杰合作过的电影有哪些？
        index, params = aq.analysis(question)
        answers = ga.get_data(index, params)
        print('答案:')
        for ans in answers:
            print(ans[0])
