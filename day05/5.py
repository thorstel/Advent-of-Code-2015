with open('input.txt', 'r') as file:
    data = file.read().splitlines()

vowels = 'aeiou'
bad_words = ['ab', 'cd', 'pq', 'xy']

def part1_good(word):
    if any(bad in word for bad in bad_words):
        return False
    vowel_count = sum(1 for c in word if c in vowels)
    twice = any(a == b for a, b in zip(word, word[1:]))
    return vowel_count >= 3 and twice

def part2_good(word):
    between = any(a == b for a, _, b in zip(word, word[1:], word[2:]))
    no_overlap = any(word[i:i+2] in word[i+2:] for i in range(len(word) - 1))
    return no_overlap and between

print(sum(1 for word in data if part1_good(word)))
print(sum(1 for word in data if part2_good(word)))
