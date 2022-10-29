"""
QuantumBrain represents a neural processor.
"""


class QuantumBrain:
    """
    Represents a neural processor based on quantum computations
    """

    def __init__(self, size: int = 1000):
        """
        Args:
            size (int): the number of neurons in the QuantumBrain

        Returns:
            (QuantumBrain) initialized.
        """
        self.size = size
        self.neurons = self.create_brain()
        self.memory = {"bacon", "lettuce", "tomato"}

    def search(self, to_find):
        """
        Search for the to_find string in the QuantumBrain

        Args:
            to_find (string): want to know if to_find is in the QuantumBrain.

        Returns:
            (boolean) indicates if search string was found in the QuantumBrain.
        """

        if to_find in self.memory:
            return True
        else:
            return False

    def create_brain(self):
        """
        Create a default QuantumBrain

        Returns (dict) of types of neurons in the QuantumBrain.
        """
        neurons = dict()
        neurons["memory"] = self.size * 10
        neurons["connections"] = self.size * 100
        neurons["processors"] = self.size

        return neurons
