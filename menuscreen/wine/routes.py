from flask import (render_template, url_for, flash, redirect,
                    request, abort, json, jsonify, Blueprint)
from flask_login import current_user, login_required
from menuscreen import db
from menuscreen.models import User, Wines, Winelist_current, Wine_type
from menuscreen.wine.forms import WineForm, CurrentWinelistForm, WineTypeForm
from menuscreen.wine.utils import getDefaultCurrentWinelist, _getWinelistDisplay, _getWines, _getWinetypes, _convertToWinelist
from menuscreen.users.init_db_tables import getVenueId

from menuscreen import pusher_client

wine = Blueprint('wine', __name__)

# Get all wines from db
@wine.route('/_getwines', methods=['GET','POST'])
@login_required
def _getwines():
    user = User.query.filter_by(id=current_user.id).first()
    datas = user.winelist_sort_asc
    wines = []
    for data in datas:
        wine = {
            "id":data.id,
            "name":data.name,
            "varietal":data.varietal,
            "type":data.type,
            "location":data.location,
            "glass":data.glass,
            "bottle":data.bottle,
            "description":data.description,
            "foodPairings":data.foodPairings,
            "website":data.website,
        }
        wines.append(wine)
    return jsonify(wines)


# Get current all wines from db
@wine.route('/_getCurrentWinelist', methods=['GET','POST'])
@login_required
def _getCurrentWinelist():
    # user = User.query.filter_by(id=current_user.id).first()
    # result = cur.execute("SELECT wl.name, wl.location, wl.description, wl.glass, wl.bottle, wl.varietal, wl.foodPairings FROM winelist_current AS wc, wines AS wl WHERE wl.id=wc.id_wine AND wl.venue_db_id=wc.venue_db_id AND wc.venue_db_id=%s", [venuedbid])

    user = User.query.filter_by(id=current_user.id).first()
    data = user.winelist_current
    data = db.session.query(
        Wines.name,
        Wines.location,
        Wines.description,
        Wines.glass,
        Wines.bottle,
        Wines.varietal,
        Wines.foodPairings,
        Wines.website,
        Winelist_current.id_dropdown
        ).outerjoin(Winelist_current, Wines.id == Winelist_current.id_wine
        ).filter(Winelist_current.venue_db_id == current_user.id
        ).order_by(Winelist_current.id_dropdown.asc()
        ).all()

    return jsonify(data)

# Add wine type
@wine.route('/add_wine_type', methods=['GET', 'POST'])
@login_required
def add_wine_type():
    form = WineTypeForm(request.form)
    rdata = _getWinetypes(current_user.id)
    wineTypes = _convertToWinelist(rdata)

    form.wineTypeSelect.choices = [(wineType['id'], wineType['type']) for wineType in wineTypes]
    if form.validate_on_submit():
        reqData = request.form['wineType']
        wineType = Wine_type(type=reqData, venue_db_id=current_user.id)
        db.session.add(wineType)
        db.session.commit()
        return redirect(url_for('wine.add_wine_type'))

    return render_template('add_wine_type.html', title='Edit Wine Type', legend='Edit Wine Type', form=form)


# Add Wine
@wine.route('/add_wine', methods=['GET', 'POST'])
@login_required
def add_wine():
    form = WineForm(request.form)

    user = User.query.filter_by(id=current_user.id).first()
    datas = db.session.query(
        Wine_type.id,
        Wine_type.type,
        ).filter(Wine_type.venue_db_id == current_user.id
        ).order_by(Wine_type.type.asc()
        ).all()
    print(datas)
    typelist = []
    for data in datas:
        type = {
            "id" : data.id,
            "type" : data.type
        }
        typelist.append(type)

    types = typelist

    form.type.choices = [(type['id'], type['type']) for type in types]

    if request.method == 'POST' and form.validate():
        # SQLAlchemy to add to database
        wine = Wines(name=form.name.data,
            location=form.location.data,
            varietal=form.varietal.data,
            type=form.type.data,
            glass=form.glass.data,
            bottle=form.bottle.data,
            description=form.description.data,
            foodPairings=form.foodPairings.data,
            website=form.website.data,
            venue_db_id=current_user.id)
        db.session.add(wine)
        db.session.commit()

        settings = {
            "venue_db_id": current_user.id,
            "updated": True,
        }
        #######################################
        #PUSHER
        pusher_client.trigger('wine-event-channel', 'add-wine-event', {'message': settings})
        #PUSHER
        #######################################

        flash('Wine Created', 'success')
        return redirect(url_for('wine.wine_dashboard'))
    return render_template('add_wine.html', title='Add Wine', legend='Add Wine', form=form)

