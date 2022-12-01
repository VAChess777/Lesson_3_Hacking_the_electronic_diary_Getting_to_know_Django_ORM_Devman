# Hacking the electronic diary 

The program hacks the database of the electronic diary of the school, removes the student's bad grades. Replaces bad grades with good ones. Removes bad comments in the student's diary. Praises students, instead of teachers)))
### Software environment and installation:

Python3 should already be installed.

### Program installation:

Download the code: [https://github.com/VAChess777/Lesson_3_Hacking_the_electronic_diary_Getting_to_know_Django_ORM_Devman](https://github.com/VAChess777/Lesson_3_Hacking_the_electronic_diary_Getting_to_know_Django_ORM_Devman), or clone the `git` repository to a local folder:
```
git clone https://github.com/VAChess777/Lesson_3_Hacking_the_electronic_diary_Getting_to_know_Django_ORM_Devman.git
```

### Installing dependencies:
 
Use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```bach
pip install -r requirements.txt
```

### About environment variables:

The program `settings.py ` there are environment variables in the `project` folder that are responsible for configuring access to the database.
create a `.env` file, place it in the root directory of the program. Put the following data in the `.env` file in the `key=value` format.
                                                               
`DB_NAME=` - Database name. 
`SECRET_KEY=` - Django secret key.              
`DEBUG=` - True for enabling debugging mode, False for production. The default value is `False`.                                                         
`ALLOWED_HOSTS=` - This is a security measure to prevent HTTP Host header attacks, which are possible even under many seemingly-safe web server configurations.
Example of ALLOWED_HOSTS settings in file. env - `ALLOWED_HOSTS = ['www.djangoproject.dev', 'docs.djangoproject.dev', 'localhost' ...]`. Where
`www.djangoproject.dev', 'docs.djangoproject.dev, 'localhost'` -  addresses of allowed hosts. The default value is `localhost`.   

### How to run the program:

Enter the command in console: `$ python main.py schoolkid_and_subject {Фролов Иван Математика}`. Enter the last name and first name of the student who needs to pump the diary,
as well as the subject on which you need to receive praise from the teacher. For example: `python main.py schoolkid_and_subject Фролов Иван Математика`.

### How the program works:

The program contains scripts:

```main.py``` - the main program.  
```manage.py``` - the program that runs the server.
```settings.py``` - the program is located in the project folder. Responsible for setting up access to the employee database.   
```models.py``` - the program is located in the datacenter folder. The program is responsible for data models and their fields.          
```urls.py``` - the program is located in the project folder. Responsible for setting up links to the 'security console' pages.          
            
### Features works of the program:

The `main.py` program contains the functions:

* The `active_passcards_view` function - get active employee passes from the database.



### Project Goals

This code was written for educational purposes as part of an online course for web developers at [dvmn.org](https://dvmn.org/).