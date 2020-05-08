# python3.6 提供了 urllib这个库（请求库）可以获取到请求对象request

from urllib import request # 导入模块

# 1.User-Agent放入字典header中（用来模拟浏览器访问服务器资源，不会被封ip地址）

ua_value="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"

ua="User-Agent"
header={ua:ua_value}

# 2.获取请求的路径（要去爬哪个网页）
# url="https://www.baidu.com"
url='https://search.51job.com/list/010000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
# 3.通过request模块可以构建一个属于自己的请求对象
req = request.Request(url,headers=header)

# 4.发送请求并接受到服务器的响应对象
response = request.urlopen(req)

# 5. 从响应对象读取网页中的源码（读取时需要指定解码方式）
html_str = response.read().decode('gbk')

print(html_str)






