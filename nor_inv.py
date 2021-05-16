def nor_inv(filename: str):
    """
    Takes filename as parameter and returns Nornir inventory
    
    Parameter:
        filename (str): The name of file which contains device name and IP-Address
    
    Returns:
        Nornir Inventory
    """
    with open(filename) as f: 
        data = f.read().splitlines()
        #Create a new list which contains tuple of hostname and ip-address  
        newlist = [tuple(value.split(" ")) for value in data]
        #Tuple unpacking for creating nornir inventory
        for name,ip in newlist:
            print()
            print(f"{name.upper()}:") 
            print(f"   hostname: {ip}") 
            print("   groups:") 
            site_abb = name.split("-") 
            print(f"       - {site_abb[0].capitalize()}")
            print("   platform: 'ios'")

if __name__ == '__main__':
  nor_inv("ip_addr.txt")
