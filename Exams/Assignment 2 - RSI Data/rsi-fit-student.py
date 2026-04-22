import pandas as pd
import numpy as np
from scipy.stats import norm, chisquare, ttest_ind, ttest_1samp
import matplotlib.pyplot as plt

"""
Preamble: Load data from source CSV file
"""
path_to_datafile =  r"C:\Users\maddi\OneDrive\Documents\GitHub\ENGR315-sp2026-student\data\drop-jump\all_participant_data_rsi.csv"  ### I was having trouble using the short path, so I added the full path to access the data file

data = pd.read_csv(path_to_datafile)   ### Loading the data from the CSV file ###

RSI_accel = data["accelerometer_rsi"]    ### Making variables for the data
RSI_fp = data['force_plate_rsi']            ### Making variables for the data 
"""
Question 1: Load the force plate and acceleration based RSI data for all participants. Map each data set (accel and FP)
to a normal distribution. Clearly report the distribution parameters (mu and std) and generate a graph two each curve's 
probability distribution function. Include appropriate labels, titles, and legends.
"""
print('-----Question 1-----')

mu_accel, std_accel = norm.fit(RSI_accel)    ### Mean   ### Standard Deviation (a, b)

mu_fp, std_fp= norm.fit(RSI_fp)          ### Mean ### Standrd Deviation (a, b)

print('Force Plate Mean:', mu_fp)     ### Printing Force Plate Mean Value
print('Force Plate Standard Deviation:', std_fp)    ### Printing Foce Plate Standard Deviation

print('Acceleration Mean;', mu_accel)     ### Printing Acceleration Mean
print('Acceleration Standard Deviation:', std_accel)    ### Printing Acceleration Standard Deviation

x = np.linspace(0, 2, 50)   ### Making the X axis and saying how many point I want between 0 and 2
### Naming the curves for the graph 
curve_accel = norm.pdf(x, mu_accel, std_accel)
curve_rsi = norm.pdf(x, mu_fp, std_fp)

### Plot of the Curves 
plt.figure()
plt.plot(x, curve_accel, label="Acceleration")
plt.plot(x, curve_rsi, label="Force Plate")

### Labels 
plt.title("RSI Normal Distributions")
plt.xlabel("RSI")
plt.ylabel("Probability")
plt.show()
"""
Question 2: Conduct a Chi2 Goodness of Fit Test for each dataset to test whether the data is a good fit
for the derived normal distribution. Clearly print out the p-value, chi2 stat, and an indication of whether it is 
a fit or not. Do this for both acceleration and force plate distributions. It is suggested to generate 9 bins between 
[0,2), add append -inf and +inf to both ends of the bins. An alpha=0.05 is suitable for these tests.
"""
print('\n\n-----Question 2-----')
alpha = 0.05
bins = np.linspace(0, 2, 10) ### Creating the 9 bins
bins = np.concatenate(([-np.inf], bins, [np.inf])) ### Makes the string of bins end to end 
"""
Acceleration
"""
count_accel, _ = np.histogram(RSI_accel, bins=bins)   ### Counts RSI values in each "bin"
vals_accel = norm.cdf(bins, mu_accel, std_accel)      #### Finding the expected values from the normal distribution
expected_accel = len(RSI_accel) * np.diff(vals_accel)

chi2_accel, p_accel = chisquare(count_accel, expected_accel)   ### Chi2 Goodness of Fit Test 
### Printing the results from the chi test
print("\nAcceleration")
print("chi2", chi2_accel)
print("p-value", p_accel)

### Checkin if it is a normal fit 
if p_accel > 0.005:
    print("normal fit")
else:
    print("Not a normal fit")
"""
Force Plate
"""
#### Following the same procedure for the Force Plate Data
count_fp, _ = np.histogram(RSI_fp, bins=bins)
vals_fp = norm.cdf(bins, mu_fp, std_fp)
expected_fp = len(RSI_fp) * np.diff(vals_fp)
chi2_fp, p_fp = chisquare(count_fp, expected_fp)
### Print the values from the test
print("\nForce Plate:")
print('chi2:', chi2_fp)
print("p-value:", p_fp)
### Check to see if it is a normal fit 
if p_fp > 0.05:
    print("Normal Fit")
else:
    print("Not a normal fit")
"""
Question 3: Perform a t-test to determine whether the RSI means for the acceleration and force plate data are equivalent 
or not. Clearly report the p-value for the t-test and make a clear determination as to whether they are equal or not.
An alpha=0.05 is suitable for these tests.
"""
print('\n\n-----Question 3-----')

### ttest to compare the means
t_stat, p_ttest = ttest_ind(RSI_accel, RSI_fp) 
### Deciding if the means are different 
### The p-value 
print("p-value:", p_ttest) 
if p_ttest > 0.05:
    print("Means are evaluated to be the same")
else:
    print("The Means are not the same")
"""
Question 4: Calculate the RSI Error for the dataset where error is expressed as the difference between the 
Force Plate RSI measurement and the Accelerometer RSI measurement. Fit this error distribution to a normal curve and 
plot a histogram of the data on the same plot showing the fitted normal curve. Include appropriate labels, titles, and 
legends. The default binning approach from matplot lib with 16 bins is sufficient.
"""

### YOUR CODE HERE