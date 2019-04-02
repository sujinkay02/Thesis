# Sujin Kay
# Senior Thesis/Project

import os       # accessing data files on computer
import pickle   # for pickling / storing data
import nltk     # NLTK package
from nltk.util import ngrams    # to compute n-grams
from collections import Counter # to count n-gram frequencies

"""
Pre-Experimentation: Normalized frequency distributions
"""

def word_freq(feature_list, top):
    male = {}
    female = {}
    nonbinary = {}

    # Male
    a = open('m_uniwrd', 'rb')
    aa = pickle.load(a)
    a.close()

    for feature in feature_list:
        for (k, v) in aa[0].most_common(top):
            f = "\'" + feature + "\'"
            if f in str(k).lower():
                # normalized frequency (as a %)
                male[k] = (v / aa[1] * 100)

    # Female
    a = open('f_uniwrd', 'rb')
    aa = pickle.load(a)
    a.close()

    for feature in feature_list:
        for (k, v) in aa[0].most_common(top):
            f = "\'" + feature + "\'"
            if f in str(k).lower():
                # normalized frequency
                female[k] = (v / aa[1] * 100)

    # Non-Binary
    a = open('n_uniwrd', 'rb')
    aa = pickle.load(a)
    a.close()

    for feature in feature_list:
        for (k, v) in aa[0].most_common(top):
            f = "\'" + feature + "\'"
            if f in str(k).lower():
                # normalized frequency
                nonbinary[k] = (v / aa[1] * 100)

    return male, female, nonbinary
def relative_freq(feature_list, top):
    male = {}
    female = {}
    nonbinary = {}

    for f in feature_list:
        print(f)

    # Male
    a = open('m_uniwrd', 'rb')
    aa = pickle.load(a)
    a.close()

    print ("Male")
    for feature in feature_list:
        for (k, v) in aa[0].most_common(top):
            if feature in k:
                print (k)
                # normalized frequency (as a %)
                print (v / aa[1] * 100)

    # Female
    a = open('f_uniwrd', 'rb')
    aa = pickle.load(a)
    a.close()

    print ("Female")
    for feature in feature_list:
        for (k, v) in aa[0].most_common(top):
            if feature in k:
                print (k)
                # normalized frequency (as a %)
                print (v / aa[1] * 100)

    # Non-Binary
    a = open('n_uniwrd', 'rb')
    aa = pickle.load(a)
    a.close()

    print ("Non-Binary")
    for feature in feature_list:
        for (k, v) in aa[0].most_common(top):
            if feature in k:
                print (k)
                # normalized frequency (as a %)
                print (v / aa[1] * 100)

    return
def top_features(male, female, nonbinary, top):
    print ("Male")
    a = Counter(male)
    for feature in a.most_common(top):
        print (feature[0])
    for feature in a.most_common(top):
        print (feature[1])

    print ("Female")
    b = Counter(female)
    for feature in b.most_common(top):
        print (feature[0])
    for feature in b.most_common(top):
        print (feature[1])

    print ("Non-Binary")
    c = Counter(nonbinary)
    for feature in c.most_common(top):
        print (feature[0])
    for feature in c.most_common(top):
        print (feature[1])

    return


