# Exchange Rates

The program was created as part of the test task for Lokalise. A simple request to an exchange API by getting information on exchange rates for 2010-01-15(+input date) and putting the results to any Google Spreadsheet.

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
## Exchange Rates API
By changing url in exchange_rates_fixed.py you can get a number of endpoints where each of them provides different functionality.
```bash
url = 'http://api.exchangeratesapi.io/v1/2010-01-15?access_key=2146e6519dc5c7836c76a433d6049c84'
```
For more information go to https://exchangeratesapi.io/documentation/

## Google Spreadsheet Link
https://docs.google.com/spreadsheets/d/1kOaQAhonJzYo7weurSmiaYiR8B_J1iqwnckPAuJMCJU/

Fixed script(2010-01-15) uses first list and input script uses second list in this spreadsheet.

In order to change spreadsheet you need to generate a new pair of keys in Google cloud platform.

## Input any date
In the Input folder there is a version of the same scripts that allows you to select a date with input.
