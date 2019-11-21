# README #

**Setup Instructions**

  Clone repo

  ```
  $ git clone https://github.com/brightkan/tukole-web-api.git
  ```

  Install [pipenv](https://pypi.org/project/pipenv/)
  ```
  $ pipenv install 
  ```
  
  Activate virtualenv  
  ```
  $ pipenv shell
  ```

  Migrate
  ```
  $ python manage.py migrate
  ```
  
  Run app
  ```
  $ python manage.py runserver
  ```
 Format and Analyse
  ```
  $ black . -S --config black.toml
  $ flake8 . 

  ```
