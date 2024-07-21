import unittest
import os
from task_00_intro import generate_invitations

class TestMissingDataInObject(unittest.TestCase):
    def test_missing_data_in_object(self):
        template = """
Hello {{ name }},

You are invited to the {{ event_title }} on {{ event_date }} at {{ event_location }}.

We look forward to your presence.

Best regards,
Event Team
"""
        attendees = [
            {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
        ]
        
        # Clear any existing output files before running the test
        for i in range(1, len(attendees) + 1):
            if os.path.exists(f'output_{i}.txt'):
                os.remove(f'output_{i}.txt')
        
        generate_invitations(template, attendees)
        
        # Check the content of the generated file
        with open('output_1.txt', 'r') as file:
            content = file.read()
        
        # Assert that missing data is replaced with "N/A"
        self.assertIn("on N/A", content, "Failed: Missing data should be replaced with 'N/A'")

if __name__ == '__main__':
    unittest.main()
