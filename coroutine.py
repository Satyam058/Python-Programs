def print_n(prefix):
    print("Searching prefix:{}".format(prefix))
    try : 
        while True:
                name = (yield)
                if prefix in name:
                    print(name)
    except GeneratorExit:
            print("Closing coroutine!!")
 
corou = print_("Satyam")
corou.__next__()
corou.send("Burman")
corou.send("Satyam Burman")
corou.close(
