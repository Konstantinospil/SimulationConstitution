def trunc_gauss(mu, sigma, low, up):
    """
    Generates a random float with gaussian distribution within a certain range.
    :param mu: Mean of the distribution
    :param sigma: Standard deviation
    :param low: Lower bound
    :param up: Upper bound
    :return: float between top and bottom
    """
    fl = random.gauss(mu,sigma)
    while not (low <= fl <= up):
        fl = random.gauss(mu,sigma)
    return fl

def save(filename,source):
    """
    A function to save the results of the simulation
    :param filename: The destination file
    :param source: The object of type simulation to be written on a file
    :return: None
    """