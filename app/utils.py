




def to_usd(my_price):
    '''
    this is a docstring it tells us what this function is about.
    what its responsibilities are
    what the params are about
    what datatypes the params are
    what this function will return
    example of invoking the function

    invoke like this: to_usd(9.9999)
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
    