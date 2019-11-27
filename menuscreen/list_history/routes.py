from flask import (render_template, url_for, flash, redirect,
                    request, abort, jsonify, Blueprint, make_response)
from flask_login import current_user, login_required
from menuscreen import db
from menuscreen.models import (User, List_history, List_current, Font_size_options,
                        Beerscreen_settings, Winescreen_settings, Eventscreen_settings,
                        Itemscreen_settings, Template, Ticker, Ticker_type_id)
from menuscreen.list_history.forms import BeerForm, CurrentBeerListForm, NextBeerListForm
from menuscreen.list_history.utils import (getDefaultSelect, getDefaultNextSelect,
                        _getTotalBeerlist, _getCurrentBeerlist, _getOnTapNextBeerlist,
                        _addBeer, _deleteBeer, _getBottleBeers, addNewBeerToDB,
                        _deleteBeerscreenSettingByScreenId, _deleteBeerFromListCurrentByScreenId,
                        _deleteBeertickerFromTickerByScreenId)
from menuscreen.settttings.utils import _getFontSizes, _getTemplates, _getSettings, _getNameFontSize, _getTemplateName, _getAbvFontSize, _getIbuFontSize, _getBreweryFontSize
from menuscreen.users.init_db_tables import (getVenueId, initBeerscreenSettings,
                        initListCurrent, initTickerSingleTicker)

from menuscreen import pusher_client

import json

list_history = Blueprint('list_history', __name__)

@list_history.route('/_init_new_beerscreen_settings', methods=['GET', 'POST'])
@login_required
def _init_new_beerscreen_settings():
    screenId = request.get_json()
    # print(screenId)
    screenData = {
        "id": current_user.id,
        "screenId": screenId,
    }
    # print(screenData)
    # init list_current with new beer for new screen
    initListCurrent(screenData)
    # init beerscreen_settings with new setting for new screen
    initBeerscreenSettings(screenData)
    # ticker type id used for puting right ticker in 1=beer, 2=wine, 3=event, 4=item
    screenData['tickerTypeId']=1
    initTickerSingleTicker(screenData)
    return jsonify(screenData)

@list_history.route('/_remove_beerscreen_settings', methods=['GET', 'POST'])
@login_required
def _remove_beerscreen_settings():
    screenId = request.get_json()
    screenData = {
        "id": current_user.id,
        "screenId": screenId,
    }
    print("screenData: {}".format(screenData))
    _deleteBeerscreenSettingByScreenId(screenData)
    _deleteBeerFromListCurrentByScreenId(screenData)
    screenData['tickerTypeId']=1
    _deleteBeertickerFromTickerByScreenId(screenData)
    return jsonify(screenData)



@list_history.route('/_add_update_ui', methods=['GET','POST'])
# @login_required
def _add_update_ui():
    # print("***********************************************")
    # print("***********************************************")
    # print("***********************************************")
    settings = {
        "venue_db_id": current_user.id,
        "updated": True,
    }
    # print(settings)
    # print("***********************************************")
    # print("***********************************************")
    # print("***********************************************")


    ######################################
    #PUSHER
    pusher_client.trigger('my-update-channel', 'new-addUpdate-event', { 'message': settings })
    #PUSHER
    #######################################
    return jsonify(settings)

@list_history.route('/_delete_update_ui', methods=['GET','POST'])
@login_required
def _delete_update_ui():
    settings = {
        "venue_db_id": current_user.id,
        "updated": True,
    }

    ######################################
    #PUSHER
    pusher_client.trigger('my-update-channel', 'new-deleteUpdate-event', { 'message': settings })
    #PUSHER
    #######################################
    return jsonify(settings)

@list_history.route('/_getBottleBeerlist', methods=['GET', 'POST'])
# @login_required
def _getBottleBeerlist():
    data = request.get_json()
    print("**************************************")
    print("******LINE  103***********************")
    print("list_history. /_getBottleBeers")
    print("**************************************")
    print("data: {}".format(data))
    print("**************************************")
    print("**************************************")
    if (current_user.is_authenticated):
        # print("LOGGED IN")
        # print(current_user.id)
        bottleBeerlist = _getBottleBeers(current_user.id)
        data = {
        "beerlist": bottleBeerlist,
        "venue_db_id": current_user.id
        }
    elif (data):
        current_user_id = getVenueId(data['userName'])
        # print("NOT LOGGED IN")
        # print(data['userName'])
        # print(current_user_id)
        bottleBeerlist = _getBottleBeers(current_user_id)
        data = {
            "beerlist": bottleBeerlist,
            "venue_db_id": current_user_id
        }
    else:
        # print("NOT LOGGED IN AND NO URL INFO")
        data = {}
    # print("**************************************")
    # print("**************************************")
    return jsonify(data)

