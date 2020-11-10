import mysql.connector
import filetype
import pdftotext

def main():

    mydb = mysql.connector.connect(
        host="localhost",
        user="username",
        password="password",
        database="database"
    )

    mycursor = mydb.cursor()

    # save set of path variables and corresponding IDs in tuple
    mycursor.execute("SELECT inquiry_id, path FROM dsims_attach;")
    myresult = mycursor.fetchall()
    # print(myresult)
        missingPDF = open("missing_files.txt", "w")    

    
    add_abstract = ("UPDATE dsims_attach "
        "SET abstract = %(abstract)s "
        "WHERE inquiry_id = %(inquiry_id)s;")
        # Creates SQL query with embedded variables

    for i in myresult:
        # Use filetype library to determine if file is PDF
        kind = filetype.guess(i[1])
        if kind.extension == "pdf":
            # convert the file to txt if it is PDF 
            with open(i[1], "rb") as f:
                # pdf = pdftotext.PDF(f, "secret")
            
            # define string as abstract from text file
            
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
            missingPDF.write(i[1] + " is not a PDF.")
            missingPDF.write("\n")
    missingPDF.close() # close the file to keep track of files that are not PDF or are not writable

if __name__ == "__main__":
    main()
