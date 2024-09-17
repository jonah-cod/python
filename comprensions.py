from pprint import pprint as pp
import os
import glob

def listsSetComp():
    words = "well I couldn't think of any other words".split()
    # let's create a whole new list with lengths of each of above words
    # lists are iterables denoted by square brackets
    lengths_in_list = [len(word) for word in words]
    # we end up with a whole new list
    # [4, 1, 8, 5, 2, 3, 5, 5]
    print("Lists output")
    print(lengths_in_list)
    
    # same thing happens with sets
    # sets are iterables denoted by curly braces (unique items and don't contain key-values like dics)
    lengths_in_set  = {len(word) for word in words}
    # we end up with a whole new set
    # {1, 2, 3, 4, 5, 8}
    # with this time taking advantage of set's deduplication feature
    print("Sets output")
    print(lengths_in_set)
    
    
# listsSetComp()

def dicComps():
    country_to_capital = {'United Kingdom': 'London', 'Brazil': 'Brasilia', 'Morocco': 'Rabat', 'Sweden': 'Stockholm'}
    
    capital_to_country = { capital: country for country, capital in country_to_capital.items()}
    
    
    pp(capital_to_country)
    p = './'
    print("example with files")
    file_sizes = {os.path.realpath(p): f"{round(os.stat(p).st_size/1024, 3)} B" for p in glob.glob('*.py')}
    pp(file_sizes)
    
dicComps()

