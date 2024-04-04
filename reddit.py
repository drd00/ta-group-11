import liwc
import pandas as pd
from textblob import TextBlob
from nltk.tokenize import word_tokenize

parse, category_names = liwc.load_token_parser('LIWC2015_Dictionary.dic')
reddit_data = pd.read_csv('./datasets/reddit/processedReddit.csv')


def analyze_tokens_liwc(tokens_list):
    liwc_counts = {category:0 for category in category_names}
    for tokens in tokens_list:
        for token in tokens:
            categories = parse(token)
            for category in categories:
                liwc_counts[category] += 1
    return liwc_counts

def tokenize_text(text):
    return word_tokenize(text)

def analyze_text_liwc(text):
    tokens = tokenize_text(text)
    liwc_counts = {category:0 for category in category_names}
    for token in tokens:
        categories = parse(token)
        for category in categories:
            liwc_counts[category] += 1
    return liwc_counts


reddit_data['liwc_analysis_post'] = reddit_data['post'].apply(analyze_text_liwc)
print("Post, results:", reddit_data['liwc_analysis_post'])
reddit_data['liwc_analysis_tokens_with_stop'] = reddit_data['processed_tokens_with_stop'].apply(analyze_tokens_liwc)
print("Processed with stopwords, results:", reddit_data['liwc_analysis_tokens_with_stop'])
reddit_data['liwc_analysis_tokens_no_stop'] = reddit_data['processed_tokens_no_stop'].apply(analyze_tokens_liwc)
print("Processed without stopwords, results:", reddit_data['liwc_analysis_tokens_no_stop'])

print(reddit_data.head())

reddit_data.to_csv('./datasets/reddit/reddit_result.csv', index=False)
