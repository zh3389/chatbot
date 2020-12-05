from py2neo import *


class Get_answer():
    def __init__(self):
        self.graph = Graph("http://localhost:7474", username="neo4j", password="your password")

    def get_data(self, index, params):
        query = ''
        if index == 0:
            query = "MATCH (m:Movie) WHERE m.title='{}' RETURN  m.rating;".format(params[0])  # 评分
        elif index == 1:
            query = "MATCH (m:Movie) WHERE m.title='{}' RETURN  m.releasedate;".format(params[0])  # 上映时间
        elif index == 2:
            query = "MATCH (m:Movie)-[r:is]->(g:Genre) WHERE m.title='{}' RETURN g.name;".format(params[0])  # 类型
        elif index == 3:
            query = "MATCH (m:Movie) WHERE m.title='{}' RETURN  m.introduction;".format(params[0])  # 简介
        elif index == 4:
            query = "MATCH (p:Person)-[r:actedin]->(m:Movie) WHERE m.title='{}' RETURN p.name;".format(
                params[0])  # 演员列表
        elif index == 5:
            query = "MATCH (p:Person) WHERE p.name='{}'  RETURN p.biography;".format(params[0])  # 演员介绍
        elif index == 6:
            query = "MATCH(n:Person)-[:actedin]-(m:Movie) WHERE n.name ='{}' " \
                    "MATCH(g:Genre)-[:is]-(m) WHERE g.name='{}' RETURN distinct  m.title".format(params[0], params[
                1])  # 某演员演过什么类型电影有哪些
        elif index == 7:
            query = "MATCH(n:Person)-[:actedin]->(m:Movie) WHERE n.name='{}' RETURN m.title".format(
                params[0])  # 某演员演过什么电影
        elif index == 8:
            query = "MATCH(n:Person)-[:actedin]-(m:Movie) WHERE n.name ='{}' and m.rating> {} RETURN m.title".format(
                params[0], params[1])  # 参演评分 大于 x
        elif index == 9:
            query = "MATCH(n:Person)-[:actedin]-(m:Movie) WHERE n.name ='{}' and m.rating < {} RETURN m.title;".format(
                params[0], params[1])  # 参演评分 小于 x
        elif index == 10:
            query = "MATCH(n:Person)-[:actedin]-(m:Movie) WHERE n.name ='{}' " \
                    "MATCH(p:Genre)-[:is]-(m) RETURN distinct  p.name".format(params[0])  # 演员演过哪些类型电影
        elif index == 11:
            query = "MATCH(p1:Person)-[:actedin]->(m:Movie) MATCH(p2:Person)-[:actedin]->(m)" \
                    "WHERE p1.name='{}' and p2.name='{}' RETURN m.title;".format(params[0], params[1])  # 演员a和演员b合作过的电影
        elif index == 12:
            query = "MATCH(n)-[:actedin]-(m) WHERE n.name ='{}' RETURN count(*);".format(params[0])  # 演员演过电影数量
        elif index == 13:
            query = "MATCH(n:Person) WHERE n.name='{}' RETURN n.birth;".format(params[0])  # 演员出生日期

        result = self.graph.run(query)
        return result


if __name__ == "__main__":
    ga = Get_answer()
    answers = ga.get_data(1, ['卧虎藏龙'])
    for answer in answers:
        print(answer[0])
