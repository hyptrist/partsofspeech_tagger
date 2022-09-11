def pos_tagging(sent):

  """
  Input is considered to be a sentence/paragraph which will be integrated with a different function which allows passing of list of sentences
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
