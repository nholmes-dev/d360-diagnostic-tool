import unittest
from app import validate_tenant_data, bubble_sort_by_size

class TestD360DiagnosticTool(unittest.TestCase):

    def test_validation_with_valid_data(self):
        """Tests that correct data inputs return True."""
        result = validate_tenant_data(105, "Council_Epsilon_UAT")
        self.assertTrue(result)

    def test_validation_with_invalid_id(self):
        """Tests that a negative or zero ID correctly fails validation."""
        result = validate_tenant_data(-1, "Council_Invalid_UAT")
        self.assertFalse(result)

    def test_validation_with_empty_name(self):
        """Tests that an empty name string correctly fails validation."""
        result = validate_tenant_data(106, "   ")
        self.assertFalse(result)

    def test_bubble_sort_logic(self):
        """Verifies that the Bubble Sort algorithm accurately sorts records by database size ascending."""
        mock_data = [
            [101, "Tenant_A", 50.0],
            [102, "Tenant_B", 10.0],
            [103, "Tenant_C", 30.0]
        ]
        # Run our custom sorting algorithm
        sorted_output = bubble_sort_by_size(mock_data)
        
        # Verify sizes are strictly ordered: 10.0, then 30.0, then 50.0
        self.assertEqual(sorted_output[0][2], 10.0)
        self.assertEqual(sorted_output[1][2], 30.0)
        self.assertEqual(sorted_output[2][2], 50.0)

if __name__ == '__main__':
    unittest.main()