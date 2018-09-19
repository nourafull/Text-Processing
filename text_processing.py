from collections import Counter
import os as os
import pandas as pd
import matplotlib.pyplot as plt

"""
This code reads books from the Book directory, which contains text files of books for different authors in different languages.
The code reads each book, then finds some statistics about each book (the length of the book- the number of unique words).
The statistics are stored in a DataFrame, using the Pandas library.
Finally, the statistics are plotted using pylot and saved as a PDF file. 
"""

def count_words(text):
    """recieves a string of text and returns a dictionary with the occurences of each word in the text"""
    text = text.lower()
    skips = [".","!","?"]
    for ch in skips:
        text = text.replace(ch," ")
    
    word_count = Counter(text.split(" "))
    return word_count

def read_book(title_path):
    """recieves a file path, reads the file and returns the text"""
    with open(title_path, "r", encoding="utf-8") as f:
        text = f.read()
        text = text.replace("\n"," ").replace("\r"," ")
    return text

def word_stats(word_counts):
    """recieves a dictionary"""
    num_unique = len(word_counts)
    counts = word_counts.values()
    return (num_unique,counts)
    

book_dir = "./Books"
i=1
stats = pd.DataFrame(columns = ("language","author","title","length","unique"))
for language in os.listdir(book_dir):
    for author in os.listdir(book_dir + "/" + language):
        for title in os.listdir(book_dir + "/" + language + "/" + author):
            inputfile = book_dir + "/" + language + "/" + author + "/" + title
            text = read_book(inputfile)
            (unq, count) = word_stats(count_words(text))
            stats.loc[i] = language, author.capitalize(), title.replace(".txt",""),sum(count),unq
            i += 1
            
"""
#the following print statements are used to peak into our stats dataframe            
print(stats.head())
print(stats.tail())
""" 

plt.figure(figsize=(10,10))     
subset = stats[stats.language == "English"]         
plt.loglog(subset.length,subset.unique,"o",label="English",color="blue")
subset = stats[stats.language == "French"]         
plt.loglog(subset.length,subset.unique,"o",label="French",color="green")
subset = stats[stats.language == "German"]         
plt.loglog(subset.length,subset.unique,"o",label="German",color="red")
subset = stats[stats.language == "Portuguese"]         
plt.loglog(subset.length,subset.unique,"o",label="Portuguese",color="yellow")
plt.legend()
plt.xlabel("Book Length")
plt.ylabel("Number of Unique Words")
plt.savefig("lang_plot.pdf")



















