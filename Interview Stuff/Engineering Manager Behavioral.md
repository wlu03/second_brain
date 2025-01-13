1. Describe your management philosophy.
	My management philosophy centers around fostering a supportive environment where team members feel empowered to contribute their ideas, take ownerships and pride in their feature/work and continuous development in their skills.
	I want to align individual goals with the overall objective of bits of good (which is developing useable products for non-profit companies). Through open communication and clear expectation, this can achieve high performance as a team.   
	
2. What do you measure when evaluating the performance of devs?
    - Code Quality - i.e. comments (docs strings), readable code (clear variable naming), proper documentation, modular design (break large functions into smaller reusable components), error handling,  writing unit tests, avoid hardcoding, single responsibility principle 
    - Ability to learn new techniques 
    - Cycle time (time from initial commit to deployment)
    - Lead time (time from feature request to production)
    - Amount of bugs produced
    - Participation in discussions in meeting
    - Meeting deadlines and task accuracy
3. How do you measure those things?
	- Conduct **code reviews** to assess the presence and quality of comments and inline documentation
	- **Checkstyles - Java** to ensure code follows documentation standards
	- **Pylint for Python**
	- Check code structure for reusability and follow principles like SRP
	- Verify that exceptions are handled properly 
	- I will measure participation using Excel to track metrics like: participation, provide a metric for how engaged they were, the feedback
	- CI/CD tools like GitLab to measure the first commit and production deployment (Cycle Time)
	- Log Feature request using Azure DevOps
	- To ensure deadlines are met i will use either monday.com or Gantt chart in excel
    
4. When faced with an underperforming dev, what steps do you as a manager take to rectify the situation?
	- Identify the issue through a private discussion to understand their challenges
	- Define expectation and create a performance improvement plan (PIP) with specific measurable goals and check in regularly
	- Potentially, pair the dev with a more experience developer to help with challenges and provide mentoring
	- Encourage accountability and track progress with metrics
	- Monitor their progress and adjust the plan
	- if the performance doesn't improve despite the support, I will provide less task for this individuals and redistributing the work. 
	- Unfortunately, this could delay the find deployment of the project. However, quality is important when dealing with these projects, so it's important to communicate to companies of what's going on with development.
5. How do you approach estimating timelines?
	- Examine the estimates made for developments in the past with a comparable project.  
	- To be conservative with development time, I will multiply this by 1.25. For example, if development took 2 months, a new project deadline should take 2.5 months. 
	- The key is tracking the development of previous projects so we have data on making reasonable dates for future developments. 
	- Okay so what if we don't have past data? 
		- If there is not past data, I will. break the project into smaller more manageable tasks. Estimate the time for each task based on the experience of members.
		- Then I will sum these estimate for the task. Additionally, I will reach out to past EM to gain some insight on how long similar tasks might take. 
		- Instead of providing a single number, using a range of the least amount of time to the longest will allow flexibility to the development for unknown challenges.
    
6. How do you shield your team from unreasonable deadlines? What if the deadline is critical for the business to continue operating?
	I provide an estimate of how long the work will take in hours by each task. I will recommend what tasks to be removed to meet the client's goals or where we can split work across developers when possible.