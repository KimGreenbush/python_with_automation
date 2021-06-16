#Introduction to Java

Java is a **high-level, compiled, strongly typed object-oriended programming (OOP)** language. The advantages of Java are many: it is **platform independent**, has a **C-language inspired syntax**, provides **automatic memory management**, has an **extensive built-in runtime library**, is supported by the Oracle corporation, and has a rich **open source community**.

When we say Java is object-oriented, we mean that it has the constructs of **classes** and **objects** built into the language. It also allows us to use various principles of object-oriented programming, which are covered in a separate module. An object in code can represent a real-world entity, or a conceptual entity. Classes are the *blueprints* for how to create objects that contain a certain **state** - which is represented by *fields* (variables) - and **behavior** - which is defined via *methods*. Objects are instances of class definitions. However, Java is not 100% object-oriented because it still has primitive values (or just: primitives), which are defined below:

```
Primitive type      	Size                                  	Description
boolean        not specified (JVM-dep)	represents true and false
byte                     	8-bit                      	numerical, integral value
short                     	16-bit	             signed numerical, integral value
char	                   16-bit            unsigned numerical, Unicode character
int	                          32-bit                   	numerical, integral value
long	                   64-bit                    numerical, integral value
float                    	32-bit                        	floating point value
double                	64-bit                      	floating point value
```

## JVM, JRE, JDK
When we say Java is **platform independent**, we mean that Java programs are not constrained to a single operating system - Java code can be run on many different systems. Another way of saying this is that with Java, we can **write once, run anywhere (WORA)**. Portability is possible because Java code is compiled to **bytecode** and runs on a **JVM - or Java Virtual Machine**. The JVM is specific to the operating system - there is a JVM for Windows, one for Mac, one for Linux, etc. The JVM reads the compiled Java bytecode and translates it to machine code to be executed on the given system. Actually, in order to run Java code, you also need a **JRE - Java Runtime Environment**, which contains all the runtime libraries that your code will be calling and using. The JRE contains the JVM within it, so if you want to run a Java program, all you need to install is the JRE.

But how do we actually compile the Java code that we write down to bytecode that the JVM will understand? For that, you need a **JDK - Java Development Kit**, which provides developer tools like a compiler, debugger, documentation tools (`javadoc`), and other command-line utilities. The JDK also has a JRE inside of it, so if you install a JDK you can compile your Java code as well as execute it.

So, to recap - the JDK contains tools for Java development as well as a JRE, which contains the built-in Java libraries as well as a JVM, which actually executes your Java bytecode and runs it on the specific operating system it is installed upon.