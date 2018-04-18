# Function :  匹配岗位信息 - 求职者
# Input :     学历，描述， 工作年限/经验
# Output:     【岗位id， 相似度】

import logging
import pickle
import gensim

import jieba.posseg
from gensim.models.doc2vec import Doc2Vec
from gensim.models.doc2vec import TaggedDocument
from sklearn.ensemble import RandomForestClassifier

from django.conf import settings

logger = logging.getLogger('django')

RFCModel = None
DocModel = None
dec = {}
dec_keyword = []
# 加载岗位描述关键词
logger.debug("加载岗位描述关键词....")
read = open(settings.BASE_DIR + "/backend/recommend/word/dec-answer.txt", "r")
for word in read.readlines():
    dec_keyword.append(word.strip())
    jieba.add_word(word.strip())
read.close()
logger.debug("岗位描述关键词加载完成!")

# 加载字典特征矩阵
logger.debug("加载字典特征矩阵....")
for word in dec_keyword:
    dec[word] = [0]
logger.debug("字典特征矩阵加载完成!")

# 加载Doc2Vec模型
logger.debug("加载Doc2Vec model中...")
DocModel = Doc2Vec.load(settings.BASE_DIR + "/backend/recommend/model/DCDEC")
logger.debug("Doc2Vec model 加载完成!")

# 加载RFC-Dec随机森林模型
# logger.debug("加载随机森林模型中...")
# read = open(settings.BASE_DIR + "/backend/recommend/model/randomForest.pkl", "rb")
# try:
#     RFCModel = pickle.load(read)
#     read.close()
# except Exception as err:
#     logger.debug("cuowu!!!")
# logger.debug("随机森林模型加载完成！")
