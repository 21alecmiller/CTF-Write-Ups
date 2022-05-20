CSAW Writeup: The Magic Modbus (ICS)

Description: Climb on the Magic Modbus and see if you can find some of the messages being passed around!

So this one starts pretty straightforward, you get a .pcap file and you need to find a message hidden in the packets. After some research, it looks like Modbus is a communication protocol based on queries and responses. 

Looking at the pcap in wireshark, it looks like this is exactly what we have, a bunch of queries and responses, from a couple different ip addresses. Given we're looking for hidden messages, I guessed that it would probably be sent through the response packets, which are sending answers back to the addresses sending the queries. 

![1](https://user-images.githubusercontent.com/55161488/134850975-1284df28-077e-4d7a-a5b6-fb1cc0f0d67a.jpg)

So that's an example of one of the response packets. In wireshark, I filtered out the query packets, to just look at the responses. Paging through the packets, they all look pretty similar, with one exception, the last line "Register _ (UINT16): ___". 

So those numbers are probably significant. Keep paging through, turns out the numbers never go above 125… looks like ascii. I threw the first 10 numbers into an ascii -> converter, no luck. Looks like gibberish, but it looks like ascii alright, so let's try rearranging some (first try was time forward). 

After a bit of trial and error with sorting the packets, I get this from sorting by Source: OK, Bus, do. Looks promising, so I just keep copying all the numbers into the converter. Scripting this would probably be better, but this worked too. Note for the future, look for the { (123) to save yourself some typing. But this is what we get, and there's the flag!

![2](https://user-images.githubusercontent.com/55161488/134850999-bb0c54cb-fe4f-4149-87b2-f6f82c89ed78.jpg)
