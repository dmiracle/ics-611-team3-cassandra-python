from team3_app.connect_database import session


def get_demographics(tract):
    acs2017 = f'SELECT * FROM demographics_2 where "Tract" = {tract};'
    rows = session.execute(acs2017)
    for row in rows:
        print(row)
        return row
