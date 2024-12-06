import unittest
from day_05 import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_add_rules_aoc_input(self):
        rules = """47|53
                   97|13
                   97|61
                   97|47
                   75|29
                   61|13
                   75|53
                   29|13
                   97|29
                   53|29
                   61|53
                   97|53
                   61|29
                   47|13
                   75|47
                   97|75                   
                   47|61
                   75|61
                   47|29
                   75|13
                   53|13""".splitlines()
        
        for rule in rules:
            k, v = [int(x) for x in rule.split("|")]
            self.solution.add_rule(k, v)
        self.assertEqual(len(self.solution.rules.keys()), 6)
        self.assertEqual(len(self.solution.rules[97]), 6)

    def test_check_ordering_simple_rule_positive(self):
        self.solution.add_rule(1, 2)
        self.solution.add_rule(2, 3)
        self.assertTrue(self.solution.check_ordering([1,2, 3]))

    def test_check_ordering_simple_rule_negative(self):
        self.solution.add_rule(2, 1)
        self.solution.add_rule(3, 2)
        self.assertFalse(self.solution.check_ordering([1,2, 3]))

    def test_check_ordering_aoc_intput(self):
        rules = """47|53
                   97|13
                   97|61
                   97|47
                   75|29
                   61|13
                   75|53
                   29|13
                   97|29
                   53|29
                   61|53
                   97|53
                   61|29
                   47|13
                   75|47
                   97|75                   
                   47|61
                   75|61
                   47|29
                   75|13
                   53|13""".splitlines()
        
        orderings = """75,47,61,53,29
                       97,61,53,29,13
                       75,29,13
                       75,97,47,61,53
                       61,13,29
                       97,13,75,29,47""".splitlines()
        ordering_result = [True, True, True, False, False, False]
        for rule in rules:
            k, v = [int(x) for x in rule.split("|")]
            self.solution.add_rule(k, v)

        for i in range(len(orderings)):
            ordering = [int(x) for x in orderings[i].split(",")]
            self.assertEqual(self.solution.check_ordering(ordering), ordering_result[i])

    def test_validate_do_all_aoc_input(self):
        aoc_input = """47|53
                       97|13
                       97|61
                       97|47
                       75|29
                       61|13
                       75|53
                       29|13
                       97|29
                       53|29
                       61|53
                       97|53
                       61|29
                       47|13
                       75|47
                       97|75
                       47|61
                       75|61
                       47|29
                       75|13
                       53|13

                       75,47,61,53,29
                       97,61,53,29,13
                       75,29,13
                       75,97,47,61,53
                       61,13,29
                       97,13,75,29,47"""
        result = self.solution.do_all(aoc_input)
        self.assertEqual(result, 143)

    def test_validate_do_all_reordering_aoc_input(self):
        aoc_input = """47|53
                       97|13
                       97|61
                       97|47
                       75|29
                       61|13
                       75|53
                       29|13
                       97|29
                       53|29
                       61|53
                       97|53
                       61|29
                       47|13
                       75|47
                       97|75
                       47|61
                       75|61
                       47|29
                       75|13
                       53|13

                       75,47,61,53,29
                       97,61,53,29,13
                       75,29,13
                       75,97,47,61,53
                       61,13,29
                       97,13,75,29,47"""
        result = self.solution.do_all_reordering(aoc_input)
        self.assertEqual(result, 123)
if __name__ == '__main__':
    unittest.main()