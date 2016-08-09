# 01-01: Implement an algorithm to determine if a string has all unique
# characters
# Example: Funny StorY => NO
# Example: Quick tall dog => YES

import unittest

class UniqueCharacterString:
    'Checks a string for duplicate characters'

    def __init__(self):
        self.character_map = [False] * 26
        return

    def __hash_character(self, c):
        # False values are bad, -1 values are okay but don't count
        char_num = ord(c.upper())
        if char_num == ord(' '):
            return -1
        elif char_num < ord('A'):
            return False
        elif char_num > ord('Z'):
            return False
        else:
            return ord(c.upper()) - ord('A')

    def hasUniqueChars(self, str):
        self.character_map = [False] * 26
        for char in str:
            char_hash = self.__hash_character(char)
            if char_hash is False:
                return False
            elif char_hash is not -1:
                if self.character_map[char_hash] is True:
                    return False
                else:
                    self.character_map[char_hash] = True

        return True

class TestUniqueCharacterString(unittest.TestCase):
    def setUp(self):
        self.testee = UniqueCharacterString()

    def test_hasspace(self):
        self.assertTrue(self.testee.hasUniqueChars('Lucky dog'))

    def test_hasnospace(self):
        self.assertTrue(self.testee.hasUniqueChars('Fun'))

    def test_shouldfail(self):
        self.assertFalse(self.testee.hasUniqueChars('Cool'))

    def test_shouldfailwithspaces(self):
        self.assertFalse(self.testee.hasUniqueChars('Cool looc'))

if __name__ == '__main__':
    unittest.main()
