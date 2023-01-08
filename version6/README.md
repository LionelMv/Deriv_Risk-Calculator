Version6:
Improvements done on version5
Renamed instruments module to get_details.
On get_details module:
    - Added function to handle negative values when getting number of pips.
Mistake on v501s module:
    - lowest_lot and lowest_allowable_lot had been interchanged giving incorrect results
    for both lot size and total risk.
Improved documentation (README.md files) for all versions.


Version5:
- Based off version4
- Modularized version of all. Most code is optimized.
- The addition of a separate file to get the lot-size and risk.
- This provides a good template for adding other instruments with less code.

Recommendations for next changes on problems_to_tackle.md and:
 - Creating a file for all instruments to be called.
 - Is there a way to optimise get_lot code?
 - If it is going to be a webpage then mostly return values will be needed and not prints.
 - Creating a webpage and database for this project.


Version4:
- Created from version2 and version3.
- Version2 was the base i.e. calculations optimized to help in optimizing code.
- Version3 shows ways to make the project more modular.
- Created a stable version that is working and has variables that can be used to optimize code.


Version3:
- It is based off version1 but introduces classes.
- Modularization is started in this version to help in re-use of code without repeating code.
- A lot is still needed be optimized to cater for additional instruments to be added.
- Combining this version and version2, creates version4.


Version2:
- It is based off version1.
- It seeks to reduce the number of constants used in the code so that a lot of parts can be re-used.
- This was done by re-evaluating all the calculations needed to get the final lot-size and the risk.
- This aided in the creation of version4. (It was the base on which version4 uses its formulas).


Version1:
- The template of the basics of the risk calculator.
- It shows which variables to think about and what we are trying to accomplish.
- V501s instrument is used as a base for test.
