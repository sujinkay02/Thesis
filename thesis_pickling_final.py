# Sujin Kay
# Senior Thesis/Project

import os       # accessing data files on computer
import pickle   # for pickling / storing data
import nltk     # NLTK package
from nltk.util import ngrams    # to compute n-grams
from collections import Counter # to count n-gram frequencies
import shutil   # moving files to different folders


"""
Compute n-grams and frequencies -- must specify N-Gram Size (n)
"""
def n_grams(n, data):
    # code source: http://www.nltk.org/_modules/nltk/util.html
    # code also adapted from:
    # https://github.com/starfirerhf/optimized_stam_07/blob/master/stamatatos_tweaked.py
    # use NLTK's built-in ngram generator
    n_grams = ngrams(data, n)

    # count frequency
    ngram_freq = Counter(n_grams)

    # total number of ngrams
    total_ngrams = sum(ngram_freq.values())

    # create author/gender profile; empty most_common parameter yields ALL items
    profile = Counter(dict(ngram_freq.most_common(10000)))

    # return total # ngrams and the author/gender profile
    return profile, total_ngrams


"""
PICKLED DATA FILENAMES
"""
def pickle_names():
    """ Raw / Char data """
    # unigrams
    'm_unichar'
    'f_unichar'
    'n_unichar'
    # testfiles = "unichar_" + testfile

    # other char-grams
    'm_bichar'
    'm_trichar'
    'm_quadchar'
    'm_5char'

    """ Word data """
    'm_uniwrd'
    # testfiles = "uniwrd_" + testfile

    """ POS data """
    'm_unitag'
    # testfiles = "unitag_" + testfile

    # de-pickling instructions:
    # a = open('male_rawdata', 'rb')
    # aa = pickle.load(a)
    # print (aa)
    # a.close()


"""
PICKLE ALL NGRAMS - GENDER FILES ONLY
"""
def pickle_char():
    # load picked char data
    m = open('male_rawdata', 'rb')
    m_raw = pickle.load(m)
    m.close()

    f = open('female_rawdata', 'rb')
    f_raw = pickle.load(f)
    f.close()

    n = open('nonbin_rawdata', 'rb')
    n_raw = pickle.load(n)
    n.close()

    # male
    unigrams, num_uni = n_grams(1, m_raw)
    a = open('m_unichar', 'wb')
    aa = pickle.dump((unigrams, num_uni), a)
    a.close()

    bigrams, num_bi = n_grams(2, m_raw)
    b = open('m_bichar', 'wb')
    bb = pickle.dump((bigrams, num_bi), b)
    b.close()

    trigrams, num_tri = n_grams(3, m_raw)
    c = open('m_trichar', 'wb')
    cc = pickle.dump((trigrams, num_tri), c)
    c.close()

    quadgrams, num_quad = n_grams(4, m_raw)
    d = open('m_quadchar', 'wb')
    dd = pickle.dump((quadgrams, num_quad), d)
    d.close()

    fivegrams, num_5 = n_grams(5, m_raw)
    e = open('m_5char', 'wb')
    ee = pickle.dump((fivegrams, num_5), e)
    e.close()

    # female
    unigrams, num_uni = n_grams(1, f_raw)
    a = open('f_unichar', 'wb')
    aa = pickle.dump((unigrams, num_uni), a)
    a.close()

    bigrams, num_bi = n_grams(2, f_raw)
    b = open('f_bichar', 'wb')
    bb = pickle.dump((bigrams, num_bi), b)
    b.close()

    trigrams, num_tri = n_grams(3, f_raw)
    c = open('f_trichar', 'wb')
    cc = pickle.dump((trigrams, num_tri), c)
    c.close()

    quadgrams, num_quad = n_grams(4, f_raw)
    d = open('f_quadchar', 'wb')
    dd = pickle.dump((quadgrams, num_quad), d)
    d.close()

    fivegrams, num_5 = n_grams(5, f_raw)
    e = open('f_5char', 'wb')
    ee = pickle.dump((fivegrams, num_5), e)
    e.close()

    # nonbinary
    unigrams, num_uni = n_grams(1, n_raw)
    a = open('n_unichar', 'wb')
    aa = pickle.dump((unigrams, num_uni), a)
    a.close()

    bigrams, num_bi = n_grams(2, n_raw)
    b = open('n_bichar', 'wb')
    bb = pickle.dump((bigrams, num_bi), b)
    b.close()

    trigrams, num_tri = n_grams(3, n_raw)
    c = open('n_trichar', 'wb')
    cc = pickle.dump((trigrams, num_tri), c)
    c.close()

    quadgrams, num_quad = n_grams(4, n_raw)
    d = open('n_quadchar', 'wb')
    dd = pickle.dump((quadgrams, num_quad), d)
    d.close()

    fivegrams, num_5 = n_grams(5, n_raw)
    e = open('n_5char', 'wb')
    ee = pickle.dump((fivegrams, num_5), e)
    e.close()

    return

