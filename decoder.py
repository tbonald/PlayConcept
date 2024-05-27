def decode(code, candidates):
    """Decoder for Concept.
    
    Parameter
    ---------
    code: list of lists of integers
        Each list corresponds to a marker, starting with the green.
        The first element of each list is the marker (= question / exclamation mark), the others are the attributes (= cubes).
        There are at most 5 lists, each of length at most 10.
        
    candidates: list of str
        Candidate concepts.
        
    Returns
    -------
    concepts: list of str
        Concepts (up to 5, listed from the most relevant to the less relevant).
        
    Example
    -------
    Candidates = ['Apple', 'Honey', 'House']
    Code = [[26], [6]]
    Decoding = Food (main concept) related to an animal (secondary concept).
    Output = ['Honey', 'Apple']
    """
    concepts = ['']
    return concepts
