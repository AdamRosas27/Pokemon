class Character:

    # Create constructor method:
    def __init__(self, name, level=0, max_health=100, current_health=100, knocked_out=False):
        # Make sure the name given is a valid length
        assert len(
            name) > 1, f"Name {name} is too short. Name cannot be less than 2 characters."
        assert len(
            name) <= 10, f"Name {name} is too long. name cannot be more than 10 characters."

        self.name = name
        self.level = level
        self.max_health = max_health
        self.current_health = current_health
        self.knocked_out = knocked_out

    # Create str function:
    def __str__(self) -> str:
        # Return current information of character
        return f"{self.name} -- Current Level: {self.level}, Max Health: {self.max_health}, Current Health: {self.current_health}, Knocked Out Status: {self.knocked_out}"

    def instantiate_csv(self):
