from flask import Blueprint

auth_bp = Blueprint('auth', __name__)
job_postings_bp = Blueprint('job_postings', __name__)

# Import your routes
from app.routes import auth, job_postings
