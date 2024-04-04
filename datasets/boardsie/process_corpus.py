import pandas as pd
import spacy
import re
import liwc
import ftfy

parse, category_names = liwc.load_token_parser('LIWC2015_Dictionary.dic')

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
print("FTFY.")
df['post'] = df['post'].apply(ftfy.fix_text)    # fix encoding errors, etc.

def analysis():
    print("Running spaCy processing pipeline.")
    docs = [doc for doc in nlp.pipe(df['post'])]

    def normalised_liwc_politeness_calculation(doc):
        # Get a normalised politeness score (accounting for the document length).
        politeness = 0
        for token in doc:
            categories = list(parse(token.text.lower()))
            if 'politeness' in categories:
                politeness += 1
        
        return politeness / len(doc) if len(doc) > 0 else 0

    def liwc_politeness_calculation(doc):
        politeness = 0
        for token in doc:
            categories = list(parse(token.text.lower()))
            if 'politeness' in categories:
                politeness += 1
        return politeness

    def liwc_analysis(doc):
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

    collective_focus_scores = [liwc_analysis(doc) for doc in docs]
    politeness_scores = [normalised_liwc_politeness_calculation(doc) for doc in docs]
    politeness_scores_raw = [liwc_politeness_calculation(doc) for doc in docs]
    df['collective_focus'] = collective_focus_scores
    df['normalised_politeness'] = politeness_scores
    df['politeness'] = politeness_scores_raw

analysis()
pd.set_option('display.max_columns', None)
print(df.head(20))
