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
for user in list(data.keys())[42:62]:
    recommendation = ubcf.Recommendation(user, simMeasure=simMeasure, nNeighbors=30,topN=5)
    print('User: %s\n    %s\n'%(user,recommendation))
