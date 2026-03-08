while True:
    try:
        a, b = input('Enter 2 numbers: ').split()
        a, b = int(a),int(b)
        print(a,'/',b,'=',a/b)
        
    except ValueError:
        print("Numbers are not valid")

    except ZeroDivisionError:
        print('you can not divide anynumber to zero')

    