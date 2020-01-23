from flask import (jsonify)
from flask_login import current_user, login_required
from menuscreen import db
from menuscreen.models import (User, List_history, List_current, Beerscreen_setting,
                            Ticker)
from menuscreen.settttings.utils import (_getBeerSize1, _getBeerPrice1,
                            _getBeerSize2, _getBeerPrice2,
                            _getBeerSize3, _getBeerPrice3,
                            _getBeerSize4, _getBeerPrice4)

def _deleteBeerscreenSettingByScreenId(data):
    print('Data: {}'.format(data))
    userId = data['id']
    screenId = data['screenId']
    screenSettingCandidate = Beerscreen_setting.query.filter_by(beer_settings_screen_id=screenId, venue_db_id=userId).first()
    if screenSettingCandidate.venue_db_id != current_user.id:
        abort(403)
    db.session.delete(screenSettingCandidate)
    db.session.commit()
    return jsonify(data)

def _deleteBeerFromListCurrentByScreenId(data):
    print('Data: {}'.format(data))
    userId = data['id']
    screenId = data['screenId']
    beerlistCurrent = List_current.query.filter_by(beer_screen_id=screenId, venue_db_id=userId).all()
    for b in beerlistCurrent:
        print(b)
        if b.venue_db_id != current_user.id:
            abort(403)
        db.session.delete(b)
        db.session.commit()
    return jsonify(data)

def _deleteBeertickerFromTickerByScreenId(data):
    print('Data: {}'.format(data))
    userId = data['id']
    screenId = data['screenId']
    tickerTypeId = data['tickerTypeId']
    tickerCandidate = Ticker.query.filter_by(ticker_screen_id=screenId, ticker_type=tickerTypeId, venue_db_id=userId).first()
    if tickerCandidate.venue_db_id != current_user.id:
        abort(403)
    db.session.delete(tickerCandidate)
    db.session.commit()
    return jsonify(data)




def getDefaultSelect(currentId):
    thisBeer = List_current.query.filter_by(id_dropdown=currentId, venue_db_id=current_user.id).first()
    return thisBeer

def getDefaultNextSelect(nextId):
    # result = cur.execute("SELECT id_on_next FROM list_current WHERE id_dropdown=%s AND venue_db_id=%s", [nextId, venuedbid])
    thisBeer = List_current.query.filter_by(id_dropdown=nextId, venue_db_id=current_user.id).first()
    return thisBeer

def _getCurrentBeerlist(screenData):
    print("screenData: {}".format(screenData))
    userId = screenData['userId']
    displayId = screenData['screenNumber']

    # user = User.query.filter_by(id=screenData).first()
    # beers = user.beerlist_current
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
        List_history.size_id_1,
        List_history.price_id_1,
        List_history.size_id_2,
        List_history.price_id_2,
        List_history.size_id_3,
        List_history.price_id_3,
        List_history.size_id_4,
        List_history.price_id_4,
        List_current.id,
        List_current.id_history,
        List_current.id_on_next,
        List_current.id_dropdown,
        List_current.beer_of_month,
        List_current.coming_soon,
        ).outerjoin(List_current, List_history.id == List_current.id_history
        ).filter(List_current.beer_screen_id == displayId
        ).filter(List_current.venue_db_id == userId
        ).order_by(List_current.id_dropdown.asc()
        ).all()
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
        beer['size_id_1'] = _getBeerSize1(userId, b.size_id_1)
        beer['price_id_1'] = _getBeerPrice1(userId, b.price_id_1)
        beer['size_id_2'] = _getBeerSize2(userId, b.size_id_2)
        beer['price_id_2'] = _getBeerPrice2(userId, b.price_id_2)
        beer['size_id_3'] = _getBeerSize3(userId, b.size_id_3)
        beer['price_id_3'] = _getBeerPrice3(userId, b.price_id_3)
        beer['size_id_4'] = _getBeerSize4(userId, b.size_id_4)
        beer['price_id_4'] = _getBeerPrice4(userId, b.price_id_4)
        beer['id_history'] = b.id_history
        beer['id_on_next'] = b.id_on_next
        beer['id_dropdown'] = b.id_dropdown
        beer['beer_of_month'] = b.beer_of_month
        beer['coming_soon'] = b.coming_soon
        beerlist.append(beer)
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # for b in beerlist:
    #     print("b: {} - {} - {} - {} - {}".format(b['id'], b['name'], b['style'], b['abv'], b['brewery']))
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    return beerlist

def _getOnTapNextBeerlist(screenData):
    print("screenData: {}".format(screenData))
    userId = screenData['userId']
    displayId = screenData['screenNumber']
    # user = User.query.filter_by(id=user_id).first()
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
        List_history.size_id_1,
        List_history.price_id_1,
        List_history.size_id_2,
        List_history.price_id_2,
        List_history.size_id_3,
        List_history.price_id_3,
        List_history.size_id_4,
        List_history.price_id_4,
        List_current.id,
        List_current.id_history,
        List_current.id_on_next,
        List_current.id_dropdown,
        ).outerjoin(List_current, List_history.id == List_current.id_on_next
        ).filter(List_current.beer_screen_id == displayId
        ).filter(List_current.venue_db_id == userId
        ).all()
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
        beer['size_id_1'] = _getBeerSize1(userId, b.size_id_1)
        beer['price_id_1'] = _getBeerPrice1(userId, b.price_id_1)
        beer['size_id_2'] = _getBeerSize2(userId, b.size_id_2)
        beer['price_id_2'] = _getBeerPrice2(userId, b.price_id_2)
        beer['size_id_3'] = _getBeerSize3(userId, b.size_id_3)
        beer['price_id_3'] = _getBeerPrice3(userId, b.price_id_3)
        beer['size_id_4'] = _getBeerSize4(userId, b.size_id_4)
        beer['price_id_4'] = _getBeerPrice4(userId, b.price_id_4)
        beer['id_history'] = b.id_history
        beer['id_on_next'] = b.id_on_next
        beer['id_dropdown'] = b.id_dropdown
        beerlist.append(beer)
        # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        # for b in beerlist:
        #     print("b: {} - {} - {} - {} - {}".format(b['id'], b['name'], b['style'], b['abv'], b['brewery']))
        # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    return beerlist

