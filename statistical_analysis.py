import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import scikit_posthocs as sp

plot = True

# Load Boards.ie data
boardsie = pd.read_csv('./datasets/boardsie/boards_ie_politics_processed.csv')

# Load 4chan data
chan = pd.read_csv('./datasets/4chan/4chan_analysis.csv')

if plot:
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


# Calculate basic descriptive statistics for each dataset
print('Boards.ie basic descriptive stats')
print(boardsie.describe())

print('4chan basic descriptive stats')
print(chan.describe())

# Kruskal-Wallis H
print('Kruskal-Wallis H')
# TODO: add reddit here too.
print('collective_focus')
print(stats.kruskal(boardsie['collective_focus'], chan['collective_focus']))
print('normalised_politeness')
print(stats.kruskal(boardsie['normalised_politeness'], chan['normalised_politeness']))
print('raw_politeness')
print(stats.kruskal(boardsie['raw_politeness'], chan['raw_politeness']))
print('sentiment')
print(stats.kruskal(boardsie['sentiment'], chan['sentiment']))


# Dunn's post-hoc w/ Bonferroni correction
print("Dunn's post-hoc")
print('collective_focus')
print(sp.posthoc_dunn([boardsie['collective_focus'], chan['collective_focus']], p_adjust='bonferroni'))
print('normalised_politeness')
print(sp.posthoc_dunn([boardsie['normalised_politeness'], chan['normalised_politeness']], p_adjust='bonferroni'))
print('raw_politeness')
print(sp.posthoc_dunn([boardsie['raw_politeness'], chan['raw_politeness']], p_adjust='bonferroni'))
print('sentiment')
print(sp.posthoc_dunn([boardsie['sentiment'], chan['sentiment']], p_adjust='bonferroni'))

