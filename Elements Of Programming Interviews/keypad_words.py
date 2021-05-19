class Solution:
    def __init__(self):
        self.cache = {}
        self.mapping = {'2': ['A', 'B', 'C'], '3': ['D', 'E', 'F'], '4': ['G', 'H', 'I'], '5': ['J', 'K', 'L'], '6': ['M', 'N', 'O'], '7':['P', 'Q', 'R', 'S'], '8':['T', 'U', 'V'], '9':['W', 'X', 'Y', 'Z']}

    def phone_words(self, s: str):
        if len(s) == 0:
            return ''
        elif len(s) == 1:
            return self.mapping[s]
        elif s in self.cache:
            return self.cache[s]
        words = []
        if s[0] in self.mapping:
            for w in self.phone_words(s[1:]):
                for c in self.mapping[s[0]]:
                    words.append(c + w)
        self.cache[s] =  words
        return words


s = Solution()
print(s.phone_words('22'))


