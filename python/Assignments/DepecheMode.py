def main():
    depechemode=open('C:\Binus CS\PGM\DepecheMode.pgm', 'br')
    new_files=open('C:\Binus CS\PGM\InvertDepecheMode.pgm', 'bw')
    x=list(depechemode.read())
    y=[]
    for i in range (0, 14):
        y.append(x[i])
    for i in range(14, len(x)):
        y.append(255-x[i])
    new_files.write(bytes(y))
    depechemode.close()
    new_files.close()
main()
