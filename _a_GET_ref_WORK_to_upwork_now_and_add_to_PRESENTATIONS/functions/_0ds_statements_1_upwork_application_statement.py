
custom_instructions_upwrk_about_me = ''' 
Work exp:-------------------->(>3.5 years)--------------------

By now I have over 3 and a half years of professional experience in the field of ML DL acting as a data scientist.

Python R:--------------> 8 years
Stats and Math:--------> 10 years 
SQL and Hadoop :-------> 3 years
Tableau:---------------> 3 years

FORD |                                                                                                                          
Lead Data Scientist (contract)

•	Managed, manipulated, and analyzed big data from CVDOS data base which captured more data in the last 2 years compared to previous 50 years count using python to fulfill internal client data requirements
•	Acted as an expert transforming, merging, and visualizing data sets using python and internal AWS Sage maker services with Jupiter notebooks to send statistics reports and updates daily

Soothsayer Analytics | Livonia, MI                                                                                                   Machine Learning Researcher (full time)

Fiat Chrysler Automotive | Auburn Hills, MI                                                                                       
Deep Learning Specialist (contract)

Master of Science in Applied Statistics | Oakland University, Auburn Hills, MI                                                 May 2020
Bachelor of Science in Applied Statistics | Oakland University, Auburn Hills, MI                                              Apr 2017


'''


custom_instructions_upwrk_respond ='''


I need you to write the proposals as if you were looking at the mean of responses, and give me always the tone of the writing. like retrospect and think, the pool of answers at least 51% of the recruiters will say yes. I will just add, not too funny, but have some humor, and not too serious, seem excited and surprised, but don't come across arrogant or as "trying too hard"

Be concise on the intro and the small talk, but when there is opportunity to connect to what the job seeker looks for, then go more on that and how my work experience relates.

do Always give me a plan like milestones of project with a decent timeline to finish them. always have a signature at the bottom
'''

chat_gpt_stat_prop =f''' after (1) learning about the job opportunity I am deiciing to apply and (2) knowing the work 
                reference we summarized together, now build a formal proposal with the following work experience
                of mine, as well as my education, which I will ask you to show case in a organized way.\n\n
                
                <<< start: in between these symbols custom_instructions_upwrk_about_me >>>
                
                <<< {custom_instructions_upwrk_about_me} >>> \n\n
                
                
                *** in between these symbols custom_instructions_upwrk_respond ***
                
                *** {custom_instructions_upwrk_respond} *** \n\n
                
                Lastly (1) Ask me if I want to add milestones? and 
                (2) Hey Yeriko are there any custom questions that the proposal is showing  
                Just if I answer you those questions you can continue. Go ->
                
                    

'''
pyperclip.copy(chat_gpt_stat_prop)
print(' print(chat_gpt_stat_prop) to see what is copied to CLIPBOARD - > go PASTE TO CHAT GPT to get PROPOSAL !!! ')
