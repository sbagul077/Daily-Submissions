class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        arr = ["" for i in range(26)]

        for letter in letters:
            arr[ord(letter) - ord("a")] = letter
        
        for i in range(26):

            if arr[i] != "" and ord(target) < ord(arr[i]):
                return arr[i]
        
        return letters[0]

#Time complexity: O(n)
# Space complexity: O(1)