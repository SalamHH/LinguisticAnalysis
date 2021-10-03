import nltk

# Load corpus
brown = nltk.corpus.brown.tagged_words()

# Frequency distribution of words by parts of speech
brown_tagged_freq = nltk.ConditionalFreqDist([(tag, word) for (word, tag) in brown])

# Probability of a word given a part of speech
conditional_prob_emission = nltk.ConditionalProbDist(brown_tagged_freq, nltk.MLEProbDist)

# Tag bigrams from brown corpus
tag_bigrams = nltk.bigrams([tag for (word, tag) in brown])

# Frequency distribution of tags by previous tags
bigram_freq = nltk.ConditionalFreqDist(tag_bigrams)

# Probability of a tag given a previous tag
conditional_prob_transition = nltk.ConditionalProbDist(bigram_freq, nltk.MLEProbDist)

# Del 2

# Input texts
text1 = [('saw', 'VBD'), ('her', 'PP$'), ('duck', 'NN')]
text2 = [('saw', 'VBD'), ('her', 'PPO'), ('duck', 'VB')]


# Tag sequence probability calculator
def calculate_tag_prob(text, transiotion_prob, emission_prob):
    result = 1
    bigrams = nltk.bigrams([tag for (word, tag) in text])
    for bigram in bigrams:
        result *= transiotion_prob[bigram[0]].prob(bigram[1])
    for word, tag in text:
        result *= emission_prob[tag].prob(word)
    return result


if __name__ == '__main__':

    ########
    # Demo #
    ########

    # Del 1
    # 2(a)
    print('Most frequent noun is: {p[0]}.\n'.format(p=brown_tagged_freq['NN'].most_common()[0]))
    # 2(b)
    print('Number of occurrences for noun "linguist": {}.\n'.format(brown_tagged_freq['NN']['linguist']))
    # 2(c)
    print('Most frequent adjective: {p[0]}.\n'.format(p=brown_tagged_freq['JJ'].most_common()[0]))
    # 3
    print('Most probable adjective: {}.\n'.format(conditional_prob_emission['JJ'].max()))
    print('Probability of "new" given "JJ": {:.4f}.\n'.format(conditional_prob_emission['JJ'].prob('new')))
    # 5(a)
    print('"NN" is most often followed by {}.\n'.format(bigram_freq['NN'].most_common()[0]))
    # 5(b)
    print('Number of occurrences of bigram "DT NN": {}.\n'.format(bigram_freq['DT']['NN']))
    # 6(a)
    print('The probability of "NN" given "DT": {}.\n'.format(conditional_prob_transition['DT'].prob('NN')))
    # Del 2
    print('*' * 10)
    p1 = calculate_tag_prob(text1, conditional_prob_transition, conditional_prob_emission)
    print("Probability of ('saw', 'VBD'), ('her', 'PP$'), ('duck', 'NN'): {}.\n".format(p1))
    p2 = calculate_tag_prob(text2, conditional_prob_transition, conditional_prob_emission)
    print("Probability of ('saw', 'VBD'), ('her', 'PPO'), ('duck', 'VB'): {}.\n".format(p2))
    print('Second sequence is more probable: {}.'.format(p1 < p2))
