# Tai Sakuma <tai.sakuma@cern.ch>

##__________________________________________________________________||
def returnTrue(x): return True

##__________________________________________________________________||
def plusOne(x): return x + 1

##__________________________________________________________________||
class Combine(object):
    """After making an instance of the class, the main function __call__
    takes a value as an input and returns the bin to which the value
    belongs.  Instances of the Combine class merge two instances of
    other bin classes, such as Round or RoundLog, into one set of bins.
    
    UPDATE USING GOOGLE PY DOCSTRING FORMAT
    
    
    One instance is used below a specified
    threshold, and the other instance is used at or above
    the specified threshold.

 
    Instances of the Combine class create a set of bins which
    use one set of bins below a specified threshold, and a different
    set of bins for values at and above the specified threshold.
 

    The Combine class allows one variable defined with two binnings to be
    combined into one list.  An instance of this class must be created with
    three arguments:
    ``low`` -  the binning used below a specified threshold
    ``high`` - the binning used above a specified threshold
    ``at`` - the specified threshold

    an example instance of Combine is::

        low = Binning.Round(10., 100)
        high = Binning.RoundLog(0.1, 100)
        comb = Combine(low, high, at = 100)
    
    This class requires bin labels of both binnings to be values in
    the bins.

    An instance of the Combine class can be called via::

        comb(120)

    In this case, comb(120) returns 100.  In general, if the
    input value is valid, then the bin to which the value belongs
    is returned.  If the input value is not valid, then None is returned.
    If the value is equal to the low edge of bin J, then bin J is
    returned.  If the value is below the low edge of the first bin, then
    the underflow bin is returned.  If the value is above the upper
    edge of the last bin, then the overflow bin is returned.
 
    The function next requires a bin as an input parameter, and
    returns the next bin::
    
        obj.next(120)
    
    If the input parameter is the underflow
    bin, then the first bin is returned.  If the input parameter is the overflow
    bin, then the overflow bin is returned.  Each bin is identified by its
    lower edge, and next returns the upper edge of the bin (equivalent to the
    lower edge of the next bin).

    """
    def __init__(self, low, high, at):
        """initialize the two sets of bins, and the threshold 'at' where the
        binning switches from one set to the other set.
         
        UPDATE USING GOOGLE PY DOCSTRING FORMAT

        Parameters
        ---------
        low : list
    
        """
        self._low = low
        self._high = high
        self._at = at

    def __call__(self, val):
        """return the bin to which val belongs.

        SPECIFY INPUT PARAMETER AND RETURN USING GOOGLE PY FORMAT
        DONT REPEAT INFORMATION FROM CLASS DESCRIPTION
        
        """
        if val < self._at:
            return self._low(val)
        else:
            return self._high(val)

    def next(self, bin):
        """return the next bin.
            
        SPECIFY INPUT PARAMETER AND RETURN USING GOOGLE PY FORMAT
        DONT REPEAT INFORMATION FROM CLASS DESCRIPTION

        first determine if the input bin argument belongs to the
        low set of bins below the threshold 'at', or the high set
        of bins used above the threshold 'at'.
        
        Then, use the next function already defined for the low or
        high set of bins to return the next bin.

        """
        if bin < self._at:
            bin = self._low.next(bin)
            if bin < self._at:
                return bin
            else:
                return self._high(bin)
        return self._high.next(bin)

##__________________________________________________________________||
