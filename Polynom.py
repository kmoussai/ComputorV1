
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
    

    def solve(self):
        if self.degree > 2:
            print("The polynomial degree is stricly greater than 2, I can't solve.")
        else:
            pass



    def __str__(self):
        items = sorted(self.expression.items())
        ans = ""
        for expo, coeff in items:
            if expo == 0:
                ans += str(int(coeff) if coeff.is_integer() else coeff) + " * X^0 "
            else:
                ans += (("+ " if coeff > 0 else "- " )
                    + str(abs(int(coeff) if coeff.is_integer() else coeff)) + " * X^"
                    + str(expo) + " ")
        ans += "= 0\n"
        ans += "Polynomial degree: " + str(self.degree)
        return "Reduced form: " + ans




        
        





    

    