# Survey Tool - Income & Expense Analysis

##  Overview
A Flask web app for collecting spending data, storing in MongoDB, processing with Python, and visualizing in Jupyter Notebook.

 Steps to Solve the Assignment
1. Set Up Flask – Create a web application to collect user data.
2. Connect to MongoDB – Store user details, income, and expenses.
3. Design the HTML Form – A simple webpage for user input.
4. Create the User Class – Fetch, process, and store data in CSV.
5. Load CSV in Jupyter Notebook – Perform data analysis.
6. Data Visualization – Create income vs. age and spending by gender charts.
7. Deploy to AWS – Host the Flask app on Amazon Web Services

##  Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Run Flask app: `python app.py`
3. Fetch CSV data: `python data_processing.py`
4. Open `data_analysis.ipynb` for visualizations.

##  Deployment
Deployed on AWS EC2.


##  Summary
1.  Flask app collects income and expenses.
2.  MongoDB stores data, and we export it as CSV.
3.  Matplotlib & Seaborn for visualizations.
4.  AWS Deployment allows access from anywhere.
