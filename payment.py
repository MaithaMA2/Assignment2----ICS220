# payment.py
class Payment:
    """
    Handles payment processing for bookings.
    """
    def __init__(self, payment_id: int, booking, amount: float, method: str):
        self.__payment_id = payment_id
        self.__booking = booking
        self.__amount = amount
        self.__method = method
        self.__status = "Processed"  # Default processed when object is created


    def __str__(self):
        return (f"Payment ID: {self.__payment_id}, Booking ID: {self.__booking._Booking__booking_id}, "
                f"Amount: ${self.__amount:.2f}, Method: {self.__method}, Status: {self.__status}")
