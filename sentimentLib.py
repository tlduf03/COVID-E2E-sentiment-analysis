import pandas as pd
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS
stopwords = set(STOPWORDS)

def sentimentClass(label):
    """
    This function will take sentiment labels in dataset and convert them
    into 3 classes(Positive, Negative, Neutral).

    Parameters:
        label : labeled sentiment
    
    Returns: simplified classes as lowercase string
    """
    assert isinstance(label, str)
    if label == 'Extremely Negative':
        return 'negative'
    elif label == 'Negative':
        return 'negative'
    elif label == 'Extremely Positive':
        return 'positive'
    elif label == 'Neutral':
        return 'neutral'
    elif label == 'Positive':
        return 'positive'

def remove_stopwords(text):
    """
    This function removes stopwords using wordcloud package.
    
    Parameters:
        text : tweets in the dataframe
    
    Returns: text with stopword removed 
    """
    assert isinstance(text,str)
    
    cleanedText = ' '.join([word for word in text.split() if word not in stopwords])
    
    return cleanedText

def remove_Aletter(text):
    """
    This function removes a single letter which might not have special meaning.
    
    Parameters:
        text : tweets in the dataframe
    
    Returns: text with a letter removed
    """
    assert isinstance(text,str)
    
    cleanedText = ' '.join([word for word in text.split() if len(word)!= 1])
    
    return cleanedText

def wordcloud_disp(text,num):
    """
    This function displays a most common words as wordcloud 
    
    Parameters:
        text : aggregated text over the dataframe 
         num : maximum number of words to display
        mask : mask of the image

    Returns: None
    """
    assert isinstance(text,str)
    
    wordcloud = WordCloud(max_font_size=50,max_words=num,stopwords=stopwords, background_color='black').generate(text)
    plt.figure(figsize=(15,15))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()
    