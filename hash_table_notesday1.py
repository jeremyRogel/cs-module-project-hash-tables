#step 1 of hashing - make the string into a integer

def my_hash(s):
    sb = s.encode() # makes string into integer usuing UTF-8 notation

    total = 0
    for b in sb:
        total += b #adds all of the integer values together
    
    return total%8 #returns tsum of all integers in the string(%8 gets a value that is in the list of <10)

i = my_hash("jeremy")


hash_table = [None] * 8

hash_table[i] = "8 months"

##hash jeremy
##retrieve value at that hash

def get_length_timeatlambda(e):
    curr_hash = my_hash(e) #where was jeremy hashed (index value of it)
    return hash_table[curr_hash]

length_jeremy = get_length_timeatlambda("jeremy")

print("jeremy has worked at lambda for " + length_jeremy )

#step 1 - hash jeremy -> constant (0(1))
#step 2 - index into the list based on the hash -> constant (0(1))

# given a string containign just the characters '(' ')' '{' '}' '[' and ']' determine if the input string is valid
# 1.open brackets must be closed by the same type of brackets
# 2. open brackets must be closed in the correct order
# note that an empty string is also valid

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ## given a string of just parentheses
        ## go through the string
        ## keep track if something is the correct closing parentheses
        ## O(N) where n is length of the string
        ## {[]}
        stack = []
        par_mapping = {"}" : "{", "]" : "[", ")" : "("}
        for p in s:
            if p in par_mapping:
                if len(stack) == 0:
                    return False
                most_recent = stack.pop()
                if par_mapping[p] != most_recent:
                    return False
            else:
                stack.append(p)
        if len(stack) != 0:
            return False
        return True