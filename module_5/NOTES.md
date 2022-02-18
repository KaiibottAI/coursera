## WEEK 4

### Storing Data in the Cloud

Different Types of Storage
 - `Block Storage` - Block storage in the cloud acts almost exactly like a hard drive
 - `Persistent Storage` - Used for instaces that are long lived and need to keep data across reboots and upgrades
 - `Ephemeral Storage` - Used for instances that are only temporary and only need to keep local data while they're running
 - `Object Storage` - Lets you place and retrieve objects in a storage bucket
 - `Blob Storage` - Pieces of data that are stored as independent objects and require no file system (`B.L.O.B` stands for Binary Large OBject )

`Input/Output Opersations Per Second (IOPS)` - Measures how many reads or writes you can do in one second, no matter how much data you're accesssing
`Latency` - THe amount of time it takes to complete a read or write operation

### Load Balancing

`Round Robin DNS` - Common for load balancing as it will give requests in sequence to the machines in a circle
`Sticky Session` - All requests from the same client always go to the same backend server
`Content Delivery Networks` - (CDN) Make up a network of physical hosts that are georgraphically located as close to the end users as possible

### Change Management

`Continuous Integration System` - (CI) Will build and test our code every time there's a change
`Continuous Deployment` - (CD) Will deploy after successful changes / unit test / integration tests
`Environment` - Everything needed to run the services
`Test Environment` - Copy of PRODUCTION environment, but not facing customers / users
`Production Envirionment` - Live code facing your customers / users

Examples: 
You could have multiple `Test Environments` like "Dev" and "Pre-Prod"
Dev will handle multiple changes and validate all changes.
Pre-Prod will handle approved changes for further validation and testing
Prod will handle the packages changes that have been vetted by all parties in your business

`A/B Testing` - Some requests are served using sone set of code and confuration (A) and other requests are served useing a different set of code and configuration (B)


### Understanding Limitations

Example:
When using BLOB storage, there may be a write limit of 1,000 in a given second

`Rate Limits` - Prevent one service from overloading the whole system
Example: Can only make so many calls in a second or day

`Utilization limits` - Cap the total amount of a certain resource that you can provision
 
### Getting Started with Monitoring

`Monitoring and Alerting Rules`

Monitoring lets us look at the history of the service.
