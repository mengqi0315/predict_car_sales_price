from urllib import request,error   # 导入模块
import random  # 导入随机数模块

# 通过url和编码方式来获取网页源代码


def get_html(url,encoding='utf-8'):
    try:

        # 1.User-Agent放入字典header中（用来模拟浏览器访问服务器资源，不会被封ip地址）
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
        ua = [ua_value1,ua_value2,ua_value3,ua_value4,ua_value5]
        req=request.Request(url)
        req.add_header("User-Agent",random.choice(ua))



        # 2.通过request模块可以构建一个属于自己的请求对象

        # 3.发送请求并接受到服务器的响应对象
        response = request.urlopen(req)
        # 4. 从响应对象读取网页中的源码（读取时需要指定解码方式）
        html = response.read().decode(encoding)
    except error.URLError:
        print('url 错误')
    except error.HTTPError:
        print('请求异常')
    except Exception:
        print('获取网页内容失败')

    return html




