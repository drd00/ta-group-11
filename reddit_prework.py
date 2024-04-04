import re
import spacy
import tldextract
import pandas as pd
import nltk
from nltk.stem.porter import PorterStemmer
from spacy.lang.en.stop_words import STOP_WORDS as SPACY_STOP_WORDS
from nltk.corpus import stopwords

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
    token_counts = [len(doc) for doc in nlp.pipe(texts)]
    return token_counts

# run python -m spacy download en_core_web_sm
nlp = spacy.load("en_core_web_sm")

reddit_data['token_count'] = count_tokens_pipe(reddit_data['post'])
print(reddit_data.head())

# get the mean token count
print(reddit_data['token_count'].mean())

# Initialize NLTK's stemmer,
# You may try run
# ```sudo python -m nltk.downloader -d /usr/local/share/nltk_data all```
# in your terminal to download all the nltk data
nltk.download('stopwords')
stemmer = PorterStemmer()

# Initialize list of stopwords
nltk_stopwords = set(stopwords.words('english'))
all_stopwords = SPACY_STOP_WORDS.union(nltk_stopwords)


def preprocess_texts(texts):
    processed_texts_no_stop = []
    processed_texts_with_stop = []

    for doc in nlp.pipe(texts, disable=["parser", "ner"]):
        tokens_with_stop = [token.lemma_ for token in doc if not token.is_punct and not token.is_space]
        tokens_no_stop = [token for token in tokens_with_stop if token.lower() not in nltk_stopwords]

        processed_texts_with_stop.append(tokens_with_stop)
        processed_texts_no_stop.append(tokens_no_stop)

    return processed_texts_no_stop, processed_texts_with_stop


print(f'Processing {len(reddit_data)} texts...')
processed_no_stop, processed_with_stop = preprocess_texts(reddit_data['post'])
reddit_data['processed_tokens_no_stop'] = processed_no_stop
reddit_data['processed_tokens_with_stop'] = processed_with_stop
# Transform empty lists to None (or pd.NA) before the dropna operation
reddit_data['processed_tokens_no_stop'] = [None if x == [] else x for x in reddit_data['processed_tokens_no_stop']]
reddit_data['processed_tokens_with_stop'] = [None if x == [] else x for x in reddit_data['processed_tokens_with_stop']]

# Now, you can safely drop rows where the token lists are None
reddit_data.dropna(subset=['processed_tokens_no_stop', 'processed_tokens_with_stop'], inplace=True)

# Continue with the rest of your code
print(reddit_data.head())


reddit_data.to_csv('./datasets/reddit/processedReddit.csv', index=False)
