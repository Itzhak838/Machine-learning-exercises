import logistic_regression as lr


def classify(modelfile, dsfile):
    ds = []
    model = []
    result = []
    try:
        with open(modelfile, 'r') as model_file:

            for line in model_file:
                model.append([float(x) for x in line.split(',')])
    except IOError:
        print("File not found or path is incorrect")
    try:
        with open(dsfile, 'r') as ds_file:
            for line in ds_file:
                ds.append([int(x) for x in line.split(',')])
    except IOError:
        print("File not found or path is incorrect")
    for i in range(len(model[0])):

        model[0][i] = round(float(model[0][i]), 3)
    classify_val = lr.read_DS(dsfile)

    for i in classify_val:
        result.append(lr.classify(model[0], i))
    final_ds = open(dsfile, 'w')
    num = 0
    for line in classify_val:
        for val in range(len(line) - 1):
            final_ds.write(str(line[val]) + ',')
        final_ds.write(str(result[num]) + '\n')
        num += 1
