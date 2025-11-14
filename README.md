# Project Proposal Files (README)
This README explains how to run and operate the ShareTray prototype, which includes all the prerequisite files (api, api_app, audit, role, models repo, state machine, user roles criteria and database). To this end the following files cover the steps needed to run the system locally and properly:


________________________________________
**Files Contained within the Project Proposal Repository**

•	models_repo.py 
	
- Contains the Pydantic Models, InMemory Repo and the MongoRepo Adapter.

•	state_machine.py
	
- Contains the Donation Lifecycle Constraints, Audit Logging Systems and FastAPI modules.

•	user_roles_criteria.py 

- Contains the CLI Manager for Roles & Acceptance Criteria Templates.

•	api.py 

- Contains the Asynchronous FastAPI Application.

•	api_app.py 

- Contains the Self-Contained FastAPI Application.

•	audit.py 

- Contains the Audit Logging Helper used by api.py.

•	role.py

- Contains the Authentication and Role-Based Dependencies (JWT and Password Hashing).

•	database.py 
	
- Contains async Motor wrapper (new): init_db, CRUD helpers (used by api.py / role.py / audit.py).

________________________________________
**Prerequisites**

•	Python 3.10+ (Recommended)

•	Git (Optional)

•	MongoDB

**Recommended Course of Action**

(How to Create and Activate a Virtual Environment)

	- python -m venv .venv

**Linux**

	- source .venv/bin/activate

**Windows**

	- .venv\Scripts\Activate.ps1

**Dependences (To Be Installed)**

•	Minimum Version (In-Memory Dev):

	- pip install fastapi uvicorn pydantic

•	Full Version (Mongo, JWT, hashing, ngrok):

	- pip install fastapi uvicorn pydantic pymongo motor python-jose[cryptography] passlib[argon2] pyngrok nest_asyncio 
	
Then:

	- pip install -r requirements.txt
	
________________________________________
**Environment Variables**
-  Details what environmental variables exist within the files, what they do and if they could be modified.

•	MONGO_URI 
	
- Contains the MongoDB connection string, e.g. mongodb://localhost:27017.
- If set and PYmongo installed, models_repo will use MongoRepo.
- api.py also uses database.py and needs this for persistence.

•	MONGO_DB

- Contains the Database Name.
- Default Name: sharetray.

•	NGROK_AUTH_TOKEN 
-  Contains the ngrok token if you want a public URL for api.py.
-  Note: Do not commit this token.

•	JWT_SECRET_KEY 
- Contains the secret key for JWT signing used by role.py.
- Default is a dev key in code.

•	JWT_ALGORITHM 
- Default: HS256.

•	ACCESS_TOKEN_EXPIRE_MINUTES 
- Default: 60.

________________________________________
**Steps to Accomplish a Quick Dev Run**
- Minumim Version (In-Memory Dev)

1.	Start the Minimal App:

		- uvicorn api_app:app --reload --port 8000

2.	Seed Demo Data
    - Establishes and Creates Demo Donor, Recipient, Volunteer and Donation
    
			- curl -X POST http://127.0.0.1:8000/seed/demo

**Example Flow:**

•	List open donations:

	- GET http://127.0.0.1:8000/donations/open
  	
•	Run the greedy matcher:

	- POST http://127.0.0.1:8000/match/run
	
	- Body: {"max_search_km":5.0}
•	Plan a pickup:

	- POST http://127.0.0.1:8000/pickups/plan
	
	- Body: {"volunteer_id":"<vol-id>","donation_ids":["<don-id>"]}

•	Transition donation state:

	- POST http://127.0.0.1:8000/donations/<donation-id>/transition
	- Body: {"new_state":"pickup_scheduled","actor_user_id":"<user-id>","notes":"assigned"}
	
•	Fetch audit logs:

	- GET http://127.0.0.1:8000/donations/<donation-id>/audit_logs
	
****NOTE**:** api_app.py will import models_repo.repo. If MONGO_URI is not set, repo defaults to the in-memory repo.


________________________________________
**Steps to Accomplish a Full Dev Run**
- Full Version (MongoDB with Persistence and Authentication)
  
1.	Start MongoDB (Local or Docker).
   
2.	Set env vars:

		- export MONGO_URI="mongodb://localhost:27017"
		- export MONGO_DB="sharetray"
		- export JWT_SECRET_KEY="a_long_random_secret"
		- export NGROK_AUTH_TOKEN="optional_ngrok_token"
  	
3.	Install full dependencies (See Above).
4.	Start the async app (this uses database.py which relies on Motor):
   
		- uvicorn api:app --reload --port 8000
  	
5.	Use role.py endpoints to create users and obtain JWT tokens:
   
	•	POST /users to create (Returns ID).

	•	POST /token to get an access token (Use OAuth2PasswordRequestForm).

6.	Include Authorization:
   
	•	Bearer <token> header for endpoints protected by require_role









