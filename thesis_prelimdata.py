# Sujin Kay
# Senior Thesis/Project

import os       # accessing data files on computer
import pickle   # for pickling / storing data
import nltk     # NLTK package
from nltk.util import ngrams    # to compute n-grams
from collections import Counter # to count n-gram frequencies


"""------------------------------------------------------------------------
ANALYSIS AND TESTING
------------------------------------------------------------------------"""

"""
Compute simple dissimilarity measure between author text and gender profiles
"""
# only binary classification
def dissimilarity_b(author_profile, author_ngram_count, male_profile, male_ngram_count, female_profile, female_ngram_count):
    # code adapted from:
    # https://github.com/starfirerhf/optimized_stam_07/blob/master/stamatatos_tweaked.py
    dissimilarity_male = 0
    dissimilarity_female = 0

    # compare Author to Male Profile
    features = set(male_profile.keys())

    for feature in features:
        # calculate NORMALIZED frequencies
        # return 0 if key not in dictionary
        f1 = float(author_profile.get(feature, 0)) / author_ngram_count
        f2 = float(male_profile.get(feature, 0)) / male_ngram_count

        # dissimilarity formula
        dissimilarity_male += (2 * (f1 - f2) / (f1 + f2)) ** 2

    # compare Author to Female Profile
    features = set(female_profile.keys())

    for feature in features:
        # calculate NORMALIZED frequencies
        f1 = float(author_profile.get(feature, 0)) / author_ngram_count
        f2 = float(female_profile.get(feature, 0)) / female_ngram_count

        # dissimilarity formula
        dissimilarity_female += (2 * (f1 - f2) / (f1 + f2)) ** 2

    # print ("male dissimilarity: {:.2f}".format(dissimilarity_male), "\nfemale dissimilarity: {:.2f}".format(dissimilarity_female))

    # classify gender based on lowest dissimilarity
    gender_classification = min(dissimilarity_male, dissimilarity_female)

    # return gender classification
    if (gender_classification == dissimilarity_male):
        return "male"

    else:
        return "female"

# nonbinary classification
# author_profile and gender_profiles is the n-grams output (dictionary)
def dissimilarity(author_profile, author_ngram_count, male_profile, male_ngram_count, female_profile, female_ngram_count, nonbin_profile, nonbin_ngram_count):
    # code adapted from:
    # https://github.com/starfirerhf/optimized_stam_07/blob/master/stamatatos_tweaked.py
    dissimilarity_male = 0
    dissimilarity_female = 0
    dissimilarity_nonbin = 0

    # compare Author to Male Profile
    features = set(male_profile.keys())

    for feature in features:
        # calculate NORMALIZED frequencies
        # return 0 if key not in dictionary
        f1 = float(author_profile.get(feature, 0)) / author_ngram_count
        f2 = float(male_profile.get(feature, 0)) / male_ngram_count

        # dissimilarity formula
        dissimilarity_male += (2 * (f1 - f2) / (f1 + f2)) ** 2

    # compare Author to Female Profile
    features = set(female_profile.keys())

    for feature in features:
        # calculate NORMALIZED frequencies
        f1 = float(author_profile.get(feature, 0)) / author_ngram_count
        f2 = float(female_profile.get(feature, 0)) / female_ngram_count

        # dissimilarity formula
        dissimilarity_female += (2 * (f1 - f2) / (f1 + f2)) ** 2

    # compare Author to Non-binary Profile
    features = set(nonbin_profile.keys())

    for feature in features:
        # calculate NORMALIZED frequencies
        f1 = float(author_profile.get(feature, 0)) / author_ngram_count
        f2 = float(nonbin_profile.get(feature, 0)) / nonbin_ngram_count

        # dissimilarity formula
        dissimilarity_nonbin += (2 * (f1 - f2) / (f1 + f2)) ** 2

    # print ("male dissimilarity: {:.2f}".format(dissimilarity_male), "\nfemale dissimilarity: {:.2f}".format(dissimilarity_female), "\nnon-binary dissimilarity: {:.2f}".format( dissimilarity_nonbin))

    # classify gender based on lowest dissimilarity
    gender_classification = min(dissimilarity_male, dissimilarity_female, dissimilarity_nonbin)

    # return gender classification
    if (gender_classification == dissimilarity_male):
        return "male"

    elif (gender_classification == dissimilarity_female):
        return "female"

    else:
        return "non-binary"

"""
Checks classification accuracy
"""
def accuracy(guess, filename):
    # return 1 if author gender was classified correctly
    if (".female." in filename and guess == "female"):
        # print ("Accurately guessed female!\n")
        return 1

    elif (".male." in filename and guess == "male"):
        # print ("Accurately guessed male!\n")
        return 1

    elif("nonbin" in filename and guess == "non-binary"):
        # print ("Accurately guessed non-binary!\n")
        return 1

    # return 0 if incorrect
    else:
        # print ("Incorrectly guessed", guess, "\n")
        return 0

"""
Pre-Experimentation: Normalized frequency distributions
"""
def char_freq(top):
    a = open('m_unichar', 'rb')
    aa = pickle.load(a)
    a.close()

    print ("MALE:\n")
    for (k, v) in aa[0].most_common(top):
        print (k)

    for (k, v) in aa[0].most_common(top):
        print (v)
    print ("Total:", aa[1])
    print ("\n\n")

    a = open('f_unichar', 'rb')
    aa = pickle.load(a)
    a.close()

    print ("FEMALE:\n")
    for (k, v) in aa[0].most_common(top):
        print (k)

    for (k, v) in aa[0].most_common(top):
        print (v)
    print ("Total:", aa[1])
    print ("\n\n")

    a = open('n_unichar', 'rb')
    aa = pickle.load(a)
    a.close()

    print ("NONBINARY:\n")
    for (k, v) in aa[0].most_common(top):
        print (k)

    for (k, v) in aa[0].most_common(top):
        print (v)
    print ("Total:", aa[1])
    print ("\n\n")

    return
def word_freq(top):
    a = open('m_uniwrd', 'rb')
    aa = pickle.load(a)
    a.close()

    print ("MALE:\n")
    for (k, v) in aa[0].most_common(top):
        print (k)

    for (k, v) in aa[0].most_common(top):
        print (v)
    print ("Total:", aa[1])
    print ("\n\n")

    a = open('f_uniwrd', 'rb')
    aa = pickle.load(a)
    a.close()

    print ("FEMALE:\n")
    for (k, v) in aa[0].most_common(top):
        print (k)

    for (k, v) in aa[0].most_common(top):
        print (v)
    print ("Total:", aa[1])
    print ("\n\n")

    a = open('n_uniwrd', 'rb')
    aa = pickle.load(a)
    a.close()

    print ("NONBINARY:\n")
    for (k, v) in aa[0].most_common(top):
        print (k)

    for (k, v) in aa[0].most_common(top):
        print (v)
    print ("Total:", aa[1])
    print ("\n\n")

    return
