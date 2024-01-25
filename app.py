import sys
import json
import os, ibm_db
import requests
import subprocess
from flask import Flask

app = Flask(__name__)

# delete an event record
@app.get('/ticket/list')
def get_tickets():
    db2_dsn = 'DATABASE={};HOSTNAME={};PORT={};PROTOCOL=TCPIP;UID={uid};PWD={pwd};SECURITY=SSL'.format(
        'bludb',
        'fbd88901-ebdb-4a4f-a32e-9822b9fb237b.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud',
        '32731',
        uid='mvh18309',
        pwd='pxp1ZAimaSNtXJCR'
    )

    conn = ibm_db.connect(db2_dsn, "", "")
    query = 'SELECT * FROM "ISSUES"'
    ret = []
    command = ibm_db.exec_immediate(conn, query)
    result = ibm_db.fetch_assoc(command)
    while result:
        ret.append(result)
        result = ibm_db.fetch_assoc(command)

    return_string = str(ret)

    return {'message': return_string}



@app.post('/ticket/create')
def create_ticket(params):
    db2_dsn = 'DATABASE={};HOSTNAME={};PORT={};PROTOCOL=TCPIP;UID={uid};PWD={pwd};SECURITY=SSL'.format(
        'bludb',
        'fbd88901-ebdb-4a4f-a32e-9822b9fb237b.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud',
        '32731',
        uid='mvh18309',
        pwd='pxp1ZAimaSNtXJCR'
    )

    conn = ibm_db.connect(db2_dsn, "", "")
    query = 'SELECT * FROM "ISSUES"'

    name = params['name']
    employee_id = params['employee_id']
    issue_type = params['Issue_type']


    response = {}

    inser_sql = "INSERT INTO mvh18309.ISSUES (NAME, EMPLOYEE_ID, ISSUE_TYPE) VALUES('{0}', '{1}', '{2}')".format(
        name, employee_id, issue_type)
    stmt = ibm_db.prepare(conn, inser_sql)
    ibm_db.execute(stmt)
    return_string = "Record has been sucessfully achieved"

    return {'message': return_string}


# default "homepage", also needed for health check by Code Engine
@app.get('/')
def print_default():

    return {'message': 'This is the Events API server'}


# Start the actual app
# Get the PORT from environment or use the default
port = os.getenv('PORT', '5000')
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=int(port))
