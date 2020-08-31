from typing import List


def common_words(sentence1, sentence2) -> List[str]:
    sentence1_set = set(map(str.lower, sentence1))
    sentence2_set = set(map(str.lower, sentence2))
    commons = sentence1_set & sentence2_set
    return sorted(commons, key=len)
