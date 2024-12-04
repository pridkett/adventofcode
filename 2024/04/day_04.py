from typing import List

class Solution:
    def __init__(self):
        pass

    def find_words_x(self, words: List[str], search_word: str) -> int:
        assert len(search_word)%2 == 1, "search word must be odd length"
        search_letter = search_word[len(search_word)//2]
        count = 0
        for i in range(len(words)):
            indices = [index for index, letter in enumerate(words[i]) if letter == search_letter]
            for idx in indices:
                valid = True
                word1 = search_letter
                word2 = search_letter
                for offset in range(1, len(search_word)//2+1):
                    if i - offset >= 0 and i + offset < len(words) and idx - offset >= 0 and idx + offset < len(words[i]):
                        word1 = words[i-offset][idx-offset] + word1 + words[i+offset][idx+offset]
                        word2 = words[i-offset][idx+offset] + word2 + words[i+offset][idx-offset]
                    else:
                        valid = False
                        break
                if valid and (search_word in word1 or search_word in word1[::-1]) \
                         and (search_word in word2 or search_word in word2[::-1]):
                    count = count + 1
        return count
                
    def find_words(self, words: List[str], search_word: str) -> int:
        # simple method - use python string processing
        count = 0
        # print("")

        # serach each row
        for line in words:
            # print(line + " " + line[::-1])
            count = count + line.count(search_word)
            count = count + line[::-1].count(search_word)
        
        # search each column
        for i in range(0, len(words[0])):
            column = "".join([x[i] for x in words])
            count = count + column.count(search_word)
            count = count + column[::-1].count(search_word)
        
        # print("")
        # search down right diagonal
        for row in range(0, len(words)):
            search_elems = [0]
            if row == 0:
                search_elems = range(0, len(words[row]))
            for col in search_elems:
                i, j = row, col
                word = ""
                bottom_word = ""
                while True:
                    word = word + words[i][j]
                    bottom_word = bottom_word + words[-1*(i+1)][j]
                    # print(-1*(i+1), j, bottom_word, words[-1*(i+1)][j])
                    i = i + 1
                    j = j + 1
                    if i >= len(words) or j >= len(words[i]):
                        break
                # print(row, col)
                # inc_count =  word.count(search_word) + word[::-1].count(search_word)
                # print(word + " " + word[::-1] + " " + str(inc_count))

                # inc_count =  bottom_word.count(search_word) + bottom_word[::-1].count(search_word)
                # print(bottom_word + " " + bottom_word[::-1] + " " + str(inc_count))

                count = count + word.count(search_word)
                count = count + word[::-1].count(search_word)

                count = count + bottom_word.count(search_word)
                count = count + bottom_word[::-1].count(search_word)
        
        # print("\n\n")
        return count
    

def main(fn: str):
    with open(fn) as f:
        data = [x.strip() for x in f.readlines()]
        s = Solution()
        result = s.find_words(data, "XMAS")
        print(result)
        result = s.find_words_x(data, "MAS")
        print(result)

if __name__ == "__main__":
    main("input.txt")