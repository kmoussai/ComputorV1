
import sys
import Polynom as poly


def Help():
    print("usage: python3 arg [option] ... [-P | -I]")
    print("-P   :Plot fuction in 2D")

if __name__ == "__main__":

    try:
        first, second = sys.argv[1].lower().replace(' ', '').split("=")
        # print(elem.replace('*','').split("x^"))
        pol = poly.Polynom()
        for elem in first.replace('-', "+-").split("+"):
            coef, exp = elem.replace('*','').split("x^")
            coef = coef if coef != '' else 1
            pol.addElem(float(coef), int(exp))
        for elem in second.replace('-', "+-").split("+"):
            print(elem.replace('*','').split("x^"))
            coef, exp = elem.replace('*','').split("x^")
            coef = coef if coef != '' else 1
            pol.addElem(-1 * float(coef), int(exp))
        print(pol)
        pol.solve()
    except:
        pass
        # Help() 