class ProxyError(Exception):
    pass


class WrongKey(ProxyError):
    pass


class MethodError(ProxyError):
    pass