# Wine menu
@wine.route('/wine_dashboard', methods=['GET', 'POST'])
@login_required
def wine_dashboard():
    # wines = Wines.query.all()
    user = User.query.filter_by(id=current_user.id).first()
    wines = user.winelist_sort_asc
    for wine in wines:
        wine.dash_menu_id = list(wine.name)[0].lower()
    if wines:
        return render_template('wine_dashboard.html', title='Wine Dashboard', wines=wines)
    else:
        msg = 'Sorry, sad day. No wine found in your winelist!'
    return render_template('wine_dashboard.html', title='Wine Dashboard', legend='Wine Dashboard', msg=msg)

# Edit wine
@wine.route('/edit_wine/<string:wine_id>', methods=['GET', 'POST'])
@login_required
def edit_wine(wine_id):
    wine = Wines.query.get_or_404(wine_id)
    if wine.venue_db_id != current_user.id:
        abort(403)
    # Get form
    form = WineForm(request.form,
        type = wine.type
    )

    rdata = _getWinetypes(current_user.id)
    wineTypes = _convertToWinelist(rdata)
    form.type.choices = [(type['id'], type['type']) for type in wineTypes]

    if form.validate_on_submit():
    # if request.method == 'POST':
        wine.name = form.name.data
        wine.location = form.location.data
        wine.varietal = form.varietal.data
        wine.type = form.type.data
        wine.glass = form.glass.data
        wine.bottle = form.bottle.data
        wine.description = form.description.data
        wine.foodPairings = form.foodPairings.data
        wine.website = form.website.data
        db.session.add(wine)
        db.session.commit()

        settings = {
            "venue_db_id": current_user.id,
            "updated": True,
        }

        #######################################
        #PUSHER
        pusher_client.trigger('wine-event-channel', 'edit-wine-event', {'message': settings})
        #PUSHER
        #######################################

        flash('Wine Updated!!!', 'success')
        return redirect(url_for('wine.wine_dashboard'))

    elif request.method == 'GET':
        rdata = _getWinetypes(current_user.id)
        wineTypes = _convertToWinelist(rdata)
        # # print(wineTypes)
        # for x in wineTypes:
        #     print("x['type']: {}".format(x['type']))
        #
        # print("wine.type: {}".format(wine.type))

        # Populate wine form fields
        # Populate the type select with values from the DB
        form.type.data = wine.type
        form.type.choices = [(type['id'], type['type']) for type in wineTypes]
        form.name.data = wine.name
        form.location.data = wine.location
        form.varietal.data = wine.varietal
        form.glass.data = wine.glass
        form.bottle.data = wine.bottle
        form.description.data = wine.description
        form.foodPairings.data = wine.foodPairings
        form.website.data = wine.website

    return render_template('edit_wine.html', title='Edit Wine', legend='Edit Wine', form=form)

# Delete wine
@wine.route('/delete_wine/<string:wine_id>', methods=['POST'])
@login_required
def delete_wine(wine_id):

    wine = Wines.query.get_or_404(wine_id)
    if wine.venue_db_id != current_user.id:
        abort(403)
    db.session.delete(wine)
    db.session.commit()

    # Flash message
    flash('Wine Deleted!!!', 'success')
    return redirect(url_for('wine.wine_dashboard'))


