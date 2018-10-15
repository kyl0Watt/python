def accumulate(collection, operation):
    accumulator = list()
    for i in collection:
        accumulator.append(operation(i))
    return accumulator
