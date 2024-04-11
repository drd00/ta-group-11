import pandas as pd
import spacy
import re
import liwc
import ftfy
from transformers import pipeline, AutoTokenizer 

parse, category_names = liwc.load_token_parser('LIWC2015_Dictionary.dic')
sentiment_pipeline = pipeline("sentiment-analysis")
tokenizer = AutoTokenizer.from_pretrained('distilbert-base-uncased')

# If you haven't already, run python3 -m spacy download en_core_web_sm
'''
    en_core_web_sm automatically performs 
    tokenisation and lemmatisation, among other things such as 
    Part-of-Speech (POS) tagging, Sentence Boundary Detection (SBD), ...
'''
nlp = spacy.load("en_core_web_sm", disable=["parser", "ner"])
df = pd.read_csv('boards_ie_politics.csv')

df['post'] = df['post'].astype(str) # ensure string type for post col

# remove URLs using regex
print("Link removal.")
df['post'] = df['post'].apply(lambda post_text: re.sub(r'https?://\S+|www\.\S+', '', post_text))
print("Comma and semicolon removal.")
df['post'] = df['post'].str.replace(',', ' ')
print("FTFY.")
df['post'] = df['post'].apply(ftfy.fix_text)    # fix encoding errors, etc.

sentiment_pipeline = pipeline("sentiment-analysis")

def analysis(df):
    new_df = df.copy()
    print("Running spaCy processing pipeline.")

    # Remove where the post is empty
    new_df = new_df[new_df['post'].str.strip() != '']

    # spaCy NLP processing.
    docs = list(nlp.pipe(new_df['post'], n_process=-1))

    friendly_words = set()
    with open('friendly_words.txt', 'r') as f:
        for line in f:
            friendly_words.add(line.lower().strip())


    def sentiment_analysis(text, max_length=512):
        inputs = tokenizer.encode(text, truncation=True, max_length=max_length, return_tensors='pt')

        truncated_text = tokenizer.decode(inputs[0], skip_special_tokens=True)

        result = sentiment_pipeline(truncated_text)[0]
        return result['label']

    def politeness_analysis(doc):
        # unigrams
        politeness = sum(token.text.lower() in friendly_words for token in doc)
        # bigrams
        politeness += sum(get_bigrams(doc).count(bigram) for bigram in friendly_words)

        return politeness

    # get bigrams
    def get_bigrams(doc):
        return [doc[i].text.lower() + " " + doc[i + 1].text.lower() for i in range(len(doc) - 1)]
    

    def liwc_focus_ratio_analysis(doc):
        i_count = 0
        we_count = 0
        for token in doc:
            categories = list(parse(token.text.lower()))
            if 'ppron' in categories:
                if token.text.lower() == 'i':
                    i_count += 1
                elif token.text.lower() == 'we':
                    we_count += 1
        
        total = i_count + we_count
        if total == 0:
            return 0
        
        collective_focus = we_count / total
        return collective_focus

    print("LIWC focus ratio analysis.")
    collective_focus_scores = [liwc_focus_ratio_analysis(doc) for doc in docs]
    new_df['collective_focus'] = collective_focus_scores
    print("Complete.")

    print("Politeness analysis.")
    politeness_scores_raw = [politeness_analysis(doc) for doc in docs]
    politeness_scores_normalised = [score / len(doc) for score, doc in zip(politeness_scores_raw, docs)]
    new_df['normalised_politeness'] = politeness_scores_normalised
    new_df['raw_politeness'] = politeness_scores_raw
    print("Complete.")
    print("Sentiment analysis.")

    new_df['sentiment'] = new_df['post'].apply(sentiment_analysis)
    print("Complete.")
    return new_df

output_df = analysis(df)
print("To CSV...")
output_df.to_csv('boards_ie_politics_processed.csv', index=False)
