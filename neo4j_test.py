from py2neo import Graph, Node, Relationship
from flask import Flask, render_template, request, jsonify
import openai


#########################################################################################
#######################              NEO4J               ################################
#########################################################################################

# 连接到Neo4j数据库
graph = Graph("bolt://localhost:7687", auth=("neo4j", "1234567890"))

# 创建Flask应用
app = Flask(__name__)

# 查询不多于20条Project实体及其相关实体和关系
query = """
MATCH (p:Project)-[:BELONGS_TO]->(c:Category),
      (p)-[:PROTECTED_BY]->(pu:ProtectionUnit),
      (p)-[:DECLARED_IN]->(ru:RegionOrUnit)
RETURN p, c, pu, ru LIMIT 40
"""

result = graph.run(query)

# 创建一个空的知识图谱
knowledge_graph = {"nodes": [], "links": []}

for record in result:
    project = record["p"]
    category = record["c"]
    protection_unit = record["pu"]
    region_or_unit = record["ru"]
    
    # 添加节点
    knowledge_graph["nodes"].append({"id": project["名称"], "label": "Project"})
    knowledge_graph["nodes"].append({"id": category["类别名称"], "label": "Category"})
    knowledge_graph["nodes"].append({"id": protection_unit["单位名称"], "label": "ProtectionUnit"})
    knowledge_graph["nodes"].append({"id": region_or_unit["地区或单位名称"], "label": "RegionOrUnit"})
    
    # 添加关系
    knowledge_graph["links"].append({"source": project["名称"], "target": category["类别名称"], "label": "BELONGS_TO"})
    knowledge_graph["links"].append({"source": project["名称"], "target": protection_unit["单位名称"], "label": "PROTECTED_BY"})
    knowledge_graph["links"].append({"source": project["名称"], "target": region_or_unit["地区或单位名称"], "label": "DECLARED_IN"})

# 创建Flask路由
@app.route('/')
def index():
    return render_template('index.html', knowledge_graph=knowledge_graph)


#########################################################################################
#######################              GPT               ##################################
#########################################################################################

# ChatGPT API密钥
openai.api_key = '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'  # 替换为你的API密钥


# 聊天消息的POST路由
@app.route('/chatgpt-api', methods=['POST'])
def chatgpt_api():
    message = request.json.get('message')

    # 调用OpenAI的chat.completion方法来与ChatGPT进行对话
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a user."},
            {"role": "user", "content": message}
        ]
    )

    # data = response.json()
    # 提取ChatGPT的回复
    chatgpt_response = response['choices'][0]['message']['content']
    

    return jsonify({'message': chatgpt_response})

if __name__ == '__main__':
    app.run(debug=True)
