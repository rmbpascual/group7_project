#!/usr/bin/env python
from __future__ import division
from random import random
from math import pi
import matplotlib.pyplot as plt



def rain_drop(length_of_field=1):
    return [(.5 - random()) * length_of_field, (.5 - random()) * length_of_field]


def is_point_in_circle(point, length_of_field=1):
    return (point[0]) ** 2 + (point[1]) ** 2 <= (length_of_field / 2) ** 2


def plot_rain_drops(drops_in_circle, drops_out_of_circle, length_of_field=1, format='pdf'):
    number_of_drops_in_circle = len(drops_in_circle)
    number_of_drops_out_of_circle = len(drops_out_of_circle)
    number_of_drops = number_of_drops_in_circle + number_of_drops_out_of_circle
    plt.figure()
    plt.xlim(-length_of_field / 2, length_of_field / 2)
    plt.ylim(-length_of_field / 2, length_of_field / 2)
    plt.scatter([e[0] for e in drops_in_circle], [e[1] for e in drops_in_circle], color='blue', label="Drops in circle")
    plt.scatter([e[0] for e in drops_out_of_circle], [e[1] for e in drops_out_of_circle], color='black', label="Drops out of circle")
    plt.legend(loc="center")
    plt.title("%s drops: %s landed in circle, estimating $\pi$ as %.4f." % (number_of_drops, number_of_drops_in_circle, 4 * number_of_drops_in_circle / number_of_drops))
    plt.savefig("%s_drops.%s" % (number_of_drops, format))


def rain(number_of_drops=1000, length_of_field=1, plot=True, format='pdf', dynamic=False):
    number_of_drops_in_circle = 0
    drops_in_circle = []
    drops_out_of_circle = []
    pi_estimate = []
    for k in range(number_of_drops):
        d = (rain_drop(length_of_field))
        if is_point_in_circle(d, length_of_field):
            drops_in_circle.append(d)
            number_of_drops_in_circle += 1
        else:
            drops_out_of_circle.append(d)
        if dynamic:  # The dynamic option if set to True will plot every new drop (this can be used to create animations of the simulation)
            print "Plotting drop number: %s" % (k + 1)
            plot_rain_drops(drops_in_circle, drops_out_of_circle, length_of_field, format)
        pi_estimate.append(4 * number_of_drops_in_circle / (k + 1))  # This updates the list with the newest estimate for pi.
    # Plot the pi estimates
    plt.figure()
    plt.scatter(range(1, number_of_drops + 1), pi_estimate)
    max_x = plt.xlim()[1]
    plt.hlines(pi, 0, max_x, color='black')
    plt.xlim(0, max_x)
    plt.title("$\pi$ estimate against number of rain drops")
    plt.xlabel("Number of rain drops")
    plt.ylabel("$\pi$")
    plt.savefig("Pi_estimate_for_%s_drops_thrown.pdf" % number_of_drops)

    if plot and not dynamic:
        plot_rain_drops(drops_in_circle, drops_out_of_circle, length_of_field, format)

    return [number_of_drops_in_circle, number_of_drops]


if __name__ == "__main__":
    from sys import argv
    number_of_drops = 100
    if len(argv) > 1:
        number_of_drops = eval(argv[1])
    r = rain(number_of_drops, plot=True, format='png', dynamic=False)
    print "----------------------"
    print "%s drops" % number_of_drops
    print "pi estimated as:"
    print "\t%s" % (4 * r[0] / r[1])
    print "----------------------"