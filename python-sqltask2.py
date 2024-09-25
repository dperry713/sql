import sqlite3

def add_workout_session(member_id, date, duration_minutes, calories_burned):
    # Connect to the database (replace 'gym.db' with your database file)
    conn = sqlite3.connect('gym.db')
    cursor = conn.cursor()
    
    # SQL query to add a new workout session
    sql_query = '''INSERT INTO WorkoutSessions (member_id, date, duration_minutes, calories_burned) VALUES (?, ?, ?, ?)'''
    
    try:
        # Check if the member ID exists
        cursor.execute('SELECT * FROM Members WHERE id = ?', (member_id,))
        if cursor.fetchone() is None:
            print("Error: Invalid member ID.")
            return
        
        # Execute the SQL query
        cursor.execute(sql_query, (member_id, date, duration_minutes, calories_burned))
        conn.commit()  # Commit the changes
        print("Workout session added successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the connection
        cursor.close()
        conn.close()

# Example usage
add_workout_session(1, '2024-09-25', 30, 250)
