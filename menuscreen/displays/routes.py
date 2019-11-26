from flask import (render_template, request, url_for, flash, abort, jsonify, Blueprint)
from flask_login import current_user, login_required
from menuscreen import db
from menuscreen.models import (User, List_history, List_current, Wines, Winelist_current,
                                Beerscreen_settings, Winescreen_settings,
                                Eventscreen_settings, Itemscreen_settings, Template,
                                Font_size_options)
from menuscreen.displays.utils import _getTickerInfo, _getNumberOfBeerScreens
from menuscreen.settttings.utils import _getFontSizes, _getTemplates, _getSettings, _getNameFontSize, _getTemplateName, _getAbvFontSize, _getIbuFontSize, _getBreweryFontSize
from menuscreen.wine.utils import _getWinelistDisplay, _getWines, _getWinetypes, _convertToWinelist
from menuscreen.users.init_db_tables import getVenueId
import math

displays = Blueprint('displays', __name__)

# Update wine menu display
@displays.route('/_winemenu_list_display', methods=['GET', 'POST'])
@login_required
def _winemenu_list():

    # query to get types of wine
    wineTypes = _getWinetypes(current_user.id)
    # convert wineTypes to usable list
    wineTypelist = _convertToWinelist(wineTypes)
    # print(wineTypelist)

    # turn wineType list into array
    wineTypelistArr = []
    for wine in wineTypelist:
        # print("wineType: {}".format(wine['type']))
        wineTypelistArr.append(wine['type'])
    # print("")

    # get all the wines in the database
    totalWinelist = _getWines(current_user.id)
    # print(totalWinelist)
    # print("")

    # turn total winelist into usable array
    totalWinelistArr = []
    for wine in totalWinelist:
        # print("wineType: {}".format(wine.type))
        totalWinelistArr.append(wine.type)
    # print("")

    # print(wineTypelistArr)
    # print(totalWinelistArr)

    # filter out all the types of wines to use as a heading list to categorize the wines
    def filterTypes(listTypes):
        if(listTypes in totalWinelistArr):
            return True
        else:
            return False

    # filter the type of wines actually being used
    filteredTypes = filter(filterTypes, wineTypelistArr)

    # print("")
    # print(filteredTypes)
    # print("")

    # create a list of type of wines actually used
    typeList = []
    for ft in filteredTypes:
        typeList.append(ft)

    # print(typeList)

    winelist = totalWinelist
    data = {
        "wineTypelist": typeList,
        "winelist": winelist,
        "userData": {
            "venue_db_id": current_user.id
        }
    }
    return jsonify(data)



# query the DB ticker table
@displays.route('/getTickerInfo', methods=['GET', 'POST'])
# @login_required
def getTickerInfo():
    data = request.get_json()
    print("**************************************")
    print("******line 88*************************")
    print("displays. /_getTickerInfo")
    print("**************************************")
    print("data: {}".format(data))
    print("**************************************")
    print("**************************************")
    if (current_user.is_authenticated):
        print("LOGGED IN")
        print(current_user.id)

        data['userId'] = current_user.id
        print("data: {}".format(data))
        data = _getTickerInfo(data)

        tickerInfo = {}
        tickerInfo['id'] = data.id
        tickerInfo['ticker_text'] = data.ticker_text
        tickerInfo['ticker_screen_id'] = data.ticker_screen_id
        tickerInfo['tickery_type'] = data.ticker_type
    elif (data):
        print("NOT LOGGED IN")
        print(current_user_id)

        current_user_id = getVenueId(data['userName'])
        data['userId'] = current_user_id
        print("data: {}".format(data))
        data = _getTickerInfo(data)

        tickerInfo = {}
        tickerInfo['id'] = data.id
        tickerInfo['ticker_text'] = data.ticker_text
        tickerInfo['ticker_screen_id'] = data.ticker_screen_id
        tickerInfo['tickery_type'] = data.ticker_type
    else:
        print("NOT LOGGED IN AND NO URL INFO")
        tickerInfo = {}

    print("**************************************")
    print("**************************************")
    return jsonify(tickerInfo)

