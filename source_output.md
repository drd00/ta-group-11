# Source Output of reddit_prework.py
```
          title  score      id        url comms_num  created       body  \
Total         0      0       0      18027         0        0       9995   
Percent     0.0    0.0     0.0  64.237608       0.0      0.0  35.616292   
Types    object  int64  object     object     int64  float64     object   

        timestamp  
Total           0  
Percent       0.0  
Types      object  
                                               title  score      id  \
0  A Right Wing Group in Texas Is Making up Fake ...    166  ov1ll3   
1  DOJ sues Texas over Gov. Abbott’s order for la...     85  ouwc9i   
2  From white evangelicals to QAnon believers, wh...     57  ouqkxi   
3  DeSantis says he’ll sign order allowing parent...    269  oun2lc   
4  Show on the road: In Utah, Florida Gov. Ron De...     31  ouipnz   

                                                 url  comms_num       created  \
0  https://www.vice.com/en/article/wx5bg5/blm-whi...         34  1.627710e+09   
1  https://www.kxan.com/news/texas-politics/doj-s...         17  1.627688e+09   
2  https://www.modbee.com/news/coronavirus/articl...         27  1.627671e+09   
3  https://www.orlandosentinel.com/politics/os-ne...        138  1.627660e+09   
4  https://www.tallahassee.com/story/news/politic...         28  1.627644e+09   

  body            timestamp        source_domain  
0  NaN  2021-07-31 08:35:47             vice.com  
1  NaN  2021-07-31 02:26:12             kxan.com  
2  NaN  2021-07-30 21:45:09           modbee.com  
3  NaN  2021-07-30 18:43:05  orlandosentinel.com  
4  NaN  2021-07-30 14:21:54      tallahassee.com  
        source_domain  count
0                  NA  18027
1         thehill.com    736
2             cnn.com    660
3  washingtonpost.com    516
4        politico.com    379
                                               title  score      id  \
0  A Right Wing Group in Texas Is Making up Fake ...    166  ov1ll3   
1  DOJ sues Texas over Gov. Abbotts order for law...     85  ouwc9i   
2  From white evangelicals to QAnon believers, wh...     57  ouqkxi   
3  DeSantis says hell sign order allowing parents...    269  oun2lc   
4  Show on the road: In Utah, Florida Gov. Ron De...     31  ouipnz   

                                                 url  comms_num       created  \
0  https://www.vice.com/en/article/wx5bg5/blm-whi...         34  1.627710e+09   
1  https://www.kxan.com/news/texas-politics/doj-s...         17  1.627688e+09   
2  https://www.modbee.com/news/coronavirus/articl...         27  1.627671e+09   
3  https://www.orlandosentinel.com/politics/os-ne...        138  1.627660e+09   
4  https://www.tallahassee.com/story/news/politic...         28  1.627644e+09   

  body            timestamp        source_domain  \
0       2021-07-31 08:35:47             vice.com   
1       2021-07-31 02:26:12             kxan.com   
2       2021-07-30 21:45:09           modbee.com   
3       2021-07-30 18:43:05  orlandosentinel.com   
4       2021-07-30 14:21:54      tallahassee.com   

                                                post  token_count  
0  A Right Wing Group in Texas Is Making up Fake ...           14  
1  DOJ sues Texas over Gov. Abbotts order for law...           16  
2  From white evangelicals to QAnon believers, wh...           16  
3  DeSantis says hell sign order allowing parents...           13  
4  Show on the road: In Utah, Florida Gov. Ron De...           18  
34.10016748031215
[nltk_data] Error loading stopwords: <urlopen error [Errno 8] nodename
[nltk_data]     nor servname provided, or not known>
Processing 28063 texts...
                                               title  score      id  \
0  A Right Wing Group in Texas Is Making up Fake ...    166  ov1ll3   
1  DOJ sues Texas over Gov. Abbotts order for law...     85  ouwc9i   
2  From white evangelicals to QAnon believers, wh...     57  ouqkxi   
3  DeSantis says hell sign order allowing parents...    269  oun2lc   
4  Show on the road: In Utah, Florida Gov. Ron De...     31  ouipnz   

                                                 url  comms_num       created  \
0  https://www.vice.com/en/article/wx5bg5/blm-whi...         34  1.627710e+09   
1  https://www.kxan.com/news/texas-politics/doj-s...         17  1.627688e+09   
2  https://www.modbee.com/news/coronavirus/articl...         27  1.627671e+09   
3  https://www.orlandosentinel.com/politics/os-ne...        138  1.627660e+09   
4  https://www.tallahassee.com/story/news/politic...         28  1.627644e+09   

  body            timestamp        source_domain  \
0       2021-07-31 08:35:47             vice.com   
1       2021-07-31 02:26:12             kxan.com   
2       2021-07-30 21:45:09           modbee.com   
3       2021-07-30 18:43:05  orlandosentinel.com   
4       2021-07-30 14:21:54      tallahassee.com   

                                                post  token_count  \
0  A Right Wing Group in Texas Is Making up Fake ...           14   
1  DOJ sues Texas over Gov. Abbotts order for law...           16   
2  From white evangelicals to QAnon believers, wh...           16   
3  DeSantis says hell sign order allowing parents...           13   
4  Show on the road: In Utah, Florida Gov. Ron De...           18   

                            processed_tokens_no_stop  \
0  [Right, Wing, Group, Texas, make, Fake, Black,...   
1  [DOJ, sue, Texas, Gov., Abbotts, order, law, e...   
2  [white, evangelical, QAnon, believer, likely, ...   
3  [DeSantis, say, hell, sign, order, allow, pare...   
4  [show, road, Utah, Florida, Gov., Ron, DeSanti...   

                          processed_tokens_with_stop  
0  [a, Right, Wing, Group, in, Texas, be, make, u...  
1  [DOJ, sue, Texas, over, Gov., Abbotts, order, ...  
2  [from, white, evangelical, to, QAnon, believer...  
3  [DeSantis, say, hell, sign, order, allow, pare...  
4  [show, on, the, road, in, Utah, Florida, Gov.,...  

Process finished with exit code 0

```

