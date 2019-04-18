import tool
from functools import reduce
print('Load Data.')
data = tool.loadData("user.csv")
from recommender import UserBased
ubcf = UserBased()
print('Load Data Again.')
ubcf.loadData(data)
import similarity
simMeasure = similarity.cosine_intersection
ubcf.buildModel(simMeasure = simMeasure, nNeighbors = 30, pathDump = 'ubcf.model')
model= ubcf.loadExtModel('ubcf.model')
with open('pred_result.txt','w',encoding='utf-8') as f:
    for user in list(data.keys()):#[42:62]:
        recommendation,userLike= ubcf.Recommendation(user, model= model,simMeasure=simMeasure, nNeighbors=30,topN=5)
        f.write('User: %s\n    U:%s\n    P:%s\n'%(user,recommendation,userLike))
