# Request Identifier 
### Visma Solutions Summer Trainee programming task

The task seemed fairly straightforward after a couple of read-throughs, and while it didn't present any major difficulties, it had me scratching my head here and there. I think the biggest challenge for me was validating the parameter values. It took some figuring out to understand and decide what parts of the input string to validate - in the end I chose to assume that the URIs to be identified will be more or less in the correct format (scheme://path?parameter=value&...), so the program will crash if given a string that can't be split at the expected places, for example. A possible improvement then would be checking the format of the input.

I aimed to build a working solution within the time constraints, but perhaps the `validate_parameters` method with it's large amount of if statements could look prettier. The validation dilemma shows here: I wasn't entirely sure how much validation I should be doing. My solution assumes that `source` and `documentid` should include at least one letter of the alphabet, as per the examples in the instructions. I also check that the number of parameters is exactly correct for any allowed path, but somehow this feels like a workaround. I think this method could be improved further.

However I'm pretty happy with my implementation and I didn't have to make any major compromises to get the task done.

