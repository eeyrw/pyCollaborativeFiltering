import tool
from functools import reduce
data = tool.loadData("user.csv")
from recommender import UserBased
ubcf = UserBased()
ubcf.loadData(data)
import similarity
simMeasure = similarity.cosine_intersection
for user in list(data.keys())[0:10]:
    recommendation = ubcf.Recommendation(user, simMeasure=simMeasure, nNeighbors=30,topN=5)
    print('User: %s\n    %s\n'%(user,recommendation))
