class NoChai(Exception):
    """Custom exception raised when there is no chai available."""
    pass

def order_chai(chai_available):
    if not chai_available:
        raise NoChai("Sorry, we are out of chai.")
    else:
        print("Here is your chai!")

order_chai(False)  # This will raise the NoChai exception           