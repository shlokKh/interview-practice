from pyllist import sllist

class Animal:
    def __init__(self, name):
        self.name = name
    
    def search(obj):
        if isinstance(obj, Dog):
            return "Dog"
        elif isinstance(obj, Cat):
            return "Cat"
        else:
            return "unknown"

class Dog(Animal):
    def __init__(self, name, breed):
        self.breed = breed
        Animal.__init__(self, name)

class Cat(Animal):
    def __init__(self, name, breed):
        self.breed = breed
        Animal.__init__(self, name)

class AnimalShelter:
    def __init__(self):
        self.cat = Queue()
        self.dog = Queue()
        self.count = 0
    
    def enqueue(self, x):
        if x.search() == "Dog":
            self.dog.enqueue((x, self.count))
        if x.search() == "Cat":
            self.cat.enqueue((x, self.count))

        self.count += 1

    def dequeue_dog(self):
        self.count -= 1
        d,_ = self.dog.dequeue()
        return d
    
    def dequeue_cat(self):
        self.count -= 1
        c,_ = self.cat.dequeue()
        return c
    
    def dequeue_any(self):
        _, dog_age = self.dog.peek()
        _, cat_age = self.cat.peek()

        if dog_age > cat_age:
            return self.dequeue_cat()
        return self.dequeue_dog()



class Queue:
    def __init__(self):
        self.queue = sllist()
    
    def enqueue(self, x):
        self.queue.append(x)
    
    def dequeue(self):
        return self.queue.popleft()
    
    def peek(self):
        return self.queue.first()


Skipper = Dog("Skipper","Maltese")
Garfield = Cat("Garfield", "Yeet")
shelter = AnimalShelter()

shelter.enqueue(Skipper)
shelter.enqueue(Garfield)

print(shelter.dequeue_any())