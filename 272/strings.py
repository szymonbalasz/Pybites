from typing import List


def common_words(sentence1: List[str], sentence2: List[str]) -> List[str]:
    """
    Input:  Two sentences - each is a  list of words in case insensitive ways.
    Output: those common words appearing in both sentences. Capital and lowercase 
            words are treated as the same word. 

            If there are duplicate words in the results, just choose one word. 
            Returned words should be sorted by word's length.
    """
    result = []
    sentence1 = [word.lower() for word in sentence1]
    sentence2 = [word.lower() for word in sentence2]
    for word in sentence1:
        if word in sentence2 and word not in result:
            result.append(word)
    return sorted(result, key=len)
