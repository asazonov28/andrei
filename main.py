def user_menu():
    user_choice = input('Please choose:\n1.Get data by ID code\n2.Check if ID is valid\n3.Exit\n-->')
    if user_choice == '1':
        condition = True
        while condition:
            try:
                user_id = input('Please enter ID: ')
                int(user_id)
                if len(user_id) != 11:
                    raise UserWarning
            except UserWarning:
                if len(user_id) < 11:
                    print('Code is too short')
                elif len(user_id) > 11:
                    print('Code is too long')
            except:
                print('Code you entered is not numeric')
            else:
                condition = False
                get_data_by_id(user_id)


    elif user_choice == '2':
        condition = True
        while condition:
            try:
                chk_id = input('Please enter last number of ID: ')
                int(chk_id)
                if len(chk_id) != 1:
                    raise UserWarning
            except UserWarning:
                if len(chk_id) > 1:
                    print('You must enter last number of ID')
            except:
                print('Code you entered is not numeric')
            else:
                condition = False
                check_if_ID_is_valid(user_id)


    elif user_choice == '3':
        quit()
    else:
        print('Choice out of range')
user_menu()


def get_data_by_id(idcode):
    gender_num = idcode[0]
    by_num = idcode[1:3]
    bm_num = idcode[3:5]
    bd_num = idcode[5:7]
    region_num = idcode[7:10]
    chk_num = idcode[10]

    if gender_num == '1':
        cent_id = '18'
        gend_id = 'Male'
    elif gender_num == '2':
        cent_id = '18'
        gend_id = 'Female'
    elif gender_num == '3':
        cent_id = '19'
        gend_id = 'Male'
    elif gender_num == '4':
        cent_id = '19'
        gend_id = 'Female'
    elif gender_num == '5':
        cent_id = '20'
        gend_id = 'Male'
    elif gender_num == '6':
        cent_id = '20'
        gend_id = 'Female'

    if 0 <= int(region_num) <= 10:
        region_id = 'Kuressaare haigla'
    elif 11 <= int(region_num) <= 19:
        region_id = 'Tartu Ülikooli Naistekliinik'
    elif 21 <= int(region_num) <= 150:
        region_id = 'Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja Tallinn'
    elif 151 <= int(region_num) <= 160:
        region_id = 'Keila haigla'
    elif 161 <= int(region_num) <= 220:
        region_id = 'Rapla haigla, Loksa haigla, Hiiumaa haigla Kärdla'
    elif 221 <= int(region_num) <= 270:
        region_id = 'Ida-Viru keskhaigla (Kohtla-Järve, endine Jõhvi)'
    elif 271 <= int(region_num) <= 370:
        region_id = 'Maarjamõisa kliinikum (Tartu), Jõgeva haigla'
    elif 371 <= int(region_num) <= 420:
        region_id = 'Narva haigla'
    elif 421 <= int(region_num) <= 470:
        region_id = 'Pärnu haigla'
    elif 471 <= int(region_num) <= 490:
        region_id = 'Haapsalu haigla'
    elif 491 <= int(region_num) <= 520:
        region_id = 'Järvamaa haigla (Paide)'
    elif 521 <= int(region_num) <= 570:
        region_id = 'Rakvere haigla, Tapa haigla'
    elif 571 <= int(region_num) <= 600:
        region_id = 'Valga haigla'
    elif 601 <= int(region_num) <= 650:
        region_id = 'Viljandi haigla'
    elif 651 <= int(region_num) <= 700:
        region_id = 'Lõuna-Eesti haigla (Võru), Põlva haigla'

    # print(gender_num, by_num, bm_num, bd_num, region_num, chk_num)

    print(idcode)
    print('You are ' + gend_id)
    print('You were born in ' + bd_num + '.' + bm_num + '.' + cent_id + by_num)
    print('Your place of birth: ' + region_id)
    print('Please insert number in step 2 to check you ID: ' + chk_num)


def check_if_ID_is_valid(user_id):
    id_num = '37910143715'
    summ_id_num1 = 1 * int(id_num[0]) + 2 * int(id_num[1]) + 3 * int(id_num[2]) + 4 * int(id_num[3]) + 5 * \
                int(id_num[4]) + 6 * int(id_num[5]) + 7 * int(id_num[6]) + 8 * int(id_num[7]) + 9 * \
                int(id_num[8]) + 1 * int(id_num[9])
    rem_div_1 = summ_id_num1 % 11
    val_1 = summ_id_num1 - 11 * (summ_id_num1 // 11)

    summ_id_num2 = 3 * int(id_num[0]) + 4 * int(id_num[1]) + 5 * int(id_num[2]) + 6 * int(id_num[3]) + 7 * \
                int(id_num[4]) + 8 * int(id_num[5]) + 9 * int(id_num[6]) + 1 * int(id_num[7]) + 2 * \
                int(id_num[8]) + 3 * int(id_num[9])
    rem_div_2 = summ_id_num2 % 11
    val_2 = summ_id_num2 - 11 * (summ_id_num2 // 11)


    if rem_div_1 < 10 and rem_div_1 == int(id_num[10]) and val_1 == rem_div_1:
        print('The code is valid!')
    elif rem_div_2 == int(id_num[10]) and val_2 == rem_div_2 or rem_div_2 == 0:
        print('The code is invalid!')
    else:
        print('The code did not pass validation!')

user_menu()




