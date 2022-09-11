pip install flair
from flair.data import Sentence
from flair.models import SequenceTagger, MultiTagger
tagger = MultiTagger.load(['pos', 'ner'])