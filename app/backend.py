# backend.py

def ip_validation(ip):
    octets = ip.split(".")  #Splits the IP into its 4 octets

    if len(octets) != 4:    #Checks if there are exactly 4 octets
        return False, None

    for octet in octets:      ##Ensures each octet is a number
        if not octet.isdigit():
            return False, None
        num = int(octet)
        if num < 0 or num > 255:   #Ensures each octet is a number between 0 and 255
            return False, None

    if 0 <= int(octets[0]) <= 127:
        return True, "A"
    elif 128 <= int(octets[0]) <= 191:
        return True, "B"
    elif 192 <= int(octets[0]) <= 223:
        return True, "C"
    elif 224 <= int(octets[0]) <= 239:
        return True, "D (Multicast Address Range), Not defined"
    elif 240 <= int(octets[0]) <= 255:
        return True, "E (Reserved Only), Not defined"
    else:
        return False, None

def calculate_subnet(ip_class, cidr=None):
    if cidr:
        host_bits = 32 - int(cidr)
        return 2 ** host_bits - 2, get_subnet_from_cidr(cidr)
    else:
        if ip_class == "A":
            return 2 ** (32 - 8) - 2, "255.0.0.0"
        elif ip_class == "B":
            return 2 ** (32 - 16) - 2, "255.255.0.0"
        elif ip_class == "C":
            return 2 ** (32 - 24) - 2, "255.255.255.0"
        elif ip_class.startswith("D") or ip_class.startswith("E"):
            return None, None

def get_subnet_from_cidr(cidr):
    total_bits = 32
    cidr = int(cidr)
    subnet_bits = ["1"] * cidr + ["0"] * (total_bits - cidr)
    subnet_octets = [int("".join(subnet_bits[i:i+8]), 2) for i in range(0, total_bits, 8)]
    return ".".join(map(str, subnet_octets))

def get_cidr_from_subnets(num_subnets):
    bits_for_subnets = len(bin(num_subnets)) - 2
    total_bits = 32
    cidr = total_bits - bits_for_subnets
    return cidr

def get_cidr_from_hosts(num_hosts):
    total_bits = 32
    bits_for_hosts = len(bin(num_hosts + 2)) - 2  # +2 accounts for network and broadcast addresses
    cidr = total_bits - bits_for_hosts
    return cidr
