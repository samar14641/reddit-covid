Note: Analysis and data collection done on 24-3-2020

Data files: 
1. data.json and data.csv: They contain the same information, except in different formats. These two files DO NOT contain any top level comments. They fields are left as empty lists.
2. data_comments_large.json and data_comments_large.csv: They contain the same information as data.json and data.csv for the top 400 threads, along with top level comments for these threads. 

Code files:
1. gatherData.py: Uses the praw package to get threads from Reddit, and creates the json and csv files. Default output doesn't retrieve top level comments. This can be changed by setting the 'commentsReqd' variable to True. Packages required:
    1. pandas
    2. praw
    3. dotenv
2. analysis.Rmd: R Markdown file to perform some text analysis. Libraries required:
    1. dplyr
    2. ggplot2
    3. ggraph
    4. igraph
    5. readr
    6. tidyr
    7. tidytext

Misc. files:
1. .env: env file that contains OAuth2 data for praw (see praw documentation for the same). Loaded in Python using the dotenv package.
2. Analysis on COVID-19 Reddit Threads: Knitted PDF of the Rmd file.

Further topic analysis ideas:
1. Popularity of certain keywords over time: We would expect to find more occurances of terms such as 'social distancing' and 'Italy' now, as opposed to in Jan 2020, whereas terms like 'Wuhan' might not be used as much now when compared to Jan and Feb 2020.
2. Correlation between thread popularity and the information source: Most threads on r/Coronavirus have an associated information source (present in the 'url' field). We can analyse the relationship between how popular a thread is (using upvotes, number of awards, whether it was on r/all or not, etc.) and the source of information. This may help determine whether a news source is trusted, and by extension, if it is seen as a source of fake news or not.