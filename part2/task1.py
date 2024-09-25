import sqlite3

def get_members_in_age_range(start_age, end_age):
    # Connect to the database (replace 'gym.db' with your database file)
    conn = sqlite3.connect('gym.db')
    cursor = conn.cursor()
    
    # SQL query using BETWEEN to fetch members within the specified age range
    sql_query = '''SELECT name, age FROM Members WHERE age BETWEEN ? AND ?'''
    
    try:
        # Execute the SQL query with the provided age range
        cursor.execute(sql_query, (start_age, end_age))
        # Fetch all results
        members = cursor.fetchall()
        
        # Print the results
        if members:
            for member in members:
                print(f"Name: {member[0]}, Age: {member[1]}")
        else:
            print("No members found in this age range.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the connection
        cursor.close()
        conn.close()

# Example usage
get_members_in_age_range(25, 30)
