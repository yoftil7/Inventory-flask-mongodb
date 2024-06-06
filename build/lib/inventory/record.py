import os,sys
from flask_restx import Namespace, Resource, fields
from flask import (request, current_app)
from werkzeug.utils import secure_filename
import datetime
import time
import subprocess
import json
from inventory.db import get_mongodb

api = Namespace("record", description="Record APIs")

search_model = api.model(
    'Record Search', {'fname': fields.String(required=True, default="Yoftahe", description='First name')}
)

insert_model = api.model(
    'Record Insert', {
        'row': fields.String(required=True, description='Record row number'),
        'fname': fields.String(required=True, default="James", description='First name'),
        'lname': fields.String(required=True, default="Bond", description='Last name')                  
    }
)

delete_model = api.model('Record Delete',{
    'row': fields.String(required=True, description="Row of item to delete")
    }
)

update_model = api.model('Record Update', {
    'row': fields.String(required=True, description='Row of record to update'),
    'key': fields.String(required=True, description='Field to update'),
    'new_value': fields.String(required=True, description='New value')
    }
)


@api.route('/insert')
class RecordList(Resource):
    @api.doc('insert_records')
    @api.expect(insert_model)
    def post(self):
        req_obj = request.json
        mongo_dbh, error_obj = get_mongodb()
        if error_obj != {}:
            return error_obj
        res = mongo_dbh["c_inventory"].insert_one(req_obj)
        res_obj = {"status":1}
        return res_obj

    @api.doc(False)
    def get(self):
        return self.post()


@api.route('/search')
class RecordList(Resource):
    @api.doc('search_records')
    @api.expect(search_model)
    def post(self):
        req_obj = request.json
        mongo_dbh, error_obj = get_mongodb()
        if error_obj != {}:
            return error_obj
        res_obj = {"records":[]}
        for doc in mongo_dbh["c_inventory"].find(req_obj):
            if "_id" in doc:
                doc["_id"] = str(doc["_id"])
            res_obj["records"].append(doc)
        res_obj["status"] = 1

        return res_obj

    @api.doc(False) 
    def get(self):
        return self.post()


@api.route('/delete')
class RecordList(Resource):
    @api.doc('delete_records')
    @api.expect(delete_model)
    def delete(self):
        req_obj = request.json
        mongo_dbh, error_obj = get_mongodb()
        if error_obj != {}:
            return error_obj
        delete_obj = {'row': req_obj.get('row')}
        res = mongo_dbh['c_inventory'].delete_one(delete_obj)
        if res.deleted_count == 1:
            return {'status': 1, 'message': 'Record successfully deleted'}
        else: 
            return {'status': 0, 'message': 'Record not found!'}

    @api.doc(False)
    def get(self):
        return self.delete()


@api.route('/update')
class RecordList(Resource):
    @api.doc('update_records')
    @api.expect(update_model)
    def put(self):
        req_obj = request.json
        mongo_dbh, error_obj = get_mongodb()
        if error_obj:
            return error_obj
        update_row = req_obj.get('row')
        update_key = req_obj.get('key')
        new_value = req_obj.get('new_value')
        update_res = mongo_dbh['c_inventory'].update_one({"row": update_row}, {"$set": {update_key: new_value}})
        if update_res.modified_count == 1:
            return {'status': 1, 'message': 'Update successful'}
        else:
            return {'status': 0, 'message': 'Record not updated'}
        
    @api.doc(False)
    def get(self):
        return self.put()









