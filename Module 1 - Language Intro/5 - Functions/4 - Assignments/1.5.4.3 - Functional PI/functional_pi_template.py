import math


def my_pi(target_error):
    """
    Implementation of Gauss–Legendre algorithm to approximate PI from https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm

    :param target_error: Desired error for PI estimation
    :return: Approximation of PI to specified error bound
    """

    ## Initial values for the algorithm
    a = 1.0
    b = 1.0 / math.sqrt(2)
    t = 0.25
    p = 1.0 
    pi_approx = 0.0 

    while True: 
        # Step 1: Perform Iteration
        a_next = (a+b) / 2
        b_next = math.sqrt(a * b)
        t_next = t - p * (a - a_next) ** 2
        p_next = 2 * p 

        # Step 2: Calculate PI approximation
        pi_approx = (a_next + b_next) ** 2 / (4 * t_next)

        # Step 3: Check if error is within target error bound
        if abs(pi_approx - math.pi) < target_error:
            break

        # Update values for next iteration
        a = a_next
        b = b_next
        t = t_next
        p = p_next

    # change this so an actual value is returned
    return pi_approx




desired_error = 1E-10

approximation = my_pi(desired_error)

print("Solution returned PI=", approximation)

error = abs(math.pi - approximation)

if error < abs(desired_error):
    print("Solution is acceptable")
else:
    print("Solution is not acceptable")
