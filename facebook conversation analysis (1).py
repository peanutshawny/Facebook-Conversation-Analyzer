#!/usr/bin/env python
# coding: utf-8

# In[153]:


# Program for analyzing some of my facebook conversations with any one/many individual(s)
import numpy as np
import os
import json
from datetime import datetime

from wordcloud import WordCloud, STOPWORDS
from PIL import Image

path = 'D:\\Python\\fb convo analysis'
os.chdir(path)


# In[154]:


# Function that gets json from directory
def get_message(query):
    message_path = os.path.join(path, 'facebook-shawnliu90\messages\inbox') # get a user input later
    # Searching through message_path for query
    message_folder = os.listdir(message_path)
    # Combining message path with the file name
    message_file = os.path.join(message_path, 
                list(filter(lambda x: query in x, message_folder))[0], 
                'message_1.json')
    with open(message_file, 'r') as json_file:  
        file = json.load(json_file)
    return file

text = get_message('JessicaMyles')


# In[155]:


# Function that formats the message for various purposes --WORDCLOUD FIRST
def format_message(messages):
    message_string = ''
    for content in messages['messages']:
        if 'content' in content.keys():
            message_string = message_string + ' ' + content['content']
    message_string = message_string.rstrip().lstrip()
    return message_string

text_message = format_message(text).lower()


# In[156]:


junk_words = {'lol', 'yeah', 'okay', 'thank', 'thanks', 'you', 'man'
              'go', 'think', 'oh', 'ok','that', 'thats', 'yo', 'ya','bro'}
# Removing junk words by adding to stopwords
for word in junk_words:
    STOPWORDS.add(word)

# Wordcloud function
def create_wordcloud(text):
    # Mask image for the shape of the cloud
    mask = np.array(Image.open(os.path.join(path, 'mask.png')))
    # Filtering out stopwords like the, and, is, etc.
    stopwords = set(STOPWORDS)
    wc = WordCloud(background_color='white',
                  mask=mask,
                  max_words=200,
                  stopwords=stopwords)
    # Generating the wordcloud and saving it to wordcloud.png in path 
    wc.generate(text)
    wc.to_file(os.path.join(path, 'fb_wordcloud.png'))

create_wordcloud(text_message)


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

