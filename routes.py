import flask
from main import *
from main import app
from schema import *



@app.route('/')                  # Home page shows all teams
def index():
    all_teams = Teams.query.all()
    return render_template('index.html',
                           all_teams=all_teams, pageTitle='Home')

@app.route('/search', methods=['GET', 'POST'])
def search():                                     # POST used to send html data received from
    if request.method == 'POST':                  # form to the server
        form = request.form                       ## search returns all teams with characters
        search_value = form['search_string']      ## searched by the user
        search = "%{0}%".format(search_value)
        results = Teams.query.filter(Teams.team_name.like(search)).all()
        flash("These are your search results! Click Home to go back......")

        return render_template('index.html', all_teams=results, pageTitle='Search', legend="Search Results")
    else:
        return redirect('/')

@app.route('/add_team', methods=['GET', 'POST'])
def add_team():
    form = TeamForm()
    if form.validate_on_submit():
        team = Teams(team_id=form.team_id.data, team_name=form.team_name.data)
        db.session.add(team)
        db.session.commit()
        flash("Added Team!")
        return redirect('/')

    return render_template('add_team.html', form=form, pageTitle='Add A New team',
                            legend="Add A New Team")

@app.route('/delete_team/<int:id>', methods=['GET', 'POST'])
def delete_team(id):
    if request.method == 'POST': ####if its a POST request then delete the friend from the database
        team = Teams.query.get_or_404(id)
        db.session.delete(team)
        db.session.commit()
        flash("Team Deleted !!!")

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

    return render_template('details.html', team_id=id, listofplayers=player_of_specific_team, form=form, pageTitle='Details of Team', legend="Players who play for this Team")

@app.route('/updateteam/<int:id>', methods=['GET','POST'])
def update_team(id):
    team = Teams.query.get_or_404(id)
    form = TeamForm()

    if form.validate_on_submit():
        team.team_id = form.team_id.data
        team.team_name = form.team_name.data
        db.session.commit()
        flash("Team Updated Successfully!")
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
        flash("Player Added Successfully! Return to Details to view....")
        return redirect('/')

    return render_template('add_player.html', form=form,player_id=id, pageTitle='Add A New player',
                            legend="Add A New player")

@app.route('/delete_player/<int:id>', methods=['GET', 'POST'])
def delete_player(id):
    if request.method == 'POST': ####if its a POST request then delete the friend from the database
        player = Players.query.get_or_404(id)
        db.session.delete(player)
        db.session.commit()
        flash("Player Deleted !!!")

        return redirect('/')
    else: ######if its a GET request then send them to the home page
        return redirect("/")

@app.route('/updateplayer/<int:id>', methods=['GET','POST'])
def update_player(id):
    player = Players.query.get_or_404(id)
    form = PlayerForm()

    if form.validate_on_submit():
        player.player_id = form.player_id.data
        player.player_name = form.player_name.data
        db.session.commit()
        flash("Player Updated Successfully!")

        return redirect('/')

    form.player_id.data = player.player_id
    form.player_name.data = player.player_name
    return render_template('update_player.html', form=form, pageTitle='Update player', legend="Update A player")
