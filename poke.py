class Character:

    # Create constructor method:
    def __init__(self, name, level=0, max_health=100, current_health=100, knocked_out=False):
        # Make sure the name given is a valid length
        assert len(
            name) > 1, f"Name {name} is too short. Name cannot be less than 2 characters."

        self.name = name
        self.level = level
        self.max_health = max_health
        self.current_health = current_health
        self.knocked_out = knocked_out
