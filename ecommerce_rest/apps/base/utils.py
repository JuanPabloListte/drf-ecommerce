def validate_files(request, field, update=False):
    request = request.copy()

    if update:
        if type(request[field]) == str: request.__delitem__(field)
    else:
        if type(request[field]) == str: request.__setitem__(field, None)        

    return request
