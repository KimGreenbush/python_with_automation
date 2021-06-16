# DevOps Concepts

### References
- [DevOps Culture](https://martinfowler.com/bliki/DevOpsCulture.html)
- [Continuous Delivery - Atlassian](https://www.atlassian.com/continuous-delivery/pipeline)
- [CI CD CD - Atlassian](https://www.atlassian.com/continuous-delivery/principles/continuous-integration-vs-delivery-vs-deployment)
- [Continuous Deployment vs Continuous Delivery - Atlassian](https://www.atlassian.com/continuous-delivery/continuous-deployment/how-to-get-to-continuous-deployment)
- [DevOps Image Source](https://www.logigear.com/blog/continuous-delivery-devops/continuous-delivery-everything-you-need-to-know/)

## DevOps
Software Development (dev) Operations (ops) are a set of practices and methodologies designed to combine the development (production/writing of code), deployment and maintenance of code into a streamlined process. **The primary goal of DevOps is to expedite the lifecycle of application development, particularly through the automation of tasks.**

### Steps in Dev Ops and Production of Code
The steps or phases for Dev Ops refers to the **creation**, **testing**, and **deployment** of an application.

These steps include:
1) **Source code Control**: Producing (writing) code and pushing to a repository
2) **Building and Testing Automation**: Test basic functionality of code (Generally unit testing) and create a new, working build
3) **Deploying to Staging**: Deployment of working build to a temporary environment
4) **Acceptance Testing**: Undergo other more complex tests (systems, integration) within temporary environment
5) **Deployment of Build**: Migrate working build to Production environment accessible by end users

### DevOps and Agile
Agile is a mentality or philosophy utilized when approaching the creation of information systems, and is a** flexible approach** of addressing the steps of the Software Development Life Cycle. Development teams who practice an Agile methodology place a focus on producing code through iteration and collabortion rather than following a rigid plan.

Though DevOps, which involves the creation of a systematic approach to producing code, and Agile, which is a mentality that focuses on creating products by adapting to change quickly, seem contradictory, the goal of both methodologies is to produce working and valuable product more efficiently. DevOps pertains to the entire system working together to produce, test, deploy and maintain the code base, while Agile practices allow for each step of that process to change wherever and whenever needed.
- Agile Practices with DevOps:
  - Continuous Integration
  - Continuous Delivery
  - Continuous Deployment

Adoption of the Agile philosophies can provide a stepping stone for the establishment of a working DevOps pipeline, as Agile practices intrinsically produce more continuous feedback loops. Continuous Integration, Continuous Delivery and Continuous Deployment seek to automate the phases of DevOps as much as possible.

### Continuous Integration
The process of regularly and consistently merging code into a central repository and reviewing new code to ensure that it integrates well within the previously established code base.

Tools used for this task:
- [Github](https://github.com/features)
- [Gitlab](https://about.gitlab.com/features/)
- [Perforce](https://www.perforce.com/support/self-service-resources/documentation)
- [Bazaar](http://doc.bazaar.canonical.com/en/)
- [DevOps Tools](https://app.revature.com/#)

### Continuous Delivery
Development principle which focuses on the automation of the Dev Ops pipeline to the extent that human intervention is not required. Generally, this means that steps 1 - 3 (source code control, building and testing, and deployment to staging) are automated, while steps 4 (acceptance testing) may be handled by a Human, if necessary and step 5 (deployment to production environment) requires manual approval.

### Continuous Deployment
Development principle which automates all phases of the Dev Ops Pipeline.