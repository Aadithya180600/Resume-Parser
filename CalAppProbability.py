from ResumeParser import ResumeParser

class CalAppProbability:

    # Initialization
    def __init__(self) -> None:
        self.eligibility_probability = 0 # Declaring Eligibility Probability and initializing to 0
        self.threshold = 0.75 # Declared manually for testing
        self.eligible = "This resume did meet the requirements of the job. The applicant is eligible for the role"
        self.noteligible = "This resume did not meet the requirements of the job. The applicant is not eligible for the role"

    # Method for Constructing Eligibility Probability
    def CalEligibilityProbability(self):
        resumeParser = ResumeParser()
        resumeParser.ExtractingSkills()
        applicantSkills = resumeParser.skills
        jd_f = open('jd.txt', 'r')
        job_description = jd_f.read()

        required_skills = resumeParser.ComparingTextwithSkills(job_description)
        count_skills = 0
        for i in applicantSkills:
            if i in required_skills:
                count_skills+=1

        self.eligibility_probability = count_skills/len(required_skills)
    
    # Method to say is eligible or not
    def isEligible(self):
        if self.threshold <= self.eligibility_probability:
            return self.eligible
        return self.noteligible

    
    # Method for Printing Data
    def PrintingEligibilityProbability(self):

        # Printing eligibility Probability
        print("Eligibility Probability: " + str(self.eligibility_probability))
        print()

        #printing Is Eligible or not
        print(self.isEligible())