@list_history.route('/_getTotBeerlist', methods=['GET', 'POST'])
# @login_required
def _getTotBeerlist():
    data = request.get_json()
    print("**************************************")
    print("*********** LINE 136 *****************")
    print("list_history. /_getTotBeerlist")
    print("**************************************")
    print("data: {}".format(data))
    print("**************************************")
    print("**************************************")
    if (current_user.is_authenticated):
        print("LOGGED IN")
        print(current_user.id)
        beerlist = _getTotalBeerlist(current_user.id)
        print(beerlist)
        data = {
        "beerlist": beerlist,
        "venue_db_id": current_user.id
        }
    elif (data):
        print("NOT LOGGED IN")
        current_user_id = getVenueId(data['userName'])
        print(data['userName'])
        print(current_user_id)
        beerlist = _getTotalBeerlist(current_user_id)
        data = {
            "beerlist": beerlist,
            "venue_db_id": current_user_id
        }
    else:
        print("NOT LOGGED IN AND NO URL INFO")
        data = {}
    print("**************************************")
    print("**************************************")
    return jsonify(data)

@list_history.route('/_getCurBeerlist', methods=['GET', 'POST'])
# @login_required
def _getCurBeerlist():
    data = request.get_json()
    print("**************************************")
    print("******LINE  175***********************")
    print("list_history. /_getCurBeerlist")
    print("**************************************")
    print("data: {}".format(data))
    print("**************************************")
    print("**************************************")
    if (current_user.is_authenticated):
        print("LOGGED IN")
        print(current_user.id)

        data['userId'] = current_user.id
        print("data: {}".format(data))
        beerlist = _getCurrentBeerlist(data)
        # beerlist = _getCurrentBeerlist(current_user.id)
        print(beerlist)
    elif (data):
        print("NOT LOGGED IN")
        print(data['userName'])
        current_user_id = getVenueId(data['userName'])
        print(current_user_id)

        data['userId'] = current_user_id
        print("data: {}".format(data))
        beerlist = _getCurrentBeerlist(data)
    else:
        print("NOT LOGGED IN AND NO URL INFO")
        beerlist = {}
    print("**************************************")
    print("**************************************")
    return jsonify(beerlist)

@list_history.route('/_getNextBeerlist', methods=['GET', 'POST'])
# @login_required
def _getNextBeerlist():
    data = request.get_json()
    print("**************************************")
    print("******LINE  212***********************")
    print("list_history. /_getOnTapNextBeerlist")
    print("**************************************")
    print("data: {}".format(data))
    print("**************************************")
    print("**************************************")
    if (current_user.is_authenticated):
        print("LOGGED IN")
        print(current_user.id)
        data['userId'] = current_user.id
        print(data)
        beerlist = _getOnTapNextBeerlist(data)
        # beerlist = _getOnTapNextBeerlist(current_user.id)
        print(beerlist)
    elif (data):
        print("NOT LOGGED IN")
        print(data['userName'])
        current_user_id = getVenueId(data['userName'])
        print(current_user_id)

        data['userId'] = current_user_id
        print(data)
        beerlist = _getOnTapNextBeerlist(current_user_id)
    else:
        print("NOT LOGGED IN AND NO URL INFO")
        beerlist = {}
    print("**************************************")
    print("**************************************")
    return jsonify(beerlist)

@list_history.route('/_addNewBeerToDB', methods=['GET', 'POST'])
@login_required
def _addNewBeerToDB():
    # print("currentRoute: '/_addNewBeerToDB'")
    data = request.get_json()
    addNewBeerToDB(data, current_user.id)

    return jsonify({
        "venue_db_id": current_user.id,
        "updated": "true",
        "currentRoute": "_addNewBeerToDB",
    })