def pickle_word():
    # # load picked word data
    m = open('male_wordsdata', 'rb')
    m_wrd = pickle.load(m)
    m.close()

    f = open('female_wordsdata', 'rb')
    f_wrd = pickle.load(f)
    f.close()

    # n = open('nonbin_wordsdata', 'rb')
    # n_wrd = pickle.load(n)
    # n.close()

    # # male
    unigrams, num_uni = n_grams(1, m_wrd)
    a = open('m_uniwrd', 'wb')
    aa = pickle.dump((unigrams, num_uni), a)
    a.close()

    bigrams, num_bi = n_grams(2, m_wrd)
    b = open('m_biwrd', 'wb')
    bb = pickle.dump((bigrams, num_bi), b)
    b.close()

    trigrams, num_tri = n_grams(3, m_wrd)
    c = open('m_triwrd', 'wb')
    cc = pickle.dump((trigrams, num_tri), c)
    c.close()

    quadgrams, num_quad = n_grams(4, m_wrd)
    d = open('m_quadwrd', 'wb')
    dd = pickle.dump((quadgrams, num_quad), d)
    d.close()

    fivegrams, num_5 = n_grams(5, m_wrd)
    e = open('m_5wrd', 'wb')
    ee = pickle.dump((fivegrams, num_5), e)
    e.close()

    # female
    unigrams, num_uni = n_grams(1, f_wrd)
    a = open('f_uniwrd', 'wb')
    aa = pickle.dump((unigrams, num_uni), a)
    a.close()

    bigrams, num_bi = n_grams(2, f_wrd)
    b = open('f_biwrd', 'wb')
    bb = pickle.dump((bigrams, num_bi), b)
    b.close()

    trigrams, num_tri = n_grams(3, f_wrd)
    c = open('f_triwrd', 'wb')
    cc = pickle.dump((trigrams, num_tri), c)
    c.close()

    quadgrams, num_quad = n_grams(4, f_wrd)
    d = open('f_quadwrd', 'wb')
    dd = pickle.dump((quadgrams, num_quad), d)
    d.close()

    fivegrams, num_5 = n_grams(5, f_wrd)
    e = open('f_5wrd', 'wb')
    ee = pickle.dump((fivegrams, num_5), e)
    e.close()

    # nonbinary
    unigrams, num_uni = n_grams(1, n_wrd)
    a = open('n_uniwrd', 'wb')
    aa = pickle.dump((unigrams, num_uni), a)
    a.close()

    bigrams, num_bi = n_grams(2, n_wrd)
    b = open('n_biwrd', 'wb')
    bb = pickle.dump((bigrams, num_bi), b)
    b.close()

    trigrams, num_tri = n_grams(3, n_wrd)
    c = open('n_triwrd', 'wb')
    cc = pickle.dump((trigrams, num_tri), c)
    c.close()

    quadgrams, num_quad = n_grams(4, n_wrd)
    d = open('n_quadwrd', 'wb')
    dd = pickle.dump((quadgrams, num_quad), d)
    d.close()

    fivegrams, num_5 = n_grams(5, n_wrd)
    e = open('n_5wrd', 'wb')
    ee = pickle.dump((fivegrams, num_5), e)
    e.close()

    return

