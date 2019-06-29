# ASCIILines

## Stats
Copyright(c)2019 Weiwei Chen
This is a command-line program which is used to accept a single .tvg file argument and render the files as ASCLL on standard output.

### The TVG Format
The first line of the file contains the "canvas size": the number of rows and columns of text to output (both must be greater than zero). The canvas starts out filled with . characters. The rest of the file is rendering commands, one per line.
A rendering command is a line containing:
* A character to render with
* A row position to start at (0-based)
* A column position to start at (0-based)
* Either h for a horizontal line or v for a vertical line. Horizontal lines go to the right from the starting coordinate; vertical lines go down.
* A length for the rendered line (must be greater than 0)
The elements of the command should be separated by a single space.

The character positions that are part of the rendering command's rendered line should be filled with the rendering character. It is legal for the line to extend outside the canvas. There is no wraparound: only points inside the canvas should be rendered, others should be ignored.

A rendering output is produced by executing each of the rendering commands on the canvas. For example, a TVG file containing
3 4
* 1 -1 h 5
should render as
....
****
....

## Build and Run
I created the program with Python language. Before running the program, you don't need to build anything. 
Run the program under the directory 'asciilines' using the following example command:
 $ python asciilines.py tests/test1.tvg
Note: you can change .tvg file to any other .tvg file under the directory ' tests'.
 
## Bugs, Defects and Failing tests
### Bugs I encountered: 
* It gave wrong canvas when I didn't pay attention to the row and column index. It displayed more characters than I expected. It turned out that I used the wrong index number. 
* readline() method read the line of .tvg file, but I couldn't use split() method to split the elements since it was not a string. So I had to convert the line to string type bsfore using split() method.
* Indention bugs were detected when I commented out some lines. Python is very sensitive to them.
Note: All the bugs I mentioned were fixed.

### Defects:
The defect might be I used big module instead of small ones.

### Failing tests:
The failing tests were the ones with the bugs that the program with wrong index numbers. I fixed them and all the tests I listed in this project passed.

## License
This program is licensed under the "MIT License". Please see the file LICENSE in the source distributon of this software for the license terms.
