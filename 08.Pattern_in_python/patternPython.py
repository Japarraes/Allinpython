def leftTrianglePattern(len):

    for i in range(len):
        for j in range(i+1):
            print("*", end="")
        print() # for new line

def rightTrianglePatter(len):

    for i in range(len):
        
        for j in range(len - (i+1)):
            print(" ", end="")
        
        for j in range(i+1):
            print("*", end="")
        
        print() # for new line

def pyramidPattern(len):

    for i in range(len):

        for j in range(len, (i+1), -1):
            print(" ", end="")
        
        for k in range(2*(i-1)+3):
            print("*", end="")
        
        print()

def invertedPyramidPattern(len):

    for i in range(len):

        for j in range(i):
            print(" ", end="")

        for k in range((2*(len-i))-1):
            print("*", end="")

        print()

def diamondPattern(len):

    # Upper pyramid
    for i in range(len):

        for j in range(len, (i+1), -1):
            print(" ", end="")
        
        for k in range(2*(i-1)+3):
            print("*", end="")
        
        print()

    # Lower pyramid
    for i in range(1, len):

        for j in range(i):
            print(" ", end="")

        for k in range((2*(len-i))-1):
            print("*", end="")

        print()

def pascalPattern(len):
    
    # Upper section
    for i in range(len):

        for j in range(len - (i+1)):
            print(" ", end="")
        
        for j in range(i+1):
            print("*", end="")
        
        print()

    # Lower section
    for i in range(len):

        for j in range(i):
            print(" ", end="")

        for k in range(len-i):
            print("*", end="")

        print()

def hourglassPattern(len):

    # Upper Section
    for i in range(len):

        for j in range(i):
            print(" ", end="")

        for k in range((2*(len-i))-1):
            print("*", end="")

        print()

    # Lower section
    for i in range(1, len):

        for j in range((len-i)-1):
            print(" ", end="")

        for k in range((2*(i-1))+3):
            print("*", end="")    
        
        print()

def butterflyPattern(len):

    # Upper section
    for i in range(len):

        for j in range(i):
            print("*", end="")
        
        for k in range((2*(len-i))-2):
            print(" ", end="")
        
        for l in range(i):
            print("*", end="")
        
        print()

    # Lower section
    for i in range(1, len):

        for j in range(len-(i+1)):
            print("*", end="")

        for k in range(2*i):
            print(" ", end="")

        for l in range(len-(i+1)):
            print("*", end="")
        
        print()
