# Covid Data Tracker 
![Mock up of home](/readmeimages/amiresponsiveimgcoviddata.PNG)

[Link to Covid Data Tracker](https://covid-data2022.herokuapp.com/)

# 1. Project Goals
The goal of the project was to create a database application that could be used to record covid data. During the pandemic the news use to update the country on numbers stats etc. The application should allow a user to record the daily cases of covid and provide a updated summary once that data has been inputted. 

![Image of home screen](/readmeimages/enteryourdata.PNG)
##  How to use the tracker
Once the application is opened in Heroku the terminal will request the user to provide inputs. 

[Read more about the Covid here](https://en.wikipedia.org/wiki/COVID-19)

# 2. User Experience

## 2.1 User Stories 
1. As a user, I want to be able to enter in the daily data. 
2. As a user, I want the daily data to update the overall summary data.
3. As a user, I want to see my inputs.
4. As a user, i want my excel to update once i have all my inputs entered.
5. As a user, I want to be able to see the totals per column eg, Covid Confirmed Cases, Hospitalisations, Male, Female and Total Deaths after the data has ran.
6. As a user, I want to know if i have entered in too many or too few inputs. 
7. As a user, I want to know if I have made an error and recieve feedback on ho to correct this. 


# 3. Features

## 3.1 All features

1. Welcome page:
![welcome page](readmeimages/welcome.png)
- Welcomes the players and asks for their names.

2. Instructions & first go:
![instructions page](readmeimages/instructions.png)
- Give instructions on ho to play Connect four to the players. 
- Print the board for the first player to use. 
- Ask the first player for their selection. They can choose a column from 0 to 6.
- The player needs to type the number into the terminal.

3. Players turn:
![piece drop](readmeimages/piecedrop.png)
- The players take it in turns to drop their pieces. 
- As you can see in the image above, Ange's pieces are "1" and Tom's pieces are "2".

4. Player wins:
![win](readmeimages/win.png)
- When a player gets 4 pieces in a row the game is over. 
- The terminal prints who the winner is.
- The terminal asks the players if they would like to play again. 
- If they select Y it will take them to the start. 
- If they select N it will thank them for playing. 


## 3.2 Features to implement:
1. Play agianst the computer
2. Users to recieve a message if the game is a draw. 
3. Score Board. 
4. Colour markers for players.



# 4. Technologies used 
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) - Content and structure
* [Heroku](https://id.heroku.com/login) - Host
* [Gitpod](https://www.gitpod.io/) - Coding workspace
* [Github/ Github pages](https://github.com/)- Commit my code
* [Am I responsive?](http://ami.responsivedesign.is/#)- To see display the website as mock ups  
* [NumPy](https://numpy.org/) - To create a matrix for the board. 
* [termcolor](https://pypi.org/project/termcolor/) - To change the colors of the error messages and the welcome/end message. 



# 5. Testing 
 -  Used [PEP8 Python Validator](https://validator.w3.org/#validate_by_input) to check Python content.
- Validate user input tested for intergers, full colums and numbers over 6. 
- Tested in Gitpod terminal and Heroku. 

## 6. Deployment

Steps for deployment:
1. Clone this repository in Github
2. Create [Heroku](https://dashboard.heroku.com/apps) app
3. Under settings tab, add Python and Node.js buildpacks in this order
4. Under settings tab, add PORT and 8000 to config vars.
5. Under deploy tab, link the Heroku app to this repository.
6. Deploy app



## 7. Credits