@displays.route('/_get_number_of_beer_screens', methods=['GET', 'POST'])
@login_required
def _get_number_of_beer_screens():
    numberOfScreens = _getNumberOfBeerScreens()
    print("*****************numberOfScreens*********************")
    print("numberOfScreens: {}".format(numberOfScreens))
    print("*****************************************************")
    return jsonify(numberOfScreens)

# Update screen display
@displays.route('/_screen_display', methods=['GET', 'POST'])
@login_required
def _screen_display():
    user = User.query.filter_by(id=current_user.id).first()
    beers = user.beerlist_current
    beers = db.session.query(
        List_history.id,
        List_history.name,
        List_history.style,
        List_history.abv,
        List_history.ibu,
        List_history.brewery,
        List_history.location,
        List_history.website,
        List_history.description,
        List_current.id,
        List_current.id_dropdown,
        ).join(List_current, List_history.id == List_current.id_history).all()

    beers = db.session.query(
        List_current.id,
        List_history.id,
        List_history.name,
        List_history.style,
        List_history.abv,
        List_history.ibu,
        List_history.brewery,
        List_history.location,
        List_history.website,
        List_history.description,
        List_current.id_dropdown,
        List_current.beer_of_month,
        List_current.coming_soon
        ).outerjoin(List_current, List_history.id == List_current.id_history
        ).filter(List_current.venue_db_id == current_user.id).all()

    beers = beers[0:22]
    beers_01_08 = beers[0:8]
    beers_08_16 = beers[8:16]
    beers_16_22 = beers[16:22]

    beerlist = []
    for b in beers:
        beer = {}
        beer['id'] = b.id,
        beer['name'] = b.name,
        beer['style'] = b.style
        beer['abv'] = b.abv
        beer['ibu'] = b.ibu
        beer['brewery'] = b.brewery
        beer['location'] = b.location
        beer['website'] = b.website
        beer['description'] = b.description
        beer['id_dropdown'] = b.id_dropdown
        beer['beer_of_month'] = b.beer_of_month
        beer['coming_coon'] = b.coming_soon
        beerlist.append(beer)

    # eventsDb = ("SELECT * FROM events WHERE venue_db_id={} ORDER BY time_of_event ASC").format(venuedbid)
    eventsDb = user.event_sort_asc
    # print(eventsDb)
    events = []
    for event in eventsDb:
        event = {
            "id" : event.id,
            "name" : event.name,
            "artist" : event.artist,
            "date_of_event ": str(event.date_of_event),
            "starttime_of_event" : str(event.starttime_of_event),
            "endtime_of_event" : str(event.endtime_of_event),
            "location" : event.location,
            "venue_db_id" : event.venue_db_id,
        }
        events.append(event)
    # print('events:{}'.format(events))

    # nameFontSize = _getNameFontSize(current_user.id, Font_size_options.id)
    # abvFontSize = _getAbvFontSize(current_user.id, Font_size_options.id)
    # ibuFontSize = _getIbuFontSize(current_user.id, Font_size_options.id)
    # breweryFontSize = _getBreweryFontSize(current_user.id, Font_size_options.id)

    # Get user settings
    datas = db.session.query(
                User_settings.id,
                User_settings.number_of_screens,
                User_settings.screen_number_settings,
                User_settings.font_color_one,
                User_settings.font_color_two,
                User_settings.font_color_three,
                User_settings.font_color_direction,
                User_settings.shadow_font_color_one,
                User_settings.shadow_font_color_two,
                User_settings.shadow_font_color_three,
                User_settings.shadow_font_color_direction,
                User_settings.background_color_one,
                User_settings.background_color_two,
                User_settings.background_color_three,
                User_settings.background_color_direction,
                User_settings.name_font_color,
                User_settings.abv_font_color,
                User_settings.ibu_font_color,
                User_settings.brewery_font_color,
                User_settings.name_font_size,
                User_settings.abv_font_size,
                User_settings.ibu_font_size,
                User_settings.brewery_font_size,
                User_settings.screen_template,
                User_settings.venue_db_id,
                Template.template_name,
                Font_size_options.font_sizes,
                ).join(Template, User_settings.screen_template == Template.id
                ).join(Font_size_options, User_settings.name_font_size == Font_size_options.id
                ).filter(User_settings.venue_db_id == current_user.id).first()

    userSettings = {}
    userSettings['id'] = datas.id
    userSettings['number_of_screens'] = datas.number_of_screens
    userSettings['screen_number_settings'] = datas.screen_number_settings
    userSettings['font_color_one'] = datas.font_color_one
    userSettings['font_color_two'] = datas.font_color_two
    userSettings['font_color_three'] = datas.font_color_three
    userSettings['font_color_direction'] = datas.font_color_direction
    userSettings['shadow_font_color_one'] = datas.shadow_font_color_one
    userSettings['shadow_font_color_two'] = datas.shadow_font_color_two
    userSettings['shadow_font_color_three'] = datas.shadow_font_color_three
    userSettings['shadow_font_color_direction'] = datas.shadow_font_color_direction
    userSettings['background_color_one'] = datas.background_color_one
    userSettings['background_color_two'] = datas.background_color_two
    userSettings['background_color_three'] = datas.background_color_three
    userSettings['background_color_direction'] = datas.background_color_direction
    userSettings['name_font_color'] = datas.name_font_color
    userSettings['abv_font_color'] = datas.abv_font_color
    userSettings['ibu_font_color'] = datas.ibu_font_color
    userSettings['brewery_font_color'] = datas.brewery_font_color
    userSettings['template_name'] = datas.template_name
    userSettings['font_sizes'] = datas.font_sizes
    userSettings['venue_db_id'] = datas.venue_db_id

    nameFontSize = _getNameFontSize(current_user.id, Font_size_options.id)
    abvFontSize = _getAbvFontSize(current_user.id, Font_size_options.id)
    ibuFontSize = _getIbuFontSize(current_user.id, Font_size_options.id)
    breweryFontSize = _getBreweryFontSize(current_user.id, Font_size_options.id)

    userSettings['nameFontSize'] = nameFontSize
    userSettings['abvFontSize'] = abvFontSize
    userSettings['ibuFontSize'] = ibuFontSize
    userSettings['breweryFontSize'] = breweryFontSize

    settings = [
        {
            "beers":beerlist,
            "events":events,
            "userSettings":userSettings,
        }
    ]

    # # print('THIS IS _screen_display')
    # for beer in settings[0]['beers']:
    #     print(beer['name'])
    # print(settings[0]['userSettings'])

    # END /_screen_display
    return jsonify(settings)


