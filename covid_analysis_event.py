#!/usr/bin/env python
# coding: utf-8

# # COVID-19 Statistical Worksheet

# <U>Notes if you are using Jupyter Notebook</U>:  to call <B>exit()</B> from a notebook, please use <B>sys.exit()</B> (requires <B>import sys</B>); if a strange error occurs, it may be because Jupyter retains variables from all executed cells.  To reset the notebook's variables, click 'Restart Kernel' (the circular arrow) -- this will not undo any text changes.  

# <B>Please do as many of these tasks as you can.</B>  I don't know whether these tasks will be overly time consuming, so please spend a minimum of 2-3 hours and if you have not completed all credit questions after that time and are unable to continue due to time constraints, simply let me know you were not able to finish and any notes you have about the problems.  Thank you!  

# <B>please note</B> the usual caveats:
# <UL>
#     <LI>Hints and discussion are in the <B>Discussion Document</B> for this session.</LI>
#     <LI>Some tasks may require the use of <B>new features</B>.  These will be mentioned in the question and discussed in more depth in the Discussion.</LI>
#     <LI><B>My answers</B> and results <B>may not always be the best</B>, or even correct!  I am also a student of this library, so there may be better or possibly even more accurate answers than the ones I supply.  <U>If you find a discrepancy between your answer and mine, but yours looks correct</U>, the proper response is to investigate by cross-checking, not to try to fit your answer to my results!  Let me know if you see differences and we'll have a look.  </LI>
# </UL>
# 

# ### 1: import the data
# <UL>
#     <LI>Import the data file <B>covid_event.csv</B> from this week's files.</LI>
#     <LI>Set the date column as the index, as some of the charting and grouping will be done with the date as a reference.</LI>
#     <LI>Once it has been set to the index, set the type of the index to <B>datetime64[ns]</B></LI>
# (It is also possible for the index and data type to be set in the <B>.read_csv()</B> function when you first ingest the data.)
#     <LI>Check the index's <B>dtype</B> to confirm that it has changed.</LI>
# </UL>
# 

# In[1]:


import pandas as pd

df = pd.read_csv('covid_event.csv', index_col='date')
df.index = df.index.astype('datetime64[ns]')
print(df.index.dtype)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 20)
print(df)


# ### 2: explore the DataFrame
# 
# Once imported, make sure to check on the import by reviewing your DataFrame's first few rows, its structure and size, with all of the following tools (these are not required for your solution, but try each one of them to get a sense of it):
# <B><UL>
#     <LI>len()</LI>
#     <LI>.head() and .tail()</LI>
#     <LI>.columns</LI>
#     <LI>.dtypes</LI>
#     <LI>.describe()</LI>
#     </UL></B></LI>
#     <LI><U>You may also need</U> to see more of the DataFrame than Notebook displays (default maximum of 10 rows).  You can modify the pandas defaults thusly:
# 
# <PRE>
# pd.set_option('display.max_rows', 500)
# pd.set_option('display.max_columns', 20)
#         </PRE></LI>
# 

# In[2]:


print(f'{len(df)} rows'); print()
print('first 5 lines:')
print(df.head()); print()
print('last 5 lines:')  
print(df.tail()); print()
print('columns:')
print(df.columns); print()
print('column dtypes:')
print(df.dtypes); print()
print('cases.describe:')
print(df.describe())


