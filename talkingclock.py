"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2023

Code Clash #18 - Talking Clock (talkingclock.py)


Author: Andrew Scott White

Difficulty Level: 8/10

Prompt: I don’t want to be late for the BWSI Grand Prix, so I want
to program my phone to update me on the time. Can you help me make 
a Talking Clock? I need a script that takes an input 24-hour time 
(00:00 - 23:59) and translates it into words. Please format the input 
as ‘##:##’ and include am/pm in the output string. Thanks!

Test Cases:
Input: 12:00  Output: It's twelve pm

Input: 23:59  Output: It's eleven fifty nine pm

Input: 12:05  Output: It's twelve oh five pm
"""




    # This will convert military hours to regular hours, and determine AM vs PM
class Solution:    
    def ClockTalker(self, input_time):
        hour= input_time[0:2]
        min1=input_time[3]
        min2=input_time[4]
        if int(hour)>=12:
            ampm=" pm"
        else:
            ampm=" am"
        hour=int(hour)
        if int(hour)>12:
            hour=int(hour-12)
        if hour==0:
            hour+=12
        hourL=["","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve"]
        min1L=[" oh"," oh"," twenty"," thirty"," forty"," fifty"]
        min2L=[""," one"," two"," three"," four"," five"," six"," seven"," eight"," nine"]
        min2teenL=[" ten"," eleven"," twelve"," thirteen"," fourteen"," fifteen"," sixteen"," seventeen"," eighteen"," nineteen"]
        if min1=='0':
            if min2=='0':
                mins=''
            else:
                mins="oh "+min2L[int(min2)]
        elif min1=='1':
            mins=min2teenL[int(min2)]
        else:
            mins=min1L[int(min1)]+min2L[int(min2)]
        print("It's "+str(hourL[hour])+str(mins)+ampm)
            #type input_time: string
            #return type: string
            
            #TODO: Write code below to return a string with the solution to the prompt.

def main():
     str1=input()
     tc1= Solution()
     ans=tc1.ClockTalker(str1)
     print(ans)
    
if __name__ == '__main__': 
    main()
        