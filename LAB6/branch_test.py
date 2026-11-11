import unittest
import pytest
from fuel_station import fuel_bill, pump_allowed, session_status


class TestFuelStationBranchCoverage(unittest.TestCase):
    # --- fuel_bill Branch Tests ---

    def test_fuel_bill_unknown_grade(self):
        with pytest.raises(ValueError, match="unknown fuel grade"):
            fuel_bill("cng", 10, "silver")

    def test_fuel_bill_invalid_litres(self):
        with pytest.raises(ValueError, match="invalid litres"):
            fuel_bill("regular", -1, "silver")

    def test_fuel_bill_gold_non_diesel(self):
        self.assertEqual(fuel_bill("regular", 50, "gold"), 3325)

    def test_fuel_bill_gold_diesel(self):
        self.assertEqual(fuel_bill("diesel", 50, "gold"), 2700)

    def test_fuel_bill_silver_extra_over_30(self):
        self.assertEqual(fuel_bill("premium", 50, "silver"), 3465)

    def test_fuel_bill_within_voucher(self):
        self.assertEqual(fuel_bill("regular", 5, "silver"), 0)

    # --- pump_allowed Branch Tests ---

    def test_pump_allowed_fleet_true(self):
        self.assertTrue(pump_allowed(200, 5, True))

    def test_pump_allowed_fleet_false(self):
        self.assertFalse(pump_allowed(201, 5, True))

    def test_pump_allowed_non_fleet_over_60(self):
        self.assertFalse(pump_allowed(61, 1, False))

    def test_pump_allowed_non_fleet_under_60_containers_valid(self):
        self.assertTrue(pump_allowed(50, 1, False))

    def test_pump_allowed_non_fleet_under_60_containers_invalid(self):
        self.assertFalse(pump_allowed(50, 2, False))

    # --- session_status Branch Tests ---

    def test_session_status_card_night_active(self):
        self.assertEqual(session_status(95, True, True), "active")

    def test_session_status_cash_day_warning(self):
        self.assertEqual(session_status(20, False, False), "warning")

    def test_session_status_cash_day_timed_out(self):
        self.assertEqual(session_status(10, False, False), "timed_out")


if __name__ == "__main__":
    unittest.main()
