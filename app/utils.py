




def to_usd(my_price):
    '''
    this function is used to cut off after two decimals
    and place a dollar sign in front to put
    it in currency formatting
    the paramater is a float of the number you
    want formatted. it returns it in currency format

    invoke like this: to_usd(9.9999)
    and it will return $9.99
    '''

    return '${:,.2f}'.format(my_price)
    
#if this code is in the global scope
#... of a file we're trying to import from 
#... it will throw errors when we try to run those

#price = input("Please choose a price like 4.9999")

#print(to_usd(float(price)))

if __name__ == "__main__":
    
    # nesting code in the main condition will
    # allow other scripts to cleanly import functions from this file
    # without running this code

    # this code still gets run when we invoke the script from the command line
    price = input("Please choose a price like 4.9999")

    print(to_usd(float(price)))
    