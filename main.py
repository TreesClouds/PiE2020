def convert_time(num):
  
    split = list(str(num))
    
    while len(split) < 4:
      split.insert(0,"0")
      
    print(split)
    
    hour = split[0] + split[1]
    fmin = split[2] + split[3]
    
    fmin = int(fmin)
    hour = int(hour)
    
    if hour > 12:
      fhour = hour - 12
    else:
      fhour = hour
    
    print([fhour, fmin]) # fhour is final hour amount, fmin is final minute amount
    
convert_time(359)