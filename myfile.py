import sys
import math
import stdio, stdarray, stdrandom, stddraw, stdaudio # type: ignore

def tone(freq: float, t: float) -> list[float]:
    s: list[float] = [0] * int(44100 * t)#1/44100 is the smallest time interval the speaker can reach.
    for i in range(len(s)):
        s[i] = math.sin(freq * (2 * math.pi *i)/44100)
    return s 

def main() -> None: # Need the return type for mypy to type-check the body
    freq: float = float(sys.argv[1])
    duration: float = float(sys.argv[2])
    displacements: list[float] = tone(freq, duration)
    #for i in range(len(displacements)):
        #stddraw.point(i/44100, displacements[i]/2+0.5)
    
    density = 70
    mylist = newmap(density)
    for i in range(0,density**2):
        stddraw.point(mylist[i][0],mylist[i][1])
    
    stddraw.show()
    
    stdaudio.playSamples(displacements)

def newmap(numpoints)->list:
    thelist = []
    for i in range(0, numpoints):
        for i2 in range(0,numpoints):
            thelist.append([i/numpoints,i2/numpoints])
    return thelist



if __name__ == "__main__":
    main()
                                                                
