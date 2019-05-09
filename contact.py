"""Read list of contacts from JSON file, and group contacts by phone."""
import json
from toolz.itertoolz import groupby


class Contact:
    """Group users by phone number."""

    def __init__(self, jsonData):
        """Initialize class."""
        self.jsonData = jsonData
        self.data = self.read_json_data()

    def read_json_data(self):
        """Read user data from JSON file."""
        with open(self.jsonData, 'r') as f:
            dataDict = json.load(f)
            return dataDict

    def mergeUsers(self):
        """Return lists of user dicts where phone matches."""
        grouped = groupby('phone', self.data)
        return grouped
