import sqlite3

def update_member_age(member_id, new_age):
    # Connect to the database (replace 'gym.db' with your database file)
    conn = sqlite3.connect('gym.db')
    cursor = conn.cursor()
    
    # SQL query to update age
    sql_query = '''UPDATE Members SET age = ? WHERE id = ?'''
    
    try:
        # Check if the member exists
        cursor.execute('SELECT * FROM Members WHERE id = ?', (member_id,))
        member = cursor.fetchone()
        
        if member is None:
            print("Error: Member ID does not exist.")
            return
        
        # Execute the SQL query to update the age
        cursor.execute(sql_query, (new_age, member_id))
        conn.commit()  # Commit the changes
        print("Member age updated successfully.")
        
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the connection
        cursor.close()
        conn.close()

# Example usage
update_member_age(1, 25)