# Source Output of reddit.py
```
Post, results: 0        {'function': 2, 'pronoun': 0, 'ppron': 0, 'i':...
1        {'function': 5, 'pronoun': 0, 'ppron': 0, 'i':...
2        {'function': 3, 'pronoun': 1, 'ppron': 0, 'i':...
3        {'function': 1, 'pronoun': 0, 'ppron': 0, 'i':...
4        {'function': 3, 'pronoun': 0, 'ppron': 0, 'i':...
                               ...                        
27932    {'function': 4, 'pronoun': 1, 'ppron': 1, 'i':...
27933    {'function': 17, 'pronoun': 4, 'ppron': 1, 'i'...
27934    {'function': 19, 'pronoun': 2, 'ppron': 2, 'i'...
27935    {'function': 3, 'pronoun': 0, 'ppron': 0, 'i':...
27936    {'function': 12, 'pronoun': 0, 'ppron': 0, 'i'...
Name: liwc_analysis_post, Length: 27937, dtype: object
Processed with stopwords, results: 0        {'function': 15, 'pronoun': 7, 'ppron': 7, 'i'...
1        {'function': 8, 'pronoun': 5, 'ppron': 5, 'i':...
2        {'function': 10, 'pronoun': 7, 'ppron': 7, 'i'...
3        {'function': 10, 'pronoun': 3, 'ppron': 3, 'i'...
4        {'function': 18, 'pronoun': 8, 'ppron': 8, 'i'...
                               ...                        
27932    {'function': 7, 'pronoun': 1, 'ppron': 1, 'i':...
27933    {'function': 36, 'pronoun': 27, 'ppron': 27, '...
27934    {'function': 17, 'pronoun': 9, 'ppron': 9, 'i'...
27935    {'function': 4, 'pronoun': 2, 'ppron': 2, 'i':...
27936    {'function': 20, 'pronoun': 9, 'ppron': 9, 'i'...
Name: liwc_analysis_tokens_with_stop, Length: 27937, dtype: object
Processed without stopwords, results: 0        {'function': 12, 'pronoun': 5, 'ppron': 5, 'i'...
1        {'function': 7, 'pronoun': 4, 'ppron': 4, 'i':...
2        {'function': 10, 'pronoun': 7, 'ppron': 7, 'i'...
3        {'function': 10, 'pronoun': 3, 'ppron': 3, 'i'...
4        {'function': 14, 'pronoun': 6, 'ppron': 6, 'i'...
                               ...                        
27932    {'function': 5, 'pronoun': 1, 'ppron': 1, 'i':...
27933    {'function': 25, 'pronoun': 19, 'ppron': 19, '...
27934    {'function': 8, 'pronoun': 4, 'ppron': 4, 'i':...
27935    {'function': 3, 'pronoun': 1, 'ppron': 1, 'i':...
27936    {'function': 16, 'pronoun': 7, 'ppron': 7, 'i'...
Name: liwc_analysis_tokens_no_stop, Length: 27937, dtype: object
                                               title  ...  liwc_sentiment
0  A Right Wing Group in Texas Is Making up Fake ...  ...         Neutral
1  DOJ sues Texas over Gov. Abbotts order for law...  ...         Neutral
2  From white evangelicals to QAnon believers, wh...  ...         Neutral
3  DeSantis says hell sign order allowing parents...  ...        Negative
4  Show on the road: In Utah, Florida Gov. Ron De...  ...         Neutral

[5 rows x 17 columns]
Reddit Post Sentiment Counts:
liwc_sentiment
Neutral     14752
Negative     7234
Positive     5951
Name: count, dtype: int64,

Reddit Post Sentiment Percentage:
liwc_sentiment
Neutral     52.804524
Negative    25.893976
Positive    21.301500
Name: count, dtype: float64
Schumer say hope U.S. Senate vote bipartisan infrastructure plan week 's end Ajit Pai apparently mismanage $ 9 billion fundnew FCC boss start cleanup Starlink isp may give money Pai award long term option long time expire risky thus rewarding buy February legislature affect cook day possible lucky sure however one time event Pelosis speculation sure right place right time trade America absolute cesspool corruption degenerate politician even hide anymore America country solely exist allow rich pe
DeSantis say hell sign order allow parent ignore COVID-19 school mask mandate election integrity committee York County accuse voter intimidation Police Officers give Congress front row Seat Trauma politic opening day testimony Capitol 's defender try rescue January 6 Commission consume partisan rancor spawn Washington 's partisan game playing could mean defend Capitol face rioter never get answer White House defend Biden 's past remark virus CDC shift guidance reasoning watch fox news madden ext
Right Wing Group Texas make Fake Black Lives matter campaign DOJ sue Texas Gov. Abbotts order law enforcement pull vehicle migrant white evangelical QAnon believer likely refuse covid vaccine show road Utah Florida Gov. Ron DeSantis rail faucian dystopia Michigan Supreme Court limit use restraint juvenile Texas Senator use mlk word attack Critical Race Theory MLK III say Fathers work support Wisconsin GOP leader want another election probe Democrats press Biden extend eviction ban U.S. CDC recom

Process finished with exit code 0
```