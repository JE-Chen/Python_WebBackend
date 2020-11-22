from Core.Code_Core import Code_Core
from Core.SQLite_Core import SQLite_Core

FileSQL = SQLite_Core(r'../Test_Source/File.db', Table_Name='File')

AccountSQL = SQLite_Core(r'../Test_Source/Account.db', Table_Name='Account')

Code_Generate = Code_Core()

