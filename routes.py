from main import *
from schema import *


@app.route('/')
def index():
    all_teams = Teams.query.all()
    return render_template('index.html',
                           all_teams=all_teams, pageTitle='Home')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        form = request.form
        search_value = form['search_string']
        search = "%{0}%".format(search_value)
        results = Teams.query.filter(Teams.team_name.like(search)).all()
        return render_template('index.html', all_teams=results, pageTitle='Mohamed', legend="Search Results")
    else:
        return redirect('/')

@app.route('/add_team', methods=['GET', 'POST'])
def add_team():
    form = TeamForm()
    if form.validate_on_submit():
        team = Teams(team_id=form.team_id.data, team_name=form.team_name.data)
        db.session.add(team)
        db.session.commit()
        return redirect('/')

    return render_template('add_team.html', form=form, pageTitle='Add A New team',
                            legend="Add A New team")