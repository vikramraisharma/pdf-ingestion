import mysql.connector
import filetype
import pdftotext
import os

def main():

    mydb = mysql.connector.connect(
        # enter mysql connection here
    )

    mycursor = mydb.cursor()

    # save set of path variables and corresponding IDs in tuple
    mycursor.execute("SELECT inquiry_id, path FROM dsims_attach;")
    myresult = mycursor.fetchall()
    print(myresult)

    # create document and counter to keep track of files that cannot be converted/read in
    missingPDF = open("missing_files.txt", "w")
    fail_count = 0

    
    add_abstract = ("UPDATE dsims_attach "
        "SET abstract = %(abstract)s "
        "WHERE inquiry_id = %(inquiry_id)s;")
        # Creates SQL query with embedded variables

    for i in myresult:
        # Use filetype library to determine if file is PDF
        kind = filetype.guess(i[1])
        if kind.extension == "pdf":
            # convert the file to txt if it is PDF 
            name = i[1]
            text = ".txt"
            namet = name + text
            with open(name, "rb") as f:
                pdf = pdftotext.PDF(f)
            text = open(namet, "w")
            for page in pdf: 
                print(page, file = text)

            print(text.name)
            with open(text.name, 'r') as G:
                text_read = G.readline(5)
        
            data_pdf = {
                'inquiry_id': i[0],
                'abstract': text_read,
            }
            # Store variables set in earlier query
            mycursor.execute(add_abstract, data_pdf)
            # Execute query with added string and ID
            mydb.commit()
            os.remove(text.name)

        else:
            # we can use either a counter or a separate document to keep track of files that cannot be read in
            fail_count = fail_count + 1
            missingPDF.write(i[1])
            missingPDF.write("\n")
    missingPDF.close() # close the file to keep track of files that are not PDF or are not writable
    print(fail_count)

if __name__ == "__main__":
    main()
