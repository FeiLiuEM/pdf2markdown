'''
Author: FeiLiu <FeiLiuEM@outlook.com>
Date: 2024-09-19 02:59:05
LastEditors: FeiLiu <FeiLiuEM@outlook.com>
LastEditTime: 2024-09-19 03:29:53
Description: 

Copyright (c) 2024 by <FeiLiuEM@outlook.com>, All Rights Reserved. 
'''


import os
from wisup_e2m import PdfParser, ImageConverter

#get pdf file name
def getFilePathList(path, filetype):
    pathList = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(filetype):
                #pathList.append(os.path.join(file)) #不带文件位置的版本
                pathList.append(os.path.join(root,file)) #带文件位置的版本
    return pathList

if __name__ == "__main__":
    work_dir = os.getcwd()  # Set the current path as the working directory
    image_dir = os.path.join(work_dir, "figure")
    pdf_dir = os.path.join(work_dir, "pdf")
    md_dir = os.path.join(work_dir, "markdown")

    pdf_path = getFilePathList(pdf_dir, ".pdf")[0]
    md_name = pdf_path.split("\\")[-1].replace("pdf", "md")
    md_path = os.path.join(md_dir, md_name)

    # Load the parser
    pdf_parser = PdfParser(engine="marker")

    # Parse the PDF into images
    pdf_data = pdf_parser.parse(pdf_path)


    # Save the test markdown
    with open(md_path, "w") as f:
        f.write(pdf_data.text)

