# This function simplify the hardship in ANDing the IPs addresses
# For instance when find the Block address by ANDing Mask Address with IP address
from dotted_decimal_to_binary import to_binary
from ip_class import bin_class

def anding(ip1):
    """ Takes two dotted-decimals IPs and ANDing them and returns a str of Block dotted-decimal IP address"""

    result_binary_1 = to_binary(ip1)
    # Checking for the Class of IP
    ip_class = bin_class(result_binary_1[:4])

    if ip_class == "Class A":
        result_byte = list()
        byte_1 = result_binary_1[:8]
        for i in byte_1:
            if int(i) * 1 == 1:
                result_byte.append("1")
            else:
                result_byte.append("0")
        result_byte = ''.join(result_byte)
        
        res_mask = int(result_byte,2)

        res_block = str(res_mask) +".0.0.0"
        return res_block
    
    elif ip_class == "Class B":
        byte_1 = result_binary_1[:17].split(' ')
        res_block = "{}.{}.0.0".format(int(byte_1[0], 2), int(byte_1[1], 2))
        return res_block

    elif ip_class == "Class C":
        byte_1 = result_binary_1[:26].split(' ')
        res_block = "{}.{}.{}.0".format(int(byte_1[0], 2), int(byte_1[1], 2), int(byte_1[2], 2))
        return res_block
    
    else:
        res_block = "Reserved Class"
        return res_block
        

anding("255.56.7.91")