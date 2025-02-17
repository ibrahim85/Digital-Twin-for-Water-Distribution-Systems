####################### Section 1 ###########################3
############ Descrubes all the tags present in the Database

v1 = ('v1', 1)
V45 = ('V45', 1)
V47 = ('V47', 1)
V2 = ('V2', 1)
PU1 = ('PU1', 1)
PU2 = ('PU2', 1)
PU3 = ('PU3', 1)
PU4 = ('PU4', 1)
PU5 = ('PU5', 1)
PU6 = ('PU6', 1)
PU7 = ('PU7', 1)
PU8 = ('PU8', 1)
PU9 = ('PU9', 1)
PU10 = ('PU10', 1)
PU11 = ('PU11', 1)

# Pump flows
V2F = ('V2F', 1)
PU1F = ('PU1F', 1)
PU2F = ('PU2F', 1)
PU3F = ('PU3F', 1)
PU4F = ('PU4F', 1)
PU5F = ('PU5F', 1)
PU6F = ('PU6F', 1)
PU7F = ('PU7F', 1)
PU8F = ('PU8F', 1)
PU9F = ('PU9F', 1)
PU10F = ('PU10F', 1)
PU11F = ('PU11F', 1)

T1 = ('T1', 1)
T2 = ('T2', 1)
T3 = ('T3', 1)
T4 = ('T4', 1)
T5 = ('T5', 1)
T6 = ('T6', 1)
T7 = ('T7', 1)
CONTROL = ('CONTROL', 1)

# Junction nodes for SCADA
J280 = ('J280', 1)
J269 = ('J269', 1)
J300 = ('J300', 1)
J256 = ('J256', 1)
J289 = ('J289', 1)
J415 = ('J415', 1)
J302 = ('J302', 1)
J306 = ('J306', 1)
J307 = ('J307', 1)
J317 = ('J317', 1)
J14 = ('J14', 1)
J422 = ('J422', 1)

####################### Section 2 ###########################3
############ Describes the network parameters

plc_netmask = '/24'
ENIP_LISTEN_PLC_ADDR = '192.168.1.1'
SCADA_IP_ADDR = '192.168.1.2'

SIMPLE_IP_OPTIONS = {
    'plc1':'192.168.1.1',
    'plc2':'192.168.1.2',
    'plc3':'192.168.1.3',
    'plc4':'192.168.1.4',
    'plc5':'192.168.1.5',
    'plc6':'192.168.1.6',
    'plc7':'192.168.1.7',
    'plc8':'192.168.1.8',
    'plc9':'192.168.1.9',
}

CTOWN_IPS = {
    'plc1':'10.0.1.1',
    'plc2':'10.0.2.1',
    'plc3':'10.0.3.1',
    'plc4':'10.0.4.1',
    'plc5':'10.0.5.1',
    'plc6':'10.0.6.1',
    'plc7':'10.0.7.1',
    'plc8':'10.0.8.1',
    'plc9':'10.0.9.1',
}

####################### Section 3 ###########################3
############ Describes the MiniCPS servers
############ A MiniCPS server is a process that sends/receives a tag

# A server is controlled in 3 steps
# Step 1: Define which tags the server (PLC - SCADA) can control
# Step 2: Configure the address and the tags
# Step 3: Configure the protocol

PLC1_DATA = {
    'TODO': 'TODO',
}

PLC2_DATA = {
    'TODO': 'TODO',
}

PLC3_DATA = {
    'TODO': 'TODO',
}

PLC4_DATA = {
    'TODO': 'TODO',
}

PLC5_DATA = {
    'TODO': 'TODO',
}

PLC6_DATA = {
    'TODO': 'TODO',
}

PLC7_DATA = {
    'TODO': 'TODO',
}

PLC8_DATA = {
    'TODO': 'TODO',
}

PLC9_DATA = {
    'TODO': 'TODO',
}
SCADA_DATA = {
    'TODO': 'TODO',
}

# This is telling which tags can be controlled by PLC1
PLC1_TAGS = (
    ('PU1', 1, 'REAL'),
    ('PU2', 1, 'REAL'),
    ('PU1F', 1, 'REAL'),
    ('PU2F', 1, 'REAL'),
    ('T1', 1, 'REAL'),
    ('J280', 1, 'REAL'),
    ('J269', 1, 'REAL'),
    ('CONTROL', 1, 'REAL'),
)

PLC2_TAGS = (
    ('T1', 1, 'REAL'),
    ('CONTROL', 1, 'REAL'),
)

PLC3_TAGS = (
    ('T2', 1, 'REAL'),
    ('PU4', 1, 'REAL'),
    ('PU5', 1, 'REAL'),
    ('PU6', 1, 'REAL'),
    ('PU7', 1, 'REAL'),
    ('PU4F', 1, 'REAL'),
    ('PU5F', 1, 'REAL'),
    ('PU6F', 1, 'REAL'),
    ('PU7F', 1, 'REAL'),
    ('V2', 1, 'REAL'),
    ('V2F', 1, 'REAL'),
    ('T4', 1, 'REAL'),
    ('J300', 1, 'REAL'),
    ('J256', 1, 'REAL'),
    ('J289', 1, 'REAL'),
    ('J415', 1, 'REAL'),
    ('J14', 1, 'REAL'),
    ('J422', 1, 'REAL'),
    ('CONTROL', 1, 'REAL'),
)

