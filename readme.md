# Data Visual Lab 数据可视化实验室

2023年小学期实验平台

作者：王泽昊

## 方案

### 文旅问答平台

用户进入web页面，通过询问chatgpt/chatglm某些景点相关的内容，将结果反馈到网页上，并通过可视化的形式展现这些结果。

### 人格测试平台

用户进入web页面，调用chatgpt/chatglm api为用户事实生成一套定制化的人格测试问卷，并将调查的结果用可视化的网页形式展现。用户获取的问卷将被存放在数据库中，可以方便的导出为各种表单形式进行参考。

## TODO

### 基于gpt的Web可视化问答平台

* chatglm-6B 外挂知识库
  * API
* Web 可视化展示
  * Flask + Ajax + Mysql 后端框架
    * 打通 json 异步通信
  * ECharts + Bootstrap 前端框架
    * ECharts 案例
    * Bootstrap Studio 设计页面
