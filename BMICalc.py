underweight = range(1, 20)
normal = range(20, 26)
aboveavg = range(26, 31)
obese = range(31, 40)



class fact:
    def shee(*args):
        try:
            askweight = int(input("Enter your weight in pounds:"))
        except ValueError:
            print("Enter a number")
        except TypeError:
            print("One of your inputs is not a number")
        except ZeroDivisionError:
            print("You don't weigh 0")
        else:
            return askweight

    def eesh(*args):
        try:
            askheight = int(input("Enter height in inches:"))
        except ValueError:
            print("Enter a number")
        except TypeError:
            print("One of your inputs is not a number")
        except ZeroDivisionError:
            print("You entered 0 for either inputs")
        else:
            return askheight


class BMI:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def vari(weight, height):
        try:
            x = int(703 * (weight / (height ** 2)))
        except ValueError:
            print("Variable is not a number")
        except TypeError:
            print("Values are incompatible, check your input")
        except ZeroDivisionError:
            print("You inputed a 0")
        else:
            return x

    def shtalk(vari):
        if vari in underweight:
            print("You are underweight. Nurish yourself food please.")
        elif vari in normal:
            print("You average, keep it up.")
        elif vari in aboveavg:
            print("You're either slightly overweight or quite muscular")
        elif vari in obese:
            print("You are likely obese or very muscular.")
        elif vari > 41:
            print("Theres a problem with the program or you're extremely obese")
        else:
            return shtalk


class funke:
    def diff(*args):
        if BMI.vari(kiya, kiki) in underweight:
            ok = underweight[-1]
            top1 = ok - BMI.vari(kiya, kiki)
            tweight1 = (top1 / 703) * height ** 2
            print(
                "You will need to gain" + " " + tweight1 + "pounds to go up a tier. You shouldnt try to lose more weight")

        elif BMI.vari(kiya, kiki) in normal:
            ok = normal[-1]
            ko = normal[2]
            top1 = ok - BMI.vari(kiya, kiki)
            bottom1 = BMI.vari(kiya, kiki) - ko
            tweight1 = (top1 / 703) * height ** 2
            bweight1 = (bottom1 / 703) * height ** 2
            print("You will need to gain" + " " + tweight1 + "pounds to go up a tier and lose " + bweight1
            + " to go down a pound")

        elif BMI.vari(kiya, kiki) in aboveavg:
            ok = aboveavg[-1]
            ko = aboveavg[2]
            top1 = ok - BMI.vari(kiya, kiki)
            bottom1 = BMI.vari(kiya, kiki) - ko
            tweight1 = (top1 / 703) * height ** 2
            bweight1 = (bottom1 / 703) * height ** 2
            print("You will need to gain" + " " + tweight + "pounds to go up a tier and lose " + bweight1 +
            " to go down a pound")

        elif BMI.vari(kiya, kiki) in obese:
            ok = obese[-1]
            ko = obese[2]
            top1 = ok - BMI.vari(kiya, kiki)
            bottom1 = BMI.vari(kiya, kiki) - ko
            tweight1 = (top1 / 703) * height ** 2
            bweight1 = (bottom1 / 703) * height ** 2
            print("You will need to gain" + " " + tweight + "pounds to go up a tier and lose " + bweight1 +
            " to go down a pound")
        else:
            ok = obese[-1]
            bottom1 = BMI.vari(kiya, kiki) - ok
            bweight1 = (bottom1 / 703) * height ** 2
            print("You will need to lose" + " " + bweight + "pounds to go down a tier and you really should")



kiya = fact.shee()
kiki = fact.eesh()

print("Your BMI is" + " " + str(BMI.vari(kiya, kiki)))
print(str(BMI.shtalk(BMI.vari(kiya, kiki))))

print("Test")
