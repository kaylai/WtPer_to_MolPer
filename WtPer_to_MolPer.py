import pandas
import xlsxwriter

data = pandas.read_excel('wtpercent.xlsx') #import excel file 'wtpercent.xlsx' that contains all data in terms of wt% in colums
data = data.dropna(axis=1, how='all') #drop all columns that contain no data
data = data.loc[:, (data != 0).any(axis=0)] #drop all columns that contain all zeroes
data.rename(columns=lambda x: x.strip().replace(" ", "_"), inplace=True) #Remove leading and trailing spaces from column names and replace internal spaces with _ (Pandas cannot deal with spaces in column headers)
data.fillna(0) #Fill in missing data with zeros

#save each major oxide column as a variable

#remove any non-numeric data in each row
data = data.convert_objects(convert_numeric=True)

#definte molecular weights
MW_SiO2		= 60.08
MW_TiO2		= 79.866
MW_Al2O3	= 101.96
MW_FeO		= 71.844
MW_MnO		= 70.9374
MW_MgO		= 40.3044
MW_CaO		= 56.0774
MW_Na2O		= 61.9789
MW_K2O		= 94.2

#create new rows equal to the wt% value divided by the MW
data["DMP_SiO2"]	= data["SiO2"] / MW_SiO2
data["DMP_TiO2"]	= data["TiO2"] / MW_TiO2
data["DMP_Al2O3"]	= data["Al2O3"] / MW_Al2O3
data["DMP_FeO"]		= data["FeO"] / MW_FeO
data["DMP_MnO"]		= data["MnO"] / MW_MnO
data["DMP_MgO"]		= data["MgO"] / MW_MgO
data["DMP_CaO"]		= data["CaO"] / MW_CaO
data["DMP_Na2O"]	= data["Na2O"] / MW_Na2O
data["DMP_K2O"]		= data["K2O"] / MW_K2O

#sum all the newly created DMP columns
data["DMP_sum"]		= data["DMP_SiO2"] + data["DMP_TiO2"] + data["DMP_Al2O3"] + data["DMP_FeO"]	+ data["DMP_MnO"] + data["DMP_MgO"]	+ data["DMP_CaO"] + data["DMP_Na2O"] + data["DMP_K2O"]

#normalize mol% values
data["MP_SiO2"]		= 100 * (data["DMP_SiO2"] / data["DMP_sum"])
data["MP_TiO2"]		= 100 * (data["DMP_TiO2"] / data["DMP_sum"])
data["MP_Al2O3"]	= 100 * (data["DMP_Al2O3"] / data["DMP_sum"])
data["MP_FeO"]		= 100 * (data["DMP_FeO"] / data["DMP_sum"])
data["MP_MnO"]		= 100 * (data["DMP_MnO"] / data["DMP_sum"])
data["MP_MgO"]		= 100 * (data["DMP_MgO"] / data["DMP_sum"])
data["MP_CaO"]		= 100 * (data["DMP_CaO"] / data["DMP_sum"])
data["MP_Na2O"]		= 100 * (data["DMP_Na2O"] / data["DMP_sum"])
data["MP_K2O"]		= 100 * (data["DMP_K2O"] / data["DMP_sum"])

#Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pandas.ExcelWriter('molpercent.xlsx', engine='xlsxwriter')

#Convert the dataframe to an XlsxWriter Excel object.
data.to_excel(writer, sheet_name='Sheet1')

#Close the Pandas Excel writer and output the Excel file.
writer.save()
