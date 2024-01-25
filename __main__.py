import ibm_db

def main(params):

    db2_dsn = 'DATABASE={};HOSTNAME={};PORT={};PROTOCOL=TCPIP;UID={uid};PWD={pwd};SECURITY=SSL'.format(
        'bludb',
        'fbd88901-ebdb-4a4f-a32e-9822b9fb237b.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud',
        '32731',
        uid='mvh18309',
        pwd='pxp1ZAimaSNtXJCR'
    )

    conn=ibm_db.connect(db2_dsn,"", "")
    query = 'SELECT * FROM "ISSUES"'

    name = params['name']
    employee_id = params['employee_id']
    issue_type=params['Issue_type']
    extract_type=params['extract_type']

    response = {}
    return_string=""
    
    if extract_type==0:

        inser_sql = "INSERT INTO mvh18309.ISSUES (NAME, EMPLOYEE_ID, ISSUE_TYPE) VALUES('{0}', '{1}', '{2}')".format(name,employee_id,issue_type)
        stmt = ibm_db.prepare(conn, inser_sql)
        ibm_db.execute(stmt)
        return_string = "Record has been sucessfully achieved"
    else:
        ret = []
        command=ibm_db.exec_immediate(conn, query)
        result = ibm_db.fetch_assoc(command)
        while result:
            ret.append(result)
            result = ibm_db.fetch_assoc(command)


        return_string = str(ret)

    response ={
        "headers": {
        "Content-Type": "application/json",
        },
        "statusCode": 200,
        "body": return_string
        }
    return response