# Winelist editor
@wine.route('/winelist_editor', methods=['GET','POST'])
@login_required
def winelist_editor():

    user = User.query.filter_by(id=current_user.id).first()
    datas = user.winelist_sort_asc
    wines = []
    for data in datas:
        wine = {
            "id":data.id,
            "name":data.name,
            "varietal":data.varietal,
            "location":data.location,
            "glass":data.glass,
            "bottle":data.bottle,
            "description":data.description,
            "foodPairings":data.foodPairings,
            "website":data.website,
        }
        wines.append(wine)

    wine1select = getDefaultCurrentWinelist('1')
    wine2select = getDefaultCurrentWinelist('2')
    wine3select = getDefaultCurrentWinelist('3')
    wine4select = getDefaultCurrentWinelist('4')
    wine5select = getDefaultCurrentWinelist('5')
    wine6select = getDefaultCurrentWinelist('6')
    wine7select = getDefaultCurrentWinelist('7')
    wine8select = getDefaultCurrentWinelist('8')
    wine9select = getDefaultCurrentWinelist('9')
    wine10select = getDefaultCurrentWinelist('10')
    wine11select = getDefaultCurrentWinelist('11')
    wine12select = getDefaultCurrentWinelist('12')
    wine13select = getDefaultCurrentWinelist('13')
    wine14select = getDefaultCurrentWinelist('14')
    wine15select = getDefaultCurrentWinelist('15')
    wine16select = getDefaultCurrentWinelist('16')
    wine17select = getDefaultCurrentWinelist('17')
    wine18select = getDefaultCurrentWinelist('18')
    wine19select = getDefaultCurrentWinelist('19')
    wine20select = getDefaultCurrentWinelist('20')
    wine21select = getDefaultCurrentWinelist('21')
    wine22select = getDefaultCurrentWinelist('22')
    wine23select = getDefaultCurrentWinelist('23')
    wine24select = getDefaultCurrentWinelist('24')
    wine25select = getDefaultCurrentWinelist('25')
    wine26select = getDefaultCurrentWinelist('26')
    wine27select = getDefaultCurrentWinelist('27')
    wine28select = getDefaultCurrentWinelist('28')

    form = CurrentWinelistForm(request.form,
        wine1=wine1select.id_wine,
        wine2=wine2select.id_wine,
        wine3=wine3select.id_wine,
        wine4=wine4select.id_wine,
        wine5=wine5select.id_wine,
        wine6=wine6select.id_wine,
        wine7=wine7select.id_wine,
        wine8=wine8select.id_wine,
        wine9=wine9select.id_wine,
        wine10=wine10select.id_wine,
        wine11=wine11select.id_wine,
        wine12=wine12select.id_wine,
        wine13=wine13select.id_wine,
        wine14=wine14select.id_wine,
        wine15=wine15select.id_wine,
        wine16=wine16select.id_wine,
        wine17=wine17select.id_wine,
        wine18=wine18select.id_wine,
        wine19=wine19select.id_wine,
        wine20=wine20select.id_wine,
        wine21=wine21select.id_wine,
        wine22=wine22select.id_wine,
        wine23=wine23select.id_wine,
        wine24=wine24select.id_wine,
        wine25=wine25select.id_wine,
        wine26=wine26select.id_wine,
        wine27=wine27select.id_wine,
        wine28=wine28select.id_wine
    )

    form.wine1.choices = [(wine['id'], wine['name'] + ' - ' + wine['varietal']) for wine in wines]
    form.wine2.choices = [(wine['id'], wine['name'] + ' - ' + wine['varietal']) for wine in wines]
    form.wine3.choices = [(wine['id'], wine['name'] + ' - ' + wine['varietal']) for wine in wines]
    form.wine4.choices = [(wine['id'], wine['name'] + ' - ' + wine['varietal']) for wine in wines]
    form.wine5.choices = [(wine['id'], wine['name'] + ' - ' + wine['varietal']) for wine in wines]
    form.wine6.choices = [(wine['id'], wine['name'] + ' - ' + wine['varietal']) for wine in wines]
    form.wine7.choices = [(wine['id'], wine['name'] + ' - ' + wine['varietal']) for wine in wines]
    form.wine8.choices = [(wine['id'], wine['name'] + ' - ' + wine['varietal']) for wine in wines]
    form.wine9.choices = [(wine['id'], wine['name'] + ' - ' + wine['varietal']) for wine in wines]
    form.wine10.choices = [(wine['id'], wine['name'] + ' - ' + wine['varietal']) for wine in wines]
    form.wine11.choices = [(wine['id'], wine['name'] + ' - ' + wine['varietal']) for wine in wines]
    form.wine12.choices = [(wine['id'], wine['name'] + ' - ' + wine['varietal']) for wine in wines]
    form.wine13.choices = [(wine['id'], wine['name'] + ' - ' + wine['varietal']) for wine in wines]
    form.wine14.choices = [(wine['id'], wine['name'] + ' - ' + wine['varietal']) for wine in wines]
    form.wine15.choices = [(wine['id'], wine['name'] + ' - ' + wine['varietal']) for wine in wines]
    form.wine16.choices = [(wine['id'], wine['name'] + ' - ' + wine['varietal']) for wine in wines]
    form.wine17.choices = [(wine['id'], wine['name'] + ' - ' + wine['varietal']) for wine in wines]
    form.wine18.choices = [(wine['id'], wine['name'] + ' - ' + wine['varietal']) for wine in wines]
    form.wine19.choices = [(wine['id'], wine['name'] + ' - ' + wine['varietal']) for wine in wines]
    form.wine20.choices = [(wine['id'], wine['name'] + ' - ' + wine['varietal']) for wine in wines]
    form.wine21.choices = [(wine['id'], wine['name'] + ' - ' + wine['varietal']) for wine in wines]
    form.wine22.choices = [(wine['id'], wine['name'] + ' - ' + wine['varietal']) for wine in wines]
    form.wine23.choices = [(wine['id'], wine['name'] + ' - ' + wine['varietal']) for wine in wines]
    form.wine24.choices = [(wine['id'], wine['name'] + ' - ' + wine['varietal']) for wine in wines]
    form.wine25.choices = [(wine['id'], wine['name'] + ' - ' + wine['varietal']) for wine in wines]
    form.wine26.choices = [(wine['id'], wine['name'] + ' - ' + wine['varietal']) for wine in wines]
    form.wine27.choices = [(wine['id'], wine['name'] + ' - ' + wine['varietal']) for wine in wines]
    form.wine28.choices = [(wine['id'], wine['name'] + ' - ' + wine['varietal']) for wine in wines]


    if form.validate_on_submit():
        for x in range(1, 29, 1):
            wine = request.form['wine{}'.format(x)]
            wineCandidate = Winelist_current.query.filter_by(id_dropdown=x, venue_db_id=current_user.id).first()
            wineCandidate.id_wine = wine
            db.session.commit()

        wines = _getWinelistDisplay(current_user.id)

        settings = {
            "venue_db_id": current_user.id,
            "updated": True,
            # "winelist": wines
        }

        # settings = json.dumps(settings)

        #######################################
        #PUSHER
        pusher_client.trigger('wine-event-channel', 'new-wine-event', {'message': settings})
        #PUSHER
        #######################################

        # Flash success message on the screen
        flash('Winelist Updated!!!', 'success')
        return redirect(url_for('wine.winelist_editor'))

    return render_template('winelist_editor.html', title='Winelist Editor', legend='Winelist Editor', form=form, wines=wines)

