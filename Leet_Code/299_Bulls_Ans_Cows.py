from collections import Counter

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        secret_with_removed_bulls = ""
        guess_with_removed_bulls = ""
        
        bulls = 0
        cows = 0
        
        for i in range(len(secret)):
            if(secret[i] == guess[i]):
                bulls += 1
            else:
                secret_with_removed_bulls  = secret_with_removed_bulls + secret[i]
                guess_with_removed_bulls = guess_with_removed_bulls + guess[i]
        
        freq_secret_with_removed_bulls = Counter(secret_with_removed_bulls)
        freq_guess_with_removed_bulls = Counter(guess_with_removed_bulls)
        
        for key in freq_secret_with_removed_bulls:
            if(key in freq_guess_with_removed_bulls):
                cows = cows + min(freq_guess_with_removed_bulls[key],freq_secret_with_removed_bulls[key])
        return(str(bulls)+"A"+str(cows)+"B")