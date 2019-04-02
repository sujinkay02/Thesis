# Sujin Kay
# Senior Thesis/Project

import os       # accessing data files on computer
import shutil   # moving files to different folders
import pickle   # for pickling / storing data
import nltk     # NLTK package
from nltk.util import ngrams    # to compute n-grams
from collections import Counter # to count n-gram frequencies
from bs4 import BeautifulSoup   # extract URLs from page source
import urllib.request           # access URLs

""""-----------------------------------------------------------------
BLOG CORPUS DATA
------------------------------------------------------------------"""

"""
Download/rename files (convert from .xml to .txt)
"""
def download_data(filepath):
    # iterate through all files in folder
    for filename in os.listdir(filepath):
        # each filename has the format: 'blogger ID number'.'gender'.'age'.'industry'.'astrological sign'.xml
        edit = filename.split('.')

        # rename each file to just have 'ID' and 'gender', and change from .xml to a .txt file
        new_filename = edit[0] + "." + edit[1] + ".txt"
        old_filepath = os.path.join(filepath, filename)
        new_filepath = os.path.join(filepath, new_filename)
        os.rename(old_filepath, new_filepath)

"""
Extract blog post data from between <post></post> tags, rewrite files
"""
def extract_data(filepath):
    # iterate through all files in folder
    for filename in os.listdir(filepath):
        # open the .txt file
        file = open(os.path.join(filepath, filename), "r+", errors='ignore')

        # collect all post data in one raw string
        post_data = ""
        # keep track of whether this is post data or not (text between <post></post> tags)
        keep_text = False

        for line in file:
            # keep track of whether we're seeing post contents or not
            if line.startswith("<post>"):
                # skip this line that contains the <post> tag
                line = file.readline()
                keep_text = True

            elif line.startswith("</post>"):
                keep_text = False

            if keep_text:
                # concatenate to post data gathered to far
                post_data = post_data + line

        # now, we want to clear out the file and replace it with just the post data we've gathered
        # go back to start of file
        file.seek(0)
        # clear contents
        file.truncate(0)

        # fill the file with post data
        file.write(post_data)
        file.close()

    return

"""
Extract 1449 male files into TEST folder
"""
def m_testfiles(filepath):
    m_count = 0
    folder = '/Users/skay/Desktop/Thesis/Data/TESTS'

    # iterate through all files in folder
    # extract 1449 male files
    for filename in os.listdir(filepath):
        if m_count == 1449:
            return

        if ".male." in filename:
            print (filename)
            # move to test folder
            shutil.move(os.path.join(filepath, filename), folder)
            m_count = m_count + 1

"""
Extract 1449 female files into TEST folder
"""
def f_testfiles(filepath):
    f_count = 0
    folder = '/Users/skay/Desktop/Thesis/Data/TESTS'

    # iterate through all files in folder
    # extract 1449 male files
    for filename in os.listdir(filepath):
        if f_count == 1449:
            return

        if ".female." in filename:
            print (filename)
            # move to test folder
            shutil.move(os.path.join(filepath, filename), folder)
            f_count = f_count + 1


"""------------------------------------------------------------------
DATA ACQUISITION -- NON-BINARY ARTICLE DATA
------------------------------------------------------------------"""

"""
Get links to all available articles (222 as of Feb 20, 2019)
"""
def non_binary_links():
    # home page
    main = "http://beyondthebinary.co.uk/"

    # store all links to other pages
    pages = []
    pages.append(main)

    # there are currently 35 pages' worth of articles
    i = 1
    while (i < 35):
        pages.append(main+"page/"+str(i)+"/")
        i += 1

    # extract all URLs within each page
    all_links = []

    for page in pages:
        webpage = urllib.request.urlopen(page)
        soup = BeautifulSoup(webpage, from_encoding=webpage.info().get_param('charset'), features="lxml")

        for url in soup.find_all('a', href=True):
            # don't include javascript file links and invalid URLs / next-page links
            if url['href'].startswith("http") and "/page/" not in url['href']:
                all_links.append(url['href'])

    # remove links with #comments or #respond
    for link in all_links:
        if ("#comments" in link or "#respond" in link):
            all_links.remove(link)

    # keep only unique links
    unique_links = set(all_links)

    # write list of links to file
    file = open("/Users/skay/Desktop/Thesis/Data/nonbinary/links/links.txt", "w+")
    file.truncate(0)
    file.seek(0)

    for link in unique_links:
        # separate links by newline
        file.write(link + "\n")

    # close the file
    file.close()
    return

