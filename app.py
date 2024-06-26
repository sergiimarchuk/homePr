import psycopg2
import datetime
from flask import Flask, render_template, request, redirect, url_for
import matplotlib.pyplot as plt


app = Flask(__name__)

# Connect to the //PostgreSQL database
def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        port="5435",
        database="postgres",
        user="postgres",
        password="123456"
    )
    return conn

# Root route
@app.route('/')
def index():
    return redirect(url_for('list_data'))

# Route for listing data
@app.route('/list')
def list_data():
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        # Query the database tables
        cur.execute("SELECT * FROM my_schema.table_count_data")
        count_data = cur.fetchall()
        cur.execute("SELECT * FROM my_schema.table_picture_counter_data")
        picture_data = cur.fetchall()

        cur.close()
        conn.close()

        return render_template('list.html', count_data=count_data, picture_data=picture_data)
    except Exception as e:
        return str(e), 500

# Route to add count data
@app.route('/add_count_data', methods=['POST'])
def add_count_data():
    counter_data = request.form['counter_data']
    date = request.form['date']
    description = request.form['description']
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO my_schema.table_count_data (counter_data, date, description) VALUES (%s, %s, %s)",
                    (counter_data, date, description))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('list_data'))
    except Exception as e:
        return str(e), 500

# Route to add picture data
@app.route('/add_picture_data', methods=['POST'])
def add_picture_data():
    name_of_picture = request.form['name_of_picture']
    date = request.form['date']
    refer_mongo_entry = request.form['refer_mongo_entry']
    additional_info = request.form['additional_info']
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO my_schema.table_picture_counter_data (name_of_picture, id_count_data, refer_mongo_entry, additional_info)
            VALUES (%s, (SELECT id_count_data FROM my_schema.table_count_data WHERE date = %s), %s, %s)
            """,
            (name_of_picture, date, refer_mongo_entry, additional_info))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('list_data'))
    except Exception as e:
        return str(e), 500

# Route to delete count data
@app.route('/delete_count_data/<int:id>', methods=['POST'])
def delete_count_data(id):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM my_schema.table_count_data WHERE id_count_data = %s", (id,))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('list_data'))
    except Exception as e:
        return str(e), 500

# Route to delete picture data
"""@app.route('/delete_picture_data/<int:id>', methods=['POST'])
def delete_picture_data(id):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM my_schema.table_picture_counter_data WHERE id = %s", (id,))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('list_data'))
    except Exception as e:
        return str(e), 500
