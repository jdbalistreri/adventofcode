if __name__ == "__main__":
    import sys
    import importlib

    requested_module = sys.argv[1]
    print(f'running module for {requested_module}\n')

    print("results are:")
    module = importlib.import_module(requested_module)
    module.main()
