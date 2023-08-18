# Firstly Run the Flask Server with Database Connection

This repository contains a simple Flask server that connects to a database. The server is designed to serve as a starting point for building web applications that require database functionality. It demonstrates how to set up a basic Flask application and establish a connection to a SQLite database.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- Flask (`pip install Flask`)
- SQLite (usually included with Python)

## Installation

1. Clone this repository to your local machine using:

   ```bash
   git clone https://github.com/your-username/your-flask-db-app.git
   ```

2. Navigate to the project directory:

   ```bash
   cd your-flask-db-app
   ```

3. Create a virtual environment (recommended):

   ```bash
   python3 -m venv venv
   ```

4. Activate the virtual environment:

   - **Windows:**

     ```bash
     venv\Scripts\activate
     ```

   - **macOS and Linux:**

     ```bash
     source venv/bin/activate
     ```

5. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Open the `config.py` file and update the `DATABASE_URI` with the appropriate database connection URL. it was built using Mysql.

## Running the Server

1. In the terminal, make sure you are in the project directory and your virtual environment is activated.

2. Run the Flask development server:

   ```bash
   python app.py
   ```

3. Open a web browser and navigate to `http://127.0.0.1:5000/` to access the running Flask application.


# Activate the Vue Js application from "ITS SYSTEM" folder, open the readme.md file to run the server.

