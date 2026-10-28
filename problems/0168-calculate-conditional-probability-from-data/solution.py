def conditional_probability(data, x, y):
    sx = 0
    sy = 0
    for i in data:
      if i[0] == x:
        sx +=1
        if i[1] == y:
          sy += 1
    if sx == 0:
      return 0
    return sy/sx