def POS_freq(top):
    a = open('m_unitag', 'rb')
    aa = pickle.load(a)
    a.close()

    print ("MALE:\n")
    for (k, v) in aa[0].most_common(top):
        print (k)

    for (k, v) in aa[0].most_common(top):
        print (v)
    print ("Total:", aa[1])
    print ("\n\n")

    a = open('f_unitag', 'rb')
    aa = pickle.load(a)
    a.close()

    print ("FEMALE:\n")
    for (k, v) in aa[0].most_common(top):
        print (k)

    for (k, v) in aa[0].most_common(top):
        print (v)
    print ("Total:", aa[1])
    print ("\n\n")

    a = open('n_unitag', 'rb')
    aa = pickle.load(a)
    a.close()

    print ("NONBINARY:\n")
    for (k, v) in aa[0].most_common(top):
        print (k)

    for (k, v) in aa[0].most_common(top):
        print (v)
    print ("Total:", aa[1])
    print ("\n\n")

    return


"""
TESTS -- BINARY
"""
""" CHAR n-grams (L most frequent) """
def unichar_testb(L, test_folder):
    # count number of tests run
    num_tests = 0

    # calculate accuracy
    acc = 0

    # get male, female, nonbinary pickled char ngrams data
    # unigrams
    a = open('m_unichar', 'rb')
    aa = pickle.load(a)
    a.close()
    male_profile = dict(aa[0].most_common(L))
    male_ngram_count = aa[1]

    b = open('f_unichar', 'rb')
    bb = pickle.load(b)
    b.close()
    female_profile = dict(bb[0].most_common(L))
    female_ngram_count = bb[1]

    c = open('n_unichar', 'rb')
    cc = pickle.load(c)
    c.close()
    nonbin_profile = dict(cc[0].most_common(L))
    nonbin_ngram_count = cc[1]

    for testfile in os.listdir(test_folder):
        # get test pickled char data
        if "uniraw_" in testfile:
            x = open(testfile, 'rb')
            xx = pickle.load(x)
            x.close()
            author_profile = dict(xx[0].most_common(L))
            author_ngram_count = xx[1]

            # increment number of tests run
            num_tests += 1

            # classify gender
            # print (testfile)
            guess = dissimilarity_b(author_profile, author_ngram_count, male_profile, male_ngram_count, female_profile, female_ngram_count)

            # record accuracy
            acc += accuracy(guess, testfile)

    # calculate total accuracy
    print ("Character Unigrams for L=", L)
    print ("Overall accuracy over", num_tests, "tests:", acc / num_tests)
    return
def bichar_testb(L, test_folder):
    # count number of tests run
    num_tests = 0

    # calculate accuracy
    acc = 0

    # bigrams
    d = open('m_bichar', 'rb')
    dd = pickle.load(d)
    d.close()
    male_profile = dict(dd[0].most_common(L))
    male_ngram_count = dd[1]

    e = open('f_bichar', 'rb')
    ee = pickle.load(e)
    e.close()
    female_profile = dict(ee[0].most_common(L))
    female_ngram_count = ee[1]

    f = open('n_bichar', 'rb')
    ff = pickle.load(f)
    f.close()
    nonbin_profile = dict(ff[0].most_common(L))
    nonbin_ngram_count = ff[1]

    for testfile in os.listdir(test_folder):
        # get test pickled char data
        if "biraw_" in testfile:
            x = open(testfile, 'rb')
            xx = pickle.load(x)
            x.close()
            author_profile = dict(xx[0].most_common(L))
            author_ngram_count = xx[1]

            # increment number of tests run
            num_tests += 1

            # classify gender
            # print (testfile)
            guess = dissimilarity_b(author_profile, author_ngram_count, male_profile, male_ngram_count, female_profile, female_ngram_count)

            # record accuracy
            acc += accuracy(guess, testfile)

    # calculate total accuracy
    print ("Character Bigrams for L=", L)
    print ("Overall accuracy over", num_tests, "tests:", acc / num_tests)
    return
def trichar_testb(L, test_folder):
    # count number of tests run
    num_tests = 0

    # calculate accuracy
    acc = 0

    # trigrams
    g = open('m_trichar', 'rb')
    gg = pickle.load(g)
    g.close()
    male_profile = dict(gg[0].most_common(L))
    male_ngram_count = gg[1]

    h = open('f_trichar', 'rb')
    hh = pickle.load(h)
    h.close()
    female_profile = dict(hh[0].most_common(L))
    female_ngram_count = hh[1]

    i = open('n_trichar', 'rb')
    ii = pickle.load(i)
    i.close()
    nonbin_profile = dict(ii[0].most_common(L))
    nonbin_ngram_count = ii[1]

    for testfile in os.listdir(test_folder):
        # get test pickled char data
        if "triraw_" in testfile:
            x = open(testfile, 'rb')
            xx = pickle.load(x)
            x.close()
            author_profile = dict(xx[0].most_common(L))
            author_ngram_count = xx[1]

            # increment number of tests run
            num_tests += 1

            # classify gender
            # print (testfile)
            guess = dissimilarity_b(author_profile, author_ngram_count, male_profile, male_ngram_count, female_profile, female_ngram_count)

            # record accuracy
            acc += accuracy(guess, testfile)

    # calculate total accuracy
    print ("Character Trigrams for L=", L)
    print ("Overall accuracy over", num_tests, "tests:", acc / num_tests)
    return
def quadchar_testb(L, test_folder):
    # count number of tests run
    num_tests = 0

    # calculate accuracy
    acc = 0

    # quadgrams
    j = open('m_quadchar', 'rb')
    jj = pickle.load(j)
    j.close()
    male_profile = dict(jj[0].most_common(L))
    male_ngram_count = jj[1]

    k = open('f_quadchar', 'rb')
    kk = pickle.load(k)
    k.close()
    female_profile = dict(kk[0].most_common(L))
    female_ngram_count = kk[1]

    l = open('n_quadchar', 'rb')
    ll = pickle.load(l)
    l.close()
    nonbin_profile = dict(ll[0].most_common(L))
    nonbin_ngram_count = ll[1]

    for testfile in os.listdir(test_folder):
        # get test pickled char data
        if "quadraw_" in testfile:
            x = open(testfile, 'rb')
            xx = pickle.load(x)
            x.close()
            author_profile = dict(xx[0].most_common(L))
            author_ngram_count = xx[1]

            # increment number of tests run
            num_tests += 1

            # classify gender
            # print (testfile)
            guess = dissimilarity_b(author_profile, author_ngram_count, male_profile, male_ngram_count, female_profile, female_ngram_count)

            # record accuracy
            acc += accuracy(guess, testfile)

    # calculate total accuracy
    print ("Character Quadgrams for L=", L)
    print ("Overall accuracy over", num_tests, "tests:", acc / num_tests)
    return
