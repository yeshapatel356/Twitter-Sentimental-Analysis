# Twitter-Sentimental-Analysis


# Set Up
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

# Run
analysis_neg_pos.py
