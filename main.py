def main():

    while True:
        user_input = input("Enter a integer value:")
        
        try:
            number = int(user_input)
            if number > 0 and number < 100:
                break
        except ValueError:
            pass
        
                        
    print(number)

    ########################################
    # Do not delete the return statement
    ########################################
    return number


if __name__ == '__main__':
    main()
