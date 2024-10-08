import sys
def sqr(x):
    """Compute square roots using the method of Heron of Alexandria 
        Args: 
            x: The number whose square root is to be computed.
        Returns: The square root of x  
    """
    
    if x<0:
        raise ValueError("Cannot comupte square root of" 
                                f" negative number {x}")
    
    guess = x
    i=0
    
    while guess * guess != x and i < 20:
        guess = (guess + x / guess)/2.0
        i+=1
    return guess
    
def main():
    try:
        print(sqr(9))
        print(sqr(2))
        print(sqr(-1))
    except ValueError as e:
        print(e, file=sys.stderr)
    
    
if __name__ == "__main__":
    main()