Intro To Windows - Easy 2 Write Up                            
Alec Miller

Challenge: Looks like there is something malicious running on startup, this hack runs deeper than we thought.                   

![1](https://user-images.githubusercontent.com/55161488/134848871-6a7241a7-a1c6-45d4-aca3-9eb5c52a1e54.jpg)

Pretty straightforward to begin, try to find something that runs on startup that looks malicious. Open up Powershell and type Get-Process to see what's running. 

![2](https://user-images.githubusercontent.com/55161488/134848897-74b10100-880d-4075-b5e3-464fc7bb655e.jpg)

Reading through the list of processes doesn't turn up anything unordinary looking. So let's look at services now (basically background processes). Type Get-Service to display these. 

![3](https://user-images.githubusercontent.com/55161488/134848915-32c6b1eb-cd45-46b2-97c6-13699e748403.jpg)

At first, reading through doesn't look like there's anything interesting… but then:

![4](https://user-images.githubusercontent.com/55161488/134848923-2030120d-60d9-4593-b896-0896a00acb38.jpg)

That certainly looks worth investigating. Go to the start menu and type Services to bring up the windows utility for viewing services, Scroll down until you get to "HackerBackdoor", and there's the flag!

![5](https://user-images.githubusercontent.com/55161488/134848944-44bc9d0c-69f9-4ccc-8bc1-36e141256816.jpg)
