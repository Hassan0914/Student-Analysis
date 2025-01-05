import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('Global Health Statistics.csv')


df['Population Affected'] = pd.to_numeric(df['Population Affected'], errors='coerce')

# Total population affected by the disease of Malaria
filtered_data = df[df['Disease Name'].str.contains('Malaria', case=False, na=False)]
total_population_affected = filtered_data['Population Affected'].sum()
print(f"Total population affected by Malaria: {total_population_affected:,}")

# Aggregate data: Total population affected per disease
aggregated_data = df.groupby('Disease Name', as_index=False)['Population Affected'].sum()

# Find the most and least common diseases
most_common_disease = aggregated_data.loc[aggregated_data['Population Affected'].idxmax()]
least_common_disease = aggregated_data.loc[aggregated_data['Population Affected'].idxmin()]

print("Most Common Disease: ", most_common_disease)
print("Least Common Disease: ", least_common_disease)

# Create the bar chart
fig, ax = plt.subplots(figsize=(12, 6))

# Plot the data
bars = ax.bar(
    x=aggregated_data["Disease Name"], 
    height=aggregated_data["Population Affected"], 
    color="r", 
    align="center", 
    edgecolor="black"
)

# Show exact population values in millions above the bars
for bar, value in zip(bars, aggregated_data["Population Affected"]):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f'{value / 1_000_000:.1f}M',  # Convert to millions and format
        ha='center',
        va='bottom',
        fontsize=8
    )

# Format the y-axis to show values in millions
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x / 1_000_000:.1f}M'))

# Set y-axis range
ax.set_ylim(0, aggregated_data["Population Affected"].max() * 1.1)  # Add 10% for space

# Rotate x-axis labels for better readability
ax.set_xticks(range(len(aggregated_data["Disease Name"])))
ax.set_xticklabels(aggregated_data["Disease Name"], rotation=45, ha='right')

# Add labels and title
ax.set_xlabel("Disease Name")
ax.set_ylabel("Population Affected (in Millions)")
ax.set_title("Global Health Statistics")

# Add gridlines for better visualization
ax.yaxis.grid(True, linestyle='--', alpha=0.6)

# Display the plot
plt.tight_layout()
plt.show()
