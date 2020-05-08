from os.path import dirname, abspath
import sys

# Get path of parent folder
parentpath = dirname(dirname(abspath(__file__)))

# Add to directory defined by sys
sys.path.append(parentpath)

# print(parentpath)
# print(sys.path)

# Now you can import wikiscrape
import wikiscrape

def newclass(title):
    return wikiscrape.wiki(title, 'yes', 'en', True, True)

# Simple test
if __name__ == "__main__":
    newclass('armin van buuren')
else:
    testclass = wikiscrape.wiki('armin van buuren', 'yes', 'en', True, True)
