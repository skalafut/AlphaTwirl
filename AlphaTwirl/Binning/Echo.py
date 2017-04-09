# Tai Sakuma <tai.sakuma@cern.ch>

##__________________________________________________________________||
def returnTrue(x): return True

##__________________________________________________________________||
def plusOne(x): return x + 1

##__________________________________________________________________||
class Echo(object):
    """UPDATE USING GOOGLE PY DOCSTRING FORMAT
	After making an instance of the class, the main function __call__
    takes a value as an input and returns the bin to which the value
    belongs.  In instances of the Echo class, __call__ returns the
	input value.

	Echo is useful for variables which have been categorized.
	If the input is categorical labels, then Echo can be useful.

    An instance of the Echo class can be created as follows::

    obj = Echo()

    The main function of this class is __call__.  __call__
    requires one input parameter which is a value of the
    variable being summarized.  It returns the bin to which
    the input value belongs.  Users must check that the
    return value is not None.

    The function next requires one input argument - a bin.
    Next returns the bin immediately after the input bin.

    If an instance of the Echo class named obj has already
    been defined, __call__ and next can be used as follows::

    obj.__call__(4)
    obj.next(3)
    
    """
    def __init__(self, nextFunc = plusOne, valid = returnTrue):
        """nextFunc can be any user defined function.
        If the bins are identified with strings, then nextFunc can be
        set to None.

        if the input argument valid is not changed from returnTrue,
        then __call__ will never return None.

        """
        self._nextFunc = nextFunc
        self._valid = valid

    def __repr__(self):
        return '{}(nextFunc = {!r}, valid = {!r})'.format(
            self.__class__.__name__,
            self._nextFunc,
            self._valid
        )

    def __call__(self, val):
        """main function of this class.  Given the input
        value val, this function returns the bin to which
        val belongs.  None is returned if the input val is
        not valid.
        
        """
        if not self._valid(val): return None
        return val

    def next(self, bin):
        """given the input bin, this function returns the
        bin immediately following the input bin argument.

        """
        if self._nextFunc is None: return None
        return self._nextFunc(bin)

##__________________________________________________________________||
