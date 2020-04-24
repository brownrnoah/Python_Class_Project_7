"""
Noah Brown
April 16th, 2020
CS1410-602
Project 7
"""

import requests, time
from concurrent.futures import ThreadPoolExecutor

def download(flag):
    prefix = 'https://www.cia.gov/library/publications/resources/the-world-factbook/graphics/flags/large/'
    flagUrl = prefix + flag + "-lgflag.gif"
    response = requests.get(flagUrl).content
    
    if response:
        with open("flags_c/" + flag + ".gif","wb") as f:
            f.write(response)
            
        return len(response)
    
def main():  
    with open("flags.txt") as f_file:
        flags = (line.strip() for line in f_file)
    
        numBytes = 0
        startTime = time.perf_counter()
        with ThreadPoolExecutor() as p:
            numBytes = sum(p.map(download,flags))
        endTime = time.perf_counter()
        
    with open("flags_c_results.txt", "w") as results:
        timeString = "Elapsed time: " + str(endTime - startTime) + "\n"
        results.write(timeString)
        bytesString = str(numBytes) + " bytes downloaded"
        results.write(bytesString)
        results.close()


if __name__ == "__main__":
    main()