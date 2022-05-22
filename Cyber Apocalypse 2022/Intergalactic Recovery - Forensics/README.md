Cyber Apocalypse Writeup: Intergalactic Recovery

For this challenge we were given a zip file with 3 disk image files, and there was a note in the description about RAID5. Looking at the .img files, disk1 and disk2 were both about 5 mb, but disk3 was only about 4 kb, so it isn't complete. 

Without 3 full disks, the original files can't be restored, however we can use disk1 and disk2 to repair disk3. One of the aspects of RAID5 is that it is redundant, and a damaged disk can be repaired by doing a byte-wise xor of the other 2 disks. 

![RAID5 parity](https://user-images.githubusercontent.com/55161488/169713049-3997bdf6-efee-48a7-8a16-4ca7dfdc8297.png)

I wrote a quick python script to xor disk1 and disk2, writing the output to disk3_new.img, and now we can recreate and mount the RAID5 to see the files. There's a couple steps that need to happen here. 

First we need to create loop devices for each of the disks. Loop devices are pseudo-devices that let a file be treated like a block device. These can be created by running *sudo losetup /dev/loop# diskfile* for each of the images respectively to create 3 loop devices. 

Now we need to actually create the RAID5, which can be done using *mdadm --create /dev/md0 --level=5 --raid-devices=3 /dev/loop#1 /dev/loop#2 /dev/loop#3*. This creates the directory /dev/md0 which can then be mounted using *mount /dev/md0*. 

Navigating to that directory, there's only one file, which looks like a corrupted pdf when I try to open it. Another property of RAID5 here, the order in which the disks are assembled (aka the order of loop devices in the mdadm command) is relevant, otherwise the data gets all mixed up. So it's the right approach, just the wrong order. Since there's only 3 devices however, that means there's only 6 possible permutations (no repetition with this), so I just start going through them.  

The process of removing and reassembling the RAID5 turned out to be a bit finicky. First I unmounted the device with *umount dev/md0*, then deleted the device with *mdadm --stop /dev/md0*, and *mdadm --zero-superblock /dev/md0*. After repeating the create/delete process a couple times, I got a non-corrupted pdf that showed the flag!