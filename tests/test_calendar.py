import unittest
from ai_risk_replication.calendar import month_range, parse_month


class TestMonthlyCalendar(unittest.TestCase):
    def test_original_period_has_156_months(self):
        months = month_range()
        self.assertEqual(len(months), 156)
        self.assertEqual(months[0], "2012-01")
        self.assertEqual(months[-1], "2024-12")

    def test_cross_year(self):
        self.assertEqual(month_range("2020-11", "2021-02"), ["2020-11", "2020-12", "2021-01", "2021-02"])

    def test_invalid_input(self):
        for bad in ["2024-00", "2024-13", "2024-1", "foo"]:
            with self.subTest(bad=bad):
                with self.assertRaises(ValueError):
                    parse_month(bad)
        with self.assertRaises(ValueError):
            month_range("2021-01", "2020-12")


if __name__ == "__main__":
    unittest.main()
