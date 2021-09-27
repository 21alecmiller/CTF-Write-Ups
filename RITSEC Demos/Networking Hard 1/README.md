Intro To Networking - Hard 1 Write Up                       Alec Miller

Challenge: If you haven’t run into it yet, port 10000 is open for some kind of game. Looks pretty easy, just too repetitive to do myself. Maybe you can automate the solving?

To start with, let's connect to the port listed in the challenge, by typing nc localhost 10000. 

![1](https://user-images.githubusercontent.com/55161488/134850172-25714b94-f9da-44b1-a46f-750728d6ccad.jpg)

So it's a game, where we need to calculate basic stats on a set of numbers, 100 times. Again referring back to the description, it sounds like we should write a script to solve this automatically. To get working on this I switched to a different VM with a GUI just to see what was going on better, but it would be possible to do it inside the original VM as well. It's possible to connect to the game from a different VM the same way, just replace localhost with 192.168.74.133, the IP address of the original VM.

![2](https://user-images.githubusercontent.com/55161488/134850221-c6bf0c39-7531-43e4-89ec-55515e84118e.jpg)

One thing to note is that the game rotates between different headers, which impacts what line the actual problem starts on. To write the script, I wrote it in python using a package called pwntools, which is designed to help write quick CTF-style exploits by making it simple to communicate through sockets. It essentially lets the program run similar to a user, receiving and sending inputs. Sidenote: pwntools communicates in bytes, so a lot of byte translation and parsing occurs in order for types to match. 

![3](https://user-images.githubusercontent.com/55161488/134850239-674d7142-926b-4bf3-b4cc-71561911bba5.jpg)

This is the format that all the math problems follow

![4](https://user-images.githubusercontent.com/55161488/134850251-f601cace-6aea-43b4-b774-72365ad91f7e.jpg)

So the basic outline of the program looks something like this:
Find the line where the problem starts (problem:str size:int)
Parse the problem statement to get the operation and the amount of numbers in the set
Get the set of numbers
Perform the correct operation on the set of numbers
Send the answer to the socket
Repeat 99 more times

I decided to split the program into 3 parts: the line identification/outside loop, parsing/performing the operations, and getting the list of numbers. 

To identify the beginning of the problem due to the changing headers, I looped through all the initial lines until I reached one that contained 'problem:' since that indicates the correct format for the problem statement. Once that's found, it breaks out of the while loop and goes into the for loop, which parses all the math problems. None of the print statements are necessary for function, but they help with clarity when the program executes.

![5](https://user-images.githubusercontent.com/55161488/134850276-183b6366-736f-43ef-8014-44c095288bc5.jpg)

In the parse function, the first thing is to determine the type of problem (mean/median/range/max/min), and the size of the set of numbers. 

![6](https://user-images.githubusercontent.com/55161488/134850287-25243e5f-f5e5-4132-9bc5-488f9bbe5685.jpg)

Knowing the size of the set allows us to get the list of numbers by looping through the next size lines. 

![7](https://user-images.githubusercontent.com/55161488/134850299-4efe0b8f-5559-463b-ad72-4f339bcfd40d.jpg)

Once we have a list of numbers, we can go back to the parse method to perform the correct operations. Python has built-in min, max, and round functions, and a statistics module for mean and median, so performing the operations is very simple. Then the answers get returned to the console, which in return provides a new problem.

![8](https://user-images.githubusercontent.com/55161488/134850317-0a83f02c-4b11-4dd9-8682-6fe510d6747e.jpg)

After solving all 100 problems, we get the flag!

![9](https://user-images.githubusercontent.com/55161488/134850326-0c069dac-5b3f-470f-8989-db72cef89082.jpg)
