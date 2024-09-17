#! C:\Users\JonathanMwaniki\AppData\Local\Programs\Python\Python311 python3
"""This module can fetch a list of words given a url
    and can also print a collection of items given the collection
"""
import sys
from urllib.request import urlopen

def fetchWords(url):
    """Fetches a list of words
        Args: a urlcof utf-8 text document
        
        Returns: A list of words in that document
    """
    story = urlopen(url)

    story_words = []

    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)
            
    story.close()
    return story_words


def printItems(items):
    """Prints items in a collection
    
        Args: An iterable series of printable items.
    """
    for item in items:
        print(item)
    
def main(url):
    words = fetchWords(url)
    printItems(words)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("a url is required")
    else:
        main(sys.argv[1])
        