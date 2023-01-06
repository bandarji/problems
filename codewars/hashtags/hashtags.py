TESTS = [
    ('Codewars', '#Codewars', 'Should handle a single word.'),
    ('Codewars      ', '#Codewars', 'Should handle trailing whitespace.'),
    ('      Codewars', '#Codewars', 'Should handle leading whitespace.'),
    ('Codewars Is Nice', '#CodewarsIsNice', 'Should remove spaces.'),
    ('codewars is nice', '#CodewarsIsNice', 'Should capitalize first letters of words.'),
    ('CoDeWaRs is niCe', '#CodewarsIsNice', 'Only the first letter of each word should be capitalized in the final hashtag, all other letters must be lower case.'),
    ('c i n', '#CIN', 'A single letter is considered to be a word of length 1, so should capitalize first letters of words of length 1.'),
    ('codewars  is  nice', '#CodewarsIsNice', 'Should deal with unnecessary middle spaces.'),
    ('', False, 'Expected an empty string to return False'),
    ('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat', False, 'Should return False if the final string is longer than 140 chars.'),
]


def generate_hashtag(s: str) -> str | None:
    if not s:
        return False
    assembled = "#" + "".join(w.title() for w in s.split())
    return False if len(assembled) > 140 else assembled


for test, expected, _ in TESTS:
    assert generate_hashtag(test) == expected