@list_history.route('/_add_beer_to_list', methods=['GET', 'POST'])
@login_required
def _add_beer_to_list():
    data = request.get_json()
    # print('*******************************************************************************')
    # print('*******************************************************************************')
    # print('data: {}'.format(data))
    # print('*******************************************************************************')
    # print('*******************************************************************************')
    _addBeer(data, current_user.id)

    data = {
        "venue_db_id": current_user.id,
        "updated": "true",
    }
    return jsonify(data)

@list_history.route('/_delete_beer_from_current_list', methods=['POST'])
@login_required
def _delete_beer_from_current_list():
    data = request.get_json()
    print("**************************************")
    print("******LINE  278***********************")
    print("users. /_delete_beer_from_current_list")
    print("**************************************")
    print("data: {}".format(data))
    print("beerIdToBeDeleted: {}".format(data['beerIdToBeDeleted']))
    print("**************************************")
    print("**************************************")
    data['userNameScreenId']['userId'] = current_user.id

    if data['beerIdToBeDeleted'] > 1:
        _deleteBeer(data)
    flash('The beer has been deleted!', 'success')
    # return redirect(url_for('list_history.edit_beer_list'))
    return data

@list_history.route('/_getAllTotalCurrentNextLists', methods=['GET','POST'])
@login_required
def _getAllTotalCurrentNextLists():
    data = "DATA GOES HERE"
    user = User.query.filter_by(id=current_user.id).first()
    datas = user.beerlist_sort_asc
    selectBeerlist = []
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
        selectBeerlist.append(beer)
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
        List_current.id_history,
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
        List_current.id_on_next,
        List_current.id_dropdown
        ).outerjoin(List_current, List_history.id == List_current.id_on_next
        ).filter(List_current.venue_db_id == current_user.id).all()

    settings = {
        "venue_db_id": current_user.id,
        "updated": True,
        # "data": data
    }
    # data = {
    #     "selectBeerlist": selectBeerlist,
    #     "currentBeers": currentBeers,
    #     "nextBeers": nextBeers
    # }
    #
    print(settings)
    # #######################################
    # #PUSHER
    # pusher_client.trigger('my-update-channel', 'new-nextUpdate-event', {'message': settings})
    # #PUSHER
    # #######################################

    return jsonify({
        "result": "true",
        "data": data
    })




@list_history.route('/add_beer', methods=['GET', 'POST'])
@login_required
def add_beer():
    form = BeerForm()
    form.draftBottle.data = "Draft"
    if request.method == 'POST':
    # if form.validate_on_submit():
        list = List_history(name=form.name.data, style=form.style.data, abv=form.abv.data,
            ibu=form.ibu.data, brewery=form.brewery.data, location=form.location.data,
            website=form.website.data, description=form.description.data,
            draft_bottle_selection=request.form['draftBottle'], venue_db_id=current_user.id)
        db.session.add(list)
        db.session.commit()

        settings = {
            "venue_db_id": current_user.id,
            "updated": True,
        }

        #######################################
        #PUSHER
        pusher_client.trigger('myAddBeer-event-channel', 'addBeerToDb-event', {'message': settings})
        #PUSHER
        #######################################


        flash('Beer has been created and added to the list!','success')
        return redirect(url_for('list_history.beer_dashboard'))
    return render_template('add_beer.html', title='Add Beer', legend='Add Beer', form=form)

@list_history.route('/beer_dashboard')
@login_required
def beer_dashboard():
    user = User.query.filter_by(id=current_user.id).first()
    beers = user.beerlist_sort_asc
    for beer in beers:
        beer.dash_menu_id = list(beer.name)[0].lower()
    if beers:
        return render_template('beer_dashboard.html', title='Dashboard', legend='Dashboard', beers=beers)
    else:
        msg = 'Sorry, no beers found in beerlist!'
    return render_template('beer_dashboard.html', title='Dashboard', legend='Dashboard', msg=msg)

