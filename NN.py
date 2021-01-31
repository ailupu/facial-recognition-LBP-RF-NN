def NN(img1,hist):
    l_medii = list()
    suma = list() 
    for i in range(len(hist)):
        l_medii.append([])
        for j in range(len(hist[i])):
            if img1 == hist[i]:
                continue
            else:
                l_medii[i].append(img1[j]-hist[i][j])

                    
    for i in range(len(l_medii)):
        a = 0
        b = 0
        for j in range(len(l_medii[i])):
            a = abs(l_medii[i][j])
            b += a

        suma.append(b)
        
    return suma

