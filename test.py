import unittest
import poker_rules
class TestPoker(unittest.TestCase):

    def test_makeDeck(self):
        
        self.assertEqual(poker_rules.isPair([('sz', 1), ('k', 13),('t', 2),('p', 9), ('sz', 3)]), False)
        self.assertEqual(poker_rules.isPair([('sz', 1), ('k', 13),('t', 2),('p', 9), ('sz', 3)]), False)
        self.assertEqual(poker_rules.isPair([('sz', 1), ('k', 13),('t', 2),('p', 9), ('sz', 2)]), True)
        self.assertEqual(poker_rules.isPair([('sz', 1), ('k', 13),('t', 2),('p', 2), ('sz', 2)]), False)
        self.assertEqual(poker_rules.isPair([('sz', 1), ('k', 13),('t', 2),('p', 9), ('sz', 3)]), False)

    def test_isPoker(self):
        result = poker_rules.isPoker([('sz', 1), ('k', 13),('t', 2),('p', 9), ('sz', 3)])
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()
