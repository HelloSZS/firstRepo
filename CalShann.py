from math import log

#默写
def calShanonEnt(dataSet):
    data_count = len(dataSet)

    labels = {}

    # 统计每个label的出现的次数
    for data in dataSet:
        currentlabel = data[-1]

        labels[currentlabel] = labels.get(currentlabel,0) + 1

    ShannonEnt = 0.0
    Gini = 0.0
    # 计算每个label的出现的概率
    for label in labels:
        this_labelcount = labels[label]
        prober = float(this_labelcount/data_count)
        ShannonEnt -= prober*log(prober,2)
        Gini += prober * (1-prober)

    return ShannonEnt,Gini


def calShannonEnt(dataSet):
    data_count = len(dataSet)

    labelCounts = {}

    #统计各个label出现的次数
    for featVec in dataSet:
        currnetlabel = featVec[-1]
        labelCounts[currnetlabel] = labelCounts.get(currnetlabel,0) + 1
    print(labelCounts)
    shannonEnt = 0.0

    #计算每个key(label对应value)出现的频率，作为概率
    for key in labelCounts:
        prob = float(labelCounts[key]/data_count)
        # Plog_2P
        shannonEnt -= prob*log(prob,2)

    return shannonEnt

def createDataset():
    dataset = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]

    labels = ['no surfacing', 'flippers']

    return dataset, labels

dataset, label = createDataset()

print(dataset)
print("Shannon, Gini:",calShanonEnt(dataset))


# 切割数据集，比如
#[[1,2,3]，
# [2,3,4]，
# [3.4.5]]
#要把第一列的数据value=2的切割出来

def splitdata(dataSet, axis, value):
    splitdataset = []
    for data in dataSet:
        if data[axis] == value:
            temp = data[:axis]
            temp.extend(data[axis+1:])
            splitdataset.append(temp)

    return splitdataset

a = [[1, 2, 3],
     [2, 3, 4],
     [3, 4, 5]]

print(splitdata(a,0,1))

# 选择最好的数据集划分方式

def chooseBestFeatureTosplit(dataset):
    num_feature = len(dataset[0]) - 1
    print('num_feature',num_feature)
    baseEntropy = calShannonEnt(dataset)

    bestInfogain = 0.0; bestFeature = -1

    # i，代表第i个特征
    for i in range(num_feature):
        # 把每个数据对应位置的特征取出来，放进feat_list
        feat_list = [example[i] for example in dataset]

        # list转为集合，集合有一个特征是：没有重复的数值
        uniquevals = set(feat_list)

        newEntropy = 0.0

        for value in uniquevals:
            subdataset = splitdata(dataset, i, value)
            # 计算这个特征中，这个value出现的数量
            # 以及算出，用这个value切割出的subdataset占总dataset的比例
            # 即这个特征、这个value在data中出现的数量，占dataset的比例
            prob = len(subdataset)/float(len(dataset))
            newEntropy += prob*log(prob,2)
        infogain = baseEntropy - newEntropy
        print(f'{i},{newEntropy}')
        if(infogain > bestInfogain):
            bestInfogain = infogain
            bestFeature = i

    return bestFeature

print(f'the best feature index is : {chooseBestFeatureTosplit(dataset)}')