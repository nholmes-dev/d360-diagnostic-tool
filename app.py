import sqlite3

#FUNCTION 1

#Just a simple function to connect to our database file
def get_db_conn():
    my_connection = sqlite3.connect("d360_uat_mock_schema.db")
    return my_connection


#FUNCTION 2

#Simple validation checking if data is correct using if statements
def check_data(id_number, council_name):
    if id_number < 0:
        print("Error: ID cannot be negative")
        return False
    if council_name == "":
        print("Error: Name cannot be blank")
        return False
    return True


#Setting up db and inserting
def run_setup():
    #Call our reusable function
    conn = get_db_conn()
    cursor = conn.cursor()
    
    #Make a simple table for our council diagnostic metrics
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS uat_logs (
            id INTEGER PRIMARY KEY,
            name TEXT,
            size REAL,
            status TEXT
        )
    ''')
    
    #Simple arrays of mock data to insert
    #Using generic council names for privacy compliance
    cursor.execute("INSERT OR REPLACE INTO uat_logs VALUES (101, 'Council_Alpha_UAT', 45.2, 'Healthy')")
    cursor.execute("INSERT OR REPLACE INTO uat_logs VALUES (104, 'Council_Beta_UAT', 12.8, 'Degraded')")
    cursor.execute("INSERT OR REPLACE INTO uat_logs VALUES (102, 'Council_Gamma_UAT', 89.1, 'Healthy')")
    cursor.execute("INSERT OR REPLACE INTO uat_logs VALUES (103, 'Council_Delta_UAT', 31.5, 'Critical')")
    
    conn.commit()
    conn.close()


#Read, update and delete flow
def do_crud_ops():
    conn = get_db_conn()
    cursor = conn.cursor()
    
    #Read rows
    print("\n--- Executing CRUD: READ (Initial State) ---")
    cursor.execute('SELECT * FROM uat_logs')
    all_rows = cursor.fetchall()
    for row in all_rows:
        print("ID:", row[0], "| Name:", row[1], "| Size:", row[2], "GB | Status:", row[3])
        
    #Update rows (Fixing the degraded council status)
    print("\n--- Executing CRUD: UPDATE (Fixing Beta Council status) ---")
    cursor.execute("UPDATE uat_logs SET status = 'Healthy' WHERE id = 104")
    conn.commit()
    
    #Delete rows (Removing stale Delta council cache data)
    print("\n--- Executing CRUD: DELETE (Removing stale Delta Council cache) ---")
    cursor.execute("DELETE FROM uat_logs WHERE id = 103")
    conn.commit()
    
    #Fetch final data for our algorithms to use later
    cursor.execute('SELECT * FROM uat_logs')
    updated_rows = cursor.fetchall()
    
    conn.close()
    return updated_rows


#ALGORITHMS SECTION

#Basic bubble sort to arrange lists by database size
def basic_bubble_sort(my_list):
    #Convert list of tuples to a normal list of lists so we can swap them
    normal_list = []
    for item in my_list:
        normal_list.append(list(item))
        
    length = len(normal_list)
    #Simple nested loops for sorting
    for i in range(length):
        for j in range(0, length - i - 1):
            if normal_list[j][2] > normal_list[j+1][2]:
                #Classic temp swap variable style
                temp = normal_list[j]
                normal_list[j] = normal_list[j+1]
                normal_list[j+1] = temp
    return normal_list


#Simple binary search to find a matching ID
def basic_binary_search(sorted_list, target):
    low = 0
    high = len(sorted_list) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid][0] == target:
            return sorted_list[mid]
        elif sorted_list[mid][0] < target:
            low = mid + 1
        else:
            high = mid - 1
    return None


#RUN SCRIPT
if __name__ == "__main__":
    print("Initializing D360 Azure SaaS Environment Database Health Diagnostic Tool...")
    
    run_setup()
    remaining_data = do_crud_ops()
    
    print("\n--- Running Classical Algorithm: Bubble Sort (By DB Size) ---")
    sorted_data = basic_bubble_sort(remaining_data)
    for line in sorted_data:
        print("Tenant:", line[1], "| Sorted Size:", line[2], "GB")
        
    #Quick standard sort by ID so binary search works properly
    remaining_data.sort() 
    print("\n--- Running Classical Algorithm: Binary Search (Looking for ID 104) ---")
    match = basic_binary_search(remaining_data, 104)
    if match != None:
        print("Target Found! => Tenant:", match[1], "| Status:", match[3])