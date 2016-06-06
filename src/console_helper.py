def handle_user_input(caption, handlers_map):
    while True:
        print(caption)
        input_str = input()
        if input_str in handlers_map:
            print()
            handler = handlers_map[input_str]

            if callable(handler):
                return handler()

            return handler

        print('Unrecognized input, please try again\n')
