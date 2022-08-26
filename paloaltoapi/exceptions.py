"""Exceptions File"""
class ParamsError(Exception):
    """
    Params Error
    """
    def __init__(self, *args: object) -> None:
        """
        Params Error
        """
        super().__init__(*args)

class CredentialsError(Exception):
    """
    Creditnal Error
    """
    def __init__(self, *args: object) -> None:
        """
        Creditnal Error
        """
        super().__init__(*args)

class PaloAltoAPIError(Exception):
    """
    PaloAlto API Error
    """
    def __init__(self, *args: object) -> None:
        """
        PaloAlto API Error
        """
        super().__init__(*args)

class PaloAltoObj(PaloAltoAPIError):
    """Palo Alto Obj Error"""

class PaloAltoObjExists(PaloAltoAPIError):
    """Palo Alto OBJ exists"""

class PaloAltoObjNotExists(PaloAltoObj):
    """Palo Alto Task not supported"""
    def __init__(self, *args, **kwargs):
        default_message = "missing obj"
        if args:
            args = [str(a) for a in list(args)]
            default_message = f"{default_message}={' '.join(args)}"
        super().__init__(default_message, **kwargs)

class PaloAltoTAGError(PaloAltoAPIError):
    """Palo Alto Tag does not exist error"""

class PaloAltoTaskError(PaloAltoAPIError):
    """Palo Alto Task not supported"""
    def __init__(self, *args, **kwargs):
        default_message = "unsupported task"
        if args:
            args = [str(a) for a in list(args)]
            default_message = f"{default_message}={' '.join(args)}"
        super().__init__(default_message, **kwargs)

class UrlExistsError(Exception):
    """
    Url Exists Error
    """

class UrlNotExistsError(Exception):
    """
    URL Not exist error
    """
    def __init__(self, *args: object) -> None:
        """
        URL Not exist error
        """
        super().__init__(*args)

class PaloAltoMissingParam(PaloAltoAPIError):
    """Palo Alto Missing Param error"""
