# loyalty_program.py
class LoyaltyProgram:
    """
    Manages the loyalty points for a guest.
    """
    def __init__(self, guest):
        self.__guest = guest
        self.__points = 0  # Start with 0 points


    # Points management
    def add_points(self, amount: int):
        self.__points += amount


    def redeem_points(self, points: int) -> bool:
        if points <= self.__points:
            self.__points -= points
            return True
        return False


    def get_points(self) -> int:
        return self.__points


    def __str__(self):
        return f"Loyalty Account for {self.__guest.get_name()}: {self.__points} points"
