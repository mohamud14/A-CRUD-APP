import flask
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

@app.route('/delete_team/<int:id>', methods=['GET', 'POST'])
def delete_team(id):
    if request.method == 'POST': ####if its a POST request then delete the friend from the database
        team = Teams.query.get_or_404(id)
        db.session.delete(team)
        db.session.commit()
        return redirect("/")
    else: ######if its a GET request then send them to the home page
        return redirect("/")

@app.route('/details/<int:id>', methods=['GET','POST'])
def showteam(id):
    form = PlayerForm()
    player_of_specific_team = Players.query.filter_by(plays_for=id)
    #players = Players.query.get(id)
    team = Teams.query.get_or_404(id)
    if flask.request.method == 'POST':
        if form.validate_on_submit():
            player = Players(plays_for=Teams.team_id,player_id=form.player_id.data, player_name=form.player_name.data)
            db.session.add(player)
            db.session.commit()
            return redirect('/details', id=id)

    #<!--    <a href="{{url_for('add_player',id=player.player_id)}}"> Add a new player!</a>-->
    return render_template('details.html', team_id=id, listofplayers=player_of_specific_team, form=form, pageTitle='Details', legend=" players on team")

@app.route('/updateteam/<int:id>', methods=['GET','POST'])
def update_team(id):
    team = Teams.query.get_or_404(id)
    form = TeamForm()

    if form.validate_on_submit():
        team.team_id = form.team_id.data
        team.team_name = form.team_name.data
        db.session.commit()
        return redirect('/')

    form.team_id.data = team.team_id
    form.team_name.data = team.team_name
    return render_template('update_team.html', form=form, pageTitle='Update team', legend="Update A team")


@app.route('/add_player/<int:id>', methods=['GET', 'POST'])
def add_player(id):
    form = PlayerForm()
    if form.validate_on_submit():
        player = Players(plays_for=id,player_name=form.player_name.data,player_id=None)
        db.session.add(player)
        db.session.commit()
        return redirect('/')

    return render_template('add_player.html', form=form,player_id=id, pageTitle='Add A New player',
                            legend="Add A New player")