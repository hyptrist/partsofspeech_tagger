def pos_tagging(sent):

  """
  Parameters - sent
  Input is considered to be a sentence/paragraph which will be integrated with a different function which allows passing of list of sentences
  
  Output - result
  {word : POS_Tag + % accuracy}
  """
  pos_tags = []
  for i in sentences:
    sentence = Sentence(i)
    tagger.predict(sentence)
    for entity in sentence.get_spans('pos'):
      pos_tags.append(entity.labels)

  words = sent.split()

  result = dict(zip(words, pos_tags))

  return result

def postags_(list_):
      
  """
  Input = list_
  list_ holds list of sentences that we can pass to get pos tags

  Output - results
  [{},{}] Results of different sentences are appended in a single list
  To find result of a sentence at the i'th position, one might pass "postags_(list_)[i]"
  """
    
  results = []
  for sent in list_:
    res = pos_tagging(sent)
    results.append(res)

  return results
