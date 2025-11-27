import psycopg2
import csv

def connect_db():
    conn = psycopg2.connect(
        host="localhost",
        dbname="phonebook_db",
        user="postgres",
        password="2281488"
    )
    return conn

def create_table():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS phonebook (id SERIAL PRIMARY KEY,name VARCHAR(100),phone VARCHAR(20));")
    conn.commit()
    cur.close()
    conn.close()
    print('table created')

def upload_from_csv(filename):
    conn = connect_db()
    cur = conn.cursor()
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['name']
            phone = row['phone']
            cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()
    print("uploaded successfully")

def entering():
    conn = connect_db()
    cur = conn.cursor()
    while True:
        name = input("Enter name (or 'stop'): ")
        if name.lower() == 'stop':
            break
        phone = input("Enter phone number: ")
        cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()
    print("uploaded successfully")

def update_data():
    conn = connect_db()
    cur = conn.cursor()
    name = input("name for update: ")
    new_name = input("(new) name (or keep empty): ")
    new_phone = input("(new) phone (or keep empty): ")

    if new_name:
        cur.execute("UPDATE phonebook SET name = %s WHERE name = %s", (new_name, name))
    if new_phone:
        cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s", (new_phone, name))

    conn.commit()
    cur.close()
    conn.close()
    print(f"Data of {name} updated")

def query_data():
    conn = connect_db()
    cur = conn.cursor()
    filter_type = input("choose filter (name/phone): ").lower()
    filter_value = input(f"{filter_type}: ")
    
    if filter_type == 'name':
        cur.execute("SELECT * FROM phonebook WHERE name LIKE %s", (f"%{filter_value}%",))
    elif filter_type == 'phone':
        cur.execute("SELECT * FROM phonebook WHERE phone LIKE %s", (f"%{filter_value}%",))
    else:
        print("incorrect filter")
        return
    
    rows = cur.fetchall()
    for row in rows:
        print(row)
    
    cur.close()
    conn.close()

def delete_data():
    conn = connect_db()
    cur = conn.cursor()
    filter_type = input("choose filter for deleting (name/phone): ").lower()
    filter_value = input(f"{filter_type}: ")

    if filter_type == 'name':
        cur.execute("DELETE FROM phonebook WHERE name = %s", (filter_value,))
    elif filter_type == 'phone':
        cur.execute("DELETE FROM phonebook WHERE phone = %s", (filter_value,))
    else:
        print("incorrect filter")
        return
    
    conn.commit()
    cur.close()
    conn.close()
    print(f"object {filter_type} = {filter_value} deleted!")

def main():
    create_table()
    
    while True:
        print("\nPhoneBook:")
        print("1. Upload Data from CSV")
        print("2. Enter Data manually")
        print("3. Update Data")
        print("4. Select Data")
        print("5. Delete Data")
        print("6. Exit")
        
        choice = input("Choose movement: ")
        
        if choice == '1':
            filename = input("Enter SCV file name: ")
            upload_from_csv(filename)
        elif choice == '2':
            entering()
        elif choice == '3':
            update_data()
        elif choice == '4':
            query_data()
        elif choice == '5':
            delete_data()
        elif choice == '6':
            break
        else:
            print("incorrect choice! try again.")

if __name__ == "__main__":
    main()