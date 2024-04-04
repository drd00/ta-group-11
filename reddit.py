import liwc
import pandas as pd
from matplotlib import pyplot as plt
from wordcloud import WordCloud
from nltk.tokenize import word_tokenize
import ast

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


def determine_liwc_sentiment(liwc_results):
    posemo_count = liwc_results.get('posemo', 0)
    negemo_count = liwc_results.get('negemo', 0)

    if posemo_count > negemo_count:
        return 'Positive'
    elif posemo_count < negemo_count:
        return 'Negative'
    else:
        return 'Neutral'


reddit_data['liwc_sentiment'] = reddit_data['liwc_analysis_post'].apply(determine_liwc_sentiment)

print(reddit_data.head())


def plot_sentiment(df, feature, title):
    counts = df[feature].value_counts()
    percent = counts / sum(counts) * 100

    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12, 5))

    counts.plot(kind='bar', ax=ax1, color='green')
    percent.plot(kind='bar', ax=ax2, color='blue')
    print(f'{title} Sentiment Counts:\n{counts},\n\n{title} Sentiment Percentage:\n{percent}')
    ax1.set_ylabel('Counts', size=12)
    ax2.set_ylabel('Percentage (%)', size=12)
    ax1.set_title(f'{title} Sentiment Counts')
    ax2.set_title(f'{title} Sentiment Percentage')
    plt.suptitle(f"Sentiment Analysis Based on {title}")
    plt.tight_layout()
    plt.show()


plot_sentiment(reddit_data, 'liwc_sentiment', 'Reddit Post')


def generate_sentiment_wordcloud(df, sentiment_column, tokens_column, sentiment):
    # 根据情感类别筛选文本
    filtered_texts = df.loc[df[sentiment_column] == sentiment, tokens_column]

    # 将字符串形式的分词列表转换回真正的列表
    filtered_texts = filtered_texts.apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)

    # 现在将分词列表转换为单一字符串
    text_str = ' '.join([' '.join(tokens) for tokens in filtered_texts if isinstance(tokens, list)])

    # 检查文本字符串
    print(text_str[:500])  # 打印前500个字符来检查

    # 生成词云
    wordcloud = WordCloud(background_color='white', width=800, height=600).generate(text_str)

    # 显示词云
    plt.figure(figsize=(10, 7))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(f'Prevalent Words in Texts ({sentiment} Sentiment)')
    plt.show()



# 调用函数生成正面情感的词云
generate_sentiment_wordcloud(reddit_data, 'liwc_sentiment', 'processed_tokens_no_stop', 'Positive')
# 调用函数生成负面情感的词云
generate_sentiment_wordcloud(reddit_data, 'liwc_sentiment', 'processed_tokens_no_stop', 'Negative')
# 调用函数生成中性情感的词云
generate_sentiment_wordcloud(reddit_data, 'liwc_sentiment', 'processed_tokens_no_stop', 'Neutral')


reddit_data.to_csv('./datasets/reddit/reddit_result.csv', index=False)
