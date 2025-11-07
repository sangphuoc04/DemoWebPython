from flask import Blueprint

about = Blueprint('about', __name__)

@about.route('/about')
def about_page():
    from backend.services.about import about
    return about()