# tokenizer

'''
tokenizer_en = tfds.features.text.SubwordTextEncoder.build_from_corpus(
    corpus_en, target_vocab_size=2**13)
tokenizer_fr = tfds.features.text.SubwordTextEncoder.build_from_corpus(
    corpus_fr, target_vocab_size=2**13)
	
VOCAB_SIZE_EN = tokenizer_en.vocab_size + 2 # = 8190
VOCAB_SIZE_FR = tokenizer_fr.vocab_size + 2 # = 8171

inputs = [[VOCAB_SIZE_EN-2] + tokenizer_en.encode(sentence) + [VOCAB_SIZE_EN-1]
          for sentence in corpus_en]
outputs = [[VOCAB_SIZE_FR-2] + tokenizer_fr.encode(sentence) + [VOCAB_SIZE_FR-1]
           for sentence in corpus_fr]
		   
'''