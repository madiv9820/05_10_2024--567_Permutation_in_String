from Solution import Solution
import unittest
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__testCases = {1: {'s1': "ab", 's2': "eidbaooo", 'output': True},
                            2: {'s1': "ab", 's2': "eidboaoo", 'output': False}}
        self.__obj = Solution()
        return super().setUp()
    
    @timeout(0.5)
    def test_Case_1(self):
        s1, s2, output = self.__testCases[1].values()
        result = self.__obj.checkInclusion(s1, s2)
        self.assertIsInstance(result, bool)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_Case_2(self):
        s1, s2, output = self.__testCases[2].values()
        result = self.__obj.checkInclusion(s1, s2)
        self.assertIsInstance(result, bool)
        self.assertEqual(result, output)

if __name__ == '__main__': unittest.main()