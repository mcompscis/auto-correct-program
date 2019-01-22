# auto-correct-program
The AutoCorrect program contains three major parts, correction, common words, Wikipedia articles scraper.

Correction:
Correction basically takes in a string and runs through every possible combination of the given string (addition of an arbitrary letter, substitution of two letters in the string, deletion of an arbitrary letter in the string and substitution of two letters)
Correction returns a list of all the words that belong to the English dictionary. 
There is also another function called whitespace which just separates a large string into two valid words from the English dictionary. 

CommonWords:
There are essentially two ways to develop a count of the frequency of the words. The first method just reads a big file of English texts and creates the count. The second method scrapes anywhere from 100-4000 (depending on time) articles from Wikipedia, stores the word-count pair in a dictionary. Then, based on the word frequency, the top (n), where n can be any number of choice, given that the string has n alterations all in an English Dictionary, filter the list of corrected words. 

Web scraping:
This program initially reads an url that contains links to thousands of articles on the Wikipedia website. From the main page, my program returns the links to all the individual articles. The next step involves reading each link and returning a dictionary of all word-count pairs. Although this process gets the job done, it is inefficient as it can take hours to scrape 1000s of articles.

Future Aspiration:
I plan to incorporate databases (using SQL), which can help me store data from web scraping into tables and avoid the step of calling the web scraping program each time my auto-correct program runs. 
