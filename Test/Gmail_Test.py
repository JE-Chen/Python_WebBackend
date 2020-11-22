from Core.Gmail_Core import Gmail_Core

a = Gmail_Core()
a.Gmail_API.Send_Mail_Basic(r"410877027@mail.nknu.edu.tw", r"410877027@mail.nknu.edu.tw", r"Hello", r"Test",
                            UseHTML=True)
