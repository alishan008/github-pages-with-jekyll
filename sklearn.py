import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import statsmodels.api as sm

# Assuming df is your DataFrame with the holiday packages dataset
# Replace 'choice_column' with the actual column representing the chosen package

# Select relevant covariates
covariates = ['grade', 'cat', 'beds', 'bkg_wp', 'fare', 'size', 'location', 'low_cost',
              'past_customer', 'duration_grp', 'premium_paid']

# Standardize the covariates
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df[covariates])

# Choose the number of clusters (latent classes)
num_clusters = 2
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
df['cluster'] = kmeans.fit_predict(df_scaled)

# Perform logistic regression for each cluster
results = []
for cluster_id in range(num_clusters):
    cluster_data = df[df['cluster'] == cluster_id]

    X = sm.add_constant(cluster_data[covariates])
    y = (cluster_data['choice_column'] == 'chosen_alternative').astype(int)

    model = sm.Logit(y, X)
    result = model.fit()
    results.append(result)

    print(f"\nResults for Cluster {cluster_id}:\n")
    print(result.summary())

# Access class probabilities and other model attributes
class_probs = [result.predict(X) for result in results]
class_memberships = [cluster_data.index for cluster_data in df.groupby('cluster').index]
