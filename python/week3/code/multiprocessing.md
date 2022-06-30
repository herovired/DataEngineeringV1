## Introduction

The **multiprocessing module** was defined in PEP 371 by Jesse Noller and Richard Oudkerk. The idea behind this module is to take advantage of multiple processors on a machine. This module is very similar to the **threading module**.  
Given that you use processes you can avoid the Global Interpreter Lock (GIL).
Let's start by using the *Process* class.

## Getting Started With Multiprocessing
The Process class is very similar to the threading module’s Thread class.

```python
import os
 
from multiprocessing import Process


def doubler(number):
    """
    A doubling function that can be used by a process
    """
    result = number * 2
    proc = os.getpid()
    print('{0} doubled to {1} by process id: {2}'.format(
        number, result, proc))

if __name__ == '__main__':
    numbers = [5, 10, 15, 20, 25]
    procs = []

    for index, number in enumerate(numbers):
        proc = Process(target=doubler, args=(number,))
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join() 
```

This snippet is straightforward. We first import the **os module** to be able to get the process id (pid). Then, we import Process to spawn processes. The doubler function we be called five times.
If you launch the script, you should get :

```
5 doubled to 10 by process id: 10468
10 doubled to 20 by process id: 10469
15 doubled to 30 by process id: 10470
20 doubled to 40 by process id: 10471
25 doubled to 50 by process id: 10472
```

current_process will let you have more understandable processes ids :

```python
import os

from multiprocessing import Process, current_process


def doubler(number):
    """
    A doubling function that can be used by a process
    """
    result = number * 2
    proc_name = current_process().name
    print('{0} doubled to {1} by: {2}'.format(
        number, result, proc_name))


if __name__ == '__main__':
    numbers = [5, 10, 15, 20, 25]
    procs = []
    proc = Process(target=doubler, args=(5,))
    
    for index, number in enumerate(numbers):
        proc = Process(target=doubler, args=(number,))
        procs.append(proc)
        proc.start()

    proc = Process(target=doubler, name='Test', args=(2,))
    proc.start()
    procs.append(proc)

    for proc in procs:
        proc.join()
```

And it returns :

```python
5 doubled to 10 by: Process-2
10 doubled to 20 by: Process-3
15 doubled to 30 by: Process-4
20 doubled to 40 by: Process-5
25 doubled to 50 by: Process-6
2 doubled to 4 by: Test 
```
As you can read in the script, the five first processes have a default value *Process-x* but for the sixth `name = 'Test'` allows users to define a custom name for their processes ! Keep in mind that when a custom name is defined, no number is added.

## Locks

The **multiprocessing module** can work with locks in a same fashion as the **threading module** does :

```python
from multiprocessing import Process, Lock


def printer(item, lock):
    """
    Prints out the item that was passed in
    """
    lock.acquire()
    try:
        print(item)
    finally:
        lock.release()

if __name__ == '__main__':
    lock = Lock()
    items = ['tango', 'foxtrot', 10]
    for item in items:
        p = Process(target=printer, args=(item, lock))
        p.start()
```
The above script creates a printing function that prints whatever you pass as a parameter. Processes will want to use stdout to print the message. To prevent the code to write their respective message in the same time, we use a Lock object.
Because we’re using locks, the next process in line will wait for the lock to release before it can continue. 


## The Pool Class
The Pool class is used to represent a pool of worker processes. It has methods which can allow you to offload tasks to the worker processes. Let’s look at a really simple example :

```python
from multiprocessing import Pool
 

def doubler(number):
    return number * 2

if __name__ == '__main__':
    numbers = [5, 10, 20]
    pool = Pool(processes=3)
    print(pool.map(doubler, numbers))
```

Basically what’s happening here is that we create an instance of Pool and tell it to create three worker processes. Then we use the map method to map a function and an iterable to each process. Finally we print the result, which in this case is actually a list: `[10, 20, 40]``.

You can also get the result of your process in a pool by using the apply_async method:

```python
from multiprocessing import Pool
 
 
def doubler(number):
    return number * 2

if __name__ == '__main__':
    pool = Pool(processes=3)
    result = pool.apply_async(doubler, (25,))
    print(result.get(timeout=1))
```

What this allows us to do is actually ask for the result of the process. That is what the get function is all about. It tries to get our result. You will note that we also have a timeout set just in case something happened to the function we were calling. We don’t want it to block indefinitely after all.