from py2neo import *


class Get_answer():
    def __init__(self):
        self.graph = Graph("http://localhost:7474", username="neo4j", password="your password")

    def get_data(self, index, params):
        query = ''
        if index == 0:
            query = "match(m:Movie) where m.title='{}' return  m.rating;".format(params[0])  # 评分
        elif index == 1:
            query = "match(m:Movie) where m.title='{}' return  m.releasedate;".format(params[0])  # 上映时间
        elif index == 2:
            query = "match(m:Movie)-[r:is]->(g:Genre) where m.title='{}' return g.name;".format(params[0])  # 类型
        elif index == 3:
            query = "match(m:Movie) where m.title='{}' return  m.introduction;".format(params[0])  # 简介
        elif index == 4:
            query = "MATCH (p:Person)-[r:actedin]->(m:Movie) where m.title='{}' RETURN p.name;".format(
                params[0])  # 演员列表
        elif index == 5:
            query = "match(p:Person) where p.name='{}'  return p.biography;".format(params[0])  # 演员介绍
        elif index == 6:
            query = "match(n:Person)-[:actedin]-(m:Movie) where n.name ='{}' " \
                    "match(g:Genre)-[:is]-(m) where g.name='{}' return distinct  m.title".format(params[0], params[
                1])  # 某演员演过什么类型电影有哪些
        elif index == 7:
            query = "match(n:Person)-[:actedin]->(m:Movie) where n.name='{}' return m.title".format(
                params[0])  # 某演员演过什么电影
        elif index == 8:
            query = "match(n:Person)-[:actedin]-(m:Movie) where n.name ='{}' and m.rating> {} return m.title".format(
                params[0], params[1])  # 参演评分 大于 x
        elif index == 9:
            query = "match(n:Person)-[:actedin]-(m:Movie) where n.name ='{}' and m.rating < {} return m.title;".format(
                params[0], params[1])  # 参演评分 小于 x
        elif index == 10:
            query = "match(n:Person)-[:actedin]-(m:Movie) where n.name ='{}' " \
                    "match(p:Genre)-[:is]-(m) return distinct  p.name".format(params[0])  # 演员演过哪些类型电影
        elif index == 11:
            query = "match(p1:Person)-[:actedin]->(m:Movie) match(p2:Person)-[:actedin]->(m)" \
                    "where p1.name='{}' and p2.name='{}' return m.title;".format(params[0], params[1])  # 演员a和演员b合作过的电影
        elif index == 12:
            query = "match(n)-[:actedin]-(m) where n.name ='{}' return count(*);".format(params[0])  # 演员演过电影数量
        elif index == 13:
            query = "match(n:Person) where n.name='{}' return n.birth;".format(params[0])  # 演员出生日期

        result = self.graph.run(query)
        return result


if __name__ == "__main__":
    ga = Get_answer()
    answers = ga.get_data(1, ['卧虎藏龙'])
    for answer in answers:
        print(answer[0])
