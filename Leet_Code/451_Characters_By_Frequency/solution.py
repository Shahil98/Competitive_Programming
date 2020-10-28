from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:

        final_string = ""
        freq_counter = Counter(s)

        for char in sorted(freq_counter,key=freq_counter.get,reverse=True):
            for i in range(freq_counter[char]):
                final_string = final_string + char
        return(final_string)