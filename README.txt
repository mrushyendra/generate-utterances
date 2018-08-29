Adding sample utterances for each intent can be quite tedious, as there are numerous permutations and combinations possible. For example, there could be variation in the number of slots a user mentions. They might say "Transfer money to John from savings account", "Transfer money to John", or simply "Transfer money". Likewise, they might use several different synonyms in the same intent - "Transfer money", "Send cash" or "Send money".

To reduce the time needed to type all these various permutations, you can use the Generate Utterances utility. Given an input string like "(Transfer | Send) (money | cash | funds) to {recipient}", the utility generates all possible permutations of the given input string:
	
	Transfer money to {recipient}
	Send money to {recipient}
	Transfer cash to {recipient}
	Send cash to {recipient}

To use the utility, simply create a text file with all your various input strings, each in its own line. The syntax for input strings is very simple: to indicate that the utility can decide between two options, enclose the options in parentheses '()' and separate the options using the '|' character. You can indicate that a word(s) is optional using the same syntax, by leaving an option blank - i.e. "(Please | ) transfer money".

Run the python script with the following command line args:
python generateUtterances.py inputFileName outputFileName

You should see the output utterances in outputFileName. Simply copy and paste any utterances of your choice from the file into the console.



