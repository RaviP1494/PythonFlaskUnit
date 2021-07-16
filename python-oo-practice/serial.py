"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self,start):
        """Initializes attributes 'initial' and 'next'"""
        self.initial = start
        self.next = start

    def __repr__(self):
        """Returns representation of instance when instance called upon"""
        return f"<SerialGenerator initial={self.initial} next={self.next}>"


    def generate(self):
        """Returns and increments attribute 'next'"""
        temp = self.next
        self.next += 1
        return temp

    def reset(self):
        """Resets 'next' to 'initial' value"""
        self.next = self.initial


    

