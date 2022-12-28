import sympy as smp
import pprint

if __name__ == "__main__":
    x,y = smp.symbols('x y')
    y = (smp.sin(x)**2)
    y_prime = smp.diff(y)
    print(y)
    print(y_prime)
    print(y_prime2)