import numpy as np
import matplotlib.pyplot as plt

def lyapunov_exponent(r, x, n):
    sum_lyapunov = 0.0
    for _ in range(n):
        x = r * x * (1 - x)
        sum_lyapunov += np.log(np.abs(r - 2 * r * x))
    return sum_lyapunov / n

# Define the range of r values
r_values = np.linspace(3.4, 4.0, 1000)

# Calculate the Lyapunov exponent for each r value
lyapunov_values = [lyapunov_exponent(r-0.075, 0.5, 1000) for r in r_values]

# Define a threshold for chaos detection
chaos_threshold = 0.00  # You can adjust this threshold as needed

# Find indices where Lyapunov exponent crosses the threshold
chaotic_indices = np.where(np.array(lyapunov_values) > chaos_threshold)[0]

# Find the boundaries of each chaotic region
boundaries = np.where(np.diff(chaotic_indices) > 1)[0] + 1

# Initialize lists to store chaotic regions and their widths
chaotic_regions = []
chaotic_widths = []

# Process each chaotic region separately
for i in range(len(boundaries) + 1):
    if i == 0:
        start_index = 0
    else:
        start_index = boundaries[i - 1]
    
    if i == len(boundaries):
        end_index = chaotic_indices[-1] + 1
    else:
        end_index = boundaries[i]

    chaotic_region = r_values[chaotic_indices[start_index:end_index]]
    chaotic_regions.append(chaotic_region)

    # Calculate the width of each chaotic region
    chaotic_width = chaotic_region.max() - chaotic_region.min()
    chaotic_widths.append(chaotic_width)

# Plot the Lyapunov exponent with markers indicating the chaotic regions
plt.plot(r_values, lyapunov_values, 'b-', linewidth=0.5)
plt.scatter(np.concatenate(chaotic_regions), [chaos_threshold] * len(chaotic_indices), color='red', marker='.', s=2, label='Chaotic Region')
plt.xlabel('r')
plt.ylabel('Lyapunov Exponent')
plt.title('Lyapunov Exponent - Logistic Map with Chaotic Regions')
plt.legend()
plt.show()



# Print the width of each chaotic region
# for i, width in enumerate(chaotic_widths, 1):
#     print(f"Width of Chaotic Region {i}: {width}")

