from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Helper function to check if two frequency counters are the same
        def same_Freq_Dict(d1: Counter, d2: Counter) -> bool:
            for ch, freq in d1.items():
                # Check if character is missing or has different frequency
                if ch not in d2 or d2[ch] != freq:
                    return False
            return True

        # Create a frequency counter for s1
        d1 = Counter(s1)
        left_Ptr, right_Ptr = 0, len(s1)

        # Slide the window across s2
        while left_Ptr <= len(s2) - len(s1):
            # Get the current substring from s2 using the window defined by pointers
            current_Word = s2[left_Ptr:right_Ptr]
            # Create a frequency counter for the current substring
            d2 = Counter(current_Word)

            # Check if the frequency counters match
            if same_Freq_Dict(d1, d2):
                return True

            # Move the window one character to the right
            left_Ptr += 1
            right_Ptr += 1
        
        # If no matching permutation found, return False
        return False

# Time Complexity: O(n * m), where n is the length of s2 and m is the length of s1.
# In the worst case, we create a Counter for each window of length m in s2.

# Space Complexity: O(m), where m is the length of s1.
# We need space for the frequency counters d1 and d2.