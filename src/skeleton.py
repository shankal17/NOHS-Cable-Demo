"""Files that do the heavy lifting"""

import numpy as np
import matplotlib.pyplot as plt
from config import config

def generate_reduced_error_eqn(h_1, h_2, l):
    """Reduces error function to function of one Variable

    Parameters
    ----------
    h_1 : float
        Sag at leftmost pole (from standard perspective)
    h_2 : float
        Sag at rightmost pole (from standard perspective)
    l : float
        span length of midpspan

    Returns
    -------
    function
        Catenary error function of one variable
    """

    raise NotImplementedError('Ya gotta make an error equation')

def generate_derivative(f, h=1e-10):
    """Computes complex step derivative

    Parameters
    ----------
    f : function
        Function to take derivative of
    x : float
        Coordinate to take derivative
    h : float, optional
        Step size of derivative

    Returns
    -------
    function
        Complex step derivative of function f
    """

    return NotImplementedError('You know derivatives, so do it')

def newton_raphson(f, initial_guess=10, epsilon=1e-10):
    """Finds zero of function f by newton-raphson method.
    
    Parameters
    ----------
    f : function
        Function to find the zero
    initial_guess : float, optional
        Initial guess
    epsilon : float, optional
        Acceptable error to stop at

    Returns
    -------
    function
        Catenary parameter c
    """
    
    raise NotImplementedError('You know the Newton-Raphson method! Make it happen!')

def generate_transformed_catenary(c, x_translation=0, y_translation=0):
    """Generates function encompassing the general catenary equation

    Parameters
    ----------
    c : float
        Catenary parameter
    x_translation : float, optional
        Distance to shift in x-direction
    y_translation : float, optional
        Distance to shift curve in y-direction

    Returns
    -------
    function
       Translated catenary
    """

    raise NotImplementedError('You know algebra, shift that equation!')

def generate_inverse_catenary_eqn(c):
    """Generates function encompassing the inverse of a catenary with param c

    Parameters
    ----------
    c : float
        Catenary parameter

    Returns
    -------
    function
        Inverse catenary equation
    """

    raise NotImplementedError('You know algebra, find the inverse!')

def solve_problem(config):
    """Solves catenary equation modeling rope or cable

    Parameters
    ----------
    config : EasyDict
        Dictionary containing geometry inputs and graphics config
    """

    problem = config.problem
    d_1 = problem.left_attach_height
    d_2 = problem.right_attach_height
    m = problem.midspan_height
    l = problem.span_length

    # Calulate sags
    h_1 = d_1 - m
    h_2 = d_2 - m

    # Generate error function
    error_function = generate_reduced_error_eqn(h_1, h_2, l)

    # Solve for catenary parameter (Newton-Raphson Method)
    c = newton_raphson(error_function)

    # Generate inverse catenary
    inverse_catenary = generate_inverse_catenary_eqn(c)

    # Solve for translations
    x_translation = np.abs(-inverse_catenary(h_1+c))
    y_translation = m - c

    # Generate catenary equation that is transformed into world coordinates
    catenary = generate_transformed_catenary(c, x_translation, y_translation)

    # Plot da ting
    graph_config = config.graph_config
    x = np.linspace(0, l)
    y = catenary(x)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_aspect('equal')
    ax.grid(graph_config.grid)
    ax.set_xlim([-graph_config.x_margin, problem.span_length+graph_config.x_margin])
    ax.set_ylim([0, max(problem.left_attach_height, problem.right_attach_height)+graph_config.y_margin])

    plt.show()

if __name__ == '__main__':
    solve_problem(config)
