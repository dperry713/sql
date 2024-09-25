import mysql.connector
from mysql.connector import Error

def add_member(member_id, name, age):
    try:
        # Connect to the MySQL database (replace with your database credentials)
        conn = mysql.connector.connect(
            host='your_host',
            database='your_database',
            user='your_username',
            password='your_password'
        )
        if conn.is_connected():
            cursor = conn.cursor()
            
            # SQL query to add a new member
            sql_query = '''INSERT INTO Members (id, name, age) VALUES (%s, %s, %s)'''
            
            try:
                # Execute the SQL query
                cursor.execute(sql_query, (member_id, name, age))
                conn.commit()  # Commit the changes
                print("Member added successfully.")
            except mysql.connector.IntegrityError:
                print("Error: Member ID already exists. Please use a unique ID.")
            except Exception as e:
                print(f"An error occurred: {e}")
            finally:
                # Close the connection
                cursor.close()
                conn.close()
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

# Example usage
add_member(1, 'John Doe', 25)

