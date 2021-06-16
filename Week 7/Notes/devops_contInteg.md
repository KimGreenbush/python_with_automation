# Continuous integration
## DevOps - Continuous Integration

### References
- [Continuous Integration - Martin Fowler](https://martinfowler.com/articles/continuousIntegration.html)
- [CI Circle Image](https://www.qfs.de/en/blog/article/2019/07/11/using-qf-test-in-continuous-integration-systems-1.html)
Below are examples version control software:
- [Github](https://github.com/features)
- [Gitlab](https://about.gitlab.com/features/)
- [Perforce](https://www.perforce.com/support/self-service-resources/documentation)
- [Bazaar](http://doc.bazaar.canonical.com/en/)
- [DevOps Tools](https://app.revature.com/#)

## Continuous Integration
Continuous Integration (CI) is the first, and most fundamental step in creating an autonomous development pipeline.

Similarly to **Continuous Delivery** and **Continuous Deployment**, Continuous Integration is a development team mentality, and is achieved when all members of the development team practice consistent merging of code into a central repository. For CI to take place, these Central repositories should be in the form of version control software.

Version control software is a tool which utilizes some directory structure to store files. These tools can track changes to code, and allow for changes to be merged (allowing you to select which changes to keep or reject if/when conflicts arise) or files to be rolled back to a previous version. The integration of code into these repositories should happen as often as possible with at least one commit each day. Generally, the more frequently code is merged, the less conflicts and/or integration issues will arise.

Continuous Integration establishes the foundation for an automated DevOps pipeline, because it provides the following benefits:
- Ensures the entire team works on the most up to date code
  - Frequently pushing code allows developers to account for changes performed by other team members quickly.
- Detects broken builds quickly
  - If problems arise, version control software can help detect the root cause or rollback changes when necessary.
- Code can be tested easily by creating separate, test or development branches based on the mainline code.
- Reduces risk in development when a large codebase has already been established.
- Reduces the overall amount of bugs in a project

The best way to ensure your code integrates well is to marry the integration of your code with testing the code. Running test suites on the code base after new commits helps to minimise potential disruptions if conflicts do arise, particularly when utilizing certain *DevOps tools* to automatically run unit and integration tests. Despite this, it is also best to practice Test Driven Development.

## [Test Driven Development](https://gitlab.com/revature_training/automation-testing-team)
The practice of developing code based on written test cases, as opposed to writing test cases to based on developed code, in other words, Development cycle in which test cases are first written, and then code is developed in order to allow those tests to pass.