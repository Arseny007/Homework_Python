import psycopg2
from typing import List
from psycopg2.extras import RealDictCursor

conn = psycopg2.connect(database='postgres', user='postgres', password='changeme', host='localhost', port=999,
                        cursor_factory=RealDictCursor)


cursor = conn.cursor()
query = '''
select phone as "holderPhone", name as "holderName", "equipmentTitle", color as "equipmentColor",
       code as "storageCellCode", capacity as "storageCellCapacity"
from holder
         left join "equipmentToHolder" on phone = "equipmentToHolder"."holderPhone"
         left join equipment on "equipmentTitle" = title
         left join "storageCell" on phone = "storageCell"."holderPhone";
'''
class Holder:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.equipments = []
        self.storages = []

class Equipment:
    def __init__(self, title, color):
        self.title = title
        self.color = color
        self.holders = []

class Storage:
    def __init__(self, cellcode, cellcapacity):
        self.cellcode = cellcode
        self.cellcapacity = cellcapacity
        self.holder = None


cursor.execute(query)
rows = cursor.fetchall()
holder_dictionary = dict()
equipment_dictionary = dict()
storage_dictionary = dict()

for row in rows:
    holder_phone = row['holderPhone']
    holder_name = row['holderName']

    if holder_phone not in holder_dictionary:
        holder = Holder(phone = holder_phone, name = holder_name)
        holder_dictionary[holder_phone] = holder

    equipment_title = row['equipmentTitle']
    equipment_color = row['equipmentColor']
    equipment = None

    if equipment_title not in equipment_dictionary:
        equipment = Equipment(title = equipment_title, color = equipment_color)
        equipment_dictionary[equipment_title] = equipment
    else:
        equipment = equipment_dictionary[equipment_title]


    storage_cellcode = row['storageCellCode']
    storage_cellcapacity = row['storageCellCapacity']
    storage = None

    if storage_cellcode not in storage_dictionary:
        storage = Storage(cellcode = storage_cellcode, cellcapacity = storage_cellcapacity)
        storage_dictionary[storage_cellcode] = storage
    else:
        storage = storage_dictionary[storage_cellcode]

    holder.equipments.append(equipment)
    equipment.holders.append(holder)

    holder.storages.append(storage)
    storage.holder = holder



conn.close()

holders = list(holder_dictionary.values())
equipments = list(equipment_dictionary.values())
storages = list(storage_dictionary.values())

for hol in holders:
    print(hol.phone, hol.name)

for eq in equipments:
    print(eq.title, eq.color)

for st in storages:
    print(st.cellcode, st.cellcapacity)