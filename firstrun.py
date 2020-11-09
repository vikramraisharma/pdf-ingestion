import mysql.connector
import filetype
def main():

    mydb = mysql.connector.connect(
        host="localhost",
        user="username",
        password="password",
        database="database"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT inquiry_id, path FROM dsims_attach;")

    myresult = mycursor.fetchall()
    
    # Saves inquiry result in tuple named myresult

    # print(myresult)
    
    add_abstract = ("UPDATE dsims_attach "
        "SET abstract = %(abstract)s "
        "WHERE inquiry_id = %(inquiry_id)s;")
        # Creates SQL query with embedded variables
    for i in myresult:
        kind = filetype.guess(i[1])
        if kind.extension == "pdf":
            # Use filetype library to determine if file is PDF
            string = (i[1] + " is a pdf!")
            data_pdf = {
                'inquiry_id': i[0],
                'abstract': string,
            }
            # Store variables set in earlier query
            mycursor.execute(add_abstract, data_pdf)
            # Execute query with added string and ID
            mydb.commit()
        else:
            # currently no docx support in filetype python lib
            string = (i[1] + " is a docx!")
            data_docx = {
                'inquiry_id': i[0],
                'abstract': string,
            }
            mycursor.execute(add_abstract, data_docx)
            mydb.commit()


if __name__ == "__main__":
    main()
