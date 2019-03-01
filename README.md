# ManagementSystem
学校的论文管理系统


• 使用 Request,  BeautifulSoup 等第三库爬取 Web of Science 中的论文
• 将论文字段存储于 MongoDB 中
• 使用 Django 搭起后台, 实现用户登录注册, 多条件搜索等功能, 使用 fuzzywuzzy 展示匹配度降序的论文信息
• 如果用户发现爬取的信息有误, 可以提交修改建议, 管理员进行审核
• 该系统大大降低了人工校对论文的工作量, 系统还可以生成某用户论文的 PDF 文件