# <U>Expected Output</U>:<br>
# <PRE>424611 rows
# 
# first 5 lines:
#                county       state     fips  cases  deaths                  new
# date                                                                          
# 2020-01-21  Snohomish  Washington  53061.0      1       0  SnohomishWashington
# 2020-01-22  Snohomish  Washington  53061.0      0       0  SnohomishWashington
# 2020-01-23  Snohomish  Washington  53061.0      0       0  SnohomishWashington
# 2020-01-24       Cook    Illinois  17031.0      1       0         CookIllinois
# 2020-01-24  Snohomish  Washington  53061.0      0       0  SnohomishWashington
# 
# last 5 lines:
#                 county    state     fips  cases  deaths                new
# date                                                                      
# 2020-08-11  Sweetwater  Wyoming  56037.0      7       0  SweetwaterWyoming
# 2020-08-11       Teton  Wyoming  56039.0      2       0       TetonWyoming
# 2020-08-11       Uinta  Wyoming  56041.0      2       1       UintaWyoming
# 2020-08-11    Washakie  Wyoming  56043.0      2       0    WashakieWyoming
# 2020-08-11      Weston  Wyoming  56045.0     -1       0      WestonWyoming
# 
# columns:
# Index(['county', 'state', 'fips', 'cases', 'deaths', 'new'], dtype='object')
# 
# column dtypes:
# county     object
# state      object
# fips      float64
# cases       int64
# deaths      int64
# new        object
# dtype: object
# 
# cases.describe:
#                 fips          cases         deaths
# count  420389.000000  424611.000000  424611.000000
# mean    31024.987469      12.142074       0.389493
# std     16212.075849      83.494348       6.264726
# min      1001.000000   -1742.000000    -512.000000
# 25%     18147.000000       0.000000       0.000000
# 50%     29165.000000       1.000000       0.000000
# 75%     46073.000000       5.000000       0.000000
# max     78030.000000    8021.000000    1221.000000

# ### 3: count of unique states represented in the data
# Please show a count of unique states in the data.  I found <B>55</B> unique areas in the 'state' column.
# 
# (<U>Hint</U>:  the <B>.unique()</B> method discards duplicates.)

# In[4]:


print(len(df.state.unique()))


# <U>Expected Output</U>:<br>
# <PRE>55</PRE>

# ### 4. Show those 'states' not in a 50-state list.
# If there are <B>55</B> unique names in the <B>state</B> column, what are the 5 non-state names?  
# <UL>
#     <LI>Read into a DataFrame the reference file <B>state_name_abbrev.csv</B> to <I>programmatically</I> identify those names that are not part of the 50 state list.</LI>
#     <LI>Use the column of state names to identify which statements in your file are not found in the 50 state list.</LI>
#     <LI>This should be possible in one or two statements; it should not be done with looping.  (<U>Hint</U>:  consider the <B>.isin()</B> membership test in a conditional slice, and the <B>.unique()</B> method of the <B>Series</B> type)</LI>
# </UL>

# In[5]:


dfstateref = pd.read_csv('state_name_abbrev.csv')

unique = df.state.unique()
dfunique = pd.DataFrame(unique)
dfunique.columns = ['unique_state']

non_state_names = dfunique.loc[~dfunique['unique_state'].isin(dfstateref['name'])]
print(non_state_names)


# <U>Expected Result</U> will show the following states, but may come as an array, Series or set -- the below is not meant to represent a specific output:<br>
# <PRE>District of Columbia
# Puerto Rico
# Virgin Islands
# Guam
# Northern Mariana Islands</PRE>

# ### 5:  count of unique counties represented in the data
# Find a unique count of counties in the data set.  Since some county names are not unique among states, a unique count of counties will look for <B>state</B> and <B>county</B> in combination.  I found <B>3250</B> unique state + county combinations.  
# 
# <U>Hint</U>:  a groupby object has an <B>.ngroups</B> attribute which returns the number of groups.  

# In[15]:


dfgb = df.groupby(['state', 'county']).count()
print(len(dfgb))


# <U>Expected Output</U>:<br>
# <PRE>3250</PRE>

# ### 6: cases by state, sorted
# Please sum the number of cases grouped by state.  Then, use <B>.sort_values()</B> with the parameter argument <B>ascending=False</B> to sort the states by cases, from highest to lowest.

# In[19]:


dfgb2 = df.groupby('state').sum().sort_values('cases', ascending=False)['cases']
print(dfgb2)


