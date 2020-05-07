from sklearn.preprocessing import OneHotEncoder
from sklearn.datasets import load_iris
iris = load_iris()
#哑编码，对IRIS数据集的目标值，返回值为哑编码后的数据
a = OneHotEncoder().fit_transform(iris.target.reshape((-1,1)))
print(a)