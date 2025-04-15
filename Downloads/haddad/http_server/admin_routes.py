from flask import Blueprint, request, jsonify
from backend.database.db import SessionLocal
from backend.database.models import Party

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/create_party', methods=['POST'])
def create_party():
    data = request.json
    session = SessionLocal()
    try:
        new_party = Party(name=data.get("name", "Partie"))
        session.add(new_party)
        session.commit()
        return jsonify({"status": "OK", "party_id": new_party.id})
    except Exception as e:
        session.rollback()
        return jsonify({"status": "KO", "error": str(e)})
    finally:
        session.close()
