from urllib import request
import random
# 1.需要爬取的网页地址
url = 'https://search.51job.com/list/010000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
# 2.模拟多个浏览器登陆
ua_value1 = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) " \
                    "Gecko/20100101 Firefox/61.0"
ua_value2 = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 ' \
                    '(KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'
ua_value3 = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 ' \
                    '(KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
ua_value4 = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US)' \
                    ' AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16'
ua_value5 = 'Mozilla/5.0 (Windows NT 6.1; WOW64)' \
                    ' AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER'
        # 创建user-agent集合，模拟浏览器登陆
ua = (ua_value1,ua_value2,ua_value3,ua_value4,ua_value5)   # 元组里面的东西不能随便被修改
# 3.构建爬虫请求对象
req = request.Request(url)
# 4.在请求头中添加Uer-Agent
req.add_header("User-Agent",random.choice(ua))
# 5.发送请求并获取服务器的响应对象response
response = request.urlopen(req)
# 6.从响应对象中读取网页中的源码（响应正文）
html_str = response.read().decode('gbk')
print(html_str)


