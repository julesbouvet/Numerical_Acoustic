from numpy import sin, pi


def calculate_integrals(a, b):
    method = int(input('Which method do you want to use?'
                       '\n enter your response: '))

    # trapezoidal (Newton-Cotes 1st-degree) rule
    if method == 1:
        res = (b-a)*(f(a)+f(b))/2

    # Simpson’s (Newton-Cotes 2nd-degree) rule
    if method == 2:
        res = ((b-a)/6)*(f(a)+4*f(0.5*(a+b))+f(b))

    # Simpson’s 3/8 (Newton-Cotes 3rd-degree) rule
    if method == 3:
        res = ((b-a)/8)*(f(a) + 3*f((2*a+b)/3) + 3*f((a+2*b)/3) + f(b))

    # Gaussian quadrature (with 1, 2, and 3 integration points)
    if method == 4:
        y_1 = (b-a)/2
        y_2 = (a+b)/2

        # 1 ineg pt
        res1 = 2*f(y_1*0 + y_2)

        # 2 ineg pts
        res2 = f(-y_1*0.577350 + y_2) + f(y_1 + 0.577350 + y_2)

        # 3 ineg pts
        res3 = 0.555556*f(-y_1*0.774597 + y_2) + 0.8888889*f(y_2)+0.555556*f(y_1*0.774597 + y_2)

        print(f'The results are \n For 1 point: {res1} \n For 2 points: {res2} \n For 3 points: {res3}')
        return

    print(f'The integral equals {res}')
    return


if __name__ == '__main__':

    print('Enter 1 if you want to calculate the integral (I) \n'
          'Enter 2 if you want to calculate the integral (II)\n')
    which_integral = int(input(' Which integral do you want to calculate: '
                               '\n enter your response: '))

    print('\n\n Enter 1 if you want to use the trapezoidal rule '
          '\n Enter 2 if you want to use the Simpson’s rule'
          '\n Enter 3 if you want to use the Simpson’s 3/8 rule'
          '\n Enter 4 if you want to use the Gaussian quadrature \n')

    if which_integral == 1:

        def f(x):
            return x ** 4 - 1

        calculate_integrals(0, 4)

        correct_answer = (4**5 /5) - 4
        print(f'\n The correct answer was {correct_answer}')

    if which_integral == 2:

        def f(x):
            return sin(x) ** 2

        calculate_integrals(0, pi)

        correct_answer = pi**2 /4
        print(f'\n The correct answer was {correct_answer}')