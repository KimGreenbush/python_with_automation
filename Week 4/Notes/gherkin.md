# Gherkin
## Cucumber Module: Using Gherkin With Feature Files
>This file contains information about how to use Gherkin to write Cucumber feature files. It also provides some details about Gherkin keywords developers have at their disposal for creating rich scenarios.

### Resources
- [Cucumber School](https://school.cucumber.io/collections)
- [Gherkin](https://cucumber.io/docs/guides/overview/#what-is-gherkin)

### What Is Gherkin?
Cucumber allows developers to create **feature files** as a first step in implementing behavior-driven development. A feature file, which uses the `.feature` extension, is a file that contains several scenarios and steps associated with those scenarios. The scenarios within this file are ideally associated with the same feature, though this association is not a requirement.

Feature files are written in plain text in a special language called **Gherkin**. This language is specific to Cucumber, though it is not unlike the languages used in combination with other BDD tools. Gherkin is simple and built on top of standard BDD keywords.

The language has its own syntax and grammar rules. It even has support for multiple languages as the Cucumber grammar has been translated into over 70 languages. These rules make plain text structured so that the Cucumber tool can understand the scenarios written within the file in order to produce the appropriate glue code.

Perhaps the most notable feature of Gherkin is its special BDD keywords. Some of these keywords are standard BDD keywords while others are unique to Cucumber. Here are some of the keywords you might encounter while using Cucumber:
- **Feature**: provides a high-level description of some feature of the system under development or test. It is used to logically group scenarios.
- **Scenario**: a representation of a concrete example of the behavior of the system that is in development or under test.
- **Step**: scenarios are composed of steps. There are three types of steps: given, when, and then:
- **Given**: specifies a precondition to an event that will or should or occur during a scenario.
- **When**: specifies the occurrence of the event itself.
- **Then**: specifies the expected outcome of the event that has occurred.
- **Background**: used when all of the scenarios within a feature share at least one precondition. The preconditions defined using the background keyword apply to all scenarios within a feature.
- **Scenario Outline**: used to create a data-driven driven scenario that is run several times around different sets of data.
- **Examples**: used to define data sets for scenario outlines.
- **And/But**: used to replace given, when, or then. If, for instance, there are multiple preconditions for a scenario, a developer may choose to use and or but for every precondition following the first precondition. For example:

```
Given first precondition
And second precondition
And third precondition
When event occurs
And another event occurs
Then expected outcome
```
>Note that there are a few more keywords in Cucumber. The ones listed above just happen to the most commonly used keywords.

### How To Write A Feature File
In order to write a feature file, a developer only has to create a file that uses the `.feature` extension. If the developer is creating the feature file in an integrated development environment, they should also download the appropriate Cucumber extension for their environment.

After creating the file, the developer can immediately start filling it with scenarios. Here is an example of a basic feature file called `TodoCompletion.feature`:

```
#TodoComplete.feature

Feature: Checking Todo Completion

	Scenario: A user wants to update the status of any potentially completed todos
		Given a user is on the View Todos page
		And the user is logged in as a basic user
		And the user has at least one completed todo in their list of todos
		When the user hits the CHECK TODOS button
		Then the completed todos will be marked as complete on the page
```

This feature file makes use of most of keywords we saw above. It defines a feature and one scenario related to that feature. There are several steps associated with this feature. As you can see, the entire focus is on the behavior of the system under development or test, and that behavior is described using a language that everyone on a development team can understand.

Let's add another scenario:

```
#TodoComplete.feature

Feature: Checking Todo Completion

	Scenario: A user wants to update the status of any potentially completed todos
		Given a user is on the View Todos page
		And the user is logged in as a basic user
		And the user has at least one completed todo in their list of todos
		When the user hits the CHECK TODOS button
		Then the completed todos will be marked as complete on the page

	Scenario: A user wants to use the update feature when there are no completed todos
		Given a user is on the View Todos page
		And the user is logged in as a basic user
		And the user does not have a completed todo in their list of todos
		When the user hits the CHECK TODOS button
		Then none of the incomplete todos will be marked as complete on the page
```

We've added a second scenario for the sake of showing a feature file with multiple scenarios. That said, the preconditions for the new scenario look similar to those of the first scenario. In this case, we can use the **Background** keyword to remove some of that redundancy:

```
#TodoComplete.feature

Feature: Checking Todo Completion

	Background:
		Given a user is on the View Todos page
		And the user is logged in as a basic user

	Scenario: A user wants to update the status of any potentially completed todos
		Given the user has at least one completed todo in their list of todos
		When the user hits the CHECK TODOS button
		Then the completed todos will be marked as complete on the page

	Scenario: A user wants to use the update feature when there are no completed todos
		Given the user does not have a completed todo in their list of todos
		When the user hits the CHECK TODOS button
		Then none of the incomplete todos will be marked as complete on the page
```

With the addition of the our background, our scenarios are a bit less redundant and detail only the steps that are unique to themselves.

Now let's say that we want to run a data-driven test in which we pass in different data sets to our tests. In that case, we'll need to use the `Scenario Outline` and `Examples` keywords like so:

```
#TodoComplete.feature

Feature: Checking Todo Completion

	Background:
		Given a user is on the View Todos page
		And the user is logged in as a basic user

	Scenario: A user wants to update the status of any potentially completed todos
		Given the user has at least one completed todo in their list of todos
		When the user hits the CHECK TODOS button
		Then the completed todos will be marked as complete on the page

	Scenario: A user wants to use the update feature when there are no completed todos
		Given the user does not have a completed todo in their list of todos
		When the user hits the CHECK TODOS button
		Then none of the incomplete todos will be marked as complete on the page

	Scenario Outline: A user wants to update the status of any potentially completed todos
		Given the user has <complete> completed todos and <incomplete> incomplete todos in their list of todos
		When the user hits the CHECK TODOS button
		Then <complete> of the todos will be marked as complete on the page
		And there should be a total of <total> todos listed on the page

		Examples:
			| complete | incomplete | total   |
			| 3                |          6          | 9         |
			| 10              |          1          | 11       |
			| 4                |         19         | 23       |
```
>Note the parameterization of the scenario outline used above. Those parameters are taken from the example table below the scenario outline. There are three sets of data in the example table, which means that we will be able to run the test associated with this data set once per record when we start using the specialized JUnit test runner for Cucumber later on!