from flask import Flask, render_template
import psycopg2
import matplotlib.pyplot as plt
import datetime

app = Flask(__name__)

# Connect to the PostgreSQL database
def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        port="5435",
        database="postgres",
        user="postgres",
        password="123456"
    )
    return conn

# Route to display the graph when visiting the root URL
@app.route('/')
def display_graph():
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        # Query the database for data from table_count_data
        cur.execute("SELECT counter_data, date FROM my_schema.table_count_data")
        data = cur.fetchall()

        # Separate the data into lists for counter_data and dates
        counter_data = [record[0] for record in data]
        dates = [record[1] for record in data]

        # Convert date objects to strings with day of the month included
        date_strings = [date.strftime('%Y-%m-%d') for date in dates]

        # Create a line plot
        plt.plot(date_strings, counter_data, marker='o')
        plt.title('Counter Data Over Time')
        plt.xlabel('Date')
        plt.ylabel('Counter Data')
        plt.grid(True)
        plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
        plt.tight_layout()
        
        # Save the plot as a temporary file in the 'static' folder
        temp_file_path = 'static/counter_data_plot.png'
        plt.savefig(temp_file_path)
        
        plt.close()  # Close the plot to avoid displaying it in the browser
        
        # Pass the temporary file path to the template
        return render_template('graph.html', plot_image=temp_file_path)
        
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)

