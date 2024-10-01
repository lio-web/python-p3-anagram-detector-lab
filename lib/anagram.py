# your code goes here!


class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, candidates):
        """Return a list of anagrams from the candidates."""
        # Create a sorted version of the original word
        sorted_word = sorted(self.word)
        matches = []
        
        # Iterate through the list of candidates
        for candidate in candidates:
            # Check if the sorted candidate is the same as the sorted original word
            if sorted(candidate) == sorted_word:
                matches.append(candidate)  # If so, add it to the matches list
        
        return matches
