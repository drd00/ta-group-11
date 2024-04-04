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
[nltk_data] Error loading stopwords: <urlopen error [SSL:
[nltk_data]     CERTIFICATE_VERIFY_FAILED] certificate verify failed:
[nltk_data]     unable to get local issuer certificate (_ssl.c:1000)>
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
0  [right, wing, group, texa, fake, black, live, ...   
1  [doj, sue, texa, gov., abbott, order, law, enf...   
2  [white, evangel, qanon, believ, like, refus, c...   
3  [desanti, hell, sign, order, allow, parent, ig...   
4  [road, utah, florida, gov., ron, desanti, rail...   

                          processed_tokens_with_stop  
0  [a, right, wing, group, in, texa, is, make, up...  
1  [doj, sue, texa, over, gov., abbott, order, fo...  
2  [from, white, evangel, to, qanon, believ, who,...  
3  [desanti, say, hell, sign, order, allow, paren...  
4  [show, on, the, road, in, utah, florida, gov.,...  

Process finished with exit code 0
```