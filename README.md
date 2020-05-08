# Wikipedia-Article-Scraper
A full Python package that allows users to search for a Wiki article, scrape it and have features for text analytics. <br>
Please feel free to download the script file for personal usage! <b>(wikiscrape.py)</b> <br>
![Linkedin Example](https://github.com/kohjiaxuan/Wikipedia-Article-Scraper/blob/master/Images/WikiScrape_Example.PNG)  <br><br>
Old Graph Plots: <br>
![Coldplay Wiki - Years Mentioned](https://github.com/kohjiaxuan/Wikipedia-Article-Scraper/blob/master/Images/coldplayyearcount2.jpg)  <br><br>
New Graph Plots:
![Coldplay Wiki - Years Mentioned NEW](https://github.com/kohjiaxuan/Wikipedia-Article-Scraper/blob/master/Images/ColdplayWordCount2.png)  <br><br>
New Graph of plotting the most popular words in a Wikipedia Article:
![Donald Trump Wiki - 40 Most Popular Words](https://github.com/kohjiaxuan/Wikipedia-Article-Scraper/blob/master/Donald_Trump_40words.png) <br><br>
![Armin van Buuren - 10 Most Popular Words](https://github.com/kohjiaxuan/Wikipedia-Article-Scraper/blob/master/Armin_top10words_25112019.png) <br><br>
## wikiscrape Package by KJX
### This Python code can be used to search for a Wikipedia Article and do text analytics on it
<br>
To save a wikiscrape object, simply type: <br>
<b> import wikiscrape </b><br>
<b> var = wikiscrape.wiki('Search Article') </b> <br> <br>
e.g. paris = wikiscrape.wiki('PArIs','Yes','french','Yes','Yes') means to search for the article Paris, auto format to proper case (Yes for 2nd argument, default Yes), search for French wikipedia (french for 3rd argument, default English), apply nltk stoplist for french (Yes for 4th argument, default No) and lemmatize the article using nltk (Yes for 5th argument, default No) <br>

### Full capabilities of wikiscrape package include: <br>
1. Able to search in multiple languages <br>
2. Give suggestions on search terms if search is ambiguous <br>
3. Gives a short summary (2 paragraphs) of the article if it is retrieved successfully <br>
4. Retrieve full text or exact number of paragraphs in string output for data pipeline <br>
5. var.HELP() for the full list of functions available <br>
6. Basic error handling, including checking data type of arguments and reverting to defaults if errorneous args are given <br>
7. Apply local stoplist by directly editing the dictionary, and also applying NLTK stoplist for multiple languages <br>
8. Lemmatizing the article before using the text analytics functions <br>

### Text Analytics capabilities include: <br>
1. A frequency counter on the most common words in the Wikipedia article (after omitting common English words, or stoplist from NLTK for foreign languages). Can also find the Nth % of most common words, where 0 =< N =< 100. <br>
2. A graph plot of the most common words in the Wikipedia article, and save the graph as an image <br>
3. A graph plot on the most frequent Years mentioned in the article, to understand the Years of interest of the article, and save the graph as an image <br>
4. A summary on the total number of words and total number of unique words after implementing the stoplist & lemmatization of common words. <br>
5. Analytics functions available in wikiscrape object are commonwords, commonwordspct, plotwords, plotyear, totalwords, summary, gettext. 
<br><br>
Refer to images in the repository for examples. The earliest image 'bar.png' made 4 months ago was the initial design for the bar chart for word frequency. Examples of the newest images (last edit: 27 Nov 2019) are 'ColdplayWordCount2.png' and 'Donald_Trump_40words.png'.
<br><br>

#### Libraries used: requests, bs4, collections, matplotlib, re, os, math, datetime, nltk (optional, only if using stoplist or lemmatization)
Refer to requirements.txt <br>
Package itself already has a comprehensive stoplist built inside to remove common words before text analytics <br>

#### Updates:
1. <b>26 May 2019</b> - Added plotyear() function to plot the most frequent years mentioned, and removed years in the frequency count of word counter (commonwords & commonwordspct functions).
2. <b>9 June 2019</b> - Added markdown for explanation and added comments in the code for understanding <br>
3. <b>13 June 2019</b> - Updated documentation for plotyear, plotwords, summary and gettext function in .HELP(). <br>
4. <b>25 November 2019</b> - Update coming very soon to patch issues and improve on Wikipedia package, stay tuned! <br>
5. <b>27 November 2019</b> - Major update to the Python package, including: <br>
  a. Adding of lemmatization feature (using NLTK) before using text analytics functions <br>
  b. Better documentation via docstrings and updating HELP function <br>
  c. Improving of graph plotting design and font size for plotwords and plotyear <br>
  d. Fixed some bugs for graph plotting including values not showing or showing up erroneously <br>
  e. Refactored the code, provided better names for key variables for user understanding <br>
  f. Performance improvement of article search by removing unused variables and functions <br>
  g. Tested all functions and also error handling in case user puts in wrong parameters <br>
6. <b>09 May 2020</b> - New feature to exclude N number of latest years in plotwords (e.g. from current year 2020, 2019, ...) and made graph titles larger
7. For any questions or suggestions, please contact me at my Linkedin account - https://www.linkedin.com/in/kohjiaxuan/ <br>
