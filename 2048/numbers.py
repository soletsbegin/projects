from termcolor import *

numbers = {0: ['\x1b[0;33;47m      \x1b[0m',
               '\x1b[0;33;47m      \x1b[0m',
               '\x1b[0;33;47m      \x1b[0m'],

           2: ['\x1b[0;33;43m      \x1b[0m',
               '\x1b[1;30;43m   2  \x1b[0m',
               '\x1b[0;33;43m      \x1b[0m'],

           4: ['\x1b[0;33;43m      \x1b[0m',
               '\x1b[1;30;43m   4  \x1b[0m',
               '\x1b[0;33;43m      \x1b[0m'],

           8: ['\x1b[0;33;42m      \x1b[0m',
               '\x1b[1;30;42m   8  \x1b[0m',
               '\x1b[0;33;42m      \x1b[0m'],

           16: ['\x1b[0;33;42m      \x1b[0m',
                '\x1b[1;30;42m  16  \x1b[0m',
                '\x1b[0;33;42m      \x1b[0m'],

           32: ['\x1b[0;33;42m      \x1b[0m',
                '\x1b[1;30;42m  32  \x1b[0m',
                '\x1b[0;33;42m      \x1b[0m'],

           64: ['\x1b[0;33;46m      \x1b[0m',
                '\x1b[1;30;46m  64  \x1b[0m',
                '\x1b[0;33;46m      \x1b[0m'],

           128: ['\x1b[0;33;46m      \x1b[0m',
                 '\x1b[1;30;46m 128  \x1b[0m',
                 '\x1b[0;33;46m      \x1b[0m'],

           256: ['\x1b[0;33;46m      \x1b[0m',
                 '\x1b[1;30;46m 256  \x1b[0m',
                 '\x1b[0;33;46m      \x1b[0m'],

           512: ['\x1b[0;33;45m      \x1b[0m',
                 '\x1b[1;30;45m 512  \x1b[0m',
                 '\x1b[0;33;45m      \x1b[0m'],

           1024: ['\x1b[0;33;41m      \x1b[0m',
                  '\x1b[1;30;41m 1024 \x1b[0m',
                  '\x1b[0;33;41m      \x1b[0m'],

           2048: ['\x1b[0;33;41m      \x1b[0m',
                  '\x1b[1;30;41m 2048 \x1b[0m',
                  '\x1b[0;33;41m      \x1b[0m'],
           }


colored_numbers = {0: [colored('      ', 'white', attrs=['reverse', 'bold']),
                       colored('      ', 'white', attrs=['reverse', 'bold']),
                       colored('      ', 'white', attrs=['reverse', 'bold'])],

                   2: [colored('      ', 'yellow', attrs=['reverse', 'bold']),
                        colored('  2   ', 'yellow', attrs=['reverse', 'bold']),
                        colored('      ', 'yellow', attrs=['reverse', 'bold'])],

                   4: [colored('      ', 'yellow', attrs=['reverse', 'bold']),
                        colored('  4   ', 'yellow', attrs=['reverse', 'bold']),
                        colored('      ', 'yellow', attrs=['reverse', 'bold'])],

                   8: [colored('      ', 'green', attrs=['reverse', 'bold']),
                       colored('  8   ', 'green', attrs=['reverse', 'bold']),
                       colored('      ', 'green', attrs=['reverse', 'bold'])],

                   16: [colored('      ', 'green', attrs=['reverse', 'bold']),
                        colored('  16  ', 'green', attrs=['reverse', 'bold']),
                        colored('      ', 'green', attrs=['reverse', 'bold'])],

                   32: [colored('      ', 'green', attrs=['reverse', 'bold']),
                        colored('  32  ', 'green', attrs=['reverse', 'bold']),
                        colored('      ', 'green', attrs=['reverse', 'bold'])],

                   64: [colored('      ', 'blue', attrs=['reverse', 'bold']),
                        colored('  64  ', 'blue', attrs=['reverse', 'bold']),
                        colored('      ', 'blue', attrs=['reverse', 'bold'])],

                   128: [colored('      ', 'blue', attrs=['reverse', 'bold']),
                         colored(' 128  ', 'blue', attrs=['reverse', 'bold']),
                         colored('      ', 'blue', attrs=['reverse', 'bold'])],

                   256: [colored('      ', 'blue', attrs=['reverse', 'bold']),
                         colored(' 256  ', 'blue', attrs=['reverse', 'bold']),
                         colored('      ', 'blue', attrs=['reverse', 'bold'])],

                   512: [colored('      ', 'red', attrs=['reverse', 'bold']),
                        colored(' 512  ', 'red', attrs=['reverse', 'bold']),
                        colored('      ', 'red', attrs=['reverse', 'bold'])],

                   1024: [colored('      ', 'red', attrs=['reverse', 'bold']),
                         colored(' 1024 ', 'red', attrs=['reverse', 'bold']),
                         colored('      ', 'red', attrs=['reverse', 'bold'])],

                   2048: [colored('      ', 'red', attrs=['reverse', 'bold']),
                         colored(' 2048 ', 'red', attrs=['reverse', 'bold']),
                         colored('      ', 'red', attrs=['reverse', 'bold'])]
                   }
if __name__ == '__main__':
    example = {16: [colored('      ', 'green', attrs=['reverse', 'bold']),
                    colored('  16  ', 'green', attrs=['reverse', 'bold']),
                    colored('      ', 'green', attrs=['reverse', 'bold'])]}
    for i in [0,1,2]:
        print(example[16][i])


