def check_attr(obj, name):
    try:
        getattr(obj.__dict__, name)
        return True
    except AttributeError as err:
        print(f"Testing: Got Error {err}")
        #setattr(self, name, {k: None for k in DEVICEGROUP_ATTR})
        return False