@list_history.route('/edit_beer/<string:beer_id>', methods=['GET', 'POST'])
@login_required
def edit_beer(beer_id):
    beer = List_history.query.get_or_404(beer_id)
    if beer.venue_db_id != current_user.id:
        abort(403)
    form = BeerForm()
    if form.validate_on_submit():
        beer.name = form.name.data
        beer.style = form.style.data
        beer.abv = form.abv.data
        beer.ibu = form.ibu.data
        beer.brewery = form.brewery.data
        beer.location = form.location.data
        beer.website = form.website.data
        beer.description = form.description.data
        beer.draft_bottle_selection = form.draftBottle.data
        db.session.commit()

        settings = {
            "venue_db_id": current_user.id,
            "updated": True,
        }

        #######################################
        #PUSHER
        pusher_client.trigger('myEditBeer-evemt-channel', 'editBeerToDb-event', {'message': settings})
        #PUSHER
        #######################################

        flash('Beer has been updated!', 'success')
        return redirect(url_for('list_history.beer_dashboard'))
    elif request.method == 'GET':
        form.name.data = beer.name
        form.style.data = beer.style
        form.abv.data = beer.abv
        form.ibu.data = beer.ibu
        form.brewery.data = beer.brewery
        form.location.data = beer.location
        form.website.data = beer.website
        form.description.data = beer.description
        form.draftBottle.data = beer.draft_bottle_selection

    return render_template('edit_beer.html', title='Edit Beer: '+ beer_id, legend='Edit Beer '+ beer_id, form=form)

@list_history.route('/delete_beer/<string:beer_id>', methods=['POST'])
@login_required
def delete_beer(beer_id):
    beer = List_history.query.get_or_404(beer_id)
    if beer.venue_db_id != current_user.id:
        abort(403)
    db.session.delete(beer)
    db.session.commit()
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
        List_history.draft_bottle_selection,
        List_current.id_dropdown
        ).outerjoin(List_current, List_history.id == List_current.id_history
        ).filter(List_current.venue_db_id == current_user.id).all()

    settings = {
        "venue_db_id": current_user.id,
        "updated": True,
    }
    #######################################
    #PUSHER
    pusher_client.trigger('myDelBeer-evemt-channel', 'delBeerFromDb-event', {'message': settings})
    #PUSHER
    #######################################

    flash('The beer has been deleted!', 'success')
    return redirect(url_for('list_history.beer_dashboard'))

