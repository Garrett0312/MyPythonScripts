
Tm = input("What is Tmax (C)? Enter warmest temp(C) in lowest 500mb.\n\n\n\n")

if Tm == "f" or Tm == "F":
    Tm = float(input("Enter the Tmax in fahrenheit \n\n\n\n"))
    Tm = (Tm-32)*(5/9)
else:
    Tm = float(Tm)

print('%d\N{DEGREE SIGN}C' %Tm)

TmK = (Tm + 273.15)

if TmK > 271.16:
    SLR = round(12+2*(271.16-TmK),)
else:
    SLR = round(12+(271.16-TmK),)

print("The estimated Kuchera Snow/Liquid Ratio is",str(SLR)+":1")