def fivechar_testb(L, test_folder):
    # count number of tests run
    num_tests = 0

    # calculate accuracy
    acc = 0

    # 5grams
    m = open('m_5char', 'rb')
    mm = pickle.load(m)
    m.close()
    male_profile = dict(mm[0].most_common(L))
    male_ngram_count = mm[1]

    n = open('f_5char', 'rb')
    nn = pickle.load(n)
    n.close()
    female_profile = dict(nn[0].most_common(L))
    female_ngram_count = nn[1]

    o = open('n_5char', 'rb')
    oo = pickle.load(o)
    o.close()
    nonbin_profile = dict(oo[0].most_common(L))
    nonbin_ngram_count = oo[1]

    for testfile in os.listdir(test_folder):
        # get test pickled char data
        if "5raw_" in testfile:
            x = open(testfile, 'rb')
            xx = pickle.load(x)
            x.close()
            author_profile = dict(xx[0].most_common(L))
            author_ngram_count = xx[1]

            # increment number of tests run
            num_tests += 1

            # classify gender
            # print (testfile)
            guess = dissimilarity_b(author_profile, author_ngram_count, male_profile, male_ngram_count, female_profile, female_ngram_count)

            # record accuracy
            acc += accuracy(guess, testfile)

    # calculate total accuracy
    print ("Character 5grams for L=", L)
    print ("Overall accuracy over", num_tests, "tests:", acc / num_tests)
    return

""" WORD n-grams """
def uniwrd_testb(L, test_folder):
    # count number of tests run
    num_tests = 0

    # calculate accuracy
    acc = 0

    # get male, female, nonbinary pickled word ngrams data
    # unigrams
    a = open('m_uniwrd', 'rb')
    aa = pickle.load(a)
    a.close()
    male_profile = dict(aa[0].most_common(L))
    male_ngram_count = aa[1]

    b = open('f_uniwrd', 'rb')
    bb = pickle.load(b)
    b.close()
    female_profile = dict(bb[0].most_common(L))
    female_ngram_count = bb[1]

    c = open('n_uniwrd', 'rb')
    cc = pickle.load(c)
    c.close()
    nonbin_profile = dict(cc[0].most_common(L))
    nonbin_ngram_count = cc[1]

    for testfile in os.listdir(test_folder):
        # get test pickled char data
        if "uniwrds_" in testfile:
            x = open(testfile, 'rb')
            xx = pickle.load(x)
            x.close()
            author_profile = dict(xx[0].most_common(L))
            author_ngram_count = xx[1]

            # increment number of tests run
            num_tests += 1

            # classify gender
            # print (testfile)
            guess = dissimilarity_b(author_profile, author_ngram_count, male_profile, male_ngram_count, female_profile, female_ngram_count)

            # record accuracy
            acc += accuracy(guess, testfile)

    # calculate total accuracy
    print ("Word Unigrams for L=", L)
    print ("Overall accuracy over", num_tests, "tests:", acc / num_tests)
    return
def biwrd_testb(L, test_folder):
    # count number of tests run
    num_tests = 0

    # calculate accuracy
    acc = 0

    # bigrams
    d = open('m_biwrd', 'rb')
    dd = pickle.load(d)
    d.close()
    male_profile = dict(dd[0].most_common(L))
    male_ngram_count = dd[1]

    e = open('f_biwrd', 'rb')
    ee = pickle.load(e)
    e.close()
    female_profile = dict(ee[0].most_common(L))
    female_ngram_count = ee[1]

    f = open('n_biwrd', 'rb')
    ff = pickle.load(f)
    f.close()
    nonbin_profile = dict(ff[0].most_common(L))
    nonbin_ngram_count = ff[1]

    for testfile in os.listdir(test_folder):
        # get test pickled word data
        if "biwrds_" in testfile:
            x = open(testfile, 'rb')
            xx = pickle.load(x)
            x.close()
            author_profile = dict(xx[0].most_common(L))
            author_ngram_count = xx[1]

            # increment number of tests run
            num_tests += 1

            # classify gender
            # print (testfile)
            guess = dissimilarity_b(author_profile, author_ngram_count, male_profile, male_ngram_count, female_profile, female_ngram_count)

            # record accuracy
            acc += accuracy(guess, testfile)

    # calculate total accuracy
    print ("Word Bigrams for L=", L)
    print ("Overall accuracy over", num_tests, "tests:", acc / num_tests)
    return
def triwrd_testb(L, test_folder):
    # count number of tests run
    num_tests = 0

    # calculate accuracy
    acc = 0

    # trigrams
    g = open('m_triwrd', 'rb')
    gg = pickle.load(g)
    g.close()
    male_profile = dict(gg[0].most_common(L))
    male_ngram_count = gg[1]

    h = open('f_triwrd', 'rb')
    hh = pickle.load(h)
    h.close()
    female_profile = dict(hh[0].most_common(L))
    female_ngram_count = hh[1]

    i = open('n_triwrd', 'rb')
    ii = pickle.load(i)
    i.close()
    nonbin_profile = dict(ii[0].most_common(L))
    nonbin_ngram_count = ii[1]

    for testfile in os.listdir(test_folder):
        # get test pickled word data
        if "triwrds_" in testfile:
            x = open(testfile, 'rb')
            xx = pickle.load(x)
            x.close()
            author_profile = dict(xx[0].most_common(L))
            author_ngram_count = xx[1]

            # increment number of tests run
            num_tests += 1

            # classify gender
            # print (testfile)
            guess = dissimilarity_b(author_profile, author_ngram_count, male_profile, male_ngram_count, female_profile, female_ngram_count)

            # record accuracy
            acc += accuracy(guess, testfile)

    # calculate total accuracy
    print ("Word Trigrams for L=", L)
    print ("Overall accuracy over", num_tests, "tests:", acc / num_tests)
    return
def quadwrd_testb(L, test_folder):
    # count number of tests run
    num_tests = 0

    # calculate accuracy
    acc = 0

    # quadgrams
    j = open('m_quadwrd', 'rb')
    jj = pickle.load(j)
    j.close()
    male_profile = dict(jj[0].most_common(L))
    male_ngram_count = jj[1]

    k = open('f_quadwrd', 'rb')
    kk = pickle.load(k)
    k.close()
    female_profile = dict(kk[0].most_common(L))
    female_ngram_count = kk[1]

    l = open('n_quadwrd', 'rb')
    ll = pickle.load(l)
    l.close()
    nonbin_profile = dict(ll[0].most_common(L))
    nonbin_ngram_count = ll[1]

    for testfile in os.listdir(test_folder):
        # get test pickled word data
        if "quadwrds_" in testfile:
            x = open(testfile, 'rb')
            xx = pickle.load(x)
            x.close()
            author_profile = dict(xx[0].most_common(L))
            author_ngram_count = xx[1]

            # increment number of tests run
            num_tests += 1

            # classify gender
            # print (testfile)
            guess = dissimilarity_b(author_profile, author_ngram_count, male_profile, male_ngram_count, female_profile, female_ngram_count)

            # record accuracy
            acc += accuracy(guess, testfile)

    # calculate total accuracy
    print ("Word Quadgrams for L=", L)
    print ("Overall accuracy over", num_tests, "tests:", acc / num_tests)
    return
