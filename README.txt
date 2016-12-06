WtPer_to_MolPer.py

WHAT IS WTPER_TO_MOLPER.PY?
This is a script to convert major element oxide data from wt% to mol% values. 

THE WTPERCENT.XLSX FILE
The script reads from a file called “wtpercent.xlsx” located in the same directory as the python file. You need to update this excel spreadsheet with your data and then run the python script. The excel file must contain columns named SiO2, TiO2, Al2O3, FeO, MnO, MgO, CaO, Na2O, and K2O containing wt% values. Don’t worry about spaces in column names, the script removes these. Don’t worry about blank, 0 value, —-, NaN, or other values in cells, the script removes these. Don’t worry about extranneous columns, the script ignores these. Take a look at example.xlsx to see an example file that should run just fine despite it being quite a mess.

OUTPUTS OF THE SCRIPT
The script creates a new file called molpercent.xlsx, which it saves to the same directory where the python script is located. molpercent.xlsx is a clone of wtpercent.xlsx with new columns appended. The mole percent values are in columns labeled “MP_SiO2”, “MP_TiO2”, and so on.

INSTALLATION AND USE
To run this script requires some dependencies:
	1. Python 2.7
	2. pandas - use > sudo easy_install pandas
	3. XlsxWriter - use > sudo easy_install XlsxWriter

KNOWN ISSUES
