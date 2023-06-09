"""Routes for logged-in application."""
from flask import Blueprint
from flask import current_app as app
from flask import redirect, render_template, session, url_for
from flask_login import login_required, logout_user, current_user

from .assets import compile_auth_assets

# Blueprint Configuration
main = Blueprint('main', __name__, template_folder='templates', static_folder='static')

@main.route('/', methods=['GET'])
@main.route('/index', methods=['GET'])
@login_required
def dashboard():
    """Serve logged-in Dashboard screen."""
    session['redis_test'] = 'This is a session variable.'
    return render_template('dashboard.jinja2',
                           title='Flask-Session Tutorial.',
                           template='dashboard-template',
                           current_user=current_user,
                           body='You are now logged in!')

@main.route('/session', methods=['GET'])
@login_required
def session_view():
    """Display the session variable value."""
    return render_template('session.jinja2',
                           title='Flask-Session Tutorial.',
                           template='dashboard-template',
                           session_variable=str(session['redis_test']))

@main.route('/logout')
@login_required
def logout():
    """User log-out logic."""
    logout_user()
    return redirect(url_for('auth.login'))