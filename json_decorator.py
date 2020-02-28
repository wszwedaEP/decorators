'Your task is to write a decorator (for a class) that loads a given JSON file object and makes each key-value pair an attribute of the given class.'
'Take a look on descriptors: https://eev.ee/blog/2012/05/23/python-faq-descriptors/'
'https://www.codewars.com/kata/55b0fb65e1227b17d60000dc/train/python'
'https://gist.github.com/Zearin/2f40b7b9cfc51132851a' # <--- this one is absolutely great
'https://stackoverflow.com/questions/9663562/what-is-the-difference-between-init-and-call'

'So, for all intents and purposes, super is a shortcut to access a base class without having to know its type or name.'

'''How it should be used:
@jsonattr("/tmp/myClass.json")
class MyClass:
    pass
'''

json = {
  "foo": "bar",
  "an_int": 5,
  "this_kata_is_awesome": True}

filepath = "/tmp/myClass.json"

'''
def multiply_return_message_outer(how_many_times):
    def multiply_return_message(returning_func):
        def wrapper(*args, **kwargs):
            @functools.wraps(returning_func)    #   <----    This guy preserves returning_func.__name__
            # Otherwise calling return_msg.__name__  after decorating it would return 'wrapper' instead of 'returning_func'
            return how_many_times * returning_func(*args,**kwargs)
        return wrapper
    return multiply_return_message

@multiply_return_message_outer(how_many_times=3)
def return_msg(msg):
    return msg
    
# Since when you are calling the function returned by the decorator, you are
# calling the wrapper, passing arguments to the wrapper will let it pass them to 
# the decorated function

'''
'''
class new_class():
  def __init__(self, number):
    self.multi = int(number) * 2
    self.str = str(number)

a = new_class(2)
a.__dict__
>>>{'multi': 4, 'str': '2'}
'''

'''My logic below. (solution is invalid). I was insisting that decorator would have to return class. 
However it's unnecessary, cause setattr happens on the fly. 
'''
def jsonattr_bad_solution(filepath):
    def outer_class_wrapper(ClassBeingDecorated):
        def class_wrapper(*args):
            data = {filepath: json}
            for key, val in data[filepath].items():
                setattr(ClassBeingDecorated, key, val)
            return ClassBeingDecorated
        return class_wrapper
    return outer_class_wrapper

'''Proper logic below'''
def jsonattr(filepath):
    def class_wrapper(ClassBeingDecorated):
        data = {filepath: json}
        for key, val in data[filepath].items():
            setattr(ClassBeingDecorated, key, val)
        return ClassBeingDecorated
    return class_wrapper

@jsonattr(filepath)
class MyClass:
    def __init__(self, name):
        self.my_name = name
    def shout_sth(self, sth):
        print(sth.upper())


#tests:
instance=MyClass('Wojtasek')
int_unbound_to_any_instance = MyClass.an_int
print(int_unbound_to_any_instance)
instance.shout_sth('hello')

