# For finding the class name of the given IP Address: Both Binary and Dotted-Decimal
# Since these two fits most of the use-case(they are used a lot)

class IpClass:
    def __init__(self, binary: int=None):
        self.binary = binary

    def decimal_class(self, decimal):
        """ This function takes the first three decimal integers and returns str
            For example 127: 'A' i.e class A IP Address
            Since the first three integers are used to indentify the class of an IP Address
            based on the range of the given IP address.
        """
        if type(decimal) != type(int()):
            raise ValueError
        else:
            if decimal >= 0 and decimal <= 127:
                return print("Class A")
            elif decimal >= 128 and decimal <= 191:
                return print("Class B")
            elif decimal >= 192 and decimal <= 223:
                return print("Class C")
            elif decimal >= 224 and decimal <= 239:
                return print("Class D")
            elif decimal >= 240 and decimal <= 255:
                return print("Class E")
            else:
                raise ValueError

    def bin_class(self, binary):
        """ This function takes the first four binary integers and returns str
            For example 0001: 'A' i.e class A IP Address
            Since the four bits are used to identify the class of an IP Address
        """
        # Checking for the presence of weird values
        try:
            for i in binary:
                try:
                    int(i)
                except Exception:
                    return print("Enter a valid IP Address")
        except TypeError:
            return print("Enter String formatted IP Address")
        if type(binary) != type(str()):
            print(type(binary))
            return print("Expected String But Got Integer.")
        if len(binary) != 4:
            return print("Enter the first 4 digits of your IP Address")
        else:
            if binary[0] == '0':
                return print("Class A")
            elif binary[:2] == "10":
                return print("Class B")
            elif binary[:3] == "110":
                return print("Class C")
            elif binary[:4] == "1110":
                return print("Class D")
            elif binary[:] == "1111":
                return print("Class E")

    def address_space(self, binary):
        """ Returns the total number of address spaces available over a given IP Address Class """
        
        # Checking for the presence of weird values
        try:
            for i in binary:
                try:
                    int(i)
                except Exception:
                    return print("Enter a valid IP Address")
        except TypeError:
            return print("Enter String formatted IP Address")
        if type(binary) != type(str()):
            print(type(binary))
            return print("Expected String But Got Integer.")
        if len(binary) != 4:
            return print("Enter the first 4 digits of your IP Address")
        else:
            if binary[0] == '0':
                    return print(pow(2,31),":50% of address space")
            elif binary[:2] == "10":
                return print(pow(2,30),":25% of address space")
            elif binary[:3] == "110":
                return print(pow(2,29),":12.5% of address space")
            elif binary[:4] == "1110":
                return print(pow(2,28),":6.25% of address space")
            elif binary[:] == "1111":
                return print(pow(2,28),":6.25% of address space")

x  = IpClass()
print(x.decimal_class(127))