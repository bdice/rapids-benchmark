__version__ = "0.0.14"

def setFixtureParamNames(request, orderedParamNameList):
    """
    Given a request fixture and a list of param names ordered based on the order
    the params are specified for a parameterized fixture, this will set the
    names so reporting tools can label the parameterized benchmark runs
    accordingly.  This is only needed for parameterized fixtures, since
    parameterized benchmarks already assign param names to param values.

    Order matters. For example, if the fixture's params are set like this:
    params = product([True, False], [True, False])

    and the param names are set like this:
    orderedParamNameList = ["managed_memory", "pool_allocator"]

    then the reports show the options that were set for the benchmark like this:
    my_benchmark[managed_memory=True, pool_allocator=True]
    my_benchmark[managed_memory=True, pool_allocator=False]
    my_benchmark[managed_memory=False, pool_allocator=True]
    my_benchmark[managed_memory=False, pool_allocator=False]

    orderedParamNameList can have more params specified than are used. For
    example, if a fixture only has 2 params, only the first 2 names in
    orderedParamNameList are used.

    NOTE: the fixture param names set by this function are currently only used
    for ASV reporting.
    """
    # This function can also be called on a single test param, which may result
    # in request.param *not* being a list of param values.
    if type(request.param) is list:
        numParams = len(request.param)
    else:
        numParams = 1

    if len(orderedParamNameList) < numParams:
        raise IndexError("setFixtureParamNames: the number of parameter names "
                         "is less than the number of parameters.")

    request.keywords.setdefault(
        "fixture_param_names",
        dict())[request.fixturename] = orderedParamNameList[:numParams]
