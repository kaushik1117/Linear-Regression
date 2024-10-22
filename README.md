# Interactive Linear Regression Streamlit App

This is a Streamlit-based web application that performs linear regression on a dataset. The app allows users to:

- Visualize regression results with interactive Plotly charts.
- Predict salary based on user input (e.g., years of experience).
- Upload and preprocess their own CSV file, handling missing values automatically.

## Features

- **Interactive Visualization:** The app uses Plotly to display a scatter plot of actual data points and a regression line.
- **User Input for Predictions:** Users can input years of experience (or any other chosen feature), and the app will predict the corresponding salary using the trained model.
- **CSV Preprocessing:** Missing data (NaN values) are automatically filled with column means before performing the regression.

## Tech Stack

- **Python:** Core language used in the project.
- **Streamlit:** Framework for building interactive web apps.
- **Pandas:** For data manipulation and analysis.
- **Scikit-learn:** To perform linear regression.
- **Plotly:** For interactive data visualizations.

## Setup Instructions

### Clone the Repository

Start by cloning the project repository to your local machine:

```bash
git clone https://github.com/<your-username>/<your-repository-name>.git
cd <your-repository-name>
```
### Set Up a Virtual Environment

To avoid conflicts with other projects, create and activate a virtual environment.

**For Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**For macOS/Linux:**

To create and activate a virtual environment, run:

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

With the virtual environment activated, install the required dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Running the Application

To run the application, use the following command:

```bash
streamlit run main.py
```

### Running the Application

To run the application, use the following command:

```bash
streamlit run main.py
```

This will start a local Streamlit server. Open the URL (usually http://localhost:8501) in your web browser to access the app.