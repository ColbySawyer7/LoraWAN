__all__ = ['PhyPayload', 'MHDR']

from .PhyPayload import PhyPayload

def new(nwkey = [], appkey = []):
    return PhyPayload(nwkey, appkey)
