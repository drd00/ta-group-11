import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import scikit_posthocs as sp

plot_dist = False
plot_desc = True

# Load Boards.ie data
boardsie = pd.read_csv('./datasets/boardsie/boards_ie_politics_processed.csv')

# Load 4chan data
chan = pd.read_csv('./datasets/4chan/4chan_analysis.csv')

# Load Reddit data
reddit = pd.read_csv('./datasets/reddit/reddit_result_new.csv')

if plot_dist:
    print('Boards.ie')
    plt.figure(figsize=(6, 6))
    stats.probplot(boardsie['collective_focus'], dist='norm', plot=plt)
    plt.title('Q-Q plot: collective_focus, Boards.ie')
    plt.show()

    plt.figure(figsize=(6, 6))
    stats.probplot(boardsie['normalised_politeness'], dist='norm', plot=plt)
    plt.title('Q-Q plot: normalised_politeness, Boards.ie')
    plt.show()

    plt.figure(figure=(6, 6))
    stats.probplot(boardsie['raw_politeness'], dist='norm', plot=plt)
    plt.title('Q-Q plot: raw_politeness, Boards.ie')
    plt.show()

    sentiment_counts = boardsie['sentiment'].value_counts()
    sentiment_counts.plot(kind='bar', color=['red', 'blue'])
    plt.title('Sentiment distribution, Boards.ie')
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.xticks(rotation=0)
    plt.show()


    print('4chan')
    plt.figure(figsize=(6, 6))
    stats.probplot(chan['collective_focus'], dist='norm', plot=plt)
    plt.title('Q-Q plot: collective_focus, 4chan')
    plt.show()

    plt.figure(figsize=(6, 6))
    stats.probplot(chan['normalised_politeness'], dist='norm', plot=plt)
    plt.title('Q-Q plot: normalised_politeness, 4chan')
    plt.show()

    plt.figure(figsize=(6, 6))
    stats.probplot(chan['raw_politeness'], dist='norm', plot=plt)
    plt.title('Q-Q plot: raw_politeness, 4chan')
    plt.show()

    sentiment_counts = chan['sentiment'].value_counts()
    sentiment_counts.plot(kind='bar', color=['red', 'blue'])
    plt.title('Sentiment distribution, 4chan')
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.xticks(rotation=0)
    plt.show()


    # Reddit
    print('Reddit')
    plt.figure(figsize=(6, 6))
    stats.probplot(reddit['collective_focus'], dist='norm', plot=plt)
    plt.title('Q-Q plot: collective_focus, Reddit')
    plt.show()

    plt.figure(figsize=(6, 6))
    stats.probplot(reddit['normalised_politeness'], dist='norm', plot=plt)
    plt.title('Q-Q plot: normalised_politeness, Reddit')
    plt.show()

    plt.figure(figsize=(6, 6))
    stats.probplot(reddit['raw_politeness'], dist='norm', plot=plt)
    plt.title('Q-Q plot: raw_politeness, Reddit')
    plt.show()

    sentiment_counts = reddit['sentiment'].value_counts()
    sentiment_counts.plot(kind='bar', color=['red', 'blue'])
    plt.title('Sentiment distribution, Reddit')
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.xticks(rotation=0)
    plt.show()


# Calculate basic descriptive statistics for each dataset
print('Boards.ie basic descriptive stats')
boardsie_desc = boardsie.describe()
print(boardsie_desc)
boardsie_desc.to_csv('./results/boardsie_descriptive_stats.csv')

print('4chan basic descriptive stats')
chan_desc = chan.describe()
print(chan_desc)
chan_desc.to_csv('./results/chan_descriptive_stats.csv')

print('Reddit basic descriptive stats')
reddit_desc = reddit.describe()
print(reddit_desc)
reddit_desc.to_csv('./results/reddit_descriptive_stats.csv')

