# Copyright (C) 2016  <Karthik aka arhik>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Trend Tests
"""
import math

def interfail_to_failuretime(interfail):
    """
    Conversion utility from interfailure data to failure time data
    """
    failure_time = [sum(interfail[:i+1]) for i in range(len(interfail))]
    return failure_time


def laplace(interfail):
    """
    Computes Laplace Trend Test Hypothesis
    """
    laplace_data = [0]
    failure_time = interfail_to_failuretime(interfail)
    for i in range(1,len(interfail)):
        for j in range(1,i):
            U = (float((sum(failure_time[:j]))) - (i)*(failure_time[i]/2))/failure_time[i]*math.sqrt((1/12.)*(i))
            laplace_data.append(U)
    return laplace_data


def running_arithmetic_avg(interfail):
    """
    Computes the Running Arithmetic Average 
    """
    pass


def run():
    """
    Runs the Laplace Trend Test for a given file
    """
    import matplotlib
    import matplotlib.pyplot as plt
    matplotlib.rcParams.update({ 'font.size':22})
    fig = plt.figure()
    fig.suptitle("FI Failure Intensity")
    ax = fig.add_subplot(111)
    ax.set_title("MVF")
    ax.set_xlabel("FC")
    ax.set_ylabel("FT")
    with open("/home/arhik/SYS") as f:
        t = f.read()
        g = t.split(",")
        g = [float(i) if i!='ComplexInfinity' else 0.0 for i in g]
        plt.step(laplace(g),'k', linewidth = 1.0)
    plt.grid()
    plt.show()

if __name__=='__main__':
    run()

