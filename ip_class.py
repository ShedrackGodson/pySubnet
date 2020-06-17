# For finding the class name of the given IP Address: Both Binary and Dotted-Decimal
# Since these two fits most of the use-case(they are used a lot)

def bin_class(binary):
    """ This function takes the first four binary integers and returns str
        For example 0001: 'A' i.e class A IP Address
        Since the four bits are used to identify the class of an IP Address
    """
    # Checking for the presence of weird values
    for i in binary:
        try:
            int(i)
        except Exception:
            return print("Enter a valid IP Address")
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

bin_class("0000")