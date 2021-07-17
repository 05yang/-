import pandas as pd

ufo = pd.read_csv('Portmap.csv', usecols = [' Total Fwd Packets', ' Total Length of Bwd Packets', ' Fwd Packet Length Mean', 'Bwd IAT Total', 'Total Length of Fwd Packets', 'Subflow Fwd Packets', ' Source Port', ' Average Packet Size', ' Protocol', ' Destination Port', ' Down/Up Ratio', ' Bwd Packet Length Mean', ' Source IP', ' Destination IP', ' Inbound', ' Label'])

X = ufo.iloc[:, :-1].values
y = ufo.iloc[:, -1].values

for i in X:    # 将IP化为整数
    i[0] = i[0].replace('.', '')
    i[2] = i[2].replace('.', '')
for i in y:
    if i == 'BENIGN':
        i = 1
    else:
        i = 0

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)    # 划分训练集、测试集

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train = sc.fit_transform(X_train)    # 训练集标准化
X_test = sc.transform(X_test)    # 在训练集基础上标准化

from sklearn.decomposition import PCA

pca = PCA(n_components = 4)    # 对数据进行降维
X_train = pca.fit_transform(X_train)
X_test = pca.transform(X_test)

explained_variance = pca.explained_variance_ratio_    # 获取各成分方差百分比

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix

clf = SVC(kernel='linear')    # 算法采用线性核函数
clf.fit(X_train, y_train)    # 训练数据集
y_pred = clf.predict(X_test)    # 对测试集进行测试
print('准确率为： ', accuracy_score(y_test, y_pred))
cm = confusion_matrix(y_test, y_pred)
print('TP为： ', cm[1][1])
print('TN为： ', cm[0][0])
print('FP为： ', cm[0][1])
print('FN为： ', cm[1][0])
