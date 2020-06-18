# For finding the class name of the given IP Address: Both Binary and Dotted-Decimal
# Since these two fits most of the use-case(they are used a lot)

# class IpClass:
#     def __init__(self, binary: int=None):
#         self.binary = binary

def decimal_class(decimal):
    """ This function takes the first three decimal integers and returns str
        For example 127: 'A' i.e class A IP Address
        Since the first three integers are used to indentify the class of an IP Address
        based on the range of the given IP address.
    """
    result_class = str()
    if type(decimal) != type(int()):
        raise ValueError
    else:
        if decimal >= 0 and decimal <= 127:
            result_class = "Class A"
            return result_class
        elif decimal >= 128 and decimal <= 191:
            result_class = "Class B"
            return result_class
        elif decimal >= 192 and decimal <= 223:
            result_class = "Class C"
            return result_class
        elif decimal >= 224 and decimal <= 239:
            result_class = "Class D"
            return result_class
        elif decimal >= 240 and decimal <= 255:
            result_class = "Class E"
            return result_class
        else:
            raise ValueError

def bin_class(binary):
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
        result_class = str()
        if binary[0] == '0':
            result_class = "Class A"
            return result_class
        elif binary[:2] == "10":
            result_class = "Class B"
            return result_class
        elif binary[:3] == "110":
            result_class = "Class C"
            return result_class
        elif binary[:4] == "1110":
            result_class = "Class D"
            return result_class
        elif binary[:] == "1111":
            result_class = "Class E"
            return result_class

def address_space(binary):
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
            return (pow(2,31),":50% of address space")
        elif binary[:2] == "10":
            return (pow(2,30),":25% of address space")
        elif binary[:3] == "110":
            return (pow(2,29),":12.5% of address space")
        elif binary[:4] == "1110":
            return (pow(2,28),":6.25% of address space")
        elif binary[:] == "1111":
            return (pow(2,28),":6.25% of address space")

# x  = IpClass()
# print(x.decimal_class(127))