# Code Alpha Internship Task 3
import os

path = r"C:\Users\Moses Adeyemi\OneDrive\Desktop\Data science Journey\Code Alpha Internship Tasks"

dir_list = os.listdir(path)

print(dir_list)

with open("Code Alpha Internship Tasks\email_address_original.txt", mode='r') as f:
  for x in f:
    with open("Code Alpha Internship Tasks\email_address_copy.txt", mode='a') as f_copy:
      f_copy.write(x)