
class QueueOutOfRangeException(Exception):
    def __init__(self, Errormsg) -> None:
        super().__init__(Errormsg)