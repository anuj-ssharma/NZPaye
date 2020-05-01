import unittest

from nzpaye import argument_parser
from nzpaye.main import paye_summary, validate_argument_values


class TestParser(unittest.TestCase):
    def setUp(self):
        self.parser = argument_parser.get_parser()

    def test_invalid_hours_worked(self):
        args = [
            "--hours-worked", "0",
            "--hourly-rate", "110"
        ]
        opts = self.parser.parse_args(args)
        with self.assertLogs('paye', level='ERROR') as cm:
            with self.assertRaises(SystemExit):
                paye_summary(opts)
        self.assertIn(cm.output[0], 'ERROR:paye:Hours worked should be greater than 0')

    def test_invalid_hourly_rate(self):
        args = [
            "--hours-worked", "40",
            "--hourly-rate", "0"
        ]
        opts = self.parser.parse_args(args)
        with self.assertLogs('paye', level='ERROR') as cm:
            with self.assertRaises(SystemExit):
                paye_summary(opts)
        self.assertIn(cm.output[0], 'ERROR:paye:Hourly rate should be greater than 0')

    def test_invalid_witholding_tax(self):
        args = [
            "--hours-worked", "40",
            "--hourly-rate", "110",
            "--wht", "30"
        ]
        opts = self.parser.parse_args(args)

        with self.assertLogs('paye', level='ERROR') as cm:
            with self.assertRaises(SystemExit):
                paye_summary(opts)
        self.assertIn(cm.output[0], 'ERROR:paye:Witholding tax can be 10 or 20 ')

    def test_valid_values(self):
        args = [
            "--hours-worked", "40",
            "--hourly-rate", "110",
            "--wht", "10"
        ]
        opts = self.parser.parse_args(args)
        self.assertTrue(validate_argument_values(opts))