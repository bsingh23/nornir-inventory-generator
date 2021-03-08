def nor_inv(filename): 
    with open(filename) as f: 
        data = f.read().splitlines()
        #Create a new list which contains tuple of hostname and ip-address  
        newlist = [tuple(value.split(" ")) for value in data]
        #Tuple unpacking for creating nornir inventory
        for name,ip in newlist: 
            print(f"{name.upper()}:") 
            print(f"   hostname: {ip}") 
            print("   group:") 
            site_abb = name.split("-") 
            print(f"       - {site_abb[0].upper()}")
            print("   platform: 'ios'")

if __name__ == '__main__':
  nor_inv("ip_addr.txt")
