import re
import nltk
import csv
import pandas as pd
import en_core_web_sm
from nltk.stem import WordNetLemmatizer 
from nltk.corpus import wordnet
from scipy.spatial import distance
import numpy as np
from sklearn.preprocessing import normalize
import string
import matplotlib.pyplot as plt    
from wordcloud import WordCloud

def tokenize(text2):
    # takes a list of comment strings and tokenizes
    new=[]
    tokens=[]
    count=0
    for text in text2:
        pattern=r'\w[\w\'-]*\w'      
        tokens=nltk.regexp_tokenize(text, pattern)
        tokens=[tokens.lower() for tokens in tokens]
        new+=tokens 
        count+=1
    return new

def analyze2(text2):
    # takes a list of comment strings and tokenizes and finds pairs of positive and negative words with specific phone features
    new=[]
    tokens=[]
    count=0
    negations=['not', 'too', 'n\'t', 'no', 'cannot', 'neither','nor']
    with open("positive-words.txt",'r') as f:
        positive_words=[line.strip() for line in f]
    with open("negative-words.txt",'r') as f:
        negative_words=[line.strip() for line in f]
    positive_tokens=[]
    negative_tokens=[] #N is 1 this time, negating word right before pos or neg word
    reviewpos=[]
    reviewneg=[]
    features=["headphones", "battery", "sound", "charge", "screensize", "size", "space", "storage", "camera", "speed", "display", "sensor", "casing", "price"]
    for text in text2:
        #text=text.strip(string.punctuation)
        #text=text.strip(" ")
        #tokens=nltk.word_tokenize(text)
        #tokens = re.split(r"\W+", text)
        pattern=r'\w[\w\'-]*\w'      
        tokens=nltk.regexp_tokenize(text, pattern)
        tokens=[tokens.lower() for tokens in tokens]
        #tokens=[token.strip(string.punctuation) for token in tokens]
        #tokens=[token.strip() for token in tokens if token.strip()!='']
        new.append(tokens) #change += to not have seperated list per comment
        count+=1
    for x in new:
        for i in range(0, len(x)):
            previ=""
            if i>0:
                previ=x[i-1]
            if previ in positive_words and x[i] in features:
                    reviewpos.append((previ,x[i]))
            if previ in negative_words and x[i] in features:
                    reviewneg.append((previ,x[i]))
    return reviewpos, reviewneg
  

def analyze(tokens):
    #finds positive and negative words, their count, and pairs of negative/positive sentiment expressions when there is a negation word before a sentiment word
    # this is not an exhaustive list of negation words!
    negations=['not', 'too', 'n\'t', 'no', 'cannot', 'neither','nor']
    with open("positive-words.txt",'r') as f:
        positive_words=[line.strip() for line in f]
    with open("negative-words.txt",'r') as f:
        negative_words=[line.strip() for line in f]
    positive_tokens=[]
    negative_tokens=[] #N is 1 this time, negating word right before pos or neg word
    for idx, token in enumerate(tokens):
        if token in positive_words:
             if idx>0:
                if tokens[idx-1] in negations:
                    negative_tokens.append(tuple(tokens[idx-1:idx+1]))
                else:
                    positive_tokens.append(token)
             else:
                positive_tokens.append(token)
        if token in negative_words:
            if idx>0:
                if tokens[idx-1] in negations:
                    positive_tokens.append(tuple(tokens[idx-1:idx+1]))
                else:
                    negative_tokens.append(token)
            else:
                negative_tokens.append(token)
    return positive_tokens, len(positive_tokens), negative_tokens, len(negative_tokens)

                    
def mostcommon(listname,no_stopword=False):
    #returns most common 3 words
    stop_words = nltk.corpus.stopwords.words('english')
    final=[]
    if no_stopword==True:
        for i in listname:
            if i not in stop_words:
                final.append(i)
    else:
        final=listname
    com=nltk.FreqDist(final)
    x=com.most_common(3)
    return x

