Cyber Apocalypse Writeup: Fuel Crisis

For this challenge we were given a zip file containing a directory called application. Inside this directory there were a couple html files, images, 2 python files, and a file called model.h5. The python programs were the source code for the challenge website accessible through a docker instance, and allowed for running the challenge locally using flask. 

![challenge website](https://user-images.githubusercontent.com/55161488/170798998-03bd1c09-7229-429e-bee7-cac24fe7e85e.png)

The challenge description referenced a model, so looking at the model.h5 file first, it turns out it is a 'Hierarchical Data Format (v5)' file, which is a file designed to store large quantities of numerical data. I found an application called Panoply3 to view this type of file, but looking at the data itself didn't provide much insight, so I went back to looking at the challenge website. 

The goal of the challenge was to avoid the last ship in the 'Docking queue' from getting flagged, since 32166 was a banned ID, but it needed to recognize the first four ships' IDs correctly. The only way to interact with the system was by uploading a model.h5 file, so it seems that the model needs to be altered in some way to let that happen. Since the ship IDs were screenshots and being recognized by optical character recognition (OCR), it looks like the model.h5 file is a machine learning model of some type to do that character recognition. 

Looking at the source code for app.py, we can see an import for tensorflow and numpy, and later it loads a dataset called mnist. Looking up that dataset, the characters look similar to the ship IDs, so the model was almost certainly trained with that dataset. 

![mnist dataset](https://user-images.githubusercontent.com/55161488/170801598-cb9f4116-3d0d-4348-b4ef-43c504d862f4.png)

So at this point, the goal is to find a way to modify the model to mess with the last ID, without impacting the first 4. Looking at the ship IDs a bit closer to see if there's anything specific to the last ID, it turns out that '2' only shows up in the last ID. So there should be a way to mess with the model's ability to recognize '2', which would then misclassify the ID. 

Looking at tensorflow a lot more, the way the model is trained is using a set of images associated with 'labels'. So maybe by replacing every label of '2' with another digit, it would be possible for the model to always misclassify a '2' as that other digit, I picked 5 but anything should work here. In order to prevent any issues with completely removing '2', I replaced every '2' label except the first one with '5'. 

I wrote a python script to load in and modify the mnist dataset to re-label the '2' pictures, and use that to retrain the model. After a bit of debugging of the model settings, we got to the flag page! \*(placeholder because I got screenshot while running locally)

![placeholder](https://user-images.githubusercontent.com/55161488/171051763-0c721f55-2fa8-4d02-9e38-cf3adf27e255.png)