# <U>Expected Output</U>:<br>
# <PRE>state
# California                  586078
# Florida                     542784
# Texas                       522626
# New York                    426713
# Georgia                     205920
# Illinois                    198975
# Arizona                     188780
# New Jersey                  187328
# North Carolina              138124
# Louisiana                   133243
# Pennsylvania                125079
# Tennessee                   122089
# Massachusetts               121707
# Alabama                     103851
# Ohio                        102827
# South Carolina              102130
# Virginia                    101924
# Michigan                     98361
# Maryland                     97403
# Indiana                      77627
# Mississippi                  68479
# Washington                   66620
# Wisconsin                    66146
# Missouri                     61932
# Minnesota                    61880
# Nevada                       57608
# Colorado                     51578
# Connecticut                  50684
# Arkansas                     50411
# Iowa                         49521
# Utah                         44836
# Oklahoma                     44726
# Kentucky                     37503
# Kansas                       32174
# Nebraska                     29030
# Idaho                        25961
# Puerto Rico                  23403
# New Mexico                   22650
# Oregon                       21782
# Rhode Island                 20053
# Delaware                     15699
# District of Columbia         12896
# South Dakota                  9713
# North Dakota                  7889
# West Virginia                 7877
# New Hampshire                 6863
# Montana                       5125
# Alaska                        4595
# Maine                         4052
# Hawaii                        3733
# Wyoming                       3074
# Vermont                       1472
# Guam                          1403
# Virgin Islands                 639
# Northern Mariana Islands        82
# Name: cases, dtype: int64</PRE>

# ### 7: bar chart:  cases by state, 10 highest
# Working from the data built above, show the first 10 states and number of cases in a bar chart. 
# 
# <U>Note</U> that a semicolon placed at the end of any <B>.plot()</B> statements will hide the <B>&lt;AxesSubplot&gt;</B> object from display.

# In[20]:


import matplotlib.pyplot as plt

dfgb3 = df.groupby('state').sum().sort_values('cases', ascending=False)['cases'][0:10]
ax = dfgb3.plot(kind='bar', rot=45)


# <U>Expected Output</U>:<br>
# <IMG SRC="images/hw7.png" align="left">

# ### 8: show cases by county for a given state.
# Take user input for a state name (or you can hard-code the state name).  Show the cases by county within the state, sorted from highest to lowest.

# In[21]:


x = input('please enter a state name: ')
df4 = df.loc[df['state'] == x]
dfgb4 = df4.groupby('county').sum().sort_values('cases', ascending=False)['cases']
print(f'total {len(dfgb4)}')
print(dfgb4)


# <U>Expected Output</U>:<BR>
# <PRE>please enter a state name: Florida
# total 68
# county
# Miami-Dade      135129
# Broward          63605
# Palm Beach       37639
# Hillsborough     32996
# Orange           32041
# Duval            23741
# Pinellas         18103
# Lee              16717
# Polk             14645
# Collier          10487
# Osceola           9858
# Escambia          9807
# Manatee           9395
# Volusia           8040
# Seminole          7219
# Pasco             7172
# Marion            6668
# Sarasota          6314
# Brevard           6190
# St. Lucie         5920
# Lake              5229
# Leon              5115
# Bay               4523
# Alachua           4246
# Santa Rosa        4013
# Martin            3852
# St. Johns         3738
# Okaloosa          3586
# Clay              3327
# Columbia          2917
# Indian River      2555
# Charlotte         2281
# Hernando          2069
# Jackson           1936
# Gadsden           1927
# Hendry            1805
# Citrus            1594
# Monroe            1548
# Putnam            1539
# Suwannee          1507
# Highlands         1474
# Walton            1428
# DeSoto            1377
# Sumter            1344
# Nassau            1253
# Flagler           1095
# Okeechobee        1077
# Hardee             986
# Taylor             981
# Baker              964
# Washington         877
# Wakulla            726
# Unknown            721
# Madison            710
# Levy               698
# Gulf               685
# Hamilton           623
# Dixie              562
# Bradford           519
# Holmes             509
# Calhoun            481
# Jefferson          462
# Union              435
# Franklin           433
# Liberty            407
# Glades             406
# Gilchrist          369
# Lafayette          189
# Name: cases, dtype: int64</PRE>

# ### 9: bar chart:  cases by county for a given state, 10 highest
# Working from the above data, show the first 10 counties in a bar chart.

# In[22]:


x = input('please enter a state name: ')
df5 = df.loc[df['state'] == x]
dfgb5 = df5.groupby('county').sum().sort_values('cases', ascending=False)['cases'][0:10]
print(f"total {len(df5.groupby('county').sum().sort_values('cases', ascending=False)['cases'])}")
ax = dfgb5.plot(kind='bar', rot=45)


