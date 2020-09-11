from Core.Gmail_Core import Gmail_Core
a=Gmail_Core()
a.Gmail_API.Send_Mail_Basic("","","Hello",r"Test",UseHTML=True)