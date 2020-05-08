# 数据清洗
user_info1 = user_info[(user_info["性别"] == "男") | (user_info["性别"] == "女")]  # 去除掉性别不为男女的部分
user_info1 = user_info1.reindex(range(0, 5212))  # 重置索引

user_index1 = user_info1[(user_info1["国家城市"].isnull() == True) & (user_info1["星座"].isnull() == False)
                         & (user_info1["星座"].map(lambda s: str(s).find("座")) == -1)].index
for index in user_index1:
    user_info1.iloc[index, 3] = user_info1.iloc[index, 2]

user_index2 = user_info1[((user_info1["国家城市"].isnull() == True) & (user_info1["星座"].isnull() == True)
                          & (user_info1["年龄"].isnull() == False) & (
                                      user_info1["年龄"].map(lambda s: str(s).find("岁")) == -1))].index
for index in user_index2:
    user_info1.iloc[index, 3] = user_info1.iloc[index, 1]

user_index3 = user_info1[((user_info1["星座"].map(lambda s: str(s).find("座")) == -1) &
                          (user_info1["年龄"].map(lambda s: str(s).find("座")) != -1))].index
for index in user_index3:
    user_info1.iloc[index, 2] = user_info1.iloc[index, 1]

user_index4 = user_info1[(user_info1["星座"].map(lambda s: str(s).find("座")) == -1)].index
for index in user_index4:
    user_info1.iloc[index, 2] = "未知"

user_index5 = user_info1[(user_info1["年龄"].map(lambda s: str(s).find("岁")) == -1)].index
for index in user_index5:
    user_info1.iloc[index, 1] = "999岁"

user_index6 = user_info1[(user_info1["国家城市"].isnull() == True)].index
for index in user_index6:
    user_info1.iloc[index, 3] = "其他"

# 词云图制作
import fool
from collections import Counter
from PIL import Image, ImageSequence
from wordcloud import WordCloud, ImageColorGenerator

# 因留言结构比较乱，所以先保存到本地做进一步处理
# 删除掉一些html元素
pd.DataFrame(comment).to_csv(r"C:\Users\zhangjunhong\Desktop\comment.csv")

# 处理完以后再次载入进来
comment_data = pd.read_excel(r"C:\Users\zhangjunhong\Desktop\comment.xlsx")

# 将数据转换成字符串
text = (",").join(comment_data[0])

# 进行分词
cut_text = ' '.join(fool.cut(text))

# 将分词结果进行计数
c = Counter(cut_text)
c.most_common(500)  # 挑选出词频最高的500词

# 将结果导出到本地进行再一次清洗,删除无意义的符号词
pd.DataFrame(c.most_common(500)).to_excel(r"C:\Users\zhangjunhong\Desktop\fenci.xlsx")

# 导入背景图，这里选择菊姐头像
image = Image.open('C:/Users/zhangjunhong/Desktop/图片1.png')

# 将图片信息转换成数组形式
graph = np.array(image)

# 设置词云参数
# 参数分别是指定字体、背景颜色、最大的词的大小、使用给定图作为背景形状
wc = WordCloud(font_path="C:\\Windows\\Fonts\\simkai.ttf", background_color='White', max_words=150, mask=graph)

fp = pd.read_csv(r"C:\Users\zhangjunhong\Desktop\da200.csv", encoding="gbk")  # 读取词频文件
name = list(fp.name)  # 词
value = fp.time  # 词的频率
dic = dict(zip(name, value))  # 词以及词频以字典形式存储

# 根据给定词频生成词云
wc.generate_from_frequencies(dic)
image_color = ImageColorGenerator(graph)

plt.imshow(wc)
plt.axis("off")  # 不显示坐标轴
plt.show()

# 保存结果到本地
wc.to_file('C:/Users/zhangjunhong/Desktop/wordcloud.jpg')

# 地图绘制
# 导入相关库
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.patches import Polygon
from mpl_toolkits.basemap import Basemap
from matplotlib.collections import PatchCollection

# 将省份和城市进行分列
country_data = pd.DataFrame([country.split(" ") for country in user_info1["国家城市"]], columns=["省份", "城市"])

# 将国家和城市与user表合并
user_data = pd.merge(user_info1, country_data, left_index=True, right_index=True, how="left")

