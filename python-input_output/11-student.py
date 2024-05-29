class Student:
    """Defines a student by first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initializes a Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student.

        Args:
            attrs

        Returns:
            dict: Dictionary representation of the Student instance.
        """
        if attrs is None:
            # If attrs is None, retrieve all attributes
            return self.__dict__
        else:
            # Otherwise, retrieve only specified attributes
            json_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    json_dict[attr] = getattr(self, attr)
            return json_dict

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student.

        Args:
            json (dict): Dictionary containing attribute names and values.
        """
        for attr, value in json.items():
            setattr(self, attr, value)
