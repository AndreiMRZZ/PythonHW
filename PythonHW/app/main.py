from app import create_app
from app.storage.db import db_init
app = create_app()

if __name__ == "__main__":
    db_init()
    app.run(debug=True, host="0.0.0.0", port=5000)
