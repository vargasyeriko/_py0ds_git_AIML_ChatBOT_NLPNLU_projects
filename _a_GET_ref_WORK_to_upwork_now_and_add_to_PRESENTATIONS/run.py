
import sys;import io ; original_stdout = sys.stdout ; sys.stdout = io.StringIO()          # Suppress this output
exec(open(f"/Users/yerik/_apple_source/PY/GLOBAL/_1_paths.py", encoding="utf-8").read())  # GLOBAL
sys.stdout = original_stdout  

# USER INPUTS
str_ref_job_desc = input("Instert JOB Description ::: \n ")




# USER INPUTS
                                      # Reset Suppress
#packages
import pyperclip
from datetime import datetime


#
exec(open(f"{direc}/functions/_0ds_fn_1_get_ipynb_file_names.py", encoding="utf-8").read()) 
#
# see current files in PRESENTATIONS
folder_path = f'{direc}/JUPY_PRESENTATIONS'
list_jupy = list_all_ipynb_files(folder_path)
print('LIST OF DOCS IN PRESENTATIONS :: ',list_jupy)
#
exec(open(f"{direc}/functions/_0ds_fn_3_NLP_match_job_desc_and_ref_work.py", encoding="utf-8").read())
#
# Find the best matching notebook title  *** NLP ***
#
ref_notebook = find_best_match(str_ref_job_desc, document_titles)
print(f"\n ATTN !! NLP -> The best matching notebook is: {ref_notebook}")
#
#ref_notebook = list_jupy[2] # MANUALLY DECIDE # -------------------------------------------------USER INPUT
#
source_file = f'{direc}/JUPY_PRESENTATIONS/{ref_notebook}'
#
# The name of the output file
ref_new_name     = f'_a_copy_of_{ref_notebook}'
ref_name_out_path = f'{desk_path}/upwork_now/'
ref_name_out_pdf  = f'{ref_new_name[:-6]}.pdf'
#
# FN fields
notebook_file = source_file
output_file = ref_new_name
#
exec(open(f"{direc}/functions/_0ds_fn_2_copy_ipynb_file.py", encoding="utf-8").read())
# 
print(f'\n {ref_notebook} :: has been copied here :: \n -> {direc}')
print(f'\n with this new name \n -> {ref_new_name} ... & ...')
#
# # TRANSFORM TO PDF
from nbconvert import PDFExporter
pdf_exporter = PDFExporter()
pdf_data, resources = pdf_exporter.from_filename(f"{direc}/{ref_new_name}")
with open(f"{direc}/{ref_name_out_pdf}", "wb") as f:
    f.write(pdf_data)
print(f' \n Transformed it to PDF as :::\n -> {ref_name_out_pdf}')
#
# GET WORDS from chosen work ref to be edited for further job_descr custom reference porfolio sample
#
exec(open(f"{direc}/functions/_0ds_fn_4_get_description_to_modify_in_ref_work.py", encoding="utf-8").read())
#
print('done')
how_many_words = 400 # ---------------------------------------------------------------------------USER INPUT
#
# NEXT FN gives us the WORK REF to be modified
#
pdf_path = f'{direc}/{ref_name_out_pdf}'
str_ref_work = read_ref_work_words(pdf_path)
#
print('done')
# FOR CHAT GPT
chat_gpt_stat = f'''!!! !!! HEY YOU !!! PLEASE GO AHEAD AND USE THIS REF WORK enclosed by 
                <<< ref_work >>> and match it with job description enclosed by
                <(( job_desc ))> and give me a new angle to word my ref work to make it more relatable 
                to job_desc thus give me new intro starting by a new relatable title followed by Yeriko Vargas
                :::
                
<<< {str_ref_work} >>>
                
                :::
                
<(( {str_ref_job_desc} ))>
                
                PLEASE GIVE ME THE DESCRIPTION and summary in a code like square so I can just 
                do copy code as jupy markdown, for the new markdown rmemeber to set the first 
                markdown # most relatable title for this reference work by Yeriko Vargas
'''
pyperclip.copy(chat_gpt_stat) # copies it to clipboard



