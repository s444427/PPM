



if __name__ == '__main__':

    base = 'this-is-the-tithe'
    to_code = base

    c_neg = []

    for i in base:
        if i not in c_neg:
            c_neg.append(i)

    print(c_neg, '\n')

    c_0 = {}
    c_1 = {}
    c_2 = {}

    prev1 = ''
    prev2 = ''

    for sign in to_code:
        len_2 = prev2+prev1
        if len_2 in c_2:
            if sign in c_2[len_2]:
                c_2[len_2][sign] += 1
                print(c_2[len_2][sign])
            else:
                c_2[len_2][sign] = 1
        else:
            print('esc')
            len_1 = prev1
            if len_1 in c_1:
                if sign in c_1[len_1]:
                    c_1[len_1][sign] += 1
                    c_2[len_2][sign] = 1
                else:
                    c_1[len_1][sign] = 1
            else:
                print('esc')
                if sign in c_0:
                    c_0[sign] += 1
                    c_1[len_1] = {}
                    c_1[len_1][sign] = 1
                else:
                    c_0[sign] = 1
        prev2 = prev1
        prev1 = sign

        print(c_0)
        print(c_1)
        print(c_2)