def fivewrd_testb(L, test_folder):
    # count number of tests run
    num_tests = 0

    # calculate accuracy
    acc = 0

    # 5grams
    m = open('m_5wrd', 'rb')
    mm = pickle.load(m)
    m.close()
    male_profile = dict(mm[0].most_common(L))
    male_ngram_count = mm[1]

    n = open('f_5wrd', 'rb')
    nn = pickle.load(n)
    n.close()
    female_profile = dict(nn[0].most_common(L))
    female_ngram_count = nn[1]

    o = open('n_5wrd', 'rb')
    oo = pickle.load(o)
    o.close()
    nonbin_profile = dict(oo[0].most_common(L))
    nonbin_ngram_count = oo[1]

    for testfile in os.listdir(test_folder):
        # get test pickled word data
        if "5wrds_" in testfile:
            x = open(testfile, 'rb')
            xx = pickle.load(x)
            x.close()
            author_profile = dict(xx[0].most_common(L))
            author_ngram_count = xx[1]

            # increment number of tests run
            num_tests += 1

            # classify gender
            # print (testfile)
            guess = dissimilarity_b(author_profile, author_ngram_count, male_profile, male_ngram_count, female_profile, female_ngram_count)

            # record accuracy
            acc += accuracy(guess, testfile)

    # calculate total accuracy
    print ("Word 5grams for L=", L)
    print ("Overall accuracy over", num_tests, "tests:", acc / num_tests)
    return

""" POS n-grams """
def unitag_testb(L, test_folder):
    # count number of tests run
    num_tests = 0

    # calculate accuracy
    acc = 0

    # get male, female, nonbinary pickled tag ngrams data
    # unigrams
    a = open('m_unitag', 'rb')
    aa = pickle.load(a)
    a.close()
    male_profile = dict(aa[0].most_common(L))
    male_ngram_count = aa[1]

    b = open('f_unitag', 'rb')
    bb = pickle.load(b)
    b.close()
    female_profile = dict(bb[0].most_common(L))
    female_ngram_count = bb[1]

    c = open('n_unitag', 'rb')
    cc = pickle.load(c)
    c.close()
    nonbin_profile = dict(cc[0].most_common(L))
    nonbin_ngram_count = cc[1]

    for testfile in os.listdir(test_folder):
        # get test pickled char data
        if "unitags_" in testfile:
            x = open(testfile, 'rb')
            xx = pickle.load(x)
            x.close()
            author_profile = dict(xx[0].most_common(L))
            author_ngram_count = xx[1]

            # increment number of tests run
            num_tests += 1

            # classify gender
            # print (testfile)
            guess = dissimilarity_b(author_profile, author_ngram_count, male_profile, male_ngram_count, female_profile, female_ngram_count)

            # record accuracy
            acc += accuracy(guess, testfile)

    # calculate total accuracy
    print ("Tag Unigrams for L=", L)
    print ("Overall accuracy over", num_tests, "tests:", acc / num_tests)
    return
def bitag_testb(L, test_folder):
    # count number of tests run
    num_tests = 0

    # calculate accuracy
    acc = 0

    # bigrams
    d = open('m_bitag', 'rb')
    dd = pickle.load(d)
    d.close()
    male_profile = dict(dd[0].most_common(L))
    male_ngram_count = dd[1]

    e = open('f_bitag', 'rb')
    ee = pickle.load(e)
    e.close()
    female_profile = dict(ee[0].most_common(L))
    female_ngram_count = ee[1]

    f = open('n_bitag', 'rb')
    ff = pickle.load(f)
    f.close()
    nonbin_profile = dict(ff[0].most_common(L))
    nonbin_ngram_count = ff[1]

    for testfile in os.listdir(test_folder):
        # get test pickled tag data
        if "bitags_" in testfile:
            x = open(testfile, 'rb')
            xx = pickle.load(x)
            x.close()
            author_profile = dict(xx[0].most_common(L))
            author_ngram_count = xx[1]

            # increment number of tests run
            num_tests += 1

            # classify gender
            # print (testfile)
            guess = dissimilarity_b(author_profile, author_ngram_count, male_profile, male_ngram_count, female_profile, female_ngram_count)

            # record accuracy
            acc += accuracy(guess, testfile)

    # calculate total accuracy
    print ("Tag Bigrams for L=", L)
    print ("Overall accuracy over", num_tests, "tests:", acc / num_tests)
    return
def tritag_testb(L, test_folder):
    # count number of tests run
    num_tests = 0

    # calculate accuracy
    acc = 0

    # trigrams
    g = open('m_tritag', 'rb')
    gg = pickle.load(g)
    g.close()
    male_profile = dict(gg[0].most_common(L))
    male_ngram_count = gg[1]

    h = open('f_tritag', 'rb')
    hh = pickle.load(h)
    h.close()
    female_profile = dict(hh[0].most_common(L))
    female_ngram_count = hh[1]

    i = open('n_tritag', 'rb')
    ii = pickle.load(i)
    i.close()
    nonbin_profile = dict(ii[0].most_common(L))
    nonbin_ngram_count = ii[1]

    for testfile in os.listdir(test_folder):
        # get test pickled tag data
        if "tritags_" in testfile:
            x = open(testfile, 'rb')
            xx = pickle.load(x)
            x.close()
            author_profile = dict(xx[0].most_common(L))
            author_ngram_count = xx[1]

            # increment number of tests run
            num_tests += 1

            # classify gender
            # print (testfile)
            guess = dissimilarity_b(author_profile, author_ngram_count, male_profile, male_ngram_count, female_profile, female_ngram_count)

            # record accuracy
            acc += accuracy(guess, testfile)

    # calculate total accuracy
    print ("Tag Trigrams for L=", L)
    print ("Overall accuracy over", num_tests, "tests:", acc / num_tests)
    return
