from flask_restplus import Namespace, Resource, fields
from tinydb import TinyDB, Query

api = Namespace('stations', description='Stations in the schedule')

station = api.model('Station', {
    'id': fields.String(required=True, description='The station identifier'),
    'name': fields.String(required=True, description='The cat name'),
})

db = TinyDB('reference.json')
stations_table = db.table('stations')

@api.route('/')
class StationList(Resource):
    @api.doc('list_stations')
    @api.marshal_list_with(station)
    def get(self):
        '''List all stations'''
        return stations_table.all()
