import psycopg2
import csv

def connect_db():
    conn = psycopg2.connect(
        host="localhost",
        dbname="postgres",
        user="postgres",
        password="2281488"
    )
    return conn

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

def update_data():
    conn = connect_db()
    cur = conn.cursor()
    way = input("choose a way how you'll insert(by list or manually): ")

    if way == 'manually':
        name = input("name: ")
        phone = input("phone: ")
        cur.execute('CALL new_user(%s, %s)', (name, phone))

    elif way == 'list':
        incorrect_data = []
        nal = input("enter list of names separated by comma: ").split(',')
        phl = input("enter list of phones separated by comma: ").split(',')
        
        for i in range(len(nal)):
            if not phl[i].isdigit() or not len(phl[i]) == 11:
                incorrect_data.append((nal[i], phl[i]))
        cur.execute('CALL insertlist(%s, %s)', (nal, phl))
        if incorrect_data:
            print("incorrect_data:", incorrect_data)
    cur.close()
    conn.commit()
    conn.close()

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
    
    rows = cur.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("nothing founded")
    
    cur.close()
    conn.close()

def query_pagdata():
    conn = connect_db()
    cur = conn.cursor()

    limit = input("what is a limit?: ")
    offset = input("what is a offset?: ")

    try:
        limit = int(limit)
        offset = int(offset)

        cur.execute("SELECT * FROM phonebook ORDER BY id LIMIT %s OFFSET %s", (limit, offset))
        rows = cur.fetchall()

        if rows:
            for row in rows:
                print(row)
        else:
            print("nothing founded")

    except ValueError:
        print("enter integers for limit and offset!")
        query_pagdata()
    
    finally:
        cur.close()
        conn.close()

def delete_data():
    conn = connect_db()
    cur = conn.cursor()
    filter_type = input("choose filter for deleting (name/phone): ").lower()
    filter_value = input(f"{filter_type}: ")

    if filter_type == 'name':
        cur.execute("CALL delete_user(%s)", (filter_value,))
    elif filter_type == 'phone':
        cur.execute("CALL delete_phone(%s)", (filter_value,))
    else:
        print("incorrect filter")
        return
    
    conn.commit()
    cur.close()
    conn.close()
    print(f"object {filter_type} = {filter_value} deleted!")

def search_phonebook(pattern):
    conn = connect_db()
    cur = conn.cursor()
    w_pattern = f"%{pattern}%"
    cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s OR phone ILIKE %s", (w_pattern, w_pattern))

    results = cur.fetchall()
    for row in results:
        print(row)

    cur.close()
    conn.close()


def main():
    while True:
        print("\nPhoneBook:")
        print("1. Upload Data from CSV")
        print("2. Insert Data")
        print("3. Query Data with pagination")
        print("4. Query Data with filter")
        print("5. Delete Data")
        print("6. Search with pattern")
        print("7. Exit")
        
        choice = input("Choose movement: ")
        
        if choice == '1':
            filename = input("Enter CSV file name: ")
            upload_from_csv(filename)
        elif choice == '2':
            update_data()
        elif choice == '3':
            query_pagdata()
        elif choice == '4':
            query_data()
        elif choice == '5':
            delete_data()
        elif choice == '6':
            pattern = input("Enter your pattern: ")
            search_phonebook(pattern)
        elif choice == '7':
            break
        else:
            print("incorrect choice! try again.")

if __name__ == "__main__":
    main()