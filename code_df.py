# Assuming df is your DataFrame containing 'date', 'vkey', 'meta', 'cat', and 'index' columns

import pandas as pd

# Convert 'date' column to datetime if it's not already in the datetime format
df['date'] = pd.to_datetime(df['date'])

# Get unique dates and vkeys
unique_dates = df['date'].unique()
unique_vkeys = df['vkey'].unique()

# Create an empty dictionary to store maximum values for each combination of date, vkey, and cat
max_values = {}

# Loop through unique dates
for date in unique_dates:
    # Loop through unique vkeys
    for vkey in unique_vkeys:
        # Filter the DataFrame for the current date and vkey combination
        filtered_df = df[(df['date'] == date) & (df['vkey'] == vkey)]
        
        # Initialize a dictionary to store max values for each cat
        cat_max_values = {}
        
        # Loop through unique cats
        for cat in filtered_df['cat'].unique():
            # Find the max value for the current cat
            max_value = filtered_df[filtered_df['cat'] == cat]['index'].max()
            cat_max_values[cat] = max_value
        
        # Update the max_values dictionary with the current date, vkey, and max values for each cat
        max_values[(date, vkey)] = cat_max_values

# Convert the max_values dictionary to a Pandas Series
max_values_series = pd.Series(max_values)

# Create a DataFrame by concatenating the series from the dictionary
new_df = pd.concat([max_values_series.apply(pd.Series)], keys=max_values_series.index).reset_index()
new_df.columns = ['date', 'vkey', 'cat'] + list(new_df.columns[3:])

# Display the new DataFrame
print(new_df)
