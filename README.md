# Flexible File upload & Validation Rule Engine
Repo for Dell H2H

Develop a UI that will allow template definition for a given file and allow us to define rules for each attribute.  For eg: If you are uploading a customer file, need all the field in the definition template and add validation routines for each attribute / field. 
Once the template is setup, user can start uploading the files. Each record in the file must be validated against the rules defined in the template. The text/csv files can have thousands of records.
Error records should be logged and flagged. 
The file should be uploaded to an object store after successful validation
The file can be read from the object store using S3 APIs. 

When user changes the template rules, the validation should also change accordingly. 
![](https://raw.githubusercontent.com/Sahithi-Venkatesan/Flexible-File-Upload-and-Validation-rule-engine/main/Screenshot%20(576).png?token=AKDDZXDWLTSYFA7LAATS3OK72ZYYU)
![](https://drive.google.com/file/d/1Z-5geeyJDMJZPvCmFrVnwVAgGiFYBWiF/view?usp=sharing)
