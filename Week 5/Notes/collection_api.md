# Collections Framework
The Collections framework in Java is a set of classes and interfaces that implement commonly used data structures. A collection is a single object which acts as a container for other objects. The Collections API is organized in a class hierarchy.

The important interfaces in the Collections API are:
- `Iterable` - guarantees the collection can be **iterated over**
- `List` - an **ordered** collection
- `Set` - a collection **does not contain duplicates**
- `Queue` - a collection that operates on a **first-in-first-out (FIFO)** basis
- `Map` - contains **key/value pairs**. Does not extend Iterable.

## Collections Class
The [Collections](https://docs.oracle.com/javase/8/docs/api/java/util/Collections.html) class - not to be confused with the Collection interface - defines many `static` helper methods which operate on any given collection. Use this class for help with sorting, searching, reversing, or performing other operations on collections.

## List Interface
A `List` is a collection that is ordered and preserves the order in which elements are inserted into the list. Contrary to sets, duplicate entries are allowed. Also, elements are accessed by their index, which begins with 0 for the first element in the list.

## Vector
`Vector` is an older class which implements `List` - it is essentially a **thread-safe implementation of an `ArrayList`.**

## Stack
`Stack` is an older implementation of the **stack data structure (last-in-first-out, or LIFO**). Generally you should use an `ArrayDeque` for implementing a stack.

## Set Interface
Set is an interface which defines a data structure which:
- is **NOT** index driven
- only allows **unique** elements
- generally **DOES NOT preserve the order** in which elements were inserted

## Queue Interface
A Queue is a data structure used when elements should be added and removed in a specific order. Unless specified, **elements are ordered FIFO (first-in-first-out).** Some useful methods declared are:
- `offer()`
- `peek()`
- `poll()`

## Map Interface
**Map does not implement the Collection interface**, however it is considered to be part of the Collections framework. It is used to identify a value by a key, and each entry in a map is a key-value pair. Because it does not implement Iterable, **Maps cannot be iterated over directly**. Instead, one must either:
- use the `entrySet()` method to iterate over the set of `Map.Entry`
- use the `keySet()` method to iterate over the set of keys
- use the `values()` method to return a `Collection` of values which can then be iterated over

## HashMap
`HashMap` is a Map which:
- Stores elements in key-value pairs
- Insertion/Retrieval of element by key is fast
- Tradeoff is that it does not maintain the order of insertion
- Permits one null key and null values

## TreeMap
`TreeMap` is a Map whose:
- Keys are stored in a Sorted Tree structure
- Main benefit is that keys are always in a sorted order
- Insertion/Retrieval are slow
- Cannot contain null keys as null cannot be compared for sorting

## HashTable
`HashTable` is an older, thread-safe implementation of a `HashMap`. **It does not allow null keys or null values.**

## ArrayList
An `ArrayList` is a concrete class which implements `List`. It is a data structure which contains an array within it, but **can resize dynamically**. Once it reaches maximum capacity, an `ArrayList` will increase its size by 50% by copying its elements to a new (internal) array. Traversal is fast (constant time) because elements can be randomly accessed via index, just like an array. Insertion or removal of elements is slow, however (linear time, since there is a risk of having to resize the underlying array).

## LinkedList
A `LinkedList` implements both the `List` and `Queue` interfaces, so it has all methods in both interfaces. The data structure is **composed of nodes internally**, each with a reference to the previous node and the next node - i.e. a doubly-linked list. Because of this structure, **insertion or removal of elements is fast (no risk to resize, just change the nearest references), but traversal is slow for an arbitrary index.**