@displays.route('/_bottle_beers', methods=['GET', 'POST'])
@login_required
def _bottle_beers():
    user = User.query.filter_by(id=current_user.id).first()
    datas = user.beerlist_sort_asc
    beers = []
    for data in datas:
        beer = {
            "id" : data.id,
            "name" : data.name,
            "style" : data.style,
            "abv" : data.abv,
            "ibu" : data.ibu,
            "brewery" : data.brewery,
            "location" : data.location,
            "website" : data.website,
            "description" : data.description,
            "draft_bottle_selection" : data.draft_bottle_selection,
        }
        beers.append(beer)
    return jsonify(beers)

@displays.route('/_update', methods=['GET','POST'])
@login_required
def update():
    # queryStr = ("SELECT lc.id, lh.id, lh.name, lh.style, lh.abv, lh.ibu, lh.brewery, lh.location, lh.website, lh.description, lc.id_dropdown FROM list_history AS lh, list_current AS lc WHERE lh.id=lc.id_history AND lc.venue_db_id={}").format(venuedbid)
    datas = db.session.query(
                List_history.id,
                List_history.name,
                List_history.style,
                List_history.abv,
                List_history.ibu,
                List_history.brewery,
                List_history.location,
                List_history.website,
                List_history.description,
                List_history.draft_bottle_selection,
                List_current,
                ).join(List_history, List_current.id_history == List_history.id
                ).all()
    for data in datas:
        print(data)
    beers = []
    for data in datas:
        beer = {
            "id" : data.id,
            "name" : data.name,
            "style" : data.style,
            "abv" : data.abv,
            "ibu" : data.ibu,
            "brewery" : data.brewery,
            "location" : data.location,
            "website" : data.website,
            "description" : data.description,
            "draft_bottle_selection" : data.draft_bottle_selection,
        }
        beers.append(beer)
    beers_01_16 = beers[0:16]
    beers_17_22 = beers[16:22]
    return jsonify(
            {
                # "beers": beers,
                "beers_01_16": beers_01_16,
                "beers_17_22": beers_17_22,
            }
        )