PLC4_TAGS = (
    ('T3', 1, 'REAL'),
    ('CONTROL', 1, 'REAL'),
)

PLC5_TAGS = (
    ('PU8', 1, 'REAL'),
    ('PU9', 1, 'REAL'),
    ('PU10', 1, 'REAL'),
    ('PU11', 1, 'REAL'),
    ('PU8F', 1, 'REAL'),
    ('PU9F', 1, 'REAL'),
    ('PU10F', 1, 'REAL'),
    ('PU11F', 1, 'REAL'),
    ('T7', 1, 'REAL'),
    ('T5', 1, 'REAL'),
    ('J302', 1, 'REAL'),
    ('J306', 1, 'REAL'),
    ('J307', 1, 'REAL'),
    ('J317', 1, 'REAL'),
    ('CONTROL', 1, 'REAL'),
)

PLC6_TAGS = (
    ('T4', 1, 'REAL'),
    ('CONTROL', 1, 'REAL'),
)

PLC7_TAGS = (
    ('T5', 1, 'REAL'),
    ('CONTROL', 1, 'REAL'),
)

PLC8_TAGS = (
    ('T6', 1, 'REAL'),
    ('CONTROL', 1, 'REAL'),
)

PLC9_TAGS = (
    ('T7', 1, 'REAL'),
    ('CONTROL', 1, 'REAL'),
)

SCADA_TAGS = (
    ('v1', 1, 'REAL'),
    ('V45', 1, 'REAL'),
    ('V47', 1, 'REAL'),
    ('V2', 1, 'REAL'),
    ('PU1', 1, 'REAL'),
    ('PU2', 1, 'REAL'),
    ('PU3', 1, 'REAL'),
    ('PU4', 1, 'REAL'),
    ('PU5', 1, 'REAL'),
    ('PU6', 1, 'REAL'),
    ('PU7', 1, 'REAL'),
    ('PU8', 1, 'REAL'),
    ('PU9', 1, 'REAL'),
    ('PU10', 1, 'REAL'),
    ('PU11', 1, 'REAL'),
    ('V2F', 1, 'REAL'),
    ('PU1F', 1, 'REAL'),
    ('PU2F', 1, 'REAL'),
    ('PU3F', 1, 'REAL'),
    ('PU4F', 1, 'REAL'),
    ('PU5F', 1, 'REAL'),
    ('PU6F', 1, 'REAL'),
    ('PU7F', 1, 'REAL'),
    ('PU8F', 1, 'REAL'),
    ('PU9F', 1, 'REAL'),
    ('PU10F', 1, 'REAL'),
    ('PU11F', 1, 'REAL'),
    ('T1', 1, 'REAL'),
    ('T2', 1, 'REAL'),
    ('T3', 1, 'REAL'),
    ('T4', 1, 'REAL'),
    ('T5', 1, 'REAL'),
    ('T6', 1, 'REAL'),
    ('T7', 1, 'REAL'),
    ('J280', 1, 'REAL'),
    ('J269', 1, 'REAL'),
    ('J300', 1, 'REAL'),
    ('J256', 1, 'REAL'),
    ('J289', 1, 'REAL'),
    ('J415', 1, 'REAL'),
    ('J302', 1, 'REAL'),
    ('J306', 1, 'REAL'),
    ('J307', 1, 'REAL'),
    ('J317', 1, 'REAL'),
    ('J14', 1, 'REAL'),
    ('J422', 1, 'REAL'),
)

flag_attack_communication_plc1_plc2_replay_empty = 0
flag_attack_plc1 = 0
flag_attack_communication_plc1_plc2 = 0
ATT_1 = ('ATT_1', 1)
ATT_2 = ('ATT_2', 1)

# Configures the MiniCPS servers
PLC1_SERVER = {
    'address': ENIP_LISTEN_PLC_ADDR,
    'tags': PLC1_TAGS
}
PLC2_SERVER = {
    'address': ENIP_LISTEN_PLC_ADDR,
    'tags': PLC2_TAGS
}
PLC3_SERVER = {
    'address': ENIP_LISTEN_PLC_ADDR,
    'tags': PLC3_TAGS
}
PLC4_SERVER = {
    'address': ENIP_LISTEN_PLC_ADDR,
    'tags': PLC4_TAGS
}
PLC5_SERVER = {
    'address': ENIP_LISTEN_PLC_ADDR,
    'tags': PLC5_TAGS
}
PLC6_SERVER = {
    'address': ENIP_LISTEN_PLC_ADDR,
    'tags': PLC6_TAGS
}
PLC7_SERVER = {
    'address': ENIP_LISTEN_PLC_ADDR,
    'tags': PLC7_TAGS
}
PLC8_SERVER = {
    'address': ENIP_LISTEN_PLC_ADDR,
    'tags': PLC8_TAGS
}
PLC9_SERVER = {
    'address': ENIP_LISTEN_PLC_ADDR,
    'tags': PLC9_TAGS
}

