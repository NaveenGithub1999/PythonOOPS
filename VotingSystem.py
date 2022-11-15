print("****Welcome to Election commission of india****")
people_1 = input("Enter your 1st name: ")
people_2 = input("Enter your 2nd name: ")
cand_votes1 = 0
cand_votes2 = 0
voters_id = [101,102,103,104,105]
no_of_voters = len(voters_id)
print(f"no of voter ",{no_of_voters})
voted = []
while True:
    if voters_id==[]:
        print("voting is over")
        if cand_votes1>cand_votes2:
            print(f'candidate {people_1} is win',{cand_votes1})

        elif cand_votes2>cand_votes1:
            print(f'candidate {people_2} is win',{cand_votes2})

        elif cand_votes2==cand_votes1:
        
            print("Tie!!")
        break    
    else:
        voter = int(input("Enter your id: "))
        if voter in voted:
            print("you already voted")
        else:
            if voter in voters_id:
                print(f'1.{people_1}\n2.{people_2}') 
                choice = int(input("enter your choice: "))
                if choice==1:
                    cand_votes1+=1
                    print(f"you voted {people_1}:")
                elif choice==2:
                    cand_votes2+=1
                    print(f'you voted {people_2}')
                voters_id.remove(voter)
                voted.append(voter)
            else:
                print(f"invalid voter id", {voters_id})    