def quadtag_testb(L, test_folder):
    # count number of tests run
    num_tests = 0

    # calculate accuracy
    acc = 0

    # quadgrams
    j = open('m_quadtag', 'rb')
    jj = pickle.load(j)
    j.close()
    male_profile = dict(jj[0].most_common(L))
    male_ngram_count = jj[1]

    k = open('f_quadtag', 'rb')
    kk = pickle.load(k)
    k.close()
    female_profile = dict(kk[0].most_common(L))
    female_ngram_count = kk[1]

    l = open('n_quadtag', 'rb')
    ll = pickle.load(l)
    l.close()
    nonbin_profile = dict(ll[0].most_common(L))
    nonbin_ngram_count = ll[1]

    for testfile in os.listdir(test_folder):
        # get test pickled tag data
        if "quadtags_" in testfile:
            x = open(testfile, 'rb')
            xx = pickle.load(x)
            x.close()
            author_profile = dict(xx[0].most_common(L))
            author_ngram_count = xx[1]

            # increment number of tests run
            num_tests += 1

            # classify gender
            # print (testfile)
            guess = dissimilarity_b(author_profile, author_ngram_count, male_profile, male_ngram_count, female_profile, female_ngram_count)

            # record accuracy
            acc += accuracy(guess, testfile)

    # calculate total accuracy
    print ("Tag Quadgrams for L=", L)
    print ("Overall accuracy over", num_tests, "tests:", acc / num_tests)
    return
def fivetag_testb(L, test_folder):
    # count number of tests run
    num_tests = 0

    # calculate accuracy
    acc = 0

    # 5grams
    m = open('m_5tag', 'rb')
    mm = pickle.load(m)
    m.close()
    male_profile = dict(mm[0].most_common(L))
    male_ngram_count = mm[1]

    n = open('f_5tag', 'rb')
    nn = pickle.load(n)
    n.close()
    female_profile = dict(nn[0].most_common(L))
    female_ngram_count = nn[1]

    o = open('n_5tag', 'rb')
    oo = pickle.load(o)
    o.close()
    nonbin_profile = dict(oo[0].most_common(L))
    nonbin_ngram_count = oo[1]

    for testfile in os.listdir(test_folder):
        # get test pickled tag data
        if "5tags_" in testfile:
            x = open(testfile, 'rb')
            xx = pickle.load(x)
            x.close()
            author_profile = dict(xx[0].most_common(L))
            author_ngram_count = xx[1]

            # increment number of tests run
            num_tests += 1

            # classify gender
            # print (testfile)
            guess = dissimilarity_b(author_profile, author_ngram_count, male_profile, male_ngram_count, female_profile, female_ngram_count)

            # record accuracy
            acc += accuracy(guess, testfile)

    # calculate total accuracy
    print ("Tag 5grams for L=", L)
    print ("Overall accuracy over", num_tests, "tests:", acc / num_tests)
    return

"""
TESTS -- NONBINARY
"""
""" CHAR n-grams (L most frequent) """
def unichar_test(L, test_folder):
    # count number of tests run
    num_tests = 0

    # calculate accuracy
    acc = 0

    # get male, female, nonbinary pickled char ngrams data
    # unigrams
    a = open('m_unichar', 'rb')
    aa = pickle.load(a)
    a.close()
    male_profile = dict(aa[0].most_common(L))
    male_ngram_count = aa[1]

    b = open('f_unichar', 'rb')
    bb = pickle.load(b)
    b.close()
    female_profile = dict(bb[0].most_common(L))
    female_ngram_count = bb[1]

    c = open('n_unichar', 'rb')
    cc = pickle.load(c)
    c.close()
    nonbin_profile = dict(cc[0].most_common(L))
    nonbin_ngram_count = cc[1]

    for testfile in os.listdir(test_folder):
        # get test pickled char data
        if "uniraw_" in testfile:
            x = open(testfile, 'rb')
            xx = pickle.load(x)
            x.close()
            author_profile = dict(xx[0].most_common(L))
            author_ngram_count = xx[1]

            # increment number of tests run
            num_tests += 1

            # classify gender
            # print (testfile)
            guess = dissimilarity(author_profile, author_ngram_count, male_profile, male_ngram_count, female_profile, female_ngram_count, nonbin_profile, nonbin_ngram_count)

            # record accuracy
            acc += accuracy(guess, testfile)

    # calculate total accuracy
    print ("Character Unigrams for L=", L, "\n")
    print ("Overall accuracy over", num_tests, "tests:", acc / num_tests)
    return
def bichar_test(L, test_folder):
    # count number of tests run
    num_tests = 0

    # calculate accuracy
    acc = 0

    # bigrams
    d = open('m_bichar', 'rb')
    dd = pickle.load(d)
    d.close()
    male_profile = dict(dd[0].most_common(L))
    male_ngram_count = dd[1]

    e = open('f_bichar', 'rb')
    ee = pickle.load(e)
    e.close()
    female_profile = dict(ee[0].most_common(L))
    female_ngram_count = ee[1]

    f = open('n_bichar', 'rb')
    ff = pickle.load(f)
    f.close()
    nonbin_profile = dict(ff[0].most_common(L))
    nonbin_ngram_count = ff[1]

    for testfile in os.listdir(test_folder):
        # get test pickled char data
        if "biraw_" in testfile:
            x = open(testfile, 'rb')
            xx = pickle.load(x)
            x.close()
            author_profile = dict(xx[0].most_common(L))
            author_ngram_count = xx[1]

            # increment number of tests run
            num_tests += 1

            # classify gender
            # print (testfile)
            guess = dissimilarity(author_profile, author_ngram_count, male_profile, male_ngram_count, female_profile, female_ngram_count, nonbin_profile, nonbin_ngram_count)

            # record accuracy
            acc += accuracy(guess, testfile)

    # calculate total accuracy
    print ("Character Bigrams for L=", L, "\n")
    print ("Overall accuracy over", num_tests, "tests:", acc / num_tests)
    return
def trichar_test(L, test_folder):
    # count number of tests run
    num_tests = 0

    # calculate accuracy
    acc = 0

    # trigrams
    g = open('m_trichar', 'rb')
    gg = pickle.load(g)
    g.close()
    male_profile = dict(gg[0].most_common(L))
    male_ngram_count = gg[1]

    h = open('f_trichar', 'rb')
    hh = pickle.load(h)
    h.close()
    female_profile = dict(hh[0].most_common(L))
    female_ngram_count = hh[1]

    i = open('n_trichar', 'rb')
    ii = pickle.load(i)
    i.close()
    nonbin_profile = dict(ii[0].most_common(L))
    nonbin_ngram_count = ii[1]

    for testfile in os.listdir(test_folder):
        # get test pickled char data
        if "triraw_" in testfile:
            x = open(testfile, 'rb')
            xx = pickle.load(x)
            x.close()
            author_profile = dict(xx[0].most_common(L))
            author_ngram_count = xx[1]

            # increment number of tests run
            num_tests += 1

            # classify gender
            # print (testfile)
            guess = dissimilarity(author_profile, author_ngram_count, male_profile, male_ngram_count, female_profile, female_ngram_count, nonbin_profile, nonbin_ngram_count)

            # record accuracy
            acc += accuracy(guess, testfile)

    # calculate total accuracy
    print ("Character Trigrams for L=", L, "\n")
    print ("Overall accuracy over", num_tests, "tests:", acc / num_tests)
    return
