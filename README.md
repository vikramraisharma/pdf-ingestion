# pdf-ingestion

## Script built to parse PDF and docx documents as plain text to extract relevant text for a project under SURVICE
This uses Python modules: pdfottext, docx-text, mysql.connector, filetype found on PyPI

## Objective
### 1. Obtain document paths from MySQL database stored as VARCHARs in table column
### 2. Use document path to determine if document is a PDF or DOCX
### 3. (TBD) Use pawk or Python selection to extract a specific string from each document if it is present
### 4. Save string as variable to be embedded in MySQL query
### 5. Save to MySQL database via MySQL controller

