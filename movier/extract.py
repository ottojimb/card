import functools


from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from movier.db import get_db
from movier.external_api import find_movie_by_title

bp = Blueprint('extract', __name__, url_prefix='/extract')

@bp.route('/list', methods=('GET', 'POST'))
def list():
    if request.method == 'POST':
        error = f'Not defined yet'
        flash(error)


    title = request.args.get("title")
    g.results = find_movie_by_title(title)

    return render_template('extract/index.html')