@list_history.route('/edit_beer_list', methods=['GET', 'POST'])
@login_required
def edit_beer_list():

    beerscreenSettings = db.session.query(
        Beerscreen_settings.beer_settings_screen_id
    ).filter(Beerscreen_settings.venue_db_id == current_user.id
    ).all()
    beerscreenSettingsIds = []
    for data in beerscreenSettings:
        beerscreenSettingsIds.append(data[0])

    user = User.query.filter_by(id=current_user.id).first()
    datas = user.beerlist_sort_asc
    beersDropdown = []
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
            "venue_db_id" : data.venue_db_id,
        }
        beersDropdown.append(beer)


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
        List_history.venue_db_id,
        List_current.id,
        List_current.id_dropdown,
        List_current.beer_of_month,
        List_current.coming_soon,
        ).outerjoin(List_current, List_history.id == List_current.id_history
        ).filter(List_current.venue_db_id == current_user.id
        ).filter(List_current.beer_screen_id == 1
        ).order_by(List_current.id.asc()
        ).all()

    beerlist = []
    for b in beers:
        beer = {}
        beer['id'] = b.id
        beer['name'] = b.name
        beer['style'] = b.style
        beer['abv'] = b.abv
        beer['ibu'] = b.ibu
        beer['brewery'] = b.brewery
        beer['location'] = b.location
        beer['website'] = b.website
        beer['description'] = b.description
        beer['draft_bottle_selection'] = b.draft_bottle_selection
        beer['venue_db_id'] = b.venue_db_id
        beer['id_dropdown'] = b.id_dropdown
        beer['defaultDropdown'] = getDefaultSelect(b.id_dropdown)
        beerlist.append(beer)

    # for b in beerlist:
        # print(b['defaultDropdown'].beer_of_month)
        # print(b['defaultDropdown'].id_history )

    # beerselect = []
    # for i, b in enumerate(beerlist):
        # print('i = {}, '.format(i), b['id_dropdown'], b['name'], b['id'])
    #     beerselect.append(getDefaultSelect(b['id_dropdown']))
    #
    # for b in beerselect:
        # print(b.id_history)

    tickerInfo = db.session.query(
        Ticker.id,
        Ticker.ticker_text,
        Ticker.ticker_screen_id,
        Ticker.venue_db_id,
        Ticker_type_id.ticker_type
    ).join(Ticker_type_id, Ticker_type_id.ticker_type_id_fk == Ticker.ticker_type
    ).filter(Ticker.venue_db_id == current_user.id
    ).first()
    if (tickerInfo):
        tickerText = tickerInfo.ticker_text
    else:
        tickerText = ''
        newTicker = Ticker(ticker_text='', tickerscreen_id='1', venue_db_id=current_user.id)
        db.session.add(newTicker)
        db.session.commit()

    if request.method == 'POST':
        rdata = request.form

        print(rdata)
        print(len(rdata))

        newData = rdata.copy()
        tickerText = newData.popitem()[1]
        print(tickerText)

        beerCandidateList = []

        for i, (key, value) in enumerate(rdata.items()):
            print(key)
            if key != 'ticker-text':
                print(key, value)
                beerCandidate = {
                    "id_dropdown": "",
                    "id_history": "",
                    "bom": "",
                    "cs": ""
                }
                print(i+1 , key, value)
                splitData = key.split('_')
                print(splitData)

                splitKeyName = splitData[0]
                splitKeyIter = splitData[1]


                if splitKeyName == 'beer':
                    beerCandidate['id_dropdown'] = splitKeyIter
                    beerCandidate['id_history'] = value
                    beerCandidate['bom'] = 0
                    beerCandidate['cs'] = 0

                    print(beerCandidate)

                    beerCandidateList.append(beerCandidate)


        for i, (key, value) in enumerate(rdata.items()):

            if key != 'ticker-text':
                print(i+1 , key, value)
                splitData = key.split('_')
                splitKeyName = splitData[0]
                splitKeyIter = splitData[1]
                splitKeyIterNum = int(splitKeyIter)

                if splitKeyName == 'beer-of-month':
                    print(splitKeyName + "_" + splitKeyIter + " ---- value= " + value)
                    print(splitKeyIter)
                    print(splitKeyIterNum-1)
                    print(beerCandidateList[splitKeyIterNum-1]['bom'])
                    if value != "":
                        beerCandidateList[splitKeyIterNum-1]['bom'] = True
                    else:
                        beerCandidateList[splitKeyIterNum-1]['bom'] = False
                elif splitKeyName == 'coming-soon':
                    print(splitKeyName + "_" + splitKeyIter + " ---- value= " + value)
                    print(splitKeyIter)
                    print(splitKeyIterNum-1)
                    print(beerCandidateList[splitKeyIterNum-1]['cs'])
                    if value != "":
                        beerCandidateList[splitKeyIterNum-1]['cs'] = True
                    else:
                        beerCandidateList[splitKeyIterNum-1]['cs'] = False

        # for b in beerCandidateList:
            print(b)

        beerCandidate = List_current.query.filter_by(id_dropdown=1, venue_db_id=current_user.id).first()
        print("beerCandidate: {}".format(beerCandidate))

        for x in range(1, len(beerCandidateList) + 1, 1):
            beerCandidate = List_current.query.filter_by(id_dropdown=x, venue_db_id=current_user.id).first()
            print("beerCandidate: {}".format(beerCandidate))
            beerCandidate.id_history = beerCandidateList[x-1]['id_history']
            beerCandidate.beer_of_month = beerCandidateList[x-1]['bom']
            beerCandidate.coming_soon = beerCandidateList[x-1]['cs']
            db.session.commit()

        if (tickerInfo):
            # print(tickerText)
            tickerCandidate = Ticker.query.filter_by(venue_db_id=current_user.id).first()
            tickerCandidate.ticker_text = tickerText
            db.session.commit()

        settings = {
            "venue_db_id": current_user.id,
            "updated": True,
        }
        ######################################
        #PUSHER
        pusher_client.trigger('my-event-channel', 'new-event', { 'message': settings })
        #PUSHER
        #######################################


    return render_template('edit_beer_list.html', title='Testing', legend='Testing', currentUserId=current_user.id, beersDropdown=beersDropdown, beerlist=beerlist, tickerText=tickerText, beerscreenSettingsIds=beerscreenSettingsIds)



