from flask_login import current_user
from sqlalchemy import and_
from menuscreen import db
from menuscreen.models import User, Wines, Winelist_current, Wine_type

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
    return wines

def _getWines(id):
    wines = db.session.query(
        Wines.id,
        Wines.name,
        Wines.location,
        Wines.description,
        Wines.glass,
        Wines.bottle,
        Wines.varietal,
        Wines.foodPairings,
        Wines.website,
        Wine_type.type
        ).outerjoin(Wine_type, Wines.type == Wine_type.id
        ).filter(Wines.venue_db_id == id
        # ).filter(Wines.venue_db_id == current_user.id
        ).order_by(Wines.name.asc()
        ).all()
    return wines

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
