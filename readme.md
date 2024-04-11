# CS7IS4 Text Analytics Group 11 Repository
This is where we will write code associated with the Text Analytics group project.

## General information
### Dependencies
Dependencies may be installed using `pip`: `pip install -r requirements.txt`.

### Approach outline
Use of `spaCy` for tokenisation, `pandas` for dataset processing and `scipy` for statistical analysis.

### Displaying statistics
From the root directory, run `python3 statistical_analysis.py`, ensuring that each dataset exists in `.csv` (comma-separated) in repository root.

# Data preprocessing
Preprocessing of data is consistent across datasets to ensure a valid statistical analysis. The following preprocessing steps have been carried out for each dataset:
1. **Link removal:** The group agreed that links represent non-textual data and could interfere with the analysis. For the textual analyses, links are hence removed from posts.
2. **FTFY:** This is a Python package often used for data-preprocessing, and it fixes encoding issues in text.
3. **Removal of empty posts**: In the data collection process, it may rarely occur that a post is obtained which is empty. This could be an artifact of the scraping process or inherent in the underlying data.


# Metrics
The following metrics are used in our analysis:
1. **Politeness / friendliness:** The metric used for politeness / friendliness is based on the occurrence of words associated with this, from the group's own word / sequence list. In the current analysis, only unigrams and bigrams are considered. Also, because longer texts increase the likelihood of politeness / friendliness markers appearing, this is balanced by using another column for normalised politeness / friendliness, which is this value divided by the total number of tokens in the document.
2. **Sentiment**: Sentiment is measured on a binary basis, either positive or negative. This is achieved using a BERT-based sentiment analysis tool in the `transformers` library. Specifically, the `distilbert/distilbert-base-uncased-finetuned-sst2-english` model is used. This model has a token limit of 512, which is not typically an issue, but some of the post entries in the corpora analysed exceed this. Hence, only the first `512` tokens of the input are considered in the classification.
3. **Collective-focus**: Collective focus metrics are gathered using LIWC 2015. This allows for the counting of various personal pronouns, and the collective-focus metric may be calculated by considering the (we_count / (i_count + we_count)) --- i.e., when speaking in the first-person, what proportion of the time is one talking about the collective we and what proportion of the time is one talking about the singular self.

# Statistical analysis
TODO: write this section.