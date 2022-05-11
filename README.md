# PITCH SITE
## Author

[Brenda Nthenya](https://github.com/brenda-nthenya)

# Description
This  is a flask application that allows users to post one minute pitches and also allows other users who have signed up to comment and upvote or downvote a pitch. It also allows a person to signup to be able to access the functionalities of the application

## Live Link



## User Story

* Comment on the different pitches posted py other uses.
* See the pitches posted by other uses.
* Vote on s pitch they have viwed by giving it a upvote or a downvote.
* Register to be allowed to log in to the application
* View pitches from the different categories.
* Submit a pitch to a specific category of their choice.

## BDD
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Load the page | **Page load** | Get all posts, Select between signup and login|
| Select SignUp| **Email**,**Username**,**Password** | Redirect to login|
| Select Login | **Username** and **password** | Redirect to page with app pitches based on categories and commenting section|
| Select comment button | **Comment** | Form that you input your comment|
| Click on submit |  | Redirect to all comments tamplate with your comment and other comments|





## Development Installation
To get the code..

1. Cloning the repository:
  ```bash
  https://github.com/brenda-nthenya/pitch_deck.git
  ```
2. Move to the folder and install requirements
  ```bash
  cd pitch-world
  pip install -r requirements.txt
  ```
3. Exporting Configurations
  ```bash
  export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}
  ```
4. Running the application
  ```bash
  python3 manage.py server
  ```
5. Testing the application
  ```bash
  python3 manage.py test
  ```
Open the application on your browser `127.0.0.1:5000`.


## Technology used

* [Python3.6](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)
* [Heroku](https://heroku.com)


## Known Bugs
* There are no known bugs currently but pull requests are allowed incase you spot a bug


## License
### MIT License

Copyright (c) 2022 brenda-nthenya

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
