Intro To Linux - Hard 1 Write Up                                
Alec Miller

Challenge: Become a Hard1 User

To see the users on the machine, login as ritsec and type cd /home to get to the home directory. Type ls to see all the user folders in the home directory.

![users](https://user-images.githubusercontent.com/55161488/134847846-9c3e4e5b-f2c9-4485-80b9-c07eeefc0628.jpg)

So we can see that there is a user named Hard1, so we need to get access to that account. So we can move into Hard1's user directory by typing cd Hard1. Then to see what's in Hard1's directory type ls -la.

![files](https://user-images.githubusercontent.com/55161488/134847870-6d6ccf31-be76-4e00-bf71-a3ca33840e24.jpg)

So there's a couple interesting things here, but especially id_rsa. And looking at the file permissions, everyone has read, write, and execute permissions. So to just take a look at the file, type more id_rsa.

![ssh_key](https://user-images.githubusercontent.com/55161488/134847885-7051f33c-7923-4bd9-b747-89d4756e631a.jpg)

It's Hard1's private ssh key, which we can use to login as Hard1, completely unencrypted and accessible. So let's copy that ssh key over to the ritsec directory so we can use it to login as Hard1, by typing cp id_rsa /home/ritsec/Hard1_id_rsa. Now we can try to login as Hard1 through ssh. Type ssh Hard1@localhost -i Hard1_id_rsa. 

![error](https://user-images.githubusercontent.com/55161488/134847893-9e742faa-7cf2-4bfa-9c1d-f5a3807f89ea.jpg)

So it won't allow connection through ssh because it recognizes the private key file is insecure, so it's prompting for the password instead. Exit out of that command with CTRL+C since we don't know Hard1's password. Well that can be fixed by modifying the permissions so that only the owner (for this copy, ritsec) has permissions. Type chmod 600 Hard1_id_rsa to set those permissions. Type ls -l to view file permissions to make sure the permissions we want were set properly.

![chmod](https://user-images.githubusercontent.com/55161488/134847906-3c7be289-036b-4ca1-8a2b-c648c851a5c1.jpg)

Now that the private key permissions are more secure, we should be able to login through ssh. Type ssh Hard1@localhost -i Hard1_id_rsa again. This time it worked. Now let's look around a bit for the flag, so type ls -la, and we can see a file named Hard1. To look at that file type cat Hard1, and there's the flag!

 ![flag](https://user-images.githubusercontent.com/55161488/134847929-0df92ffb-dc48-4e26-a28b-38ed3b8965b2.jpg)

