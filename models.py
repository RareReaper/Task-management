from app import db
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    due_date = db.Column(db.String(10), nullable=True)
    priority = db.Column(db.Integer, nullable=True)
    completed = db.Column(db.Boolean, default=False)