# Plot means
if plot_desc:
    print('Mean comparison')
    plt.figure(figsize=(6, 6))
    plt.bar(['Boards.ie', '4chan', 'Reddit'], [boardsie['collective_focus'].mean(), chan['collective_focus'].mean(), reddit['collective_focus'].mean()])
    plt.title('Mean collective_focus')
    plt.show()

    plt.figure(figsize=(6, 6))
    plt.bar(['Boards.ie', '4chan', 'Reddit'], [boardsie['normalised_politeness'].mean(), chan['normalised_politeness'].mean(), reddit['normalised_politeness'].mean()])
    plt.title('Mean normalised_politeness')
    plt.show()

    plt.figure(figsize=(6, 6))
    plt.bar(['Boards.ie', '4chan', 'Reddit'], [boardsie['raw_politeness'].mean(), chan['raw_politeness'].mean(), reddit['raw_politeness'].mean()])
    plt.title('Mean raw_politeness')
    plt.show()


    print('Mean sentiment')
    boardsie_sentiment_counts = boardsie['sentiment'].value_counts()
    plt.figure(figsize=(6, 6))
    plt.bar(boardsie_sentiment_counts.index, boardsie_sentiment_counts.values)
    plt.title('Sentiment distribution, Boards.ie')
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.xticks(rotation=0)
    plt.show()

    chan_sentiment_counts = chan['sentiment'].value_counts()
    plt.figure(figsize=(6, 6))
    plt.bar(chan_sentiment_counts.index, chan_sentiment_counts.values)
    plt.title('Sentiment distribution, 4chan')
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.xticks(rotation=0)
    plt.show()

    reddit_sentiment_counts = reddit['sentiment'].value_counts()
    plt.figure(figsize=(6, 6))
    plt.bar(reddit_sentiment_counts.index, reddit_sentiment_counts.values)
    plt.title('Sentiment distribution, Reddit')
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.xticks(rotation=0)
    plt.show()


# Kruskal-Wallis H
print('Kruskal-Wallis H')
print('collective_focus')
print(stats.kruskal(boardsie['collective_focus'], chan['collective_focus'], reddit['collective_focus']))
print('normalised_politeness')
print(stats.kruskal(boardsie['normalised_politeness'], chan['normalised_politeness'], reddit['normalised_politeness']))
print('raw_politeness')
print(stats.kruskal(boardsie['raw_politeness'], chan['raw_politeness'], reddit['raw_politeness']))
print('sentiment')
print(stats.kruskal(boardsie['sentiment'], chan['sentiment'], reddit['sentiment']))


# Dunn's post-hoc w/ Bonferroni correction
print("Dunn's post-hoc")
print('collective_focus')
print(sp.posthoc_dunn([boardsie['collective_focus'], chan['collective_focus'], reddit['collective_focus']], p_adjust='bonferroni'))
print('normalised_politeness')
print(sp.posthoc_dunn([boardsie['normalised_politeness'], chan['normalised_politeness'], reddit['normalised_politeness']], p_adjust='bonferroni'))
print('raw_politeness')
print(sp.posthoc_dunn([boardsie['raw_politeness'], chan['raw_politeness'], reddit['raw_politeness']], p_adjust='bonferroni'))
print('sentiment')
print(sp.posthoc_dunn([boardsie['sentiment'], chan['sentiment'], reddit['sentiment']], p_adjust='bonferroni'))

# Save each post-hoc test result to a CSV
cf_posthoc = sp.posthoc_dunn([boardsie['collective_focus'], chan['collective_focus'], reddit['collective_focus']], p_adjust='bonferroni')
cf_posthoc.to_csv('./results/collective_focus_posthoc.csv')

np_posthoc = sp.posthoc_dunn([boardsie['normalised_politeness'], chan['normalised_politeness'], reddit['normalised_politeness']], p_adjust='bonferroni')
np_posthoc.to_csv('./results/normalised_politeness_posthoc.csv')

rp_posthoc = sp.posthoc_dunn([boardsie['raw_politeness'], chan['raw_politeness'], reddit['raw_politeness']], p_adjust='bonferroni')
rp_posthoc.to_csv('./results/raw_politeness_posthoc.csv')

sentiment_posthoc = sp.posthoc_dunn([boardsie['sentiment'], chan['sentiment'], reddit['sentiment']], p_adjust='bonferroni')
sentiment_posthoc.to_csv('./results/sentiment_posthoc.csv')