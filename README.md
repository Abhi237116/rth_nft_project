Ethereum Gas Fees vs. NFT Market Activity
This project analyzes the causal impact of Ethereum gas prices on NFT market transaction volume and minting activity.

We use time series analysis (ARIMAX, Granger Causality) and causal inference (CausalImpact) to determine if high gas fees reduce or merely delay NFT sales.

Data Source
All historical data (gas prices, NFT sales, NFT mints) is fetched from the Dune Analytics API using pre-defined SQL queries.

## 🚀 Quick Start

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/](https://github.com/)[your-username]/[your-repo-name].git
    cd [your-repo-name]
    ```

2.  **Install Dependencies:**
    ```bash
    # Create and activate a virtual environment
    python -m venv venv
    source venv/bin/activate

    # Install required libraries
    pip install -r requirements.txt
    ```

3.  **Set Up API Key:**
    * Copy the example environment file: `cp .env.example .env`
    * Open the new `.env` file and paste your Dune API key:
        ```bash
        DUNE_API_KEY="YOUR_API_KEY_HERE"
        ```

4.  **Run the Analysis:**
    * **Data Collection:** Run `notebooks/01_data_collection.ipynb` to fetch data and create `data/merged_timeseries.csv`.
    * **Modeling:** Open and run `notebooks/02_exploratory_analysis.ipynb` and `notebooks/03_time_series_modeling.ipynb`.

