def main():

    user = input()

    user_result = conversion(user)
    print(user_result)

def conversion(user):
    user1 = user.replace(":)", '🙂')
    user2 = user1.replace(":(", '🙁')

    return user2
main()