def pickle_tag():
    # load picked word data
    m = open('male_tagsdata', 'rb')
    m_tag = pickle.load(m)
    m.close()

    f = open('female_tagsdata', 'rb')
    f_tag = pickle.load(f)
    f.close()

    n = open('nonbin_tagsdata', 'rb')
    n_tag = pickle.load(n)
    n.close()

    # male
    unigrams, num_uni = n_grams(1, m_tag)
    a = open('m_unitag', 'wb')
    aa = pickle.dump((unigrams, num_uni), a)
    a.close()

    bigrams, num_bi = n_grams(2, m_tag)
    b = open('m_bitag', 'wb')
    bb = pickle.dump((bigrams, num_bi), b)
    b.close()

    trigrams, num_tri = n_grams(3, m_tag)
    c = open('m_tritag', 'wb')
    cc = pickle.dump((trigrams, num_tri), c)
    c.close()

    quadgrams, num_quad = n_grams(4, m_tag)
    d = open('m_quadtag', 'wb')
    dd = pickle.dump((quadgrams, num_quad), d)
    d.close()

    fivegrams, num_5 = n_grams(5, m_tag)
    e = open('m_5tag', 'wb')
    ee = pickle.dump((fivegrams, num_5), e)
    e.close()

    # female
    unigrams, num_uni = n_grams(1, f_tag)
    a = open('f_unitag', 'wb')
    aa = pickle.dump((unigrams, num_uni), a)
    a.close()

    bigrams, num_bi = n_grams(2, f_tag)
    b = open('f_bitag', 'wb')
    bb = pickle.dump((bigrams, num_bi), b)
    b.close()

    trigrams, num_tri = n_grams(3, f_tag)
    c = open('f_tritag', 'wb')
    cc = pickle.dump((trigrams, num_tri), c)
    c.close()

    quadgrams, num_quad = n_grams(4, f_tag)
    d = open('f_quadtag', 'wb')
    dd = pickle.dump((quadgrams, num_quad), d)
    d.close()

    fivegrams, num_5 = n_grams(5, f_tag)
    e = open('f_5tag', 'wb')
    ee = pickle.dump((fivegrams, num_5), e)
    e.close()

    # nonbinary
    unigrams, num_uni = n_grams(1, n_tag)
    a = open('n_unitag', 'wb')
    aa = pickle.dump((unigrams, num_uni), a)
    a.close()

    bigrams, num_bi = n_grams(2, n_tag)
    b = open('n_bitag', 'wb')
    bb = pickle.dump((bigrams, num_bi), b)
    b.close()

    trigrams, num_tri = n_grams(3, n_tag)
    c = open('n_tritag', 'wb')
    cc = pickle.dump((trigrams, num_tri), c)
    c.close()

    quadgrams, num_quad = n_grams(4, n_tag)
    d = open('n_quadtag', 'wb')
    dd = pickle.dump((quadgrams, num_quad), d)
    d.close()

    fivegrams, num_5 = n_grams(5, n_tag)
    e = open('n_5tag', 'wb')
    ee = pickle.dump((fivegrams, num_5), e)
    e.close()

    return


"""
PICKLE ALL NGRAMS - TEST FILES ONLY
"""
# make sure to delete .DS_Store files before running
def pickle_char_tests(test_pickles_folder):
    for test_file in os.listdir(test_pickles_folder):
        # load pickled char data if it's a char file
        if "tags_" in test_file:
            a = open(test_file, 'rb')
            aa = pickle.load(a)
            a.close()

            # unigrams
            unigrams, num_uni = n_grams(1, aa)
            b = open('uni' + test_file, 'wb')
            bb = pickle.dump((unigrams, num_uni), b)
            b.close()

            # bigrams
            bigrams, num_bi = n_grams(2, aa)
            c = open('bi' + test_file, 'wb')
            cc = pickle.dump((bigrams, num_bi), c)
            c.close()

            # trigrams
            trigrams, num_tri = n_grams(3, aa)
            d = open('tri' + test_file, 'wb')
            dd = pickle.dump((trigrams, num_tri), d)
            d.close()

            # quadgrams
            quadgrams, num_quad = n_grams(4, aa)
            e = open('quad' + test_file, 'wb')
            ee = pickle.dump((quadgrams, num_quad), e)
            e.close()

            # 5grams
            fivegrams, num_5 = n_grams(5, aa)
            f = open('5' + test_file, 'wb')
            ff = pickle.dump((fivegrams, num_5), f)
            f.close()

    return

