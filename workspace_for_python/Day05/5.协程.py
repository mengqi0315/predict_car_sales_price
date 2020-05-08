# 协程是微型的线程（可以利用一切可以利用的时间来执行代码，在一定程度上提高代码的执行效率）
import gevent
from gevent import monkey;monkey.patch_all() # gevent 是并发库，monkey是猴子补丁可以让所有的阻塞模块变成非阻塞式
import time


def test(num):
    print(num)
    time.sleep(2)
# test(1)
# test(2)
# test(3)

# python中方法m默认都是阻塞的，执行完一个才能执行另外一个
# 使用协程完成函数调用

task = [
    # gevent.spawn("函数名"，参数)
    gevent.spawn(test,1),
gevent.spawn(test,2),
gevent.spawn(test,3),
gevent.spawn(test,4)

]
# 添加并执行所有的协程任务
gevent.joinall(task)