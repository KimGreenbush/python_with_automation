# Creational: Singleton
## Singleton Pattern
A Singleton is a design pattern which allows the **creation of an object in memory only once in an application and can be shared across multiple classes**. It can be useful for services in an application, or other resources like a connection or thread pool.

To make a class into a Singleton, use:
1) `private static` variable of the class' type
2) `private` constructor - to prevent arbitrary object creation
3) `public static getInstance()` method, which will either instantiate the object or return the instance in memory

```java
    public class Singleton {
        // Private static variable of the class' type
        private static Singleton instance;

        // Private Constructor
        private Singleton() {}

        // Public static getInstance method
        public static Singleton getInstance() {
            if (instance == null)
                instance = new Singleton();
            return instance;
        }
    }
```