Intro To Linux - Hard 2 Write Up                                
Alec Miller

Challenge: Use ctrl+c to stop a command, the clear command to reset your screen, and cp command to make backups of files. You’re gonna need it :)

So based on the previous challenge to access Hard1's account, let's look around Hard1's directory some. Type ls -la to see what's there. 

![1](https://user-images.githubusercontent.com/55161488/134848432-d094111b-894b-47ea-b2cd-f25734fc4d21.jpg)

So we can see there's a file called Hard2, which looks promising. Type file Hard2 to figure out more about it. 

![2](https://user-images.githubusercontent.com/55161488/134848441-e772a802-63ce-4320-a4f5-94d0c943ea46.jpg)

So it's a gzip file, which is a type of compressed file, and it has been renamed from Almost.tar.gz.There. To unzip a gzip file type gunzip Hard2. This doesn't work as the file type is recognized, so let's try renaming the file to Hard2.gz  by typing mv Hard2 Hard2.gz. That seems to work so type ls -la to see what we got. Now there's a new file called Hard2, so type file Hard2 to find out more information. 

![3](https://user-images.githubusercontent.com/55161488/134848445-ce79543c-395a-40e6-b020-9bf8d7e3cee7.jpg)

Another gzip file, so let's just do what we did on the first gzip file again. Rename the file so it recognizes the extension, run gunzip, and look at the new file.

![4](https://user-images.githubusercontent.com/55161488/134848453-bbf50763-bbee-48a6-bb44-2d4432dde55e.jpg)

So now it's a tar archive, that's new. Another thing to note is that the file sizes of the Hard2 file have gotten larger with each gunzip. Tar is just another type of compressed file, so type tar -xvf Hard2. And now we have a new file named Hard2. Use file Hard2 and we can see that it's an ASCII file. Use more Hard2 to dump the file contents. 

![5](https://user-images.githubusercontent.com/55161488/134848456-9b7e5a01-cac0-49fa-b1e7-82cbc02599a0.jpg)

So Hard2 looks like a hexdump, and there's no discernable file type since there's no file signature bits at the beginning (ex. JPG, PNG, etc). If we want to really figure out what the file is, we can convert it into its original binary. To do that, and send the output to a new file so we don't lose the original, type xxd -r Hard2 > Hard2_b. Type ls -la to see the new file, and type file Hard2_b to find out more information. Still looks like an ASCII file, so type head Hard2_b to see what the beginning looks like.

![6](https://user-images.githubusercontent.com/55161488/134848465-2958253c-5f74-4d34-95e7-90c6e2cc45f4.jpg)

Still looks like a hexdump, so we'll repeat our last step of converting to binary and saving to a new file. Looking at the ls -la output, we can see that Hard2_b is a smaller file than Hard2, which indicates that we're getting closer to the real file. So keep repeating the binary conversion for a bit, checking each new file to see if it still looks like a hexdump, or if it's a new file type. And eventually, you get to this: 

![7](https://user-images.githubusercontent.com/55161488/134848470-2d0c9cae-f361-459d-a656-a9fbbe83c635.jpg)

It's a gzip file, so we know what to do with that, rename to Hard2_b10.gz (b10 to avoid overwriting Hard_b9) and gunzip.

![8](https://user-images.githubusercontent.com/55161488/134848474-cc3c7ff7-26ce-4518-a190-1cf97c985db8.jpg)

And file Hard2_b10 shows it's an ASCII file, so cat Hard2_b10 reveals the flag.

![9](https://user-images.githubusercontent.com/55161488/134848481-560632ad-b23a-487f-bbfe-69705c39702c.jpg)

