import pandas as pd
ufo = pd.read_csv('Portmap.csv', usecols = [' Total Fwd Packets', ' Total Length of Bwd Packets', ' Fwd Packet Length Mean', 'Bwd IAT Total', 'Total Length of Fwd Packets', 'Subflow Fwd Packets', ' Source Port', ' Average Packet Size', ' Protocol', ' Destination Port', ' Down/Up Ratio', ' Bwd Packet Length Mean', ' Source IP', ' Destination IP', ' Inbound', ' Label'])

X = ufo.iloc[:, :-1].values
y = ufo.iloc[:, -1].values

for i in X:
    i[0] = i[0].replace('.', '')
    i[2] = i[2].replace('.', '')
for i in y:
    if i == 'BENIGN':
        i = 1
    else:
        i = 0

from sklearn.model_selection import train_test_split 
  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

from sklearn.preprocessing import StandardScaler 
sc = StandardScaler() 
X_train = sc.fit_transform(X_train) 
X_test = sc.transform(X_test)

from sklearn.decomposition import PCA 
pca = PCA(n_components = 4) 
X_train = pca.fit_transform(X_train) 
X_test = pca.transform(X_test) 
  
explained_variance = pca.explained_variance_ratio_ 


from sklearn.linear_model import LogisticRegression   
classifier = LogisticRegression(random_state = 0) 
classifier.fit(X_train, y_train)

from sklearn.metrics import confusion_matrix,accuracy_score 
y_pred = classifier.predict(X_test)
print('准确率为： ', accuracy_score(y_test, y_pred))
cm = confusion_matrix(y_test, y_pred)
print('TP为： ', cm[1][1])
print('TN为： ', cm[0][0])
print('FP为： ', cm[0][1])
print('FN为： ', cm[1][0])
