# Continuous delivery
## DevOps - Continuous Delivery

### References
- [Continuous Delivery - Martin Fowler](https://martinfowler.com/bliki/ContinuousDelivery.html)
- [Continuous Delivery - Atlassian](https://www.atlassian.com/continuous-delivery/pipeline)
- [CI CD CD - Atlassian](https://www.atlassian.com/continuous-delivery/principles/continuous-integration-vs-delivery-vs-deployment)

## Continuous Delivery
Continuous Delivery is a paradigm in which the building, management and testing of produced software is automated such that deployments can be performed at the push of a button.

Continuous delivery is often confused with Continuous Deployment, which automates the entire production pipeline, including deployment. Continuous Delivery; however is the process of automating all steps of a Development pipeline except for the final deployment step. Inherently, Continuous Delivery is dependent on the implementation of Continuous Integration, and also serves as a stepping stone to creating a fully automated Development Pipeline (Continuous Deployment). Though Continuous Integration can technically be achieved without automation, Continuous Delivery is only achieved when code integration, testing and product building has been automated. In this way, you are able to perform frequent deployments "at the press of a button", but may choose not to do so, usually for business purposes or possibly due to a preference for a regular scheduled deployment process.

The deployment to production may also be kept manual so that final user acceptance tests can be performed manually as a final safety check on the code to ensure that it meets business needs. This is due to the difficulty and cost of creating tests to evaluate the user experience and not simply the functionality.

### Benefits of Continuous Delivery:
- **Reduced Risk in Deployment**
  - Since new builds are not deployed automatically, faulty code is less likely to by deployed to production environments.
  - Less pressure is placed on the development team by allowing for small, more frequent changes to be made. This expedites the iteration of code.
- **Predictable Progress**
  - Since pipelines are a programmable infrastructure by the development team, desired behavior during the production of code is easier to configure.
  - With a pipeline the deployment process is more predictable, allowing development team to focus on the production of code rather than operational steps required to deploy the new codebase.
- **Frequent Feedback**
  - With the increased efficiency of producing code, smaller, more incremental changes can be applied to a system more frequently. If human error does cause problems, it is easy to roll back changes to a working build.
  - More releases accelerates the communication and feedback loop with client/product owners as well.

### Costs/Considerations of Continuous Delivery
- Requires a strong foundtation with Continuous Integration culture, and test suite coverage
- The Final deployment must still be automated which is an additional cost, Though the trigger to begin the process is manual this can still cause slowdown for the development.
- Communication of incomplete features and backlog must be maintained rigorously to communicate expectations to client and development team