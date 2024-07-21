import unittest
import os
from task_00_intro import generate_invitations

class TestEmptyTemplate(unittest.TestCase):
    def test_empty_template(self):
        template = ""
        attendees = [
            {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"}
        ]
        
        # Clear any existing output files before running the test
        for i in range(1, len(attendees) + 1):
            if os.path.exists(f'output_{i}.txt'):
                os.remove(f'output_{i}.txt')
        
        generate_invitations(template, attendees)
        
        # Check that no output files were created
        for i in range(1, len(attendees) + 1):
            self.assertFalse(os.path.exists(f'output_{i}.txt'))

if __name__ == '__main__':
    unittest.main()
