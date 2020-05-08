# 获取51job上的职位，公司名，工作地点，薪资，发布时间
from Day05 import crawl_tool as tool
from lxml import etree   # 元素树
url = 'https://search.51job.com/list/010000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
# 通过爬虫工具根据url获取网页源码
html_str1 = tool.get_html(url,'gbk')

# 将字符串转换成html文档结构
html_=etree.HTML(html_str1)

# 3.将html文档结构转换成元素树结构
html=etree.ElementTree(html_)

# 4.使用xpath语法进行数据清洗
div_el = html.xpath('//div[@id="resultList"]/div[@class="el"]')  # 获取id=“resultlist‘ 内所有的class=’el‘的div,div的列表
rows = list()
# 通过for循环寻找每一行el数据
for index, el in enumerate(div_el):             # el数据类型是html文档类型
    el = etree.ElementTree(el)                   # 同上：需要将html文档结构再转换成元素树的格式（节点）
    title = el.xpath('/div/p/span/a/@title')  # 职位名
    title = title[0] if title else None

    link_url = el.xpath('/div/p/span/a/@href')  # 进入详情页的地址
    link_url = link_url[0] if link_url else None

    company = el.xpath('/div/span[@class="t2"]/a/@title')  # 公司
    company = company[0] if company else None

    city = el.xpath('/div/span[@class="t3"]/text()')       # 工作地点
    city = city[0] if city else None

    salary = el.xpath('/div/span[@class="t4"]/text()')      # 薪水
    salary = salary[0] if salary else None

    time = el.xpath('/div/span[@class="t5"]/text()')       # 发布时间
    time = time[0] if time else None
    row = (title, company, city, salary, time)  # 将每一行数据封装到元祖中
    # print(row)
    rows.append(row)

print(rows)

