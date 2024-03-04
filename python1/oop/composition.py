#In simple terms, composition is like building something 
#by putting different parts together. It's a way of 
#organizing and structuring things, 
#especially when one thing is made up of several smaller things.

class Engine:
    def __init__(self, pistons, crankshaft, valves):
        self.pistons = pistons
        self.crankshaft = crankshaft
        self.valves = valves

    def start(self):
        return "Engine started"

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        return f"Car started. {self.engine.start()}"

# Creating engine components
pistons = "Four Pistons"
crankshaft = "Crankshaft"
valves = "Valves"

# Creating an engine using the components
car_engine = Engine(pistons, crankshaft, valves)

# Creating a car with the engine
my_car = Car(car_engine)

# Starting the car
print(my_car.start())


#In this example, the Engine class represents 
#the engine components, and the Car class is 
#composed of an instance of the Engine class.
#The Car class has a method start that calls the start method 
#of the Engine class, demonstrating how composition allows one class 
#to use the functionality of another. 
#This way, we can encapsulate the details of the engine 
#within the Engine class and build a more complex 
#object (Car) by composing it with simpler objects (Engine).

#Composition is the act of collecting several objects together 
#to create a new one.
#Composition is usually a good choice when one object 
#is part of another object.

#Composition in object-oriented programming typically 
#represents a "has-a" relationship. This means that one 
#class has another class as a part of its structure. 
#The key idea is that a class is composed of one or more 
#objects of other classes. This is in contrast 
#to an "is-a" relationship, which is associated with inheritance.

class Player:
    def __init__(self, name):
        self.name = name

class ChessSet:
    def __init__(self):
        # Assume a basic chess set with a board and pieces
        self.board = ChessBoard()
        self.pieces = ChessPieces()

class ChessBoard:
    def __init__(self):
        # Implementation of the chess board
        self.positions = [[None for _ in range(8)] for _ in range(8)]

class ChessPieces:
    def __init__(self):
        # Implementation of chess pieces
        self.white_pieces = [Piece("Pawn"), Piece("Rook"), Piece("Knight"), ...]
        self.black_pieces = [Piece("Pawn"), Piece("Rook"), Piece("Knight"), ...]

class Piece:
    def __init__(self, type):
        self.type = type
