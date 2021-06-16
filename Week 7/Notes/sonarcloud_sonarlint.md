# SonarCloud & SonarLint
## DevOps Tools - Sonar
Sonar cloud, Sonar Qube and Sonar lint are code quality analysis tools which increase the readability, security and matainability of code. Utilizing code quality analysis tools can help development teams produce higher quality code, and provide standardization between developers, which can play a vital role in the integration of code.

### References
- [Sonar Cloud - Documentation](https://sonarcloud.io/documentation)
- [Sonar Qube - Documentation](https://docs.sonarqube.org/latest/)
- [Sonar Lint - Github](https://github.com/SonarSource/sonarlint-eclipse)

## Code Quality Analysis and Code Smells
Code Quality Analysis tools are programs specifically designed to expose errors as well as 'code smells'.
- Vulnerabilities
  - Data security issues
- Bugs
    - Issues with functionality of code
- Maintainability issues
  - Confusing or hard to maintain code
  - Repeated instances of code
  - Unused imports
  - Empty code blocks
  - Unaddressed automated code comments

## Sonar Cloud
A cloud based code review solution which can be configured to review code within a cloud repositoy, such as Github.

### Sonar Cloud with Github Installation
- Navigate to the [Sonar Cloud Login Page](https://sonarcloud.io/sessions/new), and select "Log in with Github"
- Click on "Analyze your code" and follow the steps for project setup
- Select the repository to analyze.

You may Automatically analyze your code with Sonar Cloud, or by configuring another Continuous Integration Tool.

- [Sonar Cloud with Travis CI](https://sonarcloud.io/documentation/integrations/ci/travis-ci/)
- [Sonar Cloud with Circle CI](https://sonarcloud.io/documentation/integrations/ci/circleci/)

## Sonar Qube
Code review tool built to work on a centralized server or integrated into a development pipeline. Due to the increased flexibility and configuration options of Sonar Qube, it can be seen as a more powerful tool.

### Sona Qube Installation
- [Quickstart Guide](https://docs.sonarqube.org/latest/setup/get-started-2-minutes/)
- [Production Environment Guide](https://docs.sonarqube.org/latest/setup/install-server/)

## Sonar Lint
Sonar Lint is a free, open-source linting tool. A linting tool/linter is a software tool which, when integrated with an IDE, can provide increased feedback to the developer. Traditional IDE tools utilize built-in linters to identify code syntax errors, and exceptions. Sonar Lint provides further suggestions by recognizing code smells.

### [Sonar Lint - Ecplise](https://marketplace.eclipse.org/content/sonarlint)
1. Open Eclipse
2. Select "Ecplise Marketplace..." from the Help Menu
3. Search for "Sonar Lint" in the searchbox
4. Select Install and accept the User Agreement
5. Restart Ecplise

### [Sonar Lint - Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=SonarSource.sonarlint-vscode)
1. Open Visual Studio Code
2. Select the "Extensions" Tab from the project explorer
3. Search for "Sonar Lint" and Select Install