def quadchar_test(L, test_folder):
    # count number of tests run
    num_tests = 0

    # calculate accuracy
    acc = 0

    # quadgrams
    j = open('m_quadchar', 'rb')
    jj = pickle.load(j)
    j.close()
    male_profile = dict(jj[0].most_common(L))
    male_ngram_count = jj[1]

    k = open('f_quadchar', 'rb')
    kk = pickle.load(k)
    k.close()
    female_profile = dict(kk[0].most_common(L))
    female_ngram_count = kk[1]

    l = open('n_quadchar', 'rb')
    ll = pickle.load(l)
    l.close()
    nonbin_profile = dict(ll[0].most_common(L))
    nonbin_ngram_count = ll[1]

    for testfile in os.listdir(test_folder):
        # get test pickled char data
        if "quadraw_" in testfile:
            x = open(testfile, 'rb')
            xx = pickle.load(x)
            x.close()
            author_profile = dict(xx[0].most_common(L))
            author_ngram_count = xx[1]

            # increment number of tests run
            num_tests += 1

            # classify gender
            # print (testfile)
            guess = dissimilarity(author_profile, author_ngram_count, male_profile, male_ngram_count, female_profile, female_ngram_count, nonbin_profile, nonbin_ngram_count)

            # record accuracy
            acc += accuracy(guess, testfile)

    # calculate total accuracy
    print ("Character Quadgrams for L=", L, "\n")
    print ("Overall accuracy over", num_tests, "tests:", acc / num_tests)
    return
def fivechar_test(L, test_folder):
    # count number of tests run
    num_tests = 0

    # calculate accuracy
    acc = 0

    # 5grams
    m = open('m_5char', 'rb')
    mm = pickle.load(m)
    m.close()
    male_profile = dict(mm[0].most_common(L))
    male_ngram_count = mm[1]

    n = open('f_5char', 'rb')
    nn = pickle.load(n)
    n.close()
    female_profile = dict(nn[0].most_common(L))
    female_ngram_count = nn[1]

    o = open('n_5char', 'rb')
    oo = pickle.load(o)
    o.close()
    nonbin_profile = dict(oo[0].most_common(L))
    nonbin_ngram_count = oo[1]

    for testfile in os.listdir(test_folder):
        # get test pickled char data
        if "5raw_" in testfile:
            x = open(testfile, 'rb')
            xx = pickle.load(x)
            x.close()
            author_profile = dict(xx[0].most_common(L))
            author_ngram_count = xx[1]

            # increment number of tests run
            num_tests += 1

            # classify gender
            # print (testfile)
            guess = dissimilarity(author_profile, author_ngram_count, male_profile, male_ngram_count, female_profile, female_ngram_count, nonbin_profile, nonbin_ngram_count)

            # record accuracy
            acc += accuracy(guess, testfile)

    # calculate total accuracy
    print ("Character 5grams for L=", L, "\n")
    print ("Overall accuracy over", num_tests, "tests:", acc / num_tests)
    return

""" WORD n-grams """
def uniwrd_test(L, test_folder):
    # count number of tests run
    num_tests = 0

    # calculate accuracy
    acc = 0

    # get male, female, nonbinary pickled word ngrams data
    # unigrams
    a = open('m_uniwrd', 'rb')
    aa = pickle.load(a)
    a.close()
    male_profile = dict(aa[0].most_common(L))
    male_ngram_count = aa[1]

    b = open('f_uniwrd', 'rb')
    bb = pickle.load(b)
    b.close()
    female_profile = dict(bb[0].most_common(L))
    female_ngram_count = bb[1]

    c = open('n_uniwrd', 'rb')
    cc = pickle.load(c)
    c.close()
    nonbin_profile = dict(cc[0].most_common(L))
    nonbin_ngram_count = cc[1]

    for testfile in os.listdir(test_folder):
        # get test pickled char data
        if "uniwrds_" in testfile:
            x = open(testfile, 'rb')
            xx = pickle.load(x)
            x.close()
            author_profile = dict(xx[0].most_common(L))
            author_ngram_count = xx[1]

            # increment number of tests run
            num_tests += 1

            # classify gender
            # print (testfile)
            guess = dissimilarity(author_profile, author_ngram_count, male_profile, male_ngram_count, female_profile, female_ngram_count, nonbin_profile, nonbin_ngram_count)

            # record accuracy
            acc += accuracy(guess, testfile)

    # calculate total accuracy
    print ("Word Unigrams for L=", L, "\n")
    print ("Overall accuracy over", num_tests, "tests:", acc / num_tests)
    return
def biwrd_test(L, test_folder):
    # count number of tests run
    num_tests = 0

    # calculate accuracy
    acc = 0

    # bigrams
    d = open('m_biwrd', 'rb')
    dd = pickle.load(d)
    d.close()
    male_profile = dict(dd[0].most_common(L))
    male_ngram_count = dd[1]

    e = open('f_biwrd', 'rb')
    ee = pickle.load(e)
    e.close()
    female_profile = dict(ee[0].most_common(L))
    female_ngram_count = ee[1]

    f = open('n_biwrd', 'rb')
    ff = pickle.load(f)
    f.close()
    nonbin_profile = dict(ff[0].most_common(L))
    nonbin_ngram_count = ff[1]

    for testfile in os.listdir(test_folder):
        # get test pickled word data
        if "biwrds_" in testfile:
            x = open(testfile, 'rb')
            xx = pickle.load(x)
            x.close()
            author_profile = dict(xx[0].most_common(L))
            author_ngram_count = xx[1]

            # increment number of tests run
            num_tests += 1

            # classify gender
            # print (testfile)
            guess = dissimilarity(author_profile, author_ngram_count, male_profile, male_ngram_count, female_profile, female_ngram_count, nonbin_profile, nonbin_ngram_count)

            # record accuracy
            acc += accuracy(guess, testfile)

    # calculate total accuracy
    print ("Word Bigrams for L=", L, "\n")
    print ("Overall accuracy over", num_tests, "tests:", acc / num_tests)
    return
def triwrd_test(L, test_folder):
    # count number of tests run
    num_tests = 0

    # calculate accuracy
    acc = 0

    # trigrams
    g = open('m_triwrd', 'rb')
    gg = pickle.load(g)
    g.close()
    male_profile = dict(gg[0].most_common(L))
    male_ngram_count = gg[1]

    h = open('f_triwrd', 'rb')
    hh = pickle.load(h)
    h.close()
    female_profile = dict(hh[0].most_common(L))
    female_ngram_count = hh[1]

    i = open('n_triwrd', 'rb')
    ii = pickle.load(i)
    i.close()
    nonbin_profile = dict(ii[0].most_common(L))
    nonbin_ngram_count = ii[1]

    for testfile in os.listdir(test_folder):
        # get test pickled word data
        if "triwrds_" in testfile:
            x = open(testfile, 'rb')
            xx = pickle.load(x)
            x.close()
            author_profile = dict(xx[0].most_common(L))
            author_ngram_count = xx[1]

            # increment number of tests run
            num_tests += 1

            # classify gender
            # print (testfile)
            guess = dissimilarity(author_profile, author_ngram_count, male_profile, male_ngram_count, female_profile, female_ngram_count, nonbin_profile, nonbin_ngram_count)

            # record accuracy
            acc += accuracy(guess, testfile)

    # calculate total accuracy
    print ("Word Trigrams for L=", L, "\n")
    print ("Overall accuracy over", num_tests, "tests:", acc / num_tests)
    return
