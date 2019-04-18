import tool
trainSet = tool.loadData("user.csv")
testSet = trainSet
from recommender import UserBased
ubcf = UserBased()
ubcf.loadData(trainSet)
model = ubcf.loadExtModel('ubcf.model')
from validation import CrossValidation
cv=CrossValidation()
import similarity
simMeasure = similarity.cosine_intersection
result = cv.LeaveOneOut(trainSet,ubcf,model= model,simMeasure=simMeasure)
print(result)