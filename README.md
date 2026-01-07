# Ascii-image
This project converts a color image stored in PPM (P3) format into an ASCII art representation using Python. Instead of displaying images using pixels, the program recreates the image using a set of ASCII characters whose visual density represents different brightness levels.
The program works directly with raw pixel data, converting RGB values into grayscale intensity and applying gamma correction to improve visual contrast. To maintain proper proportions in text form, pixels are grouped into small blocks, and the average brightness of each block is mapped to a corresponding ASCII character arranged from darkest to lightest. 
The final output is a text-based image that closely resembles the original input image. This project demonstrates how basic image processing techniques and simple mathematical operations can be used to create creative and meaningful visual results without relying on advanced image-processing libraries.

## Objective:
-To understand the internal structure of digital images and pixel representation
-To work with images in PPM (P3) format using raw pixel data
-To convert RGB color images into grayscale intensity values
-To apply gamma correction to enhance contrast in ASCII output
-To map pixel brightness levels to appropriate ASCII characters
-To generate a text-based ASCII representation of an image using Python
-To strengthen knowledge of basic image processing and file handling concepts

## Project Structure:
ASCII-Image-Generator-
 bill_clinton_4.ppm    # Input image (PPM P3 format)
 ascii_generator.py    # Main Python script
 ascii_output.txt      # Generated ASCII art output
 README.md             # Project documentation
 
 ## Technologies Used:
Programming Language: Python
Image Format: PPM (P3 – ASCII format)
Output Format: Text file (.txt)

## Key Features:
This project converts a color image in PPM (P3) format into ASCII art using raw RGB pixel data without external image-processing libraries. It applies grayscale conversion and gamma correction to improve visual contrast, while block-based sampling is used to maintain proper image proportions. Pixel brightness is mapped to ASCII characters arranged from darkest to lightest, producing a clear text-based image that can be viewed in the terminal or saved as a text file, with easy customization options for characters, block size, and gamma value.

## Author
Aditi Verma

Computer Science Student.


