# 01-01: Implement an algorithm to determine if a string has all unique
# characters
# Example: Funny StorY => NO
# Example: Quick tall dog => YES

class UniqueCharacterString:
    'Checks a string for duplicate characters'

    def __init__(self):
        self.character_map = [False] * 26
        return

    def __hash_character(self, c):
        # False values are bad, -1 values are okay but don't count
        if c < 'A':
            return False
        if c > 'Z' && c < 'a':
            return False
        if c > 'z':
            return False
        if c == ' ':
            return -1
        return ord(c.upper()) - 'A'

    def hasUniqueChars(self, str):
        for (char in str):
            char_hash = self.__hash_character(c)
            if (char_hash == False):
                return False
            if (char_hash != -1):
                if (self.character_map[char_hash] == True)
                    return False
                else
                    self.character_map[char_hash] = True

        return True




def has_unique_chars(str):
    "Returns true if a word has all unique characters"
    for char in str:



def hash_letter(character):
    "Hashes A-Za-z to [0-25]"
    if character < 'A':
        return False
    if character > 'Z' && character < 'a':
        return False
    if character > 'z':
        return False
    if character == ' ':
        return -1

    return ord(character.upper()) - 'A'



has_unique_chars('Funny story')
hash_letter('A')
