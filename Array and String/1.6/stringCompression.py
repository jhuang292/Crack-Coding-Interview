import unittest


def string_compression(string):
    
    res = ""
    counter = 0
    for i in range(len(string)):
    
        if i != 0 and string[i-1] != string[i]:
            res += string[i-1] 
            res += str(counter)
            counter = 0
        counter += 1

    res = res + string[-1] + str(counter)
    return min(string, res, key=len)



class Test(unittest.TestCase):

    data = [('aabcccccaaa', 'a2b1c5a3'),
            ('abcdef', 'abcdef')]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = string_compression(test_string)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
