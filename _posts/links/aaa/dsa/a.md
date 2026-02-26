CLASS 

A Class is a blueprint for the object. We can think of class as a sketch of a parrot with labels. It contains all the details about the name, colours, size etc.




An object is an instance of a class.    



1. Class
A Class is a blueprint for the object.
A class is a logical template that defines the shared attributes (data) and behaviors (methods) that all objects created from that class will have. The example provided shows the basic syntax for defining an empty class in Python using the class keyword:
Python

class Parrot:
    pass

The pass statement is a placeholder that does nothing and is used when a statement is syntactically required but no code needs to be executed.


2. OBJECT
Answer: An object is an instantiation of a class, which is a fundamental concept in object-oriented programming.
When a class is defined, it merely provides a blueprint or description for an object, and no memory or storage is allocated at that point. Memory is only allocated when an object (instance) of that class is actually created.
The example provided illustrates a Python class named Vehicle and the creation of an object from it:
Class Vehicle: defines the blueprint.
Vehicle_object = Vehicle ('Honda', 'truck') creates an instance (object) of the Vehicle class, which is a specific object with brand 'Honda' and type 'truck'.
3. INHERITANCE
Answer: Inheritance is a mechanism in object-oriented programming that allows a new class to use the details and properties of an existing class without modifying the original.
This promotes code reusability and establishes a hierarchical relationship between classes, where the new class (child/derived class) inherits attributes and methods from the existing class (parent/base class).

# OOPS in PYTHON

CLASS: 
A Class is a blueprint for the object. We can think of class as a sketch of a parrot with labels. It contains all the detalls about the name, colours, size etc.
Example:-
```py
class parrot:
    pass
```
`class` Keyword to define an empty class parrot.