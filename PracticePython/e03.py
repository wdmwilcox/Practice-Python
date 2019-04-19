from sys import argv

def populate_list(argv):
    user_list = []
    try:
        for i in argv[1:]:
            user_list.append(i)
        else:
            print('Please provide exactly one list')
            print(f'You provided {len(argv)} items.')
    except:
        print('Something went wrong')
        exit(1)

def return_less_than_five(user_list):
    for num in filter(lambda x: x < 5, user_list):
        print(num)

def main():
    user_list = populate_list(argv)
    return_less_than_five(user_list)
    exit(0)

main()
