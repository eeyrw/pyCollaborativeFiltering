import tool
trainSet = tool.loadData("user.csv")
testSet = trainSet
from recommender import UserBased
ubcf = UserBased()
ubcf.loadData(trainSet)
model = ubcf.buildModel(nNeighbors=30)
import validation
result = validation.evaluateRecommender(testSet, ubcf, model=model, topN=10)
print(result)