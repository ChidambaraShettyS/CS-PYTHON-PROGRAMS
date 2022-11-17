# import time
# s = time.time()

with open("regex1.txt", "w") as file:
    ph_no = ["+917760269972\n", "+912260248972\n", "+919972100909\n"]
    std_usn = ["20RWSAC007\n", "220hay09ju\n"]
    ip_add = ["192.168.1.149\n", "19.249.168.1.149\n"]
    pan_no = ["BvtPC39791M\n", "BVTPC3971M\n"]
    dob = ["20-100-1999\n", "20-04-1999\n"]
    mail_id = ["shetty3355.cs@gmail.in.com\n", "chidu5533.cs@gmail.in.com\n"]

    file.writelines(ph_no)
    file.writelines(std_usn)
    file.writelines(ip_add)
    file.writelines(pan_no)
    file.writelines(dob)
    file.writelines(mail_id)

with open("regex1.txt", "r") as file:
    res = file.read()



import re

print(re.findall("\+91[6-9]\d{9}", res))
print(re.findall("\d{2}[A-Z]{5}\d{3}", res))
print(re.findall("\d{3}\.\d{3}\.\d\.\d{3}", res))
print(re.findall("[A-Z]{5}\d{4}[A-z]", res))
print(re.findall("\d{2}-\d{2}-\d{4}", res))
print(re.findall("\w+\.?\w*\@\w+\.\w*\.?\w*", res))


# e = time.time()
# print("Execution time : ", e-s)






















































































































































































