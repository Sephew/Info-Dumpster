import math
import pandas as pd
n1 = 89
n2 = 18


halving=[n1]

while (min(halving) > 1):
    halving.append(math.floor(min(halving)/2)) #appends to the smallest digit the wholenumber /2 of the current smallest digit


doubling=[n2]

while(len(doubling) < len(halving)):
    doubling.append(doubling[-1]*2) #appends to the top most digit the wholenumber * 2 of the current top most digit
    #can also be written as "doubling.append(max(doubling)*2)"

half_double = pd.DataFrame(zip(halving,doubling)) #zips together halving & doubling using pandas' DataFrame
print(half_double) #I wanted to see the DataFrame
half_double = half_double.loc[half_double[0]%2 == 1,:] #locates [row,column] the condition for the row is it needs to be a whole number through checking using modulo, while the column is all columns indicated with ":"
print("------------------\nHalf_Double After Removing Even Numbers")
print(half_double)
answer = sum(half_double.loc[:,1]) #adds together all rows, on the "1th" column
print(answer)

import matplotlib.pyplot as plt

# Original DataFrame
print("Original DataFrame")
print(half_double)

# Filtered DataFrame
print("\nFiltered DataFrame (Odd Halving Values Only)")
print(filtered_half_double)

# Visualization
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# Bar plot for original data
ax[0].bar(half_double['Halving'], half_double['Doubling'], color='blue')
ax[0].set_title('Original Halving and Doubling Values')
ax[0].set_xlabel('Halving')
ax[0].set_ylabel('Doubling')

# Bar plot for filtered data
ax[1].bar(filtered_half_double['Halving'], filtered_half_double['Doubling'], color='green')
ax[1].set_title('Filtered (Odd Halving Values)')
ax[1].set_xlabel('Halving')
ax[1].set_ylabel('Doubling')

plt.show()
