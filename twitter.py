import string
from collections import Counter
import matplotlib.pyplot as plt
import GetOldTweets3  as got
from datetime import date
def get_tweets():
    today_date=date.today()
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('Internship') \
        .setSince("2020-01-01") \
        .setUntil(str(today_date)) \
        .setMaxTweets(100)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    text_tweets=[[tweet.text] for tweet in tweets]
    return text_tweets
text_tweet=get_tweets()
text=""
for i in text_tweet:
    text=i[0]+" "+text
lower_case=text.lower()
cleaned_text=lower_case.translate(str.maketrans('','',string.punctuation))
tokenization_word=cleaned_text.split()
stop_words=["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
final_words=[]
for i in tokenization_word:
    if i not in stop_words:
        final_words.append(i)
emotion_list=[]
with open('emotions.txt','r') as f:
    for line in f:
        clear_line=line.replace('\n','').replace(',','').replace("'",'').strip()
        word,emotion=map(str,clear_line.split(':'))
        if word in final_words:
            emotion_list.append(emotion)
# print(emotion_list)
w=Counter(emotion_list)
fig,axl=plt.subplots()
axl.bar(w.keys(),w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()