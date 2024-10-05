from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def same_Freq_Dict(d1: Counter, d2: Counter) -> bool:
            for ch, freq in d1.items():
                if ch not in d2 or d2[ch] != freq:
                    return False
            return True

        # Create a frequency counter for s1
        d1 = Counter(s1)
        left_Ptr = 0
        right_Ptr = left_Ptr + len(s1)
        d2 = Counter(s2[left_Ptr:right_Ptr])

        # Initial window frequency counter for the first segment of s2
        # and check the first window
        if right_Ptr <= len(s2) and same_Freq_Dict(d1, d2):
                return True

        # Slide the window across s2
        while right_Ptr < len(s2):
            # Remove the character going out of the window
            d2[s2[left_Ptr]] -= 1
            if d2[s2[left_Ptr]] == 0:
                d2.pop(s2[left_Ptr])  # Remove key if count is 0

            # Move the window one character to the right
            left_Ptr += 1
            right_Ptr += 1

            # Add the new character coming into the window
            if right_Ptr <= len(s2):  # Ensure right_Ptr is within bounds
                d2[s2[right_Ptr - 1]] += 1

            # Check if current window matches
            if same_Freq_Dict(d1, d2):
                return True

        return False

# Time Complexity: O(n + m)
# Space Complexity: O(m)