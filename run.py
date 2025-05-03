from app import create_app, db

app = create_app()

# Création de la base de données si elle n'existe pas encore
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
