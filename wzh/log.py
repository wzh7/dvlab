from datetime import datetime

def log_cli(source:str, content:str, type:str="info"):
    '''命令行日志记录'''
    if type == "info":
        print("\033[94m[INFO]\033[95m", source, "\033[0m:", content)
    elif type == "error":
        print("\033[91m[ERROR]\033[95m", source, "\033[0m:\033[91m", content, "\033[0m")
    elif type == "warning":
        print("\033[93m[WARNING]\033[95m", source, "\033[0m:\033[93m", content, "\033[0m")

def log_file(source:str, content:str, type:str="info"):
    '''文件日志记录'''
    pass
    # now = datetime.now()
    # path = str(now.year) + "." + str(now.month) + "." + str(now.day) + "." + "csv"
    # with open(path, 'w', encoding="utf-8") as file:
    #     content = "1,2,3,1,4,2"
    #     file.write(content)

def log_db(source:str, content:str, type:str="info"):
    '''数据库日志记录'''
    pass

def info(source:str, content:str, type:str="info"):
    '''日志记录'''
    log_cli(source, content, type)
    log_file(source, content, type)
    log_db(source, content, type)

def warning(source:str, content:str):
    '''日志记录'''
    info(source, content, "warning")

def error(source:str, content:str):
    '''日志记录'''
    info(source, content, "error")
