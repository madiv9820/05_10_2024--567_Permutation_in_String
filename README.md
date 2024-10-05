# 567. Permutation in String

__Type:__ Medium <br>
__Topics:__ Hash Table, Two Pointers, String, Sliding Window <br>
__Companies:__ Microsoft, Google, Meta, Yandex, Amazon, Bloomberg, Goldman Sachs, Adobe, Apple, Uber, Yahoo, Revolut, Expedia, Groww <br>
__Leetcode Link:__ [567. Permutation in String](https://leetcode.com/problems/permutation-in-string/description/)
<hr>

### Question

Given two strings `s1` and `s2`, return `true` if `s2` contains a [__permutation__](https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/) of `s1`, or `false` otherwise.

In other words, return `true` if one of `s1`'s permutations is the substring of `s2`.
<hr>

### Examples

__Example 1:__

__Input:__ s1 = "ab", s2 = "eidbaooo" <br>
__Output:__ true <br>
__Explanation:__ s2 contains one permutation of s1 ("ba").

__Example 2:__

__Input:__ s1 = "ab", s2 = "eidboaoo" <br>
__Output:__ false
<hr>

### Constraints:

- <code>1 <= s1.length, s2.length <= 10<sup>4</sup></code>
- `s1` and `s2` consist of lowercase English letters.
<hr>

### Hints
- Obviously, brute force will result in TLE. Think of something else.
- How will you check whether one string is a permutation of another string?
- One way is to sort the string and then compare. But, Is there a better way?
- If one string is a permutation of another string then they must have one common metric. What is that?
- Both strings must have same character frequencies, if one is permutation of another. Which data structure should be used to store frequencies?
- What about hash table? An array of size 26?