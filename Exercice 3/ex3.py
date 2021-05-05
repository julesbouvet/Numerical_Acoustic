from numpy import sin, pi


def calculate_integrals(a, b):

    # trapezoidal (Newton-Cotes 1st-degree) rule
    res = (b-a)*(f(a)+f(b))/2
    print(f'Trapezoidal rule : {res}')

    # Simpson’s (Newton-Cotes 2nd-degree) rule
    res = ((b-a)/6)*(f(a)+4*f(0.5*(a+b))+f(b))
    print(f'Simpson rule : {res}')

    # Simpson’s 3/8 (Newton-Cotes 3rd-degree) rule
    res = ((b-a)/8)*(f(a) + 3*f((2*a+b)/3) + 3*f((a+2*b)/3) + f(b))
    print(f'Simpson 3/8 rule : {res}')

    # Gaussian quadrature (with 1, 2, and 3 integration points)
    y_1 = (b-a)/2
    y_2 = (a+b)/2

    # 1 ineg pt
    res1 = 2*f(y_1*0 + y_2)

    # 2 ineg pts
    res2 = f(-y_1*0.577350 + y_2) + f(y_1 + 0.577350 + y_2)

    # 3 ineg pts
    res3 = 0.555556*f(-y_1*0.774597 + y_2) + 0.8888889*f(y_2)+0.555556*f(y_1*0.774597 + y_2)

    print(f'Gaussian quadrature \n For 1 point: {res1} \n For 2 points: {res2} \n For 3 points: {res3}')
    return


if __name__ == '__main__':

    print('Enter 1 if you want to calculate the integral (I) \n'
          'Enter 2 if you want to calculate the integral (II)\n')
    which_integral = int(input(' Which integral do you want to calculate: '
                               '\n enter your response: '))

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

