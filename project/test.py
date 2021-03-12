pairs = {
    1:2,
    2:3,
    3:4
}
idf = {}
for key in pairs.keys():
    if key in idf:
        idf[key] += 1 
    else:
        idf[key] = 1
print(idf)
for key in pairs.keys():
    if key in idf:
        idf[key] += 1 
    else:
        idf[key] = 1
print(idf)