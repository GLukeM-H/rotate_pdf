# rotate_pdf
A small python program to rotate pdf pages.
# How to Use
### Setup (using Python script)
You will need [Python](https://www.python.org/) installed with tkinter. And an additional dependency [PyPDF2](https://pypi.org/project/PyPDF2/).
### Setup (using exe)
Download ```rotate_pdf_exe.zip``` and extract.
### Run the Program
To run the Python script:
```
python rotate_pdf.py
```
Or, double click ```rotate_pdf.exe``` after unzipping.

Select the pdf that needs pages rotated.
You will then be asked which pages you would like rotated.
```
List or range of pages to rotate (e.g. 3 4 5 or 3-5)
```
Enter a space separated list of pages and/or page ranges that you would like rotated. A page listed once will be rotated clockwise by 90&deg;. A page listed twice will be rotated by 90&deg; twice (180&deg;) and so on.

For example, all of the following will rotate even numbered pages from 1-10 clockwise by 90&deg; and odd numbered pages by 180&deg; while leaving all pages after 10 oriented the same.
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
If ```example.pdf``` was chosen, a new file ```example - rotated.pdf``` will be written to the original pdf's directory with the specified pages rotated.
Note that this will overwrite any existing file named ```example - rotated.pdf``` if one already exists at that location.
