
def test_while():
    N = 5
    i = 0
    while i < N:
        print (i, end=" ")
        i = i+1
    print("")

def test_double():
    dx = 0.1
    xmin = 0.0
    xmax = 1.0
    x = xmin
    while x <= xmax:
        print(f"{x:.16e}")
        x = x + dx

if __name__ == "__main__":
    #test_while()
    test_double()
else:
    print("I am being imported")