def visual(count1,count2):
    #plots positive and geative word counts
    types=["positive", "negative"]
    counts=[count1,count2]
    plt.bar(types, counts)
    plt.ylabel('Type')
    plt.xlabel('Count')
    plt.title('Count of Comments by Sentiment Type')
    plt.show()
    
def wordcloud(reviews):
    #wordcloud generator for features in positive and negative reviews
    features=[]
    for i in reviews:
        features.append(i[1])
    text=" ".join([t for t in features])
    wordcloud = WordCloud().generate(text)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()
    return features

def topcomment(commentlist):
 #takes data on user, their comment, and comment likes to find most popular comment for commentlist for a product
    highest=0
    index=0
    commentlist2=commentlist.values.tolist()
    for x in range(0, len(commentlist)):
        if commentlist[x][2] > highest:
            highest=commentlist[x][2]
            index=x
    return commentlist[index]

def sortcomments(commentlist):
    #sorts comments by likes and returns the top three comments per product from the commentlist of each product
    commentlist=commentlist.sort_values(by='likes', ascending=False)
    commentlist2=commentlist.values.tolist()
    return commentlist2[0:3]

    
if __name__ == "__main__":

 # Test Q1
    #xscomments=pd.read_csv("final_set.csv", header=0, names=['user','commentText', 'likes'])
    #s10comments=pd.read_csv("s10.csv", header=0, names=['user','commentText', 'likes'])
    #pixel3comments=pd.read_csv("pixel3.csv", header=0, names=['user','commentText', 'likes'])
    #t6comments=pd.read_csv("6t.csv", header=0, names=['user','commentText', 'likes'])

    #print("Top 3 comments for apple xs:")
    #print(sortcomments(xscomments))
    #print("Top 3 comments for samsung s10:")
    #print(sortcomments(s10comments))
    #print("Top 3 comments for google pixel3:")
    #print(sortcomments(pixel3comments))
    #print("Top 3 comments for oneplus 6t:")
    #print(sortcomments(t6comments))
    
    #result=pd.read_csv("6t.csv", header=0)
    #result=result['commentText']
    #result=result.values.tolist()
    #result=list(map(str, result))
    #x=(tokenize(result))
    #a,b,c,d=analyze(x)
    #print(b,d)
    #visual(b,d)

    #result=pd.read_csv("6t.csv", header=0)
    #result=result['commentText']
    #result=result.values.tolist()
    #result=list(map(str, result))
    #x,y=(analyze2(result))
    #print(mostcommon(x)) #most common positive expressions of features
    #print(mostcommon(y))
    

    result=pd.read_csv("6t.csv", header=0)
    result=result['commentText']
    result=result.values.tolist()
    result=list(map(str, result))
    result=tokenize(result)
    print(mostcommon(result, True))
    
    
    #commentlist=pd.read_csv("Bia660Project.csv", header=0, names=['user','commentText', 'likes'])
    #print(sortcomments(commentlist))
    #commentlist2=commentlist.values.tolist()
    #print(commentlist[0])
    #print(topcomment(commentlist2))
   
    #result=pd.read_csv("Bia660Project.csv", header=0)
    #result=list(result['commentText'])
    ##print(result[0])

    
    #SPLIT SEPERATE EXCEL FILES FOR PRODUCT
    #text=["this is not good.", "terrible headphones", "it's great", "good screensize"]
    #print("Test 1")
    #x=(tokenize(result)) #tokenize reviews into list of words
    #print(x[0])
    #a,b,c,d=analyze(x) #gets back lists of positive and negative words and the lenght of each list
    #print(analyze(x))
    #print(mostcommon(a)) #most common positive sentiment words
    #print(mostcommon(c)) #most common negative sentiment words
    #visual(b,d) #graph of word count positive vs negative sentiments
    
    #print("Test 2")
    #x,y=(analyze2(text))
    #print(x)#positive feature sentiment reviews
    #print(y) #negative feature sentiment reviews
    #print(wordcloud(x))  #wordcloud of positive features
    #print(wordcloud(y)) #wordcloud of negative features
    #print(mostcommon(x)) #most common positive expressions of features
    #print(mostcommon(y)) #most common negative expressions of features
   
    
    
