# generation-mini-project-1

# When running docker image docker run -t -i (image name)
docker run -t -i michael-huynh-project-image


## Project Background
The aim of this project was to create an application that will store a list of products, couriers and orders for the user to manipulate. The program will have a menu-based command line interface (CLI) that will provide an overview of the menu system for the program.

## Client requirements
It will contain a main menu, products menu, couriers menu and a orders menu. The user will be able to communicate with the interface to manage different activities such as adding a new product, viewing a list of products. The list of products, couriers and orders will be stored within a csv file that will be overwritten when the program has been exited to save any changes the user has made.

## how to run the app
To run the application you will will need to run the program in an integrated terminal and run the command 'py my_project_w1.py' otherwise you can also run the program by selecting the play button in the top right hand corner of visual studio. (Note: if there is an error when using the play button you may need to use the drop down menu located next to the play button after hovering and select to run python file)

## how to run any unit tests
The Non-test driven development (NTDD) can be found in the testing folder, they have been split up into different sections to test each of the functions for the program.

above each functions they are titled to give a brief description below the main parts they are split up to test whether you need to connect to a database or read/write into a file.

Once we are able to save and load the program to a database or file, you will be able to test the functionality of the menu actions separately. Although some difficult functions may need previous functions to be called first.

Note: function calls have been commented out to test other functions you will need to remove the comments to call the functions.

The Test driven development can be run in the unit_testing.py file to test the function for checking input to see if it can be changed to an integer and another function to test the list sorting feature.

## Project Reflections
I really enjoyed this project as I have not coded for a long time, I am happy that I was able to use my past experience in college/university to help me in this project. Being able to understand how to tackle the requirements helped to structure my project very well and understand the importance of unit testing. I am learning new things and recapping on stuff I have forgotten such as databases.

## How did your design go about meeting the project's requirements?
My design aligns with the project requirements very well as it meets majority of the clients needs as they are able to perform all the required actions with the program.

## How did you guarantee the project's requirements?
By reading the requirements carefully before starting on a new feature and focusing on how to tackle them using everything I have learned.

## If you had more time, what is one thing you would improve upon?
implement more fields such as product inventory to the database and attempted to do all of the stretch goals and requirements.

## What did you most enjoy implementing?
I enjoyed unit testing, learning how to sort the orders list and using databases to connect to my program to do various actions such as update, insert, delete and select.