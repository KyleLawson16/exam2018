def get_score_dict():
    dict = {}
    val = 1
    for i in range(26):
        dict[chr(97 + i)] = val
        val += 1
    return dict

def get_names(filename):
    fp = open(filename)
    names = [line.split()[0].lower() for line in fp if line != '']
    return names

def score_word(word):
    score_dict = get_score_dict()
    score = 0
    for i in word:
        if i in score_dict:
            score += score_dict[i]
    return score

def score_names(names):
    scored_names = {}
    for name in names:
        scored_names[name] = score_word(name)
    return scored_names

def find_matching_words(filename, score):
    fp = open(filename)
    words = [line.split()[0].lower() for line in fp if line != '']
    matching_words = [word for word in words if score_word(word) == score]
    return matching_words

def main():
    score_dict = get_score_dict()
    names = get_names('roster.txt')
    scores = score_names(names)
    print('The most valuable person in our class is:')
    print(max(scores, key=scores.get))

    matching_words = find_matching_words('positive-words.txt', scores['kyle'])
    print('Positive words matching my name are:')
    for word in matching_words:
        print(word)

if __name__ == '__main__':
    main()
