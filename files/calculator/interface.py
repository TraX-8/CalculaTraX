import time
def arobase(value):
    for i in range(value) :
        print("@", end="", flush=True)
        time.sleep(0.1)
    print("")
    return value


def content(text, border):
    try :
        int(border)
    except :
        print("Incorrect border value : must be an integer.")
        return ValueError
    for i in range(border) :
        print("@", end="", flush=True)
        time.sleep(0.1)
    print(end=" ")
    print(text, end=" ")
    for i in range(border) :
        print("@", end="", flush=True)
        time.sleep(0.1)
    print(end="\n")
    return

def content_sides(text, left, right):
    try :
        int(left)
        int(right)
    except :
        print("Incorrect border value : must be an integer.")
        return ValueError
    for i in range(left) :
        print("@", end="", flush=True)
        time.sleep(0.1)
    print(end=" ")
    print(text, end=" ")
    for i in range(right) :
        print("@", end="", flush=True)
        time.sleep(0.1)
    print(end="\n")
    return

def textbox(width, text):
    try:
        int(width)
    except:
        print("Width has to be an integer.")
        return ValueError
    if width < len(text) + 2:
        print("Text too long")
        return

    free_space = width - len(text) - 2
    left = free_space // 2
    right = free_space - left
    arobase(width)
    content_sides(text, left, right)
    arobase(width)

def line() :
    print("________________________________________________________________")

def appboot(apptitle, year_and_version, creator):
    leftspace_1 = (40 - len(apptitle)) // 2
    rightspace_1 = 40 - leftspace_1 - len(apptitle)
    leftspace_2 = (40 - (len(year_and_version) + len(creator))) // 2
    rightspace_2 = 40 - leftspace_2 - len(year_and_version) - len(creator) - 5
    print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
    print("|", end="")
    for i in range(leftspace_1):
        print(" ", end="")
    print(apptitle, end="")
    for i in range(rightspace_1):
        print(" ", end="")
    print("|")
    print("|", end="")
    for i in range(leftspace_2):
        print(" ", end="")
    print(f"{year_and_version}, by {creator}", end="")
    for i in range(rightspace_2):
        print(" ", end="")
    print("|")
    print("|________________________________________|")


def division_by_zero():
    print("ERROR : Division by zero.")