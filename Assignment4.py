"""4. Write a class called RestaurantCheck. It should have the following:
      • Fields called check_number, sales_tax_percent, subtotal, table_number, and server_name
      representing an identification for the check, the bill without tax added, the sales tax percentage,
      the table number, and the name of the server.
      • A constructor that sets the values of all four fields
      • A method called calculate_total that takes no arguments (besides self) and returns the total
      bill including sales tax.
      • A method called print_check that writes to a file called check###.txt, where ### is the check
      number and writes information about the check to that file, formatted like below:
      Check Number: 443
      Sales tax: 6.0%
      Subtotal: $23.14
      Total: $24.53
      Table Number: 17
      Server: Sonic the Hedgehog
      Test the class by creating a RestaurantCheck object and calling the print_check() method"""

class RestaurantCheck:
    def __init__(self,check_number, sales_tax_percent, subtotal,table_number,server_name):
        self.check_number=check_number
        self.sales_tax_percent=sales_tax_percent
        self.subtotal=subtotal
        self.table_number=table_number
        self.server_name=server_name
        
    def calculate_total(self):
        self.Total=self.subtotal*((self.sales_tax_percent/100)+1)
        return self
    def print_check(self):
        self.checkfile=open(f"Check{self.check_number}.txt","a")
        self.checkfile.write(f"""
        Check Number:{self.check_number}
        Sales Tax:{self.sales_tax_percent}%
        Subtotal:${self.subtotal}
        Total:${self.Total}
        Table number:{self.table_number}
        Server:{self.server_name}        """)
        return self
check1=RestaurantCheck(1,6,100,5,"Sonic the Hedgehog")
check1.calculate_total().print_check()