"""
Extract text from all articles (create individual documents and try to identify author)
"""
def extract_nonbinary_data(links_filepath, nonbin_folder):
    # open the list of links
    links_file = open(links_filepath, "r")

    # auto-generate file names
    incr = 0

    # extract article data (between <p></p> HTML tags)
    # code sources: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
    # https://stackoverflow.com/questions/38546575/how-to-extract-value-from-a-class-in-beautiful-soup
    for link in links_file:
        # access the webpage
        webpage = urllib.request.urlopen(link)

        # use BeautifulSoup to extract data
        soup = BeautifulSoup(webpage, 'lxml')

        # article data is between <div class=post-content description> tags
        article = soup.find_all("div", {"class": "post-content description"})

        # extract text from post data
        for data in article:
            # extract text (exclude metadata)
            post_contents = data.get_text()

            # create an INDIVIDUAL .txt file to hold each article separately
            filename = ".nonbin." + str(incr) + ".txt"
            indiv_file = open(os.path.join(nonbin_folder, filename), "w+")

            # delete previous contents, if any
            indiv_file.truncate(0)

            # write contents to individual file
            indiv_file.write(post_contents)

            # close the file
            indiv_file.close()

        # increment the counter to generate different filename
        incr += 1

    return

"""
Try to determine article's author, and rename individual files accordingly
"""
def author_rename_file(authors):
    for filename in os.listdir(authors):
        # open the file
        file = open(os.path.join(authors, filename), "r", errors='ignore')

        # initialize author name to "None"
        author_name = "None"

        # author name could be in first line after "by [name]"
        first_line = file.readline()

        if first_line.startswith("by") or first_line.startswith("By"):
            # split text to extract author name
            name = first_line.split()

            # combine first/last name into a single string
            author_name = name[1] + name[2]

        # otherwise, could be after "Words by" at end of article
        else:
            for line in file:
                if "Words by" in line:
                    # split text to extract author name
                    words_by = line.split()

                    # remove "Words by"
                    name = words_by[2:]
                    author_name = ""

                    # combine first/last name into a single string
                    for name_part in name[:2]:
                        author_name += name_part

        # rename file to include (author name, nonbin, number, .txt)
        edit = filename.split('.')
        new_filename = author_name + "." + edit[0] + "." + edit[1] + ".txt"
        old_filepath = os.path.join(authors, filename)
        new_filepath = os.path.join(authors, new_filename)
        os.rename(old_filepath, new_filepath)

    return


"""------------------------------------------------------------------
DATA PROCESSING & ORGANIZATION
------------------------------------------------------------------"""

"""
Combine all male-blogger data
"""
def combine_male_data(filepath):
    # collect all male data in one raw string
    male_data = ""

    for filename in os.listdir(filepath):
        # only open male files
        if ".male." in filename:
            # open the .txt file
            file = open(os.path.join(filepath, filename), "r+", errors='ignore')

            # add entire file contents to male_data string
            for line in file:
                male_data = male_data + line

            # close the file
            file.close()

    # write all male_data to an empty file in separate folder
    file = open("/Users/skay/Desktop/Thesis/Data/male/male_raw.txt", "r+")

    # delete contents before writing, if any
    file.truncate(0)
    file.write(male_data)

    # close the file and exit
    file.close()
    return

