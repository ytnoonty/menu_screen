from flask import Response, Blueprint
from menuscreen import db
from menuscreen.models import (User, List_history, List_current,
                                User_settings, Template, Font_size_options)
# from flask_sse import sse
# import time

streams = Blueprint('streams', __name__)

############################
# def get_message():
#     # currentBeerlist = List_current.query.filter_by(id=current_user.id).all()
#     time.sleep(1.0)
#     s = time.ctime(time.time())
#     # print(currentBeerlist)
#     print('hello CHICKEN FUCKER')
#     return currentBeelist

# @streams.route('/_beerlist_stream')
# def _beerlist_stream():
#     def eventStream():
#         while True:
#             # wait for source data to be available, then push it
#             yield 'data: {}\n\n'.format(get_message())
#     return Response(eventStream(), mimetype="text/event-stream")

############################
