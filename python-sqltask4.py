import sqlite3

def delete_workout_session(session_id):
    # Connect to the database (replace 'gym.db' with your database file)
    conn = sqlite3.connect('gym.db')
    cursor = conn.cursor()
    
    # SQL query to delete a session
    sql_query = '''DELETE FROM WorkoutSessions WHERE id = ?'''
    
    try:
        # Check if the session exists
        cursor.execute('SELECT * FROM WorkoutSessions WHERE id = ?', (session_id,))
        session = cursor.fetchone()
        
        if session is None:
            print("Error: Session ID does not exist.")
            return
        
        # Execute the SQL query to delete the session
        cursor.execute(sql_query, (session_id,))
        conn.commit()  # Commit the changes
        print("Workout session deleted successfully.")
        
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the connection
        cursor.close()
        conn.close()

# Example usage
delete_workout_session(1)
