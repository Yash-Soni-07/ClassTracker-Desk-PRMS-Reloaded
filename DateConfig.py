def DateConversion(d):
    today = str(d)
    date_split = today.split('-')
    if date_split[1] == '01':
        date_split[1] = 'January'
    elif date_split[1] == '02':
        date_split[1] = 'February'
    elif date_split[1] == '03':
        date_split[1] = 'March'
    elif date_split[1] == '04':
        date_split[1] = 'April'
    elif date_split[1] == '05':
        date_split[1] = 'May'
    elif date_split[1] == '06':
        date_split[1] = 'June'
    elif date_split[1] == '07':
        date_split[1] = 'July'
    elif date_split[1] == '08':
        date_split[1] = 'August'
    elif date_split[1] == '09':
        date_split[1] = 'September'
    elif date_split[1] == '10':
        date_split[1] = 'October'
    elif date_split[1] == '11':
        date_split[1] = 'November'
    elif date_split[1] == '12':
        date_split[1] = 'December'
    converted_date = '_'.join(date_split)
    #print("Today's Date : ",converted_date)
    return converted_date