"""
Compute simple dissimilarity measure between author text and gender profiles
"""
# nonbinary classification
# author_profile and gender_profiles is the n-grams output (dictionary)
def dissimilarity(author_profile, author_ngram_count, male_profile, male_ngram_count, female_profile, female_ngram_count, nonbin_profile, nonbin_ngram_count, feature_set):
    # code adapted from:
    # https://github.com/starfirerhf/optimized_stam_07/blob/master/stamatatos_tweaked.py
    dissimilarity_male = 0
    dissimilarity_female = 0
    dissimilarity_nonbin = 0

    # compare Author to Male Profile
    full_feature_set = set(author_profile.keys() | male_profile.keys())

    for feature in feature_set:
        # calculate NORMALIZED frequencies
        # return 0 if key not in dictionary
        for full_feature in full_feature_set:
            if feature in full_feature:
                f1 = float(author_profile.get(full_feature, 0)) / author_ngram_count
                f2 = float(male_profile.get(full_feature, 0)) / male_ngram_count

                # dissimilarity formula
                dissimilarity_male += (2 * (f1 - f2) / (f1 + f2)) ** 2

    # compare Author to Female Profile
    full_feature_set = set(author_profile.keys() | female_profile.keys())

    for feature in feature_set:
        for full_feature in full_feature_set:
            # calculate NORMALIZED frequencies
            if feature in full_feature:
                f1 = float(author_profile.get(full_feature, 0)) / author_ngram_count
                f2 = float(female_profile.get(full_feature, 0)) / female_ngram_count

                # dissimilarity formula
                dissimilarity_female += (2 * (f1 - f2) / (f1 + f2)) ** 2

    # compare Author to Non-binary Profile
    full_feature_set = set(author_profile.keys() | nonbin_profile.keys())

    for feature in feature_set:
        for full_feature in full_feature_set:
            # calculate NORMALIZED frequencies
            if feature in full_feature:
                f1 = float(author_profile.get(full_feature, 0)) / author_ngram_count
                f2 = float(nonbin_profile.get(full_feature, 0)) / nonbin_ngram_count

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
FEATURE SELECTION
"""
def feature_set1():
    # choose a bunch of features
    features = []

    pronouns = ['I', 'me', 'we', 'us', 'you', 'myself']
    gender_pronouns = ['he', 'him', 'his', 'she', 'her', 'they', 'them', 'their']
    determiners = ['A', 'a', 'the', 'it', 'an', 'The', 'what', 'which']
    possessives = ['my', 'your', 'its', 'our', 'whose']
    demonstratives = ['this', 'that', 'these', 'those']
    conjunctions = ['for', 'and', 'nor', 'but', 'or', 'yet', 'so']
    prepositions = ['of', 'in', 'to', 'with', 'on', 'at', 'from', 'by', 'about', 'as', 'into', 'like', 'through', 'after', 'over', 'between', 'out', 'against', 'during', 'without', 'before', 'under', 'around', 'among']
    assent = ['yes', 'yeah', 'yea', 'yup', 'okay', 'sure', 'yep']
    dissent = ['stop', 'no', 'nope', 'nah', 'never']
    neg_emotions = ['sad', 'mad', 'angry', 'depressed', 'unhappy', 'lonely', 'hate']
    pos_emotions = ['happy', 'excited', 'glad', 'joy', 'hope', 'pride', 'love', 'joyful', 'hopeful', 'proud']
    punctuation = ['!', '?', '&', '...', ')', '(', ':', '-', ';']
    abbrev = ['lol', 'u', 'haha']
    numerals = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    ordinals = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth']
    quantifiers = ['all', 'few', 'several', 'multiple', 'many', 'lot', 'some', 'much', 'any']
    kinship = ['mom', 'dad', 'mother', 'father', 'mommy', 'daddy', 'uncle', 'aunt', 'cousin', 'sister', 'brother', 'child', 'baby', 'children', 'kid', 'kids', 'daughter', 'son', 'niece', 'nephew', 'friend', 'bestie', 'bff', 'bro', 'sis', 'bros', 'bud', 'buddy', 'buddies', 'friends', 'family', 'parents']
    swear = ['damn', 'shit', 'fuck', 'dammit', 'crap', 'hell', 'bullshit', 'ass', 'asshole', 'bitch', 'bitches', 'assholes', 'stupid']
    nonbin = ['nonbinary', 'non-binary', 'cisgender', 'cis', 'queer', 'trans', 'transgender', 'identity', 'binary', 'gender', 'pronoun', 'pronouns', 'girl', 'boy', 'man', 'woman', 'male', 'female']

    # choose the features to include in the set
    # features.extend(pronouns)
    features.extend(gender_pronouns)
    # features.extend(determiners)
    # features.extend(possessives)
    # features.extend(demonstratives)
    # features.extend(conjunctions)
    # features.extend(prepositions)
    # features.extend(assent)
    # features.extend(dissent)
    # features.extend(neg_emotions)
    # features.extend(pos_emotions)
    # features.extend(punctuation)
    # features.extend(abbrev)
    # features.extend(numerals)
    # features.extend(ordinals)
    # features.extend(quantifiers)
    # features.extend(swear)
    # features.extend(kinship)

    return features

"""
TESTS
"""
def nonbin_tests(_L, _test_folder, _feature_set):
    def uniwrd_test(L, test_folder, feature_set):
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
                guess = dissimilarity(author_profile, author_ngram_count, male_profile, male_ngram_count, female_profile, female_ngram_count, nonbin_profile, nonbin_ngram_count, feature_set)

                # record accuracy
                acc += accuracy(guess, testfile)


        # calculate total accuracy
        print ("Word Unigrams for L=", L, "\n")
        print ("Overall accuracy over", num_tests, "tests:", acc / num_tests)
        return
    def biwrd_test(L, test_folder, feature_set):
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
                guess = dissimilarity(author_profile, author_ngram_count, male_profile, male_ngram_count, female_profile, female_ngram_count, nonbin_profile, nonbin_ngram_count, feature_set)

                # record accuracy
                acc += accuracy(guess, testfile)

        # calculate total accuracy
        print ("Word Bigrams for L=", L, "\n")
        print ("Overall accuracy over", num_tests, "tests:", acc / num_tests)
        return
    def triwrd_test(L, test_folder, feature_set):
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
                guess = dissimilarity(author_profile, author_ngram_count, male_profile, male_ngram_count, female_profile, female_ngram_count, nonbin_profile, nonbin_ngram_count, feature_set)

                # record accuracy
                acc += accuracy(guess, testfile)

        # calculate total accuracy
        print ("Word Trigrams for L=", L, "\n")
        print ("Overall accuracy over", num_tests, "tests:", acc / num_tests)
        return

    # uniwrd_test(_L, _test_folder, _feature_set)
    # biwrd_test(_L, _test_folder, _feature_set)
    triwrd_test(_L, _test_folder, _feature_set)

    return


"""---------------------------------------------------------------------------
MAIN
----------------------------------------------------------------------------"""

# this folder holds all of the test data files
# NOTE: Python program MUST be saved in the same directory, otherwise pickled data can't be loaded
test_folder = "/Users/skay/Desktop/Thesis/ALLP_TESTFILES"


"""
TESTING
"""
# Choose feature set
fset = feature_set1()

final_features = ['he', 'his', 'her', 'they', 'them', 'their', 'you', 'me', 'we', 'my', 'your', 'our', 'the', 'a', 'it', 'that', 'this', 'This', 'these', 'and', 'for', 'but', 'so', 'or', 'to', 'of', 'in', 'sure', 'yeah', 'yes', 'Yes', 'no', 'never', 'No', 'hate', 'sad', 'mad', 'angry', 'love', 'hope', 'happy', '...', '!', '?', 'u', 'lol', 'haha', 'Haha', 'one', 'two', '2', 'One', 'first', 'second', 'third', 'First', 'all', 'some', 'much', 'many', 'friends', 'friend', 'family', 'mom', 'shit', 'hell', 'stupid', 'man', 'girl', 'woman', 'gender', 'trans', 'non-binary']


# Test across n-grams size and various sizes of L
# for L in L_sizes:
nonbin_tests(10000, test_folder, final_features)

# Determine top n features in gender profiles (take union for final feature set)
# male, female, nonbinary = word_freq(fset, 5000)
# top_features(male, female, nonbinary, 3)
# relative_freq(final_features, 5000)