# Winelist editor
@wine.route('/testing_winelist_editor', methods=['GET','POST'])
@login_required
def testing_winelist_editor():

    user = User.query.filter_by(id=current_user.id).first()
    datas = _getWines(current_user.id)
    wines = []
    for data in datas:
        wine = {
            "id":data.id,
            "name":data.name,
            "varietal":data.varietal,
            "location":data.location,
            "glass":data.glass,
            "bottle":data.bottle,
            "description":data.description,
            "foodPairings":data.foodPairings,
            "website":data.website,
        }
        wines.append(wine)

    for wine in wines:
        print(wine)

    # wine1select = getDefaultCurrentWinelist('1')
    # wine2select = getDefaultCurrentWinelist('2')
    # wine3select = getDefaultCurrentWinelist('3')
    # wine4select = getDefaultCurrentWinelist('4')
    # wine5select = getDefaultCurrentWinelist('5')
    # wine6select = getDefaultCurrentWinelist('6')
    # wine7select = getDefaultCurrentWinelist('7')
    # wine8select = getDefaultCurrentWinelist('8')
    # wine9select = getDefaultCurrentWinelist('9')
    # wine10select = getDefaultCurrentWinelist('10')
    # wine11select = getDefaultCurrentWinelist('11')
    # wine12select = getDefaultCurrentWinelist('12')
    # wine13select = getDefaultCurrentWinelist('13')
    # wine14select = getDefaultCurrentWinelist('14')
    # wine15select = getDefaultCurrentWinelist('15')
    # wine16select = getDefaultCurrentWinelist('16')
    # wine17select = getDefaultCurrentWinelist('17')
    # wine18select = getDefaultCurrentWinelist('18')
    # wine19select = getDefaultCurrentWinelist('19')
    # wine20select = getDefaultCurrentWinelist('20')
    # wine21select = getDefaultCurrentWinelist('21')
    # wine22select = getDefaultCurrentWinelist('22')
    # wine23select = getDefaultCurrentWinelist('23')
    # wine24select = getDefaultCurrentWinelist('24')
    # wine25select = getDefaultCurrentWinelist('25')
    # wine26select = getDefaultCurrentWinelist('26')
    # wine27select = getDefaultCurrentWinelist('27')
    # wine28select = getDefaultCurrentWinelist('28')
    #
    # form = CurrentWinelistForm(request.form,
    #     wine1=wine1select.id_wine,
    #     wine2=wine2select.id_wine,
    #     wine3=wine3select.id_wine,
    #     wine4=wine4select.id_wine,
    #     wine5=wine5select.id_wine,
    #     wine6=wine6select.id_wine,
    #     wine7=wine7select.id_wine,
    #     wine8=wine8select.id_wine,
    #     wine9=wine9select.id_wine,
    #     wine10=wine10select.id_wine,
    #     wine11=wine11select.id_wine,
    #     wine12=wine12select.id_wine,
    #     wine13=wine13select.id_wine,
    #     wine14=wine14select.id_wine,
    #     wine15=wine15select.id_wine,
    #     wine16=wine16select.id_wine,
    #     wine17=wine17select.id_wine,
    #     wine18=wine18select.id_wine,
    #     wine19=wine19select.id_wine,
    #     wine20=wine20select.id_wine,
    #     wine21=wine21select.id_wine,
    #     wine22=wine22select.id_wine,
    #     wine23=wine23select.id_wine,
    #     wine24=wine24select.id_wine,
    #     wine25=wine25select.id_wine,
    #     wine26=wine26select.id_wine,
    #     wine27=wine27select.id_wine,
    #     wine28=wine28select.id_wine
    # )
    #
    # form.wine1.choices = [(wine['id'], wine['name'] + ' - ' + wine['varietal']) for wine in wines]
    # form.wine2.choices = [(wine['id'], wine['name'] + ' - ' + wine['varietal']) for wine in wines]
    # form.wine3.choices = [(wine['id'], wine['name'] + ' - ' + wine['varietal']) for wine in wines]
    # form.wine4.choices = [(wine['id'], wine['name'] + ' - ' + wine['varietal']) for wine in wines]
    # form.wine5.choices = [(wine['id'], wine['name'] + ' - ' + wine['varietal']) for wine in wines]
    # form.wine6.choices = [(wine['id'], wine['name'] + ' - ' + wine['varietal']) for wine in wines]
    # form.wine7.choices = [(wine['id'], wine['name'] + ' - ' + wine['varietal']) for wine in wines]
    # form.wine8.choices = [(wine['id'], wine['name'] + ' - ' + wine['varietal']) for wine in wines]
    # form.wine9.choices = [(wine['id'], wine['name'] + ' - ' + wine['varietal']) for wine in wines]
    # form.wine10.choices = [(wine['id'], wine['name'] + ' - ' + wine['varietal']) for wine in wines]
    # form.wine11.choices = [(wine['id'], wine['name'] + ' - ' + wine['varietal']) for wine in wines]
    # form.wine12.choices = [(wine['id'], wine['name'] + ' - ' + wine['varietal']) for wine in wines]
    # form.wine13.choices = [(wine['id'], wine['name'] + ' - ' + wine['varietal']) for wine in wines]
    # form.wine14.choices = [(wine['id'], wine['name'] + ' - ' + wine['varietal']) for wine in wines]
    # form.wine15.choices = [(wine['id'], wine['name'] + ' - ' + wine['varietal']) for wine in wines]
    # form.wine16.choices = [(wine['id'], wine['name'] + ' - ' + wine['varietal']) for wine in wines]
    # form.wine17.choices = [(wine['id'], wine['name'] + ' - ' + wine['varietal']) for wine in wines]
    # form.wine18.choices = [(wine['id'], wine['name'] + ' - ' + wine['varietal']) for wine in wines]
    # form.wine19.choices = [(wine['id'], wine['name'] + ' - ' + wine['varietal']) for wine in wines]
    # form.wine20.choices = [(wine['id'], wine['name'] + ' - ' + wine['varietal']) for wine in wines]
    # form.wine21.choices = [(wine['id'], wine['name'] + ' - ' + wine['varietal']) for wine in wines]
    # form.wine22.choices = [(wine['id'], wine['name'] + ' - ' + wine['varietal']) for wine in wines]
    # form.wine23.choices = [(wine['id'], wine['name'] + ' - ' + wine['varietal']) for wine in wines]
    # form.wine24.choices = [(wine['id'], wine['name'] + ' - ' + wine['varietal']) for wine in wines]
    # form.wine25.choices = [(wine['id'], wine['name'] + ' - ' + wine['varietal']) for wine in wines]
    # form.wine26.choices = [(wine['id'], wine['name'] + ' - ' + wine['varietal']) for wine in wines]
    # form.wine27.choices = [(wine['id'], wine['name'] + ' - ' + wine['varietal']) for wine in wines]
    # form.wine28.choices = [(wine['id'], wine['name'] + ' - ' + wine['varietal']) for wine in wines]


    if request.method == "POST":
        for x in range(1, 29, 1):
            wine = request.form['wine{}'.format(x)]
            wineCandidate = Winelist_current.query.filter_by(id_dropdown=x, venue_db_id=current_user.id).first()
            wineCandidate.id_wine = wine
            db.session.commit()

        wines = _getWinelistDisplay(current_user.id)

        settings = {
            "venue_db_id": current_user.id,
            "updated": True,
            # "winelist": wines
        }

        # settings = json.dumps(settings)

        #######################################
        #PUSHER
        pusher_client.trigger('wine-event-channel', 'new-wine-event', {'message': settings})
        #PUSHER
        #######################################

        # Flash success message on the screen
        flash('Winelist Updated!!!', 'success')
        return redirect(url_for('wine.testing_winelist_editor'))

    return render_template('testing_winelist_editor.html', title='Winelist Editor', legend='Winelist Editor', wines=wines)


