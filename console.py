#!/usr/bin/python3
"""
This Module Contains :-
-   HNBN Command Prompt Class
    Which Acts As The Command Line
    Which Organizes All The Classes Processes

    Class Attributes:
    Prompt - ClassMapping
"""


import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    ClassMapping = {
        "BaseModel": BaseModel,
        "User": User,
        "Amenity": Amenity,
        "City": City,
        "Place": Place,
        "Review": Review,
        "State": State
    }

    def do_quit(self, arg):
        """
        Quit Command : Exits From The Command Interpreter
        """
        return True

    def do_EOF(self, arg):
        """
        EOF (End Of The File) : Exits From The Command Interpreter
        """
        return True

    def emptyline(self):
        """
        EmptyLine : Moves Onto The next line When
                    Pressing Enter Without Entering
                    Any Command
        """
        pass

    def do_create(self, arg):
        """
        Create :    Creates A New Object
                    With Unique ID

        Command Form : Create ClassName

        Class Name Must Be Defined In
        ClassMapping Dictionary
        """
        if not arg:
            print("** class name missing **")
            return

        if arg not in self.ClassMapping:
            print("** class doesn't exist **")
            return

        cls = self.ClassMapping[arg]
        New_O = cls()
        New_O.save()
        print(New_O.id)

    def do_show(self, arg):
        """
        Show :  Prints the string representation
                of an instance based on the
                class name and id
        Example:
        show ClassName ClassId

        Class Name Must Be Defined In
        ClassMapping Dictionary
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        if args[0] not in self.ClassMapping:
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        Obj = storage.all()
        if key not in Obj:
            print("** no instance found **")
        else:
            print(Obj[key])

    def do_count(self, arg):
        """
        count : Count The Number Of
                Instances Of Certain Class
                In JSON File

        Example:
        count ClassName

        Class Name Must Be Defined In
        ClassMapping Dictionary
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        if args[0] not in self.ClassMapping:
            print("** class doesn't exist **")
            return

        c = 0
        Obj = storage.all()
        for key, value in Obj.items():
            ClassName, ClassId = key.split('.')
            if ClassName == arg:
                c += 1
        print(c)

    def default(self, line):
        """
        default :   It is Executed When
                    When The Console Doesnt
                    Find Any Of the Defined
                    Commands

        It Defines The Same Functions Listed
        In The Console But With Different Syntax

        Example:
        ClassName.Command(Arguments If Any)

        Class Name Must Be Defined In
        ClassMapping Dictionary

        Commands Must Be Defined In
        In Console Class
        """
        CommandsList = {
            'all': self.do_all,
            'count': self.do_count,
            'show': self.do_show,
            'destroy': self.do_destroy,
            'update': self.do_update
        }

        Multi_Command = ['show', 'destroy']
        if ('.' in line) and ('(' in line) and (')' in line):

            args = line.split('.')
            ClassName = args[0]
            Comm = args[1].split('(')
            name_com = Comm[0]
            if (ClassName in self.ClassMapping) and (name_com in CommandsList):
                if name_com == 'update':
                    SepAll = (
                        Comm[1]
                        .replace('"', '')
                        .replace(' ', '')
                        .split(',')
                        )
                    Class_id = SepAll[0]
                    Atr_Name = SepAll[1]
                    Atr_Value = SepAll[2].strip('\"').strip(')')
                    CommandsList[name_com](
                        f"{ClassName} {Class_id} {Atr_Name} {Atr_Value}"
                    )
                elif name_com in Multi_Command:
                    Class_id = Comm[1].split(')')[0].strip('\"')
                    CommandsList[name_com](f"{ClassName} {Class_id}")
                else:
                    CommandsList[name_com](f"{ClassName}")
            else:
                print("*** Unknown syntax: {}".format(line))
                return False
        else:
            print("*** Unknown syntax: {}".format(line))
            return False

    def do_destroy(self, arg):
        """
        destroy :   Deletes an instance based on
                    the class name and id
                    (save the change into the JSON file)
        Example :
        $ destroy ClassName ClassId

        Class Name Must Be Defined In
        ClassMapping Dictionary
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        if args[0] not in self.ClassMapping:
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        Obj = storage.all()
        if key not in Obj:
            print("** no instance found **")
        else:
            del Obj[key]
            storage.save()

    def do_all(self, arg):
        """
        all :   Prints all string representation
                of all instances based or not on
                the class name.
        Example:
        $ all ClassName or $ all

        Class Name Must Be Defined In
        ClassMapping Dictionary
        """
        if not arg:
            Obj = storage.all()
            list_Classes = []
            for key, value in Obj.items():
                list_Classes.append(str(Obj[key]))
            print(list_Classes)
        else:
            if arg not in self.ClassMapping:
                print("** class doesn't exist **")
                return
            list_Classes = []
            Obj = storage.all()
            for key, value in Obj.items():
                ClassName, ClassId = key.split('.')
                if ClassName == arg:
                    list_Classes.append(str(Obj[key]))
            print(list_Classes)

    def do_update(self, arg):
        """
        update :    Updates an instance based on the class name and id
                    by adding or updating attribute
                    (save the change into the JSON file).

        Ex:
        $ update ClassName CLassId AttributeName AttributeValue

        Class Name Must Be Defined In
        ClassMapping Dictionary

        All other arguments should not be used
        Ex:
        $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        first_name "Betty"
        = $ update BaseModel 1234-1234-1234 email "aibnb@mail.com")
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        if args[0] not in self.ClassMapping:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        Obj = storage.all()
        if key not in Obj:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        if hasattr(Obj[key], args[2]):
            A_Type = type(getattr(Obj[key], args[2]))
            if A_Type == str:
                setattr(Obj[key], args[2], str(args[3]))
            elif A_Type == int:
                setattr(Obj[key], args[2], int(args[3]))
            elif A_Type == float:
                setattr(Obj[key], args[2], float(args[3]))
        else:
            setattr(Obj[key], args[2], args[3].strip('"'))
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
