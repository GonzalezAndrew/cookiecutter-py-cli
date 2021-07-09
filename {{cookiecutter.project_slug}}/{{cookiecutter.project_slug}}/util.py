import json 

def _filter_data(filter, data):
    """ Filter the data for a specified value. """
    _filter = []

    def _nested_dict(data):
        for key, value in data.items():
            if key == filter:
                _filter.append({filter: value})
            elif isinstance(value, dict):
                _nested_dict(value)

    def _filter_dict(data):
        for key, value in data.items():
            if key == filter:
                _filter.append({filter: value})
            elif isinstance(value, dict):
                _nested_dict(value)

    if isinstance(data, list):
        for item in data:
            if isinstance(item, dict):
                _filter_dict(item)
            else:
                if item == filter:
                    _filter.append(item)
    return _filter

def _out_json(data):
    """ Json output for the issue command. """
    _json = {"JSON": data}
    print(json.dumps(_json, indent=4))

def _out_text(data):
    """ Text output for the issue command. """
    def _nested_dict(data):
        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, dict):
                    _nested_dict(value)
                else:
                    if isinstance(value, int):
                        value = str(value).strip()
                    elif len(value) == 0:
                        value = "N/A"
                    print("{:20s} {:25s}".format(key, value))
        
    for items in data:
        for key, value in items.items():
            # if key is the first key in the dictonary, lets add a newline 
            if key == next(iter(items)):
                print("\n{:20s} {:25s}".format("Attribute", "Value"))
            if isinstance(value, dict):
                _nested_dict(value)
            else:
                if isinstance(value, int):
                    value = str(value).strip()
                print("{:20s} {:25s}".format(key, value))


def output(data, output = None, filter = None):
    """ Output the request to the console. """

    if filter:
        data = _filter_data(filter, data)
    
    if output == "json":
        _out_json(data)
    elif output == "text":
        _out_text(data)
    else:
        print(json.dumps(data, indent=4))