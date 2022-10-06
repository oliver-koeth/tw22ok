
def get_bytes(local_file, lib_file):
    if local_file is not None:
        return local_file.getvalue()
    elif lib_file != '':
        return open(lib_file, "r")
    else:
        return None
