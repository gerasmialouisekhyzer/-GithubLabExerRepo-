# Project Proposal Files (README)
This README explains how to run and operate the ShareTray prototype, which includes all the prerequisite files (api, api_app, audit, role, models repo, state machine, user roles criteria and database). To this end the following files cover the steps needed to run the system locally and properly:


________________________________________
Files in this repo
•	models_repo.py — Pydantic models + InMemoryRepo and optional MongoRepo adapter.
•	state_machine.py — donation lifecycle rules + audit logging + small FastAPI endpoints.
•	user_roles_criteria.py — CLI manager for roles & acceptance-criteria templates.
•	api.py — async FastAPI app (uses database.py, JWT auth via role.py, audit logging).
•	api_app.py — self-contained minimal FastAPI app that can run with the local repo (sync). Good for fast dev.
•	audit.py — audit logging helper used by api.py.
•	role.py — authentication & role-based dependencies (JWT, password hashing).
•	database.py — async Motor wrapper (new): init_db, CRUD helpers (used by api.py / role.py / audit.py).