def _getTotalBeerlist(userId):
    print(userId)
    user = User.query.filter_by(id=userId).first()
    print(user)
    beers = user.beerlist_sort_asc
    # beers = db.session.query(
    #     List_history.id,
    #     List_history.name,
    #     List_history.style,
    #     List_history.abv,
    #     List_history.ibu,
    #     List_history.brewery,
    #     List_history.location,
    #     List_history.website,
    #     List_history.description,
    #     List_history.draft_bottle_selection,
    #     List_current.id,
    #     List_current.id_dropdown,
    #     ).outerjoin(List_current, List_history.id == List_current.id_history
    #     ).filter(List_current.venue_db_id == userId
    #     ).order_by(List_current.id_dropdown.asc()
    #     ).all()
    print(beers)
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
        beer['size_id_1'] = _getBeerSize1(userId, b.size_id_1)
        beer['price_id_1'] = _getBeerPrice1(userId, b.price_id_1)
        beer['size_id_2'] = _getBeerSize2(userId, b.size_id_2)
        beer['price_id_2'] = _getBeerPrice2(userId, b.price_id_2)
        beer['size_id_3'] = _getBeerSize3(userId, b.size_id_3)
        beer['price_id_3'] = _getBeerPrice3(userId, b.price_id_3)
        beer['size_id_4'] = _getBeerSize4(userId, b.size_id_4)
        beer['price_id_4'] = _getBeerPrice4(userId, b.price_id_4)
        beer['draft_bottle_selection'] = b.draft_bottle_selection
        # beer['id_dropdown'] = b.id_dropdown
        beerlist.append(beer)
    print(beerlist)
    return beerlist

def _addBeer(data, user_id):
    print('*******************************************************************************')
    print('*******************************************************************************')
    print('line 230 - data: {}'.format(data))
    print('*******************************************************************************')
    print('*******************************************************************************')
    newBeer = List_current(id_history=data['id_history'], id_on_next=data['id_on_next'], id_dropdown=data['id_dropdown'], beer_screen_id=data['beer_screen_id'], venue_db_id=user_id)
    db.session.add(newBeer)
    db.session.commit()
    return data

def _deleteBeer(data):
    print('*******************************************************************************')
    print('*******************************************************************************')
    print('line 241 utils.py _deleteBeer()')
    print('data: {}'.format(data))
    print('*******************************************************************************')
    print('*******************************************************************************')
    beer = List_current.query.filter_by(id_dropdown=data['beerIdToBeDeleted'], beer_screen_id=data['userNameScreenId']['screenNumber'], venue_db_id=data['userNameScreenId']['userId']).first()
    if beer.venue_db_id != current_user.id:
        abort(403)
    db.session.delete(beer)
    db.session.commit()
    return data


def _getBottleBeers(user_id):
    data = db.session.query(
        List_history.id,
        List_history.name,
        List_history.style,
        List_history.abv,
        List_history.ibu,
        List_history.brewery,
        List_history.location,
        List_history.website,
        List_history.description,
        List_history.size_id_1,
        List_history.price_id_1,
        List_history.size_id_2,
        List_history.price_id_2,
        List_history.size_id_3,
        List_history.price_id_3,
        List_history.size_id_4,
        List_history.price_id_4,
        List_history.draft_bottle_selection,
        ).filter(List_history.draft_bottle_selection != "Draft"
        ).filter(List_history.venue_db_id == user_id
        ).order_by(List_history.name.asc()
        ).all()

    beerlist = []
    for b in data:
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
        beer['size_id_1'] = _getBeerSize1(b.size_id_1)
        beer['price_id_1'] = _getBeerPrice1(b.price_id_1)
        beer['size_id_2'] = _getBeerSize2(b.size_id_2)
        beer['price_id_2'] = _getBeerPrice2(b.price_id_2)
        beer['size_id_3'] = _getBeerSize3(b.size_id_3)
        beer['price_id_3'] = _getBeerPrice3(b.price_id_3)
        beer['size_id_4'] = _getBeerSize4(b.size_id_4)
        beer['price_id_4'] = _getBeerPrice4(b.price_id_4)
        beer['draft_bottle_selection'] = b.draft_bottle_selection
        beerlist.append(beer)
    return beerlist

def addNewBeerToDB(data, user_id):
    print(data)
    print(user_id)
    user = User.query.filter_by(id=user_id).first()
    newBeer = List_history(name=data['name'],style=data['style'],abv=data['abv'],ibu=data['ibu'],brewery=data['brewery'],location=data['location'],website=data['website'],description=data['description'],draft_bottle_selection=data['draftBottle'],venue_db_id=user_id)
    db.session.add(newBeer)
    db.session.commit()
