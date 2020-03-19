import matplotlib.pyplot as plt
import numpy as np
import sys


filename = sys.argv[1]        # Stores ARG1 in filename, as in: $ python plot.py ARG1 ARG2 
datax = np.loadtxt(filename,skiprows= 33, delimiter = ',',usecols = (2))   # Attempts to load filename into local variable data.
datay = np.loadtxt(filename, skiprows = 33, delimiter = ',', usecols = (3))


## Part 0
# Figure out what arguments to add to the loadtxt function call
# so that numbers are loaded into the local function 'data'.
# Hint: look for arguments like 'skiprows' and 'delimiter', skip row 0-32
# Check by running:
#   $ python plot.py raw-data/Sp15_245L_sect-001_group-1_glass.raw
# at the command line.

plt.plot(datax,datay, color = 'k', linestyle = '-', label = filename + 'Stress vs. Strain')
plt.legend(loc='best')
plt.xlabel('Strain (MPa)')
plt.ylabel('Stress (N)')
plt.title('Engineering strain curve')

## Part 1
# Figure out what columns and rows of data we need to plot
# Stress (y-axis) vs Strain (x-axis)
# plot raw-data/Sp15_245L_sect-001_group-1_glass.raw
# Make sure to include axis labels and units!
# plt.plot(xdata,ydata, arguments-to-make-plot-pretty)


## Part 2
# Check to see if your code in part 1 will plot all of the files in raw-data/
# Edit the files (use git liberally here!) to make them more usable


## Part 3
# Use linear regression to calculate the slope of the linear part of
# the stress-strain data. Plot your line against the data to make 
# sure it makes sense! Use the slope of this line to calculate and print
# the Young's modulus (with units!)


x_mean = np.mean(datax)
y_mean = np.mean(datay) 

a_1 = np.sum(datay*(datax-x_mean))/np.sum(datax*(datax-x_mean))
a_0 = y_mean - a_1*x_mean
reg = a_0 + a_1 * datax

plt.figure(figsize = (20,10))

plt.scatter(datax, datay, color = 'blue', linestyle = '-')
plt.plot(datax, reg, 'k--', linewidth = 2, label = 'Linear regression')

plt.xlabel('Strain(N)')
plt.ylabel('Stress(MPa)')
plt.title('Linear regression')

plt.legend(loc = 'best', fontsize = 14)
plt.grid();

plt.savefig('Out.png')

## Part 4
# Modify your code to save your plots to a file and see if you can generate
# plots and Young's moduli for all of the cleaned up files in your data 
# directory. If you haven't already, this is a good time to add text to 
# your .gitignore file so you're not committing the figures to your repository.

run = datax[-1] - datax[0]
rise = reg[-1] - reg[0]
slope = str(int(rise/run)) + ' N/MPa'
print(slope)






