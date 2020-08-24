## 基于知识库问答的电影聊天机器人。

**如果本项目对你学习构建一个聊天机器人有帮助, 欢迎 Start...**

#### 环境搭建

neo4j环境搭建参考: [知识图谱篇](https://github.com/Mrzhang3389/chatbot/tree/master/KnowledgeGraph)

其它环境:

```bash
pip install -r requirements.txt
```

#### 效果图:

```bash
python chatbot.py
```

![example](assets/example.png)

![example2](assets/example2.png)

![example3](assets/example3.png)

#### 如何构建

1. 先构建知识库参考[知识图谱](https://github.com/Mrzhang3389/chatbot/tree/master/KnowledgeGraph)

2. 再构建问题处理模块参考[机器学习](https://github.com/Mrzhang3389/chatbot/tree/master/MachineLearning)
3. 然后 问题处理模块 + 答案搜索模块 = 基于知识库的问答机器人
4. 最后优化模型中的细节和捕获异常
