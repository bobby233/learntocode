#Created by bobby233. Github: https://github.com/bobby233/learnpython
#Version: V1.0.0


#Let's use '%' to solve the problem of the score's growth rate.
#We have 2 Tom's scores here.
oldscore = 75
newscore = 88

#Tom wants to know the growth rate of his scores.
#Let's use '%' to help him.

#Way 1:
print('%s, your scores growth rate is %d%%' % ('Tom', (newscore-oldscore)/newscore*100))
#'%s' means the first string in the brackets behind the last '%'.
#'%d' means the first whole number in the brackets.
#'%%' means the '%' in normal string.
#The things in the brackets provides things to print.
#You can even calculate in the brackets.

#Way2:
name = 'Tom'
rate = '%d%%' % ((newscore-oldscore)/newscore*100)
print(name, ', your scores growth rate is', rate)
#This is very similar to Way1, but has one more space.
#But the explainer has more things to explain.
#And is not pretty in format.

#Do you know the usage with the '%' ?