def pickle_word_tests(test_pickles_folder):
    for test_file in os.listdir(test_pickles_folder):
        # load pickled char data if it's a char file
        if "tags_" in test_file:
            a = open(test_file, 'rb')
            aa = pickle.load(a)
            a.close()

            # unigrams
            unigrams, num_uni = n_grams(1, aa)
            b = open('uni' + test_file, 'wb')
            bb = pickle.dump((unigrams, num_uni), b)
            b.close()

            # bigrams
            bigrams, num_bi = n_grams(2, aa)
            c = open('bi' + test_file, 'wb')
            cc = pickle.dump((bigrams, num_bi), c)
            c.close()

            # trigrams
            trigrams, num_tri = n_grams(3, aa)
            d = open('tri' + test_file, 'wb')
            dd = pickle.dump((trigrams, num_tri), d)
            d.close()

            # quadgrams
            quadgrams, num_quad = n_grams(4, aa)
            e = open('quad' + test_file, 'wb')
            ee = pickle.dump((quadgrams, num_quad), e)
            e.close()

            # 5grams
            fivegrams, num_5 = n_grams(5, aa)
            f = open('5' + test_file, 'wb')
            ff = pickle.dump((fivegrams, num_5), f)
            f.close()

    return

def pickle_tag_tests(test_pickles_folder):
    for test_file in os.listdir(test_pickles_folder):
        # load pickled char data if it's a char file
        if "tags_" in test_file:
            a = open(test_file, 'rb')
            aa = pickle.load(a)
            a.close()

            # unigrams
            unigrams, num_uni = n_grams(1, aa)
            b = open('uni' + test_file, 'wb')
            bb = pickle.dump((unigrams, num_uni), b)
            b.close()

            # bigrams
            bigrams, num_bi = n_grams(2, aa)
            c = open('bi' + test_file, 'wb')
            cc = pickle.dump((bigrams, num_bi), c)
            c.close()

            # trigrams
            trigrams, num_tri = n_grams(3, aa)
            d = open('tri' + test_file, 'wb')
            dd = pickle.dump((trigrams, num_tri), d)
            d.close()

            # quadgrams
            quadgrams, num_quad = n_grams(4, aa)
            e = open('quad' + test_file, 'wb')
            ee = pickle.dump((quadgrams, num_quad), e)
            e.close()

            # 5grams
            fivegrams, num_5 = n_grams(5, aa)
            f = open('5' + test_file, 'wb')
            ff = pickle.dump((fivegrams, num_5), f)
            f.close()

    return



"""---------------------------------------------------------------------------
MAIN
----------------------------------------------------------------------------"""

"""
DATA PROCESSING
"""
# "tests" folder holds all of the pickled raw/word/tag test data files
# test_pickles_folder = "/home/skay/Testpickles"
test_pickles_folder = "/Users/skay/Desktop/Thesis/Data/Testpickles"

# pickle all GENDER n-grams
# pickle_char()
# pickle_word()
# pickle_tag()

# pickle all TEST FILE n-grams
# pickle_char_tests(test_pickles_folder)
# pickle_word_tests(test_pickles_folder)
# pickle_tag_tests(test_pickles_folder)
#
# for test_file in os.listdir(test_pickles_folder):
#     # load pickled char data if it's a char file
#     if "unitags_" in test_file:
#         shutil.move(os.path.join(test_pickles_folder, test_file), '/Users/skay/Desktop/Thesis/TestGrams/TagGrams')
#
#     if "bitags_" in test_file:
#         shutil.move(os.path.join(test_pickles_folder, test_file), '/Users/skay/Desktop/Thesis/TestGrams/TagGrams')
#
#     if "tritags_" in test_file:
#         shutil.move(os.path.join(test_pickles_folder, test_file), '/Users/skay/Desktop/Thesis/TestGrams/TagGrams')
#
#     if "quadtags_" in test_file:
#         shutil.move(os.path.join(test_pickles_folder, test_file), '/Users/skay/Desktop/Thesis/TestGrams/TagGrams')
#
#     if "5tags_" in test_file:
#         shutil.move(os.path.join(test_pickles_folder, test_file), '/Users/skay/Desktop/Thesis/TestGrams/TagGrams')
