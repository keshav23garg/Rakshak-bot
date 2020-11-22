# Rakshak-bot

##Idealogy    
RakshakBot is designed to save lives and provide essential supplies during natural calamities. We are designing a 4-wheel robot to communicate with our servers     and obtain data to traverse through a wreaked area. It is designed to plan the most suitable and fastest way to traverse through the city using our path finding   
algorithm.   

##Code Information :   
######Rakshak_bot.py :- This is code is designed to simulate the workflow of our Rakshak Bot.    
    Usage :- python3 code and written in a linux based environment    
    libraries used :-tkinter , pyautogui , os , numpy , open-cv or cv2 , webbrowser , time.      
    Steps to execute :-   
                        1. Run the script       
                        2. From GUI either select Custom image mode or G-Map mode either way select desired file or enter corresponding latitude and longitude    
                        3. A processed image will pop-up asking you to select start and point of the travel in your maze     
                        4. If possible a path would be generated and on a keystoke a simulation would start.    
##Features   
######Path Planning:   
We get a satellite image of a city and with help of image processing and our path planning algorithm we find the shortest path for the traversal of our     RakshakBot.    
The algorithm we have used here is BFS (Breadth-First Search), a traversal algo for tree and graph data structures.   
######Smart Traversal:        
After the path being transmitted to the bot via our server the robot can traverse the plain smartly by avoiding obstacles in its path using different sensors like   
ultrasoninc sensor and LIDAR sensors. In case of any serious problem communication back to server can be easily established and another path could be easily   
planned.  
######High Durability and Better power solutions  
We are planning to use industrial and defence grade materials to build our RakshakBot to have high durabilty in adverse environments and also using modern Solar   
power battery management systems to prevent any power shortage and less harm to our environments.Also it could carry a large amount of supplies due to better   
materials.   

##Application of Rakshak Bot  
    1. It can carry supplies for the people stuck in such areas.  
    2. Show path to confused people (suffering shock is a common outcome during such mishap).   
    3. This bot can also be used to explore those areas which are difficult for humans.  
    
##WorkFlow and Latest Updates:-  
    Date - 21 Nov, 2020   
      V1 of Rakshak_bot.py :- creates simulation for the path planning of the bot in open-cv by fetching google maps of desired locations or custum made mazes   
      saved on your pc , select start and end point using your mouse and get started with the script.   
 

##Contributers:-  
Keshav Garg  
Kamal Yadav  
Varchasv Thakkar  
Aayush   

