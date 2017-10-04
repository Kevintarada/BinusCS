def main():
    robertsmith=open('C:\Binus CS\PGM\RobertSmith.pgm', 'br')
    new_files=open('C:\Binus CS\PGM\InvertRobertSmith.pgm', 'bw')
    x=list(robertsmith.read())
    y=[]
    for i in range (0, 14):
        y.append(x[i])
    for z in range(14, len(x)):
        y.append(255-x[z])
    new_files.write(bytes(y))
    robertsmith.close()
    new_files.close()
main()
