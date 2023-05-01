# Fisheries-Governance-Simulation
In this project, we explore the effects of the tragedy of the commons game on fisheries and the effectiveness of different policies in protecting these valuable resources. The over-exploitation of fisheries is a prime example of the tragedy of the commons, as individual users lack the private incentive to maintain the resource. This issue has led to the depletion of fish populations and negative economic impacts on the fishing industry. Our goal is to use evolutionary game theory to shed light on how regulatory policies can result in healthier fisheries with maximum economic benefit.

To achieve this goal, we will take a multi-agent simulation-based approach, which includes competing fishing agents and distributed fish populations. Fishermen will take actions that differ in fishing locations and the quantity of fish caught, and the fish population size and distribution will vary in response to the actions of the fishermen. We will evaluate the effectiveness of various policies, such as fishing quotas and marine protected areas, in maximizing profit for fishermen while also being sustainable in the long term.

The Python package Mesa will provide the necessary functionality to produce this policy-restricted multi-agent simulation.

## Agents
### Fisheries
The Fisheries agent is a class in the multi-agent simulation model that represents fishing vessels. These agents compete for fish in a shared resource pool, making decisions about where to fish and how many fish to catch based on available information. They seek to maximize profit while also avoiding penalties and fines for violating policies. 
### Fish
The Fish agent in the fisheries simulation model represents a single fish. Each fish has a unique ID and a position (x, y) on the grid. The fish agent can move to a neighboring cell on the grid and will reproduce yearly. Additionally, the fish agent can be caught by the Fishery agent when it is within a certain distance from the fishery's location. The behavior of the fish agent is an important factor in the overall population dynamics of the simulation and is influenced by the actions of the fishing agents and the policies implemented by the model.

## Policies
### Fishing Quotas
### Gear Restrictions
### Marine Protected Areas
### Size limits
### Taxes and Penalties
## Installations
`pip install mesa`

## Citations
