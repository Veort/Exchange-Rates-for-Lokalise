# Exchange Rates

The program was created as part of the test task for Lokalise. A simple request to an exchange API by getting information on exchange rates for 2010-01-15(+input date) and putting the results to any Google Spreadsheet

## Installation

To run the program, you need to install Python 3 (https://www.python.org/downloads/).
And also install the following libraries - pandas, requests и google-api-python-client, by typing the following commands into the command line:

```bash
pip install pandas
pip install requests
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

## Usage

In order to write data to an html table, you need to run the program in the command line start_html_table.py:

```bash
python *path to file*\start_html_table.py
```
In order to write data to the Google spreadsheet, you need to execute the script start_write_to_sheet.
```bash
python *path to file*\start_write_to_sheet.py
```
To display data from the Google spreadsheet, you need to execute the script start_read_from_sheet:
```bash
python *path to file*\start_read_from_sheet.py
```
To delete data from the Google spreadsheet, you need to execute the script start_delete_from_sheet:
```bash
python *path to file*\start_delete_from_sheet.py
```

## Google Spreadsheet Link 
https://docs.google.com/spreadsheets/d/1kOaQAhonJzYo7weurSmiaYiR8B_J1iqwnckPAuJMCJU/

## 
Also in the Input folder there is a version of the same scripts that allow you to select a date