@displays.route('/_updateBeers', methods=['GET','POST'])
@login_required
def updateBeers():
    user = User.query.filter_by(id=current_user.id).first()
    datas = user.beerlist_sort_asc
    beers = []
    for data in datas:
        beer = {
            "id" : data.id,
            "name" : data.name,
            "style" : data.style,
            "abv" : data.abv,
            "ibu" : data.ibu,
            "brewery" : data.brewery,
            "location" : data.location,
            "website" : data.website,
            "description" : data.description,
            "draft_bottle_selection" : data.draft_bottle_selection,
        }
        beers.append(beer)
    return jsonify(beers)

@displays.route('/_updateBeersDashboard', methods=['GET','POST'])
@login_required
def updateBeersDashboard():
    user = User.query.filter_by(id=current_user.id).first()
    datas = user.beerlist_sort_asc
    beers = []
    for data in datas:
        beer = {
            "id" : data.id,
            "name" : data.name,
            "style" : data.style,
            "abv" : data.abv,
            "ibu" : data.ibu,
            "brewery" : data.brewery,
            "location" : data.location,
            "website" : data.website,
            "description" : data.description,
            "draft_bottle_selection" : data.draft_bottle_selection,
        }
        beers.append(beer)
    return jsonify(beers)

@displays.route('/_searchBeerlist/<string:name>/', methods=['GET','POST'])
@login_required
def searchBeerlist(name):
    # MySQL query
    # queryStr = ("SELECT * FROM list_history WHERE name LIKE'"+ name +"%' AND venue_db_id={};").format(venuedbid)
    # ORM query equivalent to mysql query
    datas = db.session.query(List_history).filter(List_history.name.like('%' + name + '%'))
    beers = []
    for data in datas:
        beer = {
            "id" : data.id,
            "name" : data.name,
            "style" : data.style,
            "abv" : data.abv,
            "ibu" : data.ibu,
            "brewery" : data.brewery,
            "location" : data.location,
            "website" : data.website,
            "description" : data.description,
            "draft_bottle_selection" : data.draft_bottle_selection,
        }
        beers.append(beer)
    return jsonify(beers)

@displays.route('/_updateTappingNext', methods=['GET','POST'])
@login_required
def updateTappingNext():
    # Get Beer info
    # queryStr = ("SELECT lc.id, lh.id, lh.name, lh.style, lh.abv, lh.ibu, lh.brewery, lh.location, lh.website, lh.description FROM list_history AS lh, list_current AS lc WHERE lh.id=lc.id_on_next AND lc.venue_db_id={}").format(venuedbid)
    datas = db.session.query(
                List_history.id,
                List_history.name,
                List_history.style,
                List_history.abv,
                List_history.ibu,
                List_history.brewery,
                List_history.location,
                List_history.website,
                List_history.description,
                List_history.draft_bottle_selection,
                List_current,
                ).join(List_history, List_current.id_on_next == List_history.id
                ).all()
    for data in datas:
        print(data)
    beers = []
    for data in datas:
        beer = {
            "id" : data.id,
            "name" : data.name,
            "style" : data.style,
            "abv" : data.abv,
            "ibu" : data.ibu,
            "brewery" : data.brewery,
            "location" : data.location,
            "website" : data.website,
            "description" : data.description,
            "draft_bottle_selection" : data.draft_bottle_selection,
        }
        beers.append(beer)
    nextBeers = beers[0:16]
    return jsonify(
            {
                # "beers": beers,
                "nextBeers": nextBeers,
            }
        )

