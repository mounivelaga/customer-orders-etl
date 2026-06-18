Customer Orders ETL Pipeline
Project Overview

This project implements an End-to-End ETL (Extract, Transform, Load) pipeline using Python, REST APIs, Pandas, and PostgreSQL.

The pipeline extracts customer order data from a REST API, transforms the raw JSON into a structured tabular format, and loads the processed data into a PostgreSQL database.

This project demonstrates real-world Data Engineering concepts including:

REST API Integration
ETL Pipeline Design
Object-Oriented Programming (OOP)
Data Transformation with Pandas
PostgreSQL Data Loading
Logging and Monitoring
Configuration Management
Architecture
REST API
    │
    ▼
Extractor
    │
    ▼
Raw JSON File
(raw_data/orders.json)
    │
    ▼
Transformer
    │
    ▼
Pandas DataFrame
    │
    ▼
Loader
    │
    ▼
PostgreSQL Database
Project Structure
customer-orders-etl/
│
├── config/
│   └── config.json
│
├── database/
│   └── db_connection.py
│
├── extract/
│   └── extractor.py
│
├── transform/
│   └── transformer.py
│
├── load/
│   └── loader.py
│
├── utils/
│   └── logger.py
│
├── raw_data/
│   └── orders.json
│
├── logs/
│   └── etl.log
│
├── main.py
├── requirements.txt
└── README.md
Technologies Used
Technology	Purpose
Python	ETL Development
Requests	REST API Integration
Pandas	Data Transformation
PostgreSQL	Data Storage
SQLAlchemy	Database Connectivity
Psycopg2	PostgreSQL Driver
Logging	Monitoring & Troubleshooting
ETL Workflow
Extract
Fetches customer order data from a REST API.
Validates API response.
Saves raw API response into a JSON file.

Output:

raw_data/orders.json
Transform

Transforms nested JSON data into a structured format.

Output Columns:

Column
order_id
customer_name
product_name
quantity
unit_price
total_amount

Business Logic:

total_amount = quantity * unit_price
Load

Loads transformed data into PostgreSQL using SQLAlchemy.

Target Table:

orders
Database Schema
CREATE TABLE orders (
    order_id INTEGER,
    customer_name VARCHAR(100),
    product_name VARCHAR(255),
    quantity INTEGER,
    unit_price NUMERIC(10,2),
    total_amount NUMERIC(12,2)
);
Configuration

The API endpoint is configured through:

{
    "api_url": "https://dummyjson.com/carts"
}

File:

config/config.json
Installation
Clone Repository
git clone <repository-url>
cd customer-orders-etl
Create Virtual Environment
python -m venv .venv
Activate Environment

Windows:

.venv\Scripts\activate

Git Bash:

source .venv/Scripts/activate
Install Dependencies
pip install -r requirements.txt
Run ETL Pipeline
python main.py

Successful Output:

ETL Pipeline Completed Successfully
Logging

Pipeline execution logs are stored in:

logs/etl.log

Example:

2026-06-17 22:00:10 - INFO - Extraction Started
2026-06-17 22:00:11 - INFO - Raw data saved
2026-06-17 22:00:12 - INFO - Transformation Completed
2026-06-17 22:00:13 - INFO - Loading Completed
Sample Output
order_id	customer_name	product_name	quantity	unit_price	total_amount
1	Customer_33	iPhone	2	999.99	1999.98
1	Customer_33	Charger	1	50.00	50.00
Skills Demonstrated
Python Programming
Object-Oriented Programming
REST API Consumption
JSON Processing
ETL Pipeline Development
Pandas Data Transformation
PostgreSQL Integration
SQLAlchemy
Logging & Monitoring
Configuration Management
Future Enhancements
Incremental Loading
Error Handling & Retry Logic
Data Validation Framework
Unit Testing with Pytest
Dockerization
Airflow Orchestration
Cloud Deployment (AWS/GCP/Azure)
Author

Mouni

Data Engineering Portfolio Project