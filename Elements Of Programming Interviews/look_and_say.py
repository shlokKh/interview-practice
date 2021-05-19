class Solution():
    def __init__(self):
        self.cache = ['1']

    def look_and_say(self, n : int):

        if len(self.cache) < n:
            for i in range(len(self.cache)-1, n-1):
                number = self.cache[i]
                j = 0
                new_num = ''
                while j < len(number):
                    group_count = 1
                    while j+1 < len(number) and number[j+1] == number[j]:
                        group_count += 1
                        j += 1
                    new_num += str(group_count) + number[j]
                    j += 1
                self.cache.append(new_num)
        return self.cache[n-1]


s = Solution()
print(s.look_and_say(8))