"""
Combine all female-blogger data
"""
def combine_female_data(filepath):
    # collect all male data in one raw string
    female_data = ""

    for filename in os.listdir(filepath):
        # only open female files
        if ".female." in filename:
            # open the .txt file
            file = open(os.path.join(filepath, filename), "r+", errors="ignore")

            # add entire file contents to female_data string
            for line in file:
                female_data = female_data + line

            # close the file
            file.close()

    # write all female_data to an empty file in separate folder
    file = open("/Users/skay/Desktop/Thesis/Data/female/female_raw.txt", "r+")

    # delete contents before writing, if any
    file.truncate(0)
    file.write(female_data)

    # close the file and exit
    file.close()
    return

"""
Gather all non-binary author names (helper function)
"""
def nonbin_author_names(authors):
    # store all author names; use a dict to also keep track of # articles written by that author
    author_names = {}

    for filename in os.listdir(authors):
        # iterate through all files and update author names / article count
        name = filename.split(".")[0]

        # if name not in dict, add it
        if name not in author_names:
            author_names[name] = 1

        else:
            author_names[name] += 1

    return author_names

"""
Combine each non-binary author's articles into a single text
"""
def combine_nonbinary_authors(nonbin_folder, combined_folder, author_names):
    # iterate through all non-binary articles in folder
    for filename in os.listdir(nonbin_folder):
        # combine all articles for each author
        for author in author_names:
            if author != "None" and author in filename:
                # open original file
                file = open(os.path.join(nonbin_folder, filename), "r", errors='ignore')

                # open author data file (create new file if needed)
                author_filename = author + "_combined.nonbin.txt"
                author_file = open(os.path.join(combined_folder, author_filename), "w+")

                # write data to author file
                for line in file:
                    author_file.write(line)

                # close files
                file.close()
                author_file.close()
    return

"""
Combine all nonbinary-blogger data
"""
def combine_nonbinary_data(filepath):
    # collect all male data in one raw string
    nonbin_data = ""

    for filename in os.listdir(filepath):
        # only open female files
        if ".nonbin." in filename:
            # open the .txt file
            file = open(os.path.join(filepath, filename), "r+", errors="ignore")

            # add entire file contents to female_data string
            for line in file:
                nonbin_data = nonbin_data + line

            # close the file
            file.close()

    # write all female_data to an empty file in separate folder
    file = open("/Users/skay/Desktop/Thesis/Data/nonbin/nonbin_raw.txt", "r+")

    # delete contents before writing, if any
    file.truncate(0)
    file.write(nonbin_data)

    # close the file and exit
    file.close()
    return

"""
Get raw data via filepath
"""
def raw_data(filepath):
    # open file
    file = open(filepath, "r", errors='ignore')
    data = file.read()

    # close file and return data
    file.close()
    return data

"""
Tokenize text into words
"""
def tokenize(raw_text):
    # use NLTK's built-in tokenizer to split text into words
    words = nltk.word_tokenize(raw_text)

    # return tokenized data
    return words

"""
POS-tag words -- must be pre-tokenized
"""
def POS_tags(words):
    # tag words using NTLK's built-in tagger (use universal tagset)
    tagged_words = nltk.pos_tag(words, tagset="universal")

    # ONLY retain tags, not the words associated with them
    tags = [tag for (_, tag) in tagged_words]

    return tags

"""
Encode raw text into UTF-8 byte encoding
"""
def byte_encoding(raw_text):
    # encode raw text into utf-8
    byte_data = raw_text.encode("utf-8", "ignore")

    # return byte-encoded data
    return byte_data


"""
PICKLING - Remove .DS_Store files before iterating through directories!
"""
def pickle_raw(male_raw_data, female_raw_data, nonbin_raw_data, test_folder):
    a = open('male_rawdata', 'ab')
    pickle.dump(male_raw_data, a)
    a.close()

    b = open('female_rawdata', 'ab')
    pickle.dump(female_raw_data, b)
    b.close()

    c = open('nonbin_rawdata', 'ab')
    pickle.dump(nonbin_raw_data, c)
    c.close()

    # iterate through all files in test folder
    for testfile in os.listdir(test_folder):
        # open the .txt file
        filename = os.path.join(test_folder, testfile)

        # get raw data
        raw = raw_data(filename)

        # pickle each test file
        d = open("raw_" + testfile, 'ab')
        pickle.dump(raw, d)
        d.close()

