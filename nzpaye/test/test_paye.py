import unittest
from nzpaye import paye
from nzpaye.exception import ArgumentError


class TestPaye(unittest.TestCase):
    def setUp(self):
        pass

    def test_income_summary_with_valid_values(self):
        hourly_rate = 110
        hours_worked = 40
        summary = paye.income_summary(hourly_rate=hourly_rate, hours_worked=hours_worked)
        self.assertEqual(summary, {'hours_worked': '40', 'total_income': '4400.00', 'total_paye': '1277.38', 'less_witholding_tax': '440.00', 'plus_gst': '660.00', 'paid_to_account': '4620.00', 'remaining_paye_to_be_paid': '837.38', 'remaining_gst_and_paye_to_be_paid': '1497.38', 'disposable_income': '3122.62'})


    def test_income_summary_with_invalid_hourly_rate(self):
        hourly_rate = 0
        hours_worked = 40
        with self.assertRaises(ArgumentError) as cm:
            paye.income_summary(hourly_rate=hourly_rate, hours_worked=hours_worked)
        self.assertTrue("Enter a valid value for hourly rate" in str(cm.exception) )

    def test_income_summary_with_invalid_hours_worked(self):
        hourly_rate = 110
        hours_worked = 0
        with self.assertRaises(ArgumentError) as cm:
            paye.income_summary(hourly_rate=hourly_rate, hours_worked=hours_worked)
        self.assertTrue("Enter a valid value for hours worked" in str(cm.exception) )

    def test_income_summary_with_invalid_witholding_tax(self):
        hourly_rate = 110
        hours_worked = 40
        witholding_tax = 30
        with self.assertRaises(ArgumentError) as cm:
            paye.income_summary(hourly_rate=hourly_rate, hours_worked=hours_worked, witholding_tax=witholding_tax)
        self.assertTrue("Enter a valid value for witholding tax" in str(cm.exception) )

    def test_yearly_paye(self):
        self.assertEqual(paye.calculate_yearly_paye(10000),  1050.00)
        self.assertEqual(paye.calculate_yearly_paye(14000),  1470.00)
        self.assertEqual(paye.calculate_yearly_paye(20000),  2520.00)
        self.assertEqual(paye.calculate_yearly_paye(48001),  7420.30)
        self.assertEqual(paye.calculate_yearly_paye(65000),  12520.00)
        self.assertEqual(paye.calculate_yearly_paye(70000),  14020.00)
        self.assertEqual(paye.calculate_yearly_paye(100000), 23920.00)

    def test_paye_ietc(self):
        self.assertEqual(paye.calculate_yearly_paye(24001), 2700.18)
        self.assertEqual(paye.calculate_yearly_paye(44000), 6200.00)
        self.assertEqual(paye.calculate_yearly_paye(44001), 6200.30)
        self.assertEqual(paye.calculate_yearly_paye(45000), 6505.00)
        self.assertEqual(paye.calculate_yearly_paye(47999), 7419.69)
        self.assertEqual(paye.calculate_yearly_paye(44001), 6200.30)
        self.assertEqual(paye.calculate_yearly_paye(48000), 7420.00)