# winelist menu
@wine.route('/winelist_menu')
@login_required
def winelist_menu():
    # query to get types of wine
    wineTypes = _getWinetypes(current_user.id)
    # convert wineTypes to usable list
    wineTypelist = _convertToWinelist(wineTypes)
    # print(wineTypelist)

    # turn wineType list into array
    wineTypelistArr = []
    for wine in wineTypelist:
        print("wineType: {}".format(wine['type']))
        wineTypelistArr.append(wine['type'])
    print("")

    # get all the wines in the database
    totalWinelist = _getWines(current_user.id)
    print(totalWinelist)
    print("")

    # turn total winelist into usable array
    totalWinelistArr = []
    for wine in totalWinelist:
        print("wineType: {}".format(wine.type))
        totalWinelistArr.append(wine.type)
    print("")

    print(wineTypelistArr)
    print(totalWinelistArr)

    # filter out all the types of wines to use as a heading list to categorize the wines
    def filterTypes(listTypes):
        if(listTypes in totalWinelistArr):
            return True
        else:
            return False

    # filter the type of wines actually being used
    filteredTypes = filter(filterTypes, wineTypelistArr)

    print("")
    print(filteredTypes)
    print("")

    # create a list of type of wines actually used
    typeList = []
    for ft in filteredTypes:
        typeList.append(ft)

    print(typeList)

    winelist = totalWinelist
    return render_template('winelist_menu.html', title='Winelist Menu',
    wineTypelist=typeList,
    winelist=winelist,
    currentUserId=current_user.id)

