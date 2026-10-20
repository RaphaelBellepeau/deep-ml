def empirical_pmf(samples):
    if samples == []:
        return []
    else:
        out = []
        current = samples[0]
        s = 0
        for x in samples:
            if x == current:
                s += 1
            else:
                out.append((current, s/len(samples)))
                current = x
                s = 1
        out.append((current, s/len(samples)))
        return out

