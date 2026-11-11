import unittest
import pytest
from fuel_station import fuel_bill, pump_allowed, session_status


class TestFuelStationLineCoverage(unittest.TestCase):
    def test_fuel_bill_invalid_grade(self):
        with pytest.raises(ValueError, match="unknown fuel grade"):
            fuel_bill("invalid", 10, "gold")

    def test_fuel_bill_invalid_litres(self):
        with pytest.raises(ValueError, match="invalid litres"):
            fuel_bill("regular", -5, "gold")

    def test_fuel_bill_gold_tier_high_litres(self):
        result = fuel_bill("regular", 50, "gold")
        self.assertEqual(result, 3325)

    def test_fuel_bill_diesel_within_voucher(self):
        result = fuel_bill("diesel", 15, "silver")
        self.assertEqual(result, 0)

    def test_pump_allowed_fleet(self):
        self.assertTrue(pump_allowed(150, 2, True))

    def test_pump_allowed_non_fleet_over_limit(self):
        self.assertFalse(pump_allowed(70, 0, False))

    def test_session_status_card_night_active(self):
        self.assertEqual(session_status(90, True, True), "active")

    def test_session_status_cash_day_warning(self):
        self.assertEqual(session_status(20, False, False), "warning")

    def test_session_status_timed_out(self):
        self.assertEqual(session_status(5, False, False), "timed_out")


if __name__ == "__main__":
    unittest.main()
