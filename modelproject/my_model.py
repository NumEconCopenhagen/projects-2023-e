import numpy as np
import sympy as sm

def steady_state_eq(pi, g, b, alpha1, alpha2, h, s, y_bar, pi_star, gamma):
    y, pi, g, b, alpha1, alpha2, h, s, y_bar, pi_star = sm.symbols('y pi g b alpha1 alpha2 h s y_bar pi_star')
    z = alpha1/(1 + alpha2*b)*(g - y_bar)
    alpha = alpha2*h/(1 + alpha2*b)
    AD = y - y_bar - alpha*(pi - pi_star) - z

    gamma = sm.symbols('gamma')
    AS = pi - pi_star + gamma*(y - y_bar) + s

    steady_state_eq = sm.solve(sm.Eq(AD, AS), y)[0]
    return steady_state_eq

def ss_func(pi, g, b, alpha1, alpha2, h, s, y_bar, pi_star, gamma):
    eq = steady_state_eq(pi, g, b, alpha1, alpha2, h, s, y_bar, pi_star, gamma)
    ss_func = sm.lambdify((pi, g, b, alpha1, alpha2, h, s, y_bar, pi_star, gamma), eq)
    return ss_func(pi, g, b, alpha1, alpha2, h, s, y_bar, pi_star, gamma)

def ad(y, pi, pi_star, alpha, alpha_1, alpha_2, b, g, g_bar, h):
    z = alpha_1 / (1 + alpha_2 * b) * (g - g_bar)
    return y - y_bar - z + alpha * (pi - pi_star)

def as_curve(y, pi, pi_1, gamma, s):
    return pi - pi_1 - gamma * (y - y_bar) - s

def social_loss(par, *args):
    pi, g, b, alpha1, alpha2, h, s, y_bar, pi_star, gamma = args
    y = ss_func(pi, g, b, alpha1, alpha2, h, s, y_bar, pi_star, gamma)
    return (y_bar - y)**2 + (pi_star - pi)**2











