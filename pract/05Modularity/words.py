# This is to showcase defining
# and calling a function
import sys
from urllib.request import urlopen


def fetch_words(url):
    """
        Fetch a list of words from a URL.
        Args:
              url : The URL of a UTF-8 text document.
        Returns:
              A list of strings containing the words from the document.
        CLI to pass:
            (venv) PS D:\Coading\Python_pract\pract\05Modularity> python words.py 'http://sixty-north.com/c/t.txt'
    """
    story = urlopen(url)
    story_words = []

    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words


# to run a loop to print words
def print_itmes(items):
    for item in items:
        print(item)


# to fetch words when the main method is called
def main(url):
    words = fetch_words(url)
    print_itmes(words)

if __name__ == '__main__':
    main(sys.argv[1])