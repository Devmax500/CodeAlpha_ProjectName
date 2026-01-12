import os
import shutil
scr_file_path = "C:\\Users\\Moses Adeyemi\\OneDrive\\Desktop\\Data science Journey\\Code Alpha Internship Tasks\\jpg files"
dst_file_path = "C:\\Users\\Moses Adeyemi\\OneDrive\\Desktop\\Data science Journey\\Code Alpha Internship Tasks\\New jpg files"


for file in os.listdir(scr_file_path):
  src_folder = os.path.join(scr_file_path, file)
  dst_folder = os.path.join(dst_file_path, file)
  shutil.move(src_folder, dst_folder)
  print(f"Moved Jpeg file from {src_folder} to {dst_folder} Successfully")