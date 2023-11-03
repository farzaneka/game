## Medrick Game Studio coding assignment

### What is the concurrency and who do you handle it in a system with a high volume of concurrent users?

Concurrency in programming refers to the ability of a program to execute multiple tasks simultaneously. It allows for tasks to be executed in parallel, improving performance and resource utilization. Concurrency can be achieved through various techniques such as multithreading, multiprocessing, or distributed computing. Synchronization mechanisms are used to coordinate the access to shared resources and manage potential conflicts. However, concurrency also introduces challenges such as race conditions and deadlocks that need to be carefully handled.

There are a number of ways to handle concurrency in a system with high-volume concurrent users. Some of the most common approaches include:

Load balancing: This involves distributing traffic across multiple servers or instances of an application. This can be done using a hardware load balancer or a software load balancer.
Caching: This involves storing frequently accessed data in memory so that it can be quickly retrieved without having to access the database or other backend systems.
Asynchronous programming: This involves using techniques such as callbacks and promises to allow multiple tasks to execute simultaneously without blocking each other.
Database design: The database schema can be designed to minimize contention for shared resources and improve performance for concurrent reads and writes.
Microservices architecture: This involves breaking down the application into a number of smaller, independent services. This can make the application more scalable and resilient to concurrency issues.
In addition to these general approaches, there are a number of specific techniques that can be used to handle concurrency in different parts of a system. For example, a database server may use locks to prevent concurrenat updates to the same data. A web server may use a thread pool to handle multiple concurrent requests.

The best approach to handling concurrency will depend on the specific needs of the system. However, the general principles outlined above can be applied to any system that needs to handle a high volume of concurrent users.

By following these tips, we can design and build systems that can handle high-volume concurrent users without sacrificing performance or reliability.


### ﻿﻿﻿What is your biggest nightmare when designing an online system?

As a programmer, the biggest nightmares when designing an online system are performance and concurrency. To avoid these nightmares, I need to carefully choose data structures and algorithms, design a lock-free system, and handle errors gracefully.



