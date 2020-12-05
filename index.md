# 电影知识库问答机器人

## 最终效果

![效果图](https://raw.githubusercontent.com/Mrzhang3389/chatbot/master/assets/example.png)

## 知识图谱篇

#### 准备工作

- 电影知识库的数据参考: [movie data](https://github.com/Mrzhang3389/chatbot/tree/master/KnowledgeGraph/movie_data)
- Neo4j图数据库
  - Neo4j官网: [Neo4j home](https://neo4j.com/)
  - Neo4j桌面版: [Neo4j Desktop](https://neo4j.com/download-center/#desktop)
  - Neo4j服务器版: [Neo4j Server](https://neo4j.com/download-center/#community)
  - Neo4j Docker版:  `docker pull neo4j`
- 简单的Neo4j语法知识: [Neo4j Cypher](https://neo4j.com/docs/cypher-refcard/current/)

#### 操作步骤

1. 运行你的Neo4j图数据库
2. 导入电影知识库数据: [数据导入](https://github.com/Mrzhang3389/chatbot/tree/master/KnowledgeGraph#%E4%BA%8C-%E5%AF%BC%E5%85%A5%E6%95%B0%E6%8D%AE)
3. 测试数据是否导入正常: [测试知识图谱](https://github.com/Mrzhang3389/chatbot/tree/master/KnowledgeGraph#%E4%B8%89-%E4%BD%BF%E7%94%A8%E6%95%B0%E6%8D%AE)
4. 答案查找的Python代码参考: [答案搜索](https://github.com/Mrzhang3389/chatbot/blob/master/KnowledgeGraph/get_answer.py)

#### 知识图谱所达到的效果

![知识图谱效果图](知识图谱效果图.png)

## 机器学习篇

#### 准备工作

- 高斯朴素贝叶斯原理根据自身情况学习: [参考维基百科](https://zh.wikipedia.org/wiki/%E6%9C%B4%E7%B4%A0%E8%B4%9D%E5%8F%B6%E6%96%AF%E5%88%86%E7%B1%BB%E5%99%A8#%E9%AB%98%E6%96%AF%E5%96%AE%E7%B4%94%E8%B2%9D%E6%B0%8F)
- Python下scikit-learn包里面的naive_bayes的使用
- 准备模型的训练数据: [数据参考](https://github.com/Mrzhang3389/chatbot/tree/master/MachineLearning/train_model/data)
- 训练问题分析模型代码参考: 训练问题分析模型
- 使用问题分析模型代码参考: [使用问题分析模型](https://github.com/Mrzhang3389/chatbot/blob/master/MachineLearning/analyze_question.py)

#### 操作步骤

1. 对允许用户提问的问题进行分类
2. 创造用户提问的问题模板
3. 训练问题分类模型
4. 使用问题分类模型得到用户的意图

#### 机器学习所达到的效果



## 机器学习训练模型以及优化篇

#### 准备工作



#### 操作步骤



#### ......