# python-helpers
This repository contains handy shortcuts to make your day-to-day coding easier.

Below is the list of helpers available:;

1. Dictionary Formater: Python doesn't support formatting of dictionary like strings. To get that support in python, package "dict_format" can be used. Its usage:

from dict_format import dict_format

person = {
        '{0}': {
            "name": "{0}",
            "nick_name": "{1}",
            "age": {2},
            "hobbies": {3},
            "family_details": {
                "siblings": {4},
            }
        }
}

name = 'Ram'
nick_name = 'Ramu'
age = 21
hobbies = ['cooking', 'reading books', 'travelling']
sibblings = 2
dict_format.format(person, [name, nick_name, str(age), str(hobbies), str(sibblings)])
                                                    
