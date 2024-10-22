import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import plotly.graph_objs as go

def app():
    st.title("Interactive Linear Regression with Salary Prediction")
    tab1, tab2, tab3 = st.tabs(["Raw DataFrame", "Preprocessed DataFrame", "Linear Regression"])

    with tab1:
        st.header("This is Raw CSV file")
        data = pd.read_csv(r"C:\Users\disha\Desktop\Salary_Data[1].csv")

        # Display the raw data
        st.write("Raw Data Preview:", data)
    with tab2:
        st.header("Preprocess the data: Handle missing values (NaN)")
        st.write("Handling missing data...")

        # Fill missing values with the mean of the respective column
        data['Years of Experience'].fillna(data['Years of Experience'].mean(), inplace=True)
        data['Age'].fillna(data['Age'].mean(), inplace=True)
        data['Salary'].fillna(data['Salary'].mean(), inplace=True)

        st.write("Preprocessed Data Preview:", data)
    with tab3:
        st.header("Analysis using Linear Regression Algorithm")
        # Select feature and target for linear regression
        feature_column = st.selectbox("Select Feature for Prediction (X)", ['Years of Experience', 'Age'])
        target_column = 'Salary'  # Target will be Salary

        # Prepare the data for linear regression
        X = data[[feature_column]].values
        Y = data[target_column].values

        # Create and train the linear regression model
        model = LinearRegression()
        model.fit(X, Y)

        # Predictions
        Y_pred = model.predict(X)

        # Display coefficients
        st.write(f"Intercept: {model.intercept_}")
        st.write(f"Coefficient: {model.coef_[0]}")

        # Create interactive Plotly chart
        fig = go.Figure()

        # Scatter plot of actual values
        fig.add_trace(go.Scatter(x=X.flatten(), y=Y, mode='markers', name='Actual Salary', marker=dict(color='green')))

        # Line plot of predicted values
        fig.add_trace(go.Scatter(x=X.flatten(), y=Y_pred, mode='lines', name='Predicted Salary', line=dict(color='red')))

        # Set chart titles and labels
        fig.update_layout(
            title="Interactive Linear Regression: Salary Prediction",
            xaxis_title=feature_column,
            yaxis_title="Salary",
            showlegend=True,
            hovermode='x'
        )

        # Display the Plotly chart in Streamlit
        st.plotly_chart(fig)

        # Add a section for user input to predict salary based on experience or age
        st.subheader("Predict Salary Based on Experience")
        
        # User input for years of experience or age
        user_input = st.number_input(f"Enter {feature_column}", min_value=0.0, step=0.1)

        # Predict salary based on user input
        if user_input:
            user_prediction = model.predict([[user_input]])
            st.write(f"Predicted Salary for {feature_column}: {user_input} is ${user_prediction[0]:,.2f}")
