def word_tagging(sentence):
    import nltk
    lst = []

    #converting each sentence to word list
    tokens = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokens)
    lst = tagged[0:len(sentence)]
    return lst

def extracting_ProperNoun(sentence):
  #NNP for proper noun
  #https://pythonprogramming.net/part-of-speech-tagging-nltk-tutorial/
    lst = word_tagging(sentence)
    for key,val in (lst):
        if val == 'NNP':
            print(key)



#word_tagging("At Eight o' clock on morning I Arpitansh and Aditya and twenty-four are feeling very pleased why and how")
