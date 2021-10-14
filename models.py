from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin):
    def __init__(self, id, name, email, password, is_admin=False):
        self.id = id
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)
        self.is_admin = is_admin
    def set_password(self, password):
        self.password = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password, password)
    def __repr__(self):
        return '<User {}>'.format(self.email)

class Employee(UserMixin):
    def __init__(self, id, name, email, password, address,branch,job,contract,salary,contract_start
    , contract_end,is_admin=False):
        self.id = id
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)
        self.address = address
        self.branch = branch
        self.job = job
        self.contract = contract
        self.salary = salary
        self.start = contract_start
        self.end = contract_end
        self.is_admin = is_admin
    def set_password(self, password):
        self.password = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password, password)
    def __repr__(self):
        return '<User {}>'.format(self.email)

users = []
employees =[]
users.append(User(len(users) + 1, "moco", "admin", "admin",True))
def get_user(email):
    for user in users:
        if user.email == email:
            return user
    return None