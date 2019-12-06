# Hackathon-Idea-Generator

This generator works by scraping devpost.com for the project descriptions of trending projects, and then training [gpt-2-simple](https://github.com/minimaxir/gpt-2-simple) on these descriptions. Ensure that you have downloaded [chromedriver](https://chromedriver.chromium.org/downloads) corresponding to your version of Chrome and have placed it in the same directory as the code. 

To run, either run scraper.py to scrape current hacks (recommended) or use the existing hacks.txt file provided.
Then run trainer.py.
To generate new outputs, run 'gpt_2_simple generate' in the terminal, and the results will be in a directory labeled 'gen'.
