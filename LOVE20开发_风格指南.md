0. 协议名：（全大写）
1. 合约名：（大写）协议名+ （帕斯卡）动词
2. 函数名：
   - 读函数：（驼峰）名词或状态
     - 返回列表：
       - 返回数据+By 条件，默认条件 tokenAddress 和 round 不需加 by
       - 如果是分页则加 ByPage 放到最后（表示 3 个参数：start，end，reverse）
       - 如果不需要 round 参数，则返回数据上体现
       - 举例：获取行动列表
         - 取全部：ActionsAll
         - 取某轮：Actions
         - 取当轮：ActionsCurrentRound
         - 取指定：ActionsByIds
   - 写函数：（驼峰）动词
3. 变量名：（驼峰）
   - 私有和内部变量：下划线开头
   - 入参如果有重名：下划线结尾
4. 常量：全大写，单词间下划线

合约函数顺序

1. external、public、internal、private
2. write 函数、read 函数
