from Core.SQLite_Core import SQLite_Core

'''
SQL=SQLite_Core(r'..\Test_Source\test.db',Table_Name='Time')

SQL.Create_Table('CREATE TABLE IF NOT EXISTS Time(id INTEGER PRIMARY KEY,name VARCHAR(10))')

SQL.Values_Count = 2

SQL.Insert_Into_Replace(1,'小紅')

SQL.Select_From('id','name')

SQL.Insert_Into_Replace(2,'小杯')

SQL.DELETE('name','小杯')

SQL.Insert_Into_Replace(3,'哭阿')

SQL.Values_Count = 1

SQL.Select_Distinct('name')

SQL.Values_Count = 1

SQL.Select_Where('name','name','哭阿')

SQL.Close()

'''



SQL=SQLite_Core(DB_Name=r'..\Test_Source\Account.db',Table_Name='UserInfo')

SQL.Create_Table('CREATE TABLE IF NOT EXISTS UserInfo(Email VARCHAR(254),Passsword VARCHAR(20),Authority VARCHAR(10))')

SQL.Values_Count = 3

SQL.Insert_Into_Replace('zenmailman@gmail.com','12345678','Super')

SQL.Close()


'''
SQL=SQLite_Core(DB_Name=r'..\Test_Source\File.db',Table_Name='FileInfo')

SQL.Create_Table('CREATE TABLE IF NOT EXISTS FileInfo(FileName VARCHAR(50),FilePath VARCHAR(50))')

SQL.Values_Count = 2

SQL.Insert_Into_Replace('Test_Name',r'C://Test')

SQL.Close()
'''