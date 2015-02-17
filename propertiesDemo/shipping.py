class ShippingContainer:
    next_serial = 1000  #next_serial is a class property

    @staticmethod
    def _get_next_serial():
        result = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return result

    #classmethod accepts the class object as the first formal argument by convention using the abbreviated cls
    @classmethod
    def _get_next_serial_class_method(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    @classmethod
    def create_empty(cls, owner_code):
        return cls(owner_code, contents=None)

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer._get_next_serial() # calling static method
        self.serial = ShippingContainer.next_serial # access class property
        ShippingContainer.next_serial += 1 # assign class property

