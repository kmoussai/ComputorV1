
class Polynom:

    
    

    def __init__(self):
        self.expression = {}
        self.degree = 0


    def addElem(self, coeff, exponent):
        self.degree = max(self.degree, exponent)
        try:
            self.expression[exponent] += coeff
        except:
            self.expression[exponent] = coeff
        

    def printPoly(self):
        print(self.expression)
    def reducedForm(self):
        items = sorted(self.expression.items())
        ans = ""
        for expo, coeff in items:
            if expo == 0:
                ans += str(coeff) + " * X^0 "
                # print(coeff, "* X^0", end=" ")
            else:
                ans += (("+ " if coeff > 0 else "- " )+ str(abs(coeff)) + " * X^" + str(expo) + " ")
                # print("+" if coeff > 0 else "-", abs(coeff), "* X^" + str(expo),end=" ")
        return ans + "= 0"
    def __str__(self):
        items = sorted(self.expression.items())
        ans = ""
        for expo, coeff in items:
            if expo == 0:
                ans += str(coeff) + " * X^0 "
                # print(coeff, "* X^0", end=" ")
            else:
                ans += (("+ " if coeff > 0 else "- " )+ str(abs(coeff)) + " * X^" + str(expo) + " ")
                # print("+" if coeff > 0 else "-", abs(coeff), "* X^" + str(expo),end=" ")
        ans += "= 0\n"
        ans += "Polynomial degree: " + str(self.degree)
        return "Reduced form: " + ans




        
        





    

    