from app import mongo

class JobPosting:
    def __init__(self, title, description, user_id, images):
        self.title = title
        self.description = description
        self.user_id = user_id
        self.images = images

    def save(self):
        job_postings = mongo.db.job_postings
        job_posting_id = job_postings.insert_one({
            'title': self.title,
            'description': self.description,
            'user_id': self.user_id,
            'images': self.images,
        })
        return str(job_posting_id.inserted_id)
