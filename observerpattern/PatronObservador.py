from numerofibonacci.NumeroFibonacci import NumeroFibonacci

class Subscriber:
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print('{} recibio el mensaje "{}"'.format(self.name, message))


class Publisher:
        def __init__(self, events):
            self.subscribers = {event: dict()
                                 for event in events}

        def get_subscribers(self, event):
            return self.subscribers[event]

        def register(self, event, who, callback =None):
            if callback is None:
                callback = getattr(who, 'update')
            self.get_subscribers(event)[who] = callback

        def unregister(self, event, who):
            del self.get_subscribers(event)[who]

        def dispatch(self, event, message):
            for subscriber, callback in self.get_subscribers(event).items():
                callback(message)


pub = Publisher(['lunch', 'dinner'])
numero = NumeroFibonacci()
bob = Subscriber('bob')
alice = Subscriber('alice')
juan = Subscriber('juan')

pub.register("lunch", bob)
pub.register("dinner", alice)
pub.register("dinner", juan)
pub.register("lunch", juan)

numero.siguiente()
n = numero.guardarEnlista().pop()
pub.dispatch("lunch", n)
pub.dispatch("dinner", n)











