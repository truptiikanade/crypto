import streamlit as st
import mysql.connector

# Database connection details
db_host = 'localhost'
db_user = 'root'
db_password = 'abcdef'
db_name = 'try_new'

try:
    # Connect to MySQL
    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )
    st.success("Connected to MySQL database")
except mysql.connector.Error as e:
    st.error(f"Error connecting to MySQL database: {e}")

# Create cursor for database operations
mycursor = conn.cursor()

# Create streamlit app
def main():
    st.title("Crud operations with mysql")

    # Display Options for CRUD Operations
    option = st.sidebar.selectbox("Select an Option", ("Create", "Read", "Update", "Delete"))

    # Perform Selected CRUD Operation
    if option == "Create":
        st.subheader("Create a Record")
        id = st.text_input("Enter ID")
        name = st.text_input("Enter Name")
        symbol = st.text_input("Enter Symbol")
        slug = st.text_input("Enter Slug")
        if st.button("Create"):
            sql = "INSERT INTO users(id, name, symbol, slug) VALUES (%s, %s, %s, %s)"
            val = (id, name, symbol, slug)
            mycursor.execute(sql, val)
            conn.commit()
            st.success("Record Created Successfully")

    elif option == "Read":
        st.subheader("Read Records")
        mycursor.execute("SELECT * FROM crypto_data")
        result = mycursor.fetchall()
        for row in result:
            st.write(row)

    elif option == "Update":
        st.subheader("Update a Record")
        id=st.number_input("Enter ID")
        name=st.text_input("Enter New Name")
        symbol=st.text_input("Enter New Symbol")
        slug=st.text_input("Enter New Slug")
        if st.button("Update"):
            sql = "UPDATE users SET name=%s, symbol=%s, slug=%s WHERE id=%s"
            val = (name, symbol, slug, id)
            mycursor.execute(sql, val)
            conn.commit()
            st.success("Record Updated Successfully")

    elif option == "Delete":
        st.subheader("Delete a Record")
        id=st.number_input("Enter ID")
        if st.button("Delete"):
            sql="DELETE FROM users WHERE id = %s"
            val=(id,)
            mycursor.execute(sql,val)
            conn.commit()
            st.success("Record Deleted Successfully")

# Run the app
if __name__ == "__main__":
    main()
