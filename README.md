This program is designed to take data from raw text files that are sorted in a certian manner and make graphs from the 
data in the file. It will also return the slope of the line that is graphed, it will return with units of Newtons per
mega Pascal as used in engineering stress strain graph. The graphs that are produced from this program will be stored 
in two seperate '.png' files. The slope of the data is stored in 'Slope.png' and the tredline in 'Tredline.png'.

In order for this program to run, Python must be installed on the machine being used. To download Python
go to terminal, type in the command line "apt-get install python". This will start downloading Python
onto the local machine. It will ask a few permission questions and you will have to let it install 
Python onto the local machine. 

In order to run the program you must be in the directory that holds the program. Once inside the directory
you must type "python plot.py " + the path to the data file that you want to run the program on. On this repository
the files that will work on this program are located in the directory '2raw-data.' They are each called by the name
of the type of material tested followed by an integer if there are multiple samples. If there are not multiple 
samples it is just the name of the material .raw. The data stored in 'data-raw' will not work on this program.

In this program I learned a lot about committing in bash, how to do it, what it does and the importance of it. During
this project I also learned about editing text files when I was trying to take portions of the raw text files and cut
them into a new text file in order to split up the data. Trying to figure out how to edit the text files in a way that
would make the program run was the hardest part for me but when I figured out how do copy the file and then delete
mass portions of it that solved the problem. I would consider the moment when I figured out how to edit the data files
as an "Aha!" moment.
