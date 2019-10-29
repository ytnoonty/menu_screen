from menuscreen import create_app
app = create_app()
app.app_context().push()
from menuscreen import db
db.drop_all()
db.create_all()
