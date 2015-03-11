
import json
import os


""" DB """

resource_file = os.path.join(request.folder, "private", "resources.json")
with open(resource_file) as resource:
    resource_data = json.load(resource)

mysql_username, mysql_password, mysql_database, mysql_host, mysql_port = (
    resource_data["mysql"]["username"],
    resource_data["mysql"]["password"],
    resource_data["mysql"]["database"],
    resource_data["mysql"]["host"],
    resource_data["mysql"]["port"],
)

# TODO: Set migrate=False when db development is complete
db = DAL('mysql://' + mysql_username + ':' + mysql_password + '@' + mysql_host + '/' + mysql_database, pool_size=3, check_reserved=['mysql'], migrate=True)


########################################################################
# Reference: valid web2py field types
# field type                default field validators
# string                    IS_LENGTH(length) default length is 512
# text                      IS_LENGTH(65536)
# blob                      None
# boolean                   None
# integer                   IS_INT_IN_RANGE(-1e100, 1e100)
# double                    IS_FLOAT_IN_RANGE(-1e100, 1e100)
# decimal(n,m)              IS_DECIMAL_IN_RANGE(-1e100, 1e100)
# date                      IS_DATE()
# time                      IS_TIME()
# datetime                  IS_DATETIME()
# password                  None
# upload                    None
# reference <table>         IS_IN_DB(db,table.field,format)
# list:string               None
# list:integer              None
# list:reference <table>    IS_IN_DB(db,table.field,format,multiple=True)
# json                      IS_JSON()
# bigint                    None
# big-id                    None
# big-reference             None
########################################################################

db.define_table(
    'contact',
    Field('first_name', 'string'),
    Field('last_name', 'string'),
    Field('email', 'string'),
)

db.define_table(
    'phone_number',
    Field('contact_id', 'reference contact'),
    Field('number', 'string'),
)

db.define_table(
    'state',
    Field('name', 'string'),
    Field('abbreviation', 'string'),
)

db.define_table(
    'address',
    Field('contact_id', 'reference contact'),
    Field('street1', 'string'),
    Field('street2', 'string'),
    Field('city', 'string'),
    Field('state_id', 'reference state'),
    Field('zip', 'integer'),
)

# Seed data
if db(db.state.id > 0).count() == 0:

    STATES = [
        {
            "name": "Alabama",
            "abbreviation": "AL"
        },
        {
            "name": "Alaska",
            "abbreviation": "AK"
        },
        {
            "name": "American Samoa",
            "abbreviation": "AS"
        },
        {
            "name": "Arizona",
            "abbreviation": "AZ"
        },
        {
            "name": "Arkansas",
            "abbreviation": "AR"
        },
        {
            "name": "California",
            "abbreviation": "CA"
        },
        {
            "name": "Colorado",
            "abbreviation": "CO"
        },
        {
            "name": "Connecticut",
            "abbreviation": "CT"
        },
        {
            "name": "Delaware",
            "abbreviation": "DE"
        },
        {
            "name": "District Of Columbia",
            "abbreviation": "DC"
        },
        {
            "name": "Federated States Of Micronesia",
            "abbreviation": "FM"
        },
        {
            "name": "Florida",
            "abbreviation": "FL"
        },
        {
            "name": "Georgia",
            "abbreviation": "GA"
        },
        {
            "name": "Guam",
            "abbreviation": "GU"
        },
        {
            "name": "Hawaii",
            "abbreviation": "HI"
        },
        {
            "name": "Idaho",
            "abbreviation": "ID"
        },
        {
            "name": "Illinois",
            "abbreviation": "IL"
        },
        {
            "name": "Indiana",
            "abbreviation": "IN"
        },
        {
            "name": "Iowa",
            "abbreviation": "IA"
        },
        {
            "name": "Kansas",
            "abbreviation": "KS"
        },
        {
            "name": "Kentucky",
            "abbreviation": "KY"
        },
        {
            "name": "Louisiana",
            "abbreviation": "LA"
        },
        {
            "name": "Maine",
            "abbreviation": "ME"
        },
        {
            "name": "Marshall Islands",
            "abbreviation": "MH"
        },
        {
            "name": "Maryland",
            "abbreviation": "MD"
        },
        {
            "name": "Massachusetts",
            "abbreviation": "MA"
        },
        {
            "name": "Michigan",
            "abbreviation": "MI"
        },
        {
            "name": "Minnesota",
            "abbreviation": "MN"
        },
        {
            "name": "Mississippi",
            "abbreviation": "MS"
        },
        {
            "name": "Missouri",
            "abbreviation": "MO"
        },
        {
            "name": "Montana",
            "abbreviation": "MT"
        },
        {
            "name": "Nebraska",
            "abbreviation": "NE"
        },
        {
            "name": "Nevada",
            "abbreviation": "NV"
        },
        {
            "name": "New Hampshire",
            "abbreviation": "NH"
        },
        {
            "name": "New Jersey",
            "abbreviation": "NJ"
        },
        {
            "name": "New Mexico",
            "abbreviation": "NM"
        },
        {
            "name": "New York",
            "abbreviation": "NY"
        },
        {
            "name": "North Carolina",
            "abbreviation": "NC"
        },
        {
            "name": "North Dakota",
            "abbreviation": "ND"
        },
        {
            "name": "Northern Mariana Islands",
            "abbreviation": "MP"
        },
        {
            "name": "Ohio",
            "abbreviation": "OH"
        },
        {
            "name": "Oklahoma",
            "abbreviation": "OK"
        },
        {
            "name": "Oregon",
            "abbreviation": "OR"
        },
        {
            "name": "Palau",
            "abbreviation": "PW"
        },
        {
            "name": "Pennsylvania",
            "abbreviation": "PA"
        },
        {
            "name": "Puerto Rico",
            "abbreviation": "PR"
        },
        {
            "name": "Rhode Island",
            "abbreviation": "RI"
        },
        {
            "name": "South Carolina",
            "abbreviation": "SC"
        },
        {
            "name": "South Dakota",
            "abbreviation": "SD"
        },
        {
            "name": "Tennessee",
            "abbreviation": "TN"
        },
        {
            "name": "Texas",
            "abbreviation": "TX"
        },
        {
            "name": "Utah",
            "abbreviation": "UT"
        },
        {
            "name": "Vermont",
            "abbreviation": "VT"
        },
        {
            "name": "Virgin Islands",
            "abbreviation": "VI"
        },
        {
            "name": "Virginia",
            "abbreviation": "VA"
        },
        {
            "name": "Washington",
            "abbreviation": "WA"
        },
        {
            "name": "West Virginia",
            "abbreviation": "WV"
        },
        {
            "name": "Wisconsin",
            "abbreviation": "WI"
        },
        {
            "name": "Wyoming",
            "abbreviation": "WY"
        }
    ]

    for state in STATES:
        db.state.insert(
            name=state.get('name'),
            abbreviation=state.get('abbreviation')
        )