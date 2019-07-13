#!/usr/bin/env python
# coding: utf-8

# In[9]:


# Program for analyzing some of my facebook conversations with any one/many individual(s)
import numpy as np
import os
import json
#import sys
from datetime import datetime

from wordcloud import WordCloud, STOPWORDS
from PIL import Image

path = 'D:\\Python\\fb convo analysis'
os.chdir(path)


# In[10]:


# Function that gets json from directory
def get_message(query):
    message_path = os.path.join(path, 'facebook-shawnliu90\messages\inbox') # get a user input later
    # searching through message_path for query
    message_folder = os.listdir(message_path)
    # combining message path with the file name
    message_file = os.path.join(message_path, 
                list(filter(lambda x: query in x, message_folder))[0], 
                'message_1.json')
    #message_file = os.path.join(message_file, 'message_1.json')
    # loading message file as json
    with open(message_file, 'r') as json_file:  
        file = json.load(json_file)
    return file
    
# Function that formats the message for various purposes
def format_message(messages):
    '''
    extracting all text into one concatenated string to use for wordcloud
    other NLP formats yet to be determined
    '''  

# Wordcloud function
def create_wordcloud(text):
    # Mask image for the shape of the cloud
    mask = np.array(Image.open(os.path.join(path, 'mask.png')))
    # Filtering out stopwords like the, and, is, etc.
    stopwords = set(STOPWORDS)
    wc = WordCloud(background_color='white',
                  mask=mask,
                  max_words=150,
                  stopwords=stopwords)
    # Generating the wordcloud and saving it to wordcloud.png in path 
    wc.generate(text)
    wc.to_file(os.path.join(path, 'fb_wordcloud.png'))

text = get_message('AlysaaCoco')
#create_wordcloud(get_message('insert friend name'))


# In[ ]:


# Function that conducts sentiment analysis    
def sentiment_analysis(text):
    '''
    do some analysis on sentiment, as well as other preliminary analyses
    '''


# In[ ]:


# TBD more complicated stuff
def context_analysis(text):
    ''' 
    using spacy and other nlp libraries to do some more advanced analysis 
    - context
    - named entities
    - similar conversations between different people
    '''

