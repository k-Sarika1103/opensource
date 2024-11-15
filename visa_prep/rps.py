v,c = input().split()
win_conditions = {
    'R':'P','P':'S','S':'R'
}
if v==c:
    print("NULL")
elif win_conditions[v] == c:
    print("Charan")
else:
    print("Vignesh")
