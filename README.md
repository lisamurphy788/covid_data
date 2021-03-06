# Covid Data Tracker 
![Mock up of home](/readmeimages/amiresponsiveimgcoviddata.PNG)

[Link to Covid Data Tracker](https://covid-data2022.herokuapp.com/)

# Project Goals
The goal of the project was to create a database application that could be used to record covid data. During the pandemic the media recorded and updated the country on numbers stats etc. The application should allow a user to record the daily cases of covid and provide a updated summary once that data has been inputted. 

![Image of home screen](/readmeimages/enteryourdata.PNG)
##  How to use the tracker
Once the application is opened in Heroku the terminal will request the user to provide inputs. 

[Read more about the Covid here](https://en.wikipedia.org/wiki/COVID-19)

# User Experience

## User Stories 
1. As a user, I want to be able to enter in the daily Covid data. 
2. As a user, I want the daily data to update the overall summary data.
3. As a user, I want to see my inputs.
4. As a user, i want my excel to update once i have all my inputs entered.
5. As a user, I want to be able to see the totals per column eg, the five totals in a row, then broken out individually, Hospitalisations, Male, Female and Total Deaths after the data has ran.
6. As a user, I want to know if i have entered in too many or too few inputs. 
7. As a user, I want to know if I have made an error and recieve feedback on ho to correct this. 


# Features

## All features

1. Welcome page:

![welcome page](readmeimages/enteryourdata.PNG)

- Welcomes the user and requests the Covid Data inputs. 

2. Results 

![Record Data](readmeimages/dataentered.PNG)
- The data is entered and the data is checked to make sure it is valid. There are a required number of inputs, which in this case is 5 and that all the inputs are numbers seperated with a ','.
- If four numbers were entered the following error message would appear. 

Validation Messages

![Error message](readmeimages/validationerror.PNG)

- Also if a letter was entered instead of a number then the following message would appear. 

![Error message](readmeimages/errormsgtwo.PNG)

Updating Results 

- When all the data is entered correctly it will update the total results and display the entries in the record sheet, and the record row. Then it displays the summary sheet entries. 

![updating dating results](readmeimages/updatingresults.PNG)

New Summary Results 

- The data is then updated and displays the new results updated to the summary sheet under the New Summary row adding the data entered to the last row of the summary sheet. 

![new summary results](readmeimages/newsummaryresults.PNG)

Totals Displayed 

- The new totals are displayed in a row to give the new totals includeing the newly entered data and then will break down the final four column headings so the user is aware of the new results and they are easly viewed. 

![New Totals displayed](readmeimages/summarytotals.PNG)


## Future Features to implement:
- Option to have a list of numbers to choose so the user picks what fuction they would like to use. 
Example press 
1. To Enter data
2. View summary totals
3. To view total Confirmed Covid Case
4. To view total Hospitalised Case
5. To view total Male Cases
6. To view total female Cases
7. To view total Covid Deaths


# Technologies used 
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) - Content and structure
* [Heroku](https://id.heroku.com/login) - Host
* [Gitpod](https://www.gitpod.io/) - Coding workspace
* [Github/ Github pages](https://github.com/)- Commit my code
* [Am I responsive?](http://ami.responsivedesign.is/#)- To see display the website as mock ups  


# Testing 
- Throughout the project developement I was contineously testing through print statements on the gitpod terminal. 
- Continued testing on Heroku to try to improve the appearance of the data.

## Validator Testing 
- I used [PEP8 Python Validator](https://validator.w3.org/#validate_by_input) to check python code for errors 
- PEP8 code validator and returned no errors

![PEP8 Validator](readmeimages/pep8validator.PNG)


## User story testing
1. As a user, I want to be able to enter in the daily Covid data. COMPLETED 
2. As a user, I want the daily data to update the overall summary data.COMPLETED 
3. As a user, I want to see my inputs.COMPLETED  
4. As a user, I want my excel to update once I have all my inputs entered. COMPLETED 
5. As a user, I want to be able to see the totals per column eg, the five totals in a row, then broken out individually, Hospitalisations, Male, Female and Total Deaths after the data has ran.COMPLETED  
6. As a user, I want to know if i have entered in too many or too few inputs. COMPLETED 
7. As a user, I want to know if I have made an error and recieve feedback on ho to correct this. COMPLETED 

I have provided screen shots for all of the above in the features section. 

## Bugs
- I came accross few bugs. 
1. creds.json file
- Initally when I set up the excel file to link it to the gitpod environment I never pinned it. So I left if for a week and came back to it and the creds.json file that I had in my gitignore had disappeared. Once I became aware I went back over the set up of the files and just copied over the file again and everything worked.  
2. Trailing whitespace 
- I had a large number of trailing white space so I went through that and fixed. 
3. Flake8 error messages
- I just changed to flake8 linter to fix the errors and went through each of the errors. 
4. Gitpod.yml - jupyter extension is not synced.
- I have not fixed this as it is a known error and does not cause the code any problems. 


# Deployment

The game was deployed via Heroku. I followed the same insturctions that were given in the love sandwiches tutorial. 
1. Sign in to the Heroku website 
2. Create new app
3. Enter the app name and chose Europe as a region 
4. Select the app and go to settings. 
5. Under settings tab, config vars and click reveal config vars, there are two config vars that need to be set,  1st. -  is CREDS.json file, and the 2nd -  is to set the PORT to 8000
6. Go to buildpack button. Select python and node.js and they must be in that order. 
7. Under deploy tab, link the Heroku app to the correct repository and connect
8. Confirm the correct branch and choose either to automatically or manually deploy your app. Then did a manually build pack. 
9. The Build process will begin and once finished you get a message to confirm. 


# Credits
- Love Sandwiches project
- Code Institute 


# Acknowledgements
- Tutor support - I recieved a huge amount of help and guidance from Scott and John in tutor support. 
- My Mentor
- My cohort facilitator
- My classmates
- Community on Slack



