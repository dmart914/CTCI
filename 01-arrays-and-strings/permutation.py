# 1-3: Given two strings, write a method to decide if one is a permutation
#      of the other
# Permutation: an ordered set that uses the same elements as another

# Example: cat act

# Brute force: for each letter in word1, see if that letter exists in word2
# If yes, remove that letter from the word2. If you get to the end of word1 and
# there are 0 or more letters left, return True
# Worst case: n^2

# Hash
# For each letter in word1, hash. Add 1 at hash for each letter
# For each letter in word2, hash. If zero, return false. Otherwise, subtract 1

class PermutationChecker:
    'Checks two strings to see if one is a permutation of the second'

    def __init__(self):
        self.character_map = [False] * 26
        return

    def __hash_character(self, c):
        char_num = ord(c.upper())
        if char_num == ord(' '):
            return -1
        elif char_num < ord('A'):
            return False
        elif char_num > ord('Z'):
            return False
        else:
            return char_num - ord('A')

    def __add_to_map(self, c):
        char_num = self.__hash_character(c)
        if char_num is False:
            return False
        elif char_num is not -1:
            self.character_map[char_num] += 1
            return True

    def __subtract_from_map(self, c):
        char_num = self.__hash_character(c)
        if char_num is False:
            return False
        elif char_num is not -1:
            if self.character_map[char_num] is 0:
                return False
            else:
                self.character_map[char_num] -= 1
                return True

    def isPerm(self, str1, str2):
        if len(str2) > len(str1):
            return False
        else:
            # hash first word
            for char in str1:
                result = self.__add_to_map(char)
                if result is False:
                    print('str1 false')
                    return False

            # hash second word
            for char in str2:
                result = self.__subtract_from_map(char)
                if result is False:
                    return False

        return True

a = PermutationChecker()
print(a.isPerm('cat', 'act'))
print(a.isPerm('tack', 'kack'))
