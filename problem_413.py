#!/usr/bin/env python

one-child numbers
https://projecteuler.net/problem=413

alleged answer here:
https://www.tapatalk.com/groups/eulersolutionsfr/problem-413-t222.html

idea:
we look for multiples of d as substrings.
count the number of numbers in which two multiples of d are present as substrings.
look for numbers where d and d are present exactly once each (in this case d happens twice).
then d and 2d
then d and 3d
keep going until nd is the largest multiple of d such that len(d) and len(nd) = d.

start over, looking for 2d and 2d
then 2d and 3d
etc.

keep going until the first substring that is a multiple of d (call it kd)
is the largest multiple of d where the number of digits in kd is d/2.

consider 12-digit numbers

------------

how many times can the substring 12 appear in a 12 digit number exactly twice?
we care about exactly twice because with the patterns
1212--------
12--12------

the number
121212121212

matches both and we only want to count it once.