def pickle_words(male_words, female_words, nonbin_words, test_folder):
    a = open('male_wordsdata', 'ab')
    pickle.dump(male_words, a)
    a.close()

    b = open('female_wordsdata', 'ab')
    pickle.dump(female_words, b)
    b.close()

    c = open('nonbin_wordsdata', 'ab')
    pickle.dump(nonbin_words, c)
    c.close()

    for testfile in os.listdir(test_folder):
        # open the .txt file
        filename = os.path.join(test_folder, testfile)

        # get tokenized data
        raw = raw_data(filename)
        words = tokenize(raw)

        # pickle each test file
        d = open("wrds_" + testfile, 'ab')
        pickle.dump(words, d)
        d.close()

    return

def pickle_tags(male_tags, female_tags, nonbin_tags, test_folder):
    a = open('male_tagsdata', 'ab')
    pickle.dump(male_tags, a)
    a.close()

    b = open('female_tagsdata', 'ab')
    pickle.dump(female_tags, b)
    b.close()

    c = open('nonbin_tagsdata', 'ab')
    pickle.dump(nonbin_tags, c)
    c.close()

    # iterate through all files in test folder
    for testfile in os.listdir(test_folder):
        # get the pickled word data
        filename = "wrds_" + testfile
        e = open(filename, 'rb')
        words = pickle.load(e)
        e.close()

        # get tokenized data
        tags = POS_tags(words)

        # pickle each test file
        d = open("tags_" + testfile, 'ab')
        pickle.dump(tags, d)
        d.close()

"""
DE-PICKLING
"""
def depickle_raw(test_folder):
    a = open('male_rawdata', 'rb')
    aa = pickle.load(a)
    print (aa)
    a.close()

    b = open('female_rawdata', 'rb')
    ba = pickle.load(b)
    print (ba)
    b.close()

    c = open('nonbin_rawdata', 'rb')
    ca = pickle.load(c)
    print (ca)
    c.close()

    # iterate through all files in test folder
    for testfile in os.listdir(test_folder):
        # open the .txt file
        # pickle each test file
        d = open("raw_" + testfile, 'rb')
        da = pickle.load(d)
        print (da)
        d.close()

    return

def depickle_words(test_folder):
    a = open('male_wordsdata', 'rb')
    aa = pickle.load(a)
    print (aa)
    a.close()

    b = open('female_wordsdata', 'rb')
    ba = pickle.load(b)
    print (ba)
    b.close()

    c = open('nonbin_wordsdata', 'rb')
    ca = pickle.load(c)
    print (ca)
    c.close()

    # iterate through all files in test folder
    for testfile in os.listdir(test_folder):
        # open the .txt file
        # pickle each test file
        d = open("wrds_" + testfile, 'rb')
        da = pickle.load(d)
        print(da)
        d.close()

    return

def depickle_tags(test_folder):
    a = open('male_tagsdata', 'rb')
    aa = pickle.load(a)
    print (aa)
    a.close()

    b = open('female_tagsdata', 'rb')
    ba = pickle.load(b)
    print (ba)
    b.close()

    c = open('nonbin_tagsdata', 'rb')
    ca = pickle.load(c)
    print (ca)
    c.close()

    # iterate through all files in test folder
    for testfile in os.listdir(test_folder):
        # open the .txt file
        # pickle each test file
        d = open("tags_" + testfile, 'rb')
        da = pickle.load(d)
        print(da)
        d.close()

    return



"""---------------------------------------------------------------------------
MAIN
----------------------------------------------------------------------------"""

