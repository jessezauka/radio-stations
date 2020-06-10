# Irish Radio Stations Directory

The project is a database-driven online Irish radio stations directory. The project utilises Flask to create the application, using MongoDB as a data store, with the bulk of the back-end functionality written in python.

The project includes each function of CRUD, allowing a user to create, read, update and delete stations that are upheld by persistent storage.

## User Stories

As a user, I had an interest in radio stations since young. So I want to create a website with database to allow any users who have the same interest as me to contribute to this website. Therefore, I want this website to be able to:

- Add radio station information
- Display radio station information
- Display play button with ability to listen to radio station
- Edit radio station information
- Delete radio station information


## UX

This project I started with mobile first design approach. I started creating mockups wireframe on Balsamiq Frameworks. The design of the site is fully design by myself, showcasing smooth layout and interactive for most devices. Below are steps by steps of the journey that required to be achieved for this website.

1. I want to create a website to list to radio stations information
2. I link the website to a database (MongoDB)
3. I want to have a minimum display of 10 radio stations information
4. User are able to create own radio station by filling in a form
5. User are able to view their created radio station information
6. User are able to edit any radio station information by editing the form information
7. User are able to delete any radio station
8. User are able to listen to radio station by online HTML5 player
9. I want the website to be mobile, notepad, laptop and large screen responsive
10. I want the website to look trendy, smooth and overall attractive and interactive

## Technologies Used

- Python 3.8
- Flask 1.1.2 (Python Microframework)
- BootStrap 4
- Google Fonts
- JavaScript
- CSS
- HTML
- MongoDB
- Materialize

## Future Features to Implement

In the future, I would like to:
- Improve online HTML5 player
- Create user commenting system
- Add "Recommended stations" to the page (right side)

## Testing

This site is tested to be responsive on the following devices:

- iphone 6/7/8
- ipad
    - Safari
- Samsung Galaxy 8
    - Google Chrome
    - Samsung web browser
- Ubuntu 18.0
    - Google Chrome
- Window 10
    - Google Chrome
    - Firefox
    - Microsoft Edge
    - Internet Explorer 11
- Window 7
    - Google Chrome
    - Internet Explorer 11
    
## Manual testing was conducted to ensure the user story objectives where achieved.

1. Create Radio Information
        - Ensure radio station information is sent to database
		
2. Read Radio Station Information
    - Ensure all the input information is being displayed correctly
 	
3. Edit & Update Radio Station Information
    - Same rules apply to create radio station information
    - Ensure all information changed will be updated and displayed correctly
	
4. Delete Radio Station Information
    - Ensure information is being wipe clean and does not displayed
	
5. Icon Display
    - Ensure display the right icon and size
	
6. Image Display
    - Ensure display the right image and size
	
7. Button
    - Ensure all the button click to the correct link in the website
    
## Deployment 
Deployed on Heroku at [Irish Radio Stations](https://secure-ravine-58828.herokuapp.com/).
* Clone the repository by copying the clone url
* In the terminal type `git clone` followed by the copied url
* `cd` into `radio-stations`
* In the terminal type `pip3 install -r requirements.txt` to install all the dependencies 
* Create an account on Heroku if you don't have one yet and create a new app
* In the terminal, type `echo "web: python main.py" > Procfile`
* Create a new folder inside the apps directory called `secret_settings` and in it a `.env` file or 
change path in `app_setup.py` and create the `.env` file anywhere you'd like
* In the `.env` file set DBNAME, URI and SECRET_KEY
* In the terminal, `heroku login`
* `git init` to create a new repository
* `heroku git:remote -a (name of your heroku app, no brackets)`
* `git add .`
* `git commit -m "Initial commit"`
* `git push heroku master`
* `heroku ps:scale web=1`
* In your heroku app navigate to settings and reveal config vars, set IP = 0.0.0.0, PORT = 5000, DBNAME, URI and SECRET_KEY
* restart all dynos and open your heroku app

## Credits

### Images 

* Background image - [VisitLondon](https://www.visitlondon.com/things-to-do/whats-on/music)

### CDN

* jsDelivr - [jsDelivr](https://www.jsdelivr.com/)

#### Fonts

* Font Awesome - [Font Awesome](https://fontawesome.com/?from=io)

## License

MIT
