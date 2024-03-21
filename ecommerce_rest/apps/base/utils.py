from datetime import datetime

def validate_files(request, field, update=False):
    request = request.copy()

    if update:
        if type(request[field]) == str: request.__delitem__(field)
    else:
        if type(request[field]) == str: request.__setitem__(field, None)        

    return request


def format_date(date):
    try:
        date_obj = datetime.strptime(date, '%d/%m/%Y')
    except ValueError:
        try:
            date_obj = datetime.strptime(date, '%m/%d/%Y')
        except ValueError:
            return None    
    return date_obj.strftime('%Y-%m-%d')