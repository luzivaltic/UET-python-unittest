import unittest
from function import shopping

class TestShopping(unittest.TestCase):

    def test_invalid_input(self):
        accumulated_points = -1
        bill = 250
        self.assertEqual(shopping(accumulated_points, bill), 'Invalid input')

        accumulated_points = 3
        bill = -100
        self.assertEqual(shopping(accumulated_points, bill), 'Invalid input')
    
    # decision table

    def test_accumulate_point(self):
        accumulated_points = 0
        bill = 150
        self.assertEqual(shopping(accumulated_points, bill), '+1 accumulated point')

        accumulated_points = 0
        bill = 1150
        self.assertEqual(shopping(accumulated_points, bill), '+1 accumulated point')

        accumulated_points = 7
        bill = 1150
        self.assertEqual(shopping(accumulated_points, bill), '+1 accumulated point')

    def test_no_accumulate_point(self):
        accumulated_points = 3
        bill = 50
        self.assertEqual(shopping(accumulated_points, bill), '')

    def test_discount_bill(self):
        accumulated_points = 5 
        bill = 50
        self.assertEqual(shopping(accumulated_points, bill), 'You got a 10% bill discount')
        
        accumulated_points = 5
        bill = 150
        self.assertEqual(shopping(accumulated_points, bill), 'You got a 10% bill discount')

        # miss this test
        # accumulated_points = 4
        # bill = 150
        # self.assertEqual(shopping(accumulated_points, bill), 'You got a 10% bill discount')


    # equivalence partitioning

    def test_low_accumulated_point(self):

        accumulated_points = 0
        bill = 50
        self.assertEqual(shopping(accumulated_points, bill), '')

        accumulated_points = 0
        bill = 150
        self.assertEqual(shopping(accumulated_points, bill), '+1 accumulated point')

        accumulated_points = 0
        bill = 1150
        self.assertEqual(shopping(accumulated_points, bill), '+1 accumulated point')
    
    def test_high_accumulated_point(self):
        accumulated_points = 10
        bill = 50
        self.assertEqual(shopping(accumulated_points, bill), 'You got a 10% bill discount')

        accumulated_points = 10
        bill = 150
        self.assertEqual(shopping(accumulated_points, bill), 'You got a 10% bill discount')

        accumulated_points = 10
        bill = 1150
        self.assertEqual(shopping(accumulated_points, bill), '+1 accumulated point')

    def c2_test(self):
        accumulated_points = -100
        bill = -1000
        self.assertEqual(shopping(accumulated_points, bill), 'Invalid input')

        accumulated_points = 100
        bill = 999
        self.assertEqual(shopping(accumulated_points, bill), 'You got a 10% bill discount')

        accumulated_points = 1000
        bill = 2000
        self.assertEqual(shopping(accumulated_points, bill), 'You got a 10% bill discount')

        accumulated_points = 2
        bill = 50
        self.assertEqual(shopping(accumulated_points, bill), '')

        accumulated_points = 10
        bill = 50
        self.assertEqual(shopping(accumulated_points, bill), 'You got a 10% bill discount')
    
    def test_all_uses(self):
        accumulated_points = 10
        bill = -100
        self.assertEqual(shopping(accumulated_points, bill), 'Invalid input')
        
        accumulated_points = 2
        bill = 150
        self.assertEqual(shopping(accumulated_points, bill), '+1 accumulated point')

        accumulated_points = 5
        bill = 150
        self.assertEqual(shopping(accumulated_points, bill), 'You got a 10% bill discount')

        accumulated_points = 10
        bill = -100
        self.assertEqual(shopping(accumulated_points, bill), 'Invalid input')

        accumulated_points = 2
        bill = 50
        self.assertEqual(shopping(accumulated_points, bill), '')

        accumulated_points = 1
        bill = 60
        self.assertEqual(shopping(accumulated_points, bill), '')

        accumulated_points = 10
        bill = 1500
        self.assertEqual(shopping(accumulated_points, bill), '+1 accumulated point')

        accumulated_points = 10
        bill = 50
        self.assertEqual(shopping(accumulated_points, bill), 'You got a 10% bill discount')