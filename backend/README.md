# CarPartFinderPro

A web platform for posting car part listings, with a focus on parts for imported American cars and vehicles with hard-to-find parts.

---

## Workflow:

### How to start the project on a local machine:
1. `git clone` - clone the repository
2. `python -m venv venv` - install virtual environment
3. Activate The virtual environment:
- On windows
  - `venv\Scripts\activate.bat`
- On linux
  - `source venv/bin/activate`

4. `pip install -r requirements.txt` - install the required packages

### Branches:
- Use `frontend-branch` for frontend-related file modifications.
- Use `backend-branch` for backend-related file modifications.

### Synchronize between branches:
1. `git fetch` - to find new branches
2. `git checkout -b <branch-name> origin/<branch-name>` - to add a branch locally and synchronize

### Migrations:
1. `python manage.py makemigrations` - create new migrations
2. `python manage.py migrate` - apply the migrations

### Generate and load fixtures:
1. `python manage.py load_fixtures` - load the fixtures


---

### TO DO:
- [x] Create project structure
- [x] set project: 
  - [x] configuration / settings 
  - [x] requirements
  - [x] runtime
  - [x] instruction
- [x] Add models:
  - [x] address, car_part, delivery, parcel, user
  - [x] Favorite (will hold FGK for user and car part)
- [x] Add field Phone number for User model
- [ ] Add API / endpoint for:
  - [x] Favorite
  - [ ] Login
  - [ ] Register
- [ ] Refactor API
- [ ] Refactor Serializers
- [ ] Add validation for serializers