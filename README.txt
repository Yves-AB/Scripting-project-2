Step by step:
1- First if all i imported sys in order to be able to take inputs from the user from shell (command line arguments)
At first i faced an error where if i did not write the url after the file it would throw exceptions because the keep would keep running. So i added an if statement to take care of that.

2) when i first wrote my code i did not check for exceptions. So after i wrote it fully and tried running it i came across many exceptions . In which i first tried taking care of each individually but you recommended me to catch all general exceptions .

3) After that i created a loadfile() method that loads the file u sent us in order to scan for the directories and subdomains. The method returns 2 vars which i stored. 

4) Next i watched a youtube video that explained the request library and it's functionality. I found out that if the request im sendign is equal to 200 or then its valid and if its above 404 then it's invalid 