import unittest
from collections import Counter

def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False

    counter = Counter()
    for c in str1:
        counter[c] += 1

    for c in str2:
        if counter[c] == 0:
            return False
        counter[c] -= 1

    return True


class Test(unittest.TestCase):
    dataT = [('abcd', 'bacd'),
            ('3563476', '7334566'),
            ('wef34f', 'wffe34')]
    dataF = [('abcd', 'd2cba'), 
            ('34532', '34113'),
            ('dcw4f', 'dcw5f')]

    def test_cp(self):
        # True Check
        for test_string in self.dataT:
            result = check_permutation(*test_string)
            self.assertTrue(result)

        for test_string in self.dataF:
            result = check_permutation(*test_string)
            self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()