# <U>Expected Output</U> (image may be cut off at bottom):<BR>
# <PRE>please enter a state name: New York
# total 59</PRE>
# <IMG SRC="images/hw9.png" align="left">

# ### 10: pie chart showing all 50 states and share of cases
# Show the number of cases by state in a pie chart.
# <UL>
#     <LI>The plot() arguments I used were <B>kind='pie'</B>, <B>figsize=(5,5)</B>,  <B>labels=None</B> </LI>
# <LI>I set a legend by using the <B>plt.legend()</B> method with <B>loc=(.95,.35)</B> (for positioning) and <B>labels=</B> equal to the first 10 names in the index.</LI>
#     </UL>

# In[23]:


dfgb6 = df.groupby('state').sum().sort_values('cases', ascending=False)['cases']
ax = dfgb6.plot.pie(y='cases', figsize=(5, 5), labels=None).legend(loc=(.95,.35), labels=dfgb6.index[0:10])


# <U>Expected Output</U>:<BR>
# <IMG SRC="images/hw10.png" align="left">

# ### 11: pie chart showing top 10 states and share of cases among them
# perform the same aggregation and charting as above, but chart a slice of just the first 10 states

# In[24]:


dfgb7 = df.groupby('state').sum().sort_values('cases', ascending=False)['cases'][0:10]
ax = dfgb7.plot.pie(y='cases', figsize=(5, 5), labels=None).legend(loc=(.95,.35), labels=dfgb7.index)


# <U>Expected Output</U>:<BR>
# <IMG SRC="images/hw11.png" align="left">

# ### 12: cases over time for a selected state
# Take <B>input()</B> for a state name (or hard code a state name if you prefer), then build a line chart showing the increase in number of cases over time for that state.  
# 
# The data shows new cases for each day, so a line chart of just new cases will not show the increase.  In order to calculate the increase, after grouping cases by date in one state, use <B>.cumsum()</B> to calculate the cumulative sum.  Here is an example of <B>.cumsum()</B>:
# <PRE>
# df = pd.DataFrame({'a': [1, 2, 3], 'b': [9, 30, 200]})
# df['c'] = df.b.cumsum()
# print(df)
#    a    b    c        # 'c' column adds up 'b' column values
# 0  1    9    9        #   9 =  0 +   9
# 1  2   30   39        #  39 =  9 +  30
# 2  3  200  239        # 239 = 39 + 200
# </PRE>

# In[25]:


x = input('please enter a state name: ')
df8 = df.loc[df['state'] == x]
dfgb8 = df8.groupby('date').sum()
dfgb8['cum_cases'] = dfgb8.cases.cumsum()
df9 = dfgb8.loc[:, ['cum_cases']]
ax = df9.plot(title=x, style='b.', rot=45)


# <U>Expected Output</U>:<BR>
# <PRE>please enter a state name: New York</PRE>
# <IMG SRC="images/hw12.png" align="left">

# ### 13: (extra credit) cases over time:  selected states comparison
# Repeat the above exercise, but this time allow the user to input any number of states; build a line chart comparing the rates of new cases.  You can plot multiple lines from a DataFrame by calling <B>.plot()</B> on a DataFrame that has the columns you want to plot.  

# In[ ]:





# <U>Expected Output</U>:<BR>
# <PRE>please enter states separated by commas: New York, Florida</PRE>
# <IMG SRC="images/hw13.png" align="left">    

# ### 14: (extra credit) scatter plot showing cases by state population
# This chart shows the correlation of two factors:  the <B>y</B> (vertical) axis will show state population, and the <B>x</B> axis will show number of cases.  The placement of the dot within the 2D area correlates the two numers, which can visually indicate cases per capita  

# In[ ]:





# <U>Expected Output</U>:<BR>
# <IMG SRC="images/hw14.png" align="left">

# ### 15: (extra credit) bar chart showing daily increase in cases for a state
# Use <B>input()</B> for a state name.  You can use the <B>.shift()</B> method to compare count of a day's cases to the prior days, calculating the increase.  See discussion for more details.  

# In[ ]:





# <U>Expected Output</U>:<BR>
# <PRE>please enter a state name: New York</PRE>
# <IMG SRC="images/hw16.png" align="left">
