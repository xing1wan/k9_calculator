import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import pandas as pd
import sys

# Command line input: Load data from a CSV file
input_file = sys.argv[1]  # First argument: input CSV file path
output_file = sys.argv[2]  # Second argument: output image file path

# Load data from CSV file
data = pd.read_csv(input_file) 

# Extract substrate concentrations and enzyme activity from the CSV
substrate_concentrations = data['concentration'].values
enzyme_activity = data['activity'].values

# Michaelis-Menten equation
def michaelis_menten(S, Vmax, Km):
    return (Vmax * S) / (Km + S)

# Clear the current plot
plt.clf()

# Loop through each unique protein in the data
for protein in data['peak'].unique():
    # Filter data for the current protein
    protein_data = data[data['peak'] == protein]

    # Extract substrate concentrations and enzyme activity
    substrate_concentrations = protein_data['concentration'].values
    enzyme_activity = protein_data['activity'].values

    # Fit the data to the Michaelis-Menten equation
    popt, _ = curve_fit(michaelis_menten, substrate_concentrations, enzyme_activity, bounds=(0, np.inf))

    # Extracting Vmax and Km
    Vmax, Km = popt

    # Plotting each protein on the same plot
    plt.scatter(substrate_concentrations, enzyme_activity, label=f'Data ({protein})')
    plt.plot(substrate_concentrations, michaelis_menten(substrate_concentrations, *popt), 
             label=f'Fit: $V_{{max}}$=%.2f, $K_m$=%.2f ({protein})' % (Vmax, Km))


# Finalize the plot
plt.xlabel('Substrate concentration (µM)')
plt.ylabel('Reaction velocity (V)')
plt.legend()

# Save the combined plot as an image
plt.savefig(output_file) # Save each plot with the protein name
plt.show()