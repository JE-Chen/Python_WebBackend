import datetime

from Module.Generate_Vec_Code import Generate_Vec_Code


class Code_Core():

    def __init__(self):
        try:
            self.Generate = Generate_Vec_Code()
        except Exception as Errr:
            raise Errr
        print(datetime.datetime.now(), self.__class__, 'Ready', sep=' ')
