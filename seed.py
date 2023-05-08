from models import Pets, db
from app import app

db.drop_all()
db.create_all()

# empyt the table

Pets.query.delete()
# db.session.rollback();
# add some pets to the sessoin by declearing pet objecsts and
# then doing db.add

ruby = Pets(name = 'ruby', species = 'aussiedoodle',img_url= 'www.pic.com', age=2, comment = "she is super delicious", available=True)



db.session.add_all([ruby])

db.session.commit()