"""
# Route to delete picture data
@app.route('/delete_picture_data/<int:id>', methods=['POST'])
def delete_picture_data(id):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM my_schema.table_picture_counter_data WHERE id_picture = %s", (id,))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('list_data'))
    except Exception as e:
        return str(e), 500


# Route to edit count data
@app.route('/edit_count_data/<int:id>', methods=['GET', 'POST'])
def edit_count_data(id):
    if request.method == 'POST':
        counter_data = request.form['counter_data']
        date = request.form['date']
        description = request.form['description']
        try:
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute("""
                UPDATE my_schema.table_count_data
                SET counter_data = %s, date = %s, description = %s
                WHERE id_count_data = %s
                """, (counter_data, date, description, id))
            conn.commit()
            cur.close()
            conn.close()
            return redirect(url_for('list_data'))
        except Exception as e:
            return str(e), 500
    else:
        try:
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute("SELECT * FROM my_schema.table_count_data WHERE id_count_data = %s", (id,))
            data = cur.fetchone()
            cur.close()
            conn.close()
            return render_template('edit_count.html', data=data)
        except Exception as e:
            return str(e), 500

# Route to edit picture data
@app.route('/edit_picture_data/<int:id>', methods=['GET', 'POST'])
def edit_picture_data(id):
    if request.method == 'POST':
        name_of_picture = request.form['name_of_picture']
        date = request.form['date']
        refer_mongo_entry = request.form['refer_mongo_entry']
        additional_info = request.form['additional_info']
        try:
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute("""
                UPDATE my_schema.table_picture_counter_data
                SET name_of_picture = %s, id_count_data = (SELECT id_count_data FROM my_schema.table_count_data WHERE date = %s),
                refer_mongo_entry = %s, additional_info = %s
                WHERE id = %s
                """, (name_of_picture, date, refer_mongo_entry, additional_info, id))
            conn.commit()
            cur.close()
            conn.close()
            return redirect(url_for('list_data'))
        except Exception as e:
            return str(e), 500
    else:
        try:
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute("SELECT * FROM my_schema.table_picture_counter_data WHERE id = %s", (id,))
            data = cur.fetchone()
            cur.close()
            conn.close()
            return render_template('edit_picture.html', data=data)
        except Exception as e:
            return str(e), 500

# Route to add data
@app.route('/add_data', methods=['GET', 'POST'])
def add_data():
    if request.method == 'POST':
        counter_data = request.form['counter_data']
        date_input = request.form['date']
        description = request.form['description']
        name_of_picture = request.form['name_of_picture']
        refer_mongo_entry = request.form['refer_mongo_entry']
        additional_info = request.form['additional_info']
        
        # Handle the empty date input by setting it to today's date
        if not date_input:
            date_input = datetime.date.today().strftime('%Y-%m-%d')
        
        try:
            conn = get_db_connection()
            cur = conn.cursor()
            
            # Insert into table_count_data
            cur.execute("""
                INSERT INTO my_schema.table_count_data (counter_data, date, description)
                VALUES (%s, %s, %s)
                RETURNING id_count_data
                """, (counter_data, date_input, description))
            id_count_data = cur.fetchone()[0]
            
            # Insert into table_picture_counter_data
            cur.execute("""
                INSERT INTO my_schema.table_picture_counter_data (name_of_picture, id_count_data, refer_mongo_entry, additional_info)
                VALUES (%s, %s, %s, %s)
                """, (name_of_picture, id_count_data, refer_mongo_entry, additional_info))
            
            conn.commit()
            cur.close()
            conn.close()
            
            return redirect(url_for('list_data'))
        except Exception as e:
            return str(e), 500
    else:
        return render_template('add_data.html')

# Route to display the graph
@app.route('/graph')
def display_graph():
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        # Query the database for data from table_count_data and sort it by date
        cur.execute("SELECT counter_data, date FROM my_schema.table_count_data ORDER BY date")
        data = cur.fetchall()

        # Separate the data into lists for counter_data and dates
        counter_data = [record[0] for record in data]
        dates = [record[1] for record in data]

        # Convert date objects to strings with day of the month included
        date_strings = [date.strftime('%Y-%m-%d') for date in dates]

        # Calculate previous values
        previous_counter_data = [counter_data[i-1] if i > 0 else None for i in range(len(counter_data))]

        # Calculate the difference between current and previous values divided by 10
        diff_div_10 = [(counter_data[i] - prev) / 10 if prev is not None else None for i, prev in enumerate(previous_counter_data)]

        # Calculate the difference between current value and initial value
        initial_value = counter_data[0]
        diff_initial = [(value - initial_value) / 10 for value in counter_data] 

        # Create a line plot
        plt.figure(figsize=(10, 6))  # Adjust the size of the figure
        plt.plot(date_strings, counter_data, marker='o', label='Counter Data')

        # Annotate the graph with current, previous, and calculated values
        for i, (value, prev_value, diff, init_diff) in enumerate(zip(counter_data, previous_counter_data, diff_div_10, diff_initial)):
            if prev_value is not None:
                annotation_text = f'P.{prev_value}\nC.{value}\nD.{diff}\nU.{init_diff}'
            else:
                annotation_text = f'C.{value}\nD.{init_diff}'
            plt.annotate(annotation_text, (date_strings[i], value), textcoords="offset points", xytext=(0,10), ha='center')

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

