import tweepy
import token
import preprocess

# Load credential
token_ = token.get()



consumer_key = token_['consumer_key']
consumer_secret = token_['consumer_secret']
access_token = token_['access_token']
access_token_secret = token_['access_token_secret']
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#api.update_status(status="Je suis un robot donc repond moi")
results = api.search(q = "marine pen", since_id='2016-03-30 00:00',lang='fr',count=100000)
data = []
for result in results:
        data.append(preprocess.hash(result.text,stopwords=['le','la','a','de','du','et','l','t','avec','j','si','d','les','un','pour','pas','leur','en','des','est','il','au']))
	#data.append(result.text)
import operator
x = preprocess.tfidf_(data)
#x,vocab = preprocess.tfidf_sk(data)
#print vocab
sorted_x = sorted(x.items(), key=operator.itemgetter(1),reverse=True)
print sorted_x[:50]
