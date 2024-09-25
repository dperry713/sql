import sqlite3

def add_member(member_id, name, age):
    # Connect to the database (replace 'gym.db' with your database file)
    conn = sqlite3.connect('gym.db')
    cursor = conn.cursor()
    
    # SQL query to add a new member
    sql_query = '''INSERT INTO Members (id, name, age) VALUES (?, ?, ?)'''
    
    try:
        # Execute the SQL query
        cursor.execute(sql_query, (member_id, name, age))
        conn.commit()  # Commit the changes
        print("Member added successfully.")
    except sqlite3.IntegrityError:
        print("Error: Member ID already exists. Please use a unique ID.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the connection
        cursor.close()
        conn.close()

# Example usage
add_member(1, 'John Doe', 25)