# Add untappd beer info to DB
@displays.route('/_addUntappd', methods=['GET','POST'])
@login_required
def addUntappd():
    data = request.get_json()
    print(data['id'])
    print(data['name'])
    print(data['style'])
    print(data['abv'])
    print(data['ibu'])
    print(data['brewery'])
    print(data['location'])
    print(data['website'])
    print(data['description'])
    print(data['draftbottleselection'])
    print('Beer ' + data['id'] + ': ' + data['name'] + ' has been added to the database. Thank you for playing along. Have a "hoppy" day.')

    name = data['name']
    style = data['style']
    abv = data['abv']
    ibu = data['ibu']
    brewery = data['brewery']
    location = data['location']
    website = data['website']
    description = data['description']
    draftBottle = data['draftbottleselection']

    # MySQL equivalent query
    # cur.execute("INSERT INTO list_history(name, style, abv, ibu, brewery, location, website, description, draft_bottle_selection, venue_db_id) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (name, style, abv, ibu, brewery, location, website, description, draftBottle, venuedbid))
    # ORM query
    List_history(
        name = data['name'],
        style = data['style'],
        abv = data['abv'],
        ibu = data['ibu'],
        brewery = data['brewery'],
        location = data['location'],
        website = data['website'],
        description = data['description'],
        draftBottle = data['draftbottleselection'],
        venue_db_id = current_user.id)

    return jsonify(data)


@displays.route('/beers_display_screen')
@login_required
def beers_display_screen():
    user = User.query.filter_by(id=current_user.id).first()
    beers = db.session.query(
        List_current.id,
        List_history.id,
        List_history.name,
        List_history.style,
        List_history.abv,
        List_history.ibu,
        List_history.brewery,
        List_history.location,
        List_history.website,
        List_history.description,
        List_current.id_dropdown,
        List_current.beer_of_month,
        List_current.coming_soon,
        ).outerjoin(List_current, List_history.id == List_current.id_history
        ).filter(List_current.venue_db_id == current_user.id).all()

    beerlist = []
    beerlistBom = []
    beerlistCs = []

    print("")
    for beer in beers:
        if not beer.beer_of_month and not beer.coming_soon:
            beerlist.append(beer)
        elif beer.beer_of_month and beer.coming_soon:
            beerlistBom.append(beer)
            beerlistCs.append(beer)
        elif beer.beer_of_month:
            beerlist.append(beer)
            beerlistBom.append(beer)
        elif beer.coming_soon:
            beerlistCs.append(beer)

    print("beerlist")
    for beer in beerlist:
        print(beer)
    print("beerlistBom")
    for beer in beerlistBom:
        print(beer)
    print("beerlistCs")
    for beer in beerlistCs:
        print(beer)
    print("")

    halflistNum = math.trunc((len(beerlist)/2))
    beerlistFirstHalf = beerlist[:halflistNum]
    beerlistSecondHalf = beerlist[halflistNum:]

    for beer in beerlistFirstHalf:
        print(beer)
    print("")

    for beer in beerlistSecondHalf:
        print(beer)
    print("")

    tickerText = _getTickerInfo(current_user.id).ticker_text
    print(tickerText)

    if len(beers) > 0:
        return render_template('beers_display_screen.html', beers=beers, beerlistFirstHalf=beerlistFirstHalf, beerlistSecondHalf=beerlistSecondHalf, beerlistBom=beerlistBom, beerlistCs=beerlistCs, tickerText=tickerText, currentUserId=current_user.id)
    else:
        msg = 'No Beers Found'
    return render_template('beers_display_screen.html', msg=msg, currentUserId=current_user.id)

