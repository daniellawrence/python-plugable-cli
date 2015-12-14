#!/usr/bin/env python
# from functools import wraps


class ClickCommander(object):

    instances = {}

    def __new__(cls, group, *args, **kwargs):

        instance = cls.instances.get(group)
        if not instance:
            instance = super(ClickCommander, cls).__new__(cls, *args, **kwargs)
        cls.instances[group] = instance
        return instance

    def __init__(self, group):
        self.group = group
        self.commands = {}

    def add_command(self, command, command_name=None, command_map={}):
        if not command_name:
            command_name = command.__name__
        command_name = command_name.replace('_', '-')
        print "{0}: {1} > {2}".format(self.group, command_name, command.__name__)
        self.commands[command_name] = {
            'command': command,
            'docstring': command.__doc__,
            'command_map': command_map
        }

    def execute(self, command_name, *args, **kwargs):
        command_dict = self.commands.get(command_name)
        command = command_dict['command']
        command_map = command_dict['command_map'].get(self.group).copy()
        command_map.update(kwargs)
        results = command(*args, **command_map)
        return results

    def register(self, command_name=None, command_map=None):
        def x(f):
            self.add_command(f, command_name, command_map)
            def wrapper(*args, **kwargs):
                return f(*args, **command_map)
            return wrapper
        return x
  
    def __str__(self):
        return "<ClickCommander: {0} {1}>".format(self.group, len(self.commands))

    def __repr__(self):
        return "{0}".format(self)

    def get_groups(self, group_name):
        if group_name:
            return ClickCommander.instances.get(group_name)
        return ClickCommanfer.instances
