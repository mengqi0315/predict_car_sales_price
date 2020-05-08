# 爬取51job上的python工作相关信息
import MyUtil
from lxml import etree
import csv # 文件的格式csv（excel打开）

url = "https://search.51job.com/list/010000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
html_str = MyUtil.get_html(url,'gbk')

# 1.将页面源码字符串转换成html文档格式
htm = etree.HTML(html_str)

# 2. 将html文档类型再转换成html元素节点形式（只有html元素节点才能使用xpath语法进行解析）
html=etree.ElementTree(htm)

# 数据清洗（使用xpath语法进行解析）

# div[@class='red'] 查找class=red的div元素
# div[@id='d1']  查找id='d1'的div元素
# text()  获取元素标签内的文本
# @href 获取超链接中的href的值

items = html.xpath('//div[@id="resultList"]/div[@class="el"]')  # 获取id=“resultlist‘ 内所有的class=’el‘的div
rows = list()
for index,item in enumerate(items):             # item 数据类型是html文档类型

     child_item = etree.ElementTree(item)               # 将html文档类型再转换成html元素节点形式（只有节点树才能使用xpath解析）
     title = child_item.xpath('/div/p/span/a/@title')      #职位
     title = title[0] if title else None
     company = child_item.xpath('/div/span[@class="t2"]/a/@title')
     company = company[0] if company else None
     city = child_item.xpath('/div/span[@class="t3"]/text()')
     city = city[0] if city else None
     salary = child_item.xpath('/div/span[@class="t4"]/text()')
     salary = salary[0] if salary else None
     time = child_item.xpath('/div/span[@class="t5"]/text()')
     time = time[0] if time else None

     row = (title,company,city,salary,time)        # 将每一行数据封装到元祖中
     rows.append(row)


head = ["职位","公司","工作地点","薪资","发布时间"]

with open("51job1.csv","w",newline="",encoding='gbk') as job:  #  w表示只能写不能读，全部覆盖写
     file = csv.writer(job)
     file.writerow(head)  # 写一行数据

with open("51job1.csv", "a",newline="",encoding='gbk') as job:  # a用append方式写,newline默认参数为'\n'这里修改为空
     file = csv.writer(job)
     file.writerows(rows)    # 写多行数据

