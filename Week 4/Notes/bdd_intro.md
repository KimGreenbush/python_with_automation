# Introduction to BDD
## BDD with Cucumber Module: Defining Behavior-Driven Development
This file contains an overview of **behavior-driven development**. It includes information about what behavior-driven development is, the benefits of taking a behavior-driven approach to development, and how to implement behavior-driven development. It also provides a high-level overview of Cucumber.

### Resources
- [Cucumber School](https://school.cucumber.io/collections)
- [Cucumber: Behavior-Driven Development](https://cucumber.io/docs/bdd/)
- [Jbehave: A Definition of BDD](https://jbehave.org/reference/stable/concepts.html)

### What Is Behavior-Driven Development (BDD)?
**Behavior-driven development (BDD**) is an approach to software development in which developers implement the features of an application ["by describing it from the point of view of its stakeholders"](https://jbehave.org/reference/stable/concepts.html). The assumption is that the stakeholders lack technical knowledge pertaining to software development while software developers lack the business knowledge the stakeholders possess. Behavior-driven development allows both parties to bridge this gap.

It should be noted that behavior-driven development is an extension of **test-driven development**. The former emphasizes the same principles as the latter, though it takes the concept of TDD further by encouraging more effective communication during the development process so that all involved parties can develop a shared understanding of the application's behavior.

BDD takes the following steps to develop a feature:
1) Business analysts and stakeholders collaborate with developers and testers to document expected behaviors in a plain language (English-like) syntax
2) Developers write tests to validate the behaviors described
3) Developers write the code to pass the test

To this end, many BDD frameworks have established standard languages for describing a system's behavior. These languages have their own syntaxes and keywords which create shared meaning for developers and stakeholders alike. Though one BDD framework might differ from another, some common **BDD keywords** include:

- **Scenario**: a representation of a concrete example of the behavior of the system that is in development or under test.
- **Step**: scenarios are composed of steps. There are three types of steps: *given*, *when*, and *then*:
  - **Given**: specifies a precondition to an event that will or should or occur during a scenario.
  - **When**: specifies the occurrence of the event itself.
  - **Then**: specifies the expected outcome of the event that has occurred.

### Benefits of Behavior-Driven Development
There are several benefits to practicing behavior-driven development, including the following:
1) BDD encourages the development and maintenance of system documentation that is understandable to both technical and non-technical parties. This documentation guides the software development process and makes it easy for development teams to make modifications to the system over time. This documentation is often referred to as **living documentation**.
2) BDD emphasizes effective communication between even the most technical members of a project team and the least technical members. This effective communication can greatly improve the quality of the finished product and the speed at which the quality product is delivered as both parties have come to an understanding of the required behaviors for the system in development.
3) Not only does it aid in the development of system itself, but it also aids in the testing of the system as the testing team can use the provided scenarios to generate test cases.

### Implementing Behavior-Driven Development With Cucumber
Behavior-driven development has become such an integral part of the agile development process that there are tools which are dedicated BDD tools marketed to developers. One such tool is **Cucumber**. We'll be using this tool for demonstrations of BDD within this module, so you'll quickly become familiar with its inner workings.

Implementing behavior-driven development using Cucumber is simple as Cucumber follows a standard BDD formula. It defines its own high-level language called **Gherkin** which allows developers to create **feature files**. The general workflow for implementing BDD using Cucumber is as follows:
1) A developer must first write their feature files in Gherkin. A feature file defines several scenarios and steps in order to define a system's behavior at a high level.
2) After the developer has finished drafting the feature file, they should generate their glue code by running the feature file. We'll talk more about glue code in the future, but for now you need only know that this glue code consists of potential test methods that are associated with a scenario's steps. We say "potential" test methods because the developer may or may not choose to implement those suggested test methods.
3) Once the developer has generated the glue code and written the tests, they should choose a test runner for running the glue code.