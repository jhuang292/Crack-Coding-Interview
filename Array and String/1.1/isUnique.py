import unittest


def unique(string):

    # Assume character set is ASCII (128 characters)
    if len(string) > 128:
        return False

    char_set = [False for _ in range(128)]
    for char in string:
        val = ord(char)
        if char_set[val]:
            return False
        char_set[val] = True


    return True


class Test(unittest.TestCase):
    dataF = [('dafda'), ('3rs3 d'), ('dd')]
    dataT = [('asdf'), ('23esf'), ('kdlsc')]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = unique(test_string)
            self.assertTrue(actual)

        # false check
        for test_string in self.dataF:
            actual = unique(test_string)
            self.assertFalse(actual)


if __name__ == "__main__":
    unittest.main()
