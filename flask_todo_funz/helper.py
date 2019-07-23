import sqlite3

DB_PATH = './todo.db' # is this correct path?
NOTSTARTED = 'Not Started'
INPROGRESS = 'In Progress'
COMPLETED = 'Completed'

def add_to_list(item):
    try:
        conn = sqlite3.connect(DB_PATH)

        # once a connection has been established, can use the cursor
        c = conn.cursor()

        # Keep the intial status Not Started to test
        c.execute('insert into items(item, status) values(?,?)', (item, NOTSTARTED))

        # commit to save the change
        conn.commit()
        return {"item": item, "status": NOTSTARTED}

    except Exception as e:

        #send exception code
        print('Error: ', e)
        return None
