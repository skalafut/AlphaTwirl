# Tai Sakuma <tai.sakuma@cern.ch>

##__________________________________________________________________||
def returnTrue(x): return True

##__________________________________________________________________||
class Binning(object):
    """
    UPDATE USING GOOGLE PY DOCSTRING FORMAT
    After making an instance of the class, the main function __call__
    takes a value as an input and returns the bin to which the value
    belongs.  Instances of the Binning class create a set of bins
    with user defined bin boundaries.
    
    An instance of the Binning class can be defined with a single argument
    ``boundaries``, which is set equal to a list of the bin boundaries
    that begin at the lowest value, and increase for every bin
    added, like::
        
        obj = Binning(boundaries = (0, 100, 200, 400, 700, 1100))
    
    Alternatively, an instance of the Binning class can be instantiated with
    two arguments ``lows`` and ``ups``.  These two arguments are set equal
    to two lists of the same length that specify the lower and upper edge
    of every bin, like::
        
        obj = Binning(lows = (0, 20, 40, 60), ups = (20, 40, 60, 200))

    after creating obj, it can be called via::

        obj(25)

    In this case, obj(25) returns 20.  In general, if the
    input value is valid, then the bin to which the value belongs
    is returned.  If the input value is not valid, then None is returned.
    If the value is equal to the low edge of bin J, then bin J is
    returned.  If the value is below the low edge of the first bin, then
    the underflow bin is returned.  If the value is above the upper
    edge of the last bin, then the overflow bin is returned.
    

    The function next requires a bin as an input parameter, and
    returns the next bin::
    
    obj.next(20)
    
    If the input parameter is the underflow
    bin, then the first bin is returned.  If the input parameter is the overflow
    bin, then the overflow bin is returned.  Each bin is identified by its
    lower edge, and next returns the upper edge of the bin (equivalent to the
    lower edge of the next bin).
    
    """
    def __init__(self, boundaries = None, lows = None, ups = None,
                 retvalue = 'lowedge', bins = None, underflow_bin = None, overflow_bin = None,
                 valid = returnTrue):
        """__init__ creates an instance of the Binning class.
        UPDATE USING GOOGLE PY DOCSTRING FORMAT

        Parameters
        ---------
        boundaries : list
             

        By default:
            retvalue is set to lowedge.  It can also be set to number.
            every value added has the parameter valid equal to True.  Thus, __call__
            will never return None.
            specific values for underflow_bin and overflow_bin are not set.

        For example, underflow_bin could be -999, and overflow_bin could be the
        upper edge of the last bin.

        valid can be set to any user defined function which returns
        True or False.

        """

        if boundaries is None:
            if lows is None or ups is None:
                raise ValueError("Only either boundaries or pairs of lows and ups need to be given!")
            if not tuple(lows[1:]) == tuple(ups[:-1]):
                raise ValueError("Boundaries cannot be determined from lows = " + str(lows) + " and ups = " + str(ups))
            self.boundaries = tuple(lows) + (ups[-1], )
            self.lows = tuple(lows)
            self.ups = tuple(ups)
        else:
            if lows is not None or ups is not None:
                raise ValueError("Only either boundaries or pairs of lows and ups need to be given!")
            if len(boundaries) < 2:
                raise ValueError("Needs at least one bin! boundaries = " + str(boundaries))
            self.boundaries = tuple(boundaries)
            self.lows = tuple(boundaries[:-1])
            self.ups = tuple(boundaries[1:])

        supportedRetvalues = ('number', 'lowedge')
        if retvalue not in supportedRetvalues:
            raise ValueError("The retvalue '%s' is not supported! " % (retvalue, ) + "Supported values are '" + "', '".join(supportedRetvalues)  + "'")

        self.lowedge = (retvalue == 'lowedge')
        if self.lowedge:
            if bins is not None: raise ValueError("bins cannot be given when retvalue is '" + retvalue + "'!")
            if underflow_bin is not None: raise ValueError("underflow_bin cannot be given when retvalue is '" + retvalue + "'!")
            if overflow_bin is not None: raise ValueError("overflow_bin cannot be given when retvalue is '" + retvalue + "'!")

        if self.lowedge:
            self.bins = self.lows
            self.underflow_bin = float("-inf")
            self.overflow_bin = self.ups[-1]
        else:
            self.bins = bins if bins is not None else tuple(range(1, len(self.lows) + 1))
            self.underflow_bin = underflow_bin if underflow_bin is not None else min(self.bins) - 1
            self.overflow_bin = overflow_bin if overflow_bin is not None else max(self.bins) + 1

        self._valid = valid

    def __repr__(self):
        return '{}(boundaries = {!r}, underflow_bin = {!r}), overflow_bin = {!r}), valid = {!r})'.format(
            self.__class__.__name__,
            self.boundaries, self.underflow_bin, self.overflow_bin, self._valid
        )

    def __str__(self):
        ret = '{:>5} {:>10} {:>10}\n'.format('bin', 'low', 'up')
        return ret + "\n".join('{:>5} {:>10} {:>10}'.format(b, l, u) for b, l, u in zip(self.bins, self.lows, self.ups))

    def __call__(self, val):
        """main function of this class. returns the bin to which val belongs.

        SPECIFY INPUT PARAMETER AND RETURN USING GOOGLE PY FORMAT
        DONT REPEAT INFORMATION FROM CLASS DESCRIPTION
        
        if val is not valid, None is returned.  If the default value of valid set in __init__
        is not changed from returnTrue, then __call__ will never return None.  If this default
        value of valid set in __init__ is changed from returnTrue, then users must check that
        the return value of __call__ is not None.
        
        the upper bin boundary defined with __init__ belongs to the next bin, not the current
        bin.  If val passed to __call__ is the upper edge of a bin, then the value belongs
        to the next bin.

        if val is equal to the lower edge of bin J, then val belongs to bin J.
        
        """
        if not self._valid(val): return None
        if val < self.lows[0]: return self.underflow_bin
        if self.ups[-1] <= val: return self.overflow_bin
        return [b for b, l, u in zip(self.bins, self.lows, self.ups) if l <= val < u][0]

    def next(self, bin):
        """given one bin, this method returns the next bin.
        
        SPECIFY INPUT PARAMETER AND RETURN USING GOOGLE PY FORMAT
        DONT REPEAT INFORMATION FROM CLASS DESCRIPTION
        

        __call__ is called first to determine the correct current bin (this is tricky
        for bins whose edges are floating point values)
        
        if bin corresponds to underflow bin, then this function returns the lowest
        bin (just above underflow bin)

        if bin corresponds to overflow bin, then this function returns the overflow
        bin

        if bin corresponds to the last bin, then this function returns the overflow
        bin

        """
        if self.lowedge:
            # call self._call__() to ensure that the 'bin' is indeed one of the
            # bins.
            bin = self.__call__(bin)

        if bin == self.underflow_bin: return self.bins[0]
        if bin == self.overflow_bin: return self.overflow_bin
        if bin == self.bins[-1]: return self.overflow_bin
        return self.bins[self.bins.index(bin) + 1]

##__________________________________________________________________||
