
import sys
import Polynom as poly

if __name__ == "__main__":
    

    # "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
    # 4 * X^0 + 4 * X^1 - 9.3 * X^2 = 0
    # 4 * X^0 + 4 * X^1 - 9.3 * X^2 = 0
    # 4 * X^0 + 4 * X^1 - 9.3 * X^2 = 0
    # 4 * X^0 + 4 * X^1 - 9.3 * X^2 
    pol = poly.Polynom()
    pol.addElem(5, 0)
    pol.addElem(4, 1)
    pol.addElem(-9.3, 2)
    pol.addElem(-1, 0)

    print(pol)