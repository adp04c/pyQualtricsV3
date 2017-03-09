# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 10:52:49 2017

@author: AustinPeel
"""

from pyQualtricsV3 import api 
from pandas.io.json import json_normalize

surveyId = "SV_XXX"
distributionid = "EMD_XXX"
contactsId = "ML_XXX"
responseId = "insert"

#get Distribution summary by Survey
jsonData = api.qualtrics(survey=surveyId).getListDistributions()
df = json_normalize(jsonData['result']['elements'])

#gets the distribution summary for only one distribution ID. (kind of pointless)
jsonData = api.qualtrics(survey=surveyId).getDistributions(distributionId=distributionid)
df = json_normalize(jsonData['result'])

#get df of all contacts for a distributionId. the status column is bogus 
df = api.qualtrics().getAllContacts(distributionId=distributionid)

# this function isnt done the output shows multiple email history per person, we need to reconcile that before dumping it into a df. 
jsonData = api.qualtrics(survey=surveyId).getContacts(contactsId)

#download data and extract it from zip
#parameters=(lastResponseId,startDateendDate,limit,includedQuestionIds,useLabels,useLocalTime)
#defaults to csv(fileFormat="csv")
api.qualtrics(survey=surveyId).downloadExtractZip(lastResponseId=responseId)
api.qualtrics(survey=surveyId).downloadExtractZip()


