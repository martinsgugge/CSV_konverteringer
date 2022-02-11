from CSV import *
from LogItem import *
data = csvToArray("Purac tags.csv", ';')
data = transpose_undefined_matrix(data)
items = []
for i in range(len(data[1])):
    tags = []
    index = 0
    string_index = len(data[1][i])
    s_index = data[1][i].find('_S') + len('_S')
    d_index = data[1][i].find('_D') + len('_D')
    o_index = data[1][i].find('_O') + len('_O')
    p_index = data[1][i].find('_P') + len('_P')
    sp_index = data[1][i].find('_SP') + len('_SP')
    ref_index = data[1][i].find('_REF') + len('_REF')
    amp_index = data[1][i].find('_ACC_CURR') + len('_ACC_CURR')
    run_index = data[1][i].find('_RUN') + len('_RUN')
    running_index = data[1][i].find('_RUNNING') + len('_RUNNING')
    """or ('_S' in data[1][i] and string_index == s_index) \ or '_STATUS_AUTO' in data[1][i]'_HMI_ON' in data[1][i] or"""
    """'_CALC' in data[1][i]  \ 
    or ('PS' in data[1][i] and '_PS' not in data[1][i])\
                or ('TS' in data[1][i] and '_ALARM' not in data[1][i])\
                or ('_O' in data[1][i] and string_index==o_index)\
                or ('_P' in data[1][i] and string_index==p_index)\
                or ('_SP' in data[1][i] and string_index==sp_index)\
                or ('_REF' in data[1][i] and string_index==ref_index)\
                or '_ACC_SPEED' in data[1][i] \
                or ('_ACC_CURR' in data[1][i] and string_index==amp_index)\ 
                or 'LS' in data[1][i] or '_POS_CURRENT' in data[1][i] \
                 or ('_ACC_CURR' in data[1][i] and string_index == amp_index)"""
    if ('_RUNNING' in data[1][i] and string_index == running_index)\
            or ('_D' in data[1][i] and string_index == d_index) and '_DRIFTSKLAR' not in data[1][i] \
            or ('_RUN' in data[1][i] and string_index == run_index):
        if len(data[2]) > 0:
            tags.append(LogItem)
            tags[index].name = data[1][i]
            tags[index].item_id = data[2][i]
            tags[index].data_type = data[4][i]
            tags[index].description = data[6][i]
            # print(tags[index].__dict__)
            items.append([tags[index].name, tags[index].item_id, tags[index].data_type, tags[index].description])
            index += 1


ArrayTocsv(['Name', 'Address', 'Datatype', 'Description'], items, 'Filtrert Purac tags.csv')


def format_log_group(csv_file, url, user, pw, channel, device, bool_group):
    arr = csvToArray(csv_file, ';')
    length = arr.__len__()
    for i in range(0, length):
        if bool_group == 'Y' and arr[i, 3] == 'Av/på':
            skip = False

        elif bool_group == 'Y' and arr[i, 3] != 'Av/på':
            skip = True

        elif bool_group == 'N' and arr[i, 3] == 'Av/på':
            skip = True

        elif bool_group == 'N' and arr[i, 3] != 'Av/på':
            skip = False

        if skip == False:
            item = LogItem()
            item.name = str(arr[i, 4].lstrip('GU_'))
            print(item.name)
            item.name = item.name.replace(".", "_")
            print(item.name)
            #item.name = arr[i, 4]
            item.tag_id = arr[i, 0]
            if arr[i, 3] == 'Av/på':
                item.data_type = 'Boolean'
            else:
                item.data_type = 'Float'
            item.description = arr[i, 5]
            """Malmberg2.T1.A03_Active Power_Total"""
            item.item_id = '{0}.{1}.{2}'.format(channel, device, item.name)

"""for x in data:
	
	for v in x:
		print(v)"""