from subpackage import module

"""
we don't need to relativly import subpackage, because executable_directory has been add to import path
by calling python executable_directory
"""
module.say_hi()
print('executing __main__.py with name {}'.format(__name__))
