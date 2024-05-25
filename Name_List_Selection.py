def select_for(batch):
    selected_batch = batch
    f = open(f"C://Class//{selected_batch}_NAME_LIST.txt", 'r')
    raw_name_list = f.readlines()
    name_list_with_surname = []
    name_list_without_surname = []
    final_name_list = []
    num_list = []
    for raw_name in raw_name_list:
        raw_name_1 = raw_name.split('.')
        print(raw_name_1)
        name_list_with_surname.append(raw_name_1[1])
        num_list.append(raw_name_1[2])
    for name in name_list_with_surname:
        name1 = name.split(' ')
        name_list_without_surname.append(name1[0])
    a=0
    for name in name_list_without_surname:
        count = name_list_without_surname.count(name)
        #print(count)
        if count>=2:
            final_name_list.append(name_list_with_surname[a])
        else:
            final_name_list.append(name_list_without_surname[a])
        a+=1

    return final_name_list, num_list;

#select_for()