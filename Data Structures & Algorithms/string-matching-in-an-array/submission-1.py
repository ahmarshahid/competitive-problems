class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        words.sort(key=len)
        for i in range(len(words)):
            for j in range(1+i,len(words)):
                if words[i] in words[j]:
                    result.append(words[i])
                    break
        return result
