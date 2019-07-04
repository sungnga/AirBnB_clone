# AirBnB Clone - The Console
A Holberton School project of AirBnB clone

<p align="center">
![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/263/HBTN-hbnb-Final.png)
</p>


## Description
A collaborated team project that is part of the Holberton School Software Engineering curriculum.

This project is the first step towards building a full web application of the AirBnB clone. In this first step we are building a console, a custom command interpreter that will be used in subsequent AirBnB projects to manage objects of our classes.

This console will allow us to do the following:
* Create a new object
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object


## Usage
* The console can be run in both interactive and non-interactive mode.
* It prints a prompt **(hbnb)** and waits for the user for input.

### Interactive Mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

### Non-Interactive Mode:
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```


## Commands
Command | Description
--- | ---
`quit` | Exits the program
`EOF` | Exits the program
`create <class>` | Creates an instance of a class
`show <class> <id>` | Prints the string representation of an instance of a class based on class name and id
`destroy <class> <id>` | Deletes instance of a class based on class name and id
`all` | Prints all string representations of all instances
`all <class>` | Prints all string representations of all instances based on class name
`update <class> <id> <attribute name> "<attribute value>"` | Updates an attribute of an instance based on class name and id
`<class>.all()` | Retrieves all instances of a class
`<class>.count()` | Retrieves the number of instances of a class
`<class>.show(<id>)` | Retrieves an instance based on its id
`<class>.destroy(<id>)` | Destroys an instance based on its id


## Models
The [models](./models/) folder contains all the classes used in this project.

File | Description | Attributes
--- | --- | ---
[base_model.py](./models/base_model.py) | Defines the BaseModel class | id, created_at, updated_at
[user.py](./models/user.py) | Defines the User class. Information of users | email, password, first_name, last_name
[amenity.py](./models/amenity.py) | Defines the Amenity class. Information of amenity | name
[city.py](./models/city.py) | Defines the City class. Information of the city | state_id, name
[state.py](./models/state.py) | Defines the State class. Information of the state | name
[place.py](./models/place.py) | Defines the Place class. Information of accomodation | city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude, amenity_ids
[review.py](./models/review.py) | Defines the Review class. Information of review | place_id, user_id, text


## File Storage
The folder [engine](./models/engine/) manages the serialization and deserialization process of all the data for all the classes in this project.


## Tests
* All the codes are tested with the Python unit testing module - unittest.
* The tests for the classes in the [test_models](./tests/test_models/) folder.


## About
The files are interpreted/compiled on `Ubuntu 14.04 LTS` using `python3`.

---

## Authors
This project was created by
* **Drew Maring** - Github: [dmaring](https://github.com/dmaring)
* **Nga La** - Github: [sungnga](https://github.com/sungnga)
