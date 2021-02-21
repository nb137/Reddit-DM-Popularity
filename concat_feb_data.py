# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 11:07:45 2021

@author: nb137

we grabbed the top posts of the year in January, now let's grab more posts and append them so we have
almost two months of data after the start of the year

"""

import praw
import pandas as pd


from api_help import top_year

title, posted_epoch, num_com, vote = [],[],[],[]
for post in top_year:
    title.append(post.title)
    posted_epoch.append(post.created_utc)
    num_com.append(post.num_comments)
    vote.append(post.score)

df = pd.DataFrame({'title':title,'epoch':posted_epoch, 'num_comments':num_com,'score':vote})
df['created'] = pd.to_datetime(df['epoch'],unit='s', utc=True).dt.tz_convert('US/Pacific')

old_df = pd.read_pickle('dm_top_yearly_20210126.pkl')

comb = pd.concat([df,old_df]).drop_duplicates(subset='title')   # 63 posts added this month

pd.to_pickle(comb,'dm_top_yearly_20210221.pkl')
