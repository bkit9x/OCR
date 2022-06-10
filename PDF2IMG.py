from genericpath import exists
from os import mkdir, path
from pdf2image import convert_from_path
import time

def main():
    file = input("Enter the file name: ")
    file = file.replace("\\", "/").replace("\"", "")
    if exists(file):
        out = time.strftime("%Y%m%d%H%M%S")
        mkdir(out)
        pdf2img(file, out)
    else:
        print("File not found")


def pdf2img(file, out):
    start_time = time.time()
    pages = convert_from_path(file, 500, poppler_path=r'C:\OCR\poppler\bin')
    image_counter = 1
    for page in pages:
        filename = out+"/page_"+str(image_counter)+".jpg"
        page.save(filename, 'JPEG')
        image_counter = image_counter + 1
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()