# winelist menu
@wine.route('/winelist_menu/<string:venuename>/<string:screen_id>')
def winelist_menu_nologin(venuename, screen_id):
    # get user ID from venue name
    current_user_id = getVenueId(venuename)
    # query to get types of wine
    wineTypes = _getWinetypes(current_user_id)
    # convert wineTypes to usable list
    wineTypelist = _convertToWinelist(wineTypes)
    # print(wineTypelist)

    # turn wineType list into array
    wineTypelistArr = []
    for wine in wineTypelist:
        print("wineType: {}".format(wine['type']))
        wineTypelistArr.append(wine['type'])
    print("")

    # get all the wines in the database
    totalWinelist = _getWines(current_user_id)
    print(totalWinelist)
    print("")

    # turn total winelist into usable array
    totalWinelistArr = []
    for wine in totalWinelist:
        print("wineType: {}".format(wine.type))
        totalWinelistArr.append(wine.type)
    print("")

    print(wineTypelistArr)
    print(totalWinelistArr)

    # filter out all the types of wines to use as a heading list to categorize the wines
    def filterTypes(listTypes):
        if(listTypes in totalWinelistArr):
            return True
        else:
            return False

    # filter the type of wines actually being used
    filteredTypes = filter(filterTypes, wineTypelistArr)

    print("")
    print(filteredTypes)
    print("")

    # create a list of type of wines actually used
    typeList = []
    for ft in filteredTypes:
        typeList.append(ft)

    print(typeList)

    winelist = totalWinelist
    return render_template('winelist_menu.html', title='Winelist Menu',
    wineTypelist=typeList,
    winelist=winelist,
    currentUserId=current_user_id)





