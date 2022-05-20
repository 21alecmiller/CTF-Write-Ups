CSAW Writeup: Save the Tristate (MISC)

Description: So it was just another day in Danville when Phineas and Ferb were making a new device to communicate with Meep as he travels across the galaxy. To make a device suitable for galactic communication and secure enough to be safe from alien hackers, they decide to protect their device with QKD! Unfortunately, due to Phineas & Co singing their usual musical numbers about their inventions, Doofenshmirtz has caught wind of this technology and wants to use it to take over the Tristate area, using his brand new Qubit-Disrupt-inator. Naturally I, Major Monogram, have to send you, Perry the Platypus, on a mission to stop Doofenshmirtz from disrupting Phineas and Ferb's qubits with his diabolical inator. So grab your tiny fedora and doo-bee-doo-bee-doo-ba-doo your way over to stop Doofenshmirtz! 
Mission:
Receive # of qubits that translate to the flag
Measure qubits in your own basis
Monogram tells you how many qubits were measured correctly, but not which ones
Go back and fix it
Get it right
nc misc.chal.csaw.io 5001

So when you first connect to the challenge server for this problem, it prints 
    How many bases would you like to check?
and you can type any number. Then it prints 
Please enter your {# you entered} bases:
so you can type in any combo of characters that is # long (ex. if # = 3, type a1?) and then it prints 
Errors: {# errors}

So after some trial and error of typing every character on my keyboard, it turns out that the only valid characters are + and x. It turns out this relates back to the qubits aspect of the problem, but for this part of the problem it's only important that those are the only 2 valid characters. And when you type in a string the length of the number of bases in the correct order (the number of errors refers to the number of characters that are incorrect), the problem just loops back, with no additional output. 

There's no hints in the challenge description that appear to be pointing towards a specific number of bases, and after some manual tries with a couple different base numbers, it looks like this is a brute force problem to find the number of bases and the correct combination of +s and xs. So I wrote a python script (written at the end of the doc) using pwntools to connect to the server, and brute force the combination of characters (the number of bases was hardcoded initially and that ended up working out, but it could've also brute forced that too). In order to brute force the combination, it created an array combo of straight +s (+++++...etc) , counted the number of errors, then changed the character at combo[0], and checked if the errors went down. If it did, it kept the change and moved on, if it didn't it reversed it and then moved on, until the number of errors was 0. Then it printed out the next two lines, to see if the output had changed at all (under the assumption that the output would change when the correct number of bases was found). 

I tested the program with a couple different bases (0, 1, 100. 1000) just to see how the program would react, to see if I'd written it right. 1000 ended up hitting an error that seemed to say that the server didn't respond properly. So I tried some smaller numbers, 500, 300, then 200. 300 failed with the same error, but 200 worked. So following a hunch, I tried 256 (powers of 2 are cool). And that had some new output! So we found the right number of bases. The new line was in the format 1.00 + 0.00i, which looked kinda like a vector, maybe qubit related? But it looked kinda odd, so I added a loop to print out the next 256 lines of output, which then gave me 256 lines of very similar text. There were 4 variations, 1.00 + 0.00i, 0.00 + 1.00i, 0.707 + 0.707i, and -0.707 + 0.707i. It just ended there though, so I received another line, which was asking to input a key. 

So these numbers look like complex unit vectors. Looking at the output a bit more, it turns out that the 1 vectors always matched up to a +, and the 0.707 vectors always matched to an x. So I remembered this weird looking chart on the wikipedia page for quantum key distribution (QKD), from the problem description. +s and xs, and vectors, looks promising. 

![1](https://user-images.githubusercontent.com/55161488/134851175-add5fe9d-1031-42ba-90ad-ad3ed9ecaf75.jpg) 

So I tried assigning 0s and 1s for each of the vectors in the output (1 for 0 + 1, 0 for 1 + 0, 1 for -0.707, 0 for 0.707), to see if that would generate the correct key. I tried submitting the string of 0s and 1s, but no luck. Flipped around the number assignments, still nothing. Turns out, every time the program is run, the binary string is always the same, even though the combo gets randomized each time, interesting. Well maybe the key isn't binary, so I threw it in a binary -> ascii converter and I get this: "a semi-aquatic mammal of action!". That's probably it, so I put in that key, and we got the flag!