def quadwrd_test(L, test_folder):
    # count number of tests run
    num_tests = 0

    # calculate accuracy
    acc = 0

    # quadgrams
    j = open('m_quadwrd', 'rb')
    jj = pickle.load(j)
    j.close()
    male_profile = dict(jj[0].most_common(L))
    male_ngram_count = jj[1]

    k = open('f_quadwrd', 'rb')
    kk = pickle.load(k)
    k.close()
    female_profile = dict(kk[0].most_common(L))
    female_ngram_count = kk[1]

    l = open('n_quadwrd', 'rb')
    ll = pickle.load(l)
    l.close()
    nonbin_profile = dict(ll[0].most_common(L))
    nonbin_ngram_count = ll[1]

    for testfile in os.listdir(test_folder):
        # get test pickled word data
        if "quadwrds_" in testfile:
            x = open(testfile, 'rb')
            xx = pickle.load(x)
            x.close()
            author_profile = dict(xx[0].most_common(L))
            author_ngram_count = xx[1]

            # increment number of tests run
            num_tests += 1

            # classify gender
            # print (testfile)
            guess = dissimilarity(author_profile, author_ngram_count, male_profile, male_ngram_count, female_profile, female_ngram_count, nonbin_profile, nonbin_ngram_count)

            # record accuracy
            acc += accuracy(guess, testfile)

    # calculate total accuracy
    print ("Word Quadgrams for L=", L, "\n")
    print ("Overall accuracy over", num_tests, "tests:", acc / num_tests)
    return
    # count number of tests run
    num_tests = 0

    # calculate accuracy
    acc = 0

    # 5grams
    m = open('m_5wrd', 'rb')
    mm = pickle.load(m)
    m.close()
    male_profile = dict(mm[0].most_common(L))
    male_ngram_count = mm[1]

    n = open('f_5wrd', 'rb')
    nn = pickle.load(n)
    n.close()
    female_profile = dict(nn[0].most_common(L))
    female_ngram_count = nn[1]

    o = open('n_5wrd', 'rb')
    oo = pickle.load(o)
    o.close()
    nonbin_profile = dict(oo[0].most_common(L))
    nonbin_ngram_count = oo[1]

    for testfile in os.listdir(test_folder):
        # get test pickled word data
        if "5wrds_" in testfile:
            x = open(testfile, 'rb')
            xx = pickle.load(x)
            x.close()
            author_profile = dict(xx[0].most_common(L))
            author_ngram_count = xx[1]

            # increment number of tests run
            num_tests += 1

            # classify gender
            # print (testfile)
            guess = dissimilarity(author_profile, author_ngram_count, male_profile, male_ngram_count, female_profile, female_ngram_count, nonbin_profile, nonbin_ngram_count)

            # record accuracy
            acc += accuracy(guess, testfile)

    # calculate total accuracy
    print ("Word 5grams for L=", L, "\n")
    print ("Overall accuracy over", num_tests, "tests:", acc / num_tests)
    return

""" POS n-grams """
def unitag_test(L, test_folder):
    # count number of tests run
    num_tests = 0

    # calculate accuracy
    acc = 0

    # count number of tests run
    num_tests = 0

    # calculate accuracy
    acc = 0

    # get male, female, nonbinary pickled tag ngrams data
    # unigrams
    a = open('m_unitag', 'rb')
    aa = pickle.load(a)
    a.close()
    male_profile = dict(aa[0].most_common(L))
    male_ngram_count = aa[1]

    b = open('f_unitag', 'rb')
    bb = pickle.load(b)
    b.close()
    female_profile = dict(bb[0].most_common(L))
    female_ngram_count = bb[1]

    c = open('n_unitag', 'rb')
    cc = pickle.load(c)
    c.close()
    nonbin_profile = dict(cc[0].most_common(L))
    nonbin_ngram_count = cc[1]

    for testfile in os.listdir(test_folder):
        # get test pickled char data
        if "unitags_" in testfile:
            x = open(testfile, 'rb')
            xx = pickle.load(x)
            x.close()
            author_profile = dict(xx[0].most_common(L))
            author_ngram_count = xx[1]

            # increment number of tests run
            num_tests += 1

            # classify gender
            # print (testfile)
            guess = dissimilarity(author_profile, author_ngram_count, male_profile, male_ngram_count, female_profile, female_ngram_count, nonbin_profile, nonbin_ngram_count)

            # record accuracy
            acc += accuracy(guess, testfile)

    # calculate total accuracy
    print ("Tag Unigrams for L=", L, "\n")
    print ("Overall accuracy over", num_tests, "tests:", acc / num_tests)
    return
def bitag_test(L, test_folder):
    # count number of tests run
    num_tests = 0

    # calculate accuracy
    acc = 0

    # bigrams
    d = open('m_bitag', 'rb')
    dd = pickle.load(d)
    d.close()
    male_profile = dict(dd[0].most_common(L))
    male_ngram_count = dd[1]

    e = open('f_bitag', 'rb')
    ee = pickle.load(e)
    e.close()
    female_profile = dict(ee[0].most_common(L))
    female_ngram_count = ee[1]

    f = open('n_bitag', 'rb')
    ff = pickle.load(f)
    f.close()
    nonbin_profile = dict(ff[0].most_common(L))
    nonbin_ngram_count = ff[1]

    for testfile in os.listdir(test_folder):
        # get test pickled tag data
        if "bitags_" in testfile:
            x = open(testfile, 'rb')
            xx = pickle.load(x)
            x.close()
            author_profile = dict(xx[0].most_common(L))
            author_ngram_count = xx[1]

            # increment number of tests run
            num_tests += 1

            # classify gender
            # print (testfile)
            guess = dissimilarity(author_profile, author_ngram_count, male_profile, male_ngram_count, female_profile, female_ngram_count, nonbin_profile, nonbin_ngram_count)

            # record accuracy
            acc += accuracy(guess, testfile)

    # calculate total accuracy
    print ("Tag Bigrams for L=", L, "\n")
    print ("Overall accuracy over", num_tests, "tests:", acc / num_tests)
    return
