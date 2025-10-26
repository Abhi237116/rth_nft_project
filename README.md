

# Ethereum Gas Fees vs. NFT Market Activity: A Causal Analysis ⛽️🖼️

This project investigates the **causal relationship** between **Ethereum gas fees** and **NFT market activity**, specifically transaction volume and minting frequency. By applying a robust suite of time series and causal inference methodologies, we aim to answer a critical question for the crypto economy: **Do high gas fees reduce NFT sales, or merely delay them?**

## 🎯 Project Goal

The primary goal is to empirically determine the impact of Ethereum's fluctuating transaction costs (gas prices) on the behavioral metrics of the Non-Fungible Token (NFT) market. The analysis provides actionable insights into market elasticity and user behavior in response to network congestion and cost spikes.

-----

## 🔬 Methodology

Our analysis employs multiple advanced statistical techniques to triangulate the causal effect:

  * **Time Series Analysis (ARIMAX):** Modeling NFT activity (sales/mints) as a function of its own history and external variables, particularly gas price, to quantify the contemporaneous and lagged correlation.
  * **Granger Causality Testing:** Formally testing the hypothesis that past values of gas fees provide statistically significant information for forecasting future NFT market activity.
  * **Causal Impact Analysis (via Google's CausalImpact):** Leveraging a Bayesian structural time-series model to estimate the counterfactual (what would have happened to NFT activity had gas fees not spiked) during specific periods of high gas price events.

-----

## 📊 Data Source

All required historical time series data is aggregated and fetched from **Dune Analytics**. We utilize pre-defined, optimized SQL queries to collect:

  * **Ethereum Gas Prices (Gwei/USD)**
  * **NFT Market Transaction Volume (USD/ETH)**
  * **NFT Minting Activity (Count)**

-----

## 🚀 Quick Start

Follow these steps to replicate the analysis on your local machine.

### 1\. Clone the Repository

```bash
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd [your-repo-name]
```

### 2\. Install Dependencies

It is highly recommended to use a virtual environment.

```bash
# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # Use `venv\Scripts\activate` on Windows

# Install required libraries from requirements.txt
pip install -r requirements.txt
```

### 3\. Set Up API Key

Access to Dune Analytics data requires an API key.

1.  Copy the example environment file:
    ```bash
    cp .env.example .env
    ```
2.  Open the new `.env` file and paste your **Dune API Key**:
    ```bash
    DUNE_API_KEY="YOUR_API_KEY_HERE"
    ```

### 4\. Run the Analysis

The project is structured across three sequential Jupyter notebooks:

1.  **Data Collection:**
    Run `notebooks/01_data_collection.ipynb` to execute the Dune queries, fetch the historical data, and save the clean, merged time series to `data/merged_timeseries.csv`.

2.  **Exploratory Analysis:**
    Open and run `notebooks/02_exploratory_analysis.ipynb` to perform initial data cleaning, stationarity checks, visualization of trends, and calculation of correlation matrices.

3.  **Modeling & Causal Inference:**
    Open and run `notebooks/03_time_series_modeling.ipynb`. This notebook contains the implementation of the ARIMAX models, Granger Causality tests, and the final CausalImpact analysis.

-----

## 📦 Repository Structure

```
.
├── data/
│   └── merged_timeseries.csv       # Output file for all fetched time series data
├── notebooks/
│   ├── 01_data_collection.ipynb    # Fetches data from Dune Analytics
│   ├── 02_exploratory_analysis.ipynb # Initial data visualization and checks
│   └── 03_time_series_modeling.ipynb # ARIMAX, Granger, and CausalImpact models
├── .env.example                    # Template for environment variables
├── .gitignore
├── README.md
└── requirements.txt                # Python dependencies
```


-----
