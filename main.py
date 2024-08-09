# def is_even(num):
#     if num %2 == 0:
#         print("Even")
#     else:
#         print("Odd")


# '''
# Take input from user and print if it is orr or even.
# '''

# # taking input from user and storing in on variable named 'user_input"
# # Note: We have to typecast to int since input() takes any input in string form.



# user_input = int(input("Enter a number: ")) 

# # lets check the type of the input (for info only)
# # print(type(user_input))

# is_even(user_input)


counter = 0
while counter<10:
    # run some code here
    print("Value of counter: ",counter)
    counter = counter + 2
    
    if counter == 6:
        print("yoo break the loop!")
        break

print("final value ", counter)



def new_function():
    print("Function created for git class.")