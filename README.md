# Wikipedia-Article-Scraper
A full Python package that allows users to search for a Wiki article, scrape it and have features for text analytics. <br>
Please feel free to download and use it (wikiscrape.py)!!!

## wikiscrape Package by Koh Jia Xuan
### This Python code can be used to search for a Wikipedia Article and do text analytics on it
<br>
To save a wikiscrape object, simply type: <br>
<b> import wikiscrape </b><br>
<b> var = wikiscrape.wiki('Search Article') </b> <br> <br>
e.g. paris = wikiscrape.wiki('PArIs','Yes','french','Yes') means to search for the article Paris, auto format to proper case (Yes for 2nd argument, default Yes), search for French wikipedia (french for 3rd argument, default No) and apply nltk stoplist for french (Yes for 4th argument, default No) <br>

### Full capabilities of wikiscrape package include: <br>
1. Able to search in multiple languages <br>
2. Give suggestions on search terms if search is ambiguous <br>
3. Gives a short summary (2 paragraphs) of the article if it is retrieved successfully <br>
4. Retrieve full text or exact number of paragraphs in string output for data pipeline <br>
5. var.HELP() for the full list of functions available <br>
6. Basic error handling, including checking data type of arguments and reverting to defaults if errorneous args are given <br>

### Text Analytics capabilities include: <br>
1. A frequency counter on the most common words in the Wikipedia article (after omitting common English words, or stoplist from NLTK for foreign languages). Can also find the Nth % of most common words, where 0 =< N =< 100. <br>
2. A graph plot of the most common words in the Wikipedia article <br>
3. A graph plot on the most frequent Years mentioned in the article, to understand the Years of interest of the article <br>
4. A summary on the total number of words and total number of unique words after implementing the stoplist of common words. <br>

#### Libraries used: requests, bs4, collections, matplotlib, re, os, nltk

#### Updates: <br>
1. 26 May 2019 - Added plotyear() function to plot the most frequent years mentioned
2. 9 June 2019 - Added markdown for explaination and added comments in the code for understanding <br>
3. For any questions or suggestions, please contact me at my Github account - https://github.com/kohjiaxuan/ <br>
