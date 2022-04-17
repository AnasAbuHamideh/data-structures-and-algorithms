# linked-list-insertions
<!-- Description of the challenge -->
Write the following methods for the Linked List class:
append
arguments: new value
adds a new node with the given value to the end of the list
insert before
arguments: value, new value
adds a new node with the given new value immediately before the first node that has the value specified
insert after
arguments: value, new value
adds a new node with the given new value immediately after the first node that has the value specified


## Whiteboard Process
<!-- Embedded whiteboard image -->
![alt](./Insertions.jpg)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Time Complexity: O(n)
Space Complexity : O(n)


## Solution API
<!-- Show how to run your code, and examples of it in action -->
Create a Node_class that has properties for the value stored and a pointer to the next node.
Create a Linked List that has include all the below properties:
define append() method that takes in a value and adds it to the end of the list
define insert_before() method that takes 2 arguments value and new value & adds a new node with the given new value immediately before the first node that has the value specified.
define insert_after() method that takes 2 arguments value and new value and arguments: value, new value adds a new node with the given new value immediately after the first node that has the value specified.