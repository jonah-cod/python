

def get_term():
    try:
        import msvcrt
        inp = msvcrt.getche()
        # print(inp)
    except ImportError as e:
        print(e)
        
        
get_term()