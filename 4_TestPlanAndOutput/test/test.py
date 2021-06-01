import unittest
import TimeDifferenceCalculator as td


class TestCalc(unittest.TestCase):

    def test_countLeapYears(self):
        self.assertEqual(td.countLeapYears(td.Date(31,5,2021)), 490)
        self.assertEqual(td.countLeapYears(td.Date(12,1,1920)), 464)
        self.assertEqual(td.countLeapYears(td.Date(14,4,3)), 0)
        self.assertEqual(td.countLeapYears(td.Date(31,5,4)), 1)
        
    def test_getDifference(self):
        self.assertEqual(td.getDifference(td.Date(31,5,2021),td.Date(31,5,2021)), 0)
        self.assertEqual(td.getDifference(td.Date(13,12,2017),td.Date(13,12,2018)), 365)
        self.assertEqual(td.getDifference(td.Date(1,2,1),td.Date(1,2,4)), 1095)

    def test_numOfDays(self):
        self.assertEqual(td.getDifference(td.Date(1,2,1),td.Date(1,2,4)), 1095)
        self.assertEqual(td.numOfDays(td.Date(31,5,2021),td.Date(31,5,2021)), 0)

    def test_numOfMonths(self):
        self.assertEqual(td.numOfMonths(td.Date(1,2,1),td.Date(1,2,4)), 36)
        self.assertEqual(td.numOfMonths(td.Date(31,5,2021),td.Date(31,5,2021)), 0)

    def test_numOfYears(self):
        self.assertEqual(td.numOfYears(td.Date(1,2,1),td.Date(1,2,4)), 3)
        self.assertEqual(td.numOfYears(td.Date(31,5,2021),td.Date(31,5,2021)), 0)



if __name__ == '__main__':
    unittest.main()
