# Twitter-Sentimental-Analysis
It is an automatic process to determining whether a text segment contains objective or opinionated content, and it can furthermore determine the text’s sentiment polarity. The goal of Twitter sentiment classification is to automatically determine whether a tweet’s sentiment polarity is negative or positive.

## Set Up
1. You need to have Python 3 installed on your system.
2. This bot uses tweepy module.You can install tweepy by using pip. To install tweepy, use this command :
```cmd
 pip install tweepy
 ```
```python
git clone https://github.com/tweepy/tweepy.gitcd tweepypython setup.py install
```
3. Next, we need to link our Twitter account to our Python script. Go to [Twitter Developer](https://developer.twitter.com/en) and sign in with your account. Create a Twitter application and generate a Consumer Key, Consumer Secret, Access Token, and Access Token Secret. Now you are ready to begin!Under your import statements store your credentials within variables and then use the second block of code to authenticate your account with tweepy.

```python
CONSUMER_KEY = 'XXXXXX'
CONSUMER_SECRET = 'XXXXXX'
ACCESS_KEY = 'XXXXXX'
ACCESS_SECRET = 'XXXXXX'
```
```python
auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
api = tweepy.API(auth)
````
In order to check if your program is working you could add:
```python
user = api.me()
print (user.name)
```
This should return the name of your Twitter account in the console.

## Run
analysis_neg_pos.py

## Conclusion
The analysis of Twitter data is being done in different points of view to mine the opinion or sentiment. Our proposed approach
classify the tweets as Positive and Negative tweets which further helps in sentiment analysis and uses that sentiment analysis
for further decision making. For our prototype, Twitter API is utilized to gather data in real-time. The prototype back-end tests
on retrieving and processing the API data indicate that it is successful in gathering large amounts of data from popular search
terms in real-time. We will use various machine learning algorithms to conduct sentiment analysis using the extracted features.
However, just relying on individual models did not give a high accuracy so we pick the top few models to generate a model. 

