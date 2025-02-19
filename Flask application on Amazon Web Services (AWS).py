import os
import sys
import subprocess

# Function to check if Flask is installed
def check_flask():
    try:
        import flask
        print("✅ Flask is already installed!")
    except ImportError:
        print("❌ Flask not found. Installing now...")
        install_flask()

# Function to install Flask
def install_flask():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
        subprocess.check_call([sys.executable, "-m", "pip", "install", "flask"])
        print("✅ Flask installed successfully!")
    except Exception as e:
        print(f"⚠️ Error installing Flask: {e}")

# Function to set up a virtual environment (Recommended)
def setup_virtual_env():
    venv_dir = "venv"
    if not os.path.exists(venv_dir):
        print("📌 Creating virtual environment...")
        subprocess.check_call([sys.executable, "-m", "venv", venv_dir])
        print("✅ Virtual environment created!")
    
    # Activate virtual environment (Windows & macOS/Linux)
    if os.name == "nt":
        activate_script = os.path.join(venv_dir, "Scripts", "activate")
    else:
        activate_script = os.path.join(venv_dir, "bin", "activate")

    print(f"🔄 Activate your virtual environment using:\nsource {activate_script} (macOS/Linux) or {venv_dir}\\Scripts\\activate (Windows)")
    print("Then install Flask again using:\n pip install flask")

# Run setup functions
if __name__ == "__main__":
    setup_virtual_env()
    check_flask()


# Install pymongo if not installed
try:
    import pymongo
except ModuleNotFoundError:
    import os
    os.system("pip install pymongo")
    import pymongo  # Try importing again

# Import required libraries
from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Initialize Flask app
app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["survey_db"]  # Create a database named 'survey_db'
collection = db["users"]  # Create a collection (table) named 'users'

@app.route("/", methods=["GET", "POST"])
def index():
    """
    Handles both GET and POST requests.
    - GET: Displays the form to collect user data.
    - POST: Saves form data to MongoDB and redirects to home.
    """
    if request.method == "POST":
        # Collect form data
        user_data = {
            "name": request.form["name"],
            "age": int(request.form["age"]),
            "gender": request.form["gender"],
            "income": float(request.form["income"]),
            "expenses": {
                "utilities": float(request.form.get("utilities", 0)),
                "entertainment": float(request.form.get("entertainment", 0)),
                "school_fees": float(request.form.get("school_fees", 0)),
                "shopping": float(request.form.get("shopping", 0)),
                "healthcare": float(request.form.get("healthcare", 0))
            }
        }
        # Insert data into MongoDB
        collection.insert_one(user_data)
        return redirect("/")  # Refresh page after form submission

    return render_template("index.html")  # Display HTML form


class User:
    """
    The User class is responsible for fetching and processing user data.
    - fetch_data(): Retrieves data from MongoDB and saves it as a CSV file.
    - load_data(): Loads the saved CSV file for visualization.
    """

    def __init__(self):
        """ Initialize MongoDB connection """
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["survey_db"]
        self.collection = self.db["users"]

    def fetch_data(self):
        """ Retrieve data from MongoDB and store it as a CSV file. """
        data = list(self.collection.find({}, {"_id": 0}))  # Exclude MongoDB's default '_id' field
        df = pd.DataFrame(data)  # Convert to Pandas DataFrame
        df.to_csv("user_data.csv", index=False)  # Save as CSV file
        print("Data saved to user_data.csv")

    def load_data(self):
        """ Load data from CSV file for visualization. """
        if os.path.exists("user_data.csv"):
            return pd.read_csv("user_data.csv")
        else:
            print("CSV file not found. Fetching new data...")
            self.fetch_data()
            return pd.read_csv("user_data.csv")


def visualize_data():
    """
    Generates two key visualizations:
    1. Income vs. Age
    2. Gender-based spending distribution
    """
    user = User()
    df = user.load_data()  # Load data from CSV file

    # Visualization 1: Income vs Age
    plt.figure(figsize=(10, 5))
    sns.barplot(x=df["age"], y=df["income"], palette="coolwarm")
    plt.title("Income by Age")
    plt.xlabel("Age")
    plt.ylabel("Income")
    plt.savefig("income_vs_age.png")  # Save the plot
    plt.show()

    # Reshape DataFrame for better visualization
    df_melted = df.melt(id_vars=["gender"], value_vars=["expenses.utilities", "expenses.entertainment",
                                                         "expenses.school_fees", "expenses.shopping",
                                                         "expenses.healthcare"], var_name="Expense Type",
                         value_name="Amount Spent")

    # Visualization 2: Spending by Gender
    plt.figure(figsize=(12, 6))
    sns.barplot(x="Expense Type", y="Amount Spent", hue="gender", data=df_melted)
    plt.title("Spending Distribution by Gender")
    plt.savefig("spending_by_gender.png")  # Save the plot
    plt.show()


# Run Flask app
if __name__ == "__main__":
    app.run(debug=True)

    # Fetch data and visualize once the app is running
    user = User()
    user.fetch_data()
    visualize_data()
