import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX

# Load the data file and prepare the data
file_path = 'YourFile.csv'
data = pd.read_csv(file_path)
data['Date'] = pd.to_datetime(data['Date'], format='%d.%m.%Y')
data = data.sort_values(by='Date')
data['Current'] = data['Current'].str.replace(',', '.').astype(float)

# Define and apply the SARIMA model
# Using SARIMA parameters (1, 1, 1)x(1, 1, 1, 12) - assuming annual seasonality
model = SARIMAX(data['Current'], order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
sarima_result = model.fit()

# Forecast the next value
sarima_forecast = sarima_result.forecast(steps=1)

# Print the forecasted value
print(sarima_forecast)

