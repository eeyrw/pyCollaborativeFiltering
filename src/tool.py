import os
import pandas as pd
import numpy as np
import pprint



def loadData(filePath, inv = False):
    '''
    Load data from a input file into memory with dictionary format.
    * Input file format: userID \t itemID \t rating \n
    * Output data format: {userID: {itemID: rating, ...}, ...}
    '''
    data = {}
    try:
        print('Load CSV')
        dat=pd.read_csv(filePath)
        print('Convert CSV')
        for _,row in dat.iterrows():
            user=row['用户名']
            item=row['电影名']
            rating=row['评分']
            if inv == False:
                data.setdefault(user, {})
                data[user][item] = float(rating)
            else:
                data.setdefault(item, {})
                data[item][user] = float(rating)
        # with open(filePath) as file:
        #     for line in file:
        #         line = line.replace("\n", "")
        #         tokens = line.split("\t")
                
        #         if len(tokens) < 2:
        #             continue
        #         elif len(tokens) == 2:
        #             user = tokens[0]
        #             item = tokens[1]
        #             rating = 1
        #         else:
        #             user = tokens[0]
        #             item = tokens[1]
        #             rating = tokens[2]
                
        #         # Store data
        #         if inv == False:
        #             data.setdefault(user, {})
        #             data[user][item] = float(rating)
        #         else:
        #             data.setdefault(item, {})
        #             data[item][user] = float(rating)
        #     file.close()

    except IOError as e:
        print(e)
    return data

def transposePrefs(prefs):
    '''
    Transpose the preference data by switching object and subject.
    For example, the preference data on users can be transformed into the preferences data on items.
    '''
    transposed = {}
    for obj in prefs:
        for subj in prefs[obj]:
            transposed.setdefault(subj, {})
            transposed[subj][obj] = prefs[obj][subj]
    return transposed

def getCurrentDir(filePath):
    return os.path.dirname(os.path.abspath(filePath)) + "/"

def getFilename(filePath):
    return os.path.basename(filePath)

def getFilenameWithoutExtension(filePath):
    fullname = getFilename(filePath)
    return os.path.splitext(fullname)[0]

if __name__ == '__main__':
    a=pd.read_csv('user.csv')
    for row in a.loc[:, ['用户ID','电影名','评分']].iterrows():
        print(row[1]['电影名'])
