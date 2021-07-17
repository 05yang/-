# 文献模型复现
本工程复现了论文Evaluation of Classification algorithms for Distributed Denial of Service Attack Detection中的四种模型，同时完成了该论文的翻译工作

## Folders:
The repository is organised as follows:

- `Support_Vector_Machine.py` 支持向量机算法模型
- `Naive_Bayes.py` 朴素贝叶斯算法模型
- `Decision_Tree.py` 决策树算法模型
- `Logistic_Regression.py` 逻辑回归算法模型
- `Translate.pdf` 论文的中文翻译结果，内含实验的运行结果截图

## Data:
- 数据集使用的是新不伦瑞克大学（University of New Brunswick）的开源数据集CICDDoS2019，该数据集包含88个特征，获取地址：https://www.unb.ca/cic/datasets/ddos-2019.html
- 工程只针对CSV-03-11里的Portmap.csv数据进行了处理，利用了其中的15个特征字段

## 开发语言：
- python 3.7.0

## 开发环境：
- Windows 10
