import tweepy
import time
import io

CONSUMER_KEY = 'XXXXXX'
CONSUMER_SECRET =  'XXXXXX'
ACCESS_KEY = 'XXXXXX'
ACCESS_SECRET = 'XXXXXX'


negative_word_file = 'negative.txt'
positive_woed_file = 'positive.txt'
resultingDataFile = open("resulting_data.csv","w")
auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
api = tweepy.API(auth) 

home = api.home_timeline()
for home_tweet in reversed(home):
    with io.open("my_twitter_data.txt","+a",encoding="utf-8") as file:
        file.write(home_tweet.text)
        file.close()

twitterDataFile = open("my_twitter_data.txt","r",encoding="utf-8")
resultingDataFile = open("resulting_data.csv","w")

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

positive_words = []
with open("positive.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

negative_words = []
with open("negetive.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

    
def strip_punctuation(strWord):
    for charPunct in punctuation_chars:
        strWord = strWord.replace(charPunct, "")
    return strWord

def get_pos(strSentences):
    strSentences = strip_punctuation(strSentences)
    listStrSentences= strSentences.split()
    
    count=0
    for word in listStrSentences:
        for positiveWord in positive_words:
            if word == positiveWord:
                count+=1
    return count

def get_neg(strSentences):
    strSentences = strip_punctuation(strSentences)
    listStrSentences = strSentences.split()
    
    count=0
    for word in listStrSentences:
        for negativeWord in negative_words:
            if word == negativeWord:
                count+=1
    return count


def writeInDataFile(resultingDataFile):
    resultingDataFile.write("Positive Score, Negative Score, Net Score")
    resultingDataFile.write("\n")

    linesPTDF =  twitterDataFile.readlines()
    headerDontUsed= linesPTDF.pop(0)
    for linesTD in linesPTDF:
        listTD = linesTD.strip().split(',')
        resultingDataFile.write("{}, {}, {}".format(get_pos(listTD[0]), get_neg(listTD[0]), (get_pos(listTD[0])-get_neg(listTD[0]))))    
        resultingDataFile.write("\n")    

writeInDataFile(resultingDataFile)
twitterDataFile.close()
resultingDataFile.close()


