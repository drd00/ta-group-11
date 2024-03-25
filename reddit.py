import re
import spacy
import tldextract
import pandas as pd
from matplotlib import pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import numpy as np


reddit_data = pd.read_csv('./datasets/reddit/reddit_politics.csv')


def get_missing_data(data):
    total_missing = data.isnull().sum()
    percent_missing = (total_missing / len(data) * 100)
    missing_data = pd.concat([total_missing, percent_missing], axis=1, keys=['Total', 'Percent'])
    data_types = [str(data[col].dtype) for col in data.columns]
    missing_data['Types'] = data_types
    missing_data_transposed = missing_data.T
    return missing_data_transposed


def extract_domain(url):
    if "http" in str(url) or "www" in str(url):
        parsed = tldextract.extract(url)
        domain_parts = [parsed.domain, parsed.suffix]
        domain = ".".join(part for part in domain_parts if part)
        return domain
    else:
        return "NA"


pd.set_option('display.max_columns', None)

print(get_missing_data(reddit_data))

reddit_data.loc[:, 'source_domain'] = reddit_data.loc[:, 'url'].apply(lambda x: extract_domain(x))

print(reddit_data.head())

df_source = reddit_data['source_domain'].value_counts(ascending=False).reset_index()

df_source.columns = ['source_domain', 'count']

print(df_source.head())

# data cleaning
reddit_data['body'] = reddit_data['body'].astype(str)
# remove url and unicode
reddit_data['body'] = reddit_data['body'].apply(lambda x:re.sub(r'https?://\S+|www\.\S+', '', x))
reddit_data['title'] = reddit_data['title'].apply(lambda x:re.sub(r'[^\x00-\x7F]+', '', x))
reddit_data['body'] = reddit_data['body'].apply(lambda x:re.sub(r'[^\x00-\x7F]+', '', x))
# The empty field will have nan after processing
reddit_data['body'] = reddit_data['body'].apply(lambda x: re.sub(r'\bnan\b', '', x))
# delete "Comment" in title field
reddit_data['title'] = reddit_data['title'].apply(lambda x: re.sub(r'\bComment\b', '', x))
# merge title and body into new fields called post
reddit_data['post'] = reddit_data['title'] + ' ' + reddit_data['body']
# reddit_data.drop(['title', 'body'], axis=1, inplace=True)


def count_tokens_pipe(texts):
    # token_counts = [len(doc) for doc in nlp.pipe(texts, disable=["parser", "ner"])] # This may be faster
    token_counts = [len(doc) for doc in nlp.pipe(texts)]
    return token_counts


nlp = spacy.load("en_core_web_sm")

reddit_data['token_count'] = count_tokens_pipe(reddit_data['post'])
print(reddit_data.head())

# get the mean token count
print(reddit_data['token_count'].mean())

reddit_data.to_csv('./datasets/reddit/processedReddit.csv', index=False)