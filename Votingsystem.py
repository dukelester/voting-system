print("===========*****WELCOME TO CLASS PREFECT VOTING SYSTEM****============ \n\n")

#Enter the names of the Nominees to be voted for
nominee_one = input("Enter The Nominee 1 Name:\t")
nominee_two= input("Enter The Nominee 2 Name:\t")
nominee_three = input("Enter The Nominee 3 Name:\t")
nominee_four = input("Enter The Nominee 4 Name:\t")
nominee_five = input("Enter The Nominee 5 Name:\t")

#Store the votes of each nominee:
nominee_one_votes = 0 #initialize each nominee votes with a zero (0)
nominee_two_votes = 0
nominee_three_votes = 0
nominee_four_votes = 0
nominee_five_votes = 0

votes_id = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30] #number of votes(People to vote)

#votes_id = [1,2,3,4] #testing with 4 voters

number_of_voters = len(votes_id) #the total number of votes len() for finding the length of the list

while True: #infinite loop to allow the voters to vote
    
    if votes_id == []:
        print("====== Voting Session Over ======\n ")
        
        # votes_result = [nominee_one_votes,nominee_two_votes,nominee_three_votes,nominee_four_votes,nominee_five_votes]
        # winner = max(votes_result)
        # print("Winner")
        print("------------------The Results----------------\n")
        if nominee_one_votes > nominee_two_votes and nominee_one_votes > nominee_three_votes:
            if nominee_one_votes > nominee_four_votes and nominee_one_votes > nominee_five_votes:
                
                #Sorting the votes 
                total_votes = {
                    'nominee_one':nominee_one_votes,
                    'nominee_two':nominee_two_votes,
                    'nominee_three':nominee_three_votes,
                    'nominee_four':nominee_four_votes,
                    'nominee_five':nominee_five_votes,
                }
                
                sort_total_votes = sorted(total_votes.items(), key=lambda x: x[1], reverse=True)
                for i in sort_total_votes:
    	            print(i[0], i[1])
                # for vote in total_votes:
                #     print(nominee_one,':\t', total_votes[votes])
                
                percentage = (nominee_one_votes/number_of_voters)*100
                print('\n',nominee_one, "Worn with ", nominee_one_votes, ' votes')
                print("\nThe percentage of votes is ", percentage)
                
                print('\n===========================End of Voting========================\n')

            break #to break the inifinte loop for voting
        if nominee_two_votes > nominee_one_votes and nominee_two_votes > nominee_three_votes:
            if nominee_two_votes > nominee_four_votes and nominee_two_votes > nominee_five_votes:
                
                #Sorting the votes 
                total_votes = {
                    'nominee_one':nominee_one_votes,
                    'nominee_two':nominee_two_votes,
                    'nominee_three':nominee_three_votes,
                    'nominee_four':nominee_four_votes,
                    'nominee_five':nominee_five_votes,
                }
                
                sort_total_votes = sorted(total_votes.items(), key=lambda x: x[1], reverse=True)
                for i in sort_total_votes:
    	            print(i[0], i[1])
                
                percentage = (nominee_two_votes/number_of_voters)*100
                print('\n',nominee_two, "Worn with ", nominee_two_votes, ' votes')
                print("\nThe percentage of votes is ", percentage)
                
                print('\n===========================End of Voting========================\n')
                
            break
        if nominee_three_votes > nominee_one_votes and nominee_three_votes > nominee_two_votes:
            if nominee_three_votes > nominee_four_votes and nominee_three_votes > nominee_five_votes:
                
                #Sorting the votes 
                total_votes = {
                    'nominee_one':nominee_one_votes,
                    'nominee_two':nominee_two_votes,
                    'nominee_three':nominee_three_votes,
                    'nominee_four':nominee_four_votes,
                    'nominee_five':nominee_five_votes,
                }
                
                sort_total_votes = sorted(total_votes.items(), key=lambda x: x[1], reverse=True)
                for i in sort_total_votes:
    	            print(i[0], i[1])
                
                percentage = (nominee_three_votes/number_of_voters)*100
                
                print('\n',nominee_three, "Worn with ", nominee_three_votes, ' votes')
                print("\nThe percentage of votes is ", percentage)
                 
                print('\n===========================End of Voting========================\n')
            break
               
        if nominee_four_votes > nominee_one_votes and nominee_four_votes > nominee_two_votes:
            if nominee_four_votes > nominee_three_votes and nominee_four_votes > nominee_five_votes:
                
                #Sorting the votes 
                total_votes = {
                    'nominee_one':nominee_one_votes,
                    'nominee_two':nominee_two_votes,
                    'nominee_three':nominee_three_votes,
                    'nominee_four':nominee_four_votes,
                    'nominee_five':nominee_five_votes,
                }
                
                sort_total_votes = sorted(total_votes.items(), key=lambda x: x[1], reverse=True)
                for i in sort_total_votes:
    	            print(i[0], i[1])
                
                percentage = (nominee_four_votes/number_of_voters)*100
                print('\n',nominee_four, "Worn with ", nominee_four_votes, ' votes')
                print("\nThe percentage of votes is ", percentage)
                
                print('\n===========================End of Voting========================\n')
            break
            
        if nominee_five_votes > nominee_one_votes and nominee_five_votes > nominee_two_votes:
            if nominee_five_votes > nominee_three_votes and nominee_five_votes > nominee_four_votes:
                
                #Sorting the votes 
                total_votes = {
                    'nominee_one':nominee_one_votes,
                    'nominee_two':nominee_two_votes,
                    'nominee_three':nominee_three_votes,
                    'nominee_four':nominee_four_votes,
                    'nominee_five':nominee_five_votes,
                }
                
                sort_total_votes = sorted(total_votes.items(), key=lambda x: x[1], reverse=True)
                for i in sort_total_votes:
    	            print(i[0], i[1])
                
                percentage = (nominee_five_votes/number_of_voters)*100
                print('\n',nominee_two, "Worn with ", nominee_two_votes, ' votes')
                print("\nThe percentage of votes is ", percentage)
                
                print('\n===========================End of Voting========================\n')
                
            break
        #if they all have the same vote:
        elif nominee_one_votes == nominee_two_votes and nominee_one_votes == nominee_three_votes:
            if nominee_one_votes == nominee_four_votes and nominee_one_votes == nominee_five_votes:
                print("No Winner because they have same votes")
                
            break
                
        
        
    else:
        #display the nominees to the user to choose:
        print("1: ", nominee_one, '\n')
        print("2: ", nominee_two, '\n')
        print("3: ", nominee_three, '\n')
        print("4: ", nominee_four, '\n')
        print("5: ", nominee_five, '\n')
        
        voter = eval(input("Enter Your Voter Id:\t"))
        if voter in votes_id:#checking if the voter already exists
            print("You are a Voter!\n")
            votes_id.remove(voter) #removes the voter if the voter already exists and have voted:
            #let the voters vote:
            vote = eval(input("Who Do You Want To Vote For?\t"))
            
            #choose the person to vote for
            if vote == 1:
                nominee_one_votes +=1 #if the voter chooses 1, then add avote to nominee_one_votes
                print("Thank You For Casting Your Vote \n")
            
            elif vote == 2:
                nominee_two_votes +=1 #if the voter chooses 2, then add avote to nominee_two_votes  
                print("Thank You For Casting Your Vote \n")
                
            elif vote == 3:
                nominee_three_votes +=1 #if the voter chooses 3, then add avote to nominee_three_votes  
                print("Thank You For Casting Your Vote \n")
                
            elif vote == 4:
                nominee_four_votes +=1 #if the voter chooses 4, then add avote to nominee_four_votes  
                print("Thank You For Casting Your Vote \n")
                
            elif vote == 5:
                nominee_five_votes +=1 #if the voter chooses 5, then add avote to nominee_five_votes  
                print("Thank You For Casting Your Vote \n")
                
        else:
            print("YOU ARE NOT A VOTER HERE OR YOU HAVE ALREADY VOTED!!")
            
        
            
            