def tritag_test(L, test_folder):
    # count number of tests run
    num_tests = 0

    # calculate accuracy
    acc = 0

    # trigrams
    g = open('m_tritag', 'rb')
    gg = pickle.load(g)
    g.close()
    male_profile = dict(gg[0].most_common(L))
    male_ngram_count = gg[1]

    h = open('f_tritag', 'rb')
    hh = pickle.load(h)
    h.close()
    female_profile = dict(hh[0].most_common(L))
    female_ngram_count = hh[1]

    i = open('n_tritag', 'rb')
    ii = pickle.load(i)
    i.close()
    nonbin_profile = dict(ii[0].most_common(L))
    nonbin_ngram_count = ii[1]

    for testfile in os.listdir(test_folder):
        # get test pickled tag data
        if "tritags_" in testfile:
            x = open(testfile, 'rb')
            xx = pickle.load(x)
            x.close()
            author_profile = dict(xx[0].most_common(L))
            author_ngram_count = xx[1]

            # increment number of tests run
            num_tests += 1

            # classify gender
            # print (testfile)
            guess = dissimilarity(author_profile, author_ngram_count, male_profile, male_ngram_count, female_profile, female_ngram_count, nonbin_profile, nonbin_ngram_count)

            # record accuracy
            acc += accuracy(guess, testfile)

    # calculate total accuracy
    print ("Tag Trigrams for L=", L, "\n")
    print ("Overall accuracy over", num_tests, "tests:", acc / num_tests)
    return
def quadtag_test(L, test_folder):
    # count number of tests run
    num_tests = 0

    # calculate accuracy
    acc = 0

    # quadgrams
    j = open('m_quadtag', 'rb')
    jj = pickle.load(j)
    j.close()
    male_profile = dict(jj[0].most_common(L))
    male_ngram_count = jj[1]

    k = open('f_quadtag', 'rb')
    kk = pickle.load(k)
    k.close()
    female_profile = dict(kk[0].most_common(L))
    female_ngram_count = kk[1]

    l = open('n_quadtag', 'rb')
    ll = pickle.load(l)
    l.close()
    nonbin_profile = dict(ll[0].most_common(L))
    nonbin_ngram_count = ll[1]

    for testfile in os.listdir(test_folder):
        # get test pickled tag data
        if "quadtags_" in testfile:
            x = open(testfile, 'rb')
            xx = pickle.load(x)
            x.close()
            author_profile = dict(xx[0].most_common(L))
            author_ngram_count = xx[1]

            # increment number of tests run
            num_tests += 1

            # classify gender
            # print (testfile)
            guess = dissimilarity(author_profile, author_ngram_count, male_profile, male_ngram_count, female_profile, female_ngram_count, nonbin_profile, nonbin_ngram_count)

            # record accuracy
            acc += accuracy(guess, testfile)

    # calculate total accuracy
    print ("Tag Quadgrams for L=", L, "\n")
    print ("Overall accuracy over", num_tests, "tests:", acc / num_tests)
    return
def fivetag_test(L, test_folder):
    # count number of tests run
    num_tests = 0

    # calculate accuracy
    acc = 0

    # 5grams
    m = open('m_5tag', 'rb')
    mm = pickle.load(m)
    m.close()
    male_profile = dict(mm[0].most_common(L))
    male_ngram_count = mm[1]

    n = open('f_5tag', 'rb')
    nn = pickle.load(n)
    n.close()
    female_profile = dict(nn[0].most_common(L))
    female_ngram_count = nn[1]

    o = open('n_5tag', 'rb')
    oo = pickle.load(o)
    o.close()
    nonbin_profile = dict(oo[0].most_common(L))
    nonbin_ngram_count = oo[1]

    for testfile in os.listdir(test_folder):
        # get test pickled tag data
        if "5tags_" in testfile:
            x = open(testfile, 'rb')
            xx = pickle.load(x)
            x.close()
            author_profile = dict(xx[0].most_common(L))
            author_ngram_count = xx[1]

            # increment number of tests run
            num_tests += 1

            # classify gender
            # print (testfile)
            guess = dissimilarity(author_profile, author_ngram_count, male_profile, male_ngram_count, female_profile, female_ngram_count, nonbin_profile, nonbin_ngram_count)

            # record accuracy
            acc += accuracy(guess, testfile)

    # calculate total accuracy
    print ("Tag 5grams for L=", L, "\n")
    print ("Overall accuracy over", num_tests, "tests:", acc / num_tests)
    return


"""---------------------------------------------------------------------------
MAIN
----------------------------------------------------------------------------"""

"""
DATA PROCESSING
"""
# this folder holds all of the test data files
# NOTE: Python program MUST be saved in the same directory, otherwise pickled data can't be loaded
test_folder = "/Users/skay/Desktop/Thesis/ALLP_TESTFILES"


"""
PICKLED DATA FILES
"""
def pickle_names():
    """ Raw / Char data """
    # unigrams
    'm_unichar'
    'f_unichar'
    'n_unichar'
    # testfiles = "unichar" + testfile

    # other char-grams
    'm_bichar'
    'm_trichar'
    'm_quadchar'
    'm_5char'

    """ Word data """
    'm_uniwrd'
    # testfiles = "uniwrd" + testfile

    """ POS data """
    'm_unitag'
    # testfiles = "unitag" + testfile

    # de-pickling instructions:
    # a = open('male_rawdata', 'rb')
    # aa = pickle.load(a)
    # print (aa)
    # a.close()


"""
PRE-EXPERIMENTATION
"""
top = 20

# looking at data on the POS/word/char/byte levels
# char_freq(top)
word_freq(top)
# POS_freq(top)



"""
TESTING
"""
# feature set / profile size
L_sizes = {10, 500, 1000, 5000, 10000}

# test across n-grams size and various sizes of L
# for L in L_sizes:
#     # binary tests
#     unichar_testb(L, test_folder)
#     bichar_testb(L, test_folder)
#     trichar_testb(L, test_folder)
#     quadchar_testb(L, test_folder)
#     fivechar_testb(L, test_folder)
#
#     uniwrd_testb(L, test_folder)
#     biwrd_testb(L, test_folder)
#     triwrd_testb(L, test_folder)
#     quadwrd_testb(L, test_folder)
#     fivewrd_testb(L, test_folder)
#
#     unitag_testb(L, test_folder)
#     bitag_testb(L, test_folder)
#     tritag_testb(L, test_folder)
#     quadtag_testb(L, test_folder)
#     fivetag_testb(L, test_folder)
#
#     # non-binary tests
#     unichar_test(L, test_folder)
#     bichar_test(L, test_folder)
#     trichar_test(L, test_folder)
#     quadchar_test(L, test_folder)
#     fivechar_test(L, test_folder)
#
#     uniwrd_test(L, test_folder)
#     biwrd_test(L, test_folder)
#     triwrd_test(L, test_folder)
#     quadwrd_test(L, test_folder)
#     fivewrd_test(L, test_folder)
#
#     unitag_test(L, test_folder)
#     bitag_test(L, test_folder)
#     tritag_test(L, test_folder)
#     quadtag_test(L, test_folder)
#     fivetag_test(L, test_folder)
