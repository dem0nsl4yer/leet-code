class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        conj = ".,;?!' "
        b = {}
        j = ''
        for i in paragraph:
            if i in conj:
                if j:
                    k = j.lower()
                    if k not in banned:
                        if k in b:
                            b[k] += 1
                        else:
                            b[k] = 1
                j = ''
            elif i not in conj:
                j += i

        # Check for the last word in the paragraph
        if j:
            k = j.lower()
            if k not in banned:
                if k in b:
                    b[k] += 1
                else:
                    b[k] = 1

        # Find the word with the maximum count
        most_frequent_word = ''
        max_count = 0
        for word, count in b.items():
            if count > max_count:
                most_frequent_word = word
                max_count = count

        return most_frequent_word


#######################
#### faster ##########
#####################

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        ignore = ['!','?',',',';',"'",'.','"','.']

        for char in ignore:
            paragraph = paragraph.replace(char, ' ')

# once replacements are over, count vals
        words = Counter(paragraph.lower().split())

        res = []
        count = 0
        for word, cnt in words.items():
            if word in banned:
                continue
            if cnt > count:
                count = cnt
                res = word
                
        return str(res)