"""
DATA PROCESSING
"""
# "blogs" folder holds all of the untouched data files
# each file contains all of the posts for an individual blog
filepath = "/Users/skay/Desktop/Thesis/Data/blogs"

# TRAINING folder holds all training data
training = "/Users/skay/Desktop/Thesis/Data/TRAINING"

# "tests" folder holds all of the test data files
test_folder = "/Users/skay/Desktop/Thesis/Data/TESTS"

# links.txt holds the list of links to all non-binary articles
links_filepath = "/Users/skay/Desktop/Thesis/Data/nonbin/links/links.txt"

# "indiv_author" folder holds all of the individual non-binary files
nonbin_folder = "/Users/skay/Desktop/Thesis/Data/nonbin/individual"

# nonbinary/"authors" folder holds all of the author-scraped individual files
nonbin_authors = "/Users/skay/Desktop/Thesis/Data/nonbin/authors"

# combined folder holds all author_combined files
nonbin_combined = "/Users/skay/Desktop/Thesis/Data/nonbin/combined"



# ONLY RUN THESE ONCE
# download_data(filepath)       # do NOT run this at the same time as extract_data()
# extract_data(filepath)
# m_testfiles(training)
# f_testfiles(training)
# combine_male_data(training)
# combine_female_data(training)

# ONLY RUN THESE ONCE
# gather links and extract data from non-binary articles
# links = non_binary_links()
# extract_nonbinary_data(links_filepath, nonbin_folder)
# author_rename_file(nonbin_authors)
# authors = nonbin_author_names(nonbin_authors)
# note -- need to manually copy over "None" author files into this folder
# combine_nonbinary_authors(nonbin_authors, nonbin_combined, authors)
# combine_nonbinary_data(training)

# gender profile filepaths (.txt files)
# male_filepath = "/Users/skay/Desktop/Thesis/Data/male/male_raw.txt"
# female_filepath = "/Users/skay/Desktop/Thesis/Data/female/female_raw.txt"
# nonbin_filepath = "/Users/skay/Desktop/Thesis/Data/nonbin/nonbin_raw.txt"

# gender RAW (CHAR) data
# male_raw_data = raw_data(male_filepath)
# female_raw_data = raw_data(female_filepath)
# nonbin_raw_data = raw_data(nonbin_filepath)

# gender TOKENIZED data
# a = open(picked_folder + 'male_rawdata', 'rb')
# b = open(pickled_folder + 'female_rawdata', 'rb')
# c = open(pickled_folder + 'nonbin_rawdata', 'rb')
# pickle_mraw = pickle.load(a)
# pickle_fraw = pickle.load(b)
# pickle_nraw = pickle.load(c)
# male_words = tokenize(pickle_mraw)
# female_words = tokenize(pickle_fraw)
# nonbin_words = tokenize(pickle_nraw)
# a.close()
# b.close()
# c.close()

# gender TAGGED data
# d = open('male_wordsdata', 'rb')
# e = open('female_wordsdata', 'rb')
# f = open('nonbin_wordsdata', 'rb')
# pickle_mwords = pickle.load(d)
# pickle_fwords = pickle.load(e)
# pickle_nwords = pickle.load(f)
# male_tags = POS_tags(pickle_mwords)
# female_tags = POS_tags(pickle_fwords)
# nonbin_tags = POS_tags(pickle_nwords)
# d.close()
# e.close()
# f.close()

# gender BYTE-encoded data
# male_byte_data = byte_encoding(male_raw_data)
# female_byte_data = byte_encoding(female_raw_data)
# nonbin_byte_data = byte_encoding(nonbin_raw_data)

# PICKLING
# pickle_raw(male_raw_data, female_raw_data, nonbin_raw_data, test_folder)
# pickle_words(male_words, female_words, nonbin_words, test_folder)
# pickle_tags(male_tags, female_tags, nonbin_tags, test_folder)

# DE-PICKLING
# depickle_raw(test_folder)
# depickle_words(test_folder)
# depickle_tags(test_folder)
