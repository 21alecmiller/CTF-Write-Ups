Cyber Apocalypse Writeup: Puppeteer

For this challenge, you're given a zip file with a single directory called 'Logs', filled with .evtx files. This extension is for Windows log files, so to get started we can start by opening up Windows Event Viewer to check out some promising logs. 

There were 143 log files, so I wanted to narrow that down a bit to a more manageable number to look through. It turns out that a lot of the log files were 68 KB, and didn't contain any real information. Since these logs seemed to just be empty, and filtering those out brings the number of logs to look at down to 23. There's a couple promising looking logs here, like Security.evtx, System.evtx, and Microsoft-Windows-PowerShell%4Operational.evtx.

Looking through Security and System doesn't turn much up, but looking at the Powershell log there's some warnings for remote command execution. Looking at the first warning, there's byte arrays and some code to unpack 2 of them into 'Special Orders' and rearrange the bytes of the 3rd into Shellcode (very kind of the intruders to provide helpful comments in their script). 

![Powershell event](https://user-images.githubusercontent.com/55161488/169666989-befeddcf-bc6a-4a69-9e10-1890ee86c434.png)

Special Orders sounds pretty promising, so I put the steps to unpack the byte arrays into a quick powershell script and get out a trail of ascii numbers. Put that into CyberChef and we get the flag!
