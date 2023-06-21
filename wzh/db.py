import pymysql
import json

# 数据库连接信息
host = "124.223.18.236"
port = 32006
user = "root"
password = "t103860"
database = "dvlab"

def Cmd(has_return:bool, cmd:str):
    '''数据库操作函数，[input]  是否有返回:bool  SQL语句:str  [output]  数据:str'''
    try:
        # TODO 防止SQL注入
        print("\033[93m[数据库]\033[91m防SQL注入代码未完成，可能带来安全隐患！\033[0m")

        # 与数据库交互
        db = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database)
        cursor = db.cursor() # 创建一个游标对象
        cursor.execute(cmd) # 执行 SQL 语句
        if has_return:
            data = cursor.fetchall() # 获取所有数据
            print("\033[93m[数据库]\033[92m操作成功！\033[0m数据：",data)
            # print(f"{str(data)[:20]}...") # 仅显示前20字符
            return data # 返回数据
        else:
            db.commit() # 提交到数据库执行
            print("\033[93m[数据库]\033[92m操作成功！\033[0m")
        db.close() # 关闭数据库连接
    except Exception as e:
        print("\033[93m[数据库]\033[91m操作失败！错误：",e,"\033[0m")

def insert_mbti(qu:str, d:str, ans:tuple):
    '''插入MBTI测试数据，input：是否有返回，SQL语句；output：数据'''
    # 使用了enumerate()函数来同时迭代列表的索引和值
    ans_mod = json.dumps({'ans{}'.format(i+1): ans for i, ans in enumerate(ans)}, ensure_ascii=False)
    # 执行命令
    Cmd(False, "INSERT INTO mbti(qu, d, ans) VALUES ('" + qu + "', '" + d + "', '" + str(ans_mod) + "')")


# 测试
if __name__ == "__main__":
    Cmd(True, "SELECT * FROM mbti")