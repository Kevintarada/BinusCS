def main():
    stevejobs=open('C:\Binus CS\PGM\SteveJobs.pgm', 'br')
    new_files=open('C:\Binus CS\PGM\InvertSteveJobs.pgm', 'bw')
    x=list(stevejobs.read())
    y=[]
    for i in range (0, 14):
        y.append(x[i])
    for z in range(14, len(x)):
        y.append(255-x[z])
    new_files.write(bytes(y))
    stevejobs.close()
    new_files.close()
main()
