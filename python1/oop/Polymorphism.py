#Polymorphism is a concept in object-oriented 
#programming that allows objects of different types 
#to be treated as objects of a common type.
#The word "polymorphism" means "many forms", 
#Polymorphism is often expressed through two related principles: 
#method overloading and method overriding.
class AudioFile:
    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise ValueError("Invalid file format")
        self.filename = filename

class MP3File(AudioFile):
    ext = "mp3"
    def play(self):
        print(f"Playing {self.filename} as MP3")

class WavFile(AudioFile):
    ext = "wav"
    def play(self):
        print(f"Playing {self.filename} as WAV")

class FlacFile:
    def __init__(self, filename):
        if not filename.endswith(".flac"):
            raise ValueError("Invalid file format")
        self.filename = filename

    def play(self):
        print(f"Playing {self.filename} as FLAC")

# Function that can play any audio file
def play_audio(audio_file):
    audio_file.play()

# Usage with duck typing
mp3 = MP3File("song.mp3")
wav = WavFile("music.wav")
flac = FlacFile("sound.flac")

# Using the play_audio function with different types
play_audio(mp3)  # Output: Playing song.mp3 as MP3
play_audio(wav)  # Output: Playing music.wav as WAV
play_audio(flac) # Output: Playing sound.flac as FLAC


# Duck Typing:

#     Principle: "If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck."
#     In Python, the type or class of an object is less important than the methods and properties it possesses.
#     Instead of checking the type of an object, code should often rely on the presence of specific methods or attributes.
#     This promotes a more flexible and implicit interface, allowing different objects to be used interchangeably based on their behavior.

# EAFP (Easier to Ask for Forgiveness than Permission):

#     Principle: Try to perform an operation and deal with any exceptions if it fails, rather than checking beforehand whether the operation is possible.
#     This approach assumes that it's more common for operations to succeed than to fail, making it more "Pythonic" to ask for forgiveness (handle exceptions) rather than permission (check conditions).


# # Non-Pythonic (LBYL - Look Before You Leap) approach
# if key in my_dict:
#     value = my_dict[key]
# else:
#     value = default_value

# # Pythonic (EAFP) approach
# try:
#     value = my_dict[key]
# except KeyError:
#     value = default_value


class Duck:

    def quack(self):
        print('Quack, quack')

    def fly(self):
        print('Flap, Flap!')


class Person:

    def quack(self):
        print("I'm Quacking Like a Duck!")

    def fly(self):
        print("I'm Flapping my Arms!")


def quack_and_fly(thing):
    try:
        thing.quack()
        thing.fly()
        thing.bark()
    except AttributeError as e:
        print(e)

d = Duck()
P = Person()
quack_and_fly(d)
quack_and_fly(P)



#The term "duck typing" comes from the saying, 
# "If it looks like a duck, swims like a duck, 
# and quacks like a duck, then it probably is a duck." 
# In Python, this means that if an object supports 
# the methods or attributes expected by a piece of code, 
# it can be used in that context, even if it doesn't 
# explicitly inherit from a specific class or type.

#In traditional programming languages like J
# ava or C++, polymorphism is often achieved 
# through explicit class inheritance and method overriding. 
# This is known as "classical" or "static" polymorphism, 
# where the type of an object is determined at compile-time.

# In Python, however, polymorphism is often achieved through a concept called "duck typing," which is more dynamic and doesn't rely on explicit class hierarchies or interfaces. Duck typing is a form of "runtime" or "dynamic" polymorphism.

# Here's a simple explanation of why traditional polymorphism may not match Python's approach:

#     Classical Polymorphism (Traditional):
#         In classical polymorphism, you create a class hierarchy where subclasses inherit from a common base class.
#         You define methods in the base class, and subclasses override these methods to provide their own implementations.
#         The type of an object is determined by its class, and the compiler checks method calls at compile-time.

#     Duck Typing (Python):
#         In Python, there's a saying: "If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck." This is the essence of duck typing.
#         Instead of explicitly defining interfaces or base classes, Python checks for the existence of specific methods or attributes at runtime.
#         If an object has the necessary methods, it can be used in a particular context, regardless of its actual class.

# Why They Differ:

#     Flexibility: Duck typing in Python allows for more flexibility. You don't need to plan a strict class hierarchy; you just focus on the behavior you need.
#     Dynamic Nature: Python is dynamically typed, and types can change at runtime. This dynamic nature aligns well with the philosophy of duck typing.
#     No Formal Interfaces: Python doesn't require formal interfaces or explicit inheritance for polymorphism. It's more about what an object can do than what it is.

# Example:
# Consider a function expecting an object with a quack method:

#def make_sound(animal):
    #animal.quack()

#    n classical polymorphism, you might require all animals to inherit from a common Animal class with a quack method.
#     In Python's duck typing, any object with a quack method can be passed to make_sound, regardless of its class.

# In summary, Python's polymorphism, based on duck typing, is more dynamic and doesn't rely on explicit class hierarchies. It's a key feature of the language that promotes flexibility and simplicity in code design.

