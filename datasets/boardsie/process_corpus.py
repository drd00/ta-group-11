import pandas as pd
import spacy
import re

# If you haven't already, run python3 -m spacy download en_core_web_sm
'''
    en_core_web_sm automatically performs 
    tokenisation and lemmatisation, among other things such as 
    Part-of-Speech (POS) tagging, Sentence Boundary Detection (SBD), ...
'''
nlp = spacy.load("en_core_web_sm")
df = pd.read_csv('boards_ie_politics.csv')

df['post'] = df['post'].astype(str) # ensure string type for post col

# remove URLs using regex
df['post'] = df['post'].apply(lambda post_text: re.sub(r'https?://\S+|www\.\S+', '', post_text))

def count_tokens_pipe(texts):
    # nlp.pipe improves efficiency over nlp(text) individually for each textual entry in the corpus
    token_counts = [len(doc) for doc in nlp.pipe(texts)]    # count the number of tokens for each entry

    return token_counts

df['token_count'] = count_tokens_pipe(df['post'])
print(df.head())

# get the mean token count
print(df['token_count'].mean())
