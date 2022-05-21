Cyber Apocalypse Writeup: Free Services

For this challenge you're given a zip file with an excel spreadsheet in it, specifically with the .xlsm extension, so the file has a macro in it. Opening up the file, there's a bunch of function calls in the first column, and 3 columns of numbers. 

![Excel macro](https://user-images.githubusercontent.com/55161488/169668801-2371176a-de0e-4b5a-8608-36d2f8695289.png)

Looking at the macro itself, it looks like it should be writing to process memory, so first I tried opening up a debugger and stepping through the macro to see that data. But I wasn't having any luck seeing any of the process memory changing, so i backtracked to simply step though what theoretically *should* be written to memory. 

After stepping through the macro to get a good sense of what's going on, the macro is going to every other number in those 3 columns, xor-ing the value with 24, and then writing the ascii character of that number to memory. 

Simple enough, so I start working through the first couple iterations, but I'm not getting anything meaningful. But since the flag format is consistently HTB{...}, I can find the start of the flag and not go through all 250+ rows in the file. 72 (ascii for H) xor 24 is 80, and I do the same for the next couple of characters and can find the start of the flag, which then goes to the end of the rows. I just went through those characters manually since it was pretty short, and we got the flag!