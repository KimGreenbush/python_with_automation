# Continuous deployment
## DevOps - Continuous Deployment

### References
- [Continuous Deployment - Atlassian](https://www.atlassian.com/continuous-delivery/continuous-deployment)
- [How to Achieve Continuous Deployment - Atlassian](https://www.atlassian.com/continuous-delivery/continuous-deployment/how-to-get-to-continuous-deployment)
- [CI CD CD - Atlassian](https://www.atlassian.com/continuous-delivery/principles/continuous-integration-vs-delivery-vs-deployment)

## Continuous Deployment
Continuous Deployment is a process of releasing software in which changes are tested for stability and correctness automatically. This results in immediate, autonomous deployment of code to production environments.

Continuous Deployment is often confused with Continuous Delivery due to nomenclature as both are referred to as 'CD'; however, Continuous Delivery is simply a precursor to Continuous Deployment. In Continuous Delivery there is a final, manual approval process needed before code is deployed to production environments. Continuous Deployment forgoes human intervention at every step of the deployment process, and pushes new code into the working production environment immediately so long as it meets the test requirements. When Continuous Deployment is achieved, every commited change to the code base creates and deploys a new build to the production environment.

**Continuous Deployment is the ultimate goal for establishing a true DevOps pipeline**, as it ensures that all steps for the creation of product, including code creation, testing, building, and deployment are automated and work seamlessly together.

As the major difference for Continuous Deployment and Delivery resides in the manual approval of deploying code to production, many benefits (feedback speed, code quality and efficiency) are retianed with the use of Continuous Deployment. However, there are some additional considerations for Continuous Deployment:

### Costs/Risks of Continuous Deployment
- Establishing a Continuous Deployment pipeline requires a more substantial investment in the engineering, and the testing culture.
- Documentation of processes is required to communicate to development, production and testing teams.
- Ongoing maintenance of deployment pipeline is required to ensure work continues running smoothly, increasing production costs.
- Feature flags (communication of completed features and progress) are required for coordination between departments.

### Benefits of Continuous Deployment
- Even faster development process, without the need to pause for deployment.
- New releases are less risky, as small changes can be easily recognized and fixed, allowing for better and quicker feedback.
- Increased communication and regular streams of improvements are generally regarded highly by customers.