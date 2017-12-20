# a3.py
# Saachi Gopal sg932
# 3/29/17
# skeleton by Lillian Lee (LJL2)

"""CS1110 assignment on processing and comparing text samples"""


import random
import a3given
import math # for the log function


# This function is the core of a3given.sample_from_source_file
def make_sample(textstring, label):
    """Returns: a new Sample where all its attributes are filled in correctly
    with respect to the string textstring.

    Preconditions: textstring is a nonempty string of English text.  Words are
    delimited by whitespace, are all lowercase, and all punctuation has been
    removed."""
    # STUDENTS: because we haven't talked about writing your own methods yet,
    # your function will be directly modifying the attributes of a Sample that
    # you create. This is UNORTHODOX python; later, you'll learn the "right"
    # way to do this, which involves writing the __init__ method for Sample.
    
    s = a3given.Sample()
    
    s.label = label
    s.text = textstring.split()
    s.length = len(textstring.split())
    
    s.unigram_counts = {}
    for x in s.text:
        if x not in s.unigram_counts:
            s.unigram_counts[x] = 1 
        else:
            s.unigram_counts[x] = s.unigram_counts[x] + 1
    
    s.bigram_dict = {}   
    for x in range(s.length - 1):
        nextvalue = s.text[x+1]
        if s.text[x] in s.bigram_dict:   
            s.bigram_dict[s.text[x]].append(nextvalue)
        else:
            s.bigram_dict[s.text[x]] = [nextvalue]
    
    s.trigram_dict = {}
    for x in range(s.length - 2):
        string = s.text[x] + ' ' + s.text[x+1]
        nextvalue = s.text[x+2]
        if string in s.trigram_dict:
            s.trigram_dict[string].append(nextvalue)
        else:
            s.trigram_dict[string] = [nextvalue]
   
    return s   
        
    
    # HINT: First, create a new Sample and set up the "easy" attributes.

    ## Using three separate passes through sample.text, for code simplicity
    ## Could have done one pass, with the unigram, bigram and trigram data
    ## updated simulataneously, but the code would probably be hard to read.

    # REQUIREMENT: fill in sample.unigram_counts by a for-loop through sample.text
    # HINT: Whether or not a key is already in sample.unigram_counts is important
    #       to check.

    # REQUIREMENT: Compile the bigram dictionary by going through all
    # possible bigram beginnings.
    # Note that a bigram cannot start at index sample.length-1 in sample.text

    # Compile the trigram dictionary by going through all possible trigram starts.
    # Note that a trigram can't start at index sample.length-2 in sample.text
    

def merge(samplelist, label):
    """Returns a new Sample whose text is the concatenation of the text for
    all the Samples in samplelist and whose label is <label>.

    Precondition: samplelist is a list of Samples of length >= 2.
    """
    assert len(samplelist) >= 2
    newtext = '' 
    for x in samplelist:
        for y in x.text:
            newtext = newtext + ' ' + y
            
    return make_sample(newtext, label)
    
    # Implementation hint: all you need to do is create the right text to feed
    # into make_sample.


def diffs(s1, s2, k):
    """Returns: [justs1, justs2, ranked], where
    justs1 is a list of words occurring at least k times in s1.text but never in s2.text
        (order doesn't matter);
    justs2 is a list of words occurring at least k times in s2.text but never in s1.text
        (order doesn't matter)
    ranked is a list of items [word, logprobratio] where word occurs in both s1.text
        and s2.text, and logratio is the score mentioned in the assignment
        handout, rounded to 3 decimal digits using round(f, 3) where f is a float
        The items in ranked are sorted by logprobratio, highest first.

    Precondition: s1 and s2 are Samples."""
    
    # HINT: first create justs1, justs2, and ranked as empty lists []
    justs1 = []
    justs2 = []
    ranked = []
    # HINT: first, loop through the keys of s1.unigram_counts
    # For each such word w, check whether it's in s2.unigram_counts.
    # If w isn't, if  and w occurs at least k times in s1.text, append it to justs1.
    # If it is, append [w, logratio] to ranked
  
    for x in s1.unigram_counts:
        if x not in s2.unigram_counts and s1.text.count(x) >= k:
            justs1.append(x)
        else:
            c1 = float(s1.text.count(x))
            c2 = float(s2.text.count(x))
            if c1 > 0 and c2 > 0:
                loglist = [x, round(math.log((c1 / s1.length)/(c2 / s2.length)),3)]
                ranked.append(loglist)
        
    # You can use "x in alist" and "y in adictionary" as boolean expressions
    # To get the log function, use math.log (using the default base)
    # HINT: then, check in s2.unigram_counts for words not in s1.unigram_counts
    
    for x in s2.unigram_counts:
        if x not in s1.unigram_counts and s2.text.count(x) >= k:
            justs2.append(x)
                     
    # HINT: there's a function you can use to sort ranked in module a3given.
   
    a3given.sort_weighted_list(ranked)
    
    # HINT: this should be your final line
    
    return [justs1, justs2, ranked]



def bigram_generation(s, k):
    """Returns <= k-token string according to the bigram dictionary of Sample s.
    Fewer than k tokens are generated if the generator chooses a token that
    is not followed by any token in s.text (in particular, the last token might
    have that property.)

    Preconditions: k>1 is an int."""
    
    ## STUDENTS: we start by picking the first token.
    # This line picks a random item from the list s.text and stores it in output
    output = random.choice(s.text)
    prev_word = output  # prev_word is always the most recently generated word

    ## STUDENTS: now finish the body of this function, using any hints or
    # requirements mentioned below.

    ## REQUIREMENT: use a for-loop to perform k-1 times the following:
    # if prev_word is in the bigram dictionary,
    # (1) choose the next word randomly from the dictionary entry for the
    #     previous word (since that's where the possible words to follow
    #     prev_word are stored)
    # (2) add the new next word to output
    # (3) since you're moving on to the next-next word, set prev_word to
    #     be the word you just selected.
    # But if prev_word is not in the bigram dictionary, do nothing in the loop.
    
    for x in range(k-1):
      if prev_word in s.bigram_dict:
          nextword = random.choice(s.bigram_dict[prev_word])
          output = output + ' ' + nextword
          prev_word = nextword
            
    return output

def trigram_generation(s, k):
    """Generate <= k-token string according to the trigram dictionary of Sample
    s.

    Fewer than k tokens are generated if the generator chooses a token that
    is not followed by any token in s.text (in particular, the last token might
    have that property.)

    Preconditions: k>2 is an int, s is a Sample."""

    # REQUIREMENT: first, randomly pick a starting bigram "w1 w2".
    # Then, remember that "w1 w2" were the two previously created words.
    # Then, use a for-loop to create the next k-2 words.
    # In the loop body,
    # (1) choose the next word w3 randomly from the list stored in the trigram
    #   dictionary for "w1 w2".
    # (2) do something to get w3 added to your output
    # (3) update the information you're storing so that you know that now "w2 w3"
    #   are the last two words generated.
    #
    prev_word = random.choice(s.text)
    w1index = s.text.index(prev_word)
    w2index= w1index + 2
    wordlist = s.text[w1index:w2index]
    output = wordlist[0] + ' ' + wordlist[1]
    
    for x in range(k-2): 
        startbigram = ' '.join(wordlist)
        if startbigram in s.trigram_dict:
            w3 = random.choice(s.trigram_dict[startbigram])
            output = output + ' ' + w3
            wordlist[0] = wordlist[1]
            wordlist[1] = w3
        
    return output
        
