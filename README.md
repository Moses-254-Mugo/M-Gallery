# M-Gallery
## Contributors
* Fell free to comment, critique or even submit a pull request

## Author
Mugo Moses

## Description
M-Gallery is a django application that allows users display their photos for others to see.

## Screenshots


## Setup Instructions:
 ### Requirements
 1. Clone the repository by running

        git clone https://github.com/Moses-254-Mugo/M-Gallery.git
    Navigate to the project

        cd M-Gallery
 2. Create a virtual enviroment

         pip install virtualenv 

    To activate the created virtual environment, run

        source virtual/bin/activate
3. Create database
    You will need to create a new postgress database by typing the following command to access postgress

        $ psql

    Then run below query to create a new database named gallery

        # create databases gallery;
5. Create Database migrations
    make migrations on postgres using django

        python3.8 manage.py makemigrations garage
    then run the below command.

        python3.8 manage.py migrate

6. Run the app
    To run the application on your development machine,

        pythong3.8 manage.py runserver
### Running Tests
To run tests;

        python3.8 manage.py test
## Techonogies Used
* Phthon3.8
* Django
* HTML
* Bootstrap
* Css

## User Stories 
1. View different photos that interest me.
2. Click on a single photo to expand it and also view the details of the photo.
3. Search for different categories of photos.
4. Copy a link to the photo to share with my friends.
5. View photos based on the location they were taken

## Support and contact details
If you have any question, want to contribute to the code? Please email me at 
moseskinyua12@gmail.com
## License
The project is under[MIT License](LICENSE).