# AirBnB Clone Project

 The ***Goal*** of the project is to deploy on your server a simple copy of the [AirBnB website](https://www.airbnb.com/)

 ![My GIF](https://media1.tenor.com/m/bGCuW8uql2kAAAAC/office-server.gif)

## 💡   Project Features
- Has A storage System ***(FileStorage Class)*** That storages data into ***JSON Format***
- Contains a ***BaseModel*** that has all features of the website BackEnd Needed information ***( User - State - Place - Review - City - Amenity )***
- Has a ***console*** that manages all information of objects stored in ***JSON File***

## 💻 What is The Console


![My GIF](https://i.pinimg.com/originals/3e/5b/31/3e5b31543f93a24ef48e52bc4b55d68c.gif)


Do you remember the **Shell** ? It’s ***exactly*** the same but ***limited*** to a specific use-case.

***In our case***, we want to be able to manage the objects of our project:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

###  🚀  How to start it

Simply Run The Console File In Your terminal

```
./console.py
```

***Make Sure*** it is executable first

### 👌 How to use it

these are the commands that you will need

| Command             | Description                          |
|---------------------|--------------------------------------|
| quit                | Exits the Console

| Command             | Description                          |
|---------------------|--------------------------------------|
| create              |Creates a new instance of BaseModel, saves it (to the  JSON file) and prints the id. Ex: $ create BaseModel


- If the class name is missing, it print ** class name missing ** (ex: $ create)
- If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ create MyModel)

| Command             | Description                          |
|---------------------|--------------------------------------|
| show                |Prints the string representation of an instance based on the class name and id. Ex: $ show BaseModel 1234-1234-1234.

-   If the class name is missing, print ** class name missing ** (ex: $ show)
-   If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ show MyModel)
-   If the id is missing, print ** instance id missing ** (ex: $ show BaseModel)
-   If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: $ show BaseModel 121212)

| Command             | Description                          |
|---------------------|--------------------------------------|
| destroy             |Deletes an instance based on the class name and id (save the change into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234.

-   If the class name is missing, print ** class name missing ** (ex: $ destroy)
-   If the class name doesn’t exist, print ** class doesn't exist ** (ex:$ destroy MyModel)
-   If the id is missing, print ** instance id missing ** (ex: $ destroy BaseModel)
-   If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: $ destroy BaseModel 121212)

| Command             | Description                          |
|---------------------|--------------------------------------|
| all                 |all: Prints all string representation of all instances based or not on the class name. Ex: $ all BaseModel or $ all.

-   The printed result must be a list of strings (like the example below)
-   If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ all MyModel)

| Command             | Description                          |
|---------------------|--------------------------------------|
| update                |update: Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
-   Usage: update <class name> <id> <attribute name> "<attribute value>"
-   Only one attribute can be updated at the time
-   You can assume the attribute name is valid (exists for this model)
-   The attribute value must be casted to the attribute type
-   If the class name is missing, print ** class name missing ** (ex: $ update)
-   If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ update MyModel)
-   If the id is missing, print ** instance id missing ** (ex: $ update BaseModel)
-   If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: $ update BaseModel 121212)
-   If the attribute name is missing, print ** attribute name missing ** (ex: $ update BaseModel existing-id)
-   If the value for the attribute name doesn’t exist, print ** value missing ** (ex: $ update BaseModel existing-id first_name)
-   All other arguments should not be used (Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com" first_name "Betty" = $ update BaseModel 1234-1234-1234 email "aibnb@mail.com")
-   id, created_at and updated_at cant’ be updated. You can assume they won’t be passed in the update command
-   Only “simple” arguments can be updated: string, integer and float. You can assume nobody will try to update list of ids or datetime

## ⚠️ Note Here

-    All Commands Are Case Sensitive   

-    All of These command work in this form also

```
ClassName.command("Arguments if required")
```

### Example
```
User.all()
```

## ✅ Example On How It Works

```


(hbnb) all MyModel


** class doesn't exist **

(hbnb) show BaseModel

** instance id missing **

(hbnb) show BaseModel My_First_Model

** no instance found **

(hbnb) create BaseModel

49faff9a-6318-451f-87b6-910505c55907

(hbnb) all BaseModel

["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}

(hbnb) destroy

** class name missing **

(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"

(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}

(hbnb) create BaseModel

2dd6ef5c-467c-4f82-9521-a772ea7d84e9

(hbnb) all BaseModel

["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]

(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907

(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907

** no instance found **

(hbnb) 

```