from flask import Blueprint, render_template


blueprint = Blueprint('view', __name__)


@blueprint.route('/')
def index():
	return render_template('index.html')
