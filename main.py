from contact import Contact
import pprint


def main(data):
    """Application entry point.

    1. Create instance of Contact class with contact data.
    2. Merge contacts via mergeUsers() method.
    3. Return merged contacts.
    """
    contacts = Contact(data)
    merged = contacts.mergeUsers()
    return merged


if __name__ == "__main__":
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(main('./data/users.json'))