SCADA_SERVER = {
    'address': SCADA_IP_ADDR,
    'tags': SCADA_TAGS
}


# This configures the protocol
# The name and mode of the protocol will always be the same
PLC1_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC1_SERVER
}
PLC2_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC2_SERVER
}
PLC3_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC3_SERVER
}
PLC4_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC4_SERVER
}
PLC5_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC5_SERVER
}
PLC6_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC6_SERVER
}
PLC7_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC7_SERVER
}
PLC8_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC8_SERVER
}
PLC9_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC9_SERVER
}

SCADA_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': SCADA_SERVER
}

PATH = 'ctown_db.sqlite'
NAME = 'ctown'

STATE = {
    'name': NAME,
    'path': PATH
}


# This creates the DB in SQlite

SCHEMA = """        
CREATE TABLE ctown (        
    name              TEXT NOT NULL,        
    pid               INTEGER NOT NULL,        
    value             TEXT,        
    PRIMARY KEY (name, pid)        
);
"""

# The initial conditions of the system are written in the DB.
# These files are either in the csv file or the EPANET inp
SCHEMA_INIT = """
    INSERT INTO ctown VALUES ('T1', 1, '3.0');
    INSERT INTO ctown VALUES ('T2', 1, '0.5');
    INSERT INTO ctown VALUES ('T3', 1, '3.0');
    INSERT INTO ctown VALUES ('T4', 1, '2.5');
    INSERT INTO ctown VALUES ('T5', 1, '1.0');
    INSERT INTO ctown VALUES ('T6', 1, '5.2');
    INSERT INTO ctown VALUES ('T7', 1, '2.5');
    INSERT INTO ctown VALUES ('v1', 1, '1');
    INSERT INTO ctown VALUES ('V45', 1, '1');
    INSERT INTO ctown VALUES ('V47', 1, '1');
    INSERT INTO ctown VALUES ('V2', 1, '0');
    INSERT INTO ctown VALUES ('PU1', 1, '0');
    INSERT INTO ctown VALUES ('PU2', 1, '1');
    INSERT INTO ctown VALUES ('PU3', 1, '0');
    INSERT INTO ctown VALUES ('PU4', 1, '0');
    INSERT INTO ctown VALUES ('PU5', 1, '0');
    INSERT INTO ctown VALUES ('PU6', 1, '0');
    INSERT INTO ctown VALUES ('PU7', 1, '0');
    INSERT INTO ctown VALUES ('PU8', 1, '0');
    INSERT INTO ctown VALUES ('PU9', 1, '0');
    INSERT INTO ctown VALUES ('PU10', 1, '0');
    INSERT INTO ctown VALUES ('PU11', 1, '0');
    INSERT INTO ctown VALUES ('V2F', 1, '0.0');    
    INSERT INTO ctown VALUES ('PU1F', 1, '0.0');
    INSERT INTO ctown VALUES ('PU2F', 1, '0.0');
    INSERT INTO ctown VALUES ('PU3F', 1, '0.0');
    INSERT INTO ctown VALUES ('PU4F', 1, '0.0');
    INSERT INTO ctown VALUES ('PU5F', 1, '0.0');
    INSERT INTO ctown VALUES ('PU6F', 1, '0.0');
    INSERT INTO ctown VALUES ('PU7F', 1, '0.0');
    INSERT INTO ctown VALUES ('PU8F', 1, '0.0');
    INSERT INTO ctown VALUES ('PU9F', 1, '0.0');
    INSERT INTO ctown VALUES ('PU10F', 1, '0');
    INSERT INTO ctown VALUES ('PU11F', 1, '0.0');    
    INSERT INTO ctown VALUES ('J280', 1, '0.0');
    INSERT INTO ctown VALUES ('J269', 1, '0.0');
    INSERT INTO ctown VALUES ('J300', 1, '0.0');
    INSERT INTO ctown VALUES ('J256', 1, '0.0');
    INSERT INTO ctown VALUES ('J289', 1, '0.0');
    INSERT INTO ctown VALUES ('J415', 1, '0.0');
    INSERT INTO ctown VALUES ('J302', 1, '0.0');
    INSERT INTO ctown VALUES ('J306', 1, '0.0');
    INSERT INTO ctown VALUES ('J307', 1, '0.0');
    INSERT INTO ctown VALUES ('J317', 1, '0.0');
    INSERT INTO ctown VALUES ('J14', 1, '0.0');
    INSERT INTO ctown VALUES ('J422', 1, '0.0');
    INSERT INTO ctown VALUES ('ATT_1', 1, '0');
    INSERT INTO ctown VALUES ('ATT_2', 1, '0');
    INSERT INTO ctown VALUES ('CONTROL', 1, '0');    
"""