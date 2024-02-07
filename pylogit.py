import pandas as pd
from pylogit import MixedLogit

# Assuming df is your DataFrame with the holiday packages dataset
# Replace 'choice_column' with the actual column representing the chosen package

# Select relevant covariates
covariates = ['grade', 'cat', 'beds', 'bkg_wp', 'fare', 'size', 'location', 'low_cost',
              'past_customer', 'duration_grp', 'premium_paid']

# Specify the availability of alternatives
availability_vars = {'grade': 'all', 'cat': 'all', 'beds': 'all', 'bkg_wp': 'all',
                     'fare': 'all', 'size': 'all', 'location': 'all', 'low_cost': 'all',
                     'past_customer': 'all', 'duration_grp': 'all', 'premium_paid': 'all'}

# Create a dictionary to specify the utility equations for each covariate
utilities_specification = {covariate: 'all_same' for covariate in covariates}

# Specify the mixing distribution for latent classes
num_latent_classes = 2  # You can adjust this based on your exploration
mixing_vars = covariates  # Use the same covariates for mixing distribution

# Create the Mixed Logit model
model = MixedLogit(data=df, mixing_id_col='id', mixing_vars=mixing_vars,
                   observation_id_col='obs_id', choice_col='choice_column',
                   availability_vars=availability_vars,
                   num_draws=100, num_alts=len(df['choice_column'].unique()),
                   mixing_id_choice_col='choice_column',
                   mixing_distribution=utilities_specification,
                   mixing_id_col='id', # Assuming 'id' is an identifier for each observation
                   panel_data=True, allow_panel_to_lapse=True,
                   seed=42)

# Fit the model
model.fit()

# Print the model summary
print(model.get_statsmodels_summary())

# Access class probabilities and other model attributes
class_probs = model.get_mixing_distribution()
class_memberships = model.predict(data=df, mixing_id_col='id', choice_col='choice_column')
---------------------------------------------------------------------------------------------

model_specification = {
    'covariate1': (covariates.index('grade'), 'grade', 'all_same'),
    'covariate2': (covariates.index('cat'), 'cat', 'all_same'),
    'covariate3': (covariates.index('beds'), 'beds', 'all_same'),
    'covariate4': (covariates.index('bkg_wp'), 'bkg_wp', 'all_same'),
    'covariate5': (covariates.index('fare'), 'fare', 'all_same'),
    'covariate6': (covariates.index('size'), 'size', 'all_same'),
    'covariate7': (covariates.index('location'), 'location', 'all_same'),
    'covariate8': (covariates.index('low_cost'), 'low_cost', 'all_same'),
    'covariate9': (covariates.index('past_customer'), 'past_customer', 'all_same'),
    'covariate10': (covariates.index('duration_grp'), 'duration_grp', 'all_same'),
    'covariate11': (covariates.index('premium_paid'), 'premium_paid', 'all_same'),
}
