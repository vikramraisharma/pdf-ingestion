# pdf-ingestion

## Script built to parse PDF and docx documents as plain text to extract relevant text for a project under SURVICE
This uses Python modules: pdftotext, docx-text, mysql.connector, filetype -- all found on PyPI
#### With simple changes, this can quickly be configured to manually parse PDFs if they contain critera that you can define in lines 44-45!

## Objective
### 1. Obtain document paths from MySQL database stored as VARCHARs in table column
### 2. Use document path to determine if document is a PDF or DOCX
### 3. (TBD) Use pawk or Python selection to extract a specific string from each document if it is present
### 4. Save string as variable to be embedded in MySQL query
### 5. Save to MySQL database via MySQL controller

