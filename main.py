
class NewException(BaseException):
    ...

def check(var):
    if var:
        print('check ok')
        return
    else:
        raise NewException(f"Variable nicht definiert")

def check_exists(var):
    if var in locals():
        print('check_exists ok')
        return
    else:
        raise NewException(f"Variable nicht definiert")

def check_string(var):
    if isinstance(var, str):
        print('check_string ok')
        return
    else:
        raise NewException(f"Variable ist kein String")


if __name__ == '__main__':
    try:
        a = '3'
        check(a)
        print('True')
        check_string(a)
        print("String")
        a = 34
        check_string(a)
        a = None
        check_exists('a.py')
        check(a)
        print('False')
    except FileNotFoundError as e:
        print("exception1 ist aufgetreten")
    except Exception:
        print("exception2 ist aufgetreten")
    except NewException as e:
        print(f"exception3 ist aufgetreten: {e}")
