# 20210424 UserCF demo
# movie recommend
import pandas as pd


def prediction(df, userdf, Nn=15):
    # 预测用户未评分电影的评分
    corr = df.T.corr()     # 计算用户的相关person相关系数矩阵
    rats = userdf.copy()
    for usrid in userdf.index:
        # step1:获取用户未评分电影
        dfnull = df.loc[usrid][df.loc[usrid].isnull()]    # 用户user1没有评分的电影：('mov6',nan)
        usrv = df.loc[usrid].mean()                       # 用户user1电影评分的均值
        # step2: 预测未评分电影的分值
        for i in range(len(dfnull)):
            nft = (df[dfnull.index[i]]).notnull()         # 用户user1没有评分的电影，其他人评分与否
            if(Nn <= len(nft)):
                nlist = df[dfnull.index[i]][nft][:Nn]     # 用户user1没有评分的电影，前Nn有评分的人
            else:
                nlist = df[dfnull.index[i]][nft][:len(nft)]   # len(df[dfnull.index[i]][nft]) < len(nft), 有啥用呢
            # 1)获取非null相关系数，有评分人列表
            nlist = nlist[corr.loc[usrid, nlist.index].notnull()]  # 用户user1 和 有评分人的非null 相关系数的评分人列表
            nratsum, corsum = 0, 0
            if(0!=nlist.size):
                nv = df.loc[nlist.index,:].T.mean()         # 相关有评分人对所有电影的评分的平均值
                for index in nlist.index:                   # 相关评论人userx
                    ncor = corr.loc[usrid, index]           # 用户user1 和 userx相关系数
                    nratsum += ncor*(df[dfnull.index[i]][index]-nv[index])   # ncor*(df['mov6'][userx]-nv[userx])
                    corsum += abs(ncor)
                if(corsum != 0):
                    rats.at[usrid, dfnull.index[i]] = usrv + nratsum/corsum   # 预测用户user1对没有评分电影的评分
                else:
                    rats.at[usrid, dfnull.index[i]] = usrv                    # 无其他用户评分修正的情况下，用自己的评分均值填补
            else:
                rats.at[usrid,dfnull.index[i]] = None
    return rats
def recomm(df, userdf, Nn=15, TopN=3):
    # 依据为未评分电影预测评分，给出每个用户的推荐列表。
    ratings = prediction(df, userdf, Nn)
    recomm = []
    for usrid in userdf.index:
        # 按Nan值获取未评分项
        ratft = userdf.loc[usrid].isnull()
        ratnull = ratings.loc[usrid][ratft]
        # 对预测评分项进行排序
        if(len(ratnull) >= TopN):
            sortlist = (ratnull.sort_values(ascending=False)).idnex[:TopN]
        else:
            sortlist = ratnull.sort_values(ascending=False).index[:len(ratnull)]
        recomm.append(sortlist)
    return ratings,recomm



if __name__ == "__main__":
    print("------使用基于UserCF算法对电影进行推荐中...-----")
    traindata = pd.read_csv("./data/Chapter10/u1.base", sep='\t', index_col=None, header=None)  # [用户ID,电影ID,电影评分,时间标签] 8W条数据
    print(traindata.head())
    testdata = pd.read_csv("./data/Chapter10/u1.test", sep='\t', index_col=None, header=None)
    # 删除时间列--本例中没有用
    traindata.drop(3, axis=1, inplace=True)
    testdata.drop(3, axis=1, inplace=True)
    # 行与列重新命名
    traindata.rename(columns={0: 'userid', 1: 'movid', 2: 'rat'}, inplace=True)
    testdata.rename(columns={0: 'userid', 1: 'movid', 2: 'rat'}, inplace=True)
    # 整理成共现矩阵
    traindf = traindata.pivot(index='userid', columns='movid', values='rat')
    testdf = testdata.pivot(index='userid', columns='movid', values='rat')
    # 重命名表格的行和列
    traindf.rename(index={i: 'user%d'%i for i in traindf.index}, inplace=True)
    testdf.rename(index={i: 'user%d'%i for i in testdf.index}, inplace=True)
    traindf.rename(columns={i: 'mov%d'%i for i in traindf.columns}, inplace=True)
    testdf.rename(columns={i: 'mov%d'%i for i in testdf.columns}, inplace=True)
    print('d', traindata.head())
    userdf = traindf.loc[testdf.index]
    trainrats, trainrecom = recomm(traindf, userdf)
    print(trainrecom.head())
    print('end')