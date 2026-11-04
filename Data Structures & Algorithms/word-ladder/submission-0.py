class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0
        q = deque([beginWord])
        visited = {beginWord}
        steps = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                for i in range(len(word)):
                    chars = list(word)
                    for letter in "abcdefghijklmnopqrstuvwxyz":
                        chars[i] = letter
                        new_word = "".join(chars)
                        if new_word in words and new_word not in visited:
                            if new_word == endWord:
                                return steps + 1
                            visited.add(new_word)
                            q.append(new_word)
            steps += 1
        return 0
        