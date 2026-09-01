import unittest
# Import  basic function names
from app import check_data, basic_bubble_sort


class TestMyDiagnosticTool(unittest.TestCase):

    def test_good_data(self):
        # Test that correct data returns true
        result = check_data(105, "Council_Epsilon_UAT")
        self.assertTrue(result)

    def test_negative_id(self):
        # Test that a negative ID fails
        result = check_data(-1, "Council_Invalid_UAT")
        self.assertFalse(result)

    def test_blank_name(self):
        # Test that an empty name fails
        result = check_data(106, "")
        self.assertFalse(result)

    def test_whitespace_name(self):
            # A name containing only spaces should also be rejected
            result = check_data(107, "   ")
            self.assertFalse(result)

    def test_my_bubble_sort(self):
        # Test basic sorting works
        mock_data = [
            [101, "Tenant_A", 50.0],
            [102, "Tenant_B", 10.0],
            [103, "Tenant_C", 30.0]
        ]
        sorted_output = basic_bubble_sort(mock_data)

        # Check that sizes are in order: 10.0, 30.0, 50.0
        self.assertEqual(sorted_output[0][2], 10.0)
        self.assertEqual(sorted_output[1][2], 30.0)
        self.assertEqual(sorted_output[2][2], 50.0)


if __name__ == '__main__':
    unittest.main()