@displays.route('/beers_display_screen/<string:venuename>/<string:screen_id>')
def beers_display_screen_nologin(venuename, screen_id):
    print('******************************************************************')
    print("venuename: {}".format(venuename))
    current_user_id = getVenueId(venuename)
    print("current_user_id: {}".format(current_user_id))
    print("screen_id: {}".format(screen_id))
    screenData = {
        "userId": current_user_id,
        "screenNumber": screen_id,
    }
    print('******************************************************************')

    user = User.query.filter_by(id=current_user_id).first()
    beers = db.session.query(
        List_current.id,
        List_history.id,
        List_history.name,
        List_history.style,
        List_history.abv,
        List_history.ibu,
        List_history.brewery,
        List_history.location,
        List_history.website,
        List_history.description,
        List_current.id_dropdown,
        List_current.beer_of_month,
        List_current.coming_soon,
        ).outerjoin(List_current, List_history.id == List_current.id_history
        ).filter(List_current.venue_db_id == current_user_id
        ).filter(List_current.beer_screen_id == screen_id
        ).all()

    beerlist = []
    beerlistBom = []
    beerlistCs = []

    print("")
    for beer in beers:
        if not beer.beer_of_month and not beer.coming_soon:
            beerlist.append(beer)
        elif beer.beer_of_month and beer.coming_soon:
            beerlistBom.append(beer)
            beerlistCs.append(beer)
        elif beer.beer_of_month:
            beerlist.append(beer)
            beerlistBom.append(beer)
        elif beer.coming_soon:
            beerlistCs.append(beer)

    print("")
    print("beerlist")
    for beer in beerlist:
        print(beer)
    print("")
    print("beerlistBom")
    for beer in beerlistBom:
        print(beer)
    print("")
    print("beerlistCs")
    for beer in beerlistCs:
        print(beer)
    print("")

    # halflistNum = math.trunc((len(beerlist)/2))
    halflistNum = math.ceil((len(beerlist)/2))
    # halflistNum = (len(beerlist)/2)
    print("halflistNum: {}".format(halflistNum))
    beerlistFirstHalf = beerlist[:halflistNum]
    beerlistSecondHalf = beerlist[halflistNum:]

    print("")
    print("beerlistFirstHalf")
    for beer in beerlistFirstHalf:
        print(beer)

    print("")
    print("beerlistSecondHalf")
    for beer in beerlistSecondHalf:
        print(beer)
    print("*******************************************************")
    print("*************LINE 668**********************************")
    print("*******************************************************")
    tickerText = _getTickerInfo(screenData).ticker_text
    print(tickerText)

    if len(beers) > 0:
        return render_template('beers_display_screen.html', beers=beers, beerlistFirstHalf=beerlistFirstHalf, beerlistSecondHalf=beerlistSecondHalf, beerlistBom=beerlistBom, beerlistCs=beerlistCs, tickerText=tickerText, currentUserId=current_user_id, beerlistScreenId=screen_id)
    else:
        msg = 'No Beers Found'
    return render_template('beers_display_screen.html', msg=msg, currentUserId=current_user_id, beerlistScreenId=screen_id)


@displays.route('/on_tap_next_display', methods=['GET','POST'])
@login_required
def on_tap_next_display():
    user = User.query.filter_by(id=current_user.id).first()
    currentBeers = user.beerlist_current
    currentBeers = db.session.query(
        List_history.id,
        List_history.name,
        List_history.style,
        List_history.abv,
        List_history.ibu,
        List_history.brewery,
        List_history.location,
        List_history.website,
        List_history.description,
        List_history.draft_bottle_selection,
        List_current.id_dropdown
        ).outerjoin(List_current, List_history.id == List_current.id_history
        ).filter(List_current.venue_db_id == current_user.id).all()

    beerlistLength = len(currentBeers)

    nextBeers = user.beerlist_current
    nextBeers = db.session.query(
        List_history.id,
        List_history.name,
        List_history.style,
        List_history.abv,
        List_history.ibu,
        List_history.brewery,
        List_history.location,
        List_history.website,
        List_history.description,
        List_history.draft_bottle_selection,
        List_current.id_dropdown
        ).outerjoin(List_current, List_history.id == List_current.id_on_next
        ).filter(List_current.venue_db_id == current_user.id).all()

    return render_template('on_tap_next_display.html', title='Tapping Next', legend='Tapping Next', currentUserId=current_user.id, currentBeers=currentBeers, nextBeers=nextBeers, beerlistLength=beerlistLength)


