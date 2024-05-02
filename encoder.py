def encode(label):
    """Encoder for Concept.
    
    Parameter
    ---------
    label: str
        Label to encode.
        
    Returns
    -------
    code: list of lists of integers
        Each list corresponds to a marker, starting with the green (main concept).
        The first element of each list is the concept, the others are the attributes.
        There are at most 5 lists, each of length at most 10.
        
    Example
    -------
    Label = Honey
    Code = [[26], [6, 21, 110, 112]]
    Meaning = Food (main concept) related to bees (secondary concept) coded as yellow-and-black flying animals.
    """
    code = [[0]]
    return code
