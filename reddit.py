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


