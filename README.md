## Overview
This script is designed to predict the future closing price of the any index using the Seasonal Autoregressive Integrated Moving Average (SARIMA) model. It is tailored to analyze historical price data and provide a forecast for the next trading day.

## Getting Started

### Prerequisites
- Python 3.x
- pandas library
- statsmodels library

Ensure you have the above prerequisites installed. You can install them using pip:

```bash
pip install pandas statsmodels
```

## Usage

1. Place your historical index data in a CSV file.
2. Ensure your data has a 'Date' column with dates in 'DD.MM.YYYY' format and a 'Current' column with the closing prices.
3. Update the `file_path` variable in the script to the location of your CSV file.
4. Run the script to generate a forecast for the next trading day's closing price.

## Script Details

The script performs the following steps:

- Reads the historical data from the CSV file.
- Converts the 'Date' column to a pandas datetime object and sorts the data by date.
- Cleans the 'Current' column to ensure it is in a proper numeric format.
- Defines and fits the SARIMA model to the historical data.
- Forecasts the next value and prints the result.

## Contributing

Contributions to improve the forecasting script are welcome. Please feel free to fork the repository and submit pull requests.


