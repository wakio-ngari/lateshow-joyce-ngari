from flask import Blueprint, jsonify, request
from app import db
from app.models import Episode, Guest, Appearance

bp=Blueprint('routes', __name__)

@bp.route('/episodes')
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([{'id': e.id, 'date': e.date,'number': e.number} for e in episodes])

@bp.route('/episodes/<int:id>')
def get_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return jsonify({'error': 'Episode not found'}), 404
    return jsonify({
        'id': episode.id,
        'date': episode.date,
        'number': episode.number,
        'appearances': [{
            'id': a.id,
            'rating': a.rating,
            'guest': {'id': a.guest.id, 'name': a.guest.name, 'occupation': a.guest.occupation}
        } for a in episode.appearances]
    })

@bp.route('/guests')
def get_guests():
    guests= Guest.query.all()
    return jsonify([{'id': g.id, 'name': g.name, 'occupation': g.occupation} for g in guests])

@bp.route('/appearances', methods=['POST'])
def create_appearance():
    data =request.json
    try:
        appearance = Appearance(
            rating=data['rating'],
            episode_id=data['episode_id'],
            guest_id=data['guest_id']
        )
        db.session.add(appearance)
        db.session.commit()
        return jsonify({
            'id': appearance.id,
            'rating': appearance.rating,
            'episode_id': appearance.episode_id,
            'guest_id': appearance.guest_id,
            'guest': {'id': appearance.guest.id, 'name': appearance.guest.name, 'occupation': appearance.guest.occupation},
            'episode': {'id': appearance.episode.id, 'date': appearance.episode.date, 'number': appearance.episode.number}
        }), 201
    except Exception as e:
        return jsonify({'errors': [str(e)]}), 400