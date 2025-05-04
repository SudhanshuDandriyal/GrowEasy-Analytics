# GrowEasy-Analytics

## Overview
GrowEasy-Analytics is a Flask-based web application designed to provide quick sales insights for small to medium-sized businesses without the need for complex BI tools. Users can upload sales data (e.g., CSV files) via a web interface, and the app generates analytical reports with visualizations, supporting decisions on inventory management, marketing strategies, and customer engagement.

This project showcases my ability to build end-to-end analytics solutions—from data processing and visualization to cloud deployment—making it a strong portfolio piece for data science roles in tech and fintech industries.

## Features
- **Data Processing**: Processes sales data to compute monthly trends, top products, customer segmentation, and sales forecasts using pandas and numpy.
- **Visualization**: Generates dual plots (e.g., monthly sales trends, top products) using matplotlib, displayed on the web interface.
- **Deployment**: Deployed on AWS EC2 (xxxxx) with Gunicorn; also configured for Elastic Beanstalk.
- **Error Handling**: Includes solutions for SMTP authentication errors (e.g., email reports via Gmail) and dependency issues (e.g., Flask installation).

## Tech Stack
- **Languages/Frameworks**: Python, Flask, Gunicorn
- **Libraries**: pandas, matplotlib, numpy
- **Deployment**: AWS EC2, Elastic Beanstalk, Git
- **Environment**: Ubuntu server (EC2 instance)

## Setup Instructions
1. Clone the repository: `git clone https://github.com/SudhanshuDandriyal/GrowEasy-Analytics.git`
2. Navigate to the project directory: `cd GrowEasy-Analytics`
3. Create a virtual environment: `python3 -m venv venv`
4. Activate the virtual environment: `source venv/bin/activate`
5. Install dependencies: `pip install -r requirements.txt`
6. Run the app: `flask run` or `gunicorn -w 4 -b 0.0.0.0:8000 app:app`
7. Access the app at `http://localhost:5000` (or your deployed URL).

## Usage
- Upload a CSV file (e.g., `sales_data.csv`) with columns `date`, `product`, `amount`, and `customer_id`.
- View generated reports and visualizations, including sales trends and top products.

## About Me
I’m Sudhanshu Dandriyal, a Data Scientist at ICICI Bank with expertise in risk analytics, machine learning, and cloud deployment. This project demonstrates my skills in Python, data analytics, and building scalable solutions, aligning with my goal to secure senior data science roles in tech or fintech (e.g., Amazon, Flipkart, Paytm).

## Future Improvements
- Add machine learning models (e.g., LightGBM) for enhanced sales forecasting.
- Implement user authentication for improved security.
- Expand visualizations with interactive dashboards using Plotly or Dash.

## Contact
- LinkedIn: [Sudhanshu Dandriyal](https://www.linkedin.com/in/analyticalsudhanshudandriyal/)
- Email: [Sudhanshudadndriyal7@gmail.com]
