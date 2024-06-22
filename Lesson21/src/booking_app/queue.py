# class Queue:
#     FIFO = "FIFO"
#     LIFO = "LIFO"
#     ACCEPTED_STRATEGIES = [FIFO, LIFO]
#
#     def __init__(self, strategy):
#         if strategy not in self.ACCEPTED_STRATEGIES:
#             raise TypeError
#         self.strategy = strategy
#         self.storage = []
#
#     def add(self, value):
#         if self.strategy == self.FIFO:
#             self.storage.append(value)
#
#     def pop(self):
#         if self.strategy == self.FIFO:
#             value = self.storage.pop()
#         return value

#     def get_storage(self):
#         return self.storage
#
#
# q = Queue(strategy="FIFO")
# q.add(4)
# print(type(q.get_storage()[0]))
from .models import Queue


class UniqQueue:

    FIFO = "FIFO"
    LIFO = "LIFO"
    ACCEPTED_STRATEGIES = [FIFO, LIFO]

    def __init__(self, strategy):
        self.storage = Queue()
        if strategy not in self.ACCEPTED_STRATEGIES:
            raise TypeError
        self.strategy = strategy

    def add(self, value):
        if value not in Queue.objects.all():
            Queue.objects.create(value=value)
        else:
            return f'Элемент {value} уже в очереди'

    def get_queue(self):
        return self.storage

    def len(self):
        return len(Queue.objects.count)

    def pop(self):
        if self.strategy == self.LIFO:
            if self.storage:
                value = Queue.objects.order_by("id").last()
                value = value.value
                self.storage.delete(value)
                return value.value
            return None

# q = UniqQueue(strategy="FIFO")
# print(q.len())