@list_history.route('/testing_pusher_beerlist', methods=['GET','POST'])
@login_required
def testing_pusher_beerlist():

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

    if request.method == "POST":

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
            List_current.beer_of_month,
            List_current.coming_soon,
            ).outerjoin(List_current, List_history.id == List_current.id_history
            ).filter(List_current.venue_db_id == current_user.id).all()
        # beers = beers[0:22]
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
            beer['coming_soon'] = b.coming_soon
            beerlist.append(beer)
        print(beerlist)

        eventsDb = user.event_sort_asc
        print(eventsDb)
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

        print('events:{}'.format(events))

        nameFontSize = _getNameFontSize(current_user.id, Font_size_options.id)
        abvFontSize = _getAbvFontSize(current_user.id, Font_size_options.id)
        ibuFontSize = _getIbuFontSize(current_user.id, Font_size_options.id)
        breweryFontSize = _getBreweryFontSize(current_user.id, Font_size_options.id)

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
        userSettings['venue_db_id'] = datas.venue_db_id
        # userSettings['font_sizes'] = datas.font_sizes

        userSettings['nameFontSize'] = nameFontSize
        userSettings['abvFontSize'] = abvFontSize
        userSettings['ibuFontSize'] = ibuFontSize
        userSettings['breweryFontSize'] = breweryFontSize

        settings = {
            "beers":beerlist,
            "events":events,
            "userSettings":userSettings,
        }

        # print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        # print("BEGIN EDIT BEERLIST list_history")
        # print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        # print("^^^^^^^^^^^^BEGIN BEERS^^^^^^^^^^")
        # for beer in settings['beers']:
        #     print(beer['name'])
        # print("^^^^^^^^^^^^END BEERS^^^^^^^^^^")
        # print("")
        # print("^^^^^^^^^^^^BEGIN EVENTS^^^^^^^^^^")
        # for event in settings['events']:
        #     print(event)
        # print("^^^^^^^^^^^^END EVENTS^^^^^^^^^^")
        # print("")
        # print("^^^^^^^^^^^^BEGIN USERSETTINGS^^^^^^^^^^")
        # print(settings['userSettings'])
        # print("^^^^^^^^^^^^END USERSETTINGS^^^^^^^^^^")
        # print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        # print("END EDIT BEERLIST list_history")
        # print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

        settings = json.dumps(settings)
        # print(settings)

        # ######################################
        # #PUSHER
        # pusher_client.trigger('my-event-channel', 'new-event', {
        #     'message': settings
        # })
        # #PUSHER
        # #######################################

        flash('Beer List Updated', 'success')
        return redirect(url_for('list_history.testing_pusher_beerlist'))
    return render_template('testing_pusher_beerlist.html', title='Testing Beer List', legend='Testing Beer List', beers=beers)

































@list_history.route('/on_tap_next_editor', methods=['GET','POST'])
@login_required
def on_tap_next_editor():
    user = User.query.filter_by(id=current_user.id).first()
    datas = user.beerlist_sort_asc
    selectBeerlist = []
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
        selectBeerlist.append(beer)
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
        List_current.id_history,
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
        List_current.id_on_next,
        List_current.id_dropdown
        ).outerjoin(List_current, List_history.id == List_current.id_on_next
        ).filter(List_current.venue_db_id == current_user.id).all()


    if request.method == 'POST':
        data = request.form

        for x in range(1, beerlistLength + 1, 1):
            beer = request.form['beer_{}'.format(x)]
            # print(beer)
            beerCandidate = List_current.query.filter_by(id_dropdown=x, venue_db_id=current_user.id).first()
            beerCandidate.id_on_next = beer
            db.session.commit()

        settings = {
            "venue_db_id": current_user.id,
            "updated": True,
            # "data": data
        }
        #######################################
        #PUSHER
        pusher_client.trigger('my-update-channel', 'new-nextUpdate-event', {'message': settings})
        #PUSHER
        #######################################


        flash('Next Beer list updated', 'success')
        return redirect(url_for('list_history.on_tap_next_editor'))
    return render_template('on_tap_next_editor.html', title='Tapping Next', legend='Tapping Next Editor', currentUserId=current_user.id, selectBeerlist=selectBeerlist, currentBeers=currentBeers, nextBeers=nextBeers, beerlistLength=beerlistLength)



# Search beers from untappd
@list_history.route('/beersearch', methods=['GET','POST'])
@login_required
def beersearch():
    return render_template('beersearch.html', currentUserId=current_user.id)