@displays.route('/bottle_beers', methods=['GET','POST'])
@login_required
def bottle_beers():
    user = User.query.filter_by(id=current_user.id).first()

    datas = user.beerlist_sort_asc

    datas = db.session.query(
        List_history.id,
        List_history.name,
        List_history.style,
        List_history.abv,
        List_history.ibu,
        List_history.brewery,
        List_history.location,
        List_history.website,
        List_history.description,
        List_history.draft_bottle_selection,
        ).filter(List_history.draft_bottle_selection != "Draft"
        ).filter(List_history.venue_db_id == current_user.id
        ).order_by(List_history.name.asc()
        ).all()

    beers = []
    for data in datas:
        beer = {
            "id" : data.id,
            "name" : data.name,
            "style" : data.style,
            "abv" : data.abv,
            "ibu" : data.ibu,
            "brewery" : data.brewery,
            "location" : data.location,
            "website" : data.website,
            "description" : data.description,
            "draft_bottle_selection" : data.draft_bottle_selection,
        }
        beers.append(beer)
    if len(beers) > 0:
        jsonify(beers);
        return render_template('bottle_beers.html', title='Bottle beers list', currentUserId=current_user.id, beers=beers)
    else:
        msg = 'No Beers Found!!!'
    return render_template('bottle_beers.html', title='Bottle beers list', currentUserId=current_user.id, msg=msg, beers=beers)

@displays.route('/bottle_beers/<string:venuename>/<string:screen_id>', methods=['GET','POST'])
def bottle_beers_nologin(venuename, screen_id):
    print('******************************************************************')
    print("venuename: {}".format(venuename))
    current_user_id = getVenueId(venuename)
    print("current_user_id: {}".format(current_user_id))
    print("screen_id: {}".format(screen_id))
    screenData = {
        "userId": current_user_id,
        "screenNumber": screen_id,
    }
    print('******************************************************************')
    # user = User.query.filter_by(id=current_user.id).first()
    # datas = user.beerlist_sort_asc

    datas = db.session.query(
        List_history.id,
        List_history.name,
        List_history.style,
        List_history.abv,
        List_history.ibu,
        List_history.brewery,
        List_history.location,
        List_history.website,
        List_history.description,
        List_history.draft_bottle_selection,
        ).filter(List_history.draft_bottle_selection != "Draft"
        ).filter(List_history.venue_db_id == screenData['userId']
        # ).filter(List_history.beer_screen_id == screenData['screenNumber']
        ).order_by(List_history.name.asc()
        ).all()

    beers = []
    for data in datas:
        beer = {
            "id" : data.id,
            "name" : data.name,
            "style" : data.style,
            "abv" : data.abv,
            "ibu" : data.ibu,
            "brewery" : data.brewery,
            "location" : data.location,
            "website" : data.website,
            "description" : data.description,
            "draft_bottle_selection" : data.draft_bottle_selection,
        }
        beers.append(beer)
    if len(beers) > 0:
        jsonify(beers);
        return render_template('bottle_beers.html', title='Bottle beers list', beers=beers, currentUserId=screenData['userId'], bottleBeersScreenId=screenData['screenNumber'])
    else:
        msg = 'No Beers Found!!!'
    return render_template('bottle_beers.html', title='Bottle beers list', msg=msg, beers=beers, currentUserId=screenData['userId'], bottleBeersScreenId=screenData['screenNumber'])

@displays.route('/draft_beers', methods=['GET', 'POST'])
@login_required
def draft_beers():
    user = User.query.filter_by(id=current_user.id).first()
    beers = db.session.query(
        List_current.id,
        List_history.id,
        List_history.name,
        List_history.style,
        List_history.abv,
        List_history.ibu,
        List_history.brewery,
        List_history.location,
        List_history.website,
        List_history.description,
        List_history.draft_bottle_selection,
        List_current.id_dropdown,
        List_current.beer_of_month,
        List_current.coming_soon,
        ).outerjoin(List_current, List_history.id == List_current.id_history
        ).filter(List_current.venue_db_id == current_user.id).all()

    print('THIS IS draft_beers\n')
    for beer in beers:
        print(beer)

    if len(beers) > 0:
        return render_template('draft_beers.html', title='Beer Print', legend='Beer Print', beers=beers, currentUserId=current_user.id)
    else:
        msg = 'No Beers Found'
    return render_template('draft_beers.html', msg=msg, currentUserId=current_user.id)