# winelist description menu
@wine.route('/winelist_description')
@login_required
def winelist_description():
    wineTypes = _getWinetypes(current_user.id)
    wineTypelist = _convertToWinelist(wineTypes)
    print(wineTypelist)

    wineTypelistArr = []
    for wine in wineTypelist:
        print("wineType: {}".format(wine['type']))
        wineTypelistArr.append(wine['type'])
    print("")

    totalWinelist = _getWines(current_user.id)
    print(totalWinelist)
    print("")

    totalWinelistArr = []
    for wine in totalWinelist:
        print("wineType: {}".format(wine.type))
        totalWinelistArr.append(wine.type)
    print("")

    print(wineTypelistArr)
    print(totalWinelistArr)

    def filterTypes(listTypes):

        if(listTypes in totalWinelistArr):
            return True
        else:
            return False

    filteredTypes = filter(filterTypes, wineTypelistArr)

    print("")
    print(filteredTypes)
    print("")

    typeList = []
    for ft in filteredTypes:
        typeList.append(ft)

    print(typeList)

    winelist = totalWinelist
    return render_template('winelist_description.html', title='Winelist Description',
    wineTypelist=typeList,
    winelist=winelist,
    currentUserId=current_user.id)


# winelist description menu
@wine.route('/winelist_description/<string:venuename>/<string:screen_id>')
def winelist_description_nologin(venuename, screen_id):
    # get user ID from venue name
    current_user_id = getVenueId(venuename)
    wineTypes = _getWinetypes(current_user_id)
    wineTypelist = _convertToWinelist(wineTypes)
    print(wineTypelist)

    wineTypelistArr = []
    for wine in wineTypelist:
        print("wineType: {}".format(wine['type']))
        wineTypelistArr.append(wine['type'])
    print("")

    totalWinelist = _getWines(current_user_id)
    print(totalWinelist)
    print("")

    totalWinelistArr = []
    for wine in totalWinelist:
        print("wineType: {}".format(wine.type))
        totalWinelistArr.append(wine.type)
    print("")

    print(wineTypelistArr)
    print(totalWinelistArr)

    def filterTypes(listTypes):

        if(listTypes in totalWinelistArr):
            return True
        else:
            return False

    filteredTypes = filter(filterTypes, wineTypelistArr)

    print("")
    print(filteredTypes)
    print("")

    typeList = []
    for ft in filteredTypes:
        typeList.append(ft)

    print(typeList)

    winelist = totalWinelist
    return render_template('winelist_description.html', title='Winelist Description',
    wineTypelist=typeList,
    winelist=winelist,
    currentUserId=current_user_id)
