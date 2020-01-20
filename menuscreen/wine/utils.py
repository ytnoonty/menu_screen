from flask_login import current_user
from sqlalchemy import and_
from menuscreen import db
from menuscreen.models import User, Wine, Winelist_current, Wine_type

def getDefaultCurrentWinelist(id):
    user = User.query.filter_by(id=current_user.id).first()
    # print('user: {}'.format(user))
    # print('user.id: {}'.format(user.id))

    wine = Winelist_current.query.filter_by(venue_db_id=user.id, id_dropdown=id).first()
    # print('wine: {}'.format(wine))
    # print('id_wine: {}'.format(wine.id_wine))
    return wine

def _getWinelistDisplay(id):
    user = User.query.filter_by(id=current_user.id).first()
    wines = user.winelist_current
    wines = db.session.query(
        Wine.name,
        Wine.location,
        Wine.description,
        Wine.glass,
        Wine.bottle,
        Wine.varietal,
        Wine.food_pairings,
        Wine.website,
        Winelist_current.id_dropdown
        ).outerjoin(Winelist_current, Wine.id == Winelist_current.id_wine
        ).filter(Winelist_current.venue_db_id == current_user.id
        ).order_by(Winelist_current.id_dropdown.asc()
        ).all()
    return wines

def _getWine(id):
    wines = db.session.query(
        Wine.id,
        Wine.name,
        Wine.location,
        Wine.description,
        Wine.glass,
        Wine.bottle,
        Wine.varietal,
        Wine.food_pairings,
        Wine.website,
        Wine_type.type
        ).outerjoin(Wine_type, Wine.type == Wine_type.id
        ).filter(Wine.venue_db_id == id
        # ).filter(Wine.venue_db_id == current_user.id
        ).order_by(Wine.name.asc()
        ).all()
    # print(wines)
    winelist = []
    for w in wines:
        # print(w)
        # print("")
        # print(type(w.id))
        wine = {}
        wine['id'] = w.id
        wine['name'] = w.name
        wine['location'] = w.location
        wine['description'] = w.description
        wine['glass'] = w.glass
        wine['bottle'] = w.bottle
        wine['varietal'] = w.varietal
        wine['food_pairings'] = w.food_pairings
        wine['website'] = w.website
        wine['type'] = w.type
        winelist.append(wine)
    return winelist

def _getWinetypes(id):
    # user = User.query.filter_by(id=current_user.id).first()
    wineTypes = db.session.query(
        Wine_type.id,
        Wine_type.type
        ).order_by(Wine_type.type.asc()
        ).all()
    wineTypes = db.session.query(
        Wine_type.id,
        Wine_type.type,
        ).filter(Wine_type.venue_db_id == id
        # ).filter(Wine_type.venue_db_id == current_user.id
        ).order_by(Wine_type.type.asc()
        ).all()
    return wineTypes

def _convertToWinelist(dataList):
    wineTypes = []
    for data in dataList:
        wineType = {
            "id" : data.id,
            "type" : data.type
        }
        wineTypes.append(wineType)
    return wineTypes
