# Project Proposal Files (README)
This README explains how to run and operate the ShareTray prototype, which includes all the prerequisite files (api, api_app, audit, role, models repo, state machine, user roles criteria and database). To this end the following files cover the steps needed to run the system locally and properly:


________________________________________
Files Contained within the Project Proposal Repository

•	models_repo.py 
	
	- Contains the Pydantic Models, InMemory Repo and the MongoRepo Adapter.

•	state_machine.py —
	
	- Contains the Donation Lifecycle Constraints, Audit Logging Systems and FastAPI modules.

•	user_roles_criteria.py 

	- Contains the CLI Manager for Roles & Acceptance Criteria Templates.

•	api.py 

	- Contains the Asynchronous FastAPI Application.

•	api_app.py 

	- Contains the Self-Contained FastAPI Application.

•	audit.py 

	- Contains the Audit Logging Helper used by api.py.

•	role.py — 

	- Contains the Authentication and Role-Based Dependencies (JWT and Password Hashing).

•	database.py 
	
	- Contains async Motor wrapper (new): init_db, CRUD helpers (used by api.py / role.py / audit.py).
