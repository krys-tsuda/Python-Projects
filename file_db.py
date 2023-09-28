import sqlite3

# creates a database
def create_db():
    conn = sqlite3.connect('file.db')

    with conn:
        cur = conn.cursor()
        # create table if it doesnt already exist
        # field with an auto_increment primary integer
        # field with data type "string"
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(ID INTEGER PRIMARY KEY AUTOINCREMENT,\
                    col_file TEXT)")
        conn.commit()

    conn.close()

   
# updates database adding data to into db    
def update_db():
    conn = sqlite3.connect('file.db')

    fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
                'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg') 
    print("Files added:") 

    # creates a for loop to iterate fileList
    for x in fileList:
        # if condition is met (item is a .txt file)
        if x.endswith('txt'):
            with conn:
                cur = conn.cursor()
                # in db tbl_files add items that meet condition to col_file
                cur.execute("INSERT INTO tbl_files(col_file) VALUES (?)", (x,))
                print(x)

    conn.close()


# calls function
create_db()
update_db()
            
