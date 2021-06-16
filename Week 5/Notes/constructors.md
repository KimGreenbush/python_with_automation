# Constructors
When we use the `new` keyword in order to create an object, the JVM is invoking a special class member called a **constructor**. A constructor declares how an object is to be instantiated and initialized from the class "blueprint". A constructor is declared like a method, except **its method signature does not contain a return type, and a constructor always has the same name as the class**. The new object returned from the constructor is always of the class in which the constructor is declared. A simple example is shown below:

```java
public class ConstructorExample {

  int myNumber;

  public static void main(String[] args) {
    ConstructorExample ce = new ConstructorExample(3); // a
	System.out.println(ce.myNumber); // b
  }

  public ConstructorExample(int myNumber) { // c
    this.myNumber = myNumber; // d
  }
}
```

## `this` keyword
When this program is run, it will print `3`. How does this happen? The constructor is defined on line "c" with one input parameter. Note that the constructor does not have a return type. On line "d", the **parameter** `myNumber` is assigned to the **instance variable** `myNumber` via the `this` keyword. `this` refers to the object which is being instantiated - it is used to initialize instance variables, or - to call other constructors (this is called constructor chaining).

When the program above is run, the `main` method is executed. On line "a", a new `ConstructorExample` object is created and assigned to the variable `ce`. The constructor is invoked with the `new` keyword and the int `3` is passed as the argument. This assigns the value 3 to the instance variable `myNumber` on the object returned, as explained above. Finally, the instance variable is printed out and the program finishes execution.

## `super` keyword
There is another keyword important for constructors - the `super` keyword, which references the** "super", or parent, class**. When invoked as a method (`super()`), the parent class constructor will be called. A `super()` call (or a `this()` call) **must** be the first line of any constructor. If not explicitly provided, the compiler will inject it on the first line.

## Default constructor
Earlier, in our `Example` class, we saw a constructor with no arguments used with the `new` keyword. But we didn't define a constructor, so how is this possible? It turns out the compiler will inject a "default" constructor for us if we are too lazy to define one ourselves. The "default" constructor takes no arguments and simply calls `super()` (see above) - sometimes it is referred to as the "default, no-args" constructor. However, be warned that if we define our own constructor(s) in the class, we will **not** receive a default constructor from the compiler.

Thus, the simple class:

```java
public class MySimpleClass {}
has a default no-args constructor that can be called:

MySimpleClass someVariable = new MySimpleClass();
```

# Methods and Parameters
A method is a block of code which only runs when it is called. You can pass data, known as parameters, into a method. **A method must be declared within a class**. It is defined with the name of the method, followed by parentheses ().

```java
public class MyClass {
  public static void myMethod() {
    // code to be executed
  }
}
```

Parameters are specified after the method name, inside the parentheses. You can add as many parameters as you want, just separate them with a comma.

```java
public class MyClass {
  public static void myMethod(String name) {
    System.out.println(name);
  }

  public static void main(String[] args) {
    myMethod("Liam");
    myMethod("Jenny");
  }
}
//Output:
//Liam
//Jenny
```