def distance(strand_a, strand_b):
    if len(strand_a) == len(strand_b):
        distance = 0
        for a, b in zip(strand_a, strand_b):
            if a != b:
                distance += 1
        # for i in range(len(strand_b)):
        #     if strand_a[i] != strand_b[i]:
        #         distance += 1
        return distance
    else:
        raise(ValueError('Strand lengths do not match'))
