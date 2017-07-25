def Main():
    phy=int(input("Enter your Physics Number:"))
    chem=int(input("Enter your Chemistry Number:"))
    math=int(input("Enter your Math Number:"))
    bio=int(input("Enter your Biology Number:"))
    eng=int(input("Enter your English Number:"))
    totalMark=phy+chem+math+bio+eng
    if (phy>100 or chem>100 or math>100 or bio>100 or eng>100 or totalMark>500):
        if(phy>100):
            return "You Entered Phy Mark is not vaild"
        if(chem>100):
            return "You Entered Chem Mark is not Valid"
        if(math>100):
            return "You Entered Math Mark is Not Vaild"
        if(bio>100):
            return "You Entered Bio Mark is not Valid"
        if(eng>100):
            return "You Entered Eng Mark is not Valid"
    elif (phy>30 and chem>30 and math>30 and bio>30
              and eng>30 and totalMark>400 and tatalMark<=500):
        return "Student Got Distinction"
    elif (phy>30 and chem>30 and math>30 and bio>30
              and eng>30 and totalMark>300 and totalMark<=400):
        return "Student got First Division"
    elif (phy>30 and chem>30 and math>30 and bio>30
              and eng>30 and totalMark>225 and totalMark<=300):
        return "Student Got Second Division"
    elif (phy>30 and chem>30 and math>30 and bio>30
              and eng>30 and totalMark>=150 and totalMark<=225):
        return "Student Got Third Division"
    else:
        return "Student Failed"
if __name__=="__main__":
    Main()    
