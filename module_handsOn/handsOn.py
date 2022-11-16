
"""This is the module docstring.

    :Note that -> docstring must be on the first line of each module"""

__all__ = ["say_hello" , "Voala"] # as a contract AKA nno need to provide all implementations

def say_hello():
    """This is a spesific function docstring."""
    print("Hello!")

"""Sphinx
It's a tool to generate HTML based documentation
 for Python projects based on docstrings. 
"""
def hello(name, language="en"):
 """Say hello to a person.
 :param name: the name of the person
 :type name: str
 :param language: the language in which the person should be greeted
 :type language: str GoalKicker.com – Python® Notes for Professionals 40
 :return: a number
 :rtyp: int
 """
 print(greeting[language]+" "+name)
 return 4