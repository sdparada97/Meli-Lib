from collections import deque

class Buffer:
    """A buffer that handles insertion and consumption of items.

    Has 2 possible policies: FIFO (First In First Out) and LIFO (Last In
    First Out).

    Example:
        buffer = Buffer('FIFO')
        buffer.insert(1)
        item = buffer.extract()
        item == 1

    """
    def __init__(self, policy):
        policy = policy.upper()
        if policy not in ['FIFO', 'LIFO']:
            raise ValueError()
        self._policy = policy
        self.lista_fifo_lifo = deque([])

    def insert(self, item):
        if self._policy == 'FIFO':
            # FILAS
            queue = self.lista_fifo_lifo
            queue.append(item)
        else:  
            # PILAS
            queue = self.lista_fifo_lifo
            queue.append(item)
        
    def extract(self):
            if self._policy == 'FIFO':
                # FILAS
                queue = self.lista_fifo_lifo
                return queue.popleft()
            else:  
                # PILAS
                queue = self.lista_fifo_lifo
                return queue.pop()


if __name__ == '__main__':
    buffer = Buffer('LIFO')
    if len(buffer.lista_fifo_lifo) >= 1:
        item = buffer.extract()
