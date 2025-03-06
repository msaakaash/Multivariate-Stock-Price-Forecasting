#  💹 Multivariate Stock Price Prediction - LSTM
This project implements a time series multivariate analysis using RNN/LSTM for stock price predictions. A deep RNN model was created and trained on five years of historical Google stock price data to forecast the stock performance over a two-month period.

## 📌 Features
| Topic | Description |
|-------------------------------|------------------------------------------------|
| **Multivariate Analysis** | Uses multiple stock features (Open, High, Low, Close, Adjusted Close, Volume) for robust predictions. |
| **LSTM-based Approach** | Leverages RNN/LSTM to model sequential dependencies in stock price data. |
| **Explainability (SHAP)** | Analyzes feature importance to interpret model decisions. |
| **Visualization (TensorBoard)** | Monitors training performance and helps in debugging. |
| **Deployment (TF Serving)** | Provides a scalable and production-ready model hosting solution. |
| **NLP Integration (FinBERT)** | Enhances predictions by incorporating financial sentiment analysis. |


## ⚒️ Project Workflow

| Phase | Tasks | Milestone |
|-------|-------|-----------|
| **Phase 1: Data Collection & Preprocessing** | - Collect stock data (Yahoo Finance) <br> - Clean, normalize & split data <br> - Perform feature engineering | Dataset is preprocessed and ready for training |
| **Phase 2: Model Development (LSTM)** | - Implement LSTM model <br> - Fine-Tuning hyperparameters <br> - Train on historical stock data | Trained LSTM model with initial performance metrics |
| **Phase 3: Inference, Explainability & Visualization** | - Model Inference <br> - Apply SHAP for feature importance <br> - Integrate TensorBoard for monitoring | Insights from SHAP and TensorBoard |
| **Phase 4: Deployment & Optimization** | - Deploy model using TensorFlow Serving <br> - Optimize for latency (quantization, batching) | Hosting model with API endpoints |
| **Phase 5: NLP Integration (FinBERT)** | - Process financial news data <br> - Use FinBERT to add sentiment scores <br> - Retrain model with sentiment-enhanced features | Improved predictions with sentiment analysis |


## 🌏 Potential Impact and Applications

- **Investment Strategy Enhancement**: Empowers investors and financial analysts with AI-driven insights to optimize stock market decision-making.  
- **Advanced Risk Management in Trading**: Enables proactive identification of market trends and potential fluctuations, minimizing financial risks.  
- **Scalable & Production-Ready Deployment**: Easily deployable as a REST API for real-time, high-performance stock price prediction applications.  




## 🛠️ Architectural Diagram  
The following diagram represents the architecture of the stock price prediction model:  

![LSTM Architecture Diagram](assets/architecture.png)


## 📥 Data Set ([Google Stock Price](https://finance.yahoo.com/quote/GOOG/history))
The dataset utilized comprises historical records for the stock price of [Alphabet Inc. (GOOG)](https://finance.yahoo.com/quote/GOOG/history), captured on daily basis.

The dataset is sourced from [Yahoo Finance](https://finance.yahoo.com/) and contains the following fields: *Opening price, Highest price, Lowest price, Closing price, Adjusted closing price, and Trading volume*.

The raw, interim, and preprocessed datasets can be located in their corresponding subfolders in the main data directory.


## 📂 Repository Structure
```
💹 Multivariate Stock Price Prediction
├── 📂assets
│   ├──architecture.png
├── 📂data
│   ├──📂interim
|   │   ├──google_stock_price_recent.csv
│   ├──📂 raw
|   │   ├──google_stock_price_full.csv
├── 📂notebooks
│   ├──stockMarketForecasting.ipynb
├── README.md

```

## 👨🏾‍💻 Tech Stack
- **Python** 🐍  
- **TensorFlow/Keras** 🔥
- **LSTM**
- **NumPy & Pandas** 📊
- **TensorBoard**
- **Matplotlib** 📉
- **FinBERT - Hugging Face**🤗


## 👥Development Team
- `Aakaash M S`
- `Karthik Ram S`
- `Aniketha Prasad`
- `Riya Rajesh`

## 🤝 Contributing  
Contributions are welcome! Feel free to fork the repository, work on new features, and submit pull requests.  

## 📝 License  
This project is licensed under the MIT License. 
