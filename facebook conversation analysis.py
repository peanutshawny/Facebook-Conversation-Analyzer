#!/usr/bin/env python
# coding: utf-8

# In[25]:


# Program for analyzing some of my facebook conversations with any one/many individual(s)
import wikipedia
import numpy as np
import os
import json
#import sys
from datetime import datetime

from wordcloud import WordCloud, STOPWORDS
from PIL import Image

path = 'D:/Python/fb convo analysis'
os.chdir(path)


# In[26]:


# Function that gets text content from json --REPLACE WIKI WITH FB MESSAGES LATER
def get_text(query):
    # Get best matching title for given query
    title = wikipedia.search(query)[0]
    # Get wikipedia page for selected title
    page = wikipedia.page(title)
    return page.content

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
    wc.to_file(os.path.join(path, 'wordcloud.png'))
    
create_wordcloud(get_text('python programming language'))


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

