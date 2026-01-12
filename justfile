default:
    @just -l


run-backend:
    cd backend && python app.py
    