# 按省份进行分组计数
shengfen_data = user_data.groupby("省份")["性别"].count().reset_index().rename(columns={"性别": "人次"})

# 需要先对各省份地址进行经纬度解析
# 导入解析好的省份经纬度信息
location = pd.read_table(r"C:\Users\zhangjunhong\Desktop\latlon_106318.txt", sep=",")

# 将省份数据和经纬度进行匹配
location_data = pd.merge(shengfen_data, location[["关键词", "地址", "谷歌地图纬度", "谷歌地图经度"]],
                         left_on="省份", right_on="关键词", how="left")

# 进行地图可视化
# 创建坐标轴
fig = plt.figure(figsize=(16, 12))
ax = fig.add_subplot(111)

# 需要提前下载中国省份地图的.shp
# 指明.shp所在路径进行导入
basemap = Basemap(llcrnrlon=75, llcrnrlat=0, urcrnrlon=150, urcrnrlat=55, projection='poly', lon_0=116.65, lat_0=40.02,
                  ax=ax)
basemap.readshapefile(shapefile="C:/Users/zhangjunhong/Desktop/CHN_adm/CHN_adm1", name="china")


# 定义绘图函数
def create_great_points(data):
    lon = np.array(data["谷歌地图经度"])
    lat = np.array(data["谷歌地图纬度"])
    pop = np.array(data["人次"], dtype=float)
    name = np.array(data["地址"])
    x, y = basemap(lon, lat)
    for lon, lat, pop, name in zip(x, y, pop, name):
        basemap.scatter(lon, lat, c="#778899", marker="o", s=pop * 10)
        plt.text(lon, lat, name, fontsize=10, color="#DC143C")


# 在location_data上调用绘图函数
create_great_points(location_data)

plt.axis("off")  # 关闭坐标轴
plt.savefig("C:/Users/zhangjunhong/Desktop/itwechat.png")  # 保存图表到本地
plt.show()  # 显示图表

# 树地图绘制
import squarify

# 创建数据
xingzuo = user_info1["星座"].value_counts(normalize=True).index
size = user_info1["星座"].value_counts(normalize=True).values
rate = np.array(
    ["34%", "6.93%", "5.85%", "5.70%", "5.62%", "5.31%", "5.30%", "5.24%", "5.01%", "4.78%", "4.68%", "4.36%"])

# 绘图
colors = ['steelblue', '#9999ff', 'red', 'indianred',
          'green', 'yellow', 'orange']
plot = squarify.plot(sizes=size,  # 指定绘图数据
                     label=xingzuo,  # 指定标签
                     color=colors,  # 指定自定义颜色
                     alpha=0.6,  # 指定透明度
                     value=rate,  # 添加数值标签
                     edgecolor='white',  # 设置边界框为白色
                     linewidth=3  # 设置边框宽度为3
                     )
# 设置标签大小
plt.rc('font', size=10)
# 设置标题大小
plt.title('菊粉星座分布', fontdict={'fontsize': 12})

# 去除坐标轴
plt.axis('off')
# 去除上边框和右边框刻度
plt.tick_params(top='off', right='off')

# 自定义词云图
image = Image.open('C:/Users/zhangjunhong/Desktop/图片1.png')  # 作为背景形状的图
graph = np.array(image)
# 参数分别是指定字体、背景颜色、最大的词的大小、使用给定图作为背景形状
wc = WordCloud(font_path="C:\\Windows\\Fonts\\simkai.ttf", background_color='White', max_words=150, mask=graph)

name = ["女性", "摩羯座", "20岁", "21岁", "22岁", "23岁", "24岁", "25岁", "广州", "杭州", "成都", "武汉", "长沙", "上海", "北京", "海外", "美国",
        "深圳"]
value = [20, 20, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]  # 词的频率
dic = dict(zip(name, value))  # 词频以字典形式存储
wc.generate_from_frequencies(dic)  # 根据给定词频生成词云
image_color = ImageColorGenerator(graph)
plt.imshow(wc)
plt.axis("off")  # 不显示坐标轴
plt.show()
wc.to_file('C:/Users/zhangjunhong/Desktop/wordcloud.jpg')