import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate sample Facebook ad campaign data
num_campaigns = 10
campaign_ids = range(1, num_campaigns + 1)
sample_data = {
    'Campaign_ID': campaign_ids,
    'Cost_per_Click': np.random.randint(1, 10, size=num_campaigns),
    'Impressions': np.random.randint(1000, 10000, size=num_campaigns),
    'Clicks': np.random.randint(50, 500, size=num_campaigns),
    'Conversions': np.random.randint(5, 50, size=num_campaigns),
    'Revenue': np.random.randint(1000, 5000, size=num_campaigns),
    'Expenditure': np.random.randint(1500, 8000, size=num_campaigns),
    'Returns': np.random.randint(500, 2000, size=num_campaigns)
}

# Manually set Expenditure higher than Returns for campaigns 3 and 10
sample_data['Expenditure'][2] = 8000  # Campaign 3
sample_data['Expenditure'][9] = 7500  # Campaign 10

# Create DataFrame
campaign_data = pd.DataFrame(sample_data)

# Analyze the data
# Calculate ROI for each campaign
campaign_data['ROI'] = (campaign_data['Returns'] - campaign_data['Expenditure']) / campaign_data['Expenditure']

# Identify campaigns with negligible returns (less than 10% ROI)
negligible_return_campaigns = campaign_data[campaign_data['ROI'] < 0.1]['Campaign_ID'].tolist()

# Identify campaigns likely to incur losses (expenditure greater than returns)
loss_incurring_campaigns = campaign_data[campaign_data['Expenditure'] > campaign_data['Returns']]['Campaign_ID'].tolist()

# Print results
print("Campaigns with Negligible Returns:")
print(negligible_return_campaigns)

print("\nCampaigns Likely to Incur Losses:")
print(loss_incurring_campaigns)

# Plot graph
plt.figure(figsize=(10, 6))
plt.bar(campaign_data['Campaign_ID'], campaign_data['Expenditure'], color='blue', label='Expenditure')
plt.bar(campaign_data['Campaign_ID'], campaign_data['Returns'], color='orange', label='Returns')
plt.xlabel('Campaign ID')
plt.ylabel('Amount')
plt.title('Expenditure vs Returns for Campaigns')
plt.legend()
plt.xticks(campaign_data['Campaign_ID'])
plt.show()
