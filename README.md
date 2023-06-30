# Resume-Parser

How to run: Download or clone the files to your space. Keep all the files in the same folder. Ensure all the needed packages are downloaded - NLTK, Spacy, PyPDF2, docx2txt. For the resume, Keep the resume that needs to be parsed in the same folder with the name 'resume.pdf' or give the appropriate path and extension in the Main.py file. Update the jd.txt file with the required job description for which the resume is used to apply. Run the **'Main.py'** file. Results will be displayed on the console.

Detailed Explanation of All Things: A Resume can be in any format and written in any style. Our resume parser will accept some of the basic formats of the resume everyone uses, like "pdf," "docx," "doc," "odt," "rtf," Etc., and convert it into text format. The text-formatted data will be processed using Natural Language Processing techniques, and tags will be assigned accordingly. The tagged data will be used to autofill an application.

The main things we need to extract from a resume to fill an application are name, education details, experience details, phone number, email address, URLs like LinkedIn and GitHub, and technical skills of the applicant. We used simple rule-based implementation to approach the solution. The following will explain the approach used for every field.

Extracting Name:

To extract the name of the applicant, we tried two different approaches; one was to use the “PER” tagged words from spacy NER, and the other was a direct approach where we started with the assumption that the first line of the resume will always be the name of the applicant.

Extracting Phone Number:

To extract the phone number, we used the regular expression that matched a phone number and searched the text for a match. The founded match was considered as the applicant’s phone number.

Extracting Email Address:

To extract the email address, we used a similar approach to extracting the phone number. We wrote a regular expression that matched the email addresses and searched all the text for the match. The match was extracted and tagged as an email address.

Extracting URLs:

Here also used regular expressions to match URL formats and extracted all the URLs as a list. After extracting them, we tried to match the most common URLs, like LinkedIn and GitHub and separately tagged them. The rest are classified as other URLs.

Extracting Skills:

There are numerous different skills one can find in a resume. We particularly tried to parse software-related resumes with skills related to the software side. The extraction of skills cannot be done using simple regular expressions. So, to extract the skills, we initially constructed the list of skills or skills database with different skills commonly found in a resume. We hardcoded this list and saved it. Now, using NLTK, we tokenized all the words of the resume and tried to match those words with the skills list. The matched terms are separately stored in a list. Then using the NLTK bigrams and trigrams method, we created bigrams and trigrams of the previously tokenized text. These newly formed bigrams and trigrams are also searched against the skills database and matched skills appended to applicants' skills list. Finally, we applied a set to remove all the duplicate skills, sorted them alphabetically, and returned them.

Extracting Education and Experience:

These were the trickiest part. We thought of different approaches, but no approach gave good accuracy. So, we finally settled on the following approach, which performed relatively better. We initially constructed a list of fields we can find in the resume. We approached this solution assuming that the field heading would be the first or second words of the line. For education, we searched every line’s starting word to see if there was any match with “education.” For Experience, we again created a small list of words that an applicant typically used to mark the Experience field in a resume. We mapped these words with the starting words of every line, and the matched line is considered the starting line of Experience Details. The end of the fields was also determined similarly when we searched for another field match. If there is another field match, we consider the current field ended. We stored all the data of the current field separately and returned it.

Calculating Eligibility Probability:

Every job application has specific requirements that need to be met by an applicant. We tried to decide whether the applicant was eligible for a particular job role by parsing an applicant's resume. For this, we depended on the required skills for a job and the applicant's skills. We extracted the skills mentioned in the job description using the same technique we used for extracting an applicant's skills. Then, we compared both lists to find that the number of skills of the applicant matched the skills of the job description. This count was then divided by the number of skills required for the job to get the Probability. The idea is to determine a threshold value so that the applicant will be considered eligible for the job if the Probability is above the threshold; else, he is not eligible.
