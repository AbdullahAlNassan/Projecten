import sqlite3

def list_visits():
    conn = sqlite3.connect('boardgames.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT id, collected_on, url FROM visit')
    visits = cursor.fetchall()
    
    print("Visits:")
    for visit in visits:
        print(f"{visit[0]}: {visit[1]} {visit[2]}")
    
    conn.close()
    return visits

def list_visit_items(visit_id):
    conn = sqlite3.connect('boardgames.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT id, name, rank FROM visit_item WHERE visit_id = ?', (visit_id,))
    items = cursor.fetchall()
    
    print("\nVisit items:")
    print(f"{'VISIT ID':<10} {'ID':<4} {'NAME':<30} {'RANK':<4}")
    print('-' * 50)
    for item in items:
        print(f"{visit_id:<10} {item[0]:<4} {item[1]:<30} {item[2]:<4}")
    
    conn.close()

def list_visit_item_info(visit_item_id):
    conn = sqlite3.connect('boardgames.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT key, value FROM visit_item_info WHERE visit_item_id = ?', (visit_item_id,))
    info = cursor.fetchall()
    
    print("\nVisit item info:")
    print(f"{'KEY':<15} {'VALUE':<50}")
    print('-' * 65)
    for item in info:
        print(f"{item[0]:<15} {item[1]:<50}")
    
    conn.close()

def main():
    while True:
        visits = list_visits()
        
        visit_input = input("\nPress visit number to show visit items or 'X' to exit: ")
        if visit_input.lower() == 'x':
            break
        
        try:
            visit_id = int(visit_input)
            if any(visit[0] == visit_id for visit in visits):
                list_visit_items(visit_id)
                item_input = input("\nPress item number to show item info or 'X' to go back: ")
                if item_input.lower() == 'x':
                    continue
                try:
                    item_id = int(item_input)
                    list_visit_item_info(item_id)
                except ValueError:
                    print("Invalid input. Please enter a valid item number or 'X' to go back.")
            else:
                print("Invalid visit number.")
        except ValueError:
            print("Invalid input. Please enter a valid visit number or 'X' to exit.")

if __name__ == "__main__":
    main()