@displays.route('/draft_beers/<string:venuename>/<string:screen_id>', methods=['GET', 'POST'])
def draft_beers_nologin(venuename, screen_id):
    print('******************************************************************')
    print("venuename: {}".format(venuename))
    current_user_id = getVenueId(venuename)
    print("current_user_id: {}".format(current_user_id))
    print("screen_id: {}".format(screen_id))
    screenData = {
        "userId": current_user_id,
        "screenNumber": screen_id,
    }
    print('******************************************************************')
    user = User.query.filter_by(id=current_user_id).first()
    beers = db.session.query(
        List_current.id,
        List_history.id,
        List_history.name,
        List_history.style,
        List_history.abv,
        List_history.ibu,
        List_history.brewery,
        List_history.location,
        List_history.website,
        List_history.description,
        List_history.draft_bottle_selection,
        List_current.id_dropdown,
        List_current.beer_of_month,
        List_current.coming_soon,
        ).outerjoin(List_current, List_history.id == List_current.id_history
        ).filter(List_current.venue_db_id == current_user_id
        # ).filter(List_current.beer_screen_id == screen_id
        ).all()

    print('\nTHIS IS draft_beers\n')
    for beer in beers:
        print(beer)

    if len(beers) > 0:
        return render_template('draft_beers.html', title='Beer Print', legend='Beer Print', beers=beers, currentUserId=screenData['userId'], draftBeersScreenId=screenData['screenNumber'])
    else:
        msg = 'No Beers Found'
    return render_template('draft_beers.html', msg=msg,  currentUserId=screenData['userId'], draftBeersScreenId=screenData['screenNumber'])

@displays.route('/draft_beers_print', methods=['GET','POST'])
@login_required
def draft_beers_print():
    user = User.query.filter_by(id=current_user.id).first()
    beers = db.session.query(
        List_history.id,
        List_history.name,
        List_history.style,
        List_history.abv,
        List_history.ibu,
        List_history.brewery,
        List_history.location,
        List_history.website,
        List_history.description,
        List_history.draft_bottle_selection,
        List_current.id_dropdown,
        List_current.beer_of_month,
        List_current.coming_soon
        ).outerjoin(List_current, List_history.id == List_current.id_history
        ).filter(List_current.venue_db_id == current_user.id
        ).all()

    image_file = url_for('static', filename='img/profile_pics/' + current_user.image_file)
    if len(beers) > 0:
        return render_template('draft_beers_print.html', title='Beer Print', legend='Beer Print', beers=beers, image_file=image_file, currentUserId=current_user.id)
    else:
        msg = 'No Beers Found'
    return render_template('draft_beers_print.html', msg=msg, image_file=image_file, currentUserId=current_user.id)


@displays.route('/draft_beers_print/<string:venuename>/<string:screen_id>', methods=['GET','POST'])
def draft_beers_print_nologin(venuename, screen_id):
    print('******************************************************************')
    print("venuename: {}".format(venuename))
    current_user_id = getVenueId(venuename)
    print("current_user_id: {}".format(current_user_id))
    print("screen_id: {}".format(screen_id))
    screenData = {
        "userId": current_user_id,
        "screenNumber": screen_id,
    }
    print('******************************************************************')

    user = User.query.filter_by(id=current_user_id).first()
    beers = db.session.query(
        List_history.id,
        List_history.name,
        List_history.style,
        List_history.abv,
        List_history.ibu,
        List_history.brewery,
        List_history.location,
        List_history.website,
        List_history.description,
        List_history.draft_bottle_selection,
        List_current.id_dropdown,
        List_current.beer_of_month,
        List_current.coming_soon
        ).outerjoin(List_current, List_history.id == List_current.id_history
        ).filter(List_current.venue_db_id == current_user_id
        # ).filter(List_current.beerscreen_id == screen_id
        ).all()

    if len(beers) > 0:
        return render_template('draft_beers_print.html', title='Beer Print', legend='Beer Print', beers=beers, currentUserId=current_user_id)
    else:
        msg = 'No Beers Found'
    return render_template('draft_beers_print.html', msg=msg, currentUserId=current_user_id)
