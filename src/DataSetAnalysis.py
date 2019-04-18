import os
import pandas as pd
import numpy as np
import pprint
import os.path
import pickle

def getUserAndFilmList(data):
    filmSet=set()
    userSet=set()
    for user,films in data.items():
        filmSet.update(films)
        userSet.add(user)
    return (userSet,filmSet)

def getUserRateCount(data):
    rateCount=0
    for _,films in data.items():
        rateCount+=len(films)
    return rateCount  

if __name__ == '__main__':
    data={}
    with open('user.cache','rb') as f:
        data=pickle.load(f)
    userSet,filmSet=getUserAndFilmList(data)
    rateCount=getUserRateCount(data)
    print('User#:%d,Film#:%d,RateCount#:%d'%(len(userSet),len(filmSet),rateCount))
    print('Sparse:%f%%'%(rateCount*100/(len(userSet)*len(filmSet))))
