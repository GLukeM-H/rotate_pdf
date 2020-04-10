# rotate_pdf
Need to rotate pages in a pdf? Don't have Adobe Acrobat Pro? Here's a small python program to do just that!
# How to Use
### Setup
You will need [Python](https://www.python.org/) installed. And an additional dependency.
```
pip install PyPDF2
```
Alternatively, download the library [here](https://pypi.org/project/PyPDF2/).
### Run the Program
```
python rotate_pdf.py
```
You will be asked for the path to the pdf file that needs pages rotated.
```
Enter G:\path\to\pdf file.pdf
```
Enter an absolute or relative path to the file. You will then be asked which pages you would like rotated.
```
Enter G:\path\to\pdf file.pdf
C:\Users\username\Desktop\example.pdf
List or range of pages to rotate (e.g. 3 4 5 or 3-5)
```
Enter a space separated list of pages and/or page ranges that you would like rotated. A page listed once will be rotated clockwise by 90deg. A page listed twice will be rotated by 90deg twice (180deg) and so on.

For example, all of the following will rotate even numbered pages from 1-10 clockwise by 90 deg and odd numbered pages by 180 deg while leaving all pages after 10 oriented the same.
```
1 1 2 3 3 4 5 5 6 7 7 8 9 9 10
```
```
1-10 1 3 5 7 9
```
```
1 3 5 7 9 1-5 6-10
```
```
1 3 1-5 7 9 5-10 11 11 11 11
```
In this example, a new file "example - rotated.pdf" will be written to the original file's location with the specified pages rotated.
Note that this will overwrite any existing file named "example - rotated.pdf" if one already exists at that location.