print('\n JOB DESC & WORK REF to MODIFY <<< ::: <<< COPIED to CLIPBOARD as follows ::: >>> ::: >>> ::: >>>')
print('_____________________________________________________________________________________________________start ')
print('_____________________________________________________________________________________________________ \n\n'
      ,chat_gpt_stat)
print('_____________________________________________________________________________________________________ ')
print('_____________________________________________________________________________________________________end ')
print('_________________________________STEP_1_C_GPT_&_PASTE___________________________________________________ ')

# NEW CHAT GPT WINDOW TO PASTE related-WORK to be modified
import webbrowser; safari = webbrowser.get("safari"); safari.open('https://chat.openai.com', new=1)
#
# GO MODIFY and save new REF work
#
import subprocess
rsp_1 = input(' RSP 1) ::: Did you GET new REF WORK DESCRIPTION *y* to open and modify ?? <y/n> \t')
if rsp_1 == 'y':

    # OPEN AND MODIFY
    to_modify = f"\n\n jupyter notebook {direc}/'{ref_new_name}'"
    print(f'{to_modify} ---> COPIED TO CLIPBOARD')

    pyperclip.copy(to_modify)
    #
    # OPEN NOTEBOOK trhough terminal to MODIFY 
  

    # Get clipboard content
    clipboard_content = subprocess.getoutput('pbpaste')

    # Open a new Terminal window and run the clipboard content
    command_to_run = f'tell application "Terminal" to do script "{clipboard_content}"'
    subprocess.Popen(["osascript", "-e", command_to_run])

#
rsp_2 = input( ' \nRSP 2) ::: Did you Modified it *y* to get instant TITLE else write CUSTOM ??? <y/n> \t')
#
if rsp_2 == 'y':
    #
    exec(open(f"{direc}/functions/_0ds_fn_5_get_title_of_new_work_ref.py", encoding="utf-8").read())
    #
    new_name_upwork = get_first_markdown_title(f'{direc}/{ref_new_name}')
    print("\n new_name_upwork  =  The TITLE extracted from the notebook is:\n -> ", new_name_upwork)
if rsp_2 == 'n':
    new_name_upwork = input('new_name_upwork  = CUSTOM TITLE ::: ')  # -------------------------user_input

#print('CHECKPINT')    
# EXPORT TO upwork now 

# after modifying the file 
#
# 1a # change it to a pdf
#
# # TRANSFORM TO PDF and send it to ---------- > upwork_now
from nbconvert import PDFExporter
pdf_exporter = PDFExporter()
pdf_data, resources = pdf_exporter.from_filename(f"{direc}/{ref_new_name}")
with open(f"{ref_name_out_path}/{new_name_upwork}.pdf", "wb") as f:
    f.write(pdf_data)
#
# 2a # save modified notebook to presentations 
#
print('CH')

# notebook_file = ref_new_name
# output_file = f'{direc}/JUPY_PRESENTATIONS/{new_name_upwork}.ipynb'
# exec(open(f"{direc}/functions/_0ds_fn_2_copy_ipynb_file.py", encoding="utf-8").read())
# print(f'\n {notebook_file} :: ATTN !! after being modified has been copied here as :: \n -> {output_file} ')

# print('CH')

import os

def delete_files(file_list):
    for file_path in file_list:
        try:
            os.remove(file_path)  # ^^^ path ^^^
            print(f"Successfully deleted {file_path}")
        except FileNotFoundError:
            print(f"File {file_path} not found")
        except PermissionError:
            print(f"Permission denied for {file_path}")
        except Exception as e:
            print(f"An error occurred: {e}")

# Example usage
file_list_to_delete = [f'{direc}/{ref_new_name}' ,f'{direc}/{ref_name_out_pdf}']  # Add your file paths here
delete_files(file_list_to_delete)



    
    
