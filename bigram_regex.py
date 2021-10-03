#opg3
import numpy as np
import nltk
from nltk.corpus import brown
from nltk.corpus import gutenberg
from collections import Counter
from nltk import bigrams, trigrams
from collections import defaultdict
import random

#1

bible_words = gutenberg.words("bible-kjv.txt")
total_words=len(bible_words)
print("det er " ,(total_words) , " tokens i teksten")


#2
distinct_words = []
for w in bible_words:
    distinct_words.append(w.lower())

total_distinct_words = len(set(distinct_words))
print("det er ", (total_distinct_words) , " typer i teksten")

#3
fd_bible_words=Counter(bible_words)
common_words=("most common words: ", fd_bible_words.most_common(20))
print(common_words)

#testttttt
print("######\n")
probabilities = {}
for word, count in fd_bible_words.items():
    probabilities[word] = count/total_words



text = np.random.choice(list(probabilities.keys()), 20, p=list(probabilities.values()))
print(text)



#4
print("frequency of 'heaven': ", fd_bible_words["heaven"])
print("frequency of 'death': ", fd_bible_words["death"])
print("frequency of 'life': ", fd_bible_words["life"])

#5
bible_sents=gutenberg.sents("bible-kjv.txt")
fourth_sentence=bible_sents[3]
print(list(bigrams(fourth_sentence, pad_left=True, pad_right=True)))

#6
bible_sents=gutenberg.sents("bible-kjv.txt")
fifth_sentence=bible_sents[4]
print(list(trigrams(fifth_sentence, pad_left=True, pad_right=True)))


#7

bigram_counts = defaultdict(lambda: defaultdict(lambda: 0))
bigram_model = defaultdict(lambda: defaultdict(lambda: 0.0))


for sentence in bible_sents:
    for w1, w2 in bigrams(sentence, pad_right= True, pad_left = True):
        bigram_counts[w1][w2] += 1

print(bigram_counts[None]["Thett"])



for w1 in bigram_counts:
    total_bigramcount = sum(bigram_counts[w1].values())
    for w2 in bigram_counts[w1]:
        bigram_model[w1][w2] =bigram_counts[w1][w2]/total_bigramcount


print(bigram_model["havehhhh"]["sent"])
print("#####\n")




#OPPGAVE 4
#A OG B)
brown_tagged_sents = brown.tagged_sents(categories='fiction')
brown_sents = brown.sents(categories='fiction')



patterns = [

     (r'.*est$', 'ADS...'),                  #adjective superlative
     (r'.*er$','ADC...'),                    #adjective comparative
     (r'.*ly$', 'ADV...'),                    #adverb som ender på ly
     (r'.*tion$', 'NOU...'),                   #subtantiv som ender på tion
     (r'.*able$', 'VAD...'),                #adjective derived from verb
     (r'.*ship$', 'POS...'),                #posisjon holdt, substantiv
     (r'.*ness$', 'SOB...'),                 #'state of being', substantiv
     (r'.*ity$', 'NAD...'),                 #Substantiv som kommer fra adjektiv
     (r'.*ee$', 'SUB....'),                 #substantiv som ender med ee
     (r'.*self$', 'REF...'),                #reflxive pronoun
     (r'\bthe\b', 'DET'),                     #bestemmer. matcher ordet "the"
     (r'.*ing$', 'VBG'),                # gerunds
     (r'.*ed$', 'VBD'),                 # simple past
     (r'.*es$', 'VBZ'),                 # 3rd singular present
     (r'.*ould$', 'MD'),                # modals
     (r'.*\'s$', 'NN$'),                # possessive nouns
     (r'.*s$', 'NNS'),                  # plural nouns
     (r'^-?[0-9]+(\.[0-9]+)?$', 'CD'),  # cardinal numbers
     (r'.*', 'NN'),                      # nouns (default)

 ]




regexp_tagger = nltk.RegexpTagger(patterns)
eksempler=regexp_tagger.tag(["hardest", "harder", "clearly", "caption", "likeable", "partnership", "hapiness","activity", "employee", "herself", "the"])
print(eksempler)

noyaktighet=regexp_tagger.evaluate(brown_tagged_sents)
print(noyaktighet)




#C)
with open('testsetninger.txt', "r") as word_list:
    words = word_list.read().split(' ')

res=regexp_tagger.tag(words)
print(res)
