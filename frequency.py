import nltk

brown = nltk.corpus.brown.tagged_words(categories='news')
#brown = nltk.corpus.brown.tagged_words()

# 1.3
def frequency_counter(input_data, check='word'):
    word_dict = {}

    if check == 'word':
        for i in input_data:
            if i[0].lower() not in word_dict:
                word_dict[i[0].lower()] = 1
            else:
                word_dict[i[0].lower()] += 1

    elif check == 'class':
        for i in input_data:
            if i[1] not in word_dict:
                word_dict[i[1]] = 1
            else:
                word_dict[i[1]] += 1
    return word_dict


# 1.3
def sort_items_by_frequency(input_data, rev=True):
    sorted_input_data = sorted(input_data.items(), key=lambda x: x[1], reverse=rev)
    return sorted_input_data


# 2, 2
def multiple_class_finder(input_data):
    word_dict = {}
    for i in input_data:
        temp_value = set()
        if i[0].lower() not in word_dict:
            temp_key = i[0].lower()
            temp_value.add(i[1])
            word_dict[temp_key] = temp_value
        elif i[0].lower() in word_dict:
            word_dict[i[0].lower()].add(i[1])
    return word_dict


# 2, 2
def count_multiclass_words(input_data):
    multi_class_words = [key for key in input_data if len(input_data[key]) > 1]
    return multi_class_words, len(multi_class_words)


# 2, 3
def sort_items_by_no_of_classes(input_data, rev=True):
    sorted_input_data = sorted(input_data.items(), key=lambda x: len(x[1]), reverse=rev)
    return sorted_input_data


# 2, 4
def freqs(w, brown):
    tag_dict = {}
    for token in brown:
        if w.lower() == token[0].lower() and token[1] in tag_dict:
            tag_dict[token[1]] += 1
        elif w.lower() == token[0].lower() and token[1] not in tag_dict:
            tag_dict[token[1]] = 1
    print('Word "{}" is found with the following tags'.format(w))
    for key, value in tag_dict.items():
        print('{}: {}'.format(key, value))


if __name__ == '__main__':


# 1.3, 1
    print('Output for task 1.3, 1')
    freq_dic_word = frequency_counter(brown, check='word')
    freq_dic_word_sroted = sort_items_by_frequency(freq_dic_word, rev=True)
    print('The most frequent word is "{p[0]}".\nWe found it {p[1]} times.'.format(p=freq_dic_word_sroted[0]))

# 1.3, 2
    print('\nOutput for task 1.3, 2')
    freq_dic_class = frequency_counter(brown, check='class')
    freq_dic_word_class = sort_items_by_frequency(freq_dic_class, rev=True)
    print('The most frequent class is "{p[0]}".\nWe found it {p[1]} times.'.format(p=freq_dic_word_class[0]))

# 1.3, 3
    print('\nOutput for task 1.3, 3')
    print('The least frequent class is "{p[0]}".\nWe found it {p[1]} times.'.format(p=freq_dic_word_class[-1]))

# 2, 2
    print('\nOutput for task 2, 2')
    multi_class_words_dict = multiple_class_finder(brown)
    multi_class_words_list, multi_class_words_count = count_multiclass_words(multi_class_words_dict)
    print('There are {} multiclass words in Brown.'.format(multi_class_words_count))

# 2, 3
    print('\nOutput for task 2, 3')
    multi_class_words_sorted = sort_items_by_no_of_classes(multi_class_words_dict)
    word_with_most_classes = multi_class_words_sorted[0][0]
    no_class_for_word = len(multi_class_words_sorted[0][1])
    print('The word with most classes is "{}".\n'
          'It belongs to the following no. of classes: {}'.format(word_with_most_classes, no_class_for_word))

# 2, 5
    print('\nOutput for task 2, 5')
    freqs('new', brown)

    #freq_dic_class = frequency_counter(brown, check='word')
    #print(sort_items_by_frequency(freq_dic_class, rev=True))
    print(freq_dic_class['JJ'])
    print({item for item in brown if item[1] == 'WDT'})
