import math

x = input("CAPE or Updraft Speed? (c = CAPE, u = Updraft)\n\n\n\n")

if x == "c" or "C":
    cape = int(input("What is the CAPE value? (J/kg) \n\n\n\n" ))
    Wvelmps = (math.sqrt(2*cape))/2
    Wvel = (Wvelmps)*2.23694
    Wvelmph = round(Wvel,)
else:
    Wvelmps = int(input("What is the Updraft Speed? (m/s) \n\n\n\n" ))
    Wvel = (Wvelmps)*2.23694
    Wvelmph = round(Wvel,)



'''
<24 mph    bb pellet         <1/4 inch
24 mph     pea                1/4 inch
35 mph     marble             1/2 inch
38 mph     dime              7/10 inch
40 mph     penny              3/4 inch
46 mph     nickel             7/8 inch
49 mph     quarter              1 inch
54 mph     half dollar      1 1/4 inch
60 mph     walnut           1 1/2 inch
64 mph     golf ball        1 3/4 inch
69 mph     hen egg              2 inch
77 mph     tennis ball      2 1/2 inch
81 mph     baseball         2 3/4 inch
84 mph     tea cup              3 inch
98 mph     grapefruit           4 inch
103 mph    softball         4 1/2 inch

'''

if Wvelmph <24:
    hail = "BB pellet"
    size = "< 1/4 inch"
elif Wvelmph in range (24,35):
    hail = "Pea Sized"
    size = "1/4 inch"
elif Wvelmph in range (35,38):
    hail = "Marble Sized"
    size = "1/2 inch"
elif Wvelmph in range (38,40):
    hail = "Dime Sized"
    size = "7/10 inch"
elif Wvelmph in range (40,46):
    hail = "Penny Sized"
    size = "3/4 inch"
elif Wvelmph in range (46,49):
    hail = "Nickel Sized"
    size = "7/8 inch"
elif Wvelmph in range (49,54):
    hail = "Quarter Sized"
    size = "1 inch"
elif Wvelmph in range (54,60):
    hail = "Half Dollar Sized"
    size = "1 1/4 inches"
elif Wvelmph in range (60,64):
    hail = "Walnut Sized"
    size = "1 1/2 inches"
elif Wvelmph in range (64,69):
    hail = "Golf Ball Sized"
    size = "1 3/4 inches"
elif Wvelmph in range (69,77):
    hail = "Hen Egg Sized"
    size = "2 inches"
elif Wvelmph in range (77,81):
    hail = "Tennis Ball Sized"
    size = "2 1/2 inches"
elif Wvelmph in range (81,84):
    hail = "Baseball Sized"
    size = "2 3/4 inches"
elif Wvelmph in range (84,98):
    hail = "Tea Cup Sized"
    size = "3 inches"
elif Wvelmph in range (98,103):
    hail = "Grapefuit Sized"
    size = "4 inches"
elif Wvelmph in range (103,110):
    hail = "Soft Ball Sized"
    size = "4 1/2 inches"
else:
    hail = "Softball Sized or Larger"
    size = "4 1/2 inches or bigger"


print("\n\n\n\nThe Updraft Velocity is about",Wvelmph,"mph", "("+str(round(Wvelmps,2))+" m/s)")
print("Hail sizes up to about